# scriptSpeedBoostFactorBonusBonus
#
# Used by:
# Charges from group: Warp Disruption Script (2 of 2)
type = "passive"
runTime = "early"


def handler(fit, module, context):
    module.boostItemAttr("speedBoostFactorBonus", module.getModifiedChargeAttr("speedBoostFactorBonusBonus"))
