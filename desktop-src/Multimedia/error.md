---
title: Error
description: Error
ms.assetid: 'd3a087e4-7b57-4070-aa82-3673bc18a54f'
keywords:
- AVICap callback functions,error notification messages
ms.topic: article
ms.date: 05/31/2018
---

# Error

A capture window uses error notification messages to notify your application of AVICap errors, such as running out of disk space, attempting to write to a read-only file, failing to access hardware, or dropping too many frames. The content of an error notification includes a message identifier and a formatted text string ready for display. Your application can use the message identifier to filter the notifications and limit the messages to present to the user. A message identifier of zero indicates a new operation is starting and the callback function should clear any displayed error message.

 

 




