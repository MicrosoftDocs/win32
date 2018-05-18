---
title: SysColorCtrl.GetHalfLightHex method
description: The GetHalfLightHex method derives a \ 0034;lighter \ 0034; color by calculating a color that is blended 50 between a given color and white. It is returned as a hexadecimal value.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e3962093-7f08-4831-ab33-b893bb5d1bea'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["GetHalfLightHex method MMC", "GetHalfLightHex method MMC , SysColorCtrl class", "SysColorCtrl class MMC , GetHalfLightHex method"]
topic_type:
- apiref
api_name:
- SysColorCtrl.GetHalfLightHex
api_location:
- Cic.dll
api_type:
- COM
---

# SysColorCtrl.GetHalfLightHex method

The **GetHalfLightHex** method derives a "lighter" color by calculating a color that is blended 50% between a given color and white. It is returned as a hexadecimal value.

## Syntax


```VB
SysColorCtrl.GetHalfLightHex( _
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

A string that contains the hexadecimal value for the derived color specified by the method's parameters.

## Requirements



|                            |                                                                                    |
|----------------------------|------------------------------------------------------------------------------------|
| Redistributable<br/> | MMC 1.1 or later<br/>                                                        |
| DLL<br/>             | <dl> <dt>Cic.dll</dt> </dl> |



 

 





