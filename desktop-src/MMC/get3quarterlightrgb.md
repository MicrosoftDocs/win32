---
title: SysColorCtrl.Get3QuarterLightRGB method
description: The Get3QuarterLightRGB method derives a \ 0034;lighter \ 0034; color by calculating a color that is blended 75 between a given color and white. The derived color will be a blend of 25 of the given color and 75 white. It is returned as an RGB value.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: bbbb01a3-a2b8-4aad-a169-27ceaf0e300e
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Get3QuarterLightRGB method MMC
- Get3QuarterLightRGB method MMC , SysColorCtrl class
- SysColorCtrl class MMC , Get3QuarterLightRGB method
topic_type:
- apiref
api_name:
- SysColorCtrl.Get3QuarterLightRGB
api_location:
- Cic.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SysColorCtrl.Get3QuarterLightRGB method

The **Get3QuarterLightRGB** method derives a "lighter" color by calculating a color that is blended 75% between a given color and white. The derived color will be a blend of 25% of the given color and 75% white. It is returned as an RGB value.

## Syntax


```VB
SysColorCtrl.Get3QuarterLightRGB( _
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



 

 





