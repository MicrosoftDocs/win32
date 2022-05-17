---
description: This topic discusses how hooks should be used.
ms.assetid: 9ced0ac4-e602-425f-b954-6af9c741699a
title: Hooks Overview
ms.topic: article
ms.date: 05/31/2018
---

# Hooks Overview

A *hook* is a mechanism by which an application can intercept events, such as messages, mouse actions, and keystrokes. A function that intercepts a particular type of event is known as a *hook procedure*. A hook procedure can act on each event it receives, and then modify or discard the event.

The following some example uses for hooks:

-   Monitor messages for debugging purposes
-   Provide support for recording and playback of macros
-   Provide support for a help key (F1)
-   Simulate mouse and keyboard input
-   Implement a computer-based training (CBT) application

> [!Note]  
> Hooks tend to slow down the system because they increase the amount of processing the system must perform for each message. You should install a hook only when necessary, and remove it as soon as possible.

 

This section discusses the following:

-   [Hook Chains](#hook-chains)
-   [Hook Procedures](#hook-procedures)
-   [Hook Types](#hook-types)
    -   [WH\_CALLWNDPROC and WH\_CALLWNDPROCRET](#wh_callwndproc-and-wh_callwndprocret)
    -   [WH\_CBT](#wh_cbt)
    -   [WH\_DEBUG](#wh_debug)
    -   [WH\_FOREGROUNDIDLE](#wh_foregroundidle)
    -   [WH\_GETMESSAGE](#wh_getmessage)
    -   [WH\_JOURNALPLAYBACK](#wh_journalplayback)
    -   [WH\_JOURNALRECORD](#wh_journalrecord)
    -   [WH\_KEYBOARD\_LL](#wh_keyboard_ll)
    -   [WH\_KEYBOARD](#wh_keyboard)
    -   [WH\_MOUSE\_LL](#wh_mouse_ll)
    -   [WH\_MOUSE](#wh_mouse)
    -   [WH\_MSGFILTER and WH\_SYSMSGFILTER](#wh_msgfilter-and-wh_sysmsgfilter)
    -   [WH\_SHELL](#wh_shell)

## Hook Chains

The system supports many different types of hooks; each type provides access to a different aspect of its message-handling mechanism. For example, an application can use the [WH\_MOUSE](#wh_mouse) hook to monitor the message traffic for mouse messages.

The system maintains a separate hook chain for each type of hook. A *hook chain* is a list of pointers to special, application-defined callback functions called *hook procedures*. When a message occurs that is associated with a particular type of hook, the system passes the message to each hook procedure referenced in the hook chain, one after the other. The action a hook procedure can take depends on the type of hook involved. The hook procedures for some types of hooks can only monitor messages; others can modify messages or stop their progress through the chain, preventing them from reaching the next hook procedure or the destination window.

## Hook Procedures

To take advantage of a particular type of hook, the developer provides a hook procedure and uses the [**SetWindowsHookEx**](/windows/win32/api/winuser/nf-winuser-setwindowshookexa) function to install it into the chain associated with the hook. A hook procedure must have the following syntax:

``` syntax
LRESULT CALLBACK HookProc(
  int nCode, 
  WPARAM wParam, 
  LPARAM lParam
)
{
   // process event
   ...

   return CallNextHookEx(NULL, nCode, wParam, lParam);
}
```

*HookProc* is a placeholder for an application-defined name.

The *nCode* parameter is a hook code that the hook procedure uses to determine the action to perform. The value of the hook code depends on the type of the hook; each type has its own characteristic set of hook codes. The values of the *wParam* and *lParam* parameters depend on the hook code, but they typically contain information about a message that was sent or posted.

The [**SetWindowsHookEx**](/windows/win32/api/winuser/nf-winuser-setwindowshookexa) function always installs a hook procedure at the beginning of a hook chain. When an event occurs that is monitored by a particular type of hook, the system calls the procedure at the beginning of the hook chain associated with the hook. Each hook procedure in the chain determines whether to pass the event to the next procedure. A hook procedure passes an event to the next procedure by calling the [**CallNextHookEx**](/windows/win32/api/winuser/nf-winuser-callnexthookex) function.

Note that the hook procedures for some types of hooks can only monitor messages. the system passes messages to each hook procedure, regardless of whether a particular procedure calls [**CallNextHookEx**](/windows/win32/api/winuser/nf-winuser-callnexthookex).

A *global hook* monitors messages for all threads in the same desktop as the calling thread. A *thread-specific hook* monitors messages for only an individual thread. A global hook procedure can be called in the context of any application in the same desktop as the calling thread, so the procedure must be in a separate DLL module. A thread-specific hook procedure is called only in the context of the associated thread. If an application installs a hook procedure for one of its own threads, the hook procedure can be in either the same module as the rest of the application's code or in a DLL. If the application installs a hook procedure for a thread of a different application, the procedure must be in a DLL. For information, see [Dynamic-Link Libraries](../dlls/dynamic-link-libraries.md).

> [!Note]  
> You should use global hooks only for debugging purposes; otherwise, you should avoid them. Global hooks hurt system performance and cause conflicts with other applications that implement the same type of global hook.

 

## Hook Types

Each type of hook enables an application to monitor a different aspect of the system's message-handling mechanism. The following sections describe the available hooks.

-   [WH\_CALLWNDPROC and WH\_CALLWNDPROCRET](#wh_callwndproc-and-wh_callwndprocret)
-   [WH\_CBT](#wh_cbt)
-   [WH\_DEBUG](#wh_debug)
-   [WH\_FOREGROUNDIDLE](#wh_foregroundidle)
-   [WH\_GETMESSAGE](#wh_getmessage)
-   [WH\_JOURNALPLAYBACK](#wh_journalplayback)
-   [WH\_JOURNALRECORD](#wh_journalrecord)
-   [WH\_KEYBOARD\_LL](#wh_keyboard_ll)
-   [WH\_KEYBOARD](#wh_keyboard)
-   [WH\_MOUSE\_LL](#wh_mouse_ll)
-   [WH\_MOUSE](#wh_mouse)
-   [WH\_MSGFILTER and WH\_SYSMSGFILTER](#wh_msgfilter-and-wh_sysmsgfilter)
-   [WH\_SHELL](#wh_shell)

### WH\_CALLWNDPROC and WH\_CALLWNDPROCRET

The **WH\_CALLWNDPROC** and **WH\_CALLWNDPROCRET** hooks enable you to monitor messages sent to window procedures. The system calls a **WH\_CALLWNDPROC** hook procedure before passing the message to the receiving window procedure, and calls the **WH\_CALLWNDPROCRET** hook procedure after the window procedure has processed the message.

The **WH\_CALLWNDPROCRET** hook passes a pointer to a [**CWPRETSTRUCT**](/windows/win32/api/winuser/ns-winuser-cwpretstruct) structure to the hook procedure. The structure contains the return value from the window procedure that processed the message, as well as the message parameters associated with the message. Subclassing the window does not work for messages set between processes.

For more information, see the [*CallWndProc*](/previous-versions/windows/desktop/legacy/ms644975(v=vs.85)) and [*CallWndRetProc*](/windows/win32/api/winuser/nc-winuser-hookproc) callback functions.

### WH\_CBT

The system calls a **WH\_CBT** hook procedure before activating, creating, destroying, minimizing, maximizing, moving, or sizing a window; before completing a system command; before removing a mouse or keyboard event from the system message queue; before setting the input focus; or before synchronizing with the system message queue. The value the hook procedure returns determines whether the system allows or prevents one of these operations. The **WH\_CBT** hook is intended primarily for computer-based training (CBT) applications.

For more information, see the [*CBTProc*](/previous-versions/windows/desktop/legacy/ms644977(v=vs.85)) callback function.

For information, see [WinEvents](/windows/desktop/WinAuto/winevents-infrastructure).

### WH\_DEBUG

The system calls a **WH\_DEBUG** hook procedure before calling hook procedures associated with any other hook in the system. You can use this hook to determine whether to allow the system to call hook procedures associated with other types of hooks.

For more information, see the [*DebugProc*](/previous-versions/windows/desktop/legacy/ms644978(v=vs.85)) callback function.

### WH\_FOREGROUNDIDLE

The **WH\_FOREGROUNDIDLE** hook enables you to perform low priority tasks during times when its foreground thread is idle. The system calls a **WH\_FOREGROUNDIDLE** hook procedure when the application's foreground thread is about to become idle.

For more information, see the [*ForegroundIdleProc*](/previous-versions/windows/desktop/legacy/ms644980(v=vs.85)) callback function.

### WH\_GETMESSAGE

The **WH\_GETMESSAGE** hook enables an application to monitor messages about to be returned by the [**GetMessage**](/windows/win32/api/winuser/nf-winuser-getmessage) or [**PeekMessage**](/windows/win32/api/winuser/nf-winuser-peekmessagea) function. You can use the **WH\_GETMESSAGE** hook to monitor mouse and keyboard input and other messages posted to the message queue.

For more information, see the [*GetMsgProc*](/previous-versions/windows/desktop/legacy/ms644981(v=vs.85)) callback function.

### WH\_JOURNALPLAYBACK

> [!WARNING]
> Journaling Hooks APIs are unsupported starting in Windows 11 and will be removed in a future release. Because of this, we highly recommend calling the [**SendInput**](https://docs.microsoft.com/windows/win32/api/winuser/nf-winuser-sendinput) TextInput API instead.

The **WH\_JOURNALPLAYBACK** hook enables an application to insert messages into the system message queue. You can use this hook to play back a series of mouse and keyboard events recorded earlier by using [WH\_JOURNALRECORD](#wh_journalrecord). Regular mouse and keyboard input is disabled as long as a **WH\_JOURNALPLAYBACK** hook is installed. A **WH\_JOURNALPLAYBACK** hook is a global hook—it cannot be used as a thread-specific hook.

The **WH\_JOURNALPLAYBACK** hook returns a time-out value. This value tells the system how many milliseconds to wait before processing the current message from the playback hook. This enables the hook to control the timing of the events it plays back.

For more information, see the [*JournalPlaybackProc*](/previous-versions/windows/desktop/legacy/ms644982(v=vs.85)) callback function.

### WH\_JOURNALRECORD

> [!WARNING]
> Journaling Hooks APIs are unsupported starting in Windows 11 and will be removed in a future release. Because of this, we highly recommend calling the [**SendInput**](https://docs.microsoft.com/windows/win32/api/winuser/nf-winuser-sendinput) TextInput API instead.

The **WH\_JOURNALRECORD** hook enables you to monitor and record input events. Typically, you use this hook to record a sequence of mouse and keyboard events to play back later by using [WH\_JOURNALPLAYBACK](#wh_journalplayback). The **WH\_JOURNALRECORD** hook is a global hook—it cannot be used as a thread-specific hook.

For more information, see the [*JournalRecordProc*](/previous-versions/windows/desktop/legacy/ms644983(v=vs.85)) callback function.

### WH\_KEYBOARD\_LL

The **WH\_KEYBOARD\_LL** hook enables you to monitor keyboard input events about to be posted in a thread input queue.

For more information, see the [*LowLevelKeyboardProc*](/previous-versions/windows/desktop/legacy/ms644985(v=vs.85)) callback function.

### WH\_KEYBOARD

The **WH\_KEYBOARD** hook enables an application to monitor message traffic for [**WM\_KEYDOWN**](/windows/desktop/inputdev/wm-keydown) and [**WM\_KEYUP**](/windows/desktop/inputdev/wm-keyup) messages about to be returned by the [**GetMessage**](/windows/win32/api/winuser/nf-winuser-getmessage) or [**PeekMessage**](/windows/win32/api/winuser/nf-winuser-peekmessagea) function. You can use the **WH\_KEYBOARD** hook to monitor keyboard input posted to a message queue.

For more information, see the [*KeyboardProc*](/previous-versions/windows/desktop/legacy/ms644984(v=vs.85)) callback function.

### WH\_MOUSE\_LL

The **WH\_MOUSE\_LL** hook enables you to monitor mouse input events about to be posted in a thread input queue.

For more information, see the [*LowLevelMouseProc*](/previous-versions/windows/desktop/legacy/ms644986(v=vs.85)) callback function.

### WH\_MOUSE

The **WH\_MOUSE** hook enables you to monitor mouse messages about to be returned by the [**GetMessage**](/windows/win32/api/winuser/nf-winuser-getmessage) or [**PeekMessage**](/windows/win32/api/winuser/nf-winuser-peekmessagea) function. You can use the **WH\_MOUSE** hook to monitor mouse input posted to a message queue.

For more information, see the [*MouseProc*](/previous-versions/windows/desktop/legacy/ms644988(v=vs.85)) callback function.

### WH\_MSGFILTER and WH\_SYSMSGFILTER

The **WH\_MSGFILTER** and **WH\_SYSMSGFILTER** hooks enable you to monitor messages about to be processed by a menu, scroll bar, message box, or dialog box, and to detect when a different window is about to be activated as a result of the user's pressing the ALT+TAB or ALT+ESC key combination. The **WH\_MSGFILTER** hook can only monitor messages passed to a menu, scroll bar, message box, or dialog box created by the application that installed the hook procedure. The **WH\_SYSMSGFILTER** hook monitors such messages for all applications.

The **WH\_MSGFILTER** and **WH\_SYSMSGFILTER** hooks enable you to perform message filtering during modal loops that is equivalent to the filtering done in the main message loop. For example, an application often examines a new message in the main loop between the time it retrieves the message from the queue and the time it dispatches the message, performing special processing as appropriate. However, during a modal loop, the system retrieves and dispatches messages without allowing an application the chance to filter the messages in its main message loop. If an application installs a **WH\_MSGFILTER** or **WH\_SYSMSGFILTER** hook procedure, the system calls the procedure during the modal loop.

An application can call the **WH\_MSGFILTER** hook directly by calling the [**CallMsgFilter**](/windows/win32/api/winuser/nf-winuser-callmsgfiltera) function. By using this function, the application can use the same code to filter messages during modal loops as it uses in the main message loop. To do so, encapsulate the filtering operations in a **WH\_MSGFILTER** hook procedure and call **CallMsgFilter** between the calls to the [**GetMessage**](/windows/win32/api/winuser/nf-winuser-getmessage) and [**DispatchMessage**](/windows/win32/api/winuser/nf-winuser-dispatchmessage) functions.

``` syntax
while (GetMessage(&msg, (HWND) NULL, 0, 0)) 
{ 
    if (!CallMsgFilter(&qmsg, 0)) 
        DispatchMessage(&qmsg); 
} 
```

The last argument of [**CallMsgFilter**](/windows/win32/api/winuser/nf-winuser-callmsgfiltera) is simply passed to the hook procedure; you can enter any value. The hook procedure, by defining a constant such as **MSGF\_MAINLOOP**, can use this value to determine where the procedure was called from.

For more information, see the [*MessageProc*](/previous-versions/windows/desktop/legacy/ms644987(v=vs.85)) and [*SysMsgProc*](/previous-versions/windows/desktop/legacy/ms644992(v=vs.85)) callback functions.

### WH\_SHELL

A shell application can use the **WH\_SHELL** hook to receive important notifications. The system calls a **WH\_SHELL** hook procedure when the shell application is about to be activated and when a top-level window is created or destroyed.

Note that custom shell applications do not receive **WH\_SHELL** messages. Therefore, any application that registers itself as the default shell must call the [**SystemParametersInfo**](/windows/desktop/api/winuser/nf-winuser-systemparametersinfoa) function before it (or any other application) can receive **WH\_SHELL** messages. This function must be called with **SPI\_SETMINIMIZEDMETRICS** and a [**MINIMIZEDMETRICS**](/windows/win32/api/winuser/ns-winuser-minimizedmetrics) structure. Set the **iArrange** member of this structure to **ARW\_HIDE**.

For more information, see the [*ShellProc*](/previous-versions/windows/desktop/legacy/ms644991(v=vs.85)) callback function.

 

 
