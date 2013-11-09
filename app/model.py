__author__ = 'artem'
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref





Base = declarative_base()


class ConnectionTable(Base):
    """
    table connection contain connection to aws
    """
    __tablename__ = 'connection'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)
    awsAccessKeyId = Column(String)
    awsSecretKeyId = Column(String)
    cluster = relationship("ClusterTable")

    def __init__(self, name, awsAccessKeyId, awsSecretKeyId):
        self.name = name
        self.awsAccessKeyId = awsAccessKeyId
        self.awsSecretKeyId = awsSecretKeyId

    def __repr__(self):
        return "<Connection('%d', '%s', '%s')>" % (self.id, self.name, self.awsAccessKeyId, self.awsSecretKeyId)

class ClusterTable(Base):
    """
    Main table "cluster" contain field with configuration cluster
    """
    __tablename__ = 'cluster'
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True, unique=True)
    connection = Column(Integer, ForeignKey('connection.name'))
    zone = Column(String)

    def __init__(self, name, connection_id, zone):
        self.name = name
        self.connection = connection_id
        self.zone = zone

    def __repr__(self):
        return "<Cluster('%d', '%s', '%s', '%s')>" % (self.id, self.name, self.connection, self.zone)

class SecurityGroupTable(Base):
    """
    Main table "cluster" contain field with configuration cluster
    """
    __tablename__ = 'security_group'
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True, unique=True)
    description = Column(String, index=True, unique=True)


    def __init__(self, name, description):
        self.name = name
        self.description = description


    def __repr__(self):
        return "<Cluster('%d', '%s', '%s')>" % (self.id, self.name, self.description)

