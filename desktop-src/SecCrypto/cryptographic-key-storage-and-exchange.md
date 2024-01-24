---
description: There are situations where keys must be exported from the secure environment of the cryptographic service provider (CSP) into an application's data space. Keys that have been exported are stored in encrypted key BLOB structures.
ms.assetid: 859b1bfe-6182-4728-a721-1f34cc98f66f
title: Cryptographic Key Storage and Exchange
ms.topic: article
ms.date: 05/31/2018
---

# Cryptographic Key Storage and Exchange

There are situations where keys must be exported from the secure environment of the [*cryptographic service provider*](../secgloss/c-gly.md) (CSP) into an application's data space. Keys that have been exported are stored in encrypted [*key BLOB*](../secgloss/k-gly.md) structures.

There are two specific situations where it is necessary to export keys:

-   To save a [*session key*](../secgloss/s-gly.md) for later use by an application, if, for example, an application has just encrypted a database file to be decrypted at a later time. The application is responsible for storing the encryption key. This is necessary because CSPs do not preserve [*symmetric keys*](../secgloss/s-gly.md) from session to session.
-   To send a key to someone else. This would be easier if the respective CSPs could communicate directly, but they cannot. Because CSPs cannot communicate, the key has to be exported from one CSP, transmitted to the destination application, and then imported into the destination CSP. This process can become more complicated if the communication path is not trusted.

In either case, an application must store a session key outside the CSP for a period of time. For more information, see [Procedure for Storing a Session Key](procedure-for-storing-a-session-key.md).

 

 
