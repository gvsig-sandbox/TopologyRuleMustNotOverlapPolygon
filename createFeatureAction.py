# encoding: utf-8

import gvsig
from org.gvsig.topology.lib.spi import AbstractTopologyRuleAction

#from addons.TopologyRuleMustNotOverlapPolygon.mustNotOverlapPolygonFactory import MustNotOverlapPolygonRuleFactory
#from mustNotOverlapPolygonFactory import MustNotOverlapPolygonRuleFactory
from org.gvsig.topology.lib.api import ExecuteTopologyRuleActionException

#from mustNotOverlapPolygonFactory import MustNotOverlapPolygonRuleFactory

class CreateFeatureAction(AbstractTopologyRuleAction):

  def __init__(self):
    AbstractTopologyRuleAction.__init__(
      self,
      "MustNotOverlapPolygon", #MustNotOverlapPolygonRuleFactory.NAME,
      "CreateFeature",
      "Create Feature",
      "The Create Feature fix creates a new polygon feature out "
      + "of the error shape and removes the portion of "
      + "overlap from each of the features, causing the "
      + "error to create a planar representation of the "
      + "feature geometry. This fix can be applied to "
      + "one or more selected Must Not Overlap errors."
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

    c = CreateFeatureAction()
    pass
