---
title: TB\_SETMETRICS message
description: Sets the metrics of a toolbar control.
ms.assetid: 60e35d65-6291-4a55-a4cf-19b5b1db8a65
keywords:
- TB_SETMETRICS message Windows Controls
topic_type:
- apiref
api_name:
- TB_SETMETRICS
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

# TB\_SETMETRICS message

Sets the metrics of a toolbar control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

[**TBMETRICS**](/windows/win32/Commctrl/ns-commctrl-tbmetrics?branch=master) structure that contains the toolbar metrics to set.

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



 

 





