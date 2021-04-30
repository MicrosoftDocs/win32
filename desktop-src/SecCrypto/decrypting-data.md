---
description: Presents the steps to decrypt an encrypted message.
ms.assetid: 6af7dd28-325e-431a-9cdb-109d93af6302
title: Decrypting Data
ms.topic: article
ms.date: 05/31/2018
---

# Decrypting Data

This section presents the steps to decrypt an encrypted message.

**To decrypt an encrypted message**

1.  Get a pointer to the digitally enveloped message.
2.  Open a certificate store.
3.  From the message, retrieve the recipient identifier (My ID).
4.  Use the recipient identifier to retrieve the certificate.
5.  Get the private key for the certificate.
6.  Use the private key to decrypt the symmetric (session) key.
7.  Retrieve the encryption algorithm from the message.
8.  Using the decrypted session key and the encryption algorithm, decrypt the data.

[**CryptDecryptMessage**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptdecryptmessage) does all of the tasks for decrypting a message; however, initialization of structures and other data is still necessary.

**To decrypt data using CryptDecryptMessage**

1.  Get a pointer to the encrypted BLOB.
2.  Open a certificate store.
3.  Create a certificate store array.
4.  Initialize the [**CRYPT\_DECRYPT\_MESSAGE\_PARA**](/windows/desktop/api/Wincrypt/ns-wincrypt-crypt_decrypt_message_para) structure.
5.  Call [**CryptDecryptMessage**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptdecryptmessage) to decrypt the data contained in the message.

[Example C Program: Using CryptEncryptMessage and CryptDecryptMessage](example-c-program-using-cryptencryptmessage-and-cryptdecryptmessage.md) implements the procedure just presented. Comments show which code elements accomplish each step in the procedure. For details about the function, see [**CryptDecryptMessage**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptdecryptmessage), and for details about the data structure, see [**CRYPT\_DECRYPT\_MESSAGE\_PARA**](/windows/desktop/api/Wincrypt/ns-wincrypt-crypt_decrypt_message_para).

 

 



