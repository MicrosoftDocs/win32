---
title: CBTProc callback function (Windows)
description: Receive useful notifications from the system.
ms.date: 06/27/2023
f1_keywords:
- CBTProc
- HCBT_ACTIVATE
- HCBT_DESTROYWND
- HCBT_KEYSKIPPED
- HCBT_CREATEWND
- HCBT_CLICKSKIPPED
- HCBT_MOVESIZE
- HCBT_MINMAX
- winuser/CBTProc
- HCBT_QS
- HCBT_SETFOCUS
- HCBT_SYSCOMMAND
dev_langs:
- C++
- C
api_location:
- Winuser.h
api_name:
- CBTProc
api_type:
- UserDefined
product:
- Windows
ms.topic: reference
topic_type:
- apiref
- kbSyntax
product_family_name: VS
ROBOTS: INDEX,FOLLOW
---

# CBTProc callback function

An application-defined or library-defined callback function used with the [**SetWindowsHookExA**](/windows/win32/api/winuser/nf-winuser-setwindowshookexa)/[**SetWindowsHookExW**](/windows/win32/api/winuser/nf-winuser-setwindowshookexw) function. The system calls this function before activating, creating, destroying, minimizing, maximizing, moving, or sizing a window; before completing a system command; before removing a mouse or keyboard event from the system message queue; before setting the keyboard focus; or before synchronizing with the system message queue. A computer-based training (CBT) application uses this hook procedure to receive useful notifications from the system.

## Syntax

``` c++
LRESULT CALLBACK CBTProc(
  _In_ int    nCode,
  _In_ WPARAM wParam,
  _In_ LPARAM lParam
);
```

## Parameters

  - *nCode* \[in\]  
    Type: **int**
    
    The code that the hook procedure uses to determine how to process the message. If *nCode* is less than zero, the hook procedure must pass the message to the [**CallNextHookEx**](/windows/win32/api/winuser/nf-winuser-callnexthookex) function without further processing and should return the value returned by **CallNextHookEx**. This parameter can be one of the following values.
    
    <table>
    <colgroup>
    <col style="width: 50%" />
    <col style="width: 50%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th>Value</th>
    <th>Meaning</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><span id="HCBT_ACTIVATE"></span><span id="hcbt_activate"></span>
    <strong>HCBT_ACTIVATE</strong>
    5</td>
    <td><p>The system is about to activate a window.</p></td>
    </tr>
    <tr class="even">
    <td><span id="HCBT_CLICKSKIPPED"></span><span id="hcbt_clickskipped"></span>
    <strong>HCBT_CLICKSKIPPED</strong>
    6</td>
    <td><p>The system has removed a mouse message from the system message queue. Upon receiving this hook code, a CBT application must install a <a href="/windows/win32/winmsg/about-hooks"><strong>WH_JOURNALPLAYBACK</strong></a> hook procedure in response to the mouse message.</p></td>
    </tr>
    <tr class="odd">
    <td><span id="HCBT_CREATEWND"></span><span id="hcbt_createwnd"></span>
    <strong>HCBT_CREATEWND</strong>
    3</td>
    <td><p>A window is about to be created. The system calls the hook procedure before sending the <a href="/windows/win32/winmsg/wm-create"><strong>WM_CREATE</strong></a> or <a href="/windows/win32/winmsg/wm-nccreate"><strong>WM_NCCREATE</strong></a> message to the window. If the hook procedure returns a nonzero value, the system destroys the window; the <a href="/windows/win32/api/winuser/nf-winuser-createwindowa"><strong>CreateWindow</strong></a> function returns <strong>NULL</strong>, but the <a href="/windows/win32/winmsg/wm-destroy"><strong>WM_DESTROY</strong></a> message is not sent to the window. If the hook procedure returns zero, the window is created normally.</p>
    <p>At the time of the <strong>HCBT_CREATEWND</strong> notification, the window has been created, but its final size and position may not have been determined and its parent window may not have been established. It is possible to send messages to the newly created window, although it has not yet received <a href="/windows/win32/winmsg/wm-nccreate"><strong>WM_NCCREATE</strong></a> or <a href="/windows/win32/winmsg/wm-create"><strong>WM_CREATE</strong></a> messages. It is also possible to change the position in the z-order of the newly created window by modifying the <strong>hwndInsertAfter</strong> member of the <a href="/windows/win32/api/winuser/ns-winuser-cbt_createwnda"><strong>CBT_CREATEWND</strong></a> structure.</p></td>
    </tr>
    <tr class="even">
    <td><span id="HCBT_DESTROYWND"></span><span id="hcbt_destroywnd"></span>
    <strong>HCBT_DESTROYWND</strong>
    4</td>
    <td><p>A window is about to be destroyed.</p></td>
    </tr>
    <tr class="odd">
    <td><span id="HCBT_KEYSKIPPED"></span><span id="hcbt_keyskipped"></span>
    <strong>HCBT_KEYSKIPPED</strong>
    7</td>
    <td><p>The system has removed a keyboard message from the system message queue. Upon receiving this hook code, a CBT application must install a <a href="/windows/win32/winmsg/about-hooks"><strong>WH_JOURNALPLAYBACK</strong></a> hook procedure in response to the keyboard message.</p></td>
    </tr>
    <tr class="even">
    <td><span id="HCBT_MINMAX"></span><span id="hcbt_minmax"></span>
    <strong>HCBT_MINMAX</strong>
    1</td>
    <td><p>A window is about to be minimized or maximized.</p></td>
    </tr>
    <tr class="odd">
    <td><span id="HCBT_MOVESIZE"></span><span id="hcbt_movesize"></span>
    <strong>HCBT_MOVESIZE</strong>
    0</td>
    <td><p>A window is about to be moved or sized.</p></td>
    </tr>
    <tr class="even">
    <td><span id="HCBT_QS"></span><span id="hcbt_qs"></span>
    <strong>HCBT_QS</strong>
    2</td>
    <td><p>The system has retrieved a <a href="https://msdn.microsoft.com/en-us/library/ms644972(v=vs.85)"><strong>WM_QUEUESYNC</strong></a> message from the system message queue.</p></td>
    </tr>
    <tr class="odd">
    <td><span id="HCBT_SETFOCUS"></span><span id="hcbt_setfocus"></span>
    <strong>HCBT_SETFOCUS</strong>
    9</td>
    <td><p>A window is about to receive the keyboard focus.</p></td>
    </tr>
    <tr class="even">
    <td><span id="HCBT_SYSCOMMAND"></span><span id="hcbt_syscommand"></span>
    <strong>HCBT_SYSCOMMAND</strong>
    8</td>
    <td><p>A system command is about to be carried out. This allows a CBT application to prevent task switching by means of hot keys.</p></td>
    </tr>
    </tbody>
    </table>
    
     

  - *wParam* \[in\]  
    Type: **WPARAM**
    
    Depends on the *nCode* parameter. For details, see the following Remarks section.

  - *lParam* \[in\]  
    Type: **LPARAM**
    
    Depends on the *nCode* parameter. For details, see the following Remarks section.

## Return value

Type: ****

Type: LRESULT

The value returned by the hook procedure determines whether the system allows or prevents one of these operations. For operations corresponding to the following CBT hook codes, the return value must be 0 to allow the operation, or 1 to prevent it.

  - **HCBT\_ACTIVATE**
  - **HCBT\_CREATEWND**
  - **HCBT\_DESTROYWND**
  - **HCBT\_MINMAX**
  - **HCBT\_MOVESIZE**
  - **HCBT\_SETFOCUS**
  - **HCBT\_SYSCOMMAND**

For operations corresponding to the following CBT hook codes, the return value is ignored.

  - **HCBT\_CLICKSKIPPED**
  - **HCBT\_KEYSKIPPED**
  - **HCBT\_QS**

## Remarks

The **HOOKPROC** type defines a pointer to this callback function. *CBTProc* is a placeholder for the application-defined or library-defined function name.

The hook procedure should not install a [**WH\_JOURNALPLAYBACK**](/windows/win32/winmsg/about-hooks) hook procedure except in the situations described in the preceding list of hook codes.

An application installs the hook procedure by specifying the [**WH\_CBT**](/windows/win32/winmsg/about-hooks) hook type and a pointer to the hook procedure in a call to the [**SetWindowsHookExA**](/windows/win32/api/winuser/nf-winuser-setwindowshookexa)/[**SetWindowsHookExW**](/windows/win32/api/winuser/nf-winuser-setwindowshookexw) function.

The following table describes the *wParam* and *lParam* parameters for each **HCBT\_** hook code.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>wParam</th>
<th>lParam</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>HCBT_ACTIVATE</strong></td>
<td>Specifies the handle to the window about to be activated.</td>
<td>Specifies a long pointer to a <a href="/windows/win32/api/winuser/ns-winuser-cbtactivatestruct"><strong>CBTACTIVATESTRUCT</strong></a> structure containing the handle to the active window and specifies whether the activation is changing because of a mouse click.</td>
</tr>
<tr class="even">
<td><strong>HCBT_CLICKSKIPPED</strong></td>
<td>Specifies the mouse message removed from the system message queue.</td>
<td>Specifies a long pointer to a <a href="/windows/win32/api/winuser/ns-winuser-mousehookstruct"><strong>MOUSEHOOKSTRUCT</strong></a> structure containing the hit-test code and the handle to the window for which the mouse message is intended.
<p>The <strong>HCBT_CLICKSKIPPED</strong> value is sent to a <em>CBTProc</em> hook procedure only if a <a href="/windows/win32/winmsg/about-hooks"><strong>WH_MOUSE</strong></a> hook is installed. For a list of hit-test codes, see <a href="/windows/win32/inputdev/wm-nchittest"><strong>WM_NCHITTEST</strong></a>.</p></td>
</tr>
<tr class="odd">
<td><strong>HCBT_CREATEWND</strong></td>
<td>Specifies the handle to the new window.</td>
<td>Specifies a long pointer to a <a href="/windows/win32/api/winuser/ns-winuser-cbt_createwnda"><strong>CBT_CREATEWND</strong></a> structure containing initialization parameters for the window. The parameters include the coordinates and dimensions of the window. By changing these parameters, a <em>CBTProc</em> hook procedure can set the initial size and position of the window.</td>
</tr>
<tr class="even">
<td><strong>HCBT_DESTROYWND</strong></td>
<td>Specifies the handle to the window about to be destroyed.</td>
<td>Is undefined and must be set to zero.</td>
</tr>
<tr class="odd">
<td><strong>HCBT_KEYSKIPPED</strong></td>
<td>Specifies the virtual-key code.</td>
<td>Specifies the repeat count, scan code, key-transition code, previous key state, and context code. The <strong>HCBT_KEYSKIPPED</strong> value is sent to a <em>CBTProc</em> hook procedure only if a <a href="/windows/win32/winmsg/about-hooks"><strong>WH_KEYBOARD</strong></a> hook is installed. For more information, see <a href="/windows/win32/inputdev/wm-keyup"><strong>WM_KEYUP</strong></a> or <a href="/windows/win32/inputdev/wm-keydown"><strong>WM_KEYDOWN</strong></a>.</td>
</tr>
<tr class="even">
<td><strong>HCBT_MINMAX</strong></td>
<td>Specifies the handle to the window being minimized or maximized.</td>
<td>Specifies, in the low-order word, a show-window value (<strong>SW_</strong>) specifying the operation. For a list of show-window values, see the <a href="/windows/win32/api/winuser/nf-winuser-showwindow"><strong>ShowWindow</strong></a>. The high-order word is undefined.</td>
</tr>
<tr class="odd">
<td><strong>HCBT_MOVESIZE</strong></td>
<td>Specifies the handle to the window to be moved or sized.</td>
<td>Specifies a long pointer to a <a href="/previous-versions//dd162897(v=vs.85)"><strong>RECT</strong></a> structure containing the coordinates of the window. By changing the values in the structure, a <em>CBTProc</em> hook procedure can set the final coordinates of the window.</td>
</tr>
<tr class="even">
<td><strong>HCBT_QS</strong></td>
<td>Is undefined and must be zero.</td>
<td>Is undefined and must be zero.</td>
</tr>
<tr class="odd">
<td><strong>HCBT_SETFOCUS</strong></td>
<td>Specifies the handle to the window gaining the keyboard focus.</td>
<td>Specifies the handle to the window losing the keyboard focus.</td>
</tr>
<tr class="even">
<td><strong>HCBT_SYSCOMMAND</strong></td>
<td>Specifies a system-command value (<strong>SC_</strong>) specifying the system command. For more information about system-command values, see <a href="/windows/win32/menurc/wm-syscommand"><strong>WM_SYSCOMMAND</strong></a>.</td>
<td>Contains the same data as the <em>lParam</em> value of a <a href="/windows/win32/menurc/wm-syscommand"><strong>WM_SYSCOMMAND</strong></a> message: If a system menu command is chosen with the mouse, the low-order word contains the x-coordinate of the cursor, in screen coordinates, and the high-order word contains the y-coordinate; otherwise, the parameter is not used.</td>
</tr>
</tbody>
</table>

 

For information, see [WinEvents](https://msdn.microsoft.com/en-us/library/dd373889\(v=vs.85\)).

## Requirements

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
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

**Reference**

[**CallNextHookEx**](/windows/win32/api/winuser/nf-winuser-callnexthookex)

[**CreateWindow**](https://msdn.microsoft.com/en-us/library/ms632679\(v=vs.85\))

[**SetWindowsHookExA**](/windows/win32/api/winuser/nf-winuser-setwindowshookexa)/[**SetWindowsHookExW**](/windows/win32/api/winuser/nf-winuser-setwindowshookexw)

[**WM\_SYSCOMMAND**](https://msdn.microsoft.com/en-us/library/ms646360\(v=vs.85\))

**Conceptual**

[Hooks](hooks.md)