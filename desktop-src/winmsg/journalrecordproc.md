---
UID: 
title: JournalRecordProc callback function
description: The function records messages the system removes from the system message queue.
old-location: 
ms.assetid: na
ms.date: 04/05/2019
ms.keywords: 
ms.topic: reference
req.header: 
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
- APIRef
api_type: 
api_location: 
api_name: 
targetos: Windows
req.typenames: 
req.redist: 
---

# JournalRecordProc function

## Description

An application-defined or library-defined callback function used with the [SetWindowsHookEx](/windows/desktop/api/winuser/nf-winuser-setwindowshookexw) function.
The function records messages the system removes from the system message queue.
Later, an application can use a [JournalPlaybackProc](journalplaybackproc.md) hook procedure to play back the messages.

The **HOOKPROC** type defines a pointer to this callback function.
**JournalRecordProc** is a placeholder for the application-defined or library-defined function name.

```cpp
LRESULT CALLBACK JournalRecordProc(
  _In_ int    code,
       WPARAM wParam,
  _In_ LPARAM lParam
);
```

## Parameters

### code [in]

Type: **int**

Specifies how to process the message.
If *code* is less than zero, the hook procedure must pass the message to the [CallNextHookEx](/windows/desktop/api/winuser/nf-winuser-callnexthookex) function without further processing and should return the value returned by **CallNextHookEx**.
This parameter can be one of the following values.

| Value | Meaning |
|-------|---------|
| **HC_ACTION** 0 | The *lParam* parameter is a pointer to an [EVENTMSG](/windows/desktop/api/winuser/ns-winuser-eventmsg) structure containing information about a message removed from the system queue. The hook procedure must record the contents of the structure by copying them to a buffer or file. |
| **HC_SYSMODALOFF** 5 | A system-modal dialog box has been destroyed. The hook procedure must resume recording. |
| **HC_SYSMODALON** 4 | A system-modal dialog box is being displayed. Until the dialog box is destroyed, the hook procedure must stop recording. |

### wParam

Type: **WPARAM**

This parameter is not used.

### lParam [in]

Type: **LPARAM**

A pointer to an **EVENTMSG** structure that contains the message to be recorded.

## Returns

Type: **LRESULT**

The return value is ignored.

## Remarks

A **JournalRecordProc** hook procedure must copy but not modify the messages.
After the hook procedure returns control to the system, the message continues to be processed.

Install the **JournalRecordProc** hook procedure by specifying the [WH_JOURNALRECORD](about-hooks.md) type and a pointer to the hook procedure in a call to the **SetWindowsHookEx** function.

A **JournalRecordProc** hook procedure does not need to live in a dynamic-link library.
A **JournalRecordProc** hook procedure can live in the application itself.

Unlike most other global hook procedures, the **JournalRecordProc** and [JournalPlaybackProc](journalplaybackproc.md) hook procedures are always called in the context of the thread that set the hook.

An application that has installed a **JournalRecordProc** hook procedure should watch for the [VK_CANCEL](/windows/desktop/inputdev/virtual-key-codes) virtual key code (which is implemented as the CTRL+BREAK key combination on most keyboards).
This virtual key code should be interpreted by the application as a signal that the user wishes to stop journal recording.
The application should respond by ending the recording sequence and removing the **JournalRecordProc** hook procedure.
Removal is important.
It prevents a journaling application from locking up the system by hanging inside a hook procedure.

This role as a signal to stop journl recording means that a CTRL+BREAK key combination cannot itself be recorded.
Since the CTRL+C key combination has no such role as a journaling signal, it can be recorded.
There are two other key combinations that cannot be recorded: CTRL+ESC and CTRL+ALT+DEL.
Those two key combinations cause the system to stop all journaling activities (record or playback), remove all journaling hooks, and post a [WM_CANCELJOURNAL](wm-canceljournal.md) message to the journaling application.

## See also

[CallNextHookEx](/windows/desktop/api/winuser/nf-winuser-callnexthookex)

[EVENTMSG](/windows/desktop/api/winuser/ns-winuser-eventmsg)

[JournalPlaybackProc](journalplaybackproc.md)

[SetWindowsHookEx](/windows/desktop/api/winuser/nf-winuser-setwindowshookexw)

[WM_CANCELJOURNAL](wm-canceljournal.md)

[Hooks](hooks.md)
