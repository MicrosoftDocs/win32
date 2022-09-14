---
description: WMI providers are usually designed to provide information about a specific managed object on a single computer.
ms.assetid: 9f23d599-ac37-4bfb-a3dc-0cef67e68b05
ms.tgt_platform: multiple
title: Linking Classes Together
ms.topic: article
ms.date: 05/31/2018
---

# Linking Classes Together

WMI providers are usually designed to provide information about a specific managed object on a single computer. If there is a common property that can serve as a key to uniquely identify all the different source instances, then use the [View Provider](view-provider.md) to combine properties from different classes, namespaces, or computers into a single class.

You must first [register the View Provider](registering-the-view-provider.md). After registration, you can create the following types of view classes:

-   [Join view](creating-a-new-instance-from-old-properties.md)

    Instances of different classes connected by a common property value.

-   [Association view](associating-instances-between-namespaces.md)

    Views of existing association classes across the namespace boundary.

-   [Union view](creating-a-union-view-class.md)

    Union of one or more instances.

 

 



