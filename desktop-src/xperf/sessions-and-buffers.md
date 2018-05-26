---
title: Sessions and Buffers
description: Sessions and Buffers
ms.assetid: dcb5e58b-ab5a-4867-90be-c6b66864adb5
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Sessions and Buffers

A Windows Performance Analyzer (WPA) session is a collection of in-memory buffers, typically non-paged, managed by the kernel. These buffers accept events directly from the WPA Provider API. WPA event generation and buffering is lock free to allow events to be logged from any type of code.

Each system processor is assigned an "in-use" buffer. When an event is captured, space is reserved in the in-use buffer allocated to the processor on which the calling thread is running. The event header and data is then copied into the in-use buffer. When the buffer becomes full it is flushed to the log file or application assigned to that session. A free buffer is then assigned to that processor.

 

 




