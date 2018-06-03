---
title: MMC 2.0 Interfaces and Methods
description: MMC interfaces and their methods are arranged according to where they are implemented \ 8212; MMC or snap-ins. The methods are provided in vtable order on the page describing each interface.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c95742a4-ae9b-40f3-8d88-c4955e5a3032
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- interfaces and methods MMC 2.0
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MMC 2.0 Interfaces and Methods

MMC interfaces and their methods are arranged according to where they are implemented — MMC or snap-ins. The methods are provided in vtable order on the page describing each interface.

## COM Interfaces Implemented by MMC

-   [**IColumnData**](/windows/desktop/api/Mmc/nn-mmc-icolumndata) — The IColumnData interface enables a snap-in to set and retrieve the persisted view data of list view columns to use for column customization. It provides methods for programmatically providing the same functionality that MMC provides in the Modify Columns dialog box. In addition, the IColumnData interface provides methods for setting and retrieving the sorted column and sort direction of a particular column set.
-   [**IConsole**](/windows/desktop/api/Mmc/nn-mmc-iconsole) — Enables communication with the console.
-   [**IConsole2**](/windows/desktop/api/Mmc/nn-mmc-iconsole2) — Enables communication with the console.
-   [**IConsole3**](/windows/desktop/api/Mmc/nn-mmc-iconsole3) — Enables communication with the console.
-   [**IConsoleNameSpace**](/windows/desktop/api/Mmc/nn-mmc-iconsolenamespace) — Enables snap-ins to enumerate dynamic subcontainers in the scope pane. The particular snap-in determines what qualifies as a subcontainer.
-   [**IConsoleNameSpace2**](/windows/desktop/api/Mmc/nn-mmc-iconsolenamespace2) — Enables snap-ins to enumerate dynamic subcontainers in the scope pane. The particular snap-in determines what qualifies as a subcontainer.
-   [**IConsoleVerb**](/windows/desktop/api/Mmc/nn-mmc-iconsoleverb) — The IConsoleVerb interface allows snap-ins to enable standard verbs including cut, copy, paste, delete, properties, rename, refresh, and print. When an item is selected, the snap-in can update the state of these verbs.
-   [**IContextMenuCallback**](/windows/desktop/api/Mmc/nn-mmc-icontextmenucallback) — The IContextMenuCallback interface is used to add menu items to a context menu.
-   [**IContextMenuProvider**](/windows/desktop/api/Mmc/nn-mmc-icontextmenuprovider) — The IContextMenuProvider interface implements methods that create new context menus, for the purpose of adding items to those menus, to enable extensions to extend those menus, and to display the resultant context menus.
-   [**IControlbar**](/windows/desktop/api/Mmc/nn-mmc-icontrolbar) — The IControlbar interface provides a way to create toolbars and other controls.
-   [**IDisplayHelp**](/windows/desktop/api/Mmc/nn-mmc-idisplayhelp) — The IDisplayHelp interface enables a snap-in to display a specific HTML Help topic within the merged MMC HTML Help collection file for the console.
-   [**IHeaderCtrl**](/windows/desktop/api/Mmc/nn-mmc-iheaderctrl) — Enables the manipulation of columns and indicates the kind of information that is to be presented in the result pane of the console.
-   [**IHeaderCtrl2**](/windows/desktop/api/Mmc/nn-mmc-iheaderctrl2) — Enables the manipulation of columns and indicates the kind of information that is to be presented in the result pane of the console.
-   [**IImageList**](/windows/desktop/api/Mmc/nn-mmc-iimagelist) — The IImageList interface enables the snap-in to insert images to be used as icons for items in the result or scope pane of the console.
-   [**IMenuButton**](/windows/desktop/api/Mmc/nn-mmc-imenubutton) — The IMenuButton interface enables the snap-in to add and manage menu buttons.
-   [**IMessageView**](/windows/desktop/api/Mmc/nn-mmc-imessageview) — The IMessageView interface provides support for specifying the text and icons for error messages displayed using the MMC message OCX control. MMC provides a message OCX control that snap-ins can use for that displays error messages in the result pane.
-   [**IPropertySheetCallback**](/windows/desktop/api/Mmc/nn-mmc-ipropertysheetcallback) — The IPropertySheetCallback interface is used by a snap-in to add its property pages to a property sheet.
-   [**IPropertySheetProvider**](/windows/desktop/api/Mmc/nn-mmc-ipropertysheetprovider) — The IPropertySheetProvider interface implements Win32 property sheets as COM objects. Snap-ins can use the IPropertySheetProvider interface for adding wizard pages to a snap-in. IPropertySheetProvider is also used when a snap-in adds a feature that has a property sheet as the user interface, but identifies it as something else.
-   [**IRequiredExtensions**](/windows/desktop/api/Mmc/nn-mmc-irequiredextensions) — The IRequiredExtensions interface enables a snap-in to add some or all of the extension snap-ins that extend it.
-   [**IResultData**](/windows/desktop/api/Mmc/nn-mmc-iresultdata) — The IResultData interface enables a snap-in to add, remove, find, and modify items associated with the result pane. It also enables the manipulation of the view style of the result pane.
-   [**IStringTable**](/windows/desktop/api/Mmc/nn-mmc-istringtable) — The IStringTable interface provides a means of storing string data with a snap-in. A string table is created in the console file as required for each snap-in by MMC.
-   [**IToolbar**](/windows/desktop/api/Mmc/nn-mmc-itoolbar) — The IToolbar interface is used to create new toolbars, to add items to them, to extend the toolbars, and to display the resultant new toolbars.

## COM Interfaces Implemented by the Snap-in

-   [**IComponent**](/windows/desktop/api/Mmc/nn-mmc-icomponent) — The IComponent interface enables MMC to communicate with snap-ins. Similar to the IComponentData interface, IComponent is typically implemented at the view level and is closely associated with items being displayed in the result pane.
-   [**IComponentData**](/windows/desktop/api/Mmc/nn-mmc-icomponentdata) — The IComponentData interface enables MMC to communicate with snap-ins. Similar to the IComponent interface, IComponentData is typically implemented at the document level and is closely associated with items (folders) being displayed in the scope pane.
-   [**IEnumTASK**](/windows/desktop/api/Mmc/nn-mmc-ienumtask) — The IEnumTASK interface enables a snap-in to enumerate the tasks to add to a task pad.
-   [**IExtendContextMenu**](/windows/desktop/api/Mmc/nn-mmc-iextendcontextmenu) — The IExtendContextMenu interface enables snap-ins to add items to an existing context menu.
-   [**IExtendControlbar**](/windows/desktop/api/Mmc/nn-mmc-iextendcontrolbar) — The IExtendControlbar interface enables a snap-in to add control bars to the console. This provides a way to improve the functionality and appearance of your snap-in by adding toolbars or other user interface enhancements.
-   [**IExtendPropertySheet**](/windows/desktop/api/Mmc/nn-mmc-iextendpropertysheet) — Enables a snap-in to add pages to the property sheet of an item.
-   [**IExtendPropertySheet2**](/windows/desktop/api/Mmc/nn-mmc-iextendpropertysheet2) — Enables a snap-in to add pages to the property sheet of an item.
-   [**IExtendTaskpad**](/windows/desktop/api/Mmc/nn-mmc-iextendtaskpad) — The IExtendTaskpad interface enables a snap-in to set up a taskpad and receive notifications from the taskpad.
-   [**IResultDataCompare**](/windows/desktop/api/Mmc/nn-mmc-iresultdatacompare) — The IResultDataCompare interface allows primary snap-ins to compare result items that are displayed in a sorted order in the result pane.
-   [**IResultDataCompareEx**](/windows/desktop/api/Mmc/nn-mmc-iresultdatacompareex) — The IResultDataCompareEx interface allows primary snap-ins to compare both scope and result items that are displayed in a sorted order in the result pane.
-   [**IResultOwnerData**](/windows/desktop/api/Mmc/nn-mmc-iresultownerdata) — The IResultOwnerData interface allows snap-ins to use virtual lists.
-   [**ISnapinAbout**](/windows/desktop/api/Mmc/nn-mmc-isnapinabout) — The ISnapinAbout interface enables the console to get copyright and version information from a snap-in. The console also uses this interface to obtain images for the static folder from the snap-in.
-   [**ISnapinHelp**](/windows/desktop/api/Mmc/nn-mmc-isnapinhelp) — Enables the console to get the location of a snap-in's compiled HTML Help file. The console merges the HTML Help files of all snap-ins with the MMC console HTML Help collection file.
-   [**ISnapinHelp2**](/windows/desktop/api/Mmc/nn-mmc-isnapinhelp2) — Enables the console to get the location of a snap-in's compiled HTML Help file. The console merges the HTML Help files of all snap-ins with the MMC console HTML Help collection file.

 

 




