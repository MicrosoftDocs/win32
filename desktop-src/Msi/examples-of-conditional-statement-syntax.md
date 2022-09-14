---
description: The following provides some common instances of conditional statements. For more information, see Conditional Statement Syntax.
ms.assetid: 8b6bae7a-20ae-494c-bd96-66bd537c8630
title: Examples of Conditional Statement Syntax
ms.topic: article
ms.date: 05/31/2018
---

# Examples of Conditional Statement Syntax

The following provides some common instances of conditional statements. For more information, see [Conditional Statement Syntax](conditional-statement-syntax.md).

## Run action on removal.

For information, see [Conditioning Actions to Run During Removal](conditioning-actions-to-run-during-removal.md).

## Run action only if the product has not been installed.

``` syntax
NOT Installed
```

## Run action only if the product will be installed local. Do not run action on a reinstallation.

``` syntax
(&FeatureName=3) AND NOT(!FeatureName=3)
```

The term "&FeatureName=3" means the action is to install the feature local. The term "NOT(!FeatureName=3)" means the feature is not installed local.

## Run action only if the feature will be uninstalled.

``` syntax
(&FeatureName=2) AND (!FeatureName=3)
```

This condition only checks for a transition of the feature from an installed state of local to the absent state.

## Run action only if the component was installed local, but is transitioning out of state.

``` syntax
(?ComponentName=3) AND ($ComponentName=2 OR $ComponentName=4)
```

The term "?ComponetName=3" means the component is installed local. The term "$ComponentName=2" means that the action state on the component is Absent. The term "$ComponentName=4" means that the action state on the component is run from source. Note that an action state of advertise is not valid for a component.

## Run action only on the reinstallation of a component.

``` syntax
?ComponentName=$ComponentName
```

## Run action only when a particular patch is applied.

``` syntax
PATCH AND PATCH >< MEDIASRCPROPNAME
```

For more information, see the Remarks section on the [**PATCH**](patch.md) property page.

 

 



