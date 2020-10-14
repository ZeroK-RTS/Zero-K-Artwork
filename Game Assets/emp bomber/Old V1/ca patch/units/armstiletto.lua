unitDef = {
  unitname            = "armstiletto",
  name                = "Stiletto",
  description         = "EMP Bomber",
  amphibious          = true,
  buildCostEnergy     = 600,
  buildCostMetal      = 600,
  buildPic            = "CORGRIPN.png",
  buildTime           = 600,
  canAttack           = true,
  canDropFlare        = false,
  canFly              = true,
  canGuard            = true,
  canMove             = true,
  canPatrol           = true,
  canstop             = "1",
  canSubmerge         = false,
  category            = "MOBILE VTOL",
  collide             = false,
  corpse              = "HEAP",
  cruiseAlt           = 250,

  customParams        = {
    helptext = "Sleek, fast and able to take a beating, the Stiletto drops EMP bombs that can paralyze an entire column of tanks in a single pass, rendering them helpless before allied forces.",
  },

  defaultmissiontype  = "VTOL_standby",
  explodeAs           = "GUNSHIPEX",
  fireState           = 1,
  floater             = true,
  footprintX          = 3,
  footprintZ          = 3,
  iconType            = "bomberriot",
  idleAutoHeal        = 5,
  idleTime            = 1800,
  immunetoparalyzer   = "1",
  maneuverleashlength = "1380",
  mass                = 300,
  maxAcc              = 0.5,
  maxDamage           = 1130,
  maxFuel             = 1000,
  maxVelocity         = 12,
  minCloakDistance    = 75,
  noAutoFire          = false,
  noChaseCategory     = "VTOL SINK FLOAT HOVER",
  objectName          = "armstiletto.s3o",
  seismicSignature    = 0,
  selfDestructAs      = "GUNSHIPEX",
  side                = "ARM",
  sightDistance       = 660,
  smoothAnim          = true,

  sounds              = {
    canceldestruct = "cancel2",

    cant           = {
      "cantdo4",
    },


    count          = {
      "count6",
      "count5",
      "count4",
      "count3",
      "count2",
      "count1",
    },


    ok             = {
      "vtolcrmv",
    },


    select         = {
      "vtolcrac",
    },

    underattack    = "warning1",
  },

  stealth             = true,
  steeringmode        = "1",
  TEDClass            = "VTOL",
  turnRate            = 396,

  weapons             = {

    {
      def                = "CORGRIPN_BOMB",
      badTargetCategory  = "MOBILE",
      fuelUsage          = 999,
      onlyTargetCategory = "SINK HOVER FLOAT",
    },

  },


  weaponDefs          = {

    CORGRIPN_BOMB = {
      name                    = "EMPbomb",
      areaOfEffect            = 240,
      avoidFeature            = false,
      avoidFriendly           = false,
      collideFriendly         = false,
      commandfire             = true,
      craterBoost             = 0,
      craterMult              = 0,

      damage                  = {
        default        = 1500,
        commanders     = 150,
        empresistant75 = 375,
        empresistant99 = 15,
        planes         = 15,
      },

      dropped                 = true,
      edgeEffectiveness       = 0.4,
      explosionGenerator      = "custom:ELECTRIC_EXPLOSION",
      fireStarter             = 0,
      impulseBoost            = 0,
      impulseFactor           = 0,
      interceptedByShieldType = 0,
      model                   = "bomb",
      myGravity               = 0.8,
      noSelfDamage            = true,
      paralyzer               = true,
      paralyzeTime            = 15,
      range                   = 800,
      reloadtime              = 0.3,
      renderType              = 6,
      soundHit                = "EMGPULS1",
      soundStart              = "bombrel",
      tolerance               = 7000,
      weaponType              = "AircraftBomb",
    },

  },


  featureDefs         = {

    DEAD  = {
      description      = "Wreckage - Stiletto",
      blocking         = true,
      category         = "corpses",
      damage           = 2260,
      energy           = 0,
      featureDead      = "DEAD2",
      featurereclamate = "SMUDGE01",
      footprintX       = 2,
      footprintZ       = 2,
      height           = "40",
      hitdensity       = "100",
      metal            = 360,
      object           = "ARMHAM_DEAD",
      reclaimable      = true,
      reclaimTime      = 1440,
      seqnamereclamate = "TREE1RECLAMATE",
      world            = "All Worlds",
    },


    DEAD2 = {
      description      = "Debris - Hammer",
      blocking         = false,
      category         = "heaps",
      damage           = 2260,
      energy           = 0,
      featureDead      = "HEAP",
      featurereclamate = "SMUDGE01",
      footprintX       = 2,
      footprintZ       = 2,
      height           = "4",
      hitdensity       = "100",
      metal            = 360,
      object           = "2X2E",
      reclaimable      = true,
      reclaimTime      = 1440,
      seqnamereclamate = "TREE1RECLAMATE",
      world            = "All Worlds",
    },


    HEAP  = {
      description      = "Debris - Stiletto",
      blocking         = false,
      category         = "heaps",
      damage           = 2260,
      energy           = 0,
      featurereclamate = "SMUDGE01",
      footprintX       = 2,
      footprintZ       = 2,
      height           = "4",
      hitdensity       = "100",
      metal            = 180,
      object           = "2X2E",
      reclaimable      = true,
      reclaimTime      = 720,
      seqnamereclamate = "TREE1RECLAMATE",
      world            = "All Worlds",
    },

  },

}

return lowerkeys({ armstiletto = unitDef })
