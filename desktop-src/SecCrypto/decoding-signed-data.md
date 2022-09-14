---
description: Process to decode signed data.
ms.assetid: 803220d0-7963-4fc4-8451-a979e54a9cc3
title: Decoding Signed Data
ms.topic: article
ms.date: 05/31/2018
---

# Decoding Signed Data

The following general process decodes a [*signed data*](../secgloss/s-gly.md) type.

**To decode a signed message**

1.  Get a pointer to the encoded BLOB.
2.  Call [**CryptMsgOpenToDecode**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsgopentodecode), passing the necessary arguments.
3.  Call [**CryptMsgUpdate**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsgupdate) once, passing in the handle retrieved in step 2 and a pointer to the data that is to be decoded. This causes the appropriate actions to be taken on the message, depending on the message type.
4.  Call [**CryptMsgGetParam**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsggetparam), passing in the handle retrieved in step 2 and the appropriate parameter types to access the decoded data. For example, pass in CMSG\_CONTENT\_PARAM to get a pointer to the decoded content.

The following general process verifies the signature of a decoded, signed message.

**To verify the signature of a decoded, signed message**

1.  Call [**CryptMsgGetParam**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsggetparam), passing in the message handle and CMSG\_SIGNER\_CERT\_INFO\_PARAM to get the signer's [**CERT\_INFO**](/windows/desktop/api/Wincrypt/ns-wincrypt-cert_info) from the message.
2.  Call [**CertOpenStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certopenstore) to open a temporary store that is initialized with the certificates from the message.
3.  Call [**CertGetSubjectCertificateFromStore**](/windows/desktop/api/Wincrypt/nf-wincrypt-certgetsubjectcertificatefromstore) to get the signer's [**CERT\_INFO**](/windows/desktop/api/Wincrypt/ns-wincrypt-cert_info) from the certificates included in the message.
4.  Call [**CryptMsgControl**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsgcontrol), passing in CMSG\_CTRL\_VERIFY\_SIGNATURE to verify the signatures.
5.  Call [**CryptMsgClose**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsgclose) to close the message.

The result of these procedures is that the signature is verified and a pointer is retrieved to the decoded message content obtained in step 4 of the procedure for decoding a signed message.

For C coding details, see [Example C Program: Signing, Encoding, Decoding, and Verifying a Message](example-c-program-signing-encoding-decoding-and-verifying-a-message.md).

 

 
