---
title: Creating a new instance
description: This topic provides an overview of creating new instances of WMI objects.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: C6D51645-8C20-494D-A228-67CAC9FFE7F7
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Creating a new instance

This topic provides an overview of creating new instances of WMI objects.

A new class instance is typically created by using the CreateInstance intrinsic method. To create a new class instance, you'll need the following information.

-   The name of the PowerShell verb (new or add).
-   The name of the CIM provider method (CreateInstance or extrinsic static method).
-   If the CIM provider requires certain properties (or method parameters in the case of an extrinsic method) to be filled in for a newly created instance, these must be mandatory cmdlet parameters.

It is possible to create new class instances by using an extrinsic class, or static, method as well. From the CDXML perspective, the CreateInstance intrinsic method is like a class method.

 

 




