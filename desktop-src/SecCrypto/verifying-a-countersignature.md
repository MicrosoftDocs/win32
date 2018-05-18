---
Description: 'Explains how to verify a countersignature by using CryptMsgVerifyCountersignatureEncoded.'
ms.assetid: 'b7be0d4c-338f-4319-bd82-5cf3d158d6fe'
title: Verifying a Countersignature
---

# Verifying a Countersignature

**To verify a countersignature**

1.  Call [**CryptMsgOpenToDecode**](cryptmsgopentodecode.md) to get a handle to the signed message.
2.  Get a pointer to the countersigner's certificate ( [**CERT\_INFO**](cert-info.md)).
3.  Call [**CryptMsgGetParam**](cryptmsggetparam.md) to retrieve the signer information from the message.
4.  Call [**CryptMsgGetParam**](cryptmsggetparam.md) to retrieve the [*countersignature*](security.c_gly#-security-countersignature-gly) from the message.
5.  Call [**CryptMsgVerifyCountersignatureEncoded**](cryptmsgverifycountersignatureencoded.md) to verify the countersignature.

If the [**CryptMsgVerifyCountersignatureEncoded**](cryptmsgverifycountersignatureencoded.md) function call succeeds, the [*countersignature*](security.c_gly#-security-countersignature-gly) is verified.

 

 



