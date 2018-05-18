---
title: SysColorCtrl.GetBlueFromRGB method
description: The GetBlueFromRGB method gets the blue value from an RGB value.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '0090e673-52f8-4343-ba97-59b359fe555b'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["GetBlueFromRGB method MMC", "GetBlueFromRGB method MMC , SysColorCtrl class", "SysColorCtrl class MMC , GetBlueFromRGB method"]
topic_type:
- apiref
api_name:
- SysColorCtrl.GetBlueFromRGB
api_location:
- Cic.dll
api_type:
- COM
---

# SysColorCtrl.GetBlueFromRGB method

The **GetBlueFromRGB** method gets the blue value from an RGB value.

## Syntax


```VB
SysColorCtrl.GetBlueFromRGB( _
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

An integer that contains the blue value (between 0 and 255) in the RGB value specified by *rgb*.

## Requirements



|                            |                                                                                    |
|----------------------------|------------------------------------------------------------------------------------|
| Redistributable<br/> | MMC 1.1 or later<br/>                                                        |
| DLL<br/>             | <dl> <dt>Cic.dll</dt> </dl> |



 

 





