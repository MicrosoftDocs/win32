---
title: When to Use Snap-ins
description: Helps to decide whether a task is appropriate for snap-in development.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5d5ebd37-0249-48f7-928d-c42a4da1c701
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# When to Use Snap-ins

You can create snap-ins, utility programs, and wizards with similar functionality, but snap-ins are intended for administrative tasks. To help you decide if a task is appropriate for a snap-in, here are some guidelines:

Create a snap-in when the task:

-   Requires privileged access.
-   Is administrative in nature.
-   Involves configuration of a service.
-   Extends another snap-in.

Create a program for Control Panel when the task:

-   Is end-user oriented rather than administrative.
-   Does not need to be automated.
-   Requires high, centralized visibility.
-   Does not rely on another Windows user interface.

In some cases, you can create a wizard that a user can gain access to by using a snap-in. For example, create a wizard if a task:

-   Is focused and involves several Steps.
-   Is performed with moderate frequency.
-   Has high visibility.
-   Can be accomplished with a simple nonbranching set of Steps.

 

 




