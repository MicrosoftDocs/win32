---
title: Context Uniqueness
description: NetShell is designed to be scripted and to be used remotely.
ms.assetid: 9118f70b-cb6d-45ef-8f5c-8d6b164aa82a
keywords:
- helper NetSh , command syntax, context uniqueness
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Context Uniqueness

NetShell is designed to be scripted and to be used remotely. As such, contexts should be capable of cutting and pasting into script files, without the need to change semantics. For example, if the **rip** context is designed to allow configuration commands specific to a given computer, it should provide a command that includes the command itself and the configuration parameter in a single command statement that can be cut and pasted, such as the following:

``` syntax
ip rip neighbor=10.0.0.1
```

 

 




