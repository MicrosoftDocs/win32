---
description: The Microsoft Windows HTTP Services (WinHTTP) certificate configuration tool, &\#0034;WinHttpCertCfg.exe&\#0034;, enables administrators to install and configure client certificates in any certificate store that can be accessed by the Internet Server Web Application Manager (IWAM) account. The tool also eliminates the need to do anything special to accounts such as the IWAM account to gain access to certificates when using Active Server Pages (ASP).
ms.assetid: e4c2afc2-0fd3-4bdd-812e-f112958e1576
title: WinHttpCertCfg.exe, a Certificate Configuration Tool
ms.topic: article
ms.date: 05/31/2018
---

# WinHttpCertCfg.exe, a Certificate Configuration Tool

The [Microsoft Windows HTTP Services (WinHTTP)](about-winhttp.md) certificate configuration tool, "WinHttpCertCfg.exe", enables administrators to install and configure client certificates in any [*certificate store*](glossary.md) that can be accessed by the Internet Server Web Application Manager (IWAM) account. The tool also eliminates the need to do anything special to accounts such as the IWAM account to gain access to certificates when using Active Server Pages (ASP).

The Microsoft Management Console (MMC) enables administrators to import client certificates to a local computer. However, importing a certificate does not automatically grant access to the private key for other accounts. This private key is required for client certificate authentication. The Microsoft Windows HTTP Services (WinHTTP) certificate configuration tool provides the ability to grant access to additional accounts, such as the IWAM account, when required.

-   [Using the Certificate Configuration Tool](#using-the-certificate-configuration-tool)
-   [Examples](#examples)

## Using the Certificate Configuration Tool

The WinHTTP certificate configuration tool, WinHttpCertCfg.exe, is available as a download on the [Windows Server 2003 Resource Kit Tools](https://www.microsoft.com/downloads/details.aspx?familyid=9d467a69-57ff-4ae7-96ee-b18c4790cffd) website. The following example code shows the valid command line parameters to use with this tool.

``` syntax
winhttpcertcfg [-?]
 
winhttpcertcfg [-i PFXFile | -g | -r | -l]
               [-a Account] [-c CertStore] 
               [-s SubjectStr] [-p PFXPassword]
```

The following table lists parameters for the configuration tool.




| Parameter | Description | 
|-----------|-------------|
| -? | Displays syntax data. | 
| -i | Specifies that the certificate is to be imported from a Personal Information Exchange (PFX) file. This parameter must be followed by the name of the file. When this parameter is specified, "-a" and "-c" must also be specified. | 
| -g | Specifies that access is granted to a private key. When this parameter is specified, "-a", "-c", and "-s" must also be specified. | 
| -r | Specifies that access is removed for a private key. When this parameter is specified, "-a", "-c", and "-s" must also be specified. | 
| -l | Specifies that accounts with access to a private key are listed. When this parameter is specified, "-c" and "-s" must also be specified. | 
| -a | Specifies the user account on the machine being configured. This could be a local machine or domain account, such as "IWAM_TESTMACHINE", "TESTUSER", or "TESTDOMAIN\DOMAINUSER". | 
| -c | Specifies the location and name of the <a href="glossary.md"><em>certificate store</em></a>. Use "LOCAL_MACHINE" or "CURRENT_USER" to designate which registry branch to use for the location. The <em>certificate store</em> can be any installed on the machine. Typical name examples are "MY", "Root", and "TrustedPeople". The location and name of the <em>certificate store</em> are separated with a backward slash, for example, "LOCAL_MACHINE\Root".<blockquote>[!Note]<br />Although the "CURRENT_USER" branch of the registry can be specified with this parameter, extending access to private keys is primarily intended for certificates installed in a local computer <a href="glossary.md"><em>certificate store</em></a> that can be accessed by multiple users.</blockquote><br /> | 
| -s | Specifies a case-insensitive search string for finding the first enumerated certificate with a subject name that contains this substring. | 
| -p | Specifies a password that is used to import the certificate and the private key. This is only used with the import option. | 




 

> [!NOTE]
> The user must have sufficient privileges to use this tool, which requires the user to be an administrator and the same user who installed the client certificate, if installed.
>
> The "WinHttpCertCfg.exe" tool is not useful to configure certificates stored in a file system such as FAT32, which does not support access control lists (ACL).

## Examples

The following examples show some of the ways in which the configuration tool can be used.

1.  This command lists accounts that have access to the private key for the "MyCertificate" certificate in the "Root" [*certificate store*](glossary.md) of the LOCAL\_MACHINE branch of the registry.

    **winhttpcertcfg -l -c LOCAL\_MACHINE\\Root -s MyCertificate**

2.  This command grants access to the private key of the "MyCertificate" certificate in the "My" [*certificate store*](glossary.md) for the TESTUSER account.

    **winhttpcertcfg -g -c LOCAL\_MACHINE\\My -s MyCertificate -a TESTUSER**

3.  This command imports a certificate and private key from a PFX file and extends private key access to another account.

    **winhttpcertcfg -i PFXFile -c LOCAL\_MACHINE\\My -a IWAM\_TESTMACHINE -p PFXPassword**

4.  This command denies access to the private key for the IWAM\_TESTMACHINE account with the specified certificate.

    **winhttpcertcfg -r -c LOCAL\_MACHINE\\Root -s MyCertificate -a IWAM\_TESTMACHINE**

 

 




