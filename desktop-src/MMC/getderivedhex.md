---
title: SysColorCtrl.GetDerivedHex method
description: The GetDerivedHex method derives a color based on a starting color, a color to move toward, and a percentage to move toward that color. It is returned as a hexadecimal value.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '89dae6a6-1c01-4195-a8c5-4405874f6086'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["GetDerivedHex method MMC", "GetDerivedHex method MMC , SysColorCtrl class", "SysColorCtrl class MMC , GetDerivedHex method"]
topic_type:
- apiref
api_name:
- SysColorCtrl.GetDerivedHex
api_location:
- Cic.dll
api_type:
- COM
---

# SysColorCtrl.GetDerivedHex method

The **GetDerivedHex** method derives a color based on a starting color, a color to move toward, and a percentage to move toward that color. It is returned as a hexadecimal value.

## Syntax


```VB
SysColorCtrl.GetDerivedHex( _
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

*nPercent* 
</dt> <dd>

An integer that represents the percentage (0 to 100) between the *pszFrom* and *pszTo* colors. This value represents what percentage of the *pszTo* color should be blended with the *pszFrom* color. For example, a value of 0 would return the *pszFrom* color, a value of 50 would return a color that was halfway between *pszFrom* and *pszTo*, and a value of 100 would return the *pszTo* color. This value must be between 0 and 100.

</dd> </dl>

## Return value

A string that contains the hexadecimal value for the derived color specified by the method's parameters.

## Examples

The following HTML page embeds the SysColorCtrl control as an object and uses the **GetDerivedHex** method to set the background color of the page to color that is 50% between the system color settings for activecaption and activeborder.


```HTML
<html>
<head>
<object 
    ID="SysColorX"
    classid="clsid:C47195EC-CD7A-11D1-8EA3-00C04F9900D7"
    width=0
    height=0>
</object>
 
<script language=javascript>
function init() {
    color1 = "activecaption";
    color2 = "activeborder";
    pcnt = 50;
    document.body.bgColor=SysColorX.GetDerivedHex(color1, color2,'CSS',pcnt);
}
</script>
</head>
<body onload="init()">
</body>
</html>
```



## Requirements



|                            |                                                                                    |
|----------------------------|------------------------------------------------------------------------------------|
| Redistributable<br/> | MMC 1.1 or later<br/>                                                        |
| DLL<br/>             | <dl> <dt>Cic.dll</dt> </dl> |



 

 





