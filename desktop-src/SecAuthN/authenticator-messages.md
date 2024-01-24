---
description: In a simple protocol using secret key authentication, a client presents an authenticator message in the form of a piece of information encrypted in the session key.
ms.assetid: 984c84db-96d5-479e-8917-25a0270b3b59
title: Authenticator Messages
ms.topic: article
ms.date: 05/31/2018
---

# Authenticator Messages

In a simple protocol using secret key authentication, a client presents an authenticator message in the form of a piece of information encrypted in the [*session key*](/windows/desktop/SecGloss/s-gly). The information in the authenticator message must be different each time the authentication protocol is executed, or an encrypted authenticator message could be reused by an unauthorized entity.

On receiving the authenticator message, the server decrypts it and can tell from the contents of the decrypted message whether decryption was successful. If the decrypted message is not gibberish, the server knows that the client presenting the authenticator message used the correct key to encrypt the message. Only two entities have access to the [*session key*](/windows/desktop/SecGloss/s-gly) and if the server is one of those, the client who encrypted the authenticator message must be the other.

For mutual authentication, a similar protocol is executed. The server extracts part of the information from the decrypted, original authenticator message, encrypts it with the shared session key, and sends the encrypted message to the client. The client decrypts the message and compares the result with the original. If the decrypted message matches the correct part of the original message, the client knows that the server was able to decrypt the original message with the shared secret session key and was able to re-encrypt a portion of that message with that same shared secret [*session key*](/windows/desktop/SecGloss/s-gly).

 

 
