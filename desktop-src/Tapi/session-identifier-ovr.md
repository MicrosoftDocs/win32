---
description: TAPI assigns session identifiers that are unique for each session and application.
ms.assetid: 711a9bc6-ffc6-499b-8653-ba230028c146
title: Session Identifier
ms.topic: article
ms.date: 05/31/2018
---

# Session Identifier

TAPI assigns session identifiers that are unique for each session and application. An application uses a session identifier to communicate with TAPI concerning a specific session. An application typically obtains an identifier either by creating a new communications session or when TAPI offers a session.

A session identifier cannot be used to pass information to another application. For this purpose, use the [Call ID](call-id-ovr.md), which may be assigned by a service provider.

See [Initiate a session](initiate-a-session-ovr.md) for information on operations that create sessions and return a session identifier. See [Respond to session initiated elsewhere](respond-to-session-initiated-elsewhere-ovr.md) for operations that acquire session identifiers from TAPI. See [Terminate a Session](terminate-a-session-ovr.md) for information on releasing session resources.

All service providers must support some form of session identification.

**TAPI 2.x:** The primary identifier of a communications session is the call handle.

**TAPI 3.x:** A session is represented by a [Call Object](call-object.md) and the primary identifier is a pointer to the [**ITCallInfo**](/windows/desktop/api/tapi3if/nn-tapi3if-itcallinfo) interface.

 

 



