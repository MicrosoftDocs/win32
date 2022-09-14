---
title: ACM_OPEN message (Commctrl.h)
description: Opens an AVI clip and displays its first frame in an animation control. You can send this message explicitly or use the Animate\_Open or Animate\_OpenEx macro. We recommend using the Unicode version of this message, ACM\_OPENW.
ms.assetid: 87f476ce-bb27-4b5f-bfdf-dff84bd7e4f4
keywords:
- ACM_OPEN message Windows Controls
topic_type:
- apiref
api_name:
- ACM_OPEN
- ACM_OPENA
- ACM_OPENW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# ACM\_OPEN message

Opens an AVI clip and displays its first frame in an animation control. You can send this message explicitly or use the [**Animate\_Open**](/windows/desktop/api/Commctrl/nf-commctrl-animate_open) or [**Animate\_OpenEx**](/windows/desktop/api/Commctrl/nf-commctrl-animate_openex) macro. We recommend using the Unicode version of this message, ACM\_OPENW.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

[Version 4.71](common-control-versions.md) and later. An instance handle to the module from which the resource should be loaded. Set this value to **NULL** to have the control use the HINSTANCE value used to create the window. Note that if the window is created by a DLL, the default value for *wParam* is the HINSTANCE value of the DLL, not of the application that calls the DLL.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to a buffer that contains the path of the AVI file or the name of an AVI resource. Alternatively, this parameter can consist of the AVI resource identifier in the [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)) and zero in the [**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85)). To create this value, use the [**MAKEINTRESOURCE**](/windows/desktop/api/winuser/nf-winuser-makeintresourcea) macro. The control loads the AVI resource from the module specified by the instance handle passed to the [**CreateWindow**](/windows/desktop/api/winuser/nf-winuser-createwindowa) function, the [**Animate\_Create**](/windows/desktop/api/Commctrl/nf-commctrl-animate_create) macro, or the dialog box creation function that created the control. In [Version 4.71](common-control-versions.md) and later, the resource is loaded from the module specified by *wParam*. An AVI resource must have the "AVI" type. If this parameter is **NULL**, the system closes the AVI file that was previously opened for the specified animation control, if any.

</dd> </dl>

## Return value

Returns nonzero if successful, or zero otherwise.

## Remarks

The AVI file or resource specified by *lpszName* must not contain audio.

We recommend using the Unicode version of this message, ACM\_OPENW.

You can only open silent AVI clips. ACM\_OPEN and [**Animate\_Open**](/windows/desktop/api/Commctrl/nf-commctrl-animate_open) fail if *lParam* specifies an AVI clip that contains sound.

You can use [**Animate\_Close**](/windows/desktop/api/Commctrl/nf-commctrl-animate_close) to close an AVI file or AVI resource that was previously opened for the specified animation control.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **ACM\_OPENW** (Unicode) and **ACM\_OPENA** (ANSI)<br/>                         |



 

