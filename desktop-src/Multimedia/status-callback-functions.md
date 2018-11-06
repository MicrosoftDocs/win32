---
title: Status Callback Functions
description: Status Callback Functions
ms.assetid: fe89fb97-0b56-4956-a1a6-f4ad2d06befa
keywords:
- AVICap callback functions,status
ms.topic: article
ms.date: 05/31/2018
---

# Status Callback Functions

A capture window can send messages to the status callback function while capturing video to disk or during other lengthy operations to notify your application of the progress of an operation. The status information includes a message identifier and a formatted text string ready for display. Your application can use the message identifier to filter the notifications and limit the messages to present to the user. During capture operations, the first message sent to the callback function is always IDS\_CAP\_BEGIN and the last is always IDS\_CAP\_END. A message identifier of zero indicates a new operation is starting and the callback function should clear the current status.

 

 




