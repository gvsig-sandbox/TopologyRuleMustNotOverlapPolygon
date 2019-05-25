# encoding: utf-8

import gvsig
from org.gvsig.topology.lib.api import TopologyLocator
from mustNotOverlapPolygonFactory import MustNotOverlapPolygonRuleFactory

def main(*args):
  tm = TopologyLocator.getTopologyManager()
  a = MustNotOverlapPolygonRuleFactory()
  tm.addRuleFactories(a)