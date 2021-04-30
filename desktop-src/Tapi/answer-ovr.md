---
description: The answer operation is an applications typical response to an offered communications session. If successful, this operation causes a session to transition into the connected state.
ms.assetid: '34ac0b34-1d1b-4657-a737-27a4ed9326af'
title: Answer
ms.topic: article
ms.date: 05/31/2018
---

# Answer

The answer operation is an application's typical response to an offered communications session. If successful, this operation causes a session to transition into the connected state.

In some telephony environments (like ISDN), where user alerting is separate from call offering, the application has the option to [accept](accept-ovr.md) a call prior to answering or to reject ([drop](drop-ovr.md)) or [redirect](redirect-ovr.md) the *offering* call.

If an answer operation is performed for a new session when a session is already active, the effect this has on the existing active session depends on the service provider's capabilities. The first call can be unaffected, it can automatically be dropped, or it can automatically be placed on hold. TAPI will send the appropriate event notifications concerning both calls.

In a bridged situation, if a call is connected but in the active state, it can be joined using the answer operation.

The application has the option to send user-user information at the time of the answer, if the service provider supports it.

**TAPI 2.x:** See [**lineAnswer**](/windows/win32/api/tapi/nf-tapi-lineanswer).

**TAPI 3.x:** See [**ITBasicCallControl::Answer**](/windows/desktop/api/tapi3if/nf-tapi3if-itbasiccallcontrol-answer).

 

 
