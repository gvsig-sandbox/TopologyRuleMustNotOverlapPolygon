# encoding: utf-8

import gvsig
from org.gvsig.topology.lib.spi import AbstractTopologyRuleAction
from org.gvsig.topology.lib.api import ExecuteTopologyRuleActionException

#from mustNotOverlapPolygonFactory import MustNotOverlapPolygonRuleFactory

class MergeAction(AbstractTopologyRuleAction):
  def __init__(self):
    AbstractTopologyRuleAction.__init__(
      self,
      "MustNotOverlapPolygon", #MustNotOverlapPolygonRuleFactory.NAME,
      "Merge",
      "Merge",
      "The Merge fix adds the portion of overlap from one feature "
      + "and subtracts it from the others that are "
      + "violating the rule. You need to pick the feature "
      + "that receives the portion of overlap using the "
      + "Merge dialog box. This fix can be applied to one "
      + "Must Not Overlap error only."
    )

  def execute(rule, line, parameters):
   #TopologyRule rule, TopologyReportLine line, DynObject parameters) {
   try:
     #TODO
     pass
   except Exception as ex:
     #throw ExecuteTopologyRuleActionException(ex)
     raise ExecuteTopologyRuleActionException(ex)
       
    
def main(*args):

    #Remove this lines and add here your code

    print "hola mundo"
    pass
