---
Description: The syntax of a manifest configuration file (MCF) is shown in the following diagram. To create a manifest, you must supply a completed configuration file to the Genmanifest.exe program.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 49de9275-5819-4294-9c07-f91990ebdbc2
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Manifest Configuration File Syntax
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Manifest Configuration File Syntax

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The syntax of a manifest configuration file (MCF) is shown in the following diagram. To create a manifest, you must supply a completed configuration file to the Genmanifest.exe program.

![mcf syntax diagram](images/mcf-syntax.png)

## Syntax

<dl> <dt>

<span id="VALIDITYTIME"></span><span id="validitytime"></span>**VALIDITYTIME**
</dt> <dd>

An optional value that specifies the manifest validity period. If the period is specified, both **FROM** and **UNTIL** values must be included. The validity time format is *YYYY-MM-DDTHH:MM*. For example, 2002-08-19T22:14 represents 10:14 P.M., August 19, 2002.

</dd> <dt>

<span id="ID_of_certificate_or_license"></span><span id="id_of_certificate_or_license"></span><span id="ID_OF_CERTIFICATE_OR_LICENSE"></span>**ID of certificate or license**
</dt> <dd>

A value that specifies an ID number to assign to the created manifest. If you do not manually assign a number, you must use the **AUTO-GUID** element, which instructs Genmanifest.exe to generate a number automatically.

</dd> <dt>

<span id="Private_key_file_path"></span><span id="private_key_file_path"></span><span id="PRIVATE_KEY_FILE_PATH"></span>**Private key file path**
</dt> <dd>

A required value that specifies a cryptographic service provider (CSP) and hardware security module (HSM) or the path to a .dat file that contains the private key used to sign the manifest. If you specify a private key, the associated public key is identified by the **INCLUSION** element. If any folder name in the path contains a space, surround the entire path with quotation marks. For more information about keys, see [Obtaining a Key Pair for Manifest Signing](obtaining-a-key-pair-for-manifest-signing.md).

</dd> <dt>

<span id="ISSUER"></span><span id="issuer"></span>**ISSUER**
</dt> <dd>

An optional block that describes the issuer of the license by using **TYPE** ("Corporation" for example) and **ID** elements. You can also specify the issuer name and zero or more addresses.

</dd> <dt>

<span id="MODULELIST"></span><span id="modulelist"></span>**MODULELIST**
</dt> <dd>

A required block that describes the file or files that the manifest verifies. Your application must be listed here.

-   **REQ** specifies one or more required files.
-   **OPT** specifies a file that may be loaded.
-   **HASH** instructs Genmanifest.exe to create a hash of the specified file and include it in the manifest. **HASH** is the default value.
-   **NOHASH** indicates that no hash will be created but that the file has been either single signed or catalog (CAT) file–signed using Authenticode, with the public key of the CAT file key pair listed in the **INCLUSION** block. Only Microsoft Authenticode signing is supported. For more information, see [Authenticode Signing Included Modules](authenticode-signing-included-modules.md). CAT files are used by the operating system to store signatures of binary files.

</dd> <dt>

<span id="POLICYLIST"></span><span id="policylist"></span>**POLICYLIST**
</dt> <dd>

A required value that lists the modules that can or cannot be loaded into a secure environment. Modules specified by the **INCLUSION** element can be loaded but are not required. Modules those specified by the **EXCLUSION** element cannot be loaded. The following rules apply to each type:

-   **INCLUSION** files can be specified by using the **PUBLICKEY** element which identifies the path to a file that contains a public key. At least one value must be specified, the public key that matches the private key specified at the beginning of the file. You can also specify additional public keys associated with the private keys used for single-signed or CAT file-signed modules.
-   **EXCLUSION** files can be specified by using any of the following elements:
    -   The **PUBLICKEY** element identifies a path to a file that contains the public key associated with a private key used to sign a manifest or a module.
    -   The **DIG** element identifies the path of the excluded file and creates a digest to include in the manifest.
    -   The **FILE** element lists the file name, minimum version, and maximum version. You must include the minimum and maximum version numbers.

</dd> </dl>

## MCF File Sample

The following example shows an MCF file that uses many of the elements discussed in the preceding section.

``` syntax
AUTO-GUID

%MYBASEPATH%\\keys\\mypriv1024.dat

MODULELIST
  REQ HASH MyApp.exe
  REQ NOHASH %SystemRoot%\\system32\\kernel32.dll
  OPT     %SystemRoot%\\system32\\msvcrt.dll


POLICYLIST
  INCLUSION
       PUBLICKEY     C:\\mypub1024.dat

  EXCLUSION
       DIG          C:\\ecsrv.dll
       DIG          C:\\ud.dll
       PUBLICKEY     C:\\SampleExcPubKey.dat
       FILE          MyApp.exe 5.1.3500.0 5.1.3572.0
```

## General Rules

The following list identifies several guidelines to follow when creating MCF files:

-   Line spaces are inserted for readability only. Genmanifest.exe ignores all white space when it processes the configuration file.
-   Block comments are allowed within standard C comment delimiters (/\*...\*/).
-   Text is not case-sensitive.
-   File paths can be absolute or relative and can include environment variables.
-   The backslash (\) is an escape character. When building a file path, you must use two backslashes (\\\) to avoid errors, even when the path is enclosed in quotation marks.
-   String values that include a space must be enclosed in quotation marks. Therefore, C:\\\\Myfile.fil does not need surrounding quotation marks, but "C:\\\\My file.fil" does.
-   A manifest can contain only one .exe file (your application), and this file must own the process that is running Active Directory Rights Management Services (AD RMS).

## Related topics

<dl> <dt>

[Creating an Application Manifest](creating-an-application-manifest.md)
</dt> </dl>

 

 



