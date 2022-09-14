---
title: About Dialog Boxes
description: This topic discusses using dialog boxes to create user interfaces for applications.
ms.assetid: 51960c28-a178-4ad3-b45e-426fec42a945
keywords:
- dialog boxes,about
- dialog boxes,when to use
- modal dialog boxes
- modeless dialog boxes
- dialog boxes,modal
- dialog boxes,modeless
- dialog boxes,templates
- dialog boxes,owner windows
- dialog boxes,message boxes
- dialog box procedures
- message boxes
ms.topic: article
ms.date: 05/31/2018
---

# About Dialog Boxes

There are many functions, messages, and predefined controls to help create and manage dialog boxes, thus making it easier to develop the user interface for an application. This overview describes the dialog box functions and messages and explains how to use them to create and use dialog boxes.

This overview includes the following topics:

-   [When to Use a Dialog Box](#when-to-use-a-dialog-box)
-   [Dialog Box Owner Window](#dialog-box-owner-window)
-   [Message Boxes](#message-boxes)
-   [Modal Dialog Boxes](#modal-dialog-boxes)
-   [Modeless Dialog Boxes](#modeless-dialog-boxes)
-   [Dialog Box Templates](#dialog-box-templates)
    -   [Dialog Box Template Styles](#dialog-box-template-styles)
    -   [Dialog Box Measurements](#dialog-box-measurements)
    -   [Dialog Box Controls](#dialog-box-controls)
    -   [Dialog Box Window Menu](#dialog-box-window-menu)
    -   [Dialog Box Fonts](#dialog-box-fonts)
    -   [Templates in Memory](#templates-in-memory)

For more information about the common dialog boxes, see [Common Dialog Box Library](common-dialog-box-library.md).

## When to Use a Dialog Box

Most applications use dialog boxes to prompt for additional information for menu items that require user input. Using a dialog box is the only recommended way for an application to retrieve the input. For example, a typical **Open** menu item requires the name of a file to open, so an application should use a dialog box to prompt the user for the name. In such cases, the application creates the dialog box when the user clicks the menu item and destroys the dialog box immediately after the user supplies the information.

Many applications also use dialog boxes to display information or options while the user works in another window. For example, word processing applications often use a dialog box with a text-search option. While the application searches for the text, the dialog box remains on the screen. The user can then return to the dialog box and search for the same word again; or the user can change the entry in the dialog box and search for a new word. Applications that use dialog boxes in this way typically create one when the user clicks the menu item and continue to display it for as long as the application runs or until the user explicitly closes the dialog box.

To support the different ways applications use dialog boxes, there are two types of dialog box: modal and modeless. A *modal dialog box* requires the user to supply information or cancel the dialog box before allowing the application to continue. Applications use modal dialog boxes in conjunction with menu items that require additional information before they can proceed. A *modeless dialog box* allows the user to supply information and return to the previous task without closing the dialog box. Modal dialog boxes are simpler to manage than modeless dialog boxes because they are created, perform their task, and are destroyed by calling a single function.

To create either a modal or modeless dialog box, an application must supply a dialog box template to describe the dialog box style and content; the application must also supply a dialog box procedure to carry out tasks. The *dialog box template* is a binary description of the dialog box and the controls it contains. The developer can create this template as a resource to be loaded from the application's executable file, or created in memory while the application runs. The *dialog box procedure* is an application-defined callback function that the system calls when it has input for the dialog box or tasks for the dialog box to carry out. Although a dialog box procedure is similar to a window procedure, it does not have the same responsibilities.

An application typically creates a dialog box by using either the [**DialogBox**](/windows/desktop/api/Winuser/nf-winuser-dialogboxa) or [**CreateDialog**](/windows/desktop/api/Winuser/nf-winuser-createdialoga) function. **DialogBox** creates a modal dialog box; **CreateDialog** creates a modeless dialog box. These two functions load a dialog box template from the application's executable file and create a pop-up window that matches the template's specifications. There are other functions that create a dialog box by using templates in memory; they pass additional information to the dialog box procedure as the dialog box is created.

Dialog boxes usually belong to a predefined, exclusive window class. The system uses this window class and its corresponding window procedure for both modal and modeless dialog boxes. When the function is called, it creates the window for the dialog box, as well as the windows for the controls in the dialog box, then sends selected messages to the dialog box procedure. While the dialog box is visible, the predefined window procedure manages all messages, processing some messages and passing others to the dialog box procedure so that the procedure can carry out tasks. Applications do not have direct access to the predefined window class or window procedure, but they can use the dialog box template and dialog box procedure to modify the style and behavior of a dialog box.

## Dialog Box Owner Window

Most dialog boxes have an owner window (or more simply, an owner). When creating the dialog box, the application sets the owner by specifying the owner's window handle. The system uses the owner to determine the position of the dialog box in the Z order so that the dialog box is always positioned above its owner. Also, the system can send messages to the window procedure of the owner, notifying it of events in the dialog box.

The system automatically hides or destroys the dialog box whenever its owner is hidden or destroyed. This means the dialog box procedure requires no special processing to detect changes to the state of the owner window.

Because the typical dialog box is used in conjunction with a menu item, the owner window is usually the window containing the menu. Although it is possible to create a dialog box that has no owner, it is not recommended. For example, when a modal dialog box has no owner, the system does not disable any of the application's other windows and allows the user to continue to carry out work in the other windows, defeating the purpose of the modal dialog box.

When a modeless dialog box has no owner, the system neither hides nor destroys the dialog box when other windows in the application are hidden or destroyed. Although this does not defeat the purpose of the modeless dialog box, it requires that the application carry out special processing to ensure the dialog box is hidden and destroyed at appropriate times.

## Message Boxes

A message box is a special dialog box that an application can use to display messages and prompt for simple input. A message box typically contains a text message and one or more buttons. An application creates the message box by using the [**MessageBox**](/windows/desktop/api/Winuser/nf-winuser-messagebox) or [**MessageBoxEx**](/windows/desktop/api/Winuser/nf-winuser-messageboxexa) function, specifying the text and the number and types of buttons to display. Note that currently there is no difference between how **MessageBox** and **MessageBoxEx** work.

Although the message box is a dialog box, the system takes complete control of the creation and management of the message box. This means the application does not provide a dialog box template and dialog box procedure. The system creates its own template based on the text and buttons specified for the message box and supplies its own dialog box procedure.

A message box is a modal dialog box and the system creates it by using the same internal functions that [**DialogBox**](/windows/desktop/api/Winuser/nf-winuser-dialogboxa) uses. If the application specifies an owner window when calling [**MessageBox**](/windows/desktop/api/Winuser/nf-winuser-messagebox) or [**MessageBoxEx**](/windows/desktop/api/Winuser/nf-winuser-messageboxexa), the system disables the owner. An application can also direct the system to disable all top-level windows belonging to the current thread by specifying the **MB\_TASKMODAL** value when creating the dialog box.

The system can send messages to the owner, such as [**WM\_CANCELMODE**](/windows/desktop/winmsg/wm-cancelmode) and [**WM\_ENABLE**](/windows/desktop/winmsg/wm-enable), just as it does when creating a modal dialog box. The owner window should carry out any actions requested by these messages.

## Modal Dialog Boxes

A modal dialog box should be a pop-up window having a window menu, a title bar, and a thick border; that is, the dialog box template should specify the **WS\_POPUP**, **WS\_SYSMENU**, **WS\_CAPTION**, and **DS\_MODALFRAME** styles. Although an application can designate the **WS\_VISIBLE** style, the system always displays a modal dialog box regardless of whether the dialog box template specifies the **WS\_VISIBLE** style. An application must not create a modal dialog box having the **WS\_CHILD** style. A modal dialog box with this style disables itself, preventing any subsequent input from reaching the application.

An application creates a modal dialog box by using either the [**DialogBox**](/windows/desktop/api/Winuser/nf-winuser-dialogboxa) or [**DialogBoxIndirect**](/windows/desktop/api/Winuser/nf-winuser-dialogboxindirecta) function. **DialogBox** requires the name or identifier of a resource containing a dialog box template; **DialogBoxIndirect** requires a handle to a memory object containing a dialog box template. The [**DialogBoxParam**](/windows/desktop/api/Winuser/nf-winuser-dialogboxparama) and [**DialogBoxIndirectParam**](/windows/desktop/api/Winuser/nf-winuser-dialogboxindirectparama) functions also create modal dialog boxes; they are identical to the previously mentioned functions but pass a specified parameter to the dialog box procedure when the dialog box is created.

When creating the modal dialog box, the system makes it the active window. The dialog box remains active until the dialog box procedure calls the [**EndDialog**](/windows/desktop/api/Winuser/nf-winuser-enddialog) function or the system activates a window in another application. Neither the user nor the application can make the owner window active until the modal dialog box is destroyed.

When the owner window is not already disabled, the system automatically disables the window and any child windows belonging to it when it creates the modal dialog box. The owner window remains disabled until the dialog box is destroyed. Although a dialog box procedure could potentially enable the owner window at any time, enabling the owner defeats the purpose of the modal dialog box and is not recommended. When the dialog box procedure is destroyed, the system enables the owner window again, but only if the modal dialog box caused the owner to be disabled.

As the system creates the modal dialog box, it sends the [**WM\_CANCELMODE**](/windows/desktop/winmsg/wm-cancelmode) message to the window (if any) currently capturing mouse input. An application that receives this message should release the mouse capture so that the user can move the mouse in the modal dialog box. Because the system disables the owner window, all mouse input is lost if the owner fails to release the mouse upon receiving this message.

To process messages for the modal dialog box, the system starts its own message loop, taking temporary control of the message queue for the entire application. When the system retrieves a message that is not explicitly for the dialog box, it dispatches the message to the appropriate window. If it retrieves a [**WM\_QUIT**](/windows/desktop/winmsg/wm-quit) message, it posts the message back to the application message queue so that the application's main message loop can eventually retrieve the message.

The system sends the [**WM\_ENTERIDLE**](wm-enteridle.md) message to the owner window whenever the application message queue is empty. The application can use this message to carry out a background task while the dialog box remains on the screen. When an application uses the message in this way, the application must frequently yield control (for example, by using the [**PeekMessage**](/windows/desktop/api/winuser/nf-winuser-peekmessagea) function) so that the modal dialog box can receive any user input. To prevent the modal dialog box from sending the **WM\_ENTERIDLE** messages, the application can specify the DS\_NOIDLEMSG style when creating the dialog box.

An application destroys a modal dialog box by using the [**EndDialog**](/windows/desktop/api/Winuser/nf-winuser-enddialog) function. In most cases, the dialog box procedure calls **EndDialog** when the user clicks **Close** from the dialog box's window menu or clicks the **OK** or **Cancel** button in the dialog box. The dialog box can return a value through the [**DialogBox**](/windows/desktop/api/Winuser/nf-winuser-dialogboxa) function (or other creation functions) by specifying a value when calling the **EndDialog** function. The system returns this value after destroying the dialog box. Most applications use this return value to determine whether the dialog box completed its task successfully or was canceled by the user. The system does not return control from the function that creates the dialog box until the dialog box procedure has called the **EndDialog** function.

## Modeless Dialog Boxes

A modeless dialog box should be a pop-up window having a window menu, a title bar, and a thin border; that is, the dialog box template should specify the **WS\_POPUP**, **WS\_CAPTION**, **WS\_BORDER**, and **WS\_SYSMENU** styles. The system does not automatically display the dialog box unless the template specifies the **WS\_VISIBLE** style.

An application creates a modeless dialog box by using the [**CreateDialog**](/windows/desktop/api/Winuser/nf-winuser-createdialoga) or [**CreateDialogIndirect**](/windows/desktop/api/Winuser/nf-winuser-createdialogindirecta) function. **CreateDialog** requires the name or identifier of a resource containing a dialog box template; **CreateDialogIndirect** requires a handle to a memory object containing a dialog box template. Two other functions, [**CreateDialogParam**](/windows/desktop/api/Winuser/nf-winuser-createdialogparama) and [**CreateDialogIndirectParam**](/windows/desktop/api/Winuser/nf-winuser-createdialogindirectparama), also create modeless dialog boxes; they pass a specified parameter to the dialog box procedure when the dialog box is created.

[**CreateDialog**](/windows/desktop/api/Winuser/nf-winuser-createdialoga) and other creation functions return a window handle to the dialog box. The application and the dialog box procedure can use this handle to manage the dialog box. For example, if **WS\_VISIBLE** is not specified in the dialog box template, the application can display the dialog box by passing the window handle to the [**ShowWindow**](/windows/desktop/api/winuser/nf-winuser-showwindow) function.

A modeless dialog box neither disables the owner window nor sends messages to it. When creating the dialog box, the system makes it the active window, but the user or the application can change the active window at any time. If the dialog box does become inactive, it remains above the owner window in the Z order, even if the owner window is active.

The application is responsible for retrieving and dispatching input messages to the dialog box. Most applications use the main message loop for this. To permit the user to move to and select controls by using the keyboard, however, the application must call the [**IsDialogMessage**](/windows/desktop/api/Winuser/nf-winuser-isdialogmessagea) function. For more information about this function, see [Dialog Box Keyboard Interface](dlgbox-programming-considerations.md).

A modeless dialog box cannot return a value to the application as a modal dialog box does, but the dialog box procedure can send information to the owner window by using the [**SendMessage**](/windows/desktop/api/winuser/nf-winuser-sendmessage) function.

An application must destroy all modeless dialog boxes before terminating. It can destroy a modeless dialog box by using the [**DestroyWindow**](/windows/desktop/api/winuser/nf-winuser-destroywindow) function. In most cases, the dialog box procedure calls **DestroyWindow** in response to user input, such as clicking the **Cancel** button. If the user never closes the dialog box in this way, the application must call **DestroyWindow**.

[**DestroyWindow**](/windows/desktop/api/winuser/nf-winuser-destroywindow) invalidates the window handle to the dialog box, so any subsequent calls to functions that use the handle return error values. To prevent errors, the dialog box procedure should notify the owner that the dialog box has been destroyed. Many applications maintain a global variable containing the handle to the dialog box. When the dialog box procedure destroys the dialog box, it also sets the global variable to **NULL**, indicating that the dialog box is no longer valid.

The dialog box procedure must not call the [**EndDialog**](/windows/desktop/api/Winuser/nf-winuser-enddialog) function to destroy a modeless dialog box.

## Dialog Box Templates

A dialog box template is binary data that describes the dialog box, defining its height, width, style, and the controls it contains. To create a dialog box, the system either loads a dialog box template from the resources in the application's executable file or uses the template passed to it in global memory by the application. In either case, the application must supply a template when creating a dialog box.

A developer creates template resources by using a resource compiler or a dialog box editor. A resource compiler converts a text description into a binary resource, and a dialog box editor saves an interactively constructed dialog box as a binary resource.

> [!Note]  
> An explanation of how to create template resources and add them to the application's executable file is beyond the scope of this overview. For more information about creating template resources and adding them to an executable file, see the documentation provided with your application development tools.

 

To create a dialog box without using template resources, you must create a template in memory and pass it to the [**CreateDialogIndirectParam**](/windows/desktop/api/Winuser/nf-winuser-createdialogindirectparama) or [**DialogBoxIndirectParam**](/windows/desktop/api/Winuser/nf-winuser-dialogboxindirectparama) function, or to the [**CreateDialogIndirect**](/windows/desktop/api/Winuser/nf-winuser-createdialogindirecta) or [**DialogBoxIndirect**](/windows/desktop/api/Winuser/nf-winuser-dialogboxindirecta) macro.

A dialog box template in memory consists of a header that describes the dialog box, followed by one or more additional blocks of data that describe each of the controls in the dialog box. The template can use either the standard format or the extended format. In a standard template, the header is a [**DLGTEMPLATE**](/windows/desktop/api/Winuser/ns-winuser-dlgtemplate) structure followed by additional variable-length arrays; and the data for each control consists of a [**DLGITEMTEMPLATE**](/windows/desktop/api/Winuser/ns-winuser-dlgitemtemplate) structure followed by additional variable-length arrays. In an extended dialog box template, the header uses the [**DLGTEMPLATEEX**](dlgtemplateex.md) format and the control definitions use the [**DLGITEMTEMPLATEEX**](dlgitemtemplateex.md) format.

You can create a memory template by allocating a global memory object and filling it with the standard or extended header and control definitions. A memory template is identical in form and content to a template resource. Many applications that use memory templates first use the [**LoadResource**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadresource) function to load a template resource into memory, then modify the loaded resource to create a new memory template. For more information about creating a dialog box template in memory, see [Templates in Memory](#templates-in-memory).

The following sections describe the styles, measurements, and other values used in a dialog box template.

-   [Dialog Box Template Styles](#dialog-box-template-styles)
-   [Dialog Box Measurements](#dialog-box-measurements)
-   [Dialog Box Controls](#dialog-box-controls)
-   [Dialog Box Window Menu](#dialog-box-window-menu)
-   [Dialog Box Fonts](#dialog-box-fonts)
-   [Templates in Memory](#templates-in-memory)

### Dialog Box Template Styles

Every dialog box template specifies a combination of style values that define the appearance and features of the dialog box. The style values can be window styles, such as **WS\_POPUP** and **WS\_SYSMENU**, and dialog box styles, such as **DS\_MODALFRAME**. The number and type of styles for a template depends on the type and purpose of the dialog box. For a list of values, see [**Dialog Box Styles**](dialog-box-styles.md).

The system passes all window styles specified in the template to the [**CreateWindowEx**](/windows/desktop/api/winuser/nf-winuser-createwindowexa) function when creating the dialog box. The system may pass one or more extended styles depending on the specified dialog box styles. For example, when the template specifies **DS\_MODALFRAME**, the system uses **WS\_EX\_DLGMODALFRAME** when creating the dialog box.

Most dialog boxes are pop-up windows that have a window menu and a title bar. Therefore, the typical template specifies the **WS\_POPUP**, **WS\_SYSMENU**, and **WS\_CAPTION** styles. The template also specifies a border style: **WS\_BORDER** for modeless dialog boxes, and **DS\_MODALFRAME** for modal dialog boxes. A template may specify a window type other than pop-up (such as **WS\_OVERLAPPED**) if it creates a customized window instead of a dialog box.

The system always displays a modal dialog box regardless of whether the **WS\_VISIBLE** style is specified. When the template for a modeless dialog box specifies the **WS\_VISIBLE** style, the system automatically displays the dialog box when it is created. Otherwise, the application is responsible for displaying the dialog box by using the [**ShowWindow**](/windows/desktop/api/winuser/nf-winuser-showwindow) function.

### Dialog Box Measurements

Every dialog box template contains measurements that specify the position, width, and height of the dialog box and the controls it contains. These measurements are device independent, so an application can use a single template to create the same dialog box for all types of display devices. This ensures that a dialog box will have the same proportions and appearance on all screens despite differing resolutions and aspect ratios between screens.

The measurements in a dialog box template are specified in dialog template units. To convert measurements from dialog template units to screen units (pixels), use the [**MapDialogRect**](/windows/desktop/api/Winuser/nf-winuser-mapdialogrect) function, which takes into account the font used by the dialog box and correctly converts a rectangle from dialog template units into pixels. For dialog boxes that use the system font, you can use the [**GetDialogBaseUnits**](/windows/desktop/api/Winuser/nf-winuser-getdialogbaseunits) function to perform the conversion calculations yourself, although using **MapDialogRect** is simpler.

The template must specify the initial coordinates of the upper left corner of the dialog box. Usually the coordinates are relative to the upper left corner of the owner window's client area. When the template specifies the DS\_ABSALIGN style or the dialog box has no owner, the position is relative to the upper left corner of the screen. The system sets this initial position when creating the dialog box, but permits an application to adjust the position before displaying the dialog box. For example, an application can retrieve the dimensions of the owner window, calculate a new position that centers the dialog box in the owner window, and then set the position by using the [**SetWindowPos**](/windows/desktop/api/winuser/nf-winuser-setwindowpos) function.

The template should specify a dialog box width and height that does not exceed the width and height of the screen and ensures that all controls are within the client area of the dialog box. Although the system permits a dialog box to be any size, creating one that is too small or too large can prevent the user from providing input, defeating the purpose of the dialog box. Many applications use more than one dialog box when there are a large number of controls. In such cases, the initial dialog box usually contains one or more buttons that the user can choose to display the next dialog box.

### Dialog Box Controls

The template specifies the position, width, height, style, identifier, and window class for each control in the dialog box. The system creates each control by passing this data to the [**CreateWindowEx**](/windows/desktop/api/winuser/nf-winuser-createwindowexa) function. Controls are created in the order they are specified in the template. The template should specify the appropriate number, type, and order of controls to ensure that the user can enter the input needed to complete the task associated with the dialog box.

For each control, the template specifies style values that define the appearance and operation of the control. Every control is a child window and therefore must have the **WS\_CHILD** style. To ensure that the control is visible when the dialog box is displayed, each control must also have the **WS\_VISIBLE** style. Other commonly used window styles are **WS\_BORDER** for controls that have optional borders, **WS\_DISABLED** for controls that should be disabled when the dialog box is initially created, and **WS\_TABSTOP** and **WS\_GROUP** for controls that can be accessed using the keyboard. The **WS\_TABSTOP** and **WS\_GROUP** styles are used in conjunction with the dialog keyboard interface described later in this topic.

The template may also specify control styles specific to the control's window class. For example, a template that specifies a button control must give a button control style such as **BS\_PUSHBUTTON** or **BS\_CHECKBOX**. The system passes the control styles to the control window procedure through the [**WM\_CREATE**](/windows/desktop/winmsg/wm-create) message, allowing the procedure to adapt the appearance and operation of the control.

The system converts the position coordinates and the width and height measurements from dialog base units to pixels, before passing these to [**CreateWindowEx**](/windows/desktop/api/winuser/nf-winuser-createwindowexa). When the system creates a control, it specifies the dialog box as the parent window. This means the system always interprets the position coordinates of the control as client coordinates, relative to the upper left corner of the dialog box's client area.

The template specifies the window class for each control. A typical dialog box contains controls belonging to the predefined control window classes, such as the button and edit control window classes. In this case, the template specifies window classes by supplying the corresponding predefined atom values for the classes. When a dialog box contains a control belonging to a custom control window class, the template gives the name of that registered window class or the atom value currently associated with the name.

Each control in a dialog box must have a unique identifier to distinguish it from other controls. Controls send information to the dialog box procedure through [**WM\_COMMAND**](/windows/desktop/menurc/wm-command) messages, so the control identifiers are essential for the procedure to determine which control sent a specified message. The only exception to this rule are control identifiers for static controls. Static controls do not require unique identifiers because they send no **WM\_COMMAND** messages.

To permit the user to close the dialog box, the template should specify at least one push button and give it the control identifier **IDCANCEL**. To permit the user to choose between completing or canceling the task associated with the dialog box, the template should specify two push buttons, labeled **OK** and **Cancel**, with control identifiers of **IDOK** and **IDCANCEL**, respectively.

A template also specifies optional text and creation data for a control. The text typically provides labels for button controls or specifies the initial content of a static text control. The creation data is one or more bytes of data that the system passes to the control window procedure when creating the control. Creation data is useful for controls that require more information about their initial content or style than is specified by other data. For example, an application can use creation data to set the initial setting and range for a scroll bar control.

### Dialog Box Window Menu

The system gives a dialog box a window menu when the template specifies the **WS\_SYSMENU** style. To prevent inappropriate input, the system automatically disables all items in the menu except **Move** and **Close**. The user can click **Move** to move the dialog box. When the user clicks **Close**, the system sends a [**WM\_COMMAND**](/windows/desktop/menurc/wm-command) message to the dialog box procedure with the *wParam* parameter set to **IDCANCEL**. This is identical to the message sent by the **Cancel** button when the user clicks it. The recommended action for this message is to close the dialog box and cancel the requested task.

Although other menus in dialog boxes are not recommended, a dialog box template can specify a menu by supplying the identifier or the name of a menu resource. In this case, the system loads the resource and creates the menu for the dialog box. Applications typically use menu identifiers or names in templates when using the templates to create custom windows rather than dialog boxes.

### Dialog Box Fonts

The system uses the average character width of the dialog box font to calculate the position and dimensions of the dialog box. By default, the system draws all text in a dialog box using the **SYSTEM\_FONT** font.

To specify a font for a dialog box other than the default, you must create the dialog box using a dialog box template. In a template resource, use the [FONT Statement](../menurc/font-statement.md). In a dialog box template, set the **DS\_SETFONT** or **DS\_SHELLFONT** style and specify a point size and a typeface name. Even if a dialog box template specifies a font in this manner, the system always uses the system font for the dialog box title and dialog box menus.

When the dialog box has the **DS\_SETFONT** or **DS\_SHELLFONT** style, the system sends a [**WM\_SETFONT**](/windows/desktop/winmsg/wm-setfont) message to the dialog box procedure and to each control as it creates the control. The dialog box procedure is responsible for saving the font handle passed with the **WM\_SETFONT** message and selecting the handle into the display device context whenever it writes text to the window. Predefined controls do this by default.

The system font can vary between different versions of Windows. To have your application use the system font no matter which system it is running on, use **DS\_SHELLFONT** with the typeface MS Shell Dlg, and use the [DIALOGEX Resource](../menurc/dialogex-resource.md) instead of the [DIALOG Resource](../menurc/dialog-resource.md). The system maps this typeface such that your dialog box will use the Tahoma font. Note that **DS\_SHELLFONT** has no effect if the typeface is not MS Shell Dlg.

### Templates in Memory

A dialog box template in memory consists of a header that describes the dialog box, followed by one or more additional blocks of data that describe each of the controls in the dialog box. The template can use either the standard format or the extended format. In a standard template, the header is a [**DLGTEMPLATE**](/windows/desktop/api/Winuser/ns-winuser-dlgtemplate) structure followed by additional variable-length arrays. The data for each control consists of a [**DLGITEMTEMPLATE**](/windows/desktop/api/Winuser/ns-winuser-dlgitemtemplate) structure followed by additional variable-length arrays. In an extended dialog box template, the header uses the [**DLGTEMPLATEEX**](dlgtemplateex.md) format and the control definitions use the [**DLGITEMTEMPLATEEX**](dlgitemtemplateex.md) format.

To distinguish between a standard template and an extended template, check the first 16-bits of a dialog box template. In an extended template, the first **WORD** is 0xFFFF; any other value indicates a standard template.

If you create a dialog template in memory, you must ensure that the each of the [**DLGITEMTEMPLATE**](/windows/desktop/api/Winuser/ns-winuser-dlgitemtemplate) or [**DLGITEMTEMPLATEEX**](dlgitemtemplateex.md) control definitions are aligned on **DWORD** boundaries. In addition, any creation data that follows a control definition must be aligned on a **DWORD** boundary. All of the other variable-length arrays in a dialog box template must be aligned on **WORD** boundaries.

### Template Header

In both the standard and extended templates for dialog boxes, the header includes the following general information:

-   The location and dimensions of the dialog box
-   The window and dialog box styles for the dialog box
-   The number of controls in the dialog box. This value determines the number of [**DLGITEMTEMPLATE**](/windows/desktop/api/Winuser/ns-winuser-dlgitemtemplate) or [**DLGITEMTEMPLATEEX**](dlgitemtemplateex.md) control definitions in the template.
-   An optional menu resource for the dialog box. The template can indicate that the dialog box does not have a menu, or it can specify an ordinal value or null-terminated Unicode string that identifies a menu resource in an executable file.
-   The window class of the dialog box. This can be either the predefined dialog box class, or an ordinal value or null-terminated Unicode string that identifies a registered window class.
-   A null-terminated Unicode string that specifies the title for the dialog box window. If the string is empty, the title bar of the dialog box is blank. If the dialog box does not have the **WS\_CAPTION** style, the system sets the title to the specified string but does not display it.
-   If the dialog box has the **DS\_SETFONT** style, the header specifies the point size and typeface name of the font to use for the text in the client area and controls of the dialog box.

In an extended template, the [**DLGTEMPLATEEX**](dlgtemplateex.md) header also specifies the following additional information:

-   The help context identifier of the dialog box window when the system sends a [**WM\_HELP**](../shell/wm-help.md) message.
-   If the dialog box has the **DS\_SETFONT** or **DS\_SHELLFONT** style, the header specifies the font weight and indicates whether the font is italic.

### Control Definitions

Following the template header is one or more control definitions that describe the controls of the dialog box. In both the standard and extended templates, the dialog box header has a member that indicates the number of control definitions in the template. In a standard template, each control definition consists of a [**DLGITEMTEMPLATE**](/windows/desktop/api/Winuser/ns-winuser-dlgitemtemplate) structure followed by additional variable-length arrays. In an extended template, the control definitions use the [**DLGITEMTEMPLATEEX**](dlgitemtemplateex.md) format.

In both the standard and extended templates, the control definition includes the following information:

-   The location and dimensions of the control.
-   The window and control styles for the control.
-   The control identifier.
-   The window class of the control. This can be either the ordinal value of a predefined system class or a null-terminated Unicode string that specifies the name of a registered window class.
-   A null-terminated Unicode string that specifies the initial text of the control, or an ordinal value that identifies a resource, such as an icon, in an executable file.
-   An optional variable-length block of creation data. When the system creates the control, it passes a pointer to this data in the *lParam* parameter of the [**WM\_CREATE**](/windows/desktop/winmsg/wm-create) message that it sends to the control.

In an extended template, the control definition also specifies a help context identifier for the control when the system sends a [**WM\_HELP**](../shell/wm-help.md) message.

 

 