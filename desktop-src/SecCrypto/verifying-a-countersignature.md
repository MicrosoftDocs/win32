---
Description: Explains how to verify a countersignature by using CryptMsgVerifyCountersignatureEncoded.
ms.assetid: b7be0d4c-338f-4319-bd82-5cf3d158d6fe
title: Verifying a Countersignature
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Verifying a Countersignature

**To verify a countersignature**

1.  Call [**CryptMsgOpenToDecode**](/windows/win32/Wincrypt/nf-wincrypt-cryptmsgopentodecode?branch=master) to get a handle to the signed message.
2.  Get a pointer to the countersigner's certificate ( [**CERT\_INFO**](/windows/win32/Wincrypt/ns-wincrypt-_cert_info?branch=master)).
3.  Call [**CryptMsgGetParam**](/windows/win32/Wincrypt/nf-wincrypt-cryptmsggetparam?branch=master) to retrieve the signer information from the message.
4.  Call [**CryptMsgGetParam**](/windows/win32/Wincrypt/nf-wincrypt-cryptmsggetparam?branch=master) to retrieve the [*countersignature*](security.c_gly#-security-countersignature-gly) from the message.
5.  Call [**CryptMsgVerifyCountersignatureEncoded**](/windows/win32/Wincrypt/nf-wincrypt-cryptmsgverifycountersignatureencoded?branch=master) to verify the countersignature.

If the [**CryptMsgVerifyCountersignatureEncoded**](/windows/win32/Wincrypt/nf-wincrypt-cryptmsgverifycountersignatureencoded?branch=master) function call succeeds, the [*countersignature*](security.c_gly#-security-countersignature-gly) is verified.

 

 



