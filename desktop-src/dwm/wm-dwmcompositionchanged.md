---
title: WM\_DWMCOMPOSITIONCHANGED message
description: Informs all top-level windows that Desktop Window Manager (DWM) composition has been enabled or disabled.
ms.assetid: VS|winui|~\winui\windowsuserinterface\windowing\windows\windowreference\windowmessages\wm_dwmcompositionchanged.htm
keywords:
- WM_DWMCOMPOSITIONCHANGED message Desktop Window Manager
topic_type:
- apiref
api_name:
- WM_DWMCOMPOSITIONCHANGED
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WM\_DWMCOMPOSITIONCHANGED message

Informs all top-level windows that Desktop Window Manager (DWM) composition has been enabled or disabled.

> [!Note]  
> As of Windows 8, DWM composition is always enabled, so this message is not sent regardless of video mode changes.

 

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Not used.

</dd> <dt>

*lParam* 
</dt> <dd>

Not used.

</dd> </dl>

## Return value

If an application processes this message, it should return zero.

## Remarks

A window receives this message through its [**WindowProc**](https://msdn.microsoft.com/library/windows/desktop/ms633573) function.

The [**DwmIsCompositionEnabled**](/windows/win32/Dwmapi/nf-dwmapi-dwmiscompositionenabled?branch=master) function can be used to determine the current composition state.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Winuser.h</dt> </dl> |



 

 





