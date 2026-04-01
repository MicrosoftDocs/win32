---
UID: NF:winuser.ConvertPrimaryPointerToMouseDrag
description: Starts converting the current touch or pen (pointer) input contact to mouse input.
tech.root: winmsg
title: ConvertPrimaryPointerToMouseDrag function
ms.topic: reference
ms.date: 03/31/2026
req.lib:
req.dll: User32.dll
topic_type:
- APIRef
api_type:
 - DllExport
api_location:
 - user32.dll
api_name:
 - ConvertPrimaryPointerToMouseDrag
f1_keywords:
 - ConvertPrimaryPointerToMouseDrag
 - winuser/ConvertPrimaryPointerToMouseDrag
dev_langs:
 - c++
helpviewer_keywords:
 - ConvertPrimaryPointerToMouseDrag
targetos: Windows
ms.localizationpriority: low
---

# ConvertPrimaryPointerToMouseDrag function

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

**ConvertPrimaryPointerToMouseDrag** allows an app that is handling pointer input to ask the system to generate mouse messages for the on-going pointer contact. This API is expected to be called after receiving a **WM_POINTERDOWN** for a primary pointer contact, before receiving the **WM_POINTERUP** for the same pointer ID.

## Syntax

```cpp
BOOL ConvertPrimaryPointerToMouseDrag();
```

## Return value

Type: **BOOL**

If the function returns **TRUE**, the primary pointer contact was promoted to mouse. The window receiving input will get mouse messages (**WM_LBUTTONDOWN**, **WM_MOUSEMOVE**, and **WM_LBUTTONUP**) in addition to the pointer messages for the remainder of the contact.

If the function returns **FALSE**, the primary pointer contact was not promoted. This could happen because the calling thread did not have a primary pointer contact, or because the thread had multiple simultaneous contacts.

If the function fails, the return value is zero. To get extended error information, call [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror).

## Remarks

Touch and pen input use different window messages than mouse input. See [Pointer Input](/windows/win32/api/_inputmsg/) for more info. By default, apps that do not handle pointer messages have the primary pointer contact automatically promoted to mouse input. Apps that do handle pointer messages do not receive mouse messages, which can cause problems when calling APIs that expect mouse input, such as [**DoDragDrop**](/windows/win32/api/ole2/nf-ole2-dodragdrop).

**DoDragDrop** expects to be called while mouse input is active — typically in response to a **WM_LBUTTONDOWN** or **WM_MOUSEMOVE** while the button is held. It captures mouse input and processes drag-and-drop, exiting when it receives **WM_LBUTTONUP**. During the drag, each move and up event interacts with the window under the cursor if that window is registered as a drop target.

**ConvertPrimaryPointerToMouseDrag** bridges this gap by allowing a pointer-aware app to promote the on-going pointer contact to mouse on demand. The app can use pointer messages to determine whether the input should become a drag (for example, by detecting a press and hold), then call this function immediately before calling **DoDragDrop** to switch the contact to mouse input for the remainder of the interaction.

The calling thread must have exactly one pointer contact, and it must be primary. See [**IS_POINTER_PRIMARY_WPARAM**](/windows/win32/api/winuser/nf-winuser-is_pointer_primary_wparam).

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum supported client** | Windows 11 \[desktop apps only\] |
| **Target Platform** | Windows |
| **Header** | None |
| **Library** | None |
| **DLL** | User32.dll (ordinal 2811) |
