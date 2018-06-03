---
title: SysColorCtrl.GetQuarterLightRGB method
description: The GetQuarterLightRGB method derives a \ 0034;lighter \ 0034; color by calculating a color that is blended 25 between a given color and white. The derived color will be a blend of 75 of the given color and 25 white. It is returned as an RGB value.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4ccd6744-afeb-4869-80c6-95e5ddfd810c
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- GetQuarterLightRGB method MMC
- GetQuarterLightRGB method MMC , SysColorCtrl class
- SysColorCtrl class MMC , GetQuarterLightRGB method
topic_type:
- apiref
api_name:
- SysColorCtrl.GetQuarterLightRGB
api_location:
- Cic.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SysColorCtrl.GetQuarterLightRGB method

The **GetQuarterLightRGB** method derives a "lighter" color by calculating a color that is blended 25% between a given color and white. The derived color will be a blend of 75% of the given color and 25% white. It is returned as an RGB value.

## Syntax


```VB
SysColorCtrl.GetQuarterLightRGB( _
  ByVal pszFrom, _
  ByVal pszFormat _
)
```



## Parameters

<dl> <dt>

*pszFrom* \[in\]
</dt> <dd>

A string that contains the color you want to use as the starting color. The contents of the string depend on the format specified in the *pszFormat* parameter.

</dd> <dt>

*pszFormat* \[in\]
</dt> <dd>

A string that contains the name of the format that is being passed in the *pszFrom* parameters.

<dt>

<span id="CSS"></span><span id="css"></span>

<span id="CSS"></span><span id="css"></span>**CSS**


</dt> <dd>

Name of the display element whose color you want to specify. See [System Color Values for Color Derivation Methods](system-color-values-for-color-derivation-methods.md).

</dd> <dt>

<span id="HEX"></span><span id="hex"></span>

<span id="HEX"></span><span id="hex"></span>**HEX**


</dt> <dd>

Hexadecimal form of the color. For example, specify FFFFFF for white.

</dd> <dt>

<span id="RGB"></span><span id="rgb"></span>

<span id="RGB"></span><span id="rgb"></span>**RGB**


</dt> <dd>

RGB form of the color. For example, specify 16777215 for white.

</dd> </dl> </dd> </dl>

## Return value

An integer that is the RGB value for the derived color specified by the method's parameters.

## Requirements



|                            |                                                                                    |
|----------------------------|------------------------------------------------------------------------------------|
| Redistributable<br/> | MMC 1.1 or later<br/>                                                        |
| DLL<br/>             | <dl> <dt>Cic.dll</dt> </dl> |



 

 





