---
Description: Explains how to countersign a message by using CryptMsgCountersign.
ms.assetid: e1969b43-f50e-4c7d-a7e5-b22db4e05be2
title: Countersigning a Message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Countersigning a Message

**To countersign a signed message by using CryptMsgCountersign**

1.  Call [**CryptMsgOpenToDecode**](/windows/win32/Wincrypt/nf-wincrypt-cryptmsgopentodecode?branch=master) to get a handle to the signed message.
2.  Initialize a [**CMSG\_SIGNER\_ENCODE\_INFO**](/windows/win32/Wincrypt/ns-wincrypt-_cmsg_signer_encode_info?branch=master) structure for the countersigner.
3.  Add the [**CMSG\_SIGNER\_ENCODE\_INFO**](/windows/win32/Wincrypt/ns-wincrypt-_cmsg_signer_encode_info?branch=master) structure to an array of countersigners (only one countersigner is currently supported).
4.  Call [**CryptMsgCountersign**](/windows/win32/Wincrypt/nf-wincrypt-cryptmsgcountersign?branch=master) to add the countersignature or countersignatures.

If all of the function calls succeed, the original message now has a [*countersignature*](security.c_gly#-security-countersignature-gly) included as an unauthenticated attribute.

**To countersign a signed message by using CryptMsgCountersignEncoded**

1.  Call [**CryptMsgOpenToDecode**](/windows/win32/Wincrypt/nf-wincrypt-cryptmsgopentodecode?branch=master) to get a handle to the signed message.
2.  Call [**CryptMsgGetParam**](/windows/win32/Wincrypt/nf-wincrypt-cryptmsggetparam?branch=master) to retrieve the encoded signer information of the signed message.
3.  Initialize a [**CMSG\_SIGNER\_ENCODE\_INFO**](/windows/win32/Wincrypt/ns-wincrypt-_cmsg_signer_encode_info?branch=master) structure for the countersigner.
4.  Add the [**CMSG\_SIGNER\_ENCODE\_INFO**](/windows/win32/Wincrypt/ns-wincrypt-_cmsg_signer_encode_info?branch=master) structure to an array of countersigners (only one countersigner is currently supported).
5.  Call [**CryptMsgCountersignEncoded**](/windows/win32/Wincrypt/nf-wincrypt-cryptmsgcountersignencoded?branch=master) to create the encoded countersignature attribute.
6.  Call [**CryptMsgControl**](/windows/win32/Wincrypt/nf-wincrypt-cryptmsgcontrol?branch=master) to add the countersignature attribute to the original message as an unauthenticated attribute.

If all of the function calls succeed, a [*countersignature*](security.c_gly#-security-countersignature-gly) attribute is added to the original message.

 

 



