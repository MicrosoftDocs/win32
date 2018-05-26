---
title: QOS Templates
description: The use of QOS templates enables applications to leverage well-known QOS settings for common transmission types.
ms.assetid: d1cc5634-25c9-42cf-923f-25c70c74dc2c
keywords:
- Quality of Service QOS , tasks, using templates
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# QOS Templates

The use of QOS templates enables applications to leverage well-known QOS settings for common transmission types. Templates can reduce the complexity associated with setting QOS parameters, because they enable application programmers to choose from established QOS settings (by using included and existing templates), or enable application programmers to create additional templates based for special QOS needs of applications, then simply apply that template to subsequent connections.

The RSVP SP provides three functions that facilitate the enumeration, use, creation, and deletion of QOS templates. These functions are:

-   [**WSAGetQOSByName**](https://msdn.microsoft.com/library/windows/desktop/ms741587)
-   [**WSCInstallQOSTemplate**](wscinstallqostemplate.md)
-   [**WSCRemoveQOSTemplate**](wscremoveqostemplate.md)

There are four activities associated with using QOS templates:

-   [Enumerating Available QOS Templates](enumerating-available-qos-templates.md)
-   [Applying a QOS Template](applying-a-qos-template.md)
-   [Installing a QOS Template](installing-a-qos-template.md)
-   [Removing a QOS Template](removing-a-qos-template.md)

 

 




