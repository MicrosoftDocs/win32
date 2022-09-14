---
title: Dialog Box Programming Considerations
description: This overview discusses some programming considerations concerning dialog boxes.
ms.assetid: 49024a0f-ea92-4d56-b063-8e5fcdbd884a
keywords:
- Windows User Interface,windowing
- Windows User Interface,dialog boxes
- windowing,dialog boxes
- dialog boxes,about
- dialog box procedures
- dialog boxes,procedures
- WM_INITDIALOG message
- WM_COMMAND message
- WM_PARENTNOTIFY message
- control-color messages
- dialog boxes,message processing
- dialog boxes,keyboard interface
- dialog boxes,mnemonics
- dialog boxes,custom
- custom dialog boxes
- dialog boxes,settings
ms.topic: article
ms.date: 08/25/2020
---

# Dialog Box Programming Considerations

This overview discusses some programming considerations concerning dialog boxes.

The overview includes the following topics.

-   [Dialog Box Procedures](#dialog-box-procedures)
    -   [The WM\_INITDIALOG Message](wm-initdialog.md)
    -   [The WM\_COMMAND Message](/windows/desktop/menurc/wm-command)
    -   [The WM\_PARENTNOTIFY Message](/previous-versions/windows/desktop/inputmsg/wm-parentnotify)
    -   [Control-Color Messages](#control-color-messages)
    -   [Dialog Box Default Message Processing](#dialog-box-default-message-processing)
-   [Dialog Box Keyboard Interface](#dialog-box-keyboard-interface)
    -   [The WS\_TABSTOP Style](/windows/desktop/winmsg/window-styles)
    -   [The WS\_GROUP Style](/windows/desktop/winmsg/window-styles)
    -   [Mnemonics](#mnemonics)
-   [Dialog Box Settings](#dialog-box-settings)
    -   [Radio Buttons and Check Boxes](#radio-buttons-and-check-boxes)
    -   [Dialog Box Edit Controls](#dialog-box-edit-controls)
    -   [List Boxes, Combo Boxes, and Directory Listings](#list-boxes-combo-boxes-and-directory-listings)
    -   [Dialog Box Control Messages](#dialog-box-control-messages)
-   [Custom Dialog Boxes](#custom-dialog-boxes)

## Dialog Box Procedures

A dialog box procedure is similar to a window procedure in that the system sends messages to the procedure when it has information to give or tasks to carry out. Unlike a window procedure, a dialog box procedure never calls the [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function. Instead, it returns **TRUE** if it processes a message or **FALSE** if it does not.

Every dialog box procedure has the following form:

```cpp
BOOL CALLBACK DlgProc(HWND hwndDlg, UINT message, WPARAM wParam, LPARAM lParam) 
{ 
    switch (message) 
    { 
 
        // Place message cases here. 
 
        default: 
            return FALSE; 
    } 
}
```

The procedure parameters serve the same purpose as in a window procedure, with the *hwndDlg* parameter receiving the window handle of the dialog box.

Most dialog box procedures process the [**WM\_INITDIALOG**](wm-initdialog.md) message and the [**WM\_COMMAND**](/windows/desktop/menurc/wm-command) messages sent by the controls, but process few if any other messages. If a dialog box procedure does not process a message, it must return **FALSE** to direct the system to process the messages internally. The only exception to this rule is the **WM\_INITDIALOG** message. The dialog box procedure must return **TRUE** to direct the system to further process the **WM\_INITDIALOG** message. In any case, the procedure must not call [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca).

- [The WM\_INITDIALOG Message](#the-wm_initdialog-message)
- [The WM\_COMMAND Message](#the-wm_command-message)
- [The WM\_PARENTNOTIFY Message](#the-wm_parentnotify-message)
- [Control-Color Messages](#control-color-messages)
- [Dialog Box Default Message Processing](#dialog-box-default-message-processing)

### The WM\_INITDIALOG Message

The system does not send a [**WM\_CREATE**](/windows/desktop/winmsg/wm-create) message to the dialog box procedure. Instead, it sends a [**WM\_INITDIALOG**](wm-initdialog.md) message when it creates the dialog box and all its controls but before it displays the dialog box. The procedure should carry out any initialization required to ensure that the dialog box displays the current settings associated with the task. For example, when a dialog box contains a control to show the current drive and directory, the procedure must determine the current drive and directory and set the control to that value.

The procedure can initialize controls by using functions such as [**SetDlgItemText**](/windows/desktop/api/Winuser/nf-winuser-setdlgitemtexta) and [**CheckDlgButton**](https://msdn.microsoft.com/library/Cc410649(v=MSDN.10).aspx). Because controls are windows, the procedure can also manipulate them by using window-management functions such as [**EnableWindow**](/windows/desktop/api/winuser/nf-winuser-enablewindow) and [**SetFocus**](/windows/desktop/api/winuser/nf-winuser-setfocus). The procedure can retrieve the window handle to a control by using the [**GetDlgItem**](/windows/desktop/api/Winuser/nf-winuser-getdlgitem) function.

The dialog box procedure can change the contents, state, and position of any control as needed. For example, in a dialog box that contains a list box of filenames and an **Open** button, the procedure can disable the **Open** button until the user selects a file from the list. In this example, the dialog box template specifies the [**WS\_DISABLED**](/windows/desktop/winmsg/window-styles) style for the **Open** button and the system automatically disables the button when creating it. When the dialog box procedure receives a notification message from the list box indicating that the user has selected a file, the procedure calls the [**EnableWindow**](/windows/desktop/api/winuser/nf-winuser-enablewindow) function to enable the **Open** button.

To display a custom icon on the caption bar of the dialog box, your [**WM\_INITDIALOG**](wm-initdialog.md) handler can send the [**WM\_SETICON**](/windows/desktop/winmsg/wm-seticon) message to the dialog box.

If the application creates the dialog box by using one of the functions [**DialogBoxParam**](/windows/desktop/api/Winuser/nf-winuser-dialogboxparama), [**DialogBoxIndirectParam**](/windows/desktop/api/Winuser/nf-winuser-dialogboxindirectparama), [**CreateDialogParam**](/windows/desktop/api/Winuser/nf-winuser-createdialogparama), or [**CreateDialogIndirectParam**](/windows/desktop/api/Winuser/nf-winuser-createdialogindirectparama), the *lParam* parameter for the [**WM\_INITDIALOG**](wm-initdialog.md) message contains the extra parameter passed to the function. Applications typically use this extra parameter to pass a pointer to additional initialization information to the dialog box procedure, but the dialog box procedure must determine the meaning of the parameter. If the application uses another function to create the dialog box, the system sets the *lParam* parameter to **NULL**.

Before returning from the [**WM\_INITDIALOG**](wm-initdialog.md) message, the procedure should determine whether it should set the input focus to a specified control. If the dialog box procedure returns **TRUE**, the system automatically sets the input focus to the control whose window handle is in the *wParam* parameter. If the control receiving the default focus is not appropriate, it can set the focus to the appropriate control by using the [**SetFocus**](/windows/desktop/api/winuser/nf-winuser-setfocus) function. If the procedure sets the input focus, it must return **FALSE** to prevent the system from setting the default focus. The control receiving the default input focus is always the first control specified in the template that is visible, not disabled, and has the [WS\_TABSTOP](/windows/desktop/winmsg/window-styles) style. If no such control exists, the system sets the default input focus to the first control in the template.

### The WM\_COMMAND Message

A control can send a [**WM\_COMMAND**](/windows/desktop/menurc/wm-command) message to the dialog box procedure when the user carries out an action in the control. These messages, called notification messages, inform the procedure of user input and permit it to carry out appropriate responses.

All predefined controls, except static controls, send notification messages for selected user actions. For example, a push button sends the [**BN\_CLICKED**](../controls/bn-clicked.md) notification message whenever the user clicks the button. In all cases, the low-order word of the *wParam* parameter contains the control identifier, the high-order word of *wParam* contains the notification code, and the *lParam* parameter contains the control window handle.

The dialog box procedure should monitor and process notification messages. In particular, the procedure must process messages having the IDOK or IDCANCEL identifiers; these messages represent a request by the user to close the dialog box. The procedure should close the dialog box by using the [**EndDialog**](/windows/desktop/api/Winuser/nf-winuser-enddialog) function for modal dialog boxes and the [**DestroyWindow**](/windows/desktop/api/winuser/nf-winuser-destroywindow) function for modeless dialog boxes.

The system also sends [**WM\_COMMAND**](/windows/desktop/menurc/wm-command) messages to the dialog box procedure if the dialog box has a menu, such as the **window** menu, and the user clicks a menu item. In particular, the system sends a **WM\_COMMAND** message with the *wParam* parameter set to **IDCANCEL** whenever the user clicks **Close** in the dialog box's window menu. The message is nearly identical to the notification message sent by the **Cancel** button and should be processed in exactly the same way.

### The WM\_PARENTNOTIFY Message

A control sends a [**WM\_PARENTNOTIFY**](/previous-versions/windows/desktop/inputmsg/wm-parentnotify) message whenever the user presses a mouse button while pointing to the control. Some applications interpret this message as a signal to carry out an action related to the control, such as displaying a line of text describing the purpose of the control.

The system also sends [**WM\_PARENTNOTIFY**](/previous-versions/windows/desktop/inputmsg/wm-parentnotify) messages when it creates and destroys a window, but not for controls created from a dialog box template. The system prevents these messages by specifying the **WS\_EX\_NOPARENTNOTIFY** style when creating the controls. An application cannot override this default behavior unless it creates its own controls for the dialog box.

### Control-Color Messages

Controls and the system can send control-color messages when they want the dialog box procedure to paint the background of a control or other window by using a specific brush and colors. This can be useful when applications override the default colors used in dialog boxes and their controls. Following are the control-color messages, which have replaced the **WM\_CTLCOLOR** message.

-   [**WM\_CTLCOLORBTN**](../controls/wm-ctlcolorbtn.md)
-   [**WM\_CTLCOLORDLG**](wm-ctlcolordlg.md)
-   [**WM\_CTLCOLOREDIT**](../controls/wm-ctlcoloredit.md)
-   [**WM\_CTLCOLORLISTBOX**](../controls/wm-ctlcolorlistbox.md)
-   [**WM\_CTLCOLORSCROLLBAR**](../controls/wm-ctlcolorscrollbar.md)
-   [**WM\_CTLCOLORSTATIC**](../controls/wm-ctlcolorstatic.md)

A control sends a control-color message to the dialog box procedure just before it paints its own background. The message allows the procedure to specify which brush to use and to set the background and foreground colors. The procedure specifies a brush by returning the brush handle. To set the background and foreground colors, the procedure uses the [**SetBkColor**](/windows/desktop/api/wingdi/nf-wingdi-setbkcolor) and [**SetTextColor**](/windows/desktop/api/wingdi/nf-wingdi-settextcolor) functions with the control's display device context. The control-color message passes a handle to the display device context to the procedure in the message's *wParam* parameter.

The system sends a [**WM\_CTLCOLORDLG**](wm-ctlcolordlg.md) message to the dialog box procedure if the procedure does not process the [**WM\_ERASEBKGND**](/windows/desktop/winmsg/wm-erasebkgnd) message. The predefined dialog box class does not have a class background brush, so this message lets the procedure define its own background without having to include the code to carry out the work.

In any case, when a dialog box procedure does not process a control-color message, the system uses a brush with the default window color to paint the background for all controls and windows except scroll bars. An application can retrieve the default window color by passing the **COLOR\_WINDOW** value to the [**GetSysColor**](/windows/desktop/api/winuser/nf-winuser-getsyscolor) function. While the background is painted, the foreground color for the display device context is set to the default text color (**COLOR\_WINDOWTEXT**). For scroll bars, the system uses a brush having the default scroll bar color (**COLOR\_SCROLLBAR**). In this case, the background and foreground colors for the display device context are set to white and black, respectively.

### Dialog Box Default Message Processing

The window procedure for the predefined dialog box class carries out default processing for all messages that the dialog box procedure does not process. When the dialog box procedure returns **FALSE** for any message, the predefined window procedure checks the messages and carries out the following default actions:



| Message                                            | Default action                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|----------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DM\_GETDEFID**](dm-getdefid.md)                | You can send this message to a dialog box. The dialog box returns the control identifier of the default push button, if the dialog box has one; otherwise, it returns zero.                                                                                                                                                                                                                                                                                                                      |
| [**DM\_REPOSITION**](dm-reposition.md)            | You can send this message to a top-level dialog box. The dialog box repositions itself so it fits within the desktop area.                                                                                                                                                                                                                                                                                                                                                                       |
| [**DM\_SETDEFID**](dm-setdefid.md)                | You can send this message to a dialog box. The dialog box sets the default push button to the control specified by the control identifier in the *wParam* parameter.                                                                                                                                                                                                                                                                                                                             |
| [**WM\_ACTIVATE**](/windows/desktop/inputdev/wm-activate)           | Restores the input focus to the control identified by the previously saved handle if the dialog box is activated. Otherwise, the procedure saves the handle to the control having the input focus.                                                                                                                                                                                                                                                                                               |
| [**WM\_CHARTOITEM**](../controls/wm-chartoitem.md)         | Returns zero.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [**WM\_CLOSE**](/windows/desktop/winmsg/wm-close)                   | Posts the [**BN\_CLICKED**](../controls/bn-clicked.md) notification message to the dialog box, specifying **IDCANCEL** as the control identifier. If the dialog box has an IDCANCEL control identifier and the control is currently disabled, the procedure sounds a warning and does not post the message.                                                                                                                                                                                              |
| [**WM\_COMPAREITEM**](../controls/wm-compareitem.md)       | Returns zero.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [**WM\_ERASEBKGND**](/windows/desktop/winmsg/wm-erasebkgnd)         | Fills the dialog box client area by using either the brush returned from the [**WM\_CTLCOLORDLG**](wm-ctlcolordlg.md) message or with the default window color.                                                                                                                                                                                                                                                                                                                                 |
| [**WM\_GETFONT**](/windows/desktop/winmsg/wm-getfont)               | Returns a handle to the application-defined dialog box font.                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [**WM\_INITDIALOG**](wm-initdialog.md)            | Returns zero.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [**WM\_LBUTTONDOWN**](/windows/desktop/inputdev/wm-lbuttondown)     | Sends a [**CB\_SHOWDROPDOWN**](../controls/cb-showdropdown.md) message to the combo box having the input focus, directing the control to hide its drop-down list box. The procedure calls [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) to complete the default action.                                                                                                                                                                                                                                      |
| [**WM\_NCDESTROY**](/windows/desktop/winmsg/wm-ncdestroy)           | Releases global memory allocated for edit controls in the dialog box (applies to dialog boxes that specify the [**DS\_LOCALEDIT**](dialog-box-styles.md) style) and frees any application-defined font (applies to dialog boxes that specify the [**DS\_SETFONT**](dialog-box-styles.md) or [**DS\_SHELLFONT**](dialog-box-styles.md) style). The procedure calls the [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function to complete the default action. |
| [**WM\_NCLBUTTONDOWN**](/windows/desktop/inputdev/wm-nclbuttondown) | Sends a [**CB\_SHOWDROPDOWN**](../controls/cb-showdropdown.md) message to the combo box having the input focus, directing the control to hide its drop-down list box. The procedure calls [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) to complete the default action.                                                                                                                                                                                                                                      |
| [**WM\_NEXTDLGCTL**](wm-nextdlgctl.md)            | Sets the input focus to the next or previous control in the dialog box, to the control identified by the handle in the *wParam* parameter, or to the first control in the dialog box that is visible, not disabled, and has the [**WS\_TABSTOP**](/windows/desktop/winmsg/window-styles) style. The procedure ignores this message if the current window with the input focus is not a control.                                                                                                                  |
| [**WM\_SETFOCUS**](/windows/desktop/inputdev/wm-setfocus)           | Sets the input focus to the control identified by a previously saved control window handle. If no such handle exists, the procedure sets the input focus to the first control in the dialog box template that is visible, not disabled, and has the [**WS\_TABSTOP**](/windows/desktop/winmsg/window-styles) style. If no such control exists, the procedure sets the input focus to the first control in the template.                                                                                          |
| [**WM\_SHOWWINDOW**](/windows/desktop/winmsg/wm-showwindow)         | Saves a handle to the control having the input focus if the dialog box is being hidden, then calls [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) to complete the default action.                                                                                                                                                                                                                                                                                                                     |
| [**WM\_SYSCOMMAND**](/windows/desktop/menurc/wm-syscommand)         | Saves a handle to the control having the input focus if the dialog box is being minimized, then calls [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) to complete the default action.                                                                                                                                                                                                                                                                                                                  |
| [**WM\_VKEYTOITEM**](../controls/wm-vkeytoitem.md)         | Returns zero.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

The predefined window procedure passes all other messages to [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) for default processing.

## Dialog Box Keyboard Interface

The system provides a special keyboard interface for dialog boxes that carries out special processing for several keys. The interface generates messages that correspond to certain buttons in the dialog box or changes the input focus from one control to another. Following are the keys used in this interface and their respective actions.


| Key            | Action                                                                                                                                                                    |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ALT+*mnemonic* | Moves the input focus to the first control (having the [**WS\_TABSTOP**](/windows/desktop/winmsg/window-styles) style) after the static control containing the specified mnemonic.        |
| DOWN           | Moves the input focus to the next control in the group.                                                                                                                   |
| ENTER          | Sends a [**WM\_COMMAND**](/windows/desktop/menurc/wm-command) message to the dialog box procedure. The *wParam* parameter is set to IDOK or control identifier of the default push button. |
| ESC            | Sends a [**WM\_COMMAND**](/windows/desktop/menurc/wm-command) message to the dialog box procedure. The *wParam* parameter is set to IDCANCEL.                                              |
| LEFT           | Moves the input focus to the previous control in the group.                                                                                                               |
| *mnemonic*     | Moves the input focus to the first control (having the [**WS\_TABSTOP**](/windows/desktop/winmsg/window-styles) style) after the static control containing the specified mnemonic.        |
| RIGHT          | Moves the input focus to the next control in the group.                                                                                                                   |
| SHIFT+TAB      | Moves the input focus to the previous control that has the [**WS\_TABSTOP**](/windows/desktop/winmsg/window-styles) style.                                                                |
| TAB            | Moves the input focus to the next control that has the [**WS\_TABSTOP**](/windows/desktop/winmsg/window-styles) style.                                                                    |
| UP             | Moves the input focus to the previous control in the group.                                                                                                               |

The system automatically provides the keyboard interface for all modal dialog boxes. It does not provide the interface for modeless dialog boxes unless the application calls the [**IsDialogMessage**](/windows/desktop/api/Winuser/nf-winuser-isdialogmessagea) function to filter messages in its main message loop. This means that the application must pass the message to **IsDialogMessage** immediately after retrieving the message from the message queue. The function processes the messages if it is for the dialog box and returns a nonzero value to indicate that the message has been processed and must not be passed to the [**TranslateMessage**](/windows/desktop/api/winuser/nf-winuser-translatemessage) or [**DispatchMessage**](/windows/desktop/api/winuser/nf-winuser-dispatchmessage) function.

Because the dialog box keyboard interface uses direction keys to move between controls in a dialog box, an application cannot use these keys to scroll the contents of any modal dialog box or any modeless dialog box for which [**IsDialogMessage**](/windows/desktop/api/Winuser/nf-winuser-isdialogmessagea) is called. When a dialog box has scroll bars, the application must provide an alternate keyboard interface for the scroll bars. Note that the mouse interface for scrolling is available when the system includes a mouse.

### The WS\_TABSTOP Style

The [**WS\_TABSTOP**](/windows/desktop/winmsg/window-styles) style specifies the controls to which the user can move by pressing the TAB key or SHIFT+TAB keys.

When the user presses TAB or SHIFT+TAB, the system first determines whether these keys are processed by the control that currently has the input focus. It sends the control a [**WM\_GETDLGCODE**](wm-getdlgcode.md) message, and if the control returns DLGC\_WANTTAB, the system passes the keys to the control. Otherwise, the system uses the [**GetNextDlgTabItem**](/windows/desktop/api/Winuser/nf-winuser-getnextdlgtabitem) function to locate the next control that is visible, not disabled, and that has the [**WS\_TABSTOP**](/windows/desktop/winmsg/window-styles) style. The search starts with the control currently having the input focus and proceeds in the order in which the controls were created—that is, the order in which they are defined in the dialog box template. When the system locates a control having the required characteristics, the system moves the input focus to it.

If the search for the next control with the [**WS\_TABSTOP**](/windows/desktop/winmsg/window-styles) style encounters a window with the **WS\_EX\_CONTROLPARENT** style, the system recursively searches the window's children.

An application can also use [**GetNextDlgTabItem**](/windows/desktop/api/Winuser/nf-winuser-getnextdlgtabitem) to locate controls having the [**WS\_TABSTOP**](/windows/desktop/winmsg/window-styles) style. The function retrieves the window handle of the next or previous control having the **WS\_TABSTOP** style without moving the input focus.

### The WS\_GROUP Style

By default, the system moves the input focus to the next or previous control whenever the user presses a direction key. As long as the current control with the input focus does not process these keys and the next or previous control is not a static control, the system continues to move the input focus through all controls in the dialog box as the user continues to press the direction keys.

An application can use the [**WS\_GROUP**](/windows/desktop/winmsg/window-styles) style to modify this default behavior. The style marks the beginning of a group of controls. If a control in the group has the input focus when the user begins pressing direction keys, the focus remains in the group. In general, the first control in a group must have the **WS\_GROUP** style and all other controls in the group must not have this style. All controls in the group must be contiguous—that is, they must have been created consecutively with no intervening controls.

When the user presses a direction key, the system first determines whether the current control having the input focus processes the direction keys. The system sends a [**WM\_GETDLGCODE**](wm-getdlgcode.md) message to the control and if the control returns the **DLGC\_WANTARROWS** value, passes the key to the control. Otherwise, the system uses the [**GetNextDlgGroupItem**](/windows/desktop/api/Winuser/nf-winuser-getnextdlggroupitem) function to determine the next control in the group.

[**GetNextDlgGroupItem**](/windows/desktop/api/Winuser/nf-winuser-getnextdlggroupitem) searches controls in the order (or reverse order) they were created. If the user presses the RIGHT or DOWN key, **GetNextDlgGroupItem** returns the next control if that control does not have the [**WS\_GROUP**](/windows/desktop/winmsg/window-styles) style. Otherwise, the function reverses the order of the search and returns the first control that has the **WS\_GROUP** style. If the user presses the LEFT or UP key, the function returns the previous control unless the current control already has the **WS\_GROUP** style. If the current control has this style, the function reverses the order of the search, locates the first control having the **WS\_GROUP** style, and returns the control that immediately precedes the located control.

If the search for the next control in the group encounters a window with the **WS\_EX\_CONTROLPARENT** style, the system recursively searches the window's children.

After the system has the next or previous control, it sends a [**WM\_GETDLGCODE**](wm-getdlgcode.md) message to the control to determine the control type. The system then moves the input focus to control if it is not a static control. If the control is an automatic radio button, the system sends a [**BM\_CLICK**](../controls/bm-click.md) message to it. An application can also use [**GetNextDlgGroupItem**](/windows/desktop/api/Winuser/nf-winuser-getnextdlggroupitem) to locate controls in a group.

Generally, the first control in the group combines the [**WS\_GROUP**](/windows/desktop/winmsg/window-styles) and [**WS\_TABSTOP**](/windows/desktop/winmsg/window-styles) styles so that the user can move from group to group by using the TAB key. If the group contains radio buttons, the application should apply the **WS\_TABSTOP** style only to the first control in the group. The system automatically moves the style when the user moves between controls in the group. This ensures that the input focus will always be on the most recently selected control when the user moves to the group using the TAB key.

### Mnemonics

A mnemonic is a selected letter or digit in the label of a button or in the text of a static control. The system moves the input focus to the control associated with the mnemonic whenever the user either presses the key that corresponds to the mnemonic or presses this key and the ALT key in combination. Mnemonics provide a quick way for the user to move to a specified control by using the keyboard.

An application creates a mnemonic for a control by inserting the ampersand (&) immediately before the selected letter or digit in the label or text for the control. In most cases, the null-terminated string provided with the control in the dialog box template contains the ampersand. However, an application can create a mnemonic at any time by replacing a control's existing label or text by using the [**SetDlgItemText**](/windows/desktop/api/Winuser/nf-winuser-setdlgitemtexta) function. Only one mnemonic can be specified for each control. Although it is recommended, mnemonics in a dialog box need not be unique.

When the user presses a letter or digit key, the system first determines whether the current control having the input focus processes the key. The system sends a [**WM\_GETDLGCODE**](wm-getdlgcode.md) message to the control, and if the control returns the **DLGC\_WANTALLKEYS** or **DLG\_WANTMESSAGE** value, the system passes the key to the control. Otherwise, it searches for a control whose mnemonic matches the specified letter or digit. It continues to search until it locates a control or has examined all controls. During the search, it skips any static controls that have the [**SS\_NOPREFIX**](../controls/static-control-styles.md) style.

If the search for a control with a matching mnemonic encounters a window with the **WS\_EX\_CONTROLPARENT** style, the system recursively searches the window's children.

If the system locates a static control and the control is not disabled, the system moves the input focus to the first control after the static control that is visible, not disabled, and that has the [**WS\_TABSTOP**](/windows/desktop/winmsg/window-styles) style. If the system locates some other control that has a matching mnemonic, it moves the input focus to that control. If the control is a default push button, the system sends a [**BN\_CLICKED**](../controls/bn-clicked.md) notification message to the dialog box procedure. If the control is another style of button and there is no other control in the dialog box having the same mnemonic, the system sends the [**BM\_CLICK**](../controls/bm-click.md) message to the control.

## Dialog Box Settings

The dialog box settings are the current selections and values for the controls in the dialog box. The dialog box procedure is responsible for initializing the controls to these settings when creating the dialog box. It is also responsible for retrieving the current settings from the controls before destroying the dialog box. The methods used to initialize and retrieve settings depend on the type of control.

For more information, see the following topics:

-   [Radio Buttons and Check Boxes](#radio-buttons-and-check-boxes)
-   [Dialog Box Edit Controls](#dialog-box-edit-controls)
-   [List Boxes, Combo Boxes, and Directory Listings](#list-boxes-combo-boxes-and-directory-listings)
-   [Dialog Box Control Messages](#dialog-box-control-messages)

### Radio Buttons and Check Boxes

Dialog boxes use radio buttons and check boxes to let the user choose from a list of options. Radio buttons let the user choose from mutually exclusive options; check boxes let the user pick a combination of options.

The dialog box procedure can set the initial state of a check box by using the [**CheckDlgButton**](https://msdn.microsoft.com/library/Cc410649(v=MSDN.10).aspx) function, which sets or clears the check box. For radio buttons in a group of mutually exclusive radio buttons, the dialog box procedure can use the [**CheckRadioButton**](https://msdn.microsoft.com/library/Cc410654(v=MSDN.10).aspx) function to set the appropriate radio button and automatically clear any other radio button.

Before a dialog box terminates, the dialog box procedure can check the state of each radio button and check box by using the [**IsDlgButtonChecked**](https://msdn.microsoft.com/library/Cc364806(v=MSDN.10).aspx) function, which returns the current state of the button. A dialog box typically saves this information to initialize the buttons the next time it creates the dialog box.

### Dialog Box Edit Controls

Many dialog boxes have edit controls that let the user supply text as input. Most dialog box procedures initialize an edit control when the dialog box first starts. For example, the dialog box procedure may place a proposed filename in the control that the user can then select, modify, or replace. The dialog box procedure can set the text in an edit control by using the [**SetDlgItemText**](/windows/desktop/api/Winuser/nf-winuser-setdlgitemtexta) function, which copies text from a specified buffer to the edit control. When the edit control receives the input focus, it automatically selects the complete text for editing.

Because edit controls do not automatically return their text to the dialog box, the dialog box procedure must retrieve the text before it terminates. It can retrieve the text by using the [**GetDlgItemText**](/windows/desktop/api/Winuser/nf-winuser-getdlgitemtexta) function, which copies the edit control text to a buffer. The dialog box procedure typically saves this text to initialize the edit control later or passes it on to the parent window for processing.

Some dialog boxes use edit controls that let the user enter numbers. The dialog box procedure can retrieve a number from an edit control by using the [**GetDlgItemInt**](/windows/desktop/api/Winuser/nf-winuser-getdlgitemint) function, which retrieves the text from the edit control and converts the text to a decimal value. The user types the number in decimal digits. It can be either signed or unsigned. The dialog box procedure can display an integer by using the [**SetDlgItemInt**](/windows/desktop/api/Winuser/nf-winuser-setdlgitemint) function. **SetDlgItemInt** converts a signed or unsigned integer to a string of decimal digits.

### List Boxes, Combo Boxes, and Directory Listings

Some dialog boxes display lists of names from which the user can select one or more names. To display a list of filenames, for example, a dialog box typically uses a list box and the [**DlgDirList**](https://msdn.microsoft.com/library/Cc410788(v=MSDN.10).aspx) and [**DlgDirSelectEx**](https://msdn.microsoft.com/library/Cc410769(v=MSDN.10).aspx) functions. The **DlgDirList** function automatically fills a list box with the filenames in the current directory. The **DlgDirSelect** function retrieves the selected filename from the list box. Together, these two functions provide a convenient way for a dialog box to display a directory listing so the user can select a file without having to type its name and location.

A dialog box can also use a combo box to display a list of filenames. The [**DlgDirListComboBox**](https://msdn.microsoft.com/library/Cc410798(v=MSDN.10).aspx) function automatically fills a list box portion of the combo box with the filenames in the current directory. The [**DlgDirSelectComboBoxEx**](https://msdn.microsoft.com/library/Cc410768(v=MSDN.10).aspx) function retrieves a selected filename from the list box portion.

### Dialog Box Control Messages

Many controls recognize predefined messages that, when received by controls, cause them to carry out some action. For example, the [**BM\_SETCHECK**](../controls/bm-setcheck.md) message sets the check in a check box and the [**EM\_GETSEL**](../controls/em-getsel.md) message retrieves the portion of the control's text that is currently selected. The control messages give a dialog procedure greater and more flexible access to the controls than the standard functions, so they are often used when the dialog box requires complex interactions with the user.

A dialog box procedure can send a message to a control by supplying the control identifier and using the [**SendDlgItemMessage**](/windows/desktop/api/Winuser/nf-winuser-senddlgitemmessagea) function, which is identical to the [**SendMessage**](/windows/desktop/api/winuser/nf-winuser-sendmessage) function, except that it uses a control identifier instead of a window handle to identify the control that is to receive the message. A specified message may require that the dialog procedure send parameters with the message, and the message may have corresponding return values. The operation and requirements of each control message depends on the purpose of the message and the control that processes it.

For more information about the control messages, see [Windows Controls](../controls/window-controls.md).

## Custom Dialog Boxes

An application can create custom dialog boxes by using an application-defined window class for the dialog boxes instead of using the predefined dialog box class. Applications typically use this method when a dialog box is their main window, but it is also useful for creating modal and modeless dialog boxes for applications that have standard overlapping windows.

The application-defined window class allows the application to define a window procedure for the dialog box and process messages before sending them to the dialog box procedure. It also lets the application define a class icon, a class background brush, and a class menu for the dialog box. The application must register the window class before attempting to create a dialog box and must provide the dialog box template with the atom value or name of the window class.

Many applications create a new dialog box class by first retrieving the class information for the predefined dialog box class, and passing it to the [**GetClassInfo**](/windows/desktop/api/winuser/nf-winuser-getclassinfoa) function, which fills a [**WNDCLASS**](/windows/win32/api/winuser/ns-winuser-wndclassa) structure with the information. The application modifies individual members of the structure, such as the class name, brush, and icon, then registers the new class by using the [**RegisterClass**](/windows/desktop/api/winuser/nf-winuser-registerclassa) function. If an application fills the **WNDCLASS** structure on its own, it must set the **cbWndExtra** member to the **DLGWINDOWEXTRA**, which is the number of extra bytes the system requires for each dialog box. If an application also uses extra bytes for each dialog box, they must be beyond the extra bytes required by the system.

The window procedure for the custom dialog box has the same parameters and requirements as any other window procedure. Unlike other window procedures, however, the window procedure for this dialog box should call the [**DefDlgProc**](/windows/desktop/api/Winuser/nf-winuser-defdlgprocw) function instead of the [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function for any messages it does not process. **DefDlgProc** carries out the same default message processing as the window procedure for the predefined dialog box, which includes calling the dialog box procedure.

An application can also create custom dialog boxes by subclassing the window procedure of the predefined dialog box. The [**SetWindowLong**](/windows/desktop/api/winuser/nf-winuser-setwindowlonga) function lets an application specify the window procedure for a specified window. The application may also attempt to subclass by using the [**SetClassLong**](/windows/desktop/api/winuser/nf-winuser-setclasslonga) function, but doing so affects all dialog boxes in the system, not just those belonging to the application.

Applications that create custom dialog boxes sometimes provide an alternate keyboard interface for the dialog boxes. For modeless dialog boxes, this may mean the application does not call the [**IsDialogMessage**](/windows/desktop/api/Winuser/nf-winuser-isdialogmessagea) function and instead processes all keyboard input in the custom window procedure. In such cases, the application can use the [**WM\_NEXTDLGCTL**](wm-nextdlgctl.md) message to minimize the code needed to move the input focus from one control to another. This message, when passed to [**DefDlgProc**](/windows/desktop/api/Winuser/nf-winuser-defdlgprocw), moves the input focus to a specified control and updates the appearance of the controls, such as moving the default push button border or setting an automatic radio button.
