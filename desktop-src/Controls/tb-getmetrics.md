---
title: TB\_GETMETRICS message
description: Retrieves the metrics of a toolbar control.
ms.assetid: 19c735cf-09f8-443e-8a73-dd64af0193a1
keywords:
- TB_GETMETRICS message Windows Controls
topic_type:
- apiref
api_name:
- TB_GETMETRICS
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# TB\_GETMETRICS message

Retrieves the metrics of a toolbar control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**TBMETRICS**](/windows/win32/Commctrl/ns-commctrl-tbmetrics?branch=master) structure that receives the toolbar metrics.

</dd> </dl>

## Return value

The return value is not used.

## Remarks

> [!Note]  
> To use this message, you must provide a manifest specifying Comclt32.dll version 6.0. For more information on manifests, see [Enabling Visual Styles](cookbook-overview.md).

 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





