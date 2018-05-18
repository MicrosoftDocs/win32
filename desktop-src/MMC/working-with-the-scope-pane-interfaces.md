---
title: Working with the Scope Pane Interfaces
description: The MMC SDK specifies several interfaces and other language constructs for working with the scope pane.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'dea974cd-4161-4edd-a383-7e45d0e7ae07'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["working with the scope pane MMC , interfaces"]
---

# Working with the Scope Pane: Interfaces

The MMC SDK specifies several interfaces and other language constructs for working with the scope pane. The following interfaces and methods are available for working with scope items:

-   [**IComponentData**](icomponentdata.md)
    -   [**IComponentData::GetDisplayInfo**](icomponentdata-getdisplayinfo.md)
-   [**IConsoleNamespace2**](iconsolenamespace2.md)
    -   [**IConsoleNamespace2::InsertItem**](iconsolenamespace2-insertitem.md)
    -   [**IConsoleNamespace2::DeleteItem**](iconsolenamespace2-deleteitem.md)
    -   [**IConsoleNamespace2::SetItem**](iconsolenamespace2-setitem.md)
    -   [**IConsoleNamespace2::GetItem**](iconsolenamespace2-getitem.md)
    -   [**IConsoleNamespace2::GetChildItem**](iconsolenamespace2-getchilditem.md)
    -   [**IConsoleNamespace2::GetNextItem**](iconsolenamespace2-getnextitem.md)
    -   [**IConsoleNamespace2::GetParentItem**](iconsolenamespace2-getparentitem.md)
    -   [**IConsoleNamespace2::Expand**](iconsolenamespace2-expand.md)
    -   [**IConsoleNamespace2::AddExtension**](iconsolenamespace2-addextension.md)
-   [**IConsole2**](iconsole2.md)
    -   [**IConsole2::Expand**](iconsole2-expand.md)
    -   [**IConsole2::SelectScopeItem**](iconsole2-selectscopeitem.md)
    -   [**IConsole2::NewWindow**](iconsole2-newwindow.md)

## Other Constructs

The following notifications are available for working with scope items:

-   [**MMCN\_EXPAND**](mmcn-expand.md)
-   [**MMCN\_EXPANDSYNC**](mmcn-expandsync.md)
-   [**MMCN\_PRELOAD**](mmcn-preload.md)
-   [**MMCN\_REMOVE\_CHILDREN**](mmcn-remove-children.md)

The following structures are available for working with scope items:

-   [**SCOPEDATAITEM**](scopedataitem.md)
-   [**MMC\_EXPANDSYNC\_STRUCT**](mmc-expandsync-struct.md)

## Related topics

<dl> <dt>

[Working with the Scope Pane: Implementation Details](working-with-the-scope-pane-implementation-details.md)
</dt> <dt>

[Working with the Scope Pane: Additional Topics](working-with-the-scope-pane-additional-topics.md)
</dt> </dl>

 

 




