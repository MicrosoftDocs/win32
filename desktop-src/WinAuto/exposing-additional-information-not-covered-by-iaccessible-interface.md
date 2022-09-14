---
title: Exposing Additional Information Not Covered by IAccessible Interface
description: Depending on their products, server developers might need to expose information or functionality in addition to Microsoft Active Accessibility support.
ms.assetid: c45009ca-6be3-4645-9097-36671a41dfce
ms.topic: article
ms.date: 05/31/2018
---

# Exposing Additional Information Not Covered by IAccessible Interface

Depending on their products, server developers might need to expose information or functionality in addition to Microsoft Active Accessibility support. If this is the case, work with assistive technology vendors (clients) to ensure that they add support for the features.

Do not attempt to extend the [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface. Interfaces cannot be changed once they are published. To expose additional information, use a custom interface and expose it by using one of the following techniques:

-   [Using OBJID\_NATIVEOM to expose a native object model interface for a window](using-objid-nativeom-to-expose-a-native-object-model-interface-for-a-window.md)
-   [Using QueryService to expose a native object model interface for an IAccessible object](using-queryservice-to-expose-a-native-object-model-interface-for-an-iaccessible-object.md)

Note that the goal of the [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface is to have a well-defined interface that is used by servers and clients. Before exposing custom interfaces, be sure to expose as much information as possible through **IAccessible**.

You cannot use [**QueryInterface**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-queryinterface(q)) to expose custom interfaces. Use **IServiceProvider::QueryService** as outlined in the following procedures.

 

 