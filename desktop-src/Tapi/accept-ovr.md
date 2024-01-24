---
description: In some environments, a user is not automatically alerted to an offering call, such as by ringing or by a message on their computer screen.
ms.assetid: 50684e2a-0799-458b-9402-0958e35026d7
title: Accept
ms.topic: article
ms.date: 05/31/2018
---

# Accept

In some environments, a user is not automatically alerted to an offering call, such as by ringing or by a message on their computer screen. The accept operation starts the process of alerting (usually ringing), and the [answer](answer-ovr.md) operation takes place afterward. The application may [drop](drop-ovr.md) the session, [redirect](redirect-ovr.md) it, or accept it.

If the current service provider supports it, the application has the option to send user-user information at the time of the accept. There is no guarantee that the network will deliver this information to the calling party.

Not all service providers support use of this operation.

**TAPI 2.x:** See [**lineAccept**](/windows/win32/api/tapi/nf-tapi-lineaccept).

 

 
