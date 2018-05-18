---
Description: 'There are several functions an application must call to request features.'
ms.assetid: '5253c6f0-316f-4f24-b0c0-951db8d16745'
title: Requesting a Feature
---

# Requesting a Feature

There are several functions an application must call to request features. Before requesting a feature, the application must ensure that the feature is installed. If the application calls [**MsiUseFeature**](msiusefeature.md) before the application accesses a feature, the application can use the information returned to maintain usage metrics.

**To request a feature**

1.  Call the [**MsiEnumFeatures**](msienumfeatures.md) or the [**MsiQueryFeatureState**](msiqueryfeaturestate.md) function if you want to determine the availability of a feature without incrementing the usage count.
2.  Indicate your application's intent to use a feature by calling the [**MsiUseFeature**](msiusefeature.md) function.
3.  Determine file locations by calling the [**MsiGetComponentPath**](msigetcomponentpath.md) function.
4.  Configure the feature by calling the [**MsiConfigureFeature**](msiconfigurefeature.md) function.
5.  Obtain usage metrics that your application can use by calling the [**MsiGetFeatureUsage**](msigetfeatureusage.md) function.

The following diagram illustrates the feature request model.

![feature request model. ](images/over2.png)

 

 



