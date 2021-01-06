---
description: The DisableAutoMouseProcessing property enables or disables the MSWebDVD object's mouse-processing functionality.
ms.assetid: d438deb8-3c6d-49c1-923b-d4c57e236fc9
title: DisableAutoMouseProcessing Property
ms.topic: reference
ms.date: 05/31/2018
---

# DisableAutoMouseProcessing Property

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `DisableAutoMouseProcessing` property enables or disables the **MSWebDVD** object's mouse-processing functionality.

``` syntax
[ bMouseProcessing = ] MSWebDVD.DisableAutoMouseProcessing
```

## Return Value

Returns a boolean value indicating whether to disable the default mouse processing.

## Remarks

This property is read/write with a default value of false. The **MSWebDVD** object automatically handles mouse actions for DVD on-screen menus by default; users can highlight and activate menu buttons without special programming by the application. An application can turn off this default mouse-handling functionality by setting this property to **true**. When the automatic mouse processing is turned off, an application must use the various button-related methods and properties to handle mouse moves and mouse clicks on the on-screen menus. Also, an application can use the button-related methods to override the automatic mouse handling even when when `DisableAutoMouseProcessing` is set to **false**.

 

 



