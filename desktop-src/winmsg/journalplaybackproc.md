---
UID: 
title: JournalPlaybackProc callback function
description: Plays back a series of mouse and keyboard messages recorded previously.
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

# JournalPlaybackProc function

## Description

An application-defined or library-defined callback function used with the [SetWindowsHookEx](/windows/desktop/api/winuser/nf-winuser-setwindowshookexw) function.
Typically, an application uses this function to play back a series of mouse and keyboard messages recorded previously by the **JournalRecordProc** hook procedure.
As long as a **JournalPlaybackProc** hook procedure is installed, regular mouse and keyboard input is disabled.

The **HOOKPROC** type defines a pointer to this callback function.
**JournalPlaybackProc** is a placeholder for the application-defined or library-defined function name.

```cpp
LRESULT CALLBACK JournalPlaybackProc(
  _In_ int    code,
       WPARAM wParam,
  _In_ LPARAM lParam
);
```

## Parameters

### code [in]

Type: **int**

A code the hook procedure uses to determine how to process the message.
If *code* is less than zero, the hook procedure must pass the message to the [CallNextHookEx](/windows/desktop/api/winuser/nf-winuser-callnexthookex) function without further processing and should return the value returned by **CallNextHookEx**.
This parameter can be one of the following values.

| Value | Meaning |
|-------|---------|
| **HC_GETNEXT** 1 | The hook procedure must copy the current mouse or keyboard message to the [EVENTMSG](/windows/desktop/api/winuser/ns-winuser-eventmsg) structure pointed to by the *lParam* parameter. |
| **HC_NOREMOVE** 3 | An application has called the [PeekMessage](/windows/desktop/api/winuser/nf-winuser-peekmessagew) function with wRemoveMsg set to **PM_NOREMOVE**, indicating that the message is not removed from the message queue after **PeekMessage** processing. |
| **HC_NOREMOVE** 2 | The hook procedure must prepare to copy the next mouse or keyboard message to the **EVENTMSG** structure pointed to by *lParam*. Upon receiving the **HC_GETNEXT** code, the hook procedure must copy the message to the structure. |
| **HC_SYSMODALOFF** 5 | A system-modal dialog box has been destroyed. The hook procedure must resume playing back the messages. |
| **HC_SYSMODALON** 4 | A system-modal dialog box is being displayed. Until the dialog box is destroyed, the hook procedure must stop playing back messages. |

### wParam

Type: **WPARAM**

This parameter is not used.

### lParam

Type: **LPARAM**

A pointer to an **EVENTMSG** structure that represents a message being processed by the hook procedure.
This parameter is valid only when the *code* parameter is **HC_GETNEXT**.

## Returns

Type: **LRESULT**

To have the system wait before processing the message, the return value must be the amount of time, in clock ticks, that the system should wait.

(This value can be computed by calculating the difference between the time members in the current and previous input messages.)

To process the message immediately, the return value should be zero. The return value is used only if the hook code is **HC_GETNEXT**; otherwise, it is ignored.

## Remarks

A **JournalPlaybackProc** hook procedure should copy an input message to The *lParam* parameter.
The message must have been previously recorded by using a **JournalRecordProc** hook procedure, which should not modify the message.

To retrieve the same message over and over, the hook procedure can be called several times with the *code* parameter set to **HC_GETNEXT** without an intervening call with *code* set to **HC_SKIP**.

If *code* is **HC_GETNEXT** and the return value is greater than zero, the system sleeps for the number of milliseconds specified by the return value. When the system continues, it calls the hook procedure again with *code* set to **HC_GETNEXT** to retrieve the same message.
The return value from this new call to **JournalPlaybackProc** should be zero; otherwise, the system will go back to sleep for the number of milliseconds specified by the return value, call **JournalPlaybackProc** again, and so on.
The system will appear to be not responding.

Unlike most other global hook procedures, the **JournalRecordProc** and **JournalPlaybackProc** hook procedures are always called in the context of the thread that set the hook.

After the hook procedure returns control to the system, the message continues to be processed. If *code* is **HC_SKIP**, the hook procedure must prepare to return the next recorded event message on its next call.

Install the **JournalPlaybackProc** hook procedure by specifying the [WH_JOURNALPLAYBACK](about-hooks.md) type and a pointer to the hook procedure in a call to the **SetWindowsHookEx** function.

If the user presses CTRL+ESC OR CTRL+ALT+DEL during journal playback, the system stops the playback, unhooks the journal playback procedure, and posts a [WM_CANCELJOURNAL](wm-canceljournal.md) message to the journaling application.

If the hook procedure returns a message in the range **WM_KEYFIRST** to **WM_KEYLAST**, the following conditions apply:

* The **paramL** member of the **EVENTMSG** structure specifies the virtual key code of the key that was pressed.
* The **paramH** member of the **EVENTMSG** structure specifies the scan code.
* There's no way to specify a repeat count.
The event is always taken to represent one key event.

## See also

[CallNextHookEx](/windows/desktop/api/winuser/nf-winuser-callnexthookex)

[EVENTMSG](/windows/desktop/api/winuser/ns-winuser-eventmsg)

[JournalRecordProc](journalrecordproc.md)

[PeekMessage](/windows/desktop/api/winuser/nf-winuser-peekmessagew)

[SetWindowsHookEx](/windows/desktop/api/winuser/nf-winuser-setwindowshookexw)

[WM_CANCELJOURNAL](wm-canceljournal.md)

[Hooks](hooks.md)
