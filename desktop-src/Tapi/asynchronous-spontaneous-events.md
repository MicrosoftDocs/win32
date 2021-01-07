---
description: There is another class of asynchronous events besides those described above.
ms.assetid: eaf4b014-1cab-4707-b750-9088e745083e
title: Asynchronous Spontaneous Events
ms.topic: article
ms.date: 05/31/2018
---

# Asynchronous Spontaneous Events

There is another class of asynchronous events besides those described above. These events are "spontaneous" in the sense that they are not direct results of corresponding requests. These events are detected in such cases as when an incoming call arrives, or when an outbound call goes from a "ringing" to an "answering" state. When TAPI first initializes interactions with the TSPI for a particular device, it passes a pointer to a callback procedure to be called for reporting such spontaneous events. Along with this procedure pointer is a device handle that the service provider includes as one of the actual parameters to the callback.

 

 



