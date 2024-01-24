---
description: Use CertMgr to view certificates, CRLs, and CTLs from a file or a certificate store, to copy certificates into a certificate store, to delete certificates from a certificate store, and to save certificates to files.
ms.assetid: cc2424bf-e7ea-4484-9934-3aba02b63492
title: Using CertMgr
ms.topic: article
ms.date: 05/31/2018
---

# Using CertMgr

[CertMgr](certmgr.md) can be used to view [*certificates*](../secgloss/c-gly.md), [*certificate revocation lists*](../secgloss/c-gly.md) (CRLs), and [*certificate trust lists*](../secgloss/c-gly.md) (CTLs) from a file or a certificate store, to copy certificates into a [*certificate store*](../secgloss/c-gly.md), to delete certificates from a certificate store, and to save certificates to files.

When [CertMgr](certmgr.md) is used without options, a CertMgr wizard appears to guide the user through the operation.

The file must be one of the following types:

-   An encoded CTL, CRL, or certificate file (could be base-64 encoded)
-   A PKCS \#7 file
-   An SPC file
-   A signed document
-   A serialized storeFile

The following examples use [CertMgr](certmgr.md) commands to perform common certificate tasks.

-   View the certificates, CRLs, and CTLs from *MyFile.ext*.

    **certmgr** *MyFile.ext*

-   View the certificates, CRLs, and CTLs from the MY system store.

    **certmgr -s my**

-   Copy all the certificates, CRLs, and CTLs in a file named *MyFile.ext* to a new file, called *NewFile.ext*.

    **certmgr -add -all -c** *MyFile.ext* *NewFile.ext*

-   Copy all the certificates, CRLs, and CTLs from the MY system store to a file called *NewMyFile.ext*.

    **certmgr -add -all -c -s my** *NewMyFile.ext*

-   Copy a certificate with the common name *MyCert* in the MY system store to a file called *NewCert.cer*.

    **certmgr -add -c -n** *MyCert* **-s my** *NewCert.cer*

-   Delete all the certificates from the MY system store.

    **certmgr -del -all -c -s my**

-   Delete all the CTLs from the MY system store and save the resulting store to a file called *NewStore.str*.

    **certmgr -del -all -ctl -s my** *NewStore.str*

-   Save, to a file called *NewCert.cer*, a certificate that is an [*X.509*](../secgloss/x-gly.md) encoded certificate, that has the common name *MyCert*, and that is located in the Root certificate store.

    **certmgr -put -c -n** *MyCert* **-s root** *NewCert.cer*

## Related topics

<dl> <dt>

[CertMgr](certmgr.md)
</dt> </dl>

 

 
