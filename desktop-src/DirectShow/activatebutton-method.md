---
description: The ActivateButton method activates the selected menu button.
ms.assetid: 1da486a0-dadc-4c92-b3d3-83aeace01e39
title: ActivateButton Method
ms.topic: reference
ms.date: 05/31/2018
---

# ActivateButton Method

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The ActivateButton method activates the selected menu button.

``` syntax
        MSWebDVD.ActivateButton()
```

## Return Value

No return value.

## Remarks

Use this method when implementing custom mouse handling after setting [**DisableAutoMouseProcessing**](disableautomouseprocessing-property.md) to **true**.

Use this method to activate a button that has been selected through the [**SelectLeftButton**](selectleftbutton-method.md), [**SelectLowerButton**](selectlowerbutton-method.md), [**SelectUpperButton**](selectupperbutton-method.md), or [**SelectRightButton**](selectrightbutton-method.md) method.

 

 



