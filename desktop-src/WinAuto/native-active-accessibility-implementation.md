---
title: Native Active Accessibility Implementation
description: User interface elements that implement the IAccessible interface are said to provide a native implementation.
ms.assetid: 36a5c0cd-53f0-433e-8932-da7d1de177dd
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Native Active Accessibility Implementation

User interface elements that implement the [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) interface are said to provide a *native implementation*. Although the development cost for implementing **IAccessible** (or any other Component Object Model (COM) interface) can be high, the benefit is complete control over the information exposed to clients.

If your application uses custom controls or other controls that cannot be proxied by Oleacc.dll, you will need to provide a native implementation.

 

 




