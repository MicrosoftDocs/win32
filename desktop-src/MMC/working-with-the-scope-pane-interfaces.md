---
title: Working with the Scope Pane Interfaces
description: The MMC SDK specifies several interfaces and other language constructs for working with the scope pane.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: dea974cd-4161-4edd-a383-7e45d0e7ae07
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- working with the scope pane MMC , interfaces
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Working with the Scope Pane: Interfaces

The MMC SDK specifies several interfaces and other language constructs for working with the scope pane. The following interfaces and methods are available for working with scope items:

-   [**IComponentData**](/windows/desktop/api/Mmc/nn-mmc-icomponentdata)
    -   [**IComponentData::GetDisplayInfo**](/windows/desktop/api/Mmc/nf-mmc-icomponentdata-getdisplayinfo)
-   [**IConsoleNamespace2**](/windows/desktop/api/Mmc/nn-mmc-iconsolenamespace2)
    -   [**IConsoleNamespace2::InsertItem**](https://www.bing.com/search?q=**IConsoleNamespace2::InsertItem**)
    -   [**IConsoleNamespace2::DeleteItem**](https://www.bing.com/search?q=**IConsoleNamespace2::DeleteItem**)
    -   [**IConsoleNamespace2::SetItem**](https://www.bing.com/search?q=**IConsoleNamespace2::SetItem**)
    -   [**IConsoleNamespace2::GetItem**](https://www.bing.com/search?q=**IConsoleNamespace2::GetItem**)
    -   [**IConsoleNamespace2::GetChildItem**](https://www.bing.com/search?q=**IConsoleNamespace2::GetChildItem**)
    -   [**IConsoleNamespace2::GetNextItem**](https://www.bing.com/search?q=**IConsoleNamespace2::GetNextItem**)
    -   [**IConsoleNamespace2::GetParentItem**](https://www.bing.com/search?q=**IConsoleNamespace2::GetParentItem**)
    -   [**IConsoleNamespace2::Expand**](/windows/desktop/api/Mmc/nf-mmc-iconsolenamespace2-expand)
    -   [**IConsoleNamespace2::AddExtension**](/windows/desktop/api/Mmc/nf-mmc-iconsolenamespace2-addextension)
-   [**IConsole2**](/windows/desktop/api/Mmc/nn-mmc-iconsole2)
    -   [**IConsole2::Expand**](/windows/desktop/api/Mmc/nf-mmc-iconsole2-expand)
    -   [**IConsole2::SelectScopeItem**](https://www.bing.com/search?q=**IConsole2::SelectScopeItem**)
    -   [**IConsole2::NewWindow**](https://www.bing.com/search?q=**IConsole2::NewWindow**)

## Other Constructs

The following notifications are available for working with scope items:

-   [**MMCN\_EXPAND**](mmcn-expand.md)
-   [**MMCN\_EXPANDSYNC**](mmcn-expandsync.md)
-   [**MMCN\_PRELOAD**](mmcn-preload.md)
-   [**MMCN\_REMOVE\_CHILDREN**](mmcn-remove-children.md)

The following structures are available for working with scope items:

-   [**SCOPEDATAITEM**](/windows/desktop/api/Mmc/ns-mmc-_scopedataitem)
-   [**MMC\_EXPANDSYNC\_STRUCT**](/windows/desktop/api/Mmc/ns-mmc-_mmc_expandsync_struct)

## Related topics

<dl> <dt>

[Working with the Scope Pane: Implementation Details](working-with-the-scope-pane-implementation-details.md)
</dt> <dt>

[Working with the Scope Pane: Additional Topics](working-with-the-scope-pane-additional-topics.md)
</dt> </dl>

 

 




