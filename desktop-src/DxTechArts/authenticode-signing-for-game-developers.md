---
title: Authenticode Signing for Game Developers
description: This article discusses how to get started with authenticating your game and how to integrate authentication into a daily build process.
ms.assetid: 0b3138ea-e4ea-57fb-756b-62fdc20cf813
ms.topic: article
ms.date: 05/31/2018
---

# Authenticode Signing for Game Developers

Data authentication is increasingly important for game developers. Windows Vista and Windows 7 have a number of features, such as parental controls, that require games to be properly signed to ensure that no one has tampered with the data. Microsoft Authenticode enables end users and the operating system to verify that program code comes from the rightful owner and that it hasn't been maliciously altered or accidentally corrupted. This article discusses how to get started with authenticating your game and how to integrate authentication into a daily build process.

-   [Background](#background)
-   [Getting Started](#getting-started)
-   [Using a Trusted Certificate Authority](#using-a-trusted-certificate-authority)
-   [Example Using a Test Certificate](#example-using-a-test-certificate)
-   [Integrating Code Signing into the Daily Build System](#integrating-code-signing-into-the-daily-build-system)
-   [Revocation](#revocation)
-   [Code-Signing Drivers](#code-signing-drivers)
-   [Summary](#summary)
-   [More information](#more-information)

> [!Note]  
> As of January 1, 2016, Windows 7 and later no longer trust any SHA-1 code signing certificate with an expiration date of January 1, 2016 or later. See [Windows Enforcement of Authenticode Code Signing and Timestamping](https://social.technet.microsoft.com/wiki/contents/articles/32288.windows-enforcement-of-sha1-certificates.aspx) for more information.

 

## Background

Digital certificates are used to establish the identity of the author. Digital certificates are issued by a trusted third party known as a Certificate Authority (CA) such as VeriSign or Thawte. The CA is responsible for verifying that owner is not claiming a false identify. After applying to a CA for a certificate, commercial developers can expect a response to their application in less than two weeks.

After the CA decides that you meet its policy criteria, it generates a code-signing certificate that conforms to X.509, the industry-standard certificate format created by the International Telecommunications Union, with Version 3 extensions. This certificate identifies you and contains your public key. It is stored by the CA for reference, and a copy is given to you electronically. At the same time, you also create a private, key which you must keep safe and which you must not share with anyone, even the CA.

After you have a public and private key, you can then begin distributing signed software. Microsoft provides tools to do this in the Windows SDK. The tools utilize a one-way hash, produce a fixed-length digest, and generate an encrypted signature with a private key. They then combine that encrypted signature with your certificate and credentials into a structure known as a signature block and embed it into the file format of the executable. Any type of executable binary file can be signed, including DLLs, executable files, and cabinet files.

The signature can be verified in multiple ways. Programs can call the CertVerifyCertificateChainPolicy function, and SignTool (signtool.exe) can be used to verify a signature from the command-line prompt. Windows Explorer also has a Digital Signatures tab in File Properties that displays each certificate of a signed binary file. (The Digital Signatures tab only appears in File Properties for signed files.) Also, an application can be self-verifying by use of [**CertVerifyCertificateChainPolicy**](/windows/desktop/api/wincrypt/nf-wincrypt-certverifycertificatechainpolicy).

Authenticode signing is not only useful for data authentication by end users, but is also needed for patching of Limited User Accounts and by parental controls in Windows Vista and Windows 7. In addition, future technologies in Windows operating systems may also require that code is signed, so it is strongly advised that all professional and amateur developers acquire a code-signing certificate from a CA. More information on how this is done can be found later in this article in [Using a Trusted Certificate Authority](#using-a-trusted-certificate-authority).

Game code, patchers, and installers can further leverage Authenticode signing by verifying files are authentic in code. This can be used for anti-cheat and general network security. Example code for checking if a file is signed can be found here: [Example C Program: Verifying the Signature of a PE File](/windows/desktop/SecCrypto/example-c-program--verifying-the-signature-of-a-pe-file), and example code for checking ownership of a signing certificate on a signed file can be found here: [How To Get Information from Authenticode Signed Executables](https://support.microsoft.com/kb/323809).

## Getting Started

To get started, Microsoft provides tools with Visual Studio 2005 and Visual Studio 2008, and in the [Windows SDK](https://msdn.microsoft.com/windowsserver/bb980924.aspx), to help perform and verify the code-signing process. After installing Visual Studio or the Windows SDK, the tools described in this technical article are located in a subdirectory of the installation, which may include one or more of the following:

-   %SystemDrive%\\Program Files\\Microsoft Visual Studio 8\\SDK\\v2.0\\Bin
-   %SystemDrive%\\Program Files\\Microsoft Visual Studio 8\\VC\\PlatformSDK\\Bin
-   %SystemDrive%\\Program Files\\Microsoft Visual Studio 9.0\\SmartDevices\\SDK\\SDKTools\\
-   %SystemDrive%\\Program Files\\Microsoft SDKs\\Windows\\v6.0A\\bin\\

The following tools are the most useful for signing code:

<dl> <dt>

<span id="Certificate_Creation_Tool__MakeCert.exe_"></span><span id="certificate_creation_tool__makecert.exe_"></span><span id="CERTIFICATE_CREATION_TOOL__MAKECERT.EXE_"></span>Certificate Creation Tool (MakeCert.exe)
</dt> <dd>

Generates a test X.509 certificate, as a .cer file, that contains your public key and a private key, as a .pvk file. This certificate is only for internal testing purposes and can't be used publicly.

</dd> <dt>

<span id="pvk2pfx.exe"></span><span id="PVK2PFX.EXE"></span>pvk2pfx.exe
</dt> <dd>

Creates a Personal Information Exchange (.pfx) file from a pair of .cer and .pvk files. The .pfx file contains both your public and private key.

</dd> <dt>

<span id="SignTool__SignTool.exe_"></span><span id="signtool__signtool.exe_"></span><span id="SIGNTOOL__SIGNTOOL.EXE_"></span>SignTool (SignTool.exe)
</dt> <dd>

Signs file by using the .pfx file. SignTool supports the signing of DLL files, executable files, Windows Installer (.msi) files, and cabinet (.cab) files.

</dd> </dl>

> [!Note]  
> While reading other documentation, you might find references to SignCode (SignCode.exe), but this tool is deprecated and is no longer supported—use SignTool instead.

 

## Using a Trusted Certificate Authority

To obtain a trusted certificate, you must apply to a Certificate Authority (CA), such as VeriSign or Thawte. Microsoft doesn't recommend any CA over another, but if you want to integrate into the Windows Error Reporting (WER) service, you should consider using VeriSign to issue the certificate, because accessing the WER database requires a WinQual account which requires a VeriSign ID. For a complete list of trusted third-party certificate authorities, see [Microsoft Root Certificate Program Members](/previous-versions/ms995347(v=msdn.10)). For more information about registering with WER, see "[Introducing Windows Error Reporting](https://msdn.microsoft.com/)" in [ISV Zone](https://msdn.microsoft.com/).

After you receive your certificate from the CA, you can sign your program by using SignTool and release your program to the public. However, you must be careful to protect your private key, which is contained in your .pfx and .pvk files. Be sure to keep these files in a secure location.

## Example Using a Test Certificate

The following steps demonstrate the creation of a code-signing certificate for testing purposes, followed by the signing of a Direct3D sample program (called BasicHLSL.exe) with this test certificate. This procedure creates .cer and .pvk files—your public and private keys, respectively — which cannot be used for public certification.

In this example, a time stamp is also added to the signature. A time stamp prevents the signature from becoming invalid when the certificate expires. Code that is signed but lacking a time stamp will not validate after the certificate expires. Therefore, all publicly released code should have a time stamp.

**To create a certificate and sign a program**

1.  Create a test certificate and private key by using the Certificate Creation Tool (MakeCert.exe).

    The following command-line example specifies MyPrivateKey as the file name for the private key (.pvk) file, MyPublicKey as the file name for the certificate (.cer) file, and MySoftwareCompany as the name of the certificate. It also makes the certificate self-signed, so that it does not have an untrusted root authority.

    ```
    MakeCert /n CN=MySoftwareCompany /r /h 0 /eku "1.3.6.1.5.5.7.3.3,1.3.6.1.4.1.311.10.3.13" /e 12-31-2020 /sv MyPrivateKey.pvk MyPublicKey.cer
    ```

    

2.  Create a Personal Information Exchange (.pfx) file from your private key (.pvk) file and certificate (.cer) file by using pvk2pfx.exe.

    The .pfx file combines your public and private keys into a single file. The following command-line example uses the .pvk and .cer files from the previous step to create the .pfx file named MyPFX with the password your\_password:

    ```
    pvk2pfx.exe -pvk MyPrivateKey.pvk -spc MyPublicKey.cer -pfx MyPFX.pfx -po your_password
    ```

    

3.  Sign your program with your Personal Information Exchange (.pfx) file by using SignTool.

    You can specify several options on the command line. The following command-line example uses the .pfx file from the previous step, gives your\_password as the password, specifies BasicHLSL as the file to be signed, and retrieves a time stamp from a specified server:

    ```
    signtool.exe sign /fd SHA256 /f MyPFX.pfx /p your_password /v /t URL_to_time_stamp_service BasicHLSL.exe
    ```

    

    > [!Note]  
    > The URL to the time stamp service is provided by the CA, and is optional for testing. It is important for production signing to include a valid time stamp authority, or the signature will fail to validate when the certificate expires.

     

4.  Verify that the program is signed by using SignTool.

    The following command-line example specifies that SignTool should attempt to verify the signature on BasicHLSL.exe by using all available methods while providing verbose output:

    ```
    signtool.exe verify /a /v BasicHLSL.exe
    ```

    

    In this example, SignTool should indicate that the certificate is attached, while also stating that it is not trusted, since it is not issued by a CA.

5.  Trust the test certificate.

    For test certificates you need to trust the certificate. This step should be skipped for certificates provided by a CA since those will trusted by default.

    On only the computers where you want to trust the test certificate, run the following:

    ```
    certmgr.msc
    ```

    

    Then right click on Trusted Root Certification Authorities and choose All Tasks \| Import. Then browse to the .pfx file you created and follow the wizard steps, placing the certificate in the Trusted Root Certification Authorities.

    When the wizard completes, you can start testing with the trusted certificate on that computer.

## Integrating Code Signing into the Daily Build System

To integrate code signing into a project, you can create a batch file or script to run the command line tools. After the project is built, run SignTool with the proper settings (as shown in step 3 of our example).

Be especially cautious in your build process to insure that access to the .pfx and .pvk files is restricted to as few computers and users as possible. As a best practice, developers should only sign code by using the test certificate until they are ready to ship. Again, the private key (.pvk) should be kept in a secured location, like a safe or locked room, and ideally on a cryptographic device, like a smart card.

Another layer of protection is provided by using Microsoft Authenticode to sign the Windows Installer (MSI) package itself. This helps protect the MSI package against tampering and accidental corruption. Refer to the documentation for your MSI creation tool for more information about how to sign packages with Authenticode.

## Revocation

In the event that the security of the private key is compromised or some security-related event renders a Code-Signing certificate invalid, the developer must revoke the certificate. Not doing so would weaken the integrity of the developer and the effectiveness of signing code. A CA can also issue a revocation with specific time; code signed with a time stamp prior to the revocation time will still be considered valid, but code with a subsequent time stamp will be invalid. Certificate revocation affects code in any applications that is signed with the revoked certificate.

## Code-Signing Drivers

Drivers can and should be Authenticode-signed. Kernel-mode drivers have additional requirements: 64-bit editions of Windows Vista and Windows 7 will prevent installation of all unsigned kernel-mode drivers, and all versions of Windows will present a warning prompt when a user attempts to install an unsigned driver. In addition, administrators can set Group Policy to prevent unsigned drivers from being installed on Microsoft Windows Server 2003, Windows XP Professional x64 Edition, and 32-bit editions of Windows Vista and Windows 7.

Many types of drivers can be signed with a Microsoft-trusted signature — as part of the Windows Certification Program of [Windows Hardware Quality Labs](https://www.microsoft.com/whdc/whql/) (WHQL) or the [Unclassified Signature Program](https://www.microsoft.com/whdc/winlogo/drvsign/dqs.mspx) (formerly named Driver Reliability Signature) — which allows the system to fully trust these drivers and install them even without administrative credentials.

At a minimum, drivers should be Authenticode-signed, because drivers that are unsigned or self-signed (that is, signed with a test certificate) will fail to install on many Windows-based platforms. For more information about signing drivers and code and related feature, see [Driver Signing Requirements for Windows](https://www.microsoft.com/whdc/winlogo/drvsign/drvsign.mspx) on [Windows Hardware Developer Central](https://www.microsoft.com/whdc/).

## Summary

Using Microsoft Authenticode is a straightforward process. Once you have obtained a CER and created a private key, it is a simple matter of using the tools provided by Microsoft. You can then enable important features in Windows Vista and Windows 7, such as parental controls, and let customers know that your product comes directly from its rightful owner.

## More information

More information about tools and processes related to signing code, see the following links:

-   [Cryptography Tools](/windows/desktop/SecCrypto/cryptography-tools)
-   [Crypto API Tools Reference](/windows/desktop/SecCrypto/cryptoapi-tools-reference)
-   [Authenticode Overview and Turtorials](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms537360(v=vs.85))
-   [Digital Certificates](/windows/desktop/SecCrypto/digital-certificates)
-   [Deploying Authenticode](https://www.microsoft.com/technet/security/topics/cryptographyetc/authenticodets.mspx)
-   [How To: Create Temporary Certificates for Use During Development](/dotnet/framework/wcf/feature-details/how-to-create-temporary-certificates-for-use-during-development)

 

 
