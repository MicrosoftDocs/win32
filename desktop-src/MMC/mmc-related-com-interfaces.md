---
title: MMC 2.0 Related COM Interfaces
description: Enumerates COM interfaces for use in developing snap-ins.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b5602e58-45a4-4b8c-807d-522a2bd27f44
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- MMC 2.0 related COM interfaces
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MMC 2.0: Related COM Interfaces

MMC provides a number of COM interfaces for use in developing snap-ins. Snap-ins implement some of these interfaces and expose them to MMC. MMC implements the remaining interfaces and exposes them to snap-ins to use. As a result, much of the functionality you are likely to want for your snap-in is already available to you.

MMC creates instances of your snap-in as required and calls the methods of the interfaces that your snap-in exposes. In turn, your snap-in can call the methods of the interfaces that MMC exposes, thereby incorporating features such as toolbars, context menus, and property sheets.

MMC implements the following interfaces:

[**IColumnData**](/windows/win32/Mmc/nn-mmc-icolumndata?branch=master) (new in MMC 1.2)

[**IConsole2**](/windows/win32/Mmc/nn-mmc-iconsole2?branch=master)

[**IConsoleNameSpace2**](/windows/win32/Mmc/nn-mmc-iconsolenamespace2?branch=master)

[**IConsoleVerb**](/windows/win32/Mmc/nn-mmc-iconsoleverb?branch=master)

[**IContextMenuCallback**](/windows/win32/Mmc/nn-mmc-icontextmenucallback?branch=master)

[**IContextMenuProvider**](/windows/win32/Mmc/nn-mmc-icontextmenuprovider?branch=master)

[**IControlbar**](/windows/win32/Mmc/nn-mmc-icontrolbar?branch=master)

[**IDisplayHelp**](/windows/win32/Mmc/nn-mmc-idisplayhelp?branch=master)

[**IHeaderCtrl2**](/windows/win32/Mmc/nn-mmc-iheaderctrl2?branch=master) (new in MMC 1.2)

[**IImageList**](/windows/win32/Mmc/nn-mmc-iimagelist?branch=master)

[**IMenuButton**](/windows/win32/Mmc/nn-mmc-imenubutton?branch=master)

[**IPropertySheetCallback**](/windows/win32/Mmc/nn-mmc-ipropertysheetcallback?branch=master)

[**IPropertySheetProvider**](/windows/win32/Mmc/nn-mmc-ipropertysheetprovider?branch=master)

[**IResultData**](/windows/win32/Mmc/nn-mmc-iresultdata?branch=master)

[**IToolbar**](/windows/win32/Mmc/nn-mmc-itoolbar?branch=master)

Snap-ins implement the following interfaces:

[**IComponent**](/windows/win32/Mmc/ns-wmidata-_msmcaevent_pcicomponenterror?branch=master)

[**IComponentData**](/windows/win32/Mmc/nn-mmc-icomponentdata?branch=master)

[**IEnumTASK**](/windows/win32/Mmc/nn-mmc-ienumtask?branch=master)

[**IExtendContextMenu**](/windows/win32/Mmc/nn-mmc-iextendcontextmenu?branch=master)

[**IExtendControlbar**](/windows/win32/Mmc/nn-mmc-iextendcontrolbar?branch=master)

[**IExtendPropertySheet2**](/windows/win32/Mmc/nn-mmc-iextendpropertysheet2?branch=master)

[**IExtendTaskPad**](/windows/win32/Mmc/nn-mmc-iextendtaskpad?branch=master)

[**IRequiredExtensions**](/windows/win32/Mmc/nn-mmc-irequiredextensions?branch=master)

[**IResultDataCompare**](/windows/win32/Mmc/nn-mmc-iresultdatacompare?branch=master)

[**IResultDataCompareEx**](/windows/win32/Mmc/nn-mmc-iresultdatacompareex?branch=master) (new in MMC 1.2)

[**IResultOwnerData**](/windows/win32/Mmc/nn-mmc-iresultownerdata?branch=master)

[**ISnapinAbout**](/windows/win32/Mmc/nn-mmc-isnapinabout?branch=master)

[**ISnapinHelp2**](/windows/win32/Mmc/nn-mmc-isnapinhelp2?branch=master)

Depending on the features you want, you may not need to use or implement all of these interfaces in your snap-in. Other sections of this overview refer to these interfaces and their methods frequently, so familiarizing yourself with them now may be helpful.

 

 




