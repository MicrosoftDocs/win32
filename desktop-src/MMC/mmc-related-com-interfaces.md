---
title: MMC 2.0 Related COM Interfaces
description: Enumerates COM interfaces for use in developing snap-ins.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'b5602e58-45a4-4b8c-807d-522a2bd27f44'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["MMC 2.0 related COM interfaces"]
---

# MMC 2.0: Related COM Interfaces

MMC provides a number of COM interfaces for use in developing snap-ins. Snap-ins implement some of these interfaces and expose them to MMC. MMC implements the remaining interfaces and exposes them to snap-ins to use. As a result, much of the functionality you are likely to want for your snap-in is already available to you.

MMC creates instances of your snap-in as required and calls the methods of the interfaces that your snap-in exposes. In turn, your snap-in can call the methods of the interfaces that MMC exposes, thereby incorporating features such as toolbars, context menus, and property sheets.

MMC implements the following interfaces:

[**IColumnData**](icolumndata.md) (new in MMC 1.2)

[**IConsole2**](iconsole2.md)

[**IConsoleNameSpace2**](iconsolenamespace2.md)

[**IConsoleVerb**](iconsoleverb.md)

[**IContextMenuCallback**](icontextmenucallback.md)

[**IContextMenuProvider**](icontextmenuprovider.md)

[**IControlbar**](icontrolbar.md)

[**IDisplayHelp**](idisplayhelp.md)

[**IHeaderCtrl2**](iheaderctrl2.md) (new in MMC 1.2)

[**IImageList**](iimagelist.md)

[**IMenuButton**](imenubutton.md)

[**IPropertySheetCallback**](ipropertysheetcallback.md)

[**IPropertySheetProvider**](ipropertysheetprovider.md)

[**IResultData**](iresultdata.md)

[**IToolbar**](itoolbar.md)

Snap-ins implement the following interfaces:

[**IComponent**](icomponent.md)

[**IComponentData**](icomponentdata.md)

[**IEnumTASK**](ienumtask.md)

[**IExtendContextMenu**](iextendcontextmenu.md)

[**IExtendControlbar**](iextendcontrolbar.md)

[**IExtendPropertySheet2**](iextendpropertysheet2.md)

[**IExtendTaskPad**](iextendtaskpad.md)

[**IRequiredExtensions**](irequiredextensions.md)

[**IResultDataCompare**](iresultdatacompare.md)

[**IResultDataCompareEx**](iresultdatacompareex.md) (new in MMC 1.2)

[**IResultOwnerData**](iresultownerdata.md)

[**ISnapinAbout**](isnapinabout.md)

[**ISnapinHelp2**](isnapinhelp2.md)

Depending on the features you want, you may not need to use or implement all of these interfaces in your snap-in. Other sections of this overview refer to these interfaces and their methods frequently, so familiarizing yourself with them now may be helpful.

 

 




