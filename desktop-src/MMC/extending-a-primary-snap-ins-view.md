---
title: Extending a Primary Snap-ins View
description: Before building your own view extension, determine whether the Extended View extension provides the capability required by your application.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9c4c936e-f74a-4fbf-bd32-aa78ebb6da6e
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Extending a Primary Snap-in's View

Before building your own view extension, determine whether the Extended View extension provides the capability required by your application. For more information about the Extended View extension and how to determine if a custom view extension is necessary for your application, see [Using the Extended View Extension](using-the-extended-view-extension.md).

A view extension must implement the [**IExtendView**](/windows/win32/Mmc/nn-mmc-iextendview?branch=master) interface. Other than the methods inherited from the IUnknown interface, the **IExtendView** interface contains a single method, [**IExtendView::GetViews**](/windows/win32/Mmc/nf-mmc-iextendview-getviews?branch=master). The following C++ example code shows an implementation of IExtendView::GetViews.

## Related topics

<dl> <dt>

[**IExtendView**](/windows/win32/Mmc/nn-mmc-iextendview?branch=master)
</dt> <dt>

[**IExtendView::GetViews**](/windows/win32/Mmc/nf-mmc-iextendview-getviews?branch=master)
</dt> <dt>

[**IViewExtensionCallback**](/windows/win32/Mmc/nn-mmc-iviewextensioncallback?branch=master)
</dt> <dt>

[**IViewExtensionCallback::AddView**](/windows/win32/Mmc/nf-mmc-iviewextensioncallback-addview?branch=master)
</dt> </dl>

 

 




