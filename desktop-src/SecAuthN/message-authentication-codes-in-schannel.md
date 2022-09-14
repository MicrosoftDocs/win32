---
description: A Message Authentication Code (MAC) is used to detect message tampering and forgery.
ms.assetid: 44f50407-8f55-49c4-9e42-2f1666c9da7c
title: Message Authentication Codes in Schannel
ms.topic: article
ms.date: 05/31/2018
---

# Message Authentication Codes in Schannel

A [*Message Authentication Code*](../secgloss/m-gly.md) (MAC) is used to detect message tampering and forgery. The sender of a message creates a MAC by encrypting a one-way [*hash*](../secgloss/h-gly.md) of the message body using a [*session key*](../secgloss/s-gly.md) shared by sender and recipient. The MAC is appended to the message that is sent to the recipient. The message recipient generates the MAC again, using the shared session key and message body, and compares the generated MAC to the MAC received from the sender. If the two are identical, then the sender must have the shared session key, and the message has not been altered in transit.

In Schannel protocols, the algorithm used to generate the MAC is determined by the [cipher suite](cipher-suites-in-schannel.md) in use by the sender and recipient.

 

 
