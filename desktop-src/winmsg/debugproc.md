---
title: DebugProc function (Windows)
description: The system passes information about the hook to be called to the DebugProc hook procedure, which examines the information and determines whether to allow the hook to be called.
ms.date: 06/28/2023
ms.topic: reference
f1_keywords:
- DebugProc
- WH_MOUSE
- WH_GETMESSAGE
- WH_JOURNALPLAYBACK
- WH_CALLWNDPROC
- WH_CBT
- WH_DEBUG
- WH_CALLWNDPROCRET
- WH_JOURNALRECORD
- WH_SHELL
- WH_KEYBOARD
- WH_SYSMSGFILTER
- WH_MSGFILTER
- winuser/DebugProc
dev_langs:
- C++
- C
api_location:
- Winuser.h
api_name:
- DebugProc
api_type:
- HeaderDef
product:
- Windows
topic_type:
- apiref
- kbSyntax
product_family_name: VS
ROBOTS: INDEX,FOLLOW
---

# DebugProc function

An application-defined or library-defined callback function used with the [**SetWindowsHookExA**](/windows/win32/api/winuser/nf-winuser-setwindowshookexa)/[**SetWindowsHookExW**](/windows/win32/api/winuser/nf-winuser-setwindowshookexw) function. The system calls this function before calling the hook procedures associated with any type of hook. The system passes information about the hook to be called to the *DebugProc* hook procedure, which examines the information and determines whether to allow the hook to be called.

The **HOOKPROC** type defines a pointer to this callback function. *DebugProc* is a placeholder for the application-defined or library-defined function name.

## Syntax

``` c++
LRESULT CALLBACK DebugProc(
  _In_ int    nCode,
  _In_ WPARAM wParam,
  _In_ LPARAM lParam
);
```

## Parameters

  - *nCode* \[in\]  
    Type: **int**
    
    Specifies whether the hook procedure must process the message. If *nCode* is HC\_ACTION, the hook procedure must process the message. If *nCode* is less than zero, the hook procedure must pass the message to the [**CallNextHookEx**](/windows/win32/api/winuser/nf-winuser-callnexthookex) function without further processing and should return the value returned by **CallNextHookEx**.

  - *wParam* \[in\]  
    Type: **WPARAM**
    
    The type of hook about to be called. This parameter can be one of the following values.
    
    <table>
    <colgroup>
    <col />
    <col />
    </colgroup>
    <thead>
    <tr class="header">
    <th>Value</th>
    <th>Meaning</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><span id="WH_CALLWNDPROC"></span><span id="wh_callwndproc"></span>
    <strong>WH_CALLWNDPROC</strong>
    4</td>
    <td><p>Installs a hook procedure that monitors messages sent to a window procedure. For more information, see the description of the [*CallWndProc*](callwndproc.md) hook procedure.</p></td>
    </tr>
    <tr class="even">
    <td><span id="WH_CALLWNDPROCRET"></span><span id="wh_callwndprocret"></span>
    <strong>WH_CALLWNDPROCRET</strong>
    12</td>
    <td><p>Installs a hook procedure that monitors messages that have just been processed by a window procedure. For more information, see the description of the <a href="/windows/win32/api/winuser/nc-winuser-hookproc"><em>CallWndRetProc</em></a> hook procedure.</p></td>
    </tr>
    <tr class="odd">
    <td><span id="WH_CBT"></span><span id="wh_cbt"></span>
    <strong>WH_CBT</strong>
    5</td>
    <td><p>Installs a hook procedure that receives notifications useful to a CBT application. For more information, see the description of the [**CBTProc**](cbtproc.md) hook procedure.</p></td>
    </tr>
    <tr class="even">
    <td><span id="WH_DEBUG"></span><span id="wh_debug"></span>
    <strong>WH_DEBUG</strong>
    9</td>
    <td><p>Installs a hook procedure useful for debugging other hook procedures. For more information, see the description of the <em>DebugProc</em> hook procedure.</p></td>
    </tr>
    <tr class="odd">
    <td><span id="WH_GETMESSAGE"></span><span id="wh_getmessage"></span>
    <strong>WH_GETMESSAGE</strong>
    3</td>
    <td><p>

Installs a hook procedure that monitors messages posted to a message queue. For more information, see the description of the[*GetMsgProc*](getmsgproc.md) hook procedure.

</p></td>
    </tr>
    <tr class="even">
    <td><span id="WH_JOURNALPLAYBACK"></span><span id="wh_journalplayback"></span>
    <strong>WH_JOURNALPLAYBACK</strong>
    1</td>
    <td><p>

Installs a hook procedure that posts messages previously recorded by a <strong>WH_JOURNALRECORD</strong> hook procedure. For more information, see the description of the [*JournalPlaybackProc*](journalplaybackproc.md) hook procedure.

</p></td>
    </tr>
    <tr class="odd">
    <td><span id="WH_JOURNALRECORD"></span><span id="wh_journalrecord"></span>
    <strong>WH_JOURNALRECORD</strong>
    0</td>
    <td><p>

Installs a hook procedure that records input messages posted to the system message queue. This hook is useful for recording macros. For more information, see the description of the [*JournalRecordProc*](journalrecordproc.md) hook procedure.

</p></td>
    </tr>
    <tr class="even">
    <td><span id="WH_KEYBOARD"></span><span id="wh_keyboard"></span>
    <strong>WH_KEYBOARD</strong>
    2</td>
    <td><p>

Installs a hook procedure that monitors keystroke messages. For more information, see the description of the [*KeyboardProc*](keyboardproc.md) hook procedure.

</p></td>
    </tr>
    <tr class="odd">
    <td><span id="WH_MOUSE"></span><span id="wh_mouse"></span>
    <strong>WH_MOUSE</strong>
    7</td>
    <td><p>Installs a hook procedure that monitors mouse messages. For more information, see the description of the [*MouseProc*](mouseproc.md) hook procedure.</p></td>
    </tr>
    <tr class="even">
    <td><span id="WH_MSGFILTER"></span><span id="wh_msgfilter"></span>
    <strong>WH_MSGFILTER</strong>
    -1</td>
    <td><p>Installs a hook procedure that monitors messages generated as a result of an input event in a dialog box, message box, menu, or scroll bar. The hook procedure monitors these messages only for the application that installed the hook procedure. For more information, see the [*MessageProc*](messageproc.md) hook procedure.</p></td>
    </tr>
    <tr class="odd">
    <td><span id="WH_SHELL"></span><span id="wh_shell"></span>
    <strong>WH_SHELL</strong>
    10</td>
    <td><p>Installs a hook procedure that receives notifications useful to a Shell application. For more information, see the description of the [*ShellProc*](shellproc.md) hook procedure and the <a href="/windows/win32/winmsg/about-hooks"><strong>WH_SHELL</strong></a> hook section.</p></td>
    </tr>
    <tr class="even">
    <td><span id="WH_SYSMSGFILTER"></span><span id="wh_sysmsgfilter"></span>
    <strong>WH_SYSMSGFILTER</strong>
    6</td>
    <td><p>Installs a hook procedure that monitors messages generated as a result of an input event in a dialog box, message box, menu, or scroll bar. The hook procedure monitors these messages for all applications in the system. For more information, see the description of the [*SysMsgProc*](sysmsgproc.md) hook procedure.</p></td>
    </tr>
    </tbody>
    </table>
    
     

  - *lParam* \[in\]  
    Type: **LPARAM**
    
    A pointer to a [**DEBUGHOOKINFO**](/windows/win32/api/winuser/ns-winuser-debughookinfo) structure that contains the parameters to be passed to the destination hook procedure.

## Return value

Type: ****

Type: LRESULT

To prevent the system from calling the hook, the hook procedure must return a nonzero value. Otherwise, the hook procedure must call [**CallNextHookEx**](/windows/win32/api/winuser/nf-winuser-callnexthookex).

## Remarks

An application installs this hook procedure by specifying the [**WH_DEBUG**](/windows/win32/winmsg/about-hooks) hook type and the pointer to the hook procedure in a call to the [**SetWindowsHookExA**](/windows/win32/api/winuser/nf-winuser-setwindowshookexa)/[**SetWindowsHookExW**](/windows/win32/api/winuser/nf-winuser-setwindowshookexw) function.

## Requirements

<table>
<colgroup>
<col />
<col />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Minimum supported client</p></td>
<td><p>Windows 2000 Professional [desktop apps only]</p></td>
</tr>
<tr class="even">
<td><p>Minimum supported server</p></td>
<td><p>Windows 2000 Server [desktop apps only]</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Winuser.h (include Windows.h)</td>
</tr>
</tbody>
</table>


## See also

[**CallNextHookEx**](/windows/win32/api/winuser/nf-winuser-callnexthookex)

[*CallWndProc*](callwndproc.md)

[*CallWndRetProc*](/windows/win32/api/winuser/nc-winuser-hookproc)

[*CBTProc*](cbtproc.md)

[**DEBUGHOOKINFO**](/windows/win32/api/winuser/ns-winuser-debughookinfo)

[*GetMsgProc*](getmsgproc.md)

[*JournalPlaybackProc*](journalplaybackproc.md)

[*JournalRecordProc*](journalrecordproc.md)

[*KeyboardProc*](keyboardproc.md)

[*MessageProc*](messageproc.md)

[*MouseProc*](mouseproc.md)

[**SetWindowsHookExA**](/windows/win32/api/winuser/nf-winuser-setwindowshookexa)/[**SetWindowsHookExW**](/windows/win32/api/winuser/nf-winuser-setwindowshookexw)

[*ShellProc*](shellproc.md)

[*SysMsgProc*](sysmsgproc.md)

[Hooks](hooks.md)