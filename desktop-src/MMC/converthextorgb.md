---
title: SysColorCtrl.ConvertHexToRGB method
description: The ConvertHexToRGB method converts a hexadecimal value to RGB.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b551dc70-8bda-4cd2-818f-7a6dfb0bee75
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- ConvertHexToRGB method MMC
- ConvertHexToRGB method MMC , SysColorCtrl class
- SysColorCtrl class MMC , ConvertHexToRGB method
topic_type:
- apiref
api_name:
- SysColorCtrl.ConvertHexToRGB
api_location:
- Cic.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SysColorCtrl.ConvertHexToRGB method

The **ConvertHexToRGB** method converts a hexadecimal value to RGB.

## Syntax


```VB
SysColorCtrl.ConvertHexToRGB( _
  ByVal szHex _
)
```



## Parameters

<dl> <dt>

*szHex* \[in\]
</dt> <dd>

A string that contains the hexadecimal value of the color.

</dd> </dl>

## Return value

An integer that is the RGB value equivalent of the hexadecimal value specified by *szHex*.

## Requirements



|                            |                                                                                    |
|----------------------------|------------------------------------------------------------------------------------|
| Redistributable<br/> | MMC 1.1 or later<br/>                                                        |
| DLL<br/>             | <dl> <dt>Cic.dll</dt> </dl> |



 

 





