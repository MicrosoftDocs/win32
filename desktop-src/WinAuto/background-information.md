---
title: Background Information
description: The Microsoft Active Accessibility component, oleacc.dll, creates proxy objects that implement IAccessible on behalf of standard Windows controls.
ms.assetid: c010af48-384c-40c0-ab52-c80b225502fb
ms.topic: article
ms.date: 05/31/2018
---

# Background Information

The Microsoft Active Accessibility component, oleacc.dll, creates proxy objects that implement [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) on behalf of standard Windows controls. Because these proxies use standard Windows messages and control-specific APIs to collect information about each control, there has been no direct mechanism for customizing the information these proxies expose through **IAccessible**.

Currently, you can customize an existing [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) implementation using subclassing and wrapping techniques. However, these techniques are tedious and error-prone. In fact, the majority of the code written to override one or two properties is concerned with implementing subclassing and wrapping; only a small fraction carries out the real task of overriding information. Dynamic Annotation improves the situation by providing similar capabilities without requiring you to write subclassing or wrapping code. Instead, you can focus on providing code that supplies the correct information. Dynamic Annotation allows developers to pass hints and other useful information to OLEACC to customize the information it exposes. This capability alone will reduce the cost of supporting Microsoft Active Accessibility and allow developers to greatly improve the accessibility of their user interfaces.

 

 




