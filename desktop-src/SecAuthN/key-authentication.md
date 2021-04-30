---
description: Many forms of authentication are based on the idea that an entity can prove its identity if it can prove it knows a key, such as a password, that only it can know.
ms.assetid: e17e4eb7-133e-46a0-8247-00a58b88bf61
title: Key Authentication
ms.topic: article
ms.date: 05/31/2018
---

# Key Authentication

Many forms of authentication are based on the idea that an entity can prove its identity if it can prove it knows a key, such as a password, that only it can know.

Authentication techniques that rely on a secret, such as a password, need to have a way to keep the secret from becoming public knowledge. A password owner cannot walk up to a door and give the password. Someone besides the doorkeeper might be listening; or it might be the wrong door. In order to keep a secret, there must be a way to prove a user knows the password without revealing the password. That is the idea behind secret key authentication, a method of verification used throughout the [*Kerberos protocol*](../secgloss/k-gly.md).

Notice that the "secret" in secret key authentication is that the authentication process takes place "in secret;" that is, without ever actually revealing the content of the key.

For secret key authentication to work, the two parties to a transaction must share a cryptographic [*session key*](../secgloss/s-gly.md) which is also secret, known only to them and to no others. The key is [*symmetric*](../secgloss/s-gly.md); that is, it is a single key used for both encryption and decryption. One party in the authentication process proves its knowledge of the key by encrypting a message. The other party proves its knowledge of the key by decrypting the message.

 

 
