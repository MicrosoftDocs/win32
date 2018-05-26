---
Description: This section discusses hooks. A hook is a point in the system message-handling mechanism where an application can install a subroutine to monitor the message traffic.
ms.assetid: 9ced0ac4-e602-425f-b954-6af9c741699a
title: Hooks
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Hooks

A hook is a point in the system message-handling mechanism where an application can install a subroutine to monitor the message traffic in the system and process certain types of messages before they reach the target window procedure.

### In This Section



| Name                                 | Description                                                         |
|--------------------------------------|---------------------------------------------------------------------|
| [Hook Overview](about-hooks.md)     | Discusses how hooks should be used.<br/>                      |
| [Using Hooks](using-hooks.md)       | Demonstrates how to perform tasks associated with hooks.<br/> |
| [Hook Reference](hook-reference.md) | Contains the API reference.<br/>                              |



 

### Hook Functions



| Name                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|----------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CallMsgFilter**](callmsgfilter.md)             | Passes the specified message and hook code to the hook procedures associated with the [**WH\_SYSMSGFILTER**](about-hooks.md#wh-msgfilter-and-wh-sysmsgfilter) and **WH\_MSGFILTER** hook procedures.<br/>                                                                                                                                                                                                                                                                                                                                                                                      |
| [**CallNextHookEx**](callnexthookex.md)           | Passes the hook information to the next hook procedure in the current hook chain. A hook procedure can call this function either before or after processing the hook information. <br/>                                                                                                                                                                                                                                                                                                                                                                                                         |
| [*CallWndProc*](callwndproc.md)                   | An application-defined or library-defined callback function used with the [**SetWindowsHookEx**](setwindowshookex.md) function. The system calls this function before calling the window procedure to process a message sent to the thread.<br/>                                                                                                                                                                                                                                                                                                                                               |
| [*CallWndRetProc*](callwndretproc.md)             | An application-defined or library-defined callback function used with the [**SetWindowsHookEx**](setwindowshookex.md) function. The system calls this function after the [**SendMessage**](sendmessage.md) function is called. The hook procedure can examine the message; it cannot modify it. <br/>                                                                                                                                                                                                                                                                                         |
| [*CBTProc*](cbtproc.md)                           | An application-defined or library-defined callback function used with the [**SetWindowsHookEx**](setwindowshookex.md) function. The system calls this function before activating, creating, destroying, minimizing, maximizing, moving, or sizing a window; before completing a system command; before removing a mouse or keyboard event from the system message queue; before setting the keyboard focus; or before synchronizing with the system message queue. A computer-based training (CBT) application uses this hook procedure to receive useful notifications from the system. <br/> |
| [*DebugProc*](debugproc.md)                       | An application-defined or library-defined callback function used with the [**SetWindowsHookEx**](setwindowshookex.md) function. The system calls this function before calling the hook procedures associated with any type of hook. The system passes information about the hook to be called to the [*DebugProc*](debugproc.md) hook procedure, which examines the information and determines whether to allow the hook to be called. <br/>                                                                                                                                                  |
| [*ForegroundIdleProc*](foregroundidleproc.md)     | An application-defined or library-defined callback function used with the [**SetWindowsHookEx**](setwindowshookex.md) function. The system calls this function whenever the foreground thread is about to become idle. <br/>                                                                                                                                                                                                                                                                                                                                                                   |
| [*GetMsgProc*](getmsgproc.md)                     | An application-defined or library-defined callback function used with the [**SetWindowsHookEx**](setwindowshookex.md) function. The system calls this function whenever the [**GetMessage**](/windows/win32/Winuser/nf-engextcpp-extexception-getmessage?branch=master) or [**PeekMessage**](peekmessage.md) function has retrieved a message from an application message queue. Before returning the retrieved message to the caller, the system passes the message to the hook procedure. <br/>                                                                                                                                                        |
| [*JournalPlaybackProc*](journalplaybackproc.md)   | An application-defined or library-defined callback function used with the [**SetWindowsHookEx**](setwindowshookex.md) function. Typically, an application uses this function to play back a series of mouse and keyboard messages recorded previously by the [*JournalRecordProc*](journalrecordproc.md) hook procedure. As long as a [*JournalPlaybackProc*](journalplaybackproc.md) hook procedure is installed, regular mouse and keyboard input is disabled. <br/>                                                                                                                       |
| [*JournalRecordProc*](journalrecordproc.md)       | An application-defined or library-defined callback function used with the [**SetWindowsHookEx**](setwindowshookex.md) function. The function records messages the system removes from the system message queue. Later, an application can use a [*JournalPlaybackProc*](journalplaybackproc.md) hook procedure to play back the messages. <br/>                                                                                                                                                                                                                                               |
| [*KeyboardProc*](keyboardproc.md)                 | An application-defined or library-defined callback function used with the [**SetWindowsHookEx**](setwindowshookex.md) function. The system calls this function whenever an application calls the [**GetMessage**](/windows/win32/Winuser/nf-engextcpp-extexception-getmessage?branch=master) or [**PeekMessage**](peekmessage.md) function and there is a keyboard message ([**WM\_KEYUP**](https://msdn.microsoft.com/library/windows/desktop/ms646281) or [**WM\_KEYDOWN**](https://msdn.microsoft.com/library/windows/desktop/ms646280)) to be processed. <br/>                                                                                                                                                                         |
| [*LowLevelKeyboardProc*](lowlevelkeyboardproc.md) | An application-defined or library-defined callback function used with the [**SetWindowsHookEx**](setwindowshookex.md) function. The system calls this function every time a new keyboard input event is about to be posted into a thread input queue.<br/>                                                                                                                                                                                                                                                                                                                                     |
| [*LowLevelMouseProc*](lowlevelmouseproc.md)       | An application-defined or library-defined callback function used with the [**SetWindowsHookEx**](setwindowshookex.md) function. The system calls this function every time a new mouse input event is about to be posted into a thread input queue.<br/>                                                                                                                                                                                                                                                                                                                                        |
| [*MessageProc*](messageproc.md)                   | An application-defined or library-defined callback function used with the [**SetWindowsHookEx**](setwindowshookex.md) function. The system calls this function after an input event occurs in a dialog box, message box, menu, or scroll bar, but before the message generated by the input event is processed. The hook procedure can monitor messages for a dialog box, message box, menu, or scroll bar created by a particular application or all applications.<br/>                                                                                                                       |
| [*MouseProc*](mouseproc.md)                       | An application-defined or library-defined callback function used with the [**SetWindowsHookEx**](setwindowshookex.md) function. The system calls this function whenever an application calls the [**GetMessage**](/windows/win32/Winuser/nf-engextcpp-extexception-getmessage?branch=master) or [**PeekMessage**](peekmessage.md) function and there is a mouse message to be processed. <br/>                                                                                                                                                                                                                                                           |
| [**SetWindowsHookEx**](setwindowshookex.md)       | Installs an application-defined hook procedure into a hook chain. You would install a hook procedure to monitor the system for certain types of events. These events are associated either with a specific thread or with all threads in the same desktop as the calling thread.<br/>                                                                                                                                                                                                                                                                                                           |
| [*ShellProc*](shellproc.md)                       | An application-defined or library-defined callback function used with the [**SetWindowsHookEx**](setwindowshookex.md) function. The function receives notifications of Shell events from the system.<br/>                                                                                                                                                                                                                                                                                                                                                                                      |
| [*SysMsgProc*](sysmsgproc.md)                     | An application-defined or library-defined callback function used with the [**SetWindowsHookEx**](setwindowshookex.md) function. The system calls this function after an input event occurs in a dialog box, message box, menu, or scroll bar, but before the message generated by the input event is processed. The function can monitor messages for any dialog box, message box, menu, or scroll bar in the system. <br/>                                                                                                                                                                    |
| [**UnhookWindowsHookEx**](unhookwindowshookex.md) | Removes a hook procedure installed in a hook chain by the [**SetWindowsHookEx**](setwindowshookex.md) function. <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |



 

### Hook Notifications



| Name                                          | Description                                                                                                                                                                         |
|-----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WM\_CANCELJOURNAL**](wm-canceljournal.md) | Posted to an application when a user cancels the application's journaling activities. The message is posted with a **NULL** window handle. <br/>                              |
| [**WM\_QUEUESYNC**](wm-queuesync.md)         | Sent by a CBT application to separate user-input messages from other messages sent through the [**WH\_JOURNALPLAYBACK**](about-hooks.md#wh-journalplayback) procedure. <br/> |



 

### Hook Structures



| Name                                           | Description                                                                                                                                                                                                                 |
|------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CBT\_CREATEWND**](cbt-createwnd.md)        | Contains information passed to a **WH\_CBT** hook procedure, [*CBTProc*](cbtproc.md), before a window is created.<br/>                                                                                               |
| [**CBTACTIVATESTRUCT**](cbtactivatestruct.md) | Contains information passed to a **WH\_CBT** hook procedure, [*CBTProc*](cbtproc.md), before a window is activated. <br/>                                                                                            |
| [**CWPRETSTRUCT**](cwpretstruct.md)           | Defines the message parameters passed to a **WH\_CALLWNDPROCRET** hook procedure, [*CallWndRetProc*](callwndretproc.md). <br/>                                                                                       |
| [**CWPSTRUCT**](cwpstruct.md)                 | Defines the message parameters passed to a **WH\_CALLWNDPROC** hook procedure, [*CallWndProc*](callwndproc.md). <br/>                                                                                                |
| [**DEBUGHOOKINFO**](debughookinfo.md)         | Contains debugging information passed to a **WH\_DEBUG** hook procedure, [*DebugProc*](debugproc.md). <br/>                                                                                                          |
| [**EVENTMSG**](eventmsg.md)                   | Contains information about a hardware message sent to the system message queue. This structure is used to store message information for the [*JournalPlaybackProc*](journalplaybackproc.md) callback function. <br/> |
| [**KBDLLHOOKSTRUCT**](kbdllhookstruct.md)     | Contains information about a low-level keyboard input event. <br/>                                                                                                                                                    |
| [**MOUSEHOOKSTRUCT**](mousehookstruct.md)     | Contains information about a mouse event passed to a **WH\_MOUSE** hook procedure, [*MouseProc*](mouseproc.md). <br/>                                                                                                |
| [**MOUSEHOOKSTRUCTEX**](mousehookstructex.md) | Contains information about a mouse event passed to a **WH\_MOUSE** hook procedure, [*MouseProc*](mouseproc.md). <br/>                                                                                                |
| [**MSLLHOOKSTRUCT**](msllhookstruct.md)       | Contains information about a low-level mouse input event. <br/>                                                                                                                                                       |



 

## Related topics

<dl> <dt>

[**SetWinEventHook**](https://msdn.microsoft.com/library/windows/desktop/dd373640)
</dt> </dl>

 

 




