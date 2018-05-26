---
title: DTM\_GETMCFONT message
description: Gets the font that the date and time picker (DTP) controls child month calendar control is currently using. You can send this message explicitly or use the DateTime\_GetMonthCalFont macro.
ms.assetid: 6687a1dc-6f6d-4684-80b2-f726b08d2f3a
keywords:
- DTM_GETMCFONT message Windows Controls
topic_type:
- apiref
api_name:
- DTM_GETMCFONT
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

# DTM\_GETMCFONT message

Gets the font that the date and time picker (DTP) control's child month calendar control is currently using. You can send this message explicitly or use the [**DateTime\_GetMonthCalFont**](/windows/win32/Commctrl/nf-commctrl-datetime_getmonthcalfont?branch=master) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns an HFONT value that is the handle to the current font.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





