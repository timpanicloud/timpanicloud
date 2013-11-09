import sys
sys.path.append("../..")

import boto
from model import ClusterTable, ConnectionTable
from database import session




def create_cluster(name_cluster, name_key, zone):
    """
    :name_cluster: Name new cluster
    :name_key: Name connection strint to aws in table connection
    :awsAccessKeyId: Access key id for access to aws
    :awsSecretKeyId: Secret key id for access to aws
    """

    try:
        session.add(ClusterTable(name_cluster, name_key, zone))
        session.commit()
    except:
        print "Error add cluster to table!!!"
        session.rollback()
        raise

    return Cluster(name_cluster)

def create_connection(name_key, awsAccessKeyId, awsSecretKeyId):
    """
    :name_cluster: Name new cluster
    :name_key: Name connection strint to aws in table connection
    :awsAccessKeyId: Access key id for access to aws
    :awsSecretKeyId: Secret key id for access to aws
    """
    try:
        session.add(ConnectionTable(name_key, awsAccessKeyId, awsSecretKeyId))
        session.commit()
    except:
        print "Error add connection to table!!!"
        session.rollback()
        raise
    return Connection(name_key)




class Cluster(object):
    """
    Class Cluster is AWS Cluster

    :name: Name of the cluster
    :connect: Connection string to AWS
    :zone: Zone AWS for server of the cluster
    """


    def __init__(self, cluster_name):

        self.cluster_name = cluster_name

        # get connection string to aws
        __cluster_info=session.query(ClusterTable.connection, ClusterTable.zone).filter_by(name=self.cluster_name).all()
        if not __cluster_info:
            return None


        try:
            self.connect = __cluster_info[0][0]
        except:
            self.connect = None
        try:
            self.zone = __cluster_info[0][1]
        except:
            self.zone = None


    def __repr__(self):
        return "<Cluster('%s','%s', '%s')>" % (self.cluster_name, self.connect, self.zone)

    def create_security_group(self, group_name):
        security_group = self.conn(group_name, "A group for %s"%(group_name,))




class Connection(object):
    """
    Class Connection is AWS Cluster

    :key_name: Name connection strint to aws in table connection
    :awsAccessKeyId: Access key id for access to aws
    :awsSecretKeyId: Secret key id for access to aws
    """
    def __init__(self, name):

        self.name = name

        # get connection string to aws
        ___connect=session.query(ConnectionTable.awsAccessKeyId, \
                                ConnectionTable.awsSecretKeyId).filter_by(name=self.name).all()
        try:
            self.awsAccessKeyId = ___connect[0][0]
            self.awsSecretKeyId = ___connect[0][1]
        except:
            self.awsAccessKeyId = None
            self.awsSecretKeyId = None

    def __repr__(self):
        return "<Cluster('%s','%s', '%s')>" % (self.name, self.awsAccessKeyId, self.awsSecretKeyId)


