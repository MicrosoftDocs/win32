---
description: Session termination may originate with a user request, remote disconnection by the other party, or for application-specific reasons.
ms.assetid: 69ed2e2c-f1c7-4f69-86a0-3cfdd80e423d
title: Terminate a Session
ms.topic: article
ms.date: 05/31/2018
---

# Terminate a Session

Session termination may originate with a user request, remote disconnection by the other party, or for application-specific reasons. When a session is terminated, the [session identifier](session-identifier-ovr.md) remains valid until specifically released and can be used to gather post-connection data.

Session termination is completed by deallocating and releasing the resources associated with the session. If a session is merely dropped or disconnected but resources are not released, the result is a memory leak in the application and possibly in the service provider as well.

**TAPI 2.x:** See [**lineDrop**](/windows/win32/api/tapi/nf-tapi-linedrop), [**lineDeallocateCall**](/windows/win32/api/tapi/nf-tapi-linedeallocatecall).

**TAPI 3.x:** See [**ITBasicCallControl::Disconnect**](/windows/desktop/api/tapi3if/nf-tapi3if-itbasiccallcontrol-disconnect), perform a standard COM release on the Call object pointer.

 

 
