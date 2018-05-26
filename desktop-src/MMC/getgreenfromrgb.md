---
title: SysColorCtrl.GetGreenFromRGB method
description: The GetGreenFromRGB method gets the green value from an RGB value.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5c2bbf01-300e-42cd-9895-c4b355faa136
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- GetGreenFromRGB method MMC
- GetGreenFromRGB method MMC , SysColorCtrl class
- SysColorCtrl class MMC , GetGreenFromRGB method
topic_type:
- apiref
api_name:
- SysColorCtrl.GetGreenFromRGB
api_location:
- Cic.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SysColorCtrl.GetGreenFromRGB method

The **GetGreenFromRGB** method gets the green value from an RGB value.

## Syntax


```VB
SysColorCtrl.GetGreenFromRGB( _
  ByVal rgb _
)
```



## Parameters

<dl> <dt>

*rgb* \[in\]
</dt> <dd>

An integer that is the RGB value of the color.

</dd> </dl>

## Return value

An integer that contains the green value (between 0 and 255) in the RGB value specified by *rgb*.

## Requirements



|                            |                                                                                    |
|----------------------------|------------------------------------------------------------------------------------|
| Redistributable<br/> | MMC 1.1 or later<br/>                                                        |
| DLL<br/>             | <dl> <dt>Cic.dll</dt> </dl> |



 

 





