---
title: SysColorCtrl.GetDerivedRGB method
description: The GetDerivedRGB method derives a color based on a starting color, a color to move toward, and a percentage to move toward that color. It is returned as an RGB value.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 85916fd5-ce78-4444-9302-6e2468ad5dfc
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- GetDerivedRGB method MMC
- GetDerivedRGB method MMC , SysColorCtrl class
- SysColorCtrl class MMC , GetDerivedRGB method
topic_type:
- apiref
api_name:
- SysColorCtrl.GetDerivedRGB
api_location:
- Cic.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SysColorCtrl.GetDerivedRGB method

The **GetDerivedRGB** method derives a color based on a starting color, a color to move toward, and a percentage to move toward that color. It is returned as an RGB value.

## Syntax


```VB
SysColorCtrl.GetDerivedRGB( _
  ByVal pszFrom, _
  ByVal pszTo, _
  ByVal pszFormat, _
  ByVal nPercent _
)
```



## Parameters

<dl> <dt>

*pszFrom* \[in\]
</dt> <dd>

A string that contains the color you want to use as the starting color. The contents of the string depend on the format specified in the *pszFormat* parameter.

</dd> <dt>

*pszTo* \[in\]
</dt> <dd>

A string that contains the color to move toward.

</dd> <dt>

*pszFormat* \[in\]
</dt> <dd>

A string that contains the name of the format that is being passed in the *pszFrom* and *pszTo* parameters.

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

</dd> </dl> </dd> <dt>

*nPercent* \[in\]
</dt> <dd>

An integer that represents the percentage (0 to 100) between the *pszFrom* and *pszTo* colors. This value represents what percentage of the *pszTo* color should be blended with the *pszFrom* color. For example, a value of 0 would return the *pszFrom* color, a value of 50 would return a color that was halfway between *pszFrom* and *pszTo*, and a value of 100 would return the *pszTo* color. This value must be between 0 and 100.

</dd> </dl>

## Return value

An integer that is the RGB value for the derived color specified by the method's parameters.

## Requirements



|                            |                                                                                    |
|----------------------------|------------------------------------------------------------------------------------|
| Redistributable<br/> | MMC 1.1 or later<br/>                                                        |
| DLL<br/>             | <dl> <dt>Cic.dll</dt> </dl> |



 

 





