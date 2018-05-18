---
title: SysColorCtrl.GetQuarterLightHex method
description: The GetQuarterLightHex method derives a \ 0034;lighter \ 0034; color by calculating a color that is blended 25 between a given color and white. The derived color will be a blend of 75 of the given color and 25 white. It is returned as a hexadecimal value.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '6f2a85ad-3c17-4314-9061-d16d0230bea4'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["GetQuarterLightHex method MMC", "GetQuarterLightHex method MMC , SysColorCtrl class", "SysColorCtrl class MMC , GetQuarterLightHex method"]
topic_type:
- apiref
api_name:
- SysColorCtrl.GetQuarterLightHex
api_location:
- Cic.dll
api_type:
- COM
---

# SysColorCtrl.GetQuarterLightHex method

The **GetQuarterLightHex** method derives a "lighter" color by calculating a color that is blended 25% between a given color and white. The derived color will be a blend of 75% of the given color and 25% white. It is returned as a hexadecimal value.

## Syntax


```VB
SysColorCtrl.GetQuarterLightHex( _
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

CSS
</dt> <dd>

Name of the display element whose color you want to specify. See [System Color Values for Color Derivation Methods](system-color-values-for-color-derivation-methods.md).

</dd> <dt>

HEX
</dt> <dd>

Hexadecimal form of the color. For example, specify FFFFFF for white.

</dd> <dt>

RGB
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



 

 





