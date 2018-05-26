---
title: Snap-in Namespace
description: Describes the snap-in namespace.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8ee01346-e969-462c-a937-1dec89ba7e6c
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- snap-in namespace MMC
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Snap-in Namespace

Snap-ins and the objects they manage are represented in the scope pane as nodes on a tree control. These nodes can be divided into three types:

-   Built-in nodes
-   Static nodes
-   Enumerated nodes

Built-in nodes include folders, HTML pages, and ActiveX® controls (OCXs). MMC implements built-in nodes and they do not interact directly with your snap-in. The other types of nodes, static and enumerated, offer viewing mechanisms: details view, custom HTML page, custom ActiveX control (OCX), or taskpad.

A node's most important property is its node type. This is a GUID that describes the node's overall type; for example, whether it is a user, a machine, a domain entry in a Domain Name System (DNS) database, or something else. A node type is defined by the individual snap-in rather than by MMC and it is a GUID only because GUIDs ensure that name collisions do not occur. GUIDs in this context have no COM significance, although you generate them using Guidgen.exe just as you do other GUIDs.

 

 




