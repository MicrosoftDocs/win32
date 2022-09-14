---
description: The Request Object is created using COM CoCreateInstance and exposes one interface, ITRequest.
ms.assetid: 1e4c71ce-6846-4e64-9346-455ed82aa458
title: Request Object
ms.topic: article
ms.date: 05/31/2018
---

# Request Object

The Request Object is created using COM **CoCreateInstance** and exposes one interface, [**ITRequest**](/windows/desktop/api/tapi3if/nn-tapi3if-itrequest). This interface exposes the [**MakeCall**](/windows/desktop/api/tapi3if/nf-tapi3if-itrequest-makecall) method, which allows a TAPI 3 application to use Assisted Telephony. Assisted Telephony provides telephony-enabled applications with a simple mechanism for making phone calls without requiring the developer to become fully literate in telephony.

For example, a spreadsheet application can add a "Make Call" button using Assisted Telephony without implementing the more elaborate controls available in a full TAPI application.

See the [Assisted Telephony Overview](assisted-telephony-overview.md) for additional information.

 

 



