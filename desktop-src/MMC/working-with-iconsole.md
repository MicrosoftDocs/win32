---
title: Working with IConsole
description: Every instance of a snap-in that exists in the scope pane is unique, and the methods of the IConsole interface preserve that uniqueness.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c2a42d41-9b87-45dd-acc1-c8e001659ba9
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- working with IConsole MMC
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Working with IConsole

Every instance of a snap-in that exists in the scope pane is unique, and the methods of the [**IConsole**](/windows/desktop/api/Mmc/nn-mmc-iconsole2) interface preserve that uniqueness. You use the [**SetHeader**](https://www.bing.com/search?q=**SetHeader**) and [**SetToolbar**](https://www.bing.com/search?q=**SetToolbar**) methods to associate the [**IHeaderCtrl2**](/windows/desktop/api/Mmc/nn-mmc-iheaderctrl2) and [**IToolbar**](/windows/desktop/api/Mmc/nn-mmc-itoolbar) interfaces with the snap-in's instance of **IConsole** and to provide column headers and toolbars associated with the result pane. You can use the [**QueryResultView**](https://www.bing.com/search?q=**QueryResultView**) method to get a pointer to an **IUnknown** interface to the result pane control only if your view is a custom OCX. This is the way to get the pointer to the OCX's **IDispatch** interface.

The [**QueryScopeImageList**](https://www.bing.com/search?q=**QueryScopeImageList**) and [**QueryResultImageList**](https://www.bing.com/search?q=**QueryResultImageList**) methods allow you to get interface pointers to the image lists that the console provides for inserting icons in the scope and result pane. The [**QueryConsoleVerb**](https://www.bing.com/search?q=**QueryConsoleVerb**) method allows the snap-in to incorporate the functionality of standard verbs such as cut, copy, and paste, while the [**SelectScopeItem**](https://www.bing.com/search?q=**SelectScopeItem**) method is used to programmatically select a scope item in the scope pane. The [**UpdateAllViews**](https://www.bing.com/search?q=**UpdateAllViews**) method generates a notification to update one or more views because the content has changed. You can obtain a handle to the main frame window by using the [**GetMainWindow**](https://www.bing.com/search?q=**GetMainWindow**) method. The remaining [**IConsole**](/windows/desktop/api/Mmc/nn-mmc-iconsole2) method is [**MessageBox**](https://www.bing.com/search?q=**MessageBox**), which the snap-in uses to provide information to the user.

The [**IConsole2**](/windows/desktop/api/Mmc/nn-mmc-iconsole2) interface is a newer version of the **IConsole** interface and is introduced in MMC version 1.1. **IConsole2** contains all the methods of **IConsole**, as well as three additional ones. The [**Expand**](/windows/desktop/api/Mmc/nf-mmc-iconsole2-expand) method enables the snap-in to expand or collapse an item in the scope pane. The [**IsTaskpadViewPreferred**](/windows/desktop/api/Mmc/nf-mmc-iconsole2-istaskpadviewpreferred) method determines whether the user prefers taskpad views by default. Finally, the [**SetStatusText**](/windows/desktop/api/Mmc/nf-mmc-iconsole2-setstatustext) method enables the snap-in to change the text in the status bar.

A pointer to the [**IConsole2**](/windows/desktop/api/Mmc/nn-mmc-iconsole2) interface is passed to the snap-in through [**IComponent::Initialize**](/windows/desktop/api/Mmc/nf-mmc-icomponent-initialize) and [**IComponentData::Initialize**](/windows/desktop/api/Mmc/nf-mmc-icomponentdata-initialize). Each [**IComponent**](/windows/desktop/api/Mmc/nn-mmc-icomponent) and [**IComponentData**](/windows/desktop/api/Mmc/nn-mmc-icomponentdata) object gets its own private **IConsole2** interface pointer.

When using the [**IConsole2**](/windows/desktop/api/Mmc/nn-mmc-iconsole2) interface for manipulating the result pane and result items, you should use the **IConsole2** interface pointer passed to the snap-in's [**IComponent**](/windows/desktop/api/Mmc/nn-mmc-icomponent) implementation that owns the view. When using **IConsole2** for manipulating the scope pane and scope items, use the **IConsole2** interface pointer passed to the snap-in's [**IComponentData**](/windows/desktop/api/Mmc/nn-mmc-icomponentdata) implementation.

## Related topics

<dl> <dt>

[Working with IComponentData](working-with-icomponentdata.md)
</dt> <dt>

[Working with IComponent](working-with-icomponent.md)
</dt> <dt>

[Working with IDataObject](working-with-idataobject.md)
</dt> <dt>

[Registering and Unregistering a Snap-in](registering-and-unregistering-a-snap-in.md)
</dt> </dl>

 

 




