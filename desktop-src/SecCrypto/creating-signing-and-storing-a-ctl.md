---
Description: 'Create a signed certificate trust list (CTL) and save it to a certificate store.'
ms.assetid: '82d75d60-2343-413c-ba53-ccee02d1ad41'
title: 'Creating, Signing, and Storing a CTL'
---

# Creating, Signing, and Storing a CTL

The following procedures create a signed [*certificate trust list*](security.c_gly#-security-certificate-trust-list-gly) (CTL) and save it to a [*certificate store*](security.c_gly#-security-certificate-store-gly).

**To create and sign a CTL**

1.  Create an array of items to be stored in the [*CTL*](security.c_gly#-security-certificate-trust-list-gly). In the case of trusted certificates, this must be the SHA1 or MD5 hashes of the trusted certificates.
2.  Initialize a [**CTL\_INFO**](ctl-info.md) structure that includes the array of items just created.
3.  Initialize a [**CMSG\_SIGNED\_ENCODE\_INFO**](cmsg-signed-encode-info.md) structure.
4.  Call [**CryptMsgEncodeAndSignCTL**](cryptmsgencodeandsignctl.md). This function call returns a pointer to a signed, encoded CTL (in PKCS \#7 format) that contains the list of items created in step 1.

**To add a CTL to a certificate store**

1.  Get a pointer to a signed and encoded CTL.
2.  Open the target certificate store with a call to [**CertOpenStore**](certopenstore.md).
3.  Call [**CertAddEncodedCTLToStore**](certaddencodedctltostore.md).

 

 



