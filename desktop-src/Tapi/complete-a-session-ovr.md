---
description: Completion operations allow an application to specify how it wants to handle a session when factors such as a busy destination prevent normal connection.
ms.assetid: 71e61376-7913-42a9-a8e2-2ea6e4918f30
title: Complete a Session
ms.topic: article
ms.date: 05/31/2018
---

# Complete a Session

Completion operations allow an application to specify how it wants to handle a session when factors such as a busy destination prevent normal connection.

The [LINECALLCOMPLMODE\_ Constants](./linecallcomplmode--constants.md) define the possible options an application might have, depending on service provider capabilities.

Multiple call completion requests might be outstanding for a given address at any one time. To identify individual requests, the implementation returns a [completion identifier](completion-id-ovr.md). Canceling a call completion request in progress also uses this call completion identifier.

**TAPI 2.x:** See [**lineCompleteCall**](/windows/win32/api/tapi/nf-tapi-linecompletecall), [**lineUncompleteCall**](/windows/win32/api/tapi/nf-tapi-lineuncompletecall).

**TAPI 3.x:** See [**ITBasicCallControl::Connect**](/windows/desktop/api/tapi3if/nf-tapi3if-itbasiccallcontrol-connect), [**ITBasicCallControl::Disconnect**](/windows/desktop/api/tapi3if/nf-tapi3if-itbasiccallcontrol-disconnect).

 

 
