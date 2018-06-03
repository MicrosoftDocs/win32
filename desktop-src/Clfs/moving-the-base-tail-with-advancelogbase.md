---
Description: There are two ways to move the base tail. The first is to write a restart record by calling the WriteLogRestartArea function; the second is to call the AdvanceLogBase function.
ms.assetid: be443e31-a662-495d-a5d9-5309c8ff87bd
title: Moving the Base Tail
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Moving the Base Tail

There are two ways to move the base tail. The first is to write a [restart record](restart-records.md) by calling the [**WriteLogRestartArea**](/windows/desktop/api/Clfsw32/nf-clfsw32-writelogrestartarea) function; the second is to call the [**AdvanceLogBase**](/windows/desktop/api/Clfsw32/nf-clfsw32-advancelogbase) function.

The [**AdvanceLogBase**](/windows/desktop/api/Clfsw32/nf-clfsw32-advancelogbase) function allows a user to move the base tail to a flushed record without using the same marshaling area that is used to write data.

For example, in a producer and consumer scenario, each consumer has its own marshaling area that it reads data from. It does not write any records or restart records to the log, but the application moves the base tail to free up space.

Specifically, if two applications A and B share log X, application A, the producer, is a mini-filter that logs data, and application B, the consumer is a service that reads the log data and sends the information out over a network to application C. When application B receives an acknowledgment from application C that all data is received, application B no longer needs the data and can move the base tail.

 

 



