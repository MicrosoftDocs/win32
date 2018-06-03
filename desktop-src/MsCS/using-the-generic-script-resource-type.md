---
title: Using the Generic Script Resource Type
description: The Generic Script resource type provides an easy way to achieve high availability for applications that can be controlled through scriptable interfaces.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 696f73f5-5b38-482f-9add-12a3cd9c5335
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Generic Script resource type Failover Cluster , using
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using the Generic Script Resource Type

The Generic Script resource type provides an easy way to achieve high availability for applications that can be controlled through scriptable interfaces (for example, ActiveX objects or WMI providers). If you have an application that can be started, stopped, and monitored through a script, you can run the application as a scripted resource and implement the Generic Script resource DLL entry points in the script file. A scripted resource is an instance of the Generic Script resource type under the control of a script.

**To create a scripted resource**

1.  Create a script file that implements required and optional entry points. See [Scripting Entry Points](scripting-entry-points.md).
2.  Create an instance of the Generic Script resource type (see [Creating Resources](creating-resources.md)).
3.  Set the ScriptPath property to specify the location of your script file (see [Setting Properties](setting-properties.md)).

For each instance of a scripted resource, the Generic Script resource DLL runs an instance of your script in a separate worker thread. Thus there is no need to implement instance management in your script; as far as your script is concerned there is one and only one resource instance.

The Generic Script resource DLL also creates a script object representing the resource. This object, [**Resource**](resource-object.md), allows your script to change properties

 

 




