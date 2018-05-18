---
title: Extending a Primary Snap-in's View
description: Before building your own view extension, determine whether the Extended View extension provides the capability required by your application.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '9c4c936e-f74a-4fbf-bd32-aa78ebb6da6e'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
---

# Extending a Primary Snap-in's View

Before building your own view extension, determine whether the Extended View extension provides the capability required by your application. For more information about the Extended View extension and how to determine if a custom view extension is necessary for your application, see [Using the Extended View Extension](using-the-extended-view-extension.md).

A view extension must implement the [**IExtendView**](iextendview.md) interface. Other than the methods inherited from the IUnknown interface, the **IExtendView** interface contains a single method, [**IExtendView::GetViews**](iextendview-getviews.md). The following C++ example code shows an implementation of IExtendView::GetViews.

## Related topics

<dl> <dt>

[**IExtendView**](iextendview.md)
</dt> <dt>

[**IExtendView::GetViews**](iextendview-getviews.md)
</dt> <dt>

[**IViewExtensionCallback**](iviewextensioncallback.md)
</dt> <dt>

[**IViewExtensionCallback::AddView**](iviewextensioncallback-addview.md)
</dt> </dl>

 

 




