---
title: Accessing the Containing Application
description: Describes how to access the Application object of a container.
ms.assetid: 696610c0-6944-4b90-8836-60bdc59ff6b0
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Accessing the Containing Application

Embedded objects that require access to the Application object of their container (the top-level programmability object for the process) should use the *ServiceProvider* interfaces to access it.

Containers should implement **IServiceProvider** with the same implementation as with **IOleClientSite**, and at the minimum, should support **SID\_Application**. If the container can also be embedded, use its container's **IServiceProvider** implementation to access the Application object. If an error occurs, embedded objects should perform a **QueryInterface** on **IOleClientSite** for **IServiceProvider** and use **IServiceProvider** to request **SID\_Application**.

The standards for Automation specify that document-level objects in an application's programmability model should support the **Parent** and **Application** properties. If this also doesn't work (because the immediate container does not support **IServiceProivder**, or **SID\_Application**), an embedded object can access the containing application by calling **IOleClientSite::GetContainer**, **QueryInterface**(IID\_IDispatch), followed by [**GetIDsOfNames**](/windows/previous-versions/oaidl/nf-oaidl-idispatch-getidsofnames?branch=master). This gets the DISPID for the **Parent** or **Application** property.

 

 




