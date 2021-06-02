---
description: Details the procedure for encoding a general message.
ms.assetid: 554cab0d-cfa2-46a7-80d9-f41430eb4b47
title: Procedure for Encoding and Decoding Messages
ms.topic: article
ms.date: 05/31/2018
---

# Procedure for Encoding and Decoding Messages

The procedure for encoding a general message is as follows.

**To encode a message**

1.  Initialize the appropriate data structures for the desired data type.
2.  Call [**CryptMsgOpenToEncode**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsgopentoencode), passing the necessary arguments. When calling **CryptMsgOpenToEncode**, if the data that is to be provided to [**CryptMsgUpdate**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsgupdate) has already been message-encoded, pass the appropriate object identifier in *pszInnerContentObjID* (for example, "1.2.840.113549.1.7.2" for szOID\_RSA\_signedData). If *pszInnerContentObjID* is **NULL**, the [*inner content*](../secgloss/i-gly.md) type is assumed not to have been previously encoded and is processed appropriately.
3.  Call [**CryptMsgUpdate**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsgupdate) as many times as necessary to complete the message. On the last call, set the *fFinal* parameter to **TRUE**. (For details, see **CryptMsgUpdate**).
4.  Call [**CryptMsgGetParam**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsggetparam) to get a pointer to the desired parameters, such as the content. For encoding simple, general data, use CMSG\_CONTENT\_PARAM for the *dwParamtype*.
5.  Close the message by calling [**CryptMsgClose**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsgclose).

This procedure results in an encoded message of a type specified in the function calls.

The procedure for decoding a general message is as follows.

**To decode a message**

1.  Determine the length needed for the buffer to hold the encoded data using [**CryptMsgCalculateEncodedLength**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsgcalculateencodedlength).
2.  Call [**CryptMsgOpenToDecode**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsgopentodecode), passing the necessary arguments. To maintain compatibility with Internet Explorer version 3.0, the *dwMsgType* parameter is provided. Signed data created in Internet Explorer 3.0 does not contain header information. Therefore, if such a message is extracted from file signatures, the message type must be passed into the function. If zero is passed into the *dwMsgType* parameter, the function will read the message type from the header on the message. If the header is missing, the function call will fail. If successful, a handle to the opened message is returned.
3.  Call [**CryptMsgUpdate**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsgupdate) once. This causes the appropriate actions to be taken on the message, depending on the message type.
4.  For additional processing of the message, such as additional decryption or signature verification, call [**CryptMsgControl**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsgcontrol), passing the desired action in *dwCtrlType*.
5.  Call [**CryptMsgGetParam**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsggetparam) to get a pointer to the desired parameters, such as the content. To decode simple general data, use CMSG\_CONTENT\_PARAM for the *dwParamtype* parameter.
6.  Call [**CryptMsgClose**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsgclose) to close the message.

For an example that implements these steps, see [Example C Program: Encoding and Decoding Data](example-c-program-encoding-and-decoding-data.md). For procedures and an example demonstrating the process of encoding, decoding, and verifying the signature of a signed message, see [Example C Program: Signing, Encoding, Decoding, and Verifying a Message](example-c-program-signing-encoding-decoding-and-verifying-a-message.md).

 

 
