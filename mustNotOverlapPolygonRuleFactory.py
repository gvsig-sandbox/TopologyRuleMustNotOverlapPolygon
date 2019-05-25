# encoding: utf-8

import gvsig
from gvsig import uselib
uselib.use_plugin("org.gvsig.topology.app.mainplugin")

from org.gvsig.fmap.geom import Geometry
from org.gvsig.tools.util import ListBuilder
from org.gvsig.topology.lib.api import TopologyLocator
from org.gvsig.topology.lib.api import TopologyManager
from org.gvsig.topology.lib.spi import AbstractTopologyRuleFactory
from org.gvsig.topology.lib.api import TopologyPlan
from org.gvsig.topology.lib.api import TopologyRule

from gvsig import logger
from gvsig import LOGGER_WARN,LOGGER_INFO,LOGGER_ERROR

from mustNotOverlapPolygonRule import MustNotOverlapPolygonRule
from org.gvsig.topology.lib.api import TopologyLocator


class MustNotOverlapPolygonRuleFactory(AbstractTopologyRuleFactory):
  #NAME = "MustNotOverlapPolygon"
    
  def __init__(self):
    AbstractTopologyRuleFactory.__init__(
      self,
      "MustNotOverlapPolygon2",
      "Must Not Overlap2", 
      "Requires that the interior of polygons in the dataset not overlap. The polygons can share edges or vertices. This rule is used when an area cannot belong to two or more polygons. It is useful for modeling administrative boundaries, such as ZIP Codes or voting districts, and mutually exclusive area classifications, such as land cover or landform type.", 
      ListBuilder().add(Geometry.TYPES.SURFACE).add(Geometry.TYPES.MULTISURFACE).asList()
      )
  def createRule(self, plan, dataSet1, dataSet2, tolerance):
    #TopologyPlan plan, String dataSet1, String dataSet2, double tolerance
    rule = MustNotOverlapPolygonRule(plan, self, tolerance, dataSet1)
    return rule

def selfRegister():
    try:
      manager = TopologyLocator.getTopologyManager()
      manager.addRuleFactories(MustNotOverlapPolygonRuleFactory())
    except Exception as ex:
      logger("Can't register topology rule from MustNotOverlapPolygonRuleFactory."+str(ex), LOGGER_WARN)

def main(*args):
  print "* Executing MustNotOverlapPolygonFactory main."
  selfRegister()
  pass
