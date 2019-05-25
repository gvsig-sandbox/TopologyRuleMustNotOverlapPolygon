# encoding: utf-8

import gvsig

from org.gvsig.topology.lib.spi import AbstractTopologyRuleAction
from org.gvsig.topology.lib.api import ExecuteTopologyRuleActionException

#from mustNotOverlapPolygonFactory import MustNotOverlapPolygonRuleFactory

class SubtractAction(AbstractTopologyRuleAction):
  def __init__(self):
    AbstractTopologyRuleAction.__init__(
      self,
      "MustNotOverlapPolygon", #MustNotOverlapPolygonRuleFactory.NAME,
      "Subtract",
      "Subtract",
      "The Subtract fix removes the overlapping portion of "
      + "geometry from each feature that is causing the "
      + "error and leaves a gap or void in its place. "
      + "This fix can be applied to one or more selected "
      + "Must Not Overlap errors."
    )

  def execute(rule, line, parameters):
     #TopologyRule rule, TopologyReportLine line, DynObject parameters) {
     try:
       #TODO
       pass
     except Exception as ex:
       #throw new ExecuteTopologyRuleActionException(ex);
       raise ExecuteTopologyRuleActionException(ex)

def main(*args):

    #Remove this lines and add here your code

    print "hola mundo"
    pass
