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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MMC 2.0 Interfaces and Methods

MMC interfaces and their methods are arranged according to where they are implemented — MMC or snap-ins. The methods are provided in vtable order on the page describing each interface.

## COM Interfaces Implemented by MMC

-   [**IColumnData**](/windows/win32/Mmc/nn-mmc-icolumndata?branch=master) — The IColumnData interface enables a snap-in to set and retrieve the persisted view data of list view columns to use for column customization. It provides methods for programmatically providing the same functionality that MMC provides in the Modify Columns dialog box. In addition, the IColumnData interface provides methods for setting and retrieving the sorted column and sort direction of a particular column set.
-   [**IConsole**](/windows/win32/Mmc/nn-wdtfsystemaction-iconsole?branch=master) — Enables communication with the console.
-   [**IConsole2**](/windows/win32/Mmc/nn-mmc-iconsole2?branch=master) — Enables communication with the console.
-   [**IConsole3**](/windows/win32/Mmc/nn-mmc-iconsole3?branch=master) — Enables communication with the console.
-   [**IConsoleNameSpace**](/windows/win32/Mmc/nn-mmc-iconsolenamespace?branch=master) — Enables snap-ins to enumerate dynamic subcontainers in the scope pane. The particular snap-in determines what qualifies as a subcontainer.
-   [**IConsoleNameSpace2**](/windows/win32/Mmc/nn-mmc-iconsolenamespace2?branch=master) — Enables snap-ins to enumerate dynamic subcontainers in the scope pane. The particular snap-in determines what qualifies as a subcontainer.
-   [**IConsoleVerb**](/windows/win32/Mmc/nn-mmc-iconsoleverb?branch=master) — The IConsoleVerb interface allows snap-ins to enable standard verbs including cut, copy, paste, delete, properties, rename, refresh, and print. When an item is selected, the snap-in can update the state of these verbs.
-   [**IContextMenuCallback**](/windows/win32/Mmc/nn-mmc-icontextmenucallback?branch=master) — The IContextMenuCallback interface is used to add menu items to a context menu.
-   [**IContextMenuProvider**](/windows/win32/Mmc/nn-mmc-icontextmenuprovider?branch=master) — The IContextMenuProvider interface implements methods that create new context menus, for the purpose of adding items to those menus, to enable extensions to extend those menus, and to display the resultant context menus.
-   [**IControlbar**](/windows/win32/Mmc/nn-mmc-icontrolbar?branch=master) — The IControlbar interface provides a way to create toolbars and other controls.
-   [**IDisplayHelp**](/windows/win32/Mmc/nn-mmc-idisplayhelp?branch=master) — The IDisplayHelp interface enables a snap-in to display a specific HTML Help topic within the merged MMC HTML Help collection file for the console.
-   [**IHeaderCtrl**](/windows/win32/Mmc/nn-mmc-iheaderctrl?branch=master) — Enables the manipulation of columns and indicates the kind of information that is to be presented in the result pane of the console.
-   [**IHeaderCtrl2**](/windows/win32/Mmc/nn-mmc-iheaderctrl2?branch=master) — Enables the manipulation of columns and indicates the kind of information that is to be presented in the result pane of the console.
-   [**IImageList**](/windows/win32/Mmc/nn-mmc-iimagelist?branch=master) — The IImageList interface enables the snap-in to insert images to be used as icons for items in the result or scope pane of the console.
-   [**IMenuButton**](/windows/win32/Mmc/nn-mmc-imenubutton?branch=master) — The IMenuButton interface enables the snap-in to add and manage menu buttons.
-   [**IMessageView**](/windows/win32/Mmc/nn-mmc-imessageview?branch=master) — The IMessageView interface provides support for specifying the text and icons for error messages displayed using the MMC message OCX control. MMC provides a message OCX control that snap-ins can use for that displays error messages in the result pane.
-   [**IPropertySheetCallback**](/windows/win32/Mmc/nn-mmc-ipropertysheetcallback?branch=master) — The IPropertySheetCallback interface is used by a snap-in to add its property pages to a property sheet.
-   [**IPropertySheetProvider**](/windows/win32/Mmc/nn-mmc-ipropertysheetprovider?branch=master) — The IPropertySheetProvider interface implements Win32 property sheets as COM objects. Snap-ins can use the IPropertySheetProvider interface for adding wizard pages to a snap-in. IPropertySheetProvider is also used when a snap-in adds a feature that has a property sheet as the user interface, but identifies it as something else.
-   [**IRequiredExtensions**](/windows/win32/Mmc/nn-mmc-irequiredextensions?branch=master) — The IRequiredExtensions interface enables a snap-in to add some or all of the extension snap-ins that extend it.
-   [**IResultData**](/windows/win32/Mmc/nn-mmc-iresultdata?branch=master) — The IResultData interface enables a snap-in to add, remove, find, and modify items associated with the result pane. It also enables the manipulation of the view style of the result pane.
-   [**IStringTable**](/windows/win32/Mmc/nn-mmc-istringtable?branch=master) — The IStringTable interface provides a means of storing string data with a snap-in. A string table is created in the console file as required for each snap-in by MMC.
-   [**IToolbar**](/windows/win32/Mmc/nn-mmc-itoolbar?branch=master) — The IToolbar interface is used to create new toolbars, to add items to them, to extend the toolbars, and to display the resultant new toolbars.

## COM Interfaces Implemented by the Snap-in

-   [**IComponent**](/windows/win32/Mmc/ns-wmidata-_msmcaevent_pcicomponenterror?branch=master) — The IComponent interface enables MMC to communicate with snap-ins. Similar to the IComponentData interface, IComponent is typically implemented at the view level and is closely associated with items being displayed in the result pane.
-   [**IComponentData**](/windows/win32/Mmc/nn-mmc-icomponentdata?branch=master) — The IComponentData interface enables MMC to communicate with snap-ins. Similar to the IComponent interface, IComponentData is typically implemented at the document level and is closely associated with items (folders) being displayed in the scope pane.
-   [**IEnumTASK**](/windows/win32/Mmc/nn-mmc-ienumtask?branch=master) — The IEnumTASK interface enables a snap-in to enumerate the tasks to add to a task pad.
-   [**IExtendContextMenu**](/windows/win32/Mmc/nn-mmc-iextendcontextmenu?branch=master) — The IExtendContextMenu interface enables snap-ins to add items to an existing context menu.
-   [**IExtendControlbar**](/windows/win32/Mmc/nn-mmc-iextendcontrolbar?branch=master) — The IExtendControlbar interface enables a snap-in to add control bars to the console. This provides a way to improve the functionality and appearance of your snap-in by adding toolbars or other user interface enhancements.
-   [**IExtendPropertySheet**](/windows/win32/Mmc/nn-mmc-iextendpropertysheet?branch=master) — Enables a snap-in to add pages to the property sheet of an item.
-   [**IExtendPropertySheet2**](/windows/win32/Mmc/nn-mmc-iextendpropertysheet2?branch=master) — Enables a snap-in to add pages to the property sheet of an item.
-   [**IExtendTaskpad**](/windows/win32/Mmc/nn-mmc-iextendtaskpad?branch=master) — The IExtendTaskpad interface enables a snap-in to set up a taskpad and receive notifications from the taskpad.
-   [**IResultDataCompare**](/windows/win32/Mmc/nn-mmc-iresultdatacompare?branch=master) — The IResultDataCompare interface allows primary snap-ins to compare result items that are displayed in a sorted order in the result pane.
-   [**IResultDataCompareEx**](/windows/win32/Mmc/nn-mmc-iresultdatacompareex?branch=master) — The IResultDataCompareEx interface allows primary snap-ins to compare both scope and result items that are displayed in a sorted order in the result pane.
-   [**IResultOwnerData**](/windows/win32/Mmc/nn-mmc-iresultownerdata?branch=master) — The IResultOwnerData interface allows snap-ins to use virtual lists.
-   [**ISnapinAbout**](/windows/win32/Mmc/nn-mmc-isnapinabout?branch=master) — The ISnapinAbout interface enables the console to get copyright and version information from a snap-in. The console also uses this interface to obtain images for the static folder from the snap-in.
-   [**ISnapinHelp**](/windows/win32/Mmc/nn-mmc-isnapinhelp?branch=master) — Enables the console to get the location of a snap-in's compiled HTML Help file. The console merges the HTML Help files of all snap-ins with the MMC console HTML Help collection file.
-   [**ISnapinHelp2**](/windows/win32/Mmc/nn-mmc-isnapinhelp2?branch=master) — Enables the console to get the location of a snap-in's compiled HTML Help file. The console merges the HTML Help files of all snap-ins with the MMC console HTML Help collection file.

 

 




