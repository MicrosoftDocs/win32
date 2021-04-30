---
description: The hold operation allows a single address to handle multiple communications sessions.
ms.assetid: 65e22e4e-e346-41c2-929a-ba0d1f7f1732
title: Hold
ms.topic: article
ms.date: 05/31/2018
---

# Hold

The hold operation allows a single address to handle multiple communications sessions. Placing a session on a hard hold frees the user's line/address to make other calls. A call on hard hold typically cannot be transferred or included in a conference call, but a consultation call can. Consultation calls are initiated using [conference](conference-ovr.md) or [transfer](transfer-ovr.md) operations.

After a call has been successfully placed on hold, the call state typically transitions to the onhold state. While a call is on hold, the application can receive messages about state changes of the held call. For example, if the held party hangs up, the call state can transition to disconnected.

In a bridged situation, the hold operation may not actually place the call on hold. The status of other stations on the call can govern (for example, attempting to "hold" a call when other stations are participating is not possible); instead, the call can simply be changed to the inactive state while it remains connected at other stations.

Not all service providers support use of this operation.

**TAPI 2.x:** See [**lineHold**](/windows/win32/api/tapi/nf-tapi-linehold), [**lineUnhold**](/windows/win32/api/tapi/nf-tapi-lineunhold).

**TAPI 3.x:** See [**ITBasicCallControl::Hold**](/windows/desktop/api/tapi3if/nf-tapi3if-itbasiccallcontrol-hold).

 

 
