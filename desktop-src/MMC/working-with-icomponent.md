---
title: Working with IComponent
description: Among the IComponent methods, the Initialize method provides an entry point for the snap-in by allowing QueryInterface calls to IConsole.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 137d9e95-144c-4a78-8a29-aa29685c513c
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- working with IComponent MMC
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Working with IComponent

Among the [**IComponent**](/windows/desktop/api/Mmc/nn-mmc-icomponent) methods, the [**Initialize**](/windows/desktop/api/Mmc/nf-mmc-icomponent-initialize) method provides an entry point for the snap-in by allowing [**QueryInterface**](https://www.bing.com/search?q=**QueryInterface**) calls to [**IConsole**](/windows/desktop/api/Mmc/nn-mmc-iconsole2). The console calls the [**Notify**](/windows/desktop/api/Mmc/nf-mmc-icomponent-notify) method to notify the snap-in component that an event has occurred as a result of a user action. The [**Destroy**](/windows/desktop/api/Mmc/nf-mmc-icomponent-destroy) method releases all interfaces to the console such as **IConsole**.

The [**QueryDataObject**](/windows/desktop/api/Mmc/nf-mmc-icomponent-querydataobject) method returns a pointer to an [**IDataObject**](https://www.bing.com/search?q=**IDataObject**) that provides further information about the item specified by the *cookie* parameter. The *type* parameter indicates the context in which the data object is required. A value of CCT\_SCOPE or CCT\_SNAPIN\_MANAGER indicates that the data object is for a scope item. A value of CCT\_SNAPIN\_MANAGER further indicates that the Snap-in Manager has requested the data object. A value of CCT\_RESULT indicates that the cookie is that of a result item.

The [**GetResultViewType**](/windows/desktop/api/Mmc/nf-mmc-icomponent-getresultviewtype) method determines the type of view in the result pane (for example, default list view, ActiveX® control (OCX), URL path). The [**GetDisplayInfo**](/windows/desktop/api/Mmc/nf-mmc-icomponent-getdisplayinfo) method retrieves display information for a result item. The [**CompareObjects**](/windows/desktop/api/Mmc/nf-mmc-icomponent-compareobjects) method provides a way for a snap-in component to compare two result items.

## Related topics

<dl> <dt>

[Working with IComponentData](working-with-icomponentdata.md)
</dt> <dt>

[Working with IDataObject](working-with-idataobject.md)
</dt> <dt>

[Working with IConsole](working-with-iconsole.md)
</dt> <dt>

[Registering and Unregistering a Snap-in](registering-and-unregistering-a-snap-in.md)
</dt> </dl>

 

 




