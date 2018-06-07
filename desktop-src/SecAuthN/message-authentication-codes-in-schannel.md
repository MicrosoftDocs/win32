---
Description: A Message Authentication Code (MAC) is used to detect message tampering and forgery.
ms.assetid: 44f50407-8f55-49c4-9e42-2f1666c9da7c
title: Message Authentication Codes in Schannel
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Message Authentication Codes in Schannel

A [*Message Authentication Code*](https://msdn.microsoft.com/4c4402e9-7455-4868-978f-3899a8fd86c1) (MAC) is used to detect message tampering and forgery. The sender of a message creates a MAC by encrypting a one-way [*hash*](https://msdn.microsoft.com/4165b820-30fc-477e-a690-81109f161323) of the message body using a [*session key*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50) shared by sender and recipient. The MAC is appended to the message that is sent to the recipient. The message recipient generates the MAC again, using the shared session key and message body, and compares the generated MAC to the MAC received from the sender. If the two are identical, then the sender must have the shared session key, and the message has not been altered in transit.

In Schannel protocols, the algorithm used to generate the MAC is determined by the [cipher suite](cipher-suites-in-schannel.md) in use by the sender and recipient.

 

 



