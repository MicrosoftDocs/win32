---
description: The low-level message functions encode data for transmission and decode data that has been received. Low-level message functions also decrypt and verify the signatures of received messages.
ms.assetid: 42c19920-c7f7-4a4d-9de3-3de9a34fbe0c
title: Low-level Message Functions
ms.topic: article
ms.date: 05/31/2018
---

# Low-level Message Functions

The [*low-level message functions*](../secgloss/l-gly.md) encode data for transmission and decode data that has been received. Low-level message functions also decrypt and verify the signatures of received messages.

When a message is opened using a low-level message open function, it remains open and available (maintains its [*state*](../secgloss/s-gly.md)) until it is closed. This allows a message to be constructed piecemeal using multiple calls to the [**CryptMsgUpdate**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsgupdate) function.

Using low-level message functions requires more function calls than using simplified message functions (see [Simplified Messages](simplified-messages.md)). If the simplified message functions are used, more of the work is done inside the functions of the API.

Using low-level message functions involves the additional work of making calls to other certificate or cryptographic functions. For example, data from calls to certificate functions may be needed to initialize structures used by these low-level message functions. Simplified message functions initialize many of these structures internally.

The following table lists sections with procedure descriptions and C code examples of using the low-level message functions.



| Section                                                                               | Contents                                           |
|---------------------------------------------------------------------------------------|----------------------------------------------------|
| [Low-level Message Functions](cryptography-functions.md) | Lists the low-level message functions.             |
| [Signing Data](signing-data.md)                                                      | Details the tasks needed to sign data.             |
| [Encoding Enveloped Data](encoding-enveloped-data.md)                                | Details the tasks needed to encode enveloped data. |
| [Decoding Enveloped Data](decoding-enveloped-data.md)                                | Details the tasks needed to decode enveloped data. |



 

 

 
