---
title: Overview of Automation
description: Automation enables software packages to expose their unique features to scripting tools and other applications.
ms.assetid: 4e9d6769-d73e-4daa-88ef-3ab6fa9a1497
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Overview of Automation

Automation enables software packages to expose their unique features to scripting tools and other applications. Using Automation, you can:

-   Create applications and programming tools that expose objects.

-   Create and manipulate objects exposed in one application from another application.

-   Create tools that access and manipulate objects. These tools can include embedded macro languages, external programming tools, object browsers, and compilers.

The objects an application or programming tool exposes are called ActiveX objects. Applications and programming tools that access those objects are called ActiveX clients. ActiveX objects and clients interact as follows: Applications and other software packages that support ActiveX technology define and expose objects which can be acted on by ActiveX components. ActiveX components are physical files (for example .exe and .dll files) that contain classes, which are definitions of objects. Type information describes the exposed objects, and can be used by ActiveX components at either compile time or at run time.

## In this section



| Topic                                                                                         | Description                                                                                                                                                                               |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Exposing Objects](exposing-objects.md)<br/>                                           | Exposing objects provides a way to manipulate an application's tools programmatically.<br/>                                                                                         |
| [ActiveX Objects](activex-objects.md)<br/>                                             | An ActiveX object is an instance of a class that exposes properties, methods, and events to ActiveX clients.<br/>                                                                   |
| [ActiveX Clients](activex-clients.md)<br/>                                             | An ActiveX client is an application or programming tool that manipulates one or more ActiveX objects. The objects can exist in the same application or in another application.<br/> |
| [ActiveX Client and Object Interaction](activex-client-and-object-interaction.md)<br/> | ActiveX clients can access objects using [**IDispatch**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-idispatch) or by calling one of the member functions in the objects's vtable.<br/>                                     |
| [Type Libraries](type-libraries.md)<br/>                                               | A *type library* is a file or part of a file that describes the type of one or more ActiveX objects.<br/>                                                                           |



 

 

 





