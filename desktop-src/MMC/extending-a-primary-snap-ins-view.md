---
title: Extending a Primary Snap-in's View
description: Before building your own view extension, determine whether the Extended View extension provides the capability required by your application.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9c4c936e-f74a-4fbf-bd32-aa78ebb6da6e
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Extending a Primary Snap-in's View

Before building your own view extension, determine whether the Extended View extension provides the capability required by your application. For more information about the Extended View extension and how to determine if a custom view extension is necessary for your application, see [Using the Extended View Extension](using-the-extended-view-extension.md).

A view extension must implement the [**IExtendView**](/windows/desktop/api/Mmc/nn-mmc-iextendview) interface. Other than the methods inherited from the IUnknown interface, the **IExtendView** interface contains a single method, [**IExtendView::GetViews**](/windows/desktop/api/Mmc/nf-mmc-iextendview-getviews). The following C++ example code shows an implementation of IExtendView::GetViews.

## Related topics

<dl> <dt>

[**IExtendView**](/windows/desktop/api/Mmc/nn-mmc-iextendview)
</dt> <dt>

[**IExtendView::GetViews**](/windows/desktop/api/Mmc/nf-mmc-iextendview-getviews)
</dt> <dt>

[**IViewExtensionCallback**](/windows/desktop/api/Mmc/nn-mmc-iviewextensioncallback)
</dt> <dt>

[**IViewExtensionCallback::AddView**](/windows/desktop/api/Mmc/nf-mmc-iviewextensioncallback-addview)
</dt> </dl>

 

 




