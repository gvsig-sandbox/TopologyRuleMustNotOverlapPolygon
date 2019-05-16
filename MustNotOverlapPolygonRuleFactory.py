# encoding: utf-8

import gvsig

"""
package org.gvsig.topology.rule;

import org.gvsig.fmap.geom.Geometry;
import org.gvsig.tools.util.ListBuilder;
import org.gvsig.topology.lib.spi.AbstractTopologyRuleFactory;
import org.gvsig.topology.lib.api.TopologyPlan;
import org.gvsig.topology.lib.api.TopologyRule;

/**
 *
 * @author jjdelcerro
 */
public class MustNotOverlapPolygonRuleFactory extends AbstractTopologyRuleFactory {

    public static final String NAME = "MustNotOverlapPolygon";
    
    public MustNotOverlapPolygonRuleFactory() {
        super(
                NAME, 
                "Must Not Overlap", 
                "Requires that the interior of polygons in the dataset not overlap. The polygons can share edges or vertices. This rule is used when an area cannot belong to two or more polygons. It is useful for modeling administrative boundaries, such as ZIP Codes or voting districts, and mutually exclusive area classifications, such as land cover or landform type.", 
                new ListBuilder<Integer>()
                        .add(Geometry.TYPES.SURFACE)
                        .add(Geometry.TYPES.MULTISURFACE)
                        .asList()
                
        );
    }
    
    @Override
    public TopologyRule createRule(TopologyPlan plan, String dataSet1, String dataSet2, double tolerance) {
        TopologyRule rule = new MustNotOverlapPolygonRule(plan, this, tolerance, dataSet1);
        return rule;
    }    

}

"""

from org.gvsig.topology.lib.spi import AbstractTopologyRuleFactory
from org.gvsig.topology.lib.api import TopologyLocator


class MustNotOverlapPolygonRuleFactory(AbstractTopologyRuleFactory):
  pass



def selfRegister():
  manager = TopologyLocator.getTopologyManager()
  manager.addRuleFactories(MustNotOverlapPolygonRuleFactory())


def main(*args):
  selfRegister()
