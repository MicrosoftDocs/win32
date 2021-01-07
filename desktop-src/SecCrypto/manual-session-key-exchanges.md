---
description: Shows how to send an encrypted message.
ms.assetid: 928b1863-7a54-4bf0-b447-85b8c2868bcd
title: Manual Session Key Exchanges
ms.topic: article
ms.date: 05/31/2018
---

# Manual Session Key Exchanges

> [!Note]  
> The procedure described in this section assumes that the users (or CryptoAPI clients) already possess their own set of [*public/private key pairs*](../secgloss/p-gly.md) and have also obtained each other's [*public keys*](../secgloss/p-gly.md).

 

The following illustration shows how to use this procedure to send an encrypted message.

![sending an encrypted message](images/capi04.png)

This approach is vulnerable to at least one common form of attack. An eavesdropper can acquire copies of one or more encrypted messages and the encrypted keys. Then, at some later time, the eavesdropper can send one of these messages to the receiver and the receiver will have no way of knowing the message did not come directly from the original sender. This risk can be reduced by time-stamping all messages or by using serial numbers.

The easiest way to send encrypted messages to another user is to send the message encrypted with a random session key along with the session key encrypted with the receiver's [*key exchange public key*](../secgloss/k-gly.md).

Following are the steps for sending an encrypted session key.

**To send an encrypted session key**

1.  Create a random [*session key*](../secgloss/s-gly.md) by using the [**CryptGenKey**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptgenkey) function.
2.  Encrypt the message by using the session key. This procedure is discussed in [Data Encryption and Decryption](data-encryption-and-decryption.md).
3.  Export the session key into a [*key BLOB*](../secgloss/k-gly.md) with the [**CryptExportKey**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptexportkey) function, specifying that the key be encrypted with the destination user's key exchange public key.
4.  Send both the encrypted message and the encrypted key BLOB to the destination user.
5.  The destination user imports the key BLOB into his or her CSP by using the [**CryptImportKey**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptimportkey) function. This will automatically decrypt the session key, provided the destination user's key exchange public key was specified in step 3.
6.  The destination user can then decrypt the message by using the session key, following the procedure discussed in [Data Encryption and Decryption](data-encryption-and-decryption.md).

 

 
