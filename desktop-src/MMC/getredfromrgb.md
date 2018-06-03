---
title: SysColorCtrl.GetRedFromRGB method
description: The GetRedFromRGB method gets the red value from an RGB value.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c48bc035-9226-4dae-adc0-cab6d53ccb58
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- GetRedFromRGB method MMC
- GetRedFromRGB method MMC , SysColorCtrl class
- SysColorCtrl class MMC , GetRedFromRGB method
topic_type:
- apiref
api_name:
- SysColorCtrl.GetRedFromRGB
api_location:
- Cic.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SysColorCtrl.GetRedFromRGB method

The **GetRedFromRGB** method gets the red value from an RGB value.

## Syntax


```VB
SysColorCtrl.GetRedFromRGB( _
  ByVal rgb _
)
```



## Parameters

<dl> <dt>

*rgb* 
</dt> <dd>

An integer that is the RGB value of the color.

</dd> </dl>

## Return value

An integer that contains the red value (between 0 and 255) in the RGB value specified by *rgb*.

## Requirements



|                            |                                                                                    |
|----------------------------|------------------------------------------------------------------------------------|
| Redistributable<br/> | MMC 1.1 or later<br/>                                                        |
| DLL<br/>             | <dl> <dt>Cic.dll</dt> </dl> |



 

 





