---
description: An enveloped message is a message that is encrypted for a recipient or set of recipients.
ms.assetid: caf86ec8-48b6-4017-95ad-7a21fcaed4cf
title: Creating and Receiving Enveloped Data Messages
ms.topic: article
ms.date: 05/31/2018
---

# Creating and Receiving Enveloped Data Messages

An enveloped message is a message that is encrypted for a set of recipients. In the envelopment process, a session encryption key is generated and the message is encrypted with that key. The encryption key itself is then encrypted separately for each recipient using the public keys from each intended recipient's certificate. The enveloped message consists of the encrypted message, the certificates of the intended recipients, and the set of encrypted keys, one for each recipient. The message generated is in [*PKCS \#7*](../secgloss/p-gly.md)/CMS format.

The following sections show procedures and examples for enveloped message tasks:

-   [Encoding Enveloped Data](encoding-enveloped-data.md)
-   [Decoding Enveloped Data](decoding-enveloped-data.md)
-   [Alternate Code for Encoding an Enveloped Message](alternate-code-for-encoding-an-enveloped-message.md)
-   [Example C Program: Encoding an Enveloped, Signed Message](example-c-program-encoding-an-enveloped-signed-message.md)

 

 
