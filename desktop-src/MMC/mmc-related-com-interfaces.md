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
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MMC 2.0: Related COM Interfaces

MMC provides a number of COM interfaces for use in developing snap-ins. Snap-ins implement some of these interfaces and expose them to MMC. MMC implements the remaining interfaces and exposes them to snap-ins to use. As a result, much of the functionality you are likely to want for your snap-in is already available to you.

MMC creates instances of your snap-in as required and calls the methods of the interfaces that your snap-in exposes. In turn, your snap-in can call the methods of the interfaces that MMC exposes, thereby incorporating features such as toolbars, context menus, and property sheets.

MMC implements the following interfaces:

[**IColumnData**](/windows/desktop/api/Mmc/nn-mmc-icolumndata) (new in MMC 1.2)

[**IConsole2**](/windows/desktop/api/Mmc/nn-mmc-iconsole2)

[**IConsoleNameSpace2**](/windows/desktop/api/Mmc/nn-mmc-iconsolenamespace2)

[**IConsoleVerb**](/windows/desktop/api/Mmc/nn-mmc-iconsoleverb)

[**IContextMenuCallback**](/windows/desktop/api/Mmc/nn-mmc-icontextmenucallback)

[**IContextMenuProvider**](/windows/desktop/api/Mmc/nn-mmc-icontextmenuprovider)

[**IControlbar**](/windows/desktop/api/Mmc/nn-mmc-icontrolbar)

[**IDisplayHelp**](/windows/desktop/api/Mmc/nn-mmc-idisplayhelp)

[**IHeaderCtrl2**](/windows/desktop/api/Mmc/nn-mmc-iheaderctrl2) (new in MMC 1.2)

[**IImageList**](/windows/desktop/api/Mmc/nn-mmc-iimagelist)

[**IMenuButton**](/windows/desktop/api/Mmc/nn-mmc-imenubutton)

[**IPropertySheetCallback**](/windows/desktop/api/Mmc/nn-mmc-ipropertysheetcallback)

[**IPropertySheetProvider**](/windows/desktop/api/Mmc/nn-mmc-ipropertysheetprovider)

[**IResultData**](/windows/desktop/api/Mmc/nn-mmc-iresultdata)

[**IToolbar**](/windows/desktop/api/Mmc/nn-mmc-itoolbar)

Snap-ins implement the following interfaces:

[**IComponent**](/windows/desktop/api/Mmc/nn-mmc-icomponent)

[**IComponentData**](/windows/desktop/api/Mmc/nn-mmc-icomponentdata)

[**IEnumTASK**](/windows/desktop/api/Mmc/nn-mmc-ienumtask)

[**IExtendContextMenu**](/windows/desktop/api/Mmc/nn-mmc-iextendcontextmenu)

[**IExtendControlbar**](/windows/desktop/api/Mmc/nn-mmc-iextendcontrolbar)

[**IExtendPropertySheet2**](/windows/desktop/api/Mmc/nn-mmc-iextendpropertysheet2)

[**IExtendTaskPad**](/windows/desktop/api/Mmc/nn-mmc-iextendtaskpad)

[**IRequiredExtensions**](/windows/desktop/api/Mmc/nn-mmc-irequiredextensions)

[**IResultDataCompare**](/windows/desktop/api/Mmc/nn-mmc-iresultdatacompare)

[**IResultDataCompareEx**](/windows/desktop/api/Mmc/nn-mmc-iresultdatacompareex) (new in MMC 1.2)

[**IResultOwnerData**](/windows/desktop/api/Mmc/nn-mmc-iresultownerdata)

[**ISnapinAbout**](/windows/desktop/api/Mmc/nn-mmc-isnapinabout)

[**ISnapinHelp2**](/windows/desktop/api/Mmc/nn-mmc-isnapinhelp2)

Depending on the features you want, you may not need to use or implement all of these interfaces in your snap-in. Other sections of this overview refer to these interfaces and their methods frequently, so familiarizing yourself with them now may be helpful.

 

 




