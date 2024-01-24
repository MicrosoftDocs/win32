---
description: To sign a file and create a catalog for it, you must first have a process for signing files, a certificate, and a public key.
ms.assetid: 61337ea6-2d6b-4080-9128-5b8527512ce6
title: Creating Signed Files and Catalogs
ms.topic: article
ms.date: 05/31/2018
---

# Creating Signed Files and Catalogs

To sign a file and create a catalog for it, you must first have a process for signing files, a certificate, and a public key.

**To sign a file and a create a catalog**

1.  Use [Pktextract.exe](pktextract-exe.md) to extract the [*public key token*](p-sbscs-gly.md) from the certificate file. The certificate file must be present in the same directory as the utility.
2.  Use the public key token value to update the **publicKeyToken** attribute of the **assemblyIdentity** element in the manifest file.
3.  Use [MT.exe](mt-exe.md) to generate hashes of files contained in the assembly manifest and to create the catalog description file (.cdf).
4.  Use Makecat.exe with the generated .cdf to create the security catalog for the assembly. This tool is included in the CryptoAPI.
5.  Use the [SignTool](/windows/desktop/SecCrypto/signtool) utility to sign the catalog generated with the certificate used in step 1. The .cdf from steps 3 and 4 can be deleted once the catalog is created.

See also, [Assembly Signing Example](assembly-signing-example.md).

 

 
