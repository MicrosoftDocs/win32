---
title: Implementing a Folder View
description: Windows Shell provides a default implementation of the folder view, colloquially known as DefView, so that you can avoid much of the work of implementing your own namespace extension.
ms.assetid: 8c6712d8-c3cb-4450-8277-3a8675622651
keywords:
- folder view object
- IShellView
- IShellBrowser,folder view objects
ms.topic: article
ms.date: 05/31/2018
---

# Implementing a Folder View

Windows Shell provides a default implementation of the folder view, colloquially known as DefView, so that you can avoid much of the work of implementing your own namespace extension. Because some view features cannot be achieved through custom views, it is often recommended that the default system folder view object is used in place of a custom view. For more information, see [**SHCreateShellFolderView**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shcreateshellfolderview). The remainder of this topic discusses implementing a custom folder view that cannot support newer view features.

Unlike the tree view, Windows Explorer does not manage the contents of a folder view. Instead, the folder view window hosts a child window that is provided by the folder object. The folder object is responsible for creating a folder view object to display the folder's contents in the child window.

The key to implementing a folder view object is the [**IShellView**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellview) interface. This interface is used by Windows Explorer to communicate with the folder view object. Before displaying a folder view, Windows Explorer calls the folder object's [**IShellFolder::CreateViewObject**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-createviewobject) method with *riid* set to IID\_IShellView. Create a folder view object and return its **IShellView** interface. The folder view object must then create a child window of the folder view window and use the child window to display information about the folder's contents.

In addition to controlling how data is displayed, extensions can also customize a number of the features of Windows Explorer. For instance, an extension can add items to the toolbar or menu bar, or display information on the status bar.

-   [The Folder View Object](#the-folder-view-object)
-   [Initializing the Folder View Object](#initializing-the-folder-view-object)
-   [Displaying the Folder View](#displaying-the-folder-view)
-   [Implementing IShellView](#implementing-ishellview)
    -   [AddPropertySheetPages](#addpropertysheetpages)
    -   [GetCurrentInfo](#getcurrentinfo)
    -   [Refresh](#refresh)
    -   [SaveViewState](#saveviewstate)
    -   [TranslateAcelerator](#translateacelerator)
-   [Using IShellBrowser to Communicate with Windows Explorer](#using-ishellbrowser-to-communicate-with-windows-explorer)
    -   [Modifying the Windows Explorer Menu Bar](#modifying-the-windows-explorer-menu-bar)
    -   [Modifying the Windows Explorer Toolbar](#modifying-the-windows-explorer-toolbar)
    -   [Modifying the Windows Explorer Status Bar](#modifying-the-windows-explorer-status-bar)
    -   [Storing View-specific Information](#storing-view-specific-information)

## The Folder View Object

A folder view object is a Component Object Model (COM) object that exposes an [**IShellView**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellview) interface. This object is responsible for:

-   Creating a child window of the folder view window and using it to display the contents of the folder.
-   Handling communication with Windows Explorer.
-   Adding folder-specific commands to the Windows Explorer menu bar and toolbar and handling those commands when they are selected.
-   Managing user interaction with the folder view window, such as displaying shortcut menus or handling drag-and-drop operations.

This document discusses the first three topics. Because user interaction with the folder view takes place within your child window, your folder view object is responsible for handling it as it would for any other window.

Windows Explorer requests a folder view object by calling your folder object's [**IShellFolder::CreateViewObject**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-createviewobject) with *riid* set to IID\_IShellView. The procedure for creating a folder view is:

1.  Your folder object creates a new instance of your folder view object and returns a pointer to its [**IShellView**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellview) interface.
2.  Windows Explorer initializes the folder view object by calling the [**IShellView::CreateViewWindow**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellview-createviewwindow) method. Create a child window of the folder view window and return its handle to Windows Explorer.
3.  The folder view object uses the Windows Explorer[**IShellBrowser**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellbrowser) interface to customize the Windows Explorer toolbar, menu bar, and status bar.
4.  The folder view object displays the contents of the folder in the child window.
5.  The folder view object handles user interaction with the folder view and any folder-specific toolbar or menu bar items.

## Initializing the Folder View Object

Windows Explorer initializes the folder view object by calling the [**IShellView::CreateViewWindow**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellview-createviewwindow) method. The method's parameters provide the folder view object with the information it needs to create the child window that will be used to display the folder's contents:

-   A pointer to the previous folder view object's [**IShellView**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellview) interface. This parameter can be set to **NULL**.
-   A [**FOLDERSETTINGS**](/windows/desktop/api/shobjidl_core/ns-shobjidl_core-foldersettings) structure that contains the previous folder view's settings.
-   A pointer to the Windows Explorer[**IShellBrowser**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellbrowser) interface.
-   A [RECT](/previous-versions//ms536136(v=vs.85)) structure with the dimensions of the folder view window.

The [**IShellView::CreateViewWindow**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellview-createviewwindow) method is called before the previous folder view object is destroyed. The [**IShellView**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellview) interface pointer thus allows you to communicate with the previous folder view object. This interface is primarily useful if the previous folder belonged to your extension and used the same display scheme. If so, you can communicate with the previous folder view object for such purposes as exchanging private settings.

A simple way to determine whether the [**IShellView**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellview) pointer belongs to your extension is to have all your folder view objects expose a private interface. Call [IShellView::QueryInterface](/windows/win32/api/unknwn/nf-unknwn-iunknown-queryinterface(q)) to request the private interface, and examine the return value to determine whether the folder view object is one of yours. You can then use a private method on that interface to exchange information.

The [**FOLDERSETTINGS**](/windows/desktop/api/shobjidl_core/ns-shobjidl_core-foldersettings) structure contains the previous folder view's display settings. The primary setting is the viewing mode: large icon, small icon, list, or details. There is also a flag that contains the settings of a variety of display options, such as whether the view should be left-aligned. Your folder display should follow these settings to the extent possible, to give users a consistent experience as they go from one folder to another. You should store this structure and update it as the settings change. Windows Explorer calls [**IShellView::GetCurrentInfo**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellview-getcurrentinfo) to obtain the most recent value of this structure before it opens the next folder view.

The [**IShellBrowser**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellbrowser) interface is exposed by Windows Explorer. This interface is a companion to [**IShellView**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellview) and allows a folder view object to communicate with Windows Explorer. There is no other way to retrieve this interface pointer, so your folder view object should store it for later use. In particular, you will need to call [IShellBrowser::GetWindow](/windows/win32/api/oleidl/nf-oleidl-iolewindow-getwindow) to retrieve the parent folder view window that you will use to create your child window. Note that the IShellBrowser::GetWindow method is not included in the **IShellBrowser** documentation because it is inherited from [IOleWindow](/windows/win32/api/oleidl/nn-oleidl-iolewindow). After storing the interface pointer, remember to call [IShellBrowser::AddRef](/windows/win32/api/unknwn/nf-unknwn-iunknown-addref) to increment the interface's reference count. When you no longer need the interface, call [IShellBrowser::Release](/windows/win32/api/unknwn/nf-unknwn-iunknown-release).

To create your child window:

1.  Examine the [**FOLDERSETTINGS**](/windows/desktop/api/shobjidl_core/ns-shobjidl_core-foldersettings) and [RECT](/previous-versions//ms536136(v=vs.85)) structures.
2.  If needed, obtain private settings from the previous folder view object.
3.  Call [IShellBrowser::GetWindow](/windows/win32/api/oleidl/nf-oleidl-iolewindow-getwindow) to retrieve the parent folder view window.
4.  Create a child of the folder view window obtained in the previous step and return it to Windows Explorer.

## Displaying the Folder View

Once you have created the child window and returned it to Windows Explorer, you can display the folder's contents. Typically, extensions display their information by having the child window host either a [list view control](../controls/list-view-control-reference.md) or a **WebBrowser control**. The list view control allows you to replicate the Windows Explorer [classic view](web-view.md). The WebBrowser control allows you to use a Dynamic HTML (DHTML) document to display your information, much like the Windows Explorer Web view. For further information, refer to the documentation of those controls.

The folder view window always exists, even if it does not have focus. You should therefore maintain three states for your child window:

-   Activated with focus. The folder view has been created and has focus. Set the menu bar or toolbar items that are appropriate for a focused state.
-   Activated without focus. The folder view has been created and is active, but it does not have focus. Set the menu bar or toolbar items that are appropriate for a nonfocused state. Omit any items that apply to the selection of items within the folder view.
-   Deactivated. The folder view is about to be destroyed. Remove all folder-specific menu items.

Windows Explorer notifies your folder view object when the window state changes by calling [**IShellView::UIActivate**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellview-uiactivate). In turn, the folder view object should notify Windows Explorer when a user activates the folder view window by calling [**IShellBrowser::OnViewWindowActive**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellbrowser-onviewwindowactive). For further discussion of this interface, see [Using IShellBrowser to Communicate with Windows Explorer](#using-ishellbrowser-to-communicate-with-windows-explorer).

While the folder view is active, you need to process any Windows messages, such as [WM\_SIZE](../winmsg/wm-size.md), that belong to your child window. Your window procedure will also receive [WM\_COMMAND](../menurc/wm-command.md) messages for any items you have added to the Windows Explorer menu bar or toolbar.

After creating the folder view, Windows Explorer calls the folder view object's [**IShellView**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellview) interface to pass it a variety of information. Your object must modify its display accordingly. When the folder view is about to be destroyed, Windows Explorer notifies the folder view object by calling its [**IShellView::DestroyViewWindow**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellview-destroyviewwindow) method.

## Implementing IShellView

After the folder object has been created, Windows Explorer calls various [**IShellView**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellview) methods to either request information or notify the object of a change in the state of Windows Explorer. This section outlines how to implement those **IShellView** methods. The remaining methods are used for more specialized purposes, such as the File Open common dialog box. For details, see the **IShellView** documentation.

### AddPropertySheetPages

When a user selects **Folder Options** from the Windows Explorer**Tools** menu, a property sheet is displayed that allows the user to modify the folder options. Windows Explorer calls your folder view object's [**IShellView::AddPropertySheetPages**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellview-addpropertysheetpages) method to allow you to add a page to this property sheet.

Windows Explorer passes a pointer to an [AddPropSheetPageProc](/windows/win32/api/prsht/nc-prsht-lpfnaddpropsheetpage) callback function in the *lpfn* parameter of [**IShellView::AddPropertySheetPages**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellview-addpropertysheetpages). Call [CreatePropertySheetPage](/windows/win32/api/prsht/nf-prsht-createpropertysheetpagea) to create the page, and then call the AddPropSheetPageProc to add it to the property sheet. For further discussion of how to handle property sheets, see [Property Sheets](../controls/property-sheets.md).

### GetCurrentInfo

When the user switches from one folder to another, Windows Explorer attempts to maintain a similar folder view. For instance, if the previous folder view showed large icons, the next should as well. When Windows Explorer calls [**IShellView::CreateViewWindow**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellview-createviewwindow) to initialize your folder view object, the method receives a [**FOLDERSETTINGS**](/windows/desktop/api/shobjidl_core/ns-shobjidl_core-foldersettings) structure. This structure contains information that allows you to make your folder view display consistent with the previous folder view.

To help ensure that the next view is consistent with the current view, store the [**FOLDERSETTINGS**](/windows/desktop/api/shobjidl_core/ns-shobjidl_core-foldersettings) structure. If the view changes, for instance from large to small icons, update the structure accordingly. Prior to switching views, Windows Explorer will call [**IShellView::GetCurrentInfo**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellview-getcurrentinfo) to request the current **FOLDERSETTINGS** values to pass them to the next folder view object.

### Refresh

The user can ensure that the folder view reflects the current state of the folder by selecting **Refresh** from the **View** menu or pressing the F5 key. When the user does so, Windows Explorer calls the [**IShellView::Refresh**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellview-refresh) method. Your folder view object should immediately update the folder view display.

### SaveViewState

Windows Explorer calls the [**IShellView::SaveViewState**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellview-saveviewstate) method to prompt your folder view object to save its view state. You can then recover the state the next time the folder is viewed. The preferred way to save a view state is by calling the [**IShellBrowser::GetViewStateStream**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellbrowser-getviewstatestream) method. This method returns an [IStream](/windows/win32/api/objidl/nn-objidl-istream) interface that your folder view object can use to save its state. When you create another folder view, you can call the same **IShellBrowser::GetViewStateStream** method to obtain an IStream pointer that allows you to read the settings saved by previous folder views.

### TranslateAcelerator

When the user presses a shortcut key, Windows Explorer passes the message to the folder view object by calling [**IShellView::TranslateAccelerator**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellview-translateaccelerator). Return S\_FALSE to have Windows Explorer process the message. If your folder view object has processed the message, return S\_OK.

When the folder view window has focus, Windows Explorer calls [**IShellView::TranslateAccelerator**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellview-translateaccelerator) before it processes the message. Because most of the messages are typically associated with Windows Explorer menu bar or toolbar commands, your folder view object should normally return S\_FALSE. Windows Explorer can then process the message normally. Return S\_OK only if the message is folder-specific and you do not want Windows Explorer to do any further processing. If the folder view does not have focus, Windows Explorer processes the message first. It calls [**IShellBrowser::TranslateAcceleratorSB**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellbrowser-translateacceleratorsb) only if it does not handle the message.

## Using IShellBrowser to Communicate with Windows Explorer

The [**IShellBrowser**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellbrowser) interface is used by the folder view object to communicate with Windows Explorer for a variety of purposes, including:

-   [Modifying the Windows Explorer Menu Bar](#modifying-the-windows-explorer-menu-bar)
-   [Modifying the Windows Explorer Toolbar](#modifying-the-windows-explorer-toolbar)
-   [Modifying the Windows Explorer Status Bar](#modifying-the-windows-explorer-status-bar)
-   [Storing View-specific Information](#storing-view-specific-information)

### Modifying the Windows Explorer Menu Bar

The Windows Explorer menu bar allows the user to launch a variety of commands. By default, the menu bar only supports commands that are specific to Windows Explorer. The related [WM\_COMMAND](../menurc/wm-command.md) messages are processed by Windows Explorer and are not passed to your folder view object. However, you can modify the menu bar to include one or more folder-specific menu items with [**IShellBrowser**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellbrowser). Windows Explorer passes the associated WM\_COMMAND messages of those items to your folder object's window procedure for processing. You can also remove or disable any standard commands that do not apply to your application.

Folder view objects typically modify the menu bar before the folder view is first displayed. They must return the menu bar to its original state when the folder view is destroyed. You might also need to modify the menu bar each time your folder view gains or loses focus.

Because Windows Explorer calls [**IShellView::UIActivate**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellview-uiactivate) each time the folder view window's state changes, menu bar modification is normally included in that method's implementation. The basic procedure for modifying the Windows Explorer menu bar is:

1.  Call [CreateMenu](/windows/win32/api/winuser/nf-winuser-createmenu) to create a menu handle.
2.  Pass that menu handle to Windows Explorer by calling [**IShellBrowser::InsertMenusSB**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellbrowser-insertmenussb). Windows Explorer will fill in its menu information.
3.  Modify the menu as needed.
4.  Call [**IShellBrowser::SetMenuSB**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellbrowser-setmenusb) to have Windows Explorer display the modified menu bar.

Windows Explorer has six pop-up menus on its menu bar. As with all OLE containers, the Windows Explorer menu is divided into six groups: File, Edit, Container, Object, Window, and Help. The following table lists the Windows Explorer pop-up menus and their associated group, along with the menu IDs.



| Pop-up menu | ID                     | Group     |
|-------------|------------------------|-----------|
| File        | FCIDM\_MENU\_FILE      | File      |
| Edit        | FCIDM\_MENU\_EDIT      | File      |
| View        | FCIDM\_MENU\_VIEW      | Container |
| Favorites   | FCIDM\_MENU\_FAVORITES | Container |
| Tools       | FCIDM\_MENU\_TOOLS     | Container |
| Help        | FCIDM\_MENU\_HELP      | Window    |



 

When you pass the menu handle to Windows Explorer by calling [**IShellBrowser::InsertMenusSB**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellbrowser-insertmenussb), you must also pass a pointer to an [OLEMENUGROUPWIDTHS](/windows/win32/api/oleidl/ns-oleidl-olemenugroupwidths) structure whose members have been initialized to zero.

When [**IShellBrowser::InsertMenusSB**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellbrowser-insertmenussb) returns, Windows Explorer will have added its menu items. You can then use the returned menu handle with standard Windows menu functions such as [InsertMenuItem](/windows/win32/api/winuser/nf-winuser-insertmenuitema) to:

-   Add items to the Windows Explorer pop-up menus.
-   Modify or delete existing items in the Windows Explorer pop-up menus.
-   Add new pop-up menus.

Use the IDs listed in the table to identify the various Windows Explorer pop-up menus.

> [!Note]  
> To avoid conflicts with Windows Explorer command IDs, the IDs of any menu items that you add must fall between FCIDM\_SHVIEWFIRST and FCIDM\_SHVIEWLAST. These two values are defined in Shlobj.h.

 

Once you have finished modifying the menu, call [**IShellBrowser::SetMenuSB**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellbrowser-setmenusb) to have Windows Explorer display the new menu bar.

After the folder view is initially displayed, Windows Explorer calls [**IShellView::UIActivate**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellview-uiactivate) each time the folder view gains or loses focus. If you have any menu items that are sensitive to the state of the folder view, you should modify the menu accordingly, each time the state changes. For instance, you might have a menu item that acts on an item in the folder view that has been selected by the user. You should disable or remove this menu item when the folder view loses focus.

When Windows Explorer calls [**IShellView::UIActivate**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellview-uiactivate) to indicate that the folder view is being deactivated, restore the menu bar to its original state by calling [**IShellBrowser::RemoveMenusSB**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellbrowser-removemenussb).

### Modifying the Windows Explorer Toolbar

In addition to modifying the Windows Explorer menu bar, you can also add buttons to the toolbar. As with the menu bar, toolbar modification is usually part of the [**IShellView::UIActivate**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellview-uiactivate) implementation. The procedure for adding buttons to the Windows Explorer toolbar is:

1.  Add the button's bitmap to the toolbar's image list.
2.  Define the button's text string.
3.  Add the button to the toolbar.

To add a bitmap to a toolbar's image list, send the toolbar a [TB\_ADDBITMAP](../controls/tb-addbitmap.md) message by calling [**IShellBrowser::SendControlMsg**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellbrowser-sendcontrolmsg). To specify the toolbar control, set the method's *id* parameter to **FCW\_TOOLBAR**. Set *wParam* to the number of button images in the bitmap, and *lParam* to the address of a [TBADDBITMAP](/windows/win32/api/commctrl/ns-commctrl-tbaddbitmap) structure. The image index is returned in the *pret* parameter.

There are two ways to define a string for the button:

-   Assign the string to the **iString** member of the button's [TBBUTTON](/windows/win32/api/commctrl/ns-commctrl-tbbutton) structure.
-   Call [**IShellBrowser::SendControlMsg**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellbrowser-sendcontrolmsg) to send the toolbar control a [TB\_ADDSTRING](../controls/tb-addstring.md) message. The *wParam* parameter should be set to zero and the *lParam* parameter to the string. The string index is returned in the *pret* parameter.

To add the button to the toolbar, fill in a [TBBUTTON](/windows/win32/api/commctrl/ns-commctrl-tbbutton) structure and pass it to [**IShellBrowser::SetToolbarItems**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellbrowser-settoolbaritems). As with the menu, your command ID must fall between FCIDM\_SHVIEWFIRST and FCIDM\_SHVIEWLAST. The toolbar will then append the button to the right of the existing buttons.

For instance, the following code fragment adds one standard button to the Windows Explorer toolbar with a command ID of IDB\_MYBUTTON.


```
TBADDBITMAP tbadbm;
int iButtonIndex;
TBBUTTON tbb;

tbadbm.hInst = g_hInstance;    // The module's instance handle
tbadbm.nID = IDB_BUTTONIMAGE;  // The bitmap's resource ID

psb->SendControlMsg(FCW_TOOLBAR, TB_ADDBITMAP, 1,
                    reinterpret_cast<LPARAM>(&tbadbm), &iButtonIndex);

psb->SendControlMsg(FCW_TOOLBAR, TB_ADDSTRING, NULL,
                    reinterpret_cast<LPARAM>(szLabel), &iStringIndex);

ZeroMemory(&tbb, sizeof(TBBUTTON));
tbb.iBitmap = iButtonIndex;
tbb.iCommand = IDB_MYBUTTON;
tbb.iString = iStringIndex;
tbb.fsState = TBSTATE_ENABLED;
tbb.fsStyle = TBSTYLE_BUTTON;

psb->SetToolbarItems(&tbb, 1, FCT_MERGE);
```



For further discussion of how to handle toolbar controls, see [Toolbar Controls](../controls/toolbar-control-reference.md).

### Modifying the Windows Explorer Status Bar

You can use the Windows Explorer status bar to display a variety of useful information. There are two ways to use the status bar:

-   Use [**IShellBrowser::SetStatusTextSB**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellbrowser-setstatustextsb) to display a text string on the status bar.
-   Send messages directly to the status bar control with [**IShellBrowser::SendControlMsg**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellbrowser-sendcontrolmsg).

The first method is straightforward but sufficient for many purposes. For greater flexibility, you can send messages directly to the status bar control by calling [**IShellBrowser::SendControlMsg**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellbrowser-sendcontrolmsg) with the *id* parameter set to **FCW\_STATUS**. For further discussion of status bar controls, see [Status Bars](../controls/status-bars.md).

### Storing View-specific Information

When a view is about to be destroyed, it is often useful to store information such as the view's state or settings. Windows Explorer prompts you to do this task by calling [**IShellView::SaveViewState**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellview-saveviewstate). The preferred way to save view-specific information is to call [**IShellBrowser::GetViewStateStream**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellbrowser-getviewstatestream). This method provides you with an [IStream](/windows/win32/api/objidl/nn-objidl-istream) interface that you can use to store the information. You are free to use any suitable data format.

 

 
