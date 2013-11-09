import boto
from model import *
from config import engine
from sqlalchemy.orm import sessionmaker


def create_cluster(name_cluster, name_key, zone):
    """
    :name_cluster: Name new cluster
    :name_key: Name connection strint to aws in table connection
    :awsAccessKeyId: Access key id for access to aws
    :awsSecretKeyId: Secret key id for access to aws
    """
    session = sessionmaker(bind=engine)()
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
    session = sessionmaker(bind=engine)()
    try:
        session.add(ConnectionTable(name_key, awsAccessKeyId, awsSecretKeyId))
        session.commit()
    except:
        print "Error add connection to table!!!"
        session.rollback()
        raise





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
        session = sessionmaker(bind=engine)()
        __cluster_info=session.query(ClusterTable.connection, ClusterTable.zone).filter_by(name=self.cluster_name).all()[0]
        if __cluster_info[0]:

            ___connect=session.query(ConnectionTable.name, ConnectionTable.awsAccessKeyId, \
                                ConnectionTable.awsSecretKeyId).filter_by(name=__cluster_info[0]).all()
            if ___connect:
                self.connect =  ___connect[0]
        self.zone = __cluster_info[1]
        self.conn = boto.connect_ec2(self.connect[1], self.connect[2])

    def __repr__(self):
        return "<Cluster('%s','%s', '%s')>" % (self.cluster_name, self.connect, self.zone)

    def create_security_group(self, group_name):
        security_group = self.conn(group_name, "A group for %s"%(group_name,))










#create_connection('test', 'access', 'secret')
print create_cluster('testcluster1', 'test', 'zonetest')
print Cluster('testcluster')