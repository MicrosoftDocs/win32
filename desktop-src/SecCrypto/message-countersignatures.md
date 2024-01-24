---
description: Sometimes a signed message requires a countersignature.
ms.assetid: de83a9ad-4e88-4477-8c9e-6dd7d5ec9e8f
title: Message Countersignatures
ms.topic: article
ms.date: 05/31/2018
---

# Message Countersignatures

Sometimes a signed message requires a [*countersignature*](../secgloss/c-gly.md). For example, user A may send a signed-data message to user B, expecting B to confirm agreement with the terms contained in the document. User B decodes the message, reads the terms and, if in agreement, countersigns the message. The countersigned message is then sent back to user A. User A now knows, and can prove, that user B agreed to the terms.

The following table lists sections that contain procedure descriptions or C program examples of message countersigning.



| Section                                                                                                                                 | Contents                                                           |
|-----------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| [Message Functions](cryptography-functions.md)                                                                       | Lists the counter signature functions.                             |
| [Countersigning a Message](countersigning-a-message.md)                                                                                | Details the process of counter signing a message.                  |
| [Verifying a Countersignature](verifying-a-countersignature.md)                                                                        | Details the procedure for verifying a counter signature.           |
| [Verifying a Signed Message](verifying-a-signed-message.md)                                                                            | Details a process for verifying the signature on a signed message. |
| [Example C Program: Encoding and Decoding a CounterSigned Message](example-c-program-encoding-and-decoding-a-countersigned-message.md) | Sample C program that encodes and decodes a countersigned message. |



 

 

 
