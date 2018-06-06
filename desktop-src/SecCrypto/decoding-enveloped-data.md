---
Description: General tasks required to decode an enveloped message.
ms.assetid: cb71ea3a-0edd-4d46-8088-a395fab89d2b
title: Decoding Enveloped Data
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Decoding Enveloped Data

The general tasks required to decode an enveloped message are depicted in the following illustration and described in the list that follows it.

![decoding enveloped data](images/decemsg.png)

The sequence of events for decoding enveloped data using key transport key management, as depicted in the previous illustration, is as follows:

-   A pointer to the [*digitally enveloped*](https://msdn.microsoft.com/d007cbb9-b547-4dc7-bc22-b526f650f7c2) message is retrieved.
-   A [*certificate store*](https://msdn.microsoft.com/db46def4-bfdc-4801-a57d-d568e94a2dbb) is opened.
-   From the message, the recipient ID (My ID) is retrieved.
-   The recipient ID is used to retrieve the certificate.
-   The [*private key*](https://msdn.microsoft.com/2fe6cfd3-8a2e-4dbe-9fb8-332633daa97a) associated with that certificate is retrieved.
-   The private key is used to decrypt the [*symmetric*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50) ([*session*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50)) key.
-   The encryption algorithm is retrieved from the message.
-   Using the private key and encryption algorithm, the data is decrypted.

The following procedure uses low-level message functions to accomplish the tasks just listed.

**To decode an enveloped message**

1.  Get a pointer to the encoded BLOB.
2.  Call [**CryptMsgOpenToDecode**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsgopentodecode), passing the necessary arguments.
3.  Call [**CryptMsgUpdate**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsgupdate) once, passing in the handle retrieved in step 2 and a pointer to the data that is to be decoded. This causes the appropriate actions to be taken on the message, depending on the message type.
4.  Call [**CryptMsgGetParam**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsggetparam), passing in the handle retrieved in step 2 and CMSG\_TYPE\_PARAM to verify that the message is of the enveloped data type.
5.  Again call [**CryptMsgGetParam**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsggetparam), passing in CMSG\_INNER\_CONTENT\_TYPE\_PARAM to get the data type of the [*inner content*](https://msdn.microsoft.com/af511aed-88f5-4b12-ad44-317925297f70).
6.  If the inner content data type is **data**, proceed to decrypt and decode the content. Otherwise, run a decoding procedure appropriate for the content data type.
7.  Assuming the inner content type is "data", initialize the [**CMSG\_CTRL\_DECRYPT\_PARA**](/windows/desktop/api/Wincrypt/ns-wincrypt-_cmsg_ctrl_decrypt_para) data structure, and call [**CryptMsgControl**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsgcontrol), passing in CMSG\_CTRL\_DECRYPT and the address of the structure. The content will be decrypted.
8.  Call [**CryptMsgGetParam**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsggetparam), passing in CMSG\_CONTENT\_PARAM to get a pointer to the decoded content data BLOB (**BYTE** string).
9.  Call [**CryptMsgClose**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptmsgclose) to close the message.

The result of this procedure is that the message is decoded and decrypted and a pointer is retrieved to the content data BLOB.

## Related topics

<dl> <dt>

[Example C Program: Encoding an Enveloped, Signed Message](example-c-program-encoding-an-enveloped-signed-message.md)
</dt> </dl>

 

 



