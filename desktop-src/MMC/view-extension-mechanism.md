---
title: View Extension Mechanism
description: View extension snap-ins can be used to add user-interface elements to an existing view, or to create a new view.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 410f8a6a-7df2-4610-97e9-108e185d52a6
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# View Extension Mechanism

View extension snap-ins can be used to add user-interface elements to an existing view, or to create a new view. View extension snap-ins provide views that appear in a tab selector for view-extended nodes. A node is view-extended if the view extension CLSID is registered for the node's type. When the node is active, each registered view extension and console taskpad appears in the tab selector for the user to select.

A standard view will remain in the tab selector as long as it is not replaced by an extended view or hidden by a custom taskpad. An extended view can specify that it is replacing the standard view when the extended view is added.

A view extension snap-in implements a single interface, [**IExtendView**](iextendview.md), which contains a single method, [**IExtendView::GetViews**](iextendview-getviews.md). When MMC calls the view extension's IExtendView::GetViews method, MMC provides a pointer to an [**IViewExtensionCallback**](iviewextensioncallback.md) interface. The view extension calls the [**IViewExtensionCallback::AddView**](iviewextensioncallback-addview.md) method to add a view to the node.

The view extension can call the IViewExtensionCallback::AddView method multiple times to add multiple views. The IViewExtensionCallback::AddView method uses a pointer to an [**MMC\_EXT\_VIEW\_DATA**](mmc-ext-view-data.md) structure, which has the following definition.


```C++
typedef struct _MMC_EXT_VIEW_DATA
{
  GUID      viewID;
  LPCOLESTR pszURL;
  LPCOLESTR pszViewTitle;
  LPCOLESTR pszTooltipText;
  BOOL      bReplacesDefaultView;
}  MMC_EXT_VIEW_DATA, *PMMC_EXT_VIEW_DATA;
```



The MMC\_EXT\_VIEW\_DATA structure uniquely identifies the view and provides a URL (to the HTML used in the result pane) and title for the added view. The bReplacesDefaultView member controls whether the added view replaces the standard view.

View extensions can use script, including DHTML. A key feature of a view extension's ability to use script is that it can use the [MMC 2.0 Automation Object Model](mmc-2-0-automation-object-model.md). Another feature is the ability to create value-added user interface elements for a view. View extensions are not intended to add new management functionality to the snap-in. A namespace extension or a new primary snap-in could be used if added management functionality is the goal.

Be aware that MMC's **Back**/ **Forward** buttons are not connected to the DHTML displayed by a view extension. MMC's **Back**/ **Forward** buttons apply to the entire result view. A view extension should not introduce user interface state changes for a view unless the view can easily be recreated when the node is revisited. In particular, the HTML used by the view extension should not display hyperlinks that change the entire result view; there is no means for the user to return to the previous state.

## Related topics

<dl> <dt>

[**IExtendView**](iextendview.md)
</dt> <dt>

[**IViewExtensionCallback**](iviewextensioncallback.md)
</dt> <dt>

[**MMC\_EXT\_VIEW\_DATA**](mmc-ext-view-data.md)
</dt> <dt>

[**View Object**](view-object.md)
</dt> <dt>

[Extending Views](extending-views.md)
</dt> <dt>

[Using the Extended View Extension](using-the-extended-view-extension.md)
</dt> <dt>

[Using the Extended View Extension - Implementation Details](using-the-extended-view-extension-implementation-details.md)
</dt> </dl>

 

 




