# encoding: utf-8

import gvsig

"""
package org.gvsig.topology.rule;

import org.gvsig.expressionevaluator.Expression;
import org.gvsig.expressionevaluator.ExpressionBuilder;
import org.gvsig.expressionevaluator.ExpressionEvaluatorLocator;
import org.gvsig.expressionevaluator.ExpressionEvaluatorManager;
import org.gvsig.fmap.dal.feature.Feature;
import org.gvsig.fmap.dal.feature.FeatureReference;
import org.gvsig.fmap.geom.Geometry;
import org.gvsig.tools.dynobject.DynObject;
import org.gvsig.tools.task.SimpleTaskStatus;
import org.gvsig.topology.lib.spi.AbstractTopologyRule;
import org.gvsig.topology.lib.spi.AbstractTopologyRuleAction;
import org.gvsig.topology.lib.api.ExecuteTopologyRuleActionException;
import org.gvsig.topology.lib.api.TopologyDataSet;
import org.gvsig.topology.lib.api.TopologyPlan;
import org.gvsig.topology.lib.api.TopologyReport;
import org.gvsig.topology.lib.api.TopologyReportLine;
import org.gvsig.topology.lib.api.TopologyRule;
import org.gvsig.topology.lib.api.TopologyRuleFactory;

/**
 *
 * @author jjdelcerro
 */
@SuppressWarnings("UseSpecificCatch")
public class MustNotOverlapPolygonRule extends AbstractTopologyRule {

    private class CreateFetureAction extends AbstractTopologyRuleAction {

        public CreateFetureAction() {
            super(
                    MustNotOverlapPolygonRuleFactory.NAME,
                    "CreateFeature",
                    "Create Feature",
                    "The Create Feature fix creates a new polygon feature out "
                    + "of the error shape and removes the portion of "
                    + "overlap from each of the features, causing the "
                    + "error to create a planar representation of the "
                    + "feature geometry. This fix can be applied to "
                    + "one or more selected Must Not Overlap errors."
            );
        }

        @Override
        public void execute(TopologyRule rule, TopologyReportLine line, DynObject parameters) {
            try {
                // TODO
            } catch (Exception ex) {
                throw new ExecuteTopologyRuleActionException(ex);
            }
        }

    }

    private class SubtractAction extends AbstractTopologyRuleAction {

        public SubtractAction() {
            super(
                    MustNotOverlapPolygonRuleFactory.NAME,
                    "Subtract",
                    "Subtract",
                    "The Subtract fix removes the overlapping portion of "
                    + "geometry from each feature that is causing the "
                    + "error and leaves a gap or void in its place. "
                    + "This fix can be applied to one or more selected "
                    + "Must Not Overlap errors."
            );
        }

        @Override
        public void execute(TopologyRule rule, TopologyReportLine line, DynObject parameters) {
            try {
                // TODO
            } catch (Exception ex) {
                throw new ExecuteTopologyRuleActionException(ex);
            }
        }

    }

    private class MergeAction extends AbstractTopologyRuleAction {

        public MergeAction() {
            super(
                    MustNotOverlapPolygonRuleFactory.NAME,
                    "Merge",
                    "Merge",
                    "The Merge fix adds the portion of overlap from one feature "
                    + "and subtracts it from the others that are "
                    + "violating the rule. You need to pick the feature "
                    + "that receives the portion of overlap using the "
                    + "Merge dialog box. This fix can be applied to one "
                    + "Must Not Overlap error only."
            );
        }

        @Override
        public void execute(TopologyRule rule, TopologyReportLine line, DynObject parameters) {
            try {
                // TODO
            } catch (Exception ex) {
                throw new ExecuteTopologyRuleActionException(ex);
            }
        }
    }

    private String geomName;
    private Expression expression = null;
    private ExpressionBuilder expressionBuilder = null;

    public MustNotOverlapPolygonRule(
            TopologyPlan plan,
            TopologyRuleFactory factory,
            double tolerance,
            String dataSet1
    ) {
        super(plan, factory, tolerance, dataSet1);
        this.addAction(new CreateFetureAction());
        this.addAction(new MergeAction());
        this.addAction(new SubtractAction());
    }

    @Override
    protected void check(SimpleTaskStatus taskStatus, TopologyReport report, Feature feature1) throws Exception {
        try {
            if (this.expression == null) {
                ExpressionEvaluatorManager manager = ExpressionEvaluatorLocator.getManager();
                this.expression = manager.createExpression();
                this.expressionBuilder = manager.createExpressionBuilder();
                this.geomName = feature1.getType().getDefaultGeometryAttributeName();
            }
            Geometry polygon = feature1.getDefaultGeometry();
            if( polygon==null ) {
                return;
            }
            TopologyDataSet theDataSet = this.getDataSet1();
            if (theDataSet.getSpatialIndex() != null) {
                for (FeatureReference reference : theDataSet.query(polygon)) {
                    if (reference.equals(feature1.getReference())) {
                        continue;
                    }
                    Feature feature = reference.getFeature();
                    Geometry otherPolygon = feature.getDefaultGeometry();
                    if (otherPolygon!=null && polygon.overlaps(otherPolygon)) {;
                        Geometry error = polygon.intersection(otherPolygon);
                        report.addLine(this,
                                theDataSet,
                                null,
                                polygon,
                                error,
                                feature1.getReference(),
                                null,
                                false,
                                "The polygon overlay with others."
                        );
                        break;
                    }
                }
            } else {
                this.expression.setPhrase(
                        this.expressionBuilder.ifnull(
                                this.expressionBuilder.column(this.geomName),
                                this.expressionBuilder.constant(false),
                                this.expressionBuilder.ST_Overlaps(
                                        this.expressionBuilder.column(this.geomName),
                                        this.expressionBuilder.geometry(polygon)
                                )
                        ).toString()
                );
                Feature feature = theDataSet.findFirst(this.expression);
                if ( feature != null) {
                    Geometry otherPolygon = feature.getDefaultGeometry();
                    Geometry error = null;
                    if( otherPolygon!=null ) {
                        error = polygon.difference(otherPolygon);
                    }
                    report.addLine(this,
                            theDataSet,
                            null,
                            polygon,
                            error,
                            feature1.getReference(),
                            null,
                            false,
                            "The polygon overlay with others."
                    );
                }
            }
        } catch (Exception ex) {
            LOGGER.warn("Can't check feature.", ex);
        } finally {
        }
    }

}

"""
def main(*args):

    #Remove this lines and add here your code

    print "hola mundo"
    pass
