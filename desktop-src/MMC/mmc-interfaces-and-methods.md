---
title: MMC 2.0 Interfaces and Methods
description: MMC interfaces and their methods are arranged according to where they are implemented \ 8212; MMC or snap-ins. The methods are provided in vtable order on the page describing each interface.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'c95742a4-ae9b-40f3-8d88-c4955e5a3032'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["interfaces and methods MMC 2.0"]
---

# MMC 2.0 Interfaces and Methods

MMC interfaces and their methods are arranged according to where they are implemented — MMC or snap-ins. The methods are provided in vtable order on the page describing each interface.

## COM Interfaces Implemented by MMC

-   [**IColumnData**](icolumndata.md) — The IColumnData interface enables a snap-in to set and retrieve the persisted view data of list view columns to use for column customization. It provides methods for programmatically providing the same functionality that MMC provides in the Modify Columns dialog box. In addition, the IColumnData interface provides methods for setting and retrieving the sorted column and sort direction of a particular column set.
-   [**IConsole**](iconsole.md) — Enables communication with the console.
-   [**IConsole2**](iconsole2.md) — Enables communication with the console.
-   [**IConsole3**](iconsole3.md) — Enables communication with the console.
-   [**IConsoleNameSpace**](iconsolenamespace.md) — Enables snap-ins to enumerate dynamic subcontainers in the scope pane. The particular snap-in determines what qualifies as a subcontainer.
-   [**IConsoleNameSpace2**](iconsolenamespace2.md) — Enables snap-ins to enumerate dynamic subcontainers in the scope pane. The particular snap-in determines what qualifies as a subcontainer.
-   [**IConsoleVerb**](iconsoleverb.md) — The IConsoleVerb interface allows snap-ins to enable standard verbs including cut, copy, paste, delete, properties, rename, refresh, and print. When an item is selected, the snap-in can update the state of these verbs.
-   [**IContextMenuCallback**](icontextmenucallback.md) — The IContextMenuCallback interface is used to add menu items to a context menu.
-   [**IContextMenuProvider**](icontextmenuprovider.md) — The IContextMenuProvider interface implements methods that create new context menus, for the purpose of adding items to those menus, to enable extensions to extend those menus, and to display the resultant context menus.
-   [**IControlbar**](icontrolbar.md) — The IControlbar interface provides a way to create toolbars and other controls.
-   [**IDisplayHelp**](idisplayhelp.md) — The IDisplayHelp interface enables a snap-in to display a specific HTML Help topic within the merged MMC HTML Help collection file for the console.
-   [**IHeaderCtrl**](iheaderctrl.md) — Enables the manipulation of columns and indicates the kind of information that is to be presented in the result pane of the console.
-   [**IHeaderCtrl2**](iheaderctrl2.md) — Enables the manipulation of columns and indicates the kind of information that is to be presented in the result pane of the console.
-   [**IImageList**](iimagelist.md) — The IImageList interface enables the snap-in to insert images to be used as icons for items in the result or scope pane of the console.
-   [**IMenuButton**](imenubutton.md) — The IMenuButton interface enables the snap-in to add and manage menu buttons.
-   [**IMessageView**](imessageview.md) — The IMessageView interface provides support for specifying the text and icons for error messages displayed using the MMC message OCX control. MMC provides a message OCX control that snap-ins can use for that displays error messages in the result pane.
-   [**IPropertySheetCallback**](ipropertysheetcallback.md) — The IPropertySheetCallback interface is used by a snap-in to add its property pages to a property sheet.
-   [**IPropertySheetProvider**](ipropertysheetprovider.md) — The IPropertySheetProvider interface implements Win32 property sheets as COM objects. Snap-ins can use the IPropertySheetProvider interface for adding wizard pages to a snap-in. IPropertySheetProvider is also used when a snap-in adds a feature that has a property sheet as the user interface, but identifies it as something else.
-   [**IRequiredExtensions**](irequiredextensions.md) — The IRequiredExtensions interface enables a snap-in to add some or all of the extension snap-ins that extend it.
-   [**IResultData**](iresultdata.md) — The IResultData interface enables a snap-in to add, remove, find, and modify items associated with the result pane. It also enables the manipulation of the view style of the result pane.
-   [**IStringTable**](istringtable.md) — The IStringTable interface provides a means of storing string data with a snap-in. A string table is created in the console file as required for each snap-in by MMC.
-   [**IToolbar**](itoolbar.md) — The IToolbar interface is used to create new toolbars, to add items to them, to extend the toolbars, and to display the resultant new toolbars.

## COM Interfaces Implemented by the Snap-in

-   [**IComponent**](icomponent.md) — The IComponent interface enables MMC to communicate with snap-ins. Similar to the IComponentData interface, IComponent is typically implemented at the view level and is closely associated with items being displayed in the result pane.
-   [**IComponentData**](icomponentdata.md) — The IComponentData interface enables MMC to communicate with snap-ins. Similar to the IComponent interface, IComponentData is typically implemented at the document level and is closely associated with items (folders) being displayed in the scope pane.
-   [**IEnumTASK**](ienumtask.md) — The IEnumTASK interface enables a snap-in to enumerate the tasks to add to a task pad.
-   [**IExtendContextMenu**](iextendcontextmenu.md) — The IExtendContextMenu interface enables snap-ins to add items to an existing context menu.
-   [**IExtendControlbar**](iextendcontrolbar.md) — The IExtendControlbar interface enables a snap-in to add control bars to the console. This provides a way to improve the functionality and appearance of your snap-in by adding toolbars or other user interface enhancements.
-   [**IExtendPropertySheet**](iextendpropertysheet.md) — Enables a snap-in to add pages to the property sheet of an item.
-   [**IExtendPropertySheet2**](iextendpropertysheet2.md) — Enables a snap-in to add pages to the property sheet of an item.
-   [**IExtendTaskpad**](iextendtaskpad.md) — The IExtendTaskpad interface enables a snap-in to set up a taskpad and receive notifications from the taskpad.
-   [**IResultDataCompare**](iresultdatacompare.md) — The IResultDataCompare interface allows primary snap-ins to compare result items that are displayed in a sorted order in the result pane.
-   [**IResultDataCompareEx**](iresultdatacompareex.md) — The IResultDataCompareEx interface allows primary snap-ins to compare both scope and result items that are displayed in a sorted order in the result pane.
-   [**IResultOwnerData**](iresultownerdata.md) — The IResultOwnerData interface allows snap-ins to use virtual lists.
-   [**ISnapinAbout**](isnapinabout.md) — The ISnapinAbout interface enables the console to get copyright and version information from a snap-in. The console also uses this interface to obtain images for the static folder from the snap-in.
-   [**ISnapinHelp**](isnapinhelp.md) — Enables the console to get the location of a snap-in's compiled HTML Help file. The console merges the HTML Help files of all snap-ins with the MMC console HTML Help collection file.
-   [**ISnapinHelp2**](isnapinhelp2.md) — Enables the console to get the location of a snap-in's compiled HTML Help file. The console merges the HTML Help files of all snap-ins with the MMC console HTML Help collection file.

 

 




