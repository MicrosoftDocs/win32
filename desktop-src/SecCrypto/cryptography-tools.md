---
description: Cryptography tools provide command-line tools for code signing, signature verification, and other cryptography tasks.
ms.assetid: 21adbcfb-fadd-4818-9dc5-23bfd526b525
title: Cryptography Tools
ms.topic: article
ms.date: 05/31/2018
---

# Cryptography Tools

Cryptography tools provide command-line tools for code signing, signature verification, and other cryptography tasks.

## Introduction to Code Signing

The software industry must provide users with the means to trust code including code published on the Internet. Many webpages contain only static information that can be downloaded with little risk. Some pages, however, contain controls and applications to be downloaded and run on a user's computer. These executable files can be risky to download and run.

Packaged software uses branding and trusted sales outlets to assure users of its integrity, but these guarantees are not available when code is transmitted on the Internet. Additionally, the Internet itself cannot provide any guarantee about the identity of the software creator. Nor can it guarantee that any software downloaded was not altered after its creation. Browsers can exhibit a warning message that explains the possible dangers of downloading data of any kind, but browsers cannot verify that code is what it claims to be. A more active approach must be taken to make the Internet a reliable medium for distributing software.

One approach to providing guarantees of the authenticity and [*integrity*](../secgloss/i-gly.md) of files is attaching [*digital signatures*](../secgloss/d-gly.md) to those files. A digital signature attached to a file positively identifies the distributor of that file and ensures that the contents of the file were not changed after the signature was created.

Digital signatures can be created and verified by using Microsoft's cryptography APIs. For background information on cryptography and the [*CryptoAPI*](../secgloss/c-gly.md) functions, see [Cryptography Essentials](cryptography-essentials.md).

For detailed information on [*digital signatures*](../secgloss/d-gly.md), [*certificates*](../secgloss/c-gly.md), and [*certificate stores*](../secgloss/c-gly.md), see the following topics:

-   [Hashes and Digital Signatures](hashes-and-digital-signatures.md)
-   [Digital Certificates](digital-certificates.md)
-   [Managing Certificates with Certificate Stores](managing-certificates-with-certificate-stores.md)
-   [Certificate Trust Verification](certificate-trust-verification.md)

Currently, CryptoAPI Tools supports Microsoft Authenticode technology by allowing software vendors to sign the following types of files for Authenticode verification.



| File name extension                             | Contents                                                                                                                                                                                                                              |
|-------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| .appx<br/>                                | Installer files for a Windows Store device app.<br/>                                                                                                                                                                            |
| .cab<br/>                                 | Self-contained files used for application installation and setup. In a cabinet file, multiple files are compressed into one file. They are commonly found on Microsoft software distribution disks.<br/>                        |
| .cat<br/>                                 | Files that contain digital [*thumbprints*](../secgloss/t-gly.md) of several files. A .cat file can be used to ensure the integrity of the files whose thumbprints it includes.<br/> |
| .dll<br/>                                 | Files that contain executable functions.<br/>                                                                                                                                                                                   |
| .exe<br/>                                 | Files that contain executable programs.<br/>                                                                                                                                                                                    |
| .js<br/> .vbs<br/> .wsf<br/>  | Windows shell files for JScript or Microsoft Visual Basic Scripting Edition (VBScript).<br/>                                                                                                                                    |
| .msi<br/> .msp<br/> .mst<br/> | Windows installer files.<br/>                                                                                                                                                                                                   |
| .ocx<br/>                                 | Files that contain Microsoft ActiveX controls.<br/>                                                                                                                                                                             |
| .ps1<br/>                                 | Files that contain PowerShell scripts.<br/>                                                                                                                                                                                     |
| .stl<br/>                                 | Files that contain a [*certificate trust list*](../secgloss/c-gly.md) (CTL).<br/>                                                                           |
| .sys<br/>                                 | Files that contain driver binaries.<br/>                                                                                                                                                                                        |



 

For information about digital signing, see the following documents:

-   CCITT, Recommendation X.509, *The Directory-Authentication Framework*, Consultation Committee, International Telephone and Telegraph, International Telecommunications Union, Geneva, 1989.
-   RSA Laboratories, *PKCS \#7: Cryptographic Message Syntax Standard*. Version 1.5, November, 1993.
-   Schneier, Bruce, *Applied Cryptography*, 2d ed. New York: John Wiley & Sons, 1996.
-   [https://www.rsa.com](https://www.rsa.com/)

> [!Note]  
> These resources may not be available in some languages and countries or regions.

 

## Microsoft Cryptography Tools

The publishing tools and the signing DLL are installed in the \\Bin directory of your Microsoft SDK installation. They include the following files.



| File name                    | Remarks                                                                                                                                                                                             |
|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Cert2SPC.exe](cert2spc.md) | Creates an [*Software Publisher Certificate*](../secgloss/s-gly.md) (SPC) for testing purposes only.<br/> |
| [CertMgr.exe](certmgr.md)   | Manages certificates, CTLs, and [*certificate revocation lists*](../secgloss/c-gly.md) (CRLs).<br/>             |
| [MakeCat.exe](makecat.md)   | Creates an unsigned catalog file that contains the hashes of a set of files along with associated attributes of each file.<br/>                                                               |
| [MakeCert.exe](makecert.md) | Creates an [*X.509*](../secgloss/x-gly.md) certificate for testing purposes only.<br/>                                                                      |
| Pvk2pfx.exe                  | Converts a software publisher certificate file (.spc) or a private key file (.pvk) to Personal Information Exchange (PFX) file format.<br/>                                                   |
| [SetReg.exe](setreg.md)     | Sets registry keys that control certificate verification.<br/>                                                                                                                                |
| [SignTool.exe](signtool.md) | Signs and time stamps a file. Additionally, checks the signature of a file.<br/>                                                                                                              |



 

 

 
