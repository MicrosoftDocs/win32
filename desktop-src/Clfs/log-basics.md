---
Description: The Common Log File System (CLFS) saves log records in a sequential order, and can ensure that the flushed log records are preserved&\#8212;even after a system failure.
ms.assetid: f9804eeb-4da1-44c2-8c21-893f4293eb5b
title: Log Basics
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Log Basics

The Common Log File System (CLFS) saves log records in a sequential order, and can ensure that the flushed log records are preserved—even after a system failure.

An application can fulfill one or more of the following roles when it uses CLFS to log records:

-   *Producer*. An application that actively creates records in a log.
-   *Consumer*. An application that actively reads records from a log.
-   *Producer* and *Consumer*. An application that creates records in a log and reads records from a log.

> [!Note]  
> The client application defines the format of a log record.

 

You can use CLFS to manage logs and set application policy. By default, some policies are implemented to simplify I/O operations, coordinate log use by multiple clients, and manage log size.

 

 



