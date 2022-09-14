---
title: Types of IAccessible Support
description: Types of IAccessible Support
ms.assetid: 4a61d9a4-3c05-4f12-bdf1-426223b679b5
ms.topic: article
ms.date: 05/31/2018
---

# Types of IAccessible Support

Microsoft Active Accessibility servers have two types of [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) support: native and proxied. The UI elements used in an application determine which type of support is appropriate. Many servers being written today take full advantage of **IAccessible** proxies and only implement **IAccessible** for those controls that are not proxied by Oleacc.dll, such as windowless controls or controls with a custom window class name.

## In this section

-   [Native Active Accessibility Implementation](native-active-accessibility-implementation.md)
-   [IAccessible Proxies](iaccessible-proxies.md)

 

 




