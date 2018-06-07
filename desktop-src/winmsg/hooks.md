---
Description: This section discusses hooks. A hook is a point in the system message-handling mechanism where an application can install a subroutine to monitor the message traffic.
ms.assetid: 9ced0ac4-e602-425f-b954-6af9c741699a
title: Hooks
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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
| [**CallMsgFilter**](/windows/desktop/api/Winuser/nf-winuser-callmsgfiltera)             | Passes the specified message and hook code to the hook procedures associated with the [**WH\_SYSMSGFILTER**](about-hooks.md) and **WH\_MSGFILTER** hook procedures.<br/>                                                                                                                                                                                                                                                                                                                                                                                      |
| [**CallNextHookEx**](/windows/desktop/api/Winuser/nf-winuser-callnexthookex)           | Passes the hook information to the next hook procedure in the current hook chain. A hook procedure can call this function either before or after processing the hook information. <br/>                                                                                                                                                                                                                                                                                                                                                                                                         |
| [*CallWndProc*](https://www.bing.com/search?q=*CallWndProc*)                   | An application-defined or library-defined callback function used with the [**SetWindowsHookEx**](/windows/desktop/api/Winuser/nf-winuser-setwindowshookexa) function. The system calls this function before calling the window procedure to process a message sent to the thread.<br/>                                                                                                                                                                                                                                                                                                                                               |
| [*CallWndRetProc*](https://www.bing.com/search?q=*CallWndRetProc*)             | An application-defined or library-defined callback function used with the [**SetWindowsHookEx**](/windows/desktop/api/Winuser/nf-winuser-setwindowshookexa) function. The system calls this function after the [**SendMessage**](/windows/desktop/api/Winuser/nf-winuser-insendmessage) function is called. The hook procedure can examine the message; it cannot modify it. <br/>                                                                                                                                                                                                                                                                                         |
| [*CBTProc*](https://www.bing.com/search?q=*CBTProc*)                           | An application-defined or library-defined callback function used with the [**SetWindowsHookEx**](/windows/desktop/api/Winuser/nf-winuser-setwindowshookexa) function. The system calls this function before activating, creating, destroying, minimizing, maximizing, moving, or sizing a window; before completing a system command; before removing a mouse or keyboard event from the system message queue; before setting the keyboard focus; or before synchronizing with the system message queue. A computer-based training (CBT) application uses this hook procedure to receive useful notifications from the system. <br/> |
| [*DebugProc*](https://www.bing.com/search?q=*DebugProc*)                       | An application-defined or library-defined callback function used with the [**SetWindowsHookEx**](/windows/desktop/api/Winuser/nf-winuser-setwindowshookexa) function. The system calls this function before calling the hook procedures associated with any type of hook. The system passes information about the hook to be called to the [*DebugProc*](https://www.bing.com/search?q=*DebugProc*) hook procedure, which examines the information and determines whether to allow the hook to be called. <br/>                                                                                                                                                  |
| [*ForegroundIdleProc*](https://www.bing.com/search?q=*ForegroundIdleProc*)     | An application-defined or library-defined callback function used with the [**SetWindowsHookEx**](/windows/desktop/api/Winuser/nf-winuser-setwindowshookexa) function. The system calls this function whenever the foreground thread is about to become idle. <br/>                                                                                                                                                                                                                                                                                                                                                                   |
| [*GetMsgProc*](https://www.bing.com/search?q=*GetMsgProc*)                     | An application-defined or library-defined callback function used with the [**SetWindowsHookEx**](/windows/desktop/api/Winuser/nf-winuser-setwindowshookexa) function. The system calls this function whenever the [**GetMessage**](/windows/desktop/api/Winuser/nf-winuser-getmessage) or [**PeekMessage**](/windows/desktop/api/Winuser/nf-winuser-peekmessagea) function has retrieved a message from an application message queue. Before returning the retrieved message to the caller, the system passes the message to the hook procedure. <br/>                                                                                                                                                        |
| [*JournalPlaybackProc*](https://www.bing.com/search?q=*JournalPlaybackProc*)   | An application-defined or library-defined callback function used with the [**SetWindowsHookEx**](/windows/desktop/api/Winuser/nf-winuser-setwindowshookexa) function. Typically, an application uses this function to play back a series of mouse and keyboard messages recorded previously by the [*JournalRecordProc*](https://www.bing.com/search?q=*JournalRecordProc*) hook procedure. As long as a [*JournalPlaybackProc*](https://www.bing.com/search?q=*JournalPlaybackProc*) hook procedure is installed, regular mouse and keyboard input is disabled. <br/>                                                                                                                       |
| [*JournalRecordProc*](https://www.bing.com/search?q=*JournalRecordProc*)       | An application-defined or library-defined callback function used with the [**SetWindowsHookEx**](/windows/desktop/api/Winuser/nf-winuser-setwindowshookexa) function. The function records messages the system removes from the system message queue. Later, an application can use a [*JournalPlaybackProc*](https://www.bing.com/search?q=*JournalPlaybackProc*) hook procedure to play back the messages. <br/>                                                                                                                                                                                                                                               |
| [*KeyboardProc*](https://www.bing.com/search?q=*KeyboardProc*)                 | An application-defined or library-defined callback function used with the [**SetWindowsHookEx**](/windows/desktop/api/Winuser/nf-winuser-setwindowshookexa) function. The system calls this function whenever an application calls the [**GetMessage**](/windows/desktop/api/Winuser/nf-winuser-getmessage) or [**PeekMessage**](/windows/desktop/api/Winuser/nf-winuser-peekmessagea) function and there is a keyboard message ([**WM\_KEYUP**](https://msdn.microsoft.com/library/windows/desktop/ms646281) or [**WM\_KEYDOWN**](https://msdn.microsoft.com/library/windows/desktop/ms646280)) to be processed. <br/>                                                                                                                                                                         |
| [*LowLevelKeyboardProc*](https://www.bing.com/search?q=*LowLevelKeyboardProc*) | An application-defined or library-defined callback function used with the [**SetWindowsHookEx**](/windows/desktop/api/Winuser/nf-winuser-setwindowshookexa) function. The system calls this function every time a new keyboard input event is about to be posted into a thread input queue.<br/>                                                                                                                                                                                                                                                                                                                                     |
| [*LowLevelMouseProc*](https://www.bing.com/search?q=*LowLevelMouseProc*)       | An application-defined or library-defined callback function used with the [**SetWindowsHookEx**](/windows/desktop/api/Winuser/nf-winuser-setwindowshookexa) function. The system calls this function every time a new mouse input event is about to be posted into a thread input queue.<br/>                                                                                                                                                                                                                                                                                                                                        |
| [*MessageProc*](/windows/desktop/api/Winuser/nc-dbghelp-psymbolservermessageproc)                   | An application-defined or library-defined callback function used with the [**SetWindowsHookEx**](/windows/desktop/api/Winuser/nf-winuser-setwindowshookexa) function. The system calls this function after an input event occurs in a dialog box, message box, menu, or scroll bar, but before the message generated by the input event is processed. The hook procedure can monitor messages for a dialog box, message box, menu, or scroll bar created by a particular application or all applications.<br/>                                                                                                                       |
| [*MouseProc*](https://www.bing.com/search?q=*MouseProc*)                       | An application-defined or library-defined callback function used with the [**SetWindowsHookEx**](/windows/desktop/api/Winuser/nf-winuser-setwindowshookexa) function. The system calls this function whenever an application calls the [**GetMessage**](/windows/desktop/api/Winuser/nf-winuser-getmessage) or [**PeekMessage**](/windows/desktop/api/Winuser/nf-winuser-peekmessagea) function and there is a mouse message to be processed. <br/>                                                                                                                                                                                                                                                           |
| [**SetWindowsHookEx**](/windows/desktop/api/Winuser/nf-winuser-setwindowshookexa)       | Installs an application-defined hook procedure into a hook chain. You would install a hook procedure to monitor the system for certain types of events. These events are associated either with a specific thread or with all threads in the same desktop as the calling thread.<br/>                                                                                                                                                                                                                                                                                                           |
| [*ShellProc*](https://www.bing.com/search?q=*ShellProc*)                       | An application-defined or library-defined callback function used with the [**SetWindowsHookEx**](/windows/desktop/api/Winuser/nf-winuser-setwindowshookexa) function. The function receives notifications of Shell events from the system.<br/>                                                                                                                                                                                                                                                                                                                                                                                      |
| [*SysMsgProc*](https://www.bing.com/search?q=*SysMsgProc*)                     | An application-defined or library-defined callback function used with the [**SetWindowsHookEx**](/windows/desktop/api/Winuser/nf-winuser-setwindowshookexa) function. The system calls this function after an input event occurs in a dialog box, message box, menu, or scroll bar, but before the message generated by the input event is processed. The function can monitor messages for any dialog box, message box, menu, or scroll bar in the system. <br/>                                                                                                                                                                    |
| [**UnhookWindowsHookEx**](/windows/desktop/api/Winuser/nf-winuser-unhookwindowshookex) | Removes a hook procedure installed in a hook chain by the [**SetWindowsHookEx**](/windows/desktop/api/Winuser/nf-winuser-setwindowshookexa) function. <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |



 

### Hook Notifications



| Name                                          | Description                                                                                                                                                                         |
|-----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WM\_CANCELJOURNAL**](wm-canceljournal.md) | Posted to an application when a user cancels the application's journaling activities. The message is posted with a **NULL** window handle. <br/>                              |
| [**WM\_QUEUESYNC**](wm-queuesync.md)         | Sent by a CBT application to separate user-input messages from other messages sent through the [**WH\_JOURNALPLAYBACK**](about-hooks.md) procedure. <br/> |



 

### Hook Structures



| Name                                           | Description                                                                                                                                                                                                                 |
|------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CBT\_CREATEWND**](/windows/desktop/api/Winuser/ns-winuser-tagcbt_createwnda)        | Contains information passed to a **WH\_CBT** hook procedure, [*CBTProc*](https://www.bing.com/search?q=*CBTProc*), before a window is created.<br/>                                                                                               |
| [**CBTACTIVATESTRUCT**](/windows/desktop/api/Winuser/ns-winuser-tagcbtactivatestruct) | Contains information passed to a **WH\_CBT** hook procedure, [*CBTProc*](https://www.bing.com/search?q=*CBTProc*), before a window is activated. <br/>                                                                                            |
| [**CWPRETSTRUCT**](/windows/desktop/api/Winuser/ns-winuser-tagcwpretstruct)           | Defines the message parameters passed to a **WH\_CALLWNDPROCRET** hook procedure, [*CallWndRetProc*](https://www.bing.com/search?q=*CallWndRetProc*). <br/>                                                                                       |
| [**CWPSTRUCT**](/windows/desktop/api/Winuser/ns-winuser-tagcwpstruct)                 | Defines the message parameters passed to a **WH\_CALLWNDPROC** hook procedure, [*CallWndProc*](https://www.bing.com/search?q=*CallWndProc*). <br/>                                                                                                |
| [**DEBUGHOOKINFO**](/windows/desktop/api/Winuser/ns-winuser-tagdebughookinfo)         | Contains debugging information passed to a **WH\_DEBUG** hook procedure, [*DebugProc*](https://www.bing.com/search?q=*DebugProc*). <br/>                                                                                                          |
| [**EVENTMSG**](/windows/desktop/api/Winuser/ns-winuser-tageventmsg)                   | Contains information about a hardware message sent to the system message queue. This structure is used to store message information for the [*JournalPlaybackProc*](https://www.bing.com/search?q=*JournalPlaybackProc*) callback function. <br/> |
| [**KBDLLHOOKSTRUCT**](/windows/desktop/api/Winuser/ns-winuser-tagkbdllhookstruct)     | Contains information about a low-level keyboard input event. <br/>                                                                                                                                                    |
| [**MOUSEHOOKSTRUCT**](/windows/desktop/api/Winuser/ns-winuser-tagmousehookstruct)     | Contains information about a mouse event passed to a **WH\_MOUSE** hook procedure, [*MouseProc*](https://www.bing.com/search?q=*MouseProc*). <br/>                                                                                                |
| [**MOUSEHOOKSTRUCTEX**](/windows/desktop/api/Winuser/ns-winuser-tagmousehookstructex) | Contains information about a mouse event passed to a **WH\_MOUSE** hook procedure, [*MouseProc*](https://www.bing.com/search?q=*MouseProc*). <br/>                                                                                                |
| [**MSLLHOOKSTRUCT**](/windows/desktop/api/Winuser/ns-winuser-tagmsllhookstruct)       | Contains information about a low-level mouse input event. <br/>                                                                                                                                                       |



 

## Related topics

<dl> <dt>

[**SetWinEventHook**](https://msdn.microsoft.com/library/windows/desktop/dd373640)
</dt> </dl>

 

 




