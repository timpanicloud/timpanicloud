__author__ = 'artem'
import random
import unittest
import sys, os
sys.path.append("../..")
from config import Base, db_path, engine
from app.database import session
from app.Cluster import create_cluster, create_connection, Cluster, Connection
from app.model import ConnectionTable, ClusterTable


class TestConnectionFunctions(unittest.TestCase):

    def setUp(self):
        try:
            os.remove(db_path)
        except:
            pass
        Base.metadata.create_all(engine)
        self.nameCluster = 'testCluster'
        self.nameConnection = 'testConnection'
        self.nameZone = 'testZone'
        self.nameAccessKeyId = 'testAccessKeyId'
        self.nameSecretKeyId = 'testSecretKeyId'

        self.nameCluster1 = 'testCluster1'
        self.nameConnection_no_exist = 'testConnection_no_exist'
        self.nameZone1 = 'testZone1'


    def test_db_model(self):
        """
        make sure workable of create_connection and create_cluster
        and that all elements of Classes Cluster and Connection was added to database
        """

        create_connection(self.nameConnection, self.nameAccessKeyId, self.nameSecretKeyId)
        create_cluster(self.nameCluster, self.nameConnection, self.nameZone)
        clusterInstance =  Cluster(self.nameCluster)


        self.assertEqual([clusterInstance.cluster_name, clusterInstance.connect, clusterInstance.zone],\
                         [self.nameCluster, self.nameConnection, self.nameZone])

        clusterInstance1=create_cluster(self.nameCluster1, self.nameConnection_no_exist, self.nameZone1)



        connectionInstance = Connection(self.nameConnection)

        self.assertEqual([self.nameConnection, self.nameAccessKeyId, self.nameSecretKeyId],\
                         [connectionInstance.name, connectionInstance.awsAccessKeyId, connectionInstance.awsSecretKeyId])
        print Connection(self.nameConnection_no_exist)




