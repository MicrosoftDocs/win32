---
title: MMC 2.0 Interfaces
description: The following table lists interfaces that are introduced with Microsoft Management Console (MMC) version 2.0. For more information about the object model, see MMC 2.0 Automation Object Model.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1fcd1317-5777-4ea9-bfb6-ab57e8d6adbf
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Microsoft Management Console 2.0 MMC , MMC 2.0 reference, interfaces
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MMC 2.0 Interfaces

The following table lists interfaces that are introduced with Microsoft Management Console (MMC) version 2.0. For more information about the object model, see [MMC 2.0 Automation Object Model](mmc-2-0-automation-object-model.md).



| Interface                                                      | Description                                                                                                                                                                                                                                                                                              |
|----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IComponent2**](/windows/win32/Mmc/nn-mmc-icomponent2?branch=master)                             | Provides methods to specify a result view type and to restore a result view. Additionally, provides an IDispatch interface to the [MMC 2.0 Automation Object Model](mmc-2-0-automation-object-model.md), through the [**View object**](view-object.md). Supersedes the IComponent interface.           |
| [**IComponentData2**](/windows/win32/Mmc/nn-mmc-icomponentdata2?branch=master)                     | Provides an IDispatch interface to the [MMC 2.0 Automation Object Model](mmc-2-0-automation-object-model.md) through the [**View object**](view-object.md). Supersedes the IComponentData interface.                                                                                                   |
| [**IConsole3**](/windows/win32/Mmc/nn-mmc-iconsole3?branch=master)                                 | Provides a method to rename a new scope item. Supersedes the IConsole2 interface.                                                                                                                                                                                                                        |
| [**IConsolePower**](/windows/win32/Mmc/nn-mmc-iconsolepower?branch=master)                         | Controls the execution state and idle timers on operating systems that support power management.                                                                                                                                                                                                         |
| [**IConsolePowerSink**](/windows/win32/Mmc/nn-mmc-iconsolepowersink?branch=master)                 | Allows the MMC snap-in to control handling of WM\_POWERBROADCAST messages.                                                                                                                                                                                                                               |
| [**IContextMenuCallback2**](/windows/win32/Mmc/nn-mmc-icontextmenucallback2?branch=master)         | Provides a method to add menu items that contain a language-independent name. Supersedes the IContextMenuCallback interface.                                                                                                                                                                             |
| [**IExtendView**](/windows/win32/Mmc/nn-mmc-iextendview?branch=master)                             | Provides information about a view extension; view extensions must implement this interface. For more information, see [Extending Views](extending-views.md).                                                                                                                                            |
| [**IMMCVersionInfo**](/windows/win32/Mmc/nn-mmc-immcversioninfo?branch=master)                     | Provides MMC version information.                                                                                                                                                                                                                                                                        |
| [**INodeProperties**](/windows/win32/Mmc/nn-mmc-inodeproperties?branch=master)                     | Retrieves text-only properties for a node. This interface is used with the [Extended View extension](using-the-extended-view-extension.md). Other view extensions and the [MMC 2.0 Automation Object Model](mmc-2-0-automation-object-model.md) can also use this interface.                           |
| [**IResultData2**](/windows/win32/Mmc/nn-mmc-iresultdata2?branch=master)                           | Provides a method to rename a new result item. Supersedes the IResultData interface.                                                                                                                                                                                                                     |
| [**ISnapinProperties**](/windows/win32/Mmcobj/nn-mmcobj-isnapinproperties?branch=master)                 | Allows a snap-in to initialize its properties and to receive notification if a property is added, changed, or deleted.                                                                                                                                                                                   |
| [**ISnapinPropertiesCallback**](/windows/win32/Mmcobj/nn-mmcobj-isnapinpropertiescallback?branch=master) | Allows a snap-in to set its properties.                                                                                                                                                                                                                                                                  |
| [**IViewExtensionCallback**](/windows/win32/Mmc/nn-mmc-iviewextensioncallback?branch=master)       | Implemented by MMC and used by view extensions to add result pane views and optionally to remove the standard view from the tab of views. MMC passes a pointer to the IViewExtensionCallback interface when the view extension's [**IExtendView::GetViews**](/windows/win32/Mmc/nf-mmc-iextendview-getviews?branch=master) method is called. |



 

 

 




