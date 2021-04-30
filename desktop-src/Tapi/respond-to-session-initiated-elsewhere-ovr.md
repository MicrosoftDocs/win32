---
description: When a new communications session arrives, TAPI applications that registered an interest in the address and media type will be sent an event notification.
ms.assetid: 6074619c-6aa0-4b03-9208-10268682e704
title: Respond to Session Initiated Elsewhere
ms.topic: article
ms.date: 05/31/2018
---

# Respond to Session Initiated Elsewhere

When a new communications session arrives, TAPI applications that registered an interest in the [address](address-ovr.md) and [media type](media-type-ovr.md) will be sent an [event notification](event-notification.md). Only one application will be offered ownership [privileges](privilege-ovr.md) over the session. This application cannot refuse the session.

The initial call state of an incoming session is offering. While the call is in the offering state, an application can obtain information such as bearer mode and call reason, if the service providers supplied this information and it is available. Some call information may not be available immediately, such as caller ID.

There are six basic responses to an offered session: [answer](answer-ovr.md), [accept](accept-ovr.md), [handoff](handoffs-ovr.md), [drop](drop-ovr.md), [forward](forward-ovr.md), and [redirect](redirect-ovr.md). Depending on the service provider, the full set of these operations may not be available.

 

 



