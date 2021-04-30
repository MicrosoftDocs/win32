---
description: The enveloped message consists of the encrypted message, the certificates of the intended recipients, and the set of encrypted keys, one for each recipient. The message generated is in PKCS \#7/CMS format.
ms.assetid: 2acd0b58-1028-478d-bfa1-b02fa457d7e3
title: Creating and Receiving Enveloped Data Messages in CAPICOM
ms.topic: article
ms.date: 05/31/2018
---

# Creating and Receiving Enveloped Data Messages in CAPICOM

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the .NET Framework to implement security features. For more information, see [Alternatives to Using CAPICOM](alternatives-to-using-capicom.md).\]

An enveloped message is a message that is encrypted for a set of recipients. In the envelopment process, a session encryption key is generated and the message is encrypted with that key. The encryption key itself is then encrypted separately for each recipient using the public keys from each intended recipient's certificate. The enveloped message consists of the encrypted message, the certificates of the intended recipients, and the set of encrypted keys, one for each recipient. The message generated is in PKCS \#7/CMS format.

The following sections show procedures and examples for enveloped message tasks:

-   [Sending an Enveloped Data Message](sending-an-enveloped-data-message.md)
-   [Receiving an Enveloped Data Message](receiving-an-enveloped-data-message.md)

 

 



