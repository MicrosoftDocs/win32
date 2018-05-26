---
title: Exposing Objects
description: Exposing objects provides a way to manipulate an applications tools programmatically.
ms.assetid: 097d9cd4-577a-48b8-befe-ccd370c98109
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Exposing Objects

Exposing objects provides a way to manipulate an application's tools programmatically. This allows customers to use a programming tool that automates repetitive tasks that might not have been anticipated.

For example, Microsoft Excel exposes a variety of objects that can be used to build applications. One such object is the Workbook, which contains a group of related worksheets, charts, and macros — the Microsoft Excel equivalent of a three-ring binder. Using Automation, you could write an application that accesses Microsoft Excel Workbook objects, possibly to print them, as in the following diagram:

With Automation, solution providers can use your general-purpose objects to build applications that target a specific task. For example, you could use a general-purpose drawing tool to expose objects that draw boxes, lines, and arrows, insert text, and so forth. Another programmer could build a flowchart tool by accessing the exposed objects and then adding a user interface and other application-specific features.

Exposing objects to Automation or supporting Automation within a macro language offers several benefits.

-   Exposed objects from many applications are available in a single programming environment. Software developers can choose from these objects to create solutions that span applications.

-   Exposed objects are accessible from any macro language or programming tool that implements Automation. Systems integrators are not limited to the programming language in which the objects were developed. Instead, they can choose the programming tool or macro language that best suits their own needs and capabilities.

-   Object names can remain consistent across versions of an application, and can conform automatically to the user's national language.

 

 




