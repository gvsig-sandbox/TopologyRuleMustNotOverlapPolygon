from gvsig import uselib

uselib.use_plugin("org.gvsig.topology.app.mainplugin")
from createFeatureAction import CreateFeatureAction
from mergeAction import MergeAction
from subtractAction import SubtractAction
import sys

from org.gvsig.expressionevaluator import Expression
from org.gvsig.expressionevaluator import ExpressionBuilder
from org.gvsig.expressionevaluator import ExpressionEvaluatorLocator
from org.gvsig.expressionevaluator import ExpressionEvaluatorManager
from org.gvsig.fmap.dal.feature import Feature
from org.gvsig.fmap.dal.feature import FeatureReference
from org.gvsig.fmap.geom import Geometry
from org.gvsig.tools.dynobject import DynObject
from org.gvsig.tools.task import SimpleTaskStatus
from org.gvsig.topology.lib.spi import AbstractTopologyRule
from org.gvsig.topology.lib.spi import AbstractTopologyRuleAction
from org.gvsig.topology.lib.api import ExecuteTopologyRuleActionException
from org.gvsig.topology.lib.api import TopologyDataSet
from org.gvsig.topology.lib.api import TopologyPlan
from org.gvsig.topology.lib.api import TopologyReport
from org.gvsig.topology.lib.api import TopologyReportLine
from org.gvsig.topology.lib.api import TopologyRule
from org.gvsig.topology.lib.api import TopologyRuleFactory

from gvsig import logger
from gvsig import LOGGER_WARN,LOGGER_INFO,LOGGER_ERROR

from org.gvsig.topology.lib.api import TopologyLocator

class MustNotOverlapPolygonRule(AbstractTopologyRule):
  
  geomName = None
  expression = None
  expressionBuilder = None
  
  def __init__(self, plan, factory, tolerance, dataSet1):
    #        TopologyPlan plan,
    #        TopologyRuleFactory factory,
    #        double tolerance,
    #        String dataSet1
    
    AbstractTopologyRule.__init__(self, plan, factory, tolerance, dataSet1)
    #self.addAction(CreateFeatureAction())
    #self.addAction(MergeAction())
    #self.addAction(SubtractAction())
  
  def check(self, taskStatus, report, feature1):
    #SimpleTaskStatus taskStatus, 
    #TopologyReport report, 
    #Feature feature1
    
    try:
      logger("tak", LOGGER_INFO)
      if (self.expression == None):
        manager = ExpressionEvaluatorLocator.getManager()
        self.expression = manager.createExpression()
        self.expressionBuilder = manager.createExpressionBuilder()
        self.geomName = feature1.getType().getDefaultGeometryAttributeName()
      
      polygon = feature1.getDefaultGeometry()
      if( polygon==None ):
        return
      #logger("1", LOGGER_INFO)
      
      theDataSet = self.getDataSet1()
      #logger("2", LOGGER_INFO)
      if theDataSet.getSpatialIndex() != None:
        #logger("if", LOGGER_INFO)
        for reference in theDataSet.query(polygon):
            #FeatureReference reference
            # Misma feature
            #logger("ref"+str(reference), LOGGER_INFO)
            if (reference.equals(feature1.getReference())):
              continue;
            
            feature = reference.getFeature()
            otherPolygon = feature.getDefaultGeometry()
            if (otherPolygon!=None and polygon.overlaps(otherPolygon)):
              error = polygon.intersection(otherPolygon)
              report.addLine(self,
                theDataSet,
                None,
                polygon,
                error,
                feature1.getReference(),
                None,
                False,
                "The polygon overlay with others."
              )
              break
            
      else:
        logger("else", LOGGER_INFO)
        self.expression.setPhrase(
          self.expressionBuilder.ifnull(
            self.expressionBuilder.column(self.geomName),
            self.expressionBuilder.constant(False),
            self.expressionBuilder.ST_Overlaps(
              self.expressionBuilder.column(self.geomName),
              self.expressionBuilder.geometry(polygon)
            )
          ).toString()
        )
        feature = theDataSet.findFirst(self.expression)
        if feature != None:
            otherPolygon = feature.getDefaultGeometry()
            error = None
            if otherPolygon!=None :
              error = polygon.difference(otherPolygon)
            
            report.addLine(self,
              theDataSet,
              None,
              polygon,
              error,
              feature1.getReference(),
              None,
              False,
              "The polygon overlay with others."
            )
        logger("end", LOGGER_INFO)
    except: # Exception as ex:
      #logger("2 Can't check feature."+str(ex), LOGGER_WARN)
      ex = sys.exc_info()[1]
      logger("Can't execute rule. Class Name:" + ex.__class__.__name__ + " Except:" + str(ex))
    finally:
      pass
def main(*args):
  # testing class m = MustNotOverlapPolygonRule(None, None, 3, None)
  print "* Executing MustNotOverlapPolygon RULE main."
  tm = TopologyLocator.getTopologyManager()
  
  from mustNotOverlapPolygonRuleFactory import MustNotOverlapPolygonRuleFactory
  a = MustNotOverlapPolygonRuleFactory()
  tm.addRuleFactories(a)

