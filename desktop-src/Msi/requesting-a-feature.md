---
Description: There are several functions an application must call to request features.
ms.assetid: 5253c6f0-316f-4f24-b0c0-951db8d16745
title: Requesting a Feature
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Requesting a Feature

There are several functions an application must call to request features. Before requesting a feature, the application must ensure that the feature is installed. If the application calls [**MsiUseFeature**](/windows/win32/Msi/nf-msi-msiusefeaturea?branch=master) before the application accesses a feature, the application can use the information returned to maintain usage metrics.

**To request a feature**

1.  Call the [**MsiEnumFeatures**](/windows/win32/Msi/nf-msi-msienumfeaturesa?branch=master) or the [**MsiQueryFeatureState**](/windows/win32/Msi/nf-msi-msiqueryfeaturestatea?branch=master) function if you want to determine the availability of a feature without incrementing the usage count.
2.  Indicate your application's intent to use a feature by calling the [**MsiUseFeature**](/windows/win32/Msi/nf-msi-msiusefeaturea?branch=master) function.
3.  Determine file locations by calling the [**MsiGetComponentPath**](/windows/win32/Msi/nf-msi-msigetcomponentpatha?branch=master) function.
4.  Configure the feature by calling the [**MsiConfigureFeature**](/windows/win32/Msi/nf-msi-msiconfigurefeaturea?branch=master) function.
5.  Obtain usage metrics that your application can use by calling the [**MsiGetFeatureUsage**](/windows/win32/Msi/nf-msi-msigetfeatureusagea?branch=master) function.

The following diagram illustrates the feature request model.

![feature request model. ](images/over2.png)

 

 



