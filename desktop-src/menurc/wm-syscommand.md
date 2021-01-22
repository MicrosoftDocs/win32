---
title: WM_SYSCOMMAND message (Winuser.h)
description: A window receives this message when the user chooses a command from the Window menu (formerly known as the system or control menu) or when the user chooses the maximize button, minimize button, restore button, or close button.
ms.assetid: 82c7cc95-82d5-4f0f-8c78-ab325561b04e
keywords:
- WM_SYSCOMMAND message Menus and Other Resources
topic_type:
- apiref
api_name:
- WM_SYSCOMMAND
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.custom: snippet-project
ms.date: 07/27/2020
---

# WM\_SYSCOMMAND message

A window receives this message when the user chooses a command from the **Window** menu (formerly known as the system or control menu) or when the user chooses the maximize button, minimize button, restore button, or close button.


```C++
#define WM_SYSCOMMAND                   0x0112
```

## Example

```cpp
 case WM_SYSCOMMAND:
        if (wParam == SC_CLOSE)
        {
            EndDialog (hDlg, TRUE);
            return(TRUE);
        }
        break;

```
Example from [Windows Classic Samples](https://github.com/microsoft/Windows-classic-samples/blob/1d363ff4bd17d8e20415b92e2ee989d615cc0d91/Samples/Win7Samples/winbase/registry/RegExplorer.c) on GitHub.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The type of system command requested. This parameter can be one of the following values.



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
<td><span id="SC_CLOSE"></span><span id="sc_close"></span><dl> <dt><strong>SC_CLOSE</strong></dt> <dt>0xF060</dt> </dl></td>
<td>Closes the window.<br/></td>
</tr>
<tr class="even">
<td><span id="SC_CONTEXTHELP"></span><span id="sc_contexthelp"></span><dl> <dt><strong>SC_CONTEXTHELP</strong></dt> <dt>0xF180</dt> </dl></td>
<td>Changes the cursor to a question mark with a pointer. If the user then clicks a control in the dialog box, the control receives a <a href="/windows/desktop/shell/wm-help"><strong>WM_HELP</strong></a> message.<br/></td>
</tr>
<tr class="odd">
<td><span id="SC_DEFAULT"></span><span id="sc_default"></span><dl> <dt><strong>SC_DEFAULT</strong></dt> <dt>0xF160</dt> </dl></td>
<td>Selects the default item; the user double-clicked the window menu.<br/></td>
</tr>
<tr class="even">
<td><span id="SC_HOTKEY"></span><span id="sc_hotkey"></span><dl> <dt><strong>SC_HOTKEY</strong></dt> <dt>0xF150</dt> </dl></td>
<td>Activates the window associated with the application-specified hot key. The <em>lParam</em> parameter identifies the window to activate.<br/></td>
</tr>
<tr class="odd">
<td><span id="SC_HSCROLL"></span><span id="sc_hscroll"></span><dl> <dt><strong>SC_HSCROLL</strong></dt> <dt>0xF080</dt> </dl></td>
<td>Scrolls horizontally.<br/></td>
</tr>
<tr class="even">
<td><span id="SCF_ISSECURE"></span><span id="scf_issecure"></span><dl> <dt><strong>SCF_ISSECURE</strong></dt> <dt>0x00000001</dt> </dl></td>
<td>Indicates whether the screen saver is secure. <br/></td>
</tr>
<tr class="odd">
<td><span id="SC_KEYMENU"></span><span id="sc_keymenu"></span><dl> <dt><strong>SC_KEYMENU</strong></dt> <dt>0xF100</dt> </dl></td>
<td>Retrieves the window menu as a result of a keystroke. For more information, see the Remarks section.<br/></td>
</tr>
<tr class="even">
<td><span id="SC_MAXIMIZE"></span><span id="sc_maximize"></span><dl> <dt><strong>SC_MAXIMIZE</strong></dt> <dt>0xF030</dt> </dl></td>
<td>Maximizes the window.<br/></td>
</tr>
<tr class="odd">
<td><span id="SC_MINIMIZE"></span><span id="sc_minimize"></span><dl> <dt><strong>SC_MINIMIZE</strong></dt> <dt>0xF020</dt> </dl></td>
<td>Minimizes the window.<br/></td>
</tr>
<tr class="even">
<td><span id="SC_MONITORPOWER"></span><span id="sc_monitorpower"></span><dl> <dt><strong>SC_MONITORPOWER</strong></dt> <dt>0xF170</dt> </dl></td>
<td>Sets the state of the display. This command supports devices that have power-saving features, such as a battery-powered personal computer. <br/> The <em>lParam</em> parameter can have the following values:<br/>
<ul>
<li>-1 (the display is powering on)</li>
<li>1 (the display is going to low power)</li>
<li>2 (the display is being shut off)</li>
</ul></td>
</tr>
<tr class="odd">
<td><span id="SC_MOUSEMENU"></span><span id="sc_mousemenu"></span><dl> <dt><strong>SC_MOUSEMENU</strong></dt> <dt>0xF090</dt> </dl></td>
<td>Retrieves the window menu as a result of a mouse click.<br/></td>
</tr>
<tr class="even">
<td><span id="SC_MOVE"></span><span id="sc_move"></span><dl> <dt><strong>SC_MOVE</strong></dt> <dt>0xF010</dt> </dl></td>
<td>Moves the window.<br/></td>
</tr>
<tr class="odd">
<td><span id="SC_NEXTWINDOW"></span><span id="sc_nextwindow"></span><dl> <dt><strong>SC_NEXTWINDOW</strong></dt> <dt>0xF040</dt> </dl></td>
<td>Moves to the next window.<br/></td>
</tr>
<tr class="even">
<td><span id="SC_PREVWINDOW"></span><span id="sc_prevwindow"></span><dl> <dt><strong>SC_PREVWINDOW</strong></dt> <dt>0xF050</dt> </dl></td>
<td>Moves to the previous window.<br/></td>
</tr>
<tr class="odd">
<td><span id="SC_RESTORE"></span><span id="sc_restore"></span><dl> <dt><strong>SC_RESTORE</strong></dt> <dt>0xF120</dt> </dl></td>
<td>Restores the window to its normal position and size.<br/></td>
</tr>
<tr class="even">
<td><span id="SC_SCREENSAVE"></span><span id="sc_screensave"></span><dl> <dt><strong>SC_SCREENSAVE</strong></dt> <dt>0xF140</dt> </dl></td>
<td>Executes the screen saver application specified in the [boot] section of the System.ini file.<br/></td>
</tr>
<tr class="odd">
<td><span id="SC_SIZE"></span><span id="sc_size"></span><dl> <dt><strong>SC_SIZE</strong></dt> <dt>0xF000</dt> </dl></td>
<td>Sizes the window.<br/></td>
</tr>
<tr class="even">
<td><span id="SC_TASKLIST"></span><span id="sc_tasklist"></span><dl> <dt><strong>SC_TASKLIST</strong></dt> <dt>0xF130</dt> </dl></td>
<td>Activates the <strong>Start</strong> menu.<br/></td>
</tr>
<tr class="odd">
<td><span id="SC_VSCROLL"></span><span id="sc_vscroll"></span><dl> <dt><strong>SC_VSCROLL</strong></dt> <dt>0xF070</dt> </dl></td>
<td>Scrolls vertically.<br/></td>
</tr>
</tbody>
</table>



 

</dd> <dt>

*lParam* 
</dt> <dd>

The low-order word specifies the horizontal position of the cursor, in screen coordinates, if a window menu command is chosen with the mouse. Otherwise, this parameter is not used.

The high-order word specifies the vertical position of the cursor, in screen coordinates, if a window menu command is chosen with the mouse. This parameter is  1 if the command is chosen using a system accelerator, or zero if using a mnemonic.

</dd> </dl>

## Return value

An application should return zero if it processes this message.

## Remarks

To obtain the position coordinates in screen coordinates, use the following code:


```
xPos = GET_X_LPARAM(lParam);    // horizontal position 
yPos = GET_Y_LPARAM(lParam);    // vertical position
```



The [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function carries out the window menu request for the predefined actions specified in the previous table.

In **WM\_SYSCOMMAND** messages, the four low-order bits of the *wParam* parameter are used internally by the system. To obtain the correct result when testing the value of *wParam*, an application must combine the value 0xFFF0 with the *wParam* value by using the bitwise AND operator.

The menu items in a window menu can be modified by using the [**GetSystemMenu**](/windows/desktop/api/Winuser/nf-winuser-getsystemmenu), [**AppendMenu**](/windows/desktop/api/Winuser/nf-winuser-appendmenua), [**InsertMenu**](/windows/desktop/api/Winuser/nf-winuser-insertmenua), [**ModifyMenu**](/windows/desktop/api/Winuser/nf-winuser-modifymenua), [**InsertMenuItem**](/windows/desktop/api/Winuser/nf-winuser-insertmenuitema), and [**SetMenuItemInfo**](/windows/desktop/api/Winuser/nf-winuser-setmenuiteminfoa) functions. Applications that modify the window menu must process **WM\_SYSCOMMAND** messages.

An application can carry out any system command at any time by passing a **WM\_SYSCOMMAND** message to [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca). Any **WM\_SYSCOMMAND** messages not handled by the application must be passed to **DefWindowProc**. Any command values added by an application must be processed by the application and cannot be passed to **DefWindowProc**.

If password protection is enabled by policy, the screen saver is started regardless of what an application does with the **SC\_SCREENSAVE** notification even if fails to pass it to [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca).

Accelerator keys that are defined to choose items from the window menu are translated into **WM\_SYSCOMMAND** messages; all other accelerator keystrokes are translated into [**WM\_COMMAND**](wm-command.md) messages.

If the *wParam* is **SC\_KEYMENU**, *lParam* contains the character code of the key that is used with the ALT key to display the popup menu. For example, pressing ALT+F to display the File popup will cause a **WM\_SYSCOMMAND** with *wParam* equal to **SC\_KEYMENU** and *lParam* equal to 'f'.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**AppendMenu**](/windows/desktop/api/Winuser/nf-winuser-appendmenua)
</dt> <dt>

[**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca)
</dt> <dt>

[**GET\_X\_LPARAM**](/windows/desktop/api/windowsx/nf-windowsx-get_x_lparam)
</dt> <dt>

[**GET\_Y\_LPARAM**](/windows/desktop/api/windowsx/nf-windowsx-get_y_lparam)
</dt> <dt>

[**GetSystemMenu**](/windows/desktop/api/Winuser/nf-winuser-getsystemmenu)
</dt> <dt>

[**InsertMenu**](/windows/desktop/api/Winuser/nf-winuser-insertmenua)
</dt> <dt>

[**ModifyMenu**](/windows/desktop/api/Winuser/nf-winuser-modifymenua)
</dt> <dt>

[**WM\_COMMAND**](wm-command.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Keyboard Accelerators](keyboard-accelerators.md)
</dt> </dl>

