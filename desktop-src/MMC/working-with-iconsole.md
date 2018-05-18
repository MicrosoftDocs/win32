---
title: Working with IConsole
description: Every instance of a snap-in that exists in the scope pane is unique, and the methods of the IConsole interface preserve that uniqueness.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'c2a42d41-9b87-45dd-acc1-c8e001659ba9'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["working with IConsole MMC"]
---

# Working with IConsole

Every instance of a snap-in that exists in the scope pane is unique, and the methods of the [**IConsole**](iconsole2.md) interface preserve that uniqueness. You use the [**SetHeader**](iconsole2-setheader.md) and [**SetToolbar**](iconsole2-settoolbar.md) methods to associate the [**IHeaderCtrl2**](iheaderctrl2.md) and [**IToolbar**](itoolbar.md) interfaces with the snap-in's instance of **IConsole** and to provide column headers and toolbars associated with the result pane. You can use the [**QueryResultView**](iconsole2-queryresultview.md) method to get a pointer to an **IUnknown** interface to the result pane control only if your view is a custom OCX. This is the way to get the pointer to the OCX's **IDispatch** interface.

The [**QueryScopeImageList**](iconsole2-queryscopeimagelist.md) and [**QueryResultImageList**](iconsole2-queryresultimagelist.md) methods allow you to get interface pointers to the image lists that the console provides for inserting icons in the scope and result pane. The [**QueryConsoleVerb**](iconsole2-queryconsoleverb.md) method allows the snap-in to incorporate the functionality of standard verbs such as cut, copy, and paste, while the [**SelectScopeItem**](iconsole2-selectscopeitem.md) method is used to programmatically select a scope item in the scope pane. The [**UpdateAllViews**](iconsole2-updateallviews.md) method generates a notification to update one or more views because the content has changed. You can obtain a handle to the main frame window by using the [**GetMainWindow**](iconsole2-getmainwindow.md) method. The remaining [**IConsole**](iconsole2.md) method is [**MessageBox**](iconsole2-messagebox.md), which the snap-in uses to provide information to the user.

The [**IConsole2**](iconsole2.md) interface is a newer version of the **IConsole** interface and is introduced in MMC version 1.1. **IConsole2** contains all the methods of **IConsole**, as well as three additional ones. The [**Expand**](iconsole2-expand.md) method enables the snap-in to expand or collapse an item in the scope pane. The [**IsTaskpadViewPreferred**](iconsole2-istaskpadviewpreferred.md) method determines whether the user prefers taskpad views by default. Finally, the [**SetStatusText**](iconsole2-setstatustext.md) method enables the snap-in to change the text in the status bar.

A pointer to the [**IConsole2**](iconsole2.md) interface is passed to the snap-in through [**IComponent::Initialize**](icomponent-initialize.md) and [**IComponentData::Initialize**](icomponentdata-initialize.md). Each [**IComponent**](icomponent.md) and [**IComponentData**](icomponentdata.md) object gets its own private **IConsole2** interface pointer.

When using the [**IConsole2**](iconsole2.md) interface for manipulating the result pane and result items, you should use the **IConsole2** interface pointer passed to the snap-in's [**IComponent**](icomponent.md) implementation that owns the view. When using **IConsole2** for manipulating the scope pane and scope items, use the **IConsole2** interface pointer passed to the snap-in's [**IComponentData**](icomponentdata.md) implementation.

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

 

 




