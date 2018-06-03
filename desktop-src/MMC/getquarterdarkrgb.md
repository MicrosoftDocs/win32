---
title: SysColorCtrl.GetQuarterDarkRGB method
description: The GetQuarterDarkRGB method derives a \ 0034;darker \ 0034; color by calculating a color that is blended 25 between a given color and black. The derived color will be a blend of 75 of the given color and 25 black. It is returned as an RGB value.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 074ff30f-eca6-4602-a75a-5ff1b7d7093a
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- GetQuarterDarkRGB method MMC
- GetQuarterDarkRGB method MMC , SysColorCtrl class
- SysColorCtrl class MMC , GetQuarterDarkRGB method
topic_type:
- apiref
api_name:
- SysColorCtrl.GetQuarterDarkRGB
api_location:
- Cic.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SysColorCtrl.GetQuarterDarkRGB method

The **GetQuarterDarkRGB** method derives a "darker" color by calculating a color that is blended 25% between a given color and black. The derived color will be a blend of 75% of the given color and 25% black. It is returned as an RGB value.

## Syntax


```VB
SysColorCtrl.GetQuarterDarkRGB( _
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

A string that contains the name of the format that is being passed in the *pszFrom* parameter.

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



 

 





