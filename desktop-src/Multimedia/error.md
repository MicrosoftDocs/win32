---
title: Error
description: Error
ms.assetid: '1f9d3dba-be6d-4f7d-a80c-5bca8632e13f'
keywords: ["AVICap callback functions,error notification messages"]
---

# Error

A capture window uses error notification messages to notify your application of AVICap errors, such as running out of disk space, attempting to write to a read-only file, failing to access hardware, or dropping too many frames. The content of an error notification includes a message identifier and a formatted text string ready for display. Your application can use the message identifier to filter the notifications and limit the messages to present to the user. A message identifier of zero indicates a new operation is starting and the callback function should clear any displayed error message.

 

 




