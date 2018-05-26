---
title: PSM\_SETCURSELID message
description: Activates the given page in a property sheet based on the resource identifier of the page. You can send this message explicitly or by using the PropSheet\_SetCurSelByID macro.
ms.assetid: 6db5f6ab-77ce-4a80-a84d-cb66eb1cdeaa
keywords:
- PSM_SETCURSELID message Windows Controls
topic_type:
- apiref
api_name:
- PSM_SETCURSELID
api_location:
- Prsht.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# PSM\_SETCURSELID message

Activates the given page in a property sheet based on the resource identifier of the page. You can send this message explicitly or by using the [**PropSheet\_SetCurSelByID**](/windows/win32/Prsht/nf-prsht-propsheet_setcurselbyid?branch=master) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

Resource identifier of the page to activate.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Remarks

The window that is losing the activation receives the [PSN\_KILLACTIVE](psn-killactive.md) notification code, and the window that is gaining the activation receives the [PSN\_SETACTIVE](psn-setactive.md) notification code.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Prsht.h</dt> </dl> |



 

 





