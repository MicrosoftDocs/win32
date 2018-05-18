---
Description: 'Process to decode signed data.'
ms.assetid: '803220d0-7963-4fc4-8451-a979e54a9cc3'
title: Decoding Signed Data
---

# Decoding Signed Data

The following general process decodes a [*signed data*](security.s_gly#-security-signed-data-gly) type.

**To decode a signed message**

1.  Get a pointer to the encoded BLOB.
2.  Call [**CryptMsgOpenToDecode**](cryptmsgopentodecode.md), passing the necessary arguments.
3.  Call [**CryptMsgUpdate**](cryptmsgupdate.md) once, passing in the handle retrieved in step 2 and a pointer to the data that is to be decoded. This causes the appropriate actions to be taken on the message, depending on the message type.
4.  Call [**CryptMsgGetParam**](cryptmsggetparam.md), passing in the handle retrieved in step 2 and the appropriate parameter types to access the decoded data. For example, pass in CMSG\_CONTENT\_PARAM to get a pointer to the decoded content.

The following general process verifies the signature of a decoded, signed message.

**To verify the signature of a decoded, signed message**

1.  Call [**CryptMsgGetParam**](cryptmsggetparam.md), passing in the message handle and CMSG\_SIGNER\_CERT\_INFO\_PARAM to get the signer's [**CERT\_INFO**](cert-info.md) from the message.
2.  Call [**CertOpenStore**](certopenstore.md) to open a temporary store that is initialized with the certificates from the message.
3.  Call [**CertGetSubjectCertificateFromStore**](certgetsubjectcertificatefromstore.md) to get the signer's [**CERT\_INFO**](cert-info.md) from the certificates included in the message.
4.  Call [**CryptMsgControl**](cryptmsgcontrol.md), passing in CMSG\_CTRL\_VERIFY\_SIGNATURE to verify the signatures.
5.  Call [**CryptMsgClose**](cryptmsgclose.md) to close the message.

The result of these procedures is that the signature is verified and a pointer is retrieved to the decoded message content obtained in step 4 of the procedure for decoding a signed message.

For C coding details, see [Example C Program: Signing, Encoding, Decoding, and Verifying a Message](example-c-program-signing-encoding-decoding-and-verifying-a-message.md).

 

 



