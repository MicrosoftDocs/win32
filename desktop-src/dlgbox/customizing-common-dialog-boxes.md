---
title: Customizing Common Dialog Boxes
description: This topic discusses how to use common dialog boxes.
ms.assetid: 31ba9deb-32e6-455c-be0e-ff8bcc691c80
keywords:
- Common Dialog Box Library,customizing
- common dialog boxes,customizing
- customizing common dialog boxes
ms.topic: article
ms.date: 05/31/2018
---

# Customizing Common Dialog Boxes

You can use the common dialog boxes in their standard form, or you can customize them. From the user's perspective, the chief benefit of the common dialog box is its consistent appearance and functionality from application to application. Therefore, it is important that you customize a common dialog box only when it is absolutely necessary for an application. Otherwise, the consistent appearance and simple coding interface are lost. Appropriate customizations leave intact as many of the original controls as possible. Increasing the size of the dialog box or adding new controls in the space already available in the dialog box is an appropriate customization. Hiding original controls or otherwise changing the intended functionality of the original controls is a less appropriate customization.

This section discusses the following methods for customizing a common dialog box:

-   [Custom Templates](#custom-templates)
-   [Hook Procedures for Common Dialog Boxes](#hook-procedures-for-common-dialog-boxes)
-   [Common Dialog Messages](#common-dialog-messages)
-   [Help Support](#help-support)
    -   [Context-Sensitive Help](#context-sensitive-help)
    -   [The Help Button](#the-help-button)

## Custom Templates

Common dialog boxes have default templates that define the number, type, and position of the standard controls in the dialog box. You can define a custom template to give users access to additional controls that are unique to your application.

For all common dialog boxes except the Explorer-style **Open** and **Save As** dialog boxes, you modify the default template to create a custom template that replaces the default template. The custom template defines the type and position of the standard controls as well as any additional controls.

When you create a custom dialog box template by modifying the default dialog box template, make sure the identifiers for any added controls are unique and do not conflict with the identifiers of the standard controls. The following table lists the name of the default template file and include file for each of the common dialog box types.



| Dialog box type               | Template file | Include file |
|-------------------------------|---------------|--------------|
| **Color**                     | Color.dlg     | ColorDlg.h   |
| **Find**                      | Findtext.dlg  | Dlgs.h       |
| **Font**                      | Font.dlg      | Dlgs.h       |
| **Open** (multiple selection) | Fileopen.dlg  | Dlgs.h       |
| **Open** (single selection)   | Fileopen.dlg  | Dlgs.h       |
| **Page Setup**                | Prnsetup.dlg  | Dlgs.h       |
| **Print**                     | Prnsetup.dlg  | Dlgs.h       |
| **Print Setup** (obsolete)    | Prnsetup.dlg  | Dlgs.h       |
| **Replace**                   | Findtext.dlg  | Dlgs.h       |



 

To enable a custom template, you must set a flag in the **Flags** member of the corresponding structure for the dialog box. If the template is a resource in an application or dynamic-link library, set an **ENABLETEMPLATE** flag in the **Flags** member, and use the **hInstance** and **lpTemplateName** members of the structure to identify the module and resource name. If the template is already in memory, set an **ENABLETEMPLATEHANDLE** flag in the **Flags** member, and use the **hInstance** member to identify the memory object that contains the template.

In most cases, you must also enable a hook procedure for the dialog box to support and process input for the additional controls in your custom template.

For the Explorer-style **Open** and **Save As** dialog boxes, the default templates are not available for modification. Instead, your custom template defines a child dialog box that includes only the items to be added to the standard dialog box. The custom template can also define a static control that specifies the location of the cluster of standard controls in the child dialog box. For more information, see [Explorer-Style Custom Templates](open-and-save-as-dialog-boxes.md).

## Hook Procedures for Common Dialog Boxes

For each of the common dialog boxes, you can enable a hook procedure to process messages from the default dialog box procedure. There are two general types of common dialog hook procedures:

-   The standard hook procedure used with most common dialog boxes
-   The Explorer-style hook procedure supported by the **Open** and **Save As** dialog boxes

When you provide a standard hook procedure for one of the common dialog boxes, the default dialog box procedure handles its messages as follows.



| Message                                 | Handling                                                                                                                                                                                                             |
|-----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WM\_INITDIALOG**](wm-initdialog.md) | The default dialog box procedure processes the message before passing it to the hook procedure. The message's *lParam* parameter is a pointer to the initialization structure specified when the dialog was created. |
| All other messages                      | The hook procedure receives the message first. Then, the return value of the hook procedure determines whether the default dialog procedure processes the message or ignores it.                                     |



 

For the Explorer-style **Open** and **Save As** dialog boxes, the hook procedure does not receive messages intended for the standard controls in the dialog box. Instead, it receives notification messages from the dialog box and messages for any additional controls that you defined in a custom template. For more information, see [Explorer-Style Hook Procedures](open-and-save-as-dialog-boxes.md).

To enable a hook procedure, set an **ENABLEHOOK** value in the **Flags** member of the corresponding structure for the dialog box. If an **ENABLEHOOK** flag is set, an **lpfnHook** member of the structure must specify the address of the hook procedure.

The following table shows the type of hook procedure to provide for each of the common dialog boxes.



| Dialog box type                          | Hook procedure                                      |
|------------------------------------------|-----------------------------------------------------|
| **Color**                                | [*CCHookProc*](/windows/win32/api/commdlg/nc-commdlg-lpcchookproc)                      |
| **Find** or **Replace**                  | [*FRHookProc*](/windows/win32/api/commdlg/nc-commdlg-lpfrhookproc)                      |
| **Font**                                 | [*CFHookProc*](/windows/win32/api/commdlg/nc-commdlg-lpcfhookproc)                      |
| **Open** or **Save As** (Explorer-style) | [*OFNHookProc*](/windows/win32/api/commdlg/nc-commdlg-lpofnhookproc)                    |
| **Open** or **Save As** (Old-style)      | [*OFNHookProcOldStyle*](/previous-versions/windows/desktop/legacy/ms646932(v=vs.85)) |
| **Print**                                | [*PrintHookProc*](/windows/win32/api/commdlg/nc-commdlg-lpprinthookproc)                |
| **Page Setup**                           | [*PageSetupHook*](/windows/win32/api/commdlg/nc-commdlg-lppagesetuphook)                |



 

For the **Page Setup** dialog box, you can also specify a [*PagePaintHook*](/windows/win32/api/commdlg/nc-commdlg-lppagepainthook) hook procedure. This is a special hook procedure that you can use to customize the appearance of the sample page displayed by the **Page Setup** dialog box.

> [!Note]  
> The **Print Setup** dialog box has been superseded by the **Page Setup** dialog box. Applications should use the **Page Setup** dialog box. However, for compatibility, the [**PrintDlg**](/previous-versions/windows/desktop/legacy/ms646940(v=vs.85)) function continues to support display of the **Print Setup** dialog box. You can provide a [*SetupHookProc*](/windows/win32/api/commdlg/nc-commdlg-lpsetuphookproc) hook procedure for the **Print Setup** dialog box.

 

## Common Dialog Messages

Common dialog boxes use messages to notify your window procedure or hook procedure when certain events occur. In addition, there are messages that you can send to a common dialog box to retrieve information or to control the behavior or appearance of the dialog box. This section describes the common dialog messages registered by the [**RegisterWindowMessage**](/windows/desktop/api/winuser/nf-winuser-registerwindowmessagea) function, messages used by the **Font** dialog box and **Page Setup** dialog box, and messages used by the Explorer-style **Open** and **Save As** dialog boxes.

The Common Dialog Box Library defines a set of message strings. You can pass a constant associated with one of these message strings to [**RegisterWindowMessage**](/windows/desktop/api/winuser/nf-winuser-registerwindowmessagea) to get a message identifier. You can then use the identifier to detect and process messages sent from a common dialog box, or to send messages to a common dialog box. The following table shows the message constants and describes their use.



| Contants                               | Use                                                                                                                                                                                                                                                                                                                                                                                                                    |
|----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**COLOROKSTRING**](colorokstring.md) | A **Color** dialog box sends this message to the hook procedure when the user selects a color and clicks the **OK** button. The hook procedure can accept the color, or reject it and force the dialog box to remain open.                                                                                                                                                                                             |
| [**FILEOKSTRING**](fileokstring.md)   | An **Open** or **Save As** dialog box sends this message to the hook procedure when the user selects a file name and clicks the **OK** button. The hook procedure can accept the file name, or reject it and force the dialog box to remain open. For Explorer-style **Open** and **Save As** dialog boxes, this message has been superseded by the [**CDN\_FILEOK**](cdn-fileok.md) notification message.<br/> |
| [**FINDMSGSTRING**](findmsgstring.md) | A **Find** or **Replace** dialog box sends this message to the window procedure of its parent window when the user clicks the **Find Next**, **Replace**, or **Replace All**, or closes the dialog box. The message's *lParam* parameter is a pointer to a [**FINDREPLACE**](/windows/win32/api/commdlg/ns-commdlg-findreplacea) structure containing the user's input.                                                                               |
| [**HELPMSGSTRING**](helpmsgstring.md) | All common dialog boxes send this message to the window procedure of their parent window when the user clicks the **Help** button. For Explorer-style **Open** and **Save As** dialog boxes, this message has been superseded by the [**CDN\_HELP**](cdn-help.md) notification message.<br/>                                                                                                                    |
| [**LBSELCHSTRING**](lbselchstring.md) | An **Open** or **Save As** dialog box sends this message to the hook procedure when the user changes the selection in the **File Name** list box. For Explorer-style **Open** and **Save As** dialog boxes, this message has been superseded by the [**CDN\_SELCHANGE**](cdn-selchange.md) notification message.<br/>                                                                                           |
| [**SETRGBSTRING**](setrgbstring.md)   | A hook procedure can send this message to a **Color** dialog box to set the current color selection.                                                                                                                                                                                                                                                                                                                   |
| [**SHAREVISTRING**](sharevistring.md) | An **Open** or **Save As** dialog box sends this message to the hook procedure if a sharing violation occurs for the selected file when the user clicks the **OK** button. For Explorer-style **Open** and **Save As** dialog boxes, this message has been superseded by the [**CDN\_SHAREVIOLATION**](cdn-shareviolation.md) notification message.<br/>                                                        |



 

Some common dialog boxes send and receive other window messages. The hook procedure for a **Font** dialog box can send any of the **WM\_CHOOSEFONT\_\*** messages to the **Font** dialog box. For more information, see [Font Dialog Box](font-dialog-box.md). The **Page Setup** dialog box sends the **WM\_PSD\_\*** messages if you have enabled a [*PagePaintHook*](/windows/win32/api/commdlg/nc-commdlg-lppagepainthook) hook procedure. For more information, see [Page Setup Dialog Box](page-setup-dialog-box.md).

The Explorer-style **Open** and **Save As** dialog boxes support a set of predefined messages. These include notification messages sent in the form of a [**WM\_NOTIFY**](../controls/wm-notify.md) message to your hook procedure, and messages that your hook procedure can send to the dialog box. For a complete list of these messages, see [Explorer-Style Hook Procedures](open-and-save-as-dialog-boxes.md).

## Help Support

Common dialog boxes provide context-sensitive help for the standard controls of the dialog box. To provide additional help for a common dialog box, you can display a **Help** button and process messages generated when the user clicks the button. The **Help** button is a supplement to the default context-sensitive help. The **Help** button is useful for describing the general purpose of the dialog box as it applies to your application.

-   [Context-Sensitive Help](#context-sensitive-help)
-   [The Help Button](#the-help-button)

### Context-Sensitive Help

All common dialog boxes provide context-sensitive help for the standard controls of the dialog box. The user can display help for individual controls by any of the following methods:

-   Selecting the control and pressing the F1 key.
-   Clicking the **?** button in the title bar and subsequently clicking on a control.
-   Clicking the right mouse button over a control.

If you customize a dialog box by adding new controls, you must also extend help support for these controls by processing requests for help in the hook procedure. The hook procedure receives the following messages when the user requests help.



| User action                                                           | Message                                      |
|-----------------------------------------------------------------------|----------------------------------------------|
| Click the right mouse button over a control.                          | [**WM\_CONTEXTMENU**](/windows/desktop/menurc/wm-contextmenu) |
| Pressed the F1 key.                                                   | [**WM\_HELP**](../shell/wm-help.md)               |
| Clicked the **?** button on the title bar and then clicked a control. | [**WM\_HELP**](../shell/wm-help.md)               |



 

You should process these messages for the controls you have added, but let the default dialog box procedure process the messages for the standard controls. For more information about how to process these messages, see [Help](/previous-versions/windows/desktop/legacy/bb776786(v=vs.85)).

### The Help Button

You can display a **Help** button in any of the common dialog boxes by setting a **SHOWHELP** value in the **Flags** member of the initialization structure for the dialog box. If you display the **Help** button, you must process the user's request for help. The processing can be done either in one of your application's window procedures or in a hook procedure for the dialog box. Typically, you would process the request for help by calling the [**WinHelp**](/windows/win32/api/winuser/nf-winuser-winhelpa) function.

To process help messages in one of your window procedures, you must get a message identifier for the string defined by the [**HELPMSGSTRING**](helpmsgstring.md) value and identify the window to receive messages. To get the message identifier, specify **HELPMSGSTRING** as the parameter in a call to the [**RegisterWindowMessage**](/windows/desktop/api/winuser/nf-winuser-registerwindowmessagea) function. When you create the dialog box, use the **hwndOwner** member of the dialog box initialization structure to identify the window that is to receive the messages. The dialog box procedure sends the message to the window procedure whenever the user clicks the **Help** button.

To process help messages in a hook procedure, you should process the [**WM\_COMMAND**](/windows/desktop/menurc/wm-command) message. The hook procedure provides help if the *wParam* parameter of this message indicates that the user clicked the **Help** button. The identifier of the **Help** button is the **pshHelp** constant defined in the Dlgs.h file.

Hook procedures for the Explorer-style **Open** and **Save As** dialog boxes do not receive [**WM\_COMMAND**](/windows/desktop/menurc/wm-command) messages for the **Help** button. Instead, the dialog box sends a [**CDN\_HELP**](cdn-help.md) notification message to the hook procedure when the **Help** button is clicked.

 

