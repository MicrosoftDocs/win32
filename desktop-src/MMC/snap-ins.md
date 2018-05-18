---
title: Snap-ins
description: Introduces the concept of a snap-in and describes the two types of snap-ins used with MMC.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'b7bc5fba-5578-426d-9018-7b3ed807a0fd'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["snap-ins MMC"]
---

# Snap-ins

An MMC console has no native system or network management functionality, but rather provides a common user interface for whatever management functionality it is populated with in the form of snap-ins.

A snap-in is a Component Object Model (COM) in-process server dynamic-link library (DLL). This COM interface is situated between MMC and the snap-in. MMC does not care how the snap-in communicates with the managed service. Snap-ins can communicate with the managed service through any data protocol that the managed service supports. MMC has no knowledge of the mechanism used for this communication. Both Microsoft developers and independent software vendors (ISVs) can create snap-ins.

There are two types of snap-ins:

<dl> <dt>

<span id="Stand-alone"></span><span id="stand-alone"></span><span id="STAND-ALONE"></span>*Stand-alone*
</dt> <dd>

A stand-alone snap-in, when loaded in a console, can perform its designated management task as the only snap-in loaded in the console.

</dd> <dt>

<span id="Extension"></span><span id="extension"></span><span id="EXTENSION"></span>*Extension*
</dt> <dd>

An extension snap-in adds functionality to a stand-alone snap-in. Extension snap-ins can add their own nodes as children of the stand-alone snap-in's node. They can also add context menu items, toolbar buttons, property pages, and taskpad tasks to the stand-alone snap-in's node. Depending on the item extended, an extension snap-in can further be classified as any combination of the following:

-   Namespace extension
-   Context menu extension
-   Toolbar extension
-   Menu button extension
-   Property page extension
-   Taskpad extension

</dd> </dl>

It is possible for a snap-in to operate as a stand-alone snap-in and also to extend the functionality of another snap-in as an extension snap-in. Snap-ins that take this double role are *dual-mode* snap-ins. For example, the Event Viewer snap-in reads the event logs of computers. If the Computer Management snap-in's computer object exists in the console, the Event Viewer snap-in automatically extends each instance of the computer object and provides appropriate event logs. When the Event Viewer snap-in is used as a stand-alone snap-in, an administrator must manually provide a computer name when the snap-in is opened, and the snap-in simply provides the event logs of this one computer.

 

 




