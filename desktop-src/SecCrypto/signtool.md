---
title: SignTool
description: Learn how to use SignTool, a command-line tool that digitally signs files, verifies the signatures in files, and time stamps files.
ms.assetid: aa59cb35-5fba-4ce8-97ea-fc767c83f88e
ms.topic: article
ms.date: 02/06/2023
---

# SignTool

SignTool is a command-line tool that digitally signs files, verifies the signatures in files, and time stamps files. For information about why signing files is important, see [Introduction to code signing](cryptography-tools.md). The tool is installed in the *\Bin* folder of the Microsoft Windows Software Development Kit (SDK) installation path, for example: *C:\Program Files (x86)\Windows Kits\10\bin\10.0.19041.0\x64\signtool.exe*.

SignTool is available as part of the Windows SDK, which you can download from [Windows SDK](https://developer.microsoft.com/windows/downloads/windows-sdk).

> [!NOTE]
> The Windows 10 SDK, Windows 10 HLK, Windows 10 WDK, and Windows 10 ADK builds 20236 and later require that you specify the digest algorithm. The SignTool `sign` command requires the file digest algorithm option (`/fd`) and the time stamp digest algorithm option (`/td`) during signing and time stamping, respectively.
>
> If `/fd` isn't specified during signing and if `/td` isn't specified during time stamping, the command throws a warning, error code 0, initially. In later versions of SignTool, the warning becomes an error. We recommend SHA256. It is considered to be more secure than SHA1 by the industry.

## Syntax

```console
signtool [command] [options] [file_name | ...]
```

## Parameters

|Argument|Description|
|----|----|
|`command`|One of four commands that specifies an operation to perform on a file: `catdb`, `sign`, `timestamp`, or `verify`. For a description of each command, see the next table.|
|`options`|An option that modifies a command. In addition to the global `/q` and `/v` options, each command supports a unique set of options.|
|`file_name`|The path to a file to sign.|

SignTool supports the following commands:

|Command|Description|
|----|----|
|`catdb`|Adds a catalog file to, or removes it from, a catalog database. Catalog databases are used for automatic lookup of catalog files and are identified by GUID. For a list of the options supported by the `catdb` command, see [catdb command options](/dotnet/framework/tools/signtool-exe#catdb-command-options).|
|`sign`|Digitally signs files. Digital signatures protect files from tampering and enable users to verify the signer based on a signing certificate. For a list of the options supported by the `sign` command, see [sign command options](/dotnet/framework/tools/signtool-exe#sign-command-options).|
|`timestamp`|Time stamps files. For a list of the options supported by the `timestamp` command, see [timestamp command options](/dotnet/framework/tools/signtool-exe#timestamp-command-options).|
|`verify`|Verifies the digital signature of files. Determines whether the signing certificate was issued by a trusted authority, whether the signing certificate has been revoked, and, optionally, whether the signing certificate is valid for a specific policy. For a list of the options supported by the `verify` command, see [verify command options](/dotnet/framework/tools/signtool-exe#verify-command-options).|

The following options apply to all SignTool commands.

|Global option|Description|
|----|----|
|`/q`|Displays no output if the command runs successfully, and displays minimal output if the command fails.|
|`/v`|Displays verbose output regardless of whether the command runs successfully or fails, and displays warning messages.|
|`/debug`|Displays debugging information.|

## Catdb command options

The following table lists the options that can be used with the `catdb` command.

| Catdb option | Description |
|----|----|
| `/d` | Specifies that the default catalog database is updated. If you don't use either `/d` or `/g`, SignTool updates the system component and driver database. |
| `/g` *GUID* | Specifies that the catalog database identified by the GUID is updated.|
| `/r` | Removes the specified catalog from the catalog database. If this option isn't specified, SignTool adds the specified catalog to the catalog database.|
| `/u` | Specifies that a unique name is automatically generated for the added catalog files. If necessary, the catalog files are renamed to prevent name conflicts with existing catalog files. If this option isn't specified, SignTool overwrites any existing catalog that has the same name as the specified catalog.|

> [!NOTE]
> Catalog databases are used for automatic lookup of catalog files.

## Sign command options

 The following table lists the options that can be used with the `sign` command.

|Sign command option|Description|
|----|----|
|`/a`|Automatically selects the best signing certificate. SignTool finds all valid certificates that satisfy all specified conditions and select the one that is valid for the longest time. If this option isn't present, SignTool expects to find only one valid signing certificate.|
|`/ac` *file*|Adds another certificate from *file* to the signature block.|
|`/as`|Appends this signature. If no primary signature exists, this signature is made the primary signature instead.|
|`/c` *CertTemplateName*|Specifies the Certificate Template Name (a Microsoft extension) for the signing certificate.|
|`/csp` *CSPName*|Specifies the cryptographic service provider (CSP) that contains the private key container.|
|`/d` *Desc*|Specifies a description of the signed content.|
|`/dg` *Path*|Generates the digest to be signed and the unsigned PKCS7 files. The output digest and PKCS7 files are *\<Path>\\\<FileName>.dig* and *\<Path>\\\<FileName>.p7u*. To output an extra XML file, use `/dxml`|
|`/di` *Path*|Creates the signature by ingesting the signed digest to the unsigned PKCS7 file. The input signed digest and unsigned PKCS7 files should be *\<Path>\\\<FileName>.dig.signed* and *\<Path>\\\<FileName>.p7u*.|
|`/dlib` *DLL*|Specifies the DLL that implements the `AuthenticodeDigestSign` function to sign the digest with. This option is equivalent to using SignTool separately with the `/dg`, `/ds`, and `/di` switches, except this option invokes all three as one atomic operation.|
|`/dmdf` *Filename*|When used with the `/dg` option, passes the file’s contents to the `AuthenticodeDigestSign` function without modification.|
|`/ds` |Signs the digest only. The input file should be the digest generated by the `/dg` option. The output file is: *\<File>.signed*.|
|`/du` *URL*|Specifies a Uniform Resource Locator (URL) for the expanded description of the signed content.|
|`/dxml` |When used with the `/dg` option, produces an XML file. The output file is: *\<Path>\\\<FileName>.dig.xml*.|
|`/f` *SignCertFile*|Specifies the signing certificate in a file. If the file is in Personal Information Exchange (PFX) format and protected by a password, use the `/p` option to specify the password. If the file doesn't contain private keys, use the `/csp` and `/kc` options to specify the CSP and private key container name.|
|`/fd` *alg*|Specifies the file digest algorithm to use for creating file signatures. Note: An error is generated if the `/fd` switch isn't provided while signing.|
|`/fd` *certHash*|Specifies that the string certHash defaults to the algorithm used on the signing certificate. Note: An error is generated if the `/fd` switch isn't provided while signing.|
|`/i` *IssuerName*|Specifies the name of the issuer of the signing certificate. This value can be a substring of the entire issuer name.|
|`/kc` *PrivKeyContainerName*|Specifies the private key container name.|
|`/n` *SubjectName*|Specifies the name of the subject of the signing certificate. This value can be a substring of the entire subject name.|
|`/nph`|If supported, suppresses page hashes for executable files. The default is determined by the **SIGNTOOL_PAGE_HASHES** environment variable and by the *wintrust.dll* version. This option is ignored for non-PE files.|
|`/p` *Password*|Specifies the password to use when opening a PFX file. Use the `/f` option to specify a PFX file.|
|`/p7` *Path*|Specifies that a Public Key Cryptography Standards (PKCS) #7 file is produced for each specified content file. PKCS #7 files are named *\<path>\\\<filename>.p7*.|
|`/p7ce` *Value*|Specifies options for the signed PKCS #7 content. Set *Value* to `Embedded` to embed the signed content in the PKCS #7 file, or to `DetachedSignedData` to produce the signed data portion of a detached PKCS #7 file. If the `/p7ce` option isn't used, the signed content is embedded by default.|
|`/p7co` *\<OID>*|Specifies the object identifier (OID) that identifies the signed PKCS #7 content.|
|`/ph`|If supported, generates page hashes for executable files.|
|`/r` *RootSubjectName*|Specifies the name of the subject of the root certificate that the signing certificate must chain to. This value can be a substring of the entire subject name of the root certificate.|
|`/s` *StoreName*|Specifies the store to open when searching for the certificate. If this option isn't specified, the `My` store is opened.|
|`/sha1` *Hash*|Specifies the SHA1 hash of the signing certificate. The SHA1 hash is commonly used when multiple certificates satisfy the criteria specified by the remaining switches.|
|`/sm`|Specifies that the command uses a machine store, instead of a user store.|
|`/t` *URL*|Specifies the URL of the time stamp server. If this option or `/tr` isn't specified, the signed file isn't time stamped. A warning is generated if time stamping fails. This option can't be used with the `/tr` option.|
|`/td` *alg*|Used with the `/tr` option to request a digest algorithm used by the RFC 3161 time stamp server. Note: An error is generated if `/td` isn't provided while time stamping.|
|`/tr` *URL*|Specifies the URL of the RFC 3161 time stamp server. If this option or `/t` isn't specified, the signed file isn't time stamped. A warning is generated if time stamping fails. This option can't be used with the `/t` option.|
|`/u` *Usage*|Specifies the enhanced key usage (EKU) that must be present in the signing certificate. The usage value can be specified by OID or string. The default usage is `Code Signing (1.3.6.1.5.5.7.3.3)`.|
|`/uw`|Specifies usage of `Windows System Component Verification (1.3.6.1.4.1.311.10.3.6)`.|

For usage examples, see [Using SignTool to Sign a File](using-signtool-to-sign-a-file.md).

## Timestamp command options

The following table lists the options that can be used with the `timestamp` command.

|Timestamp option|Description|
|----|----|
|`/p7`|Time stamps PKCS #7 files.|
|`/t` *URL*|Specifies the URL of the time stamp server. The file being time stamped must have previously been signed. Either the `/t` or the `/tr` option is required.|
|`/td` *alg*|Used with the `/tr` option to request a digest algorithm used by the RFC 3161 time stamp server. Note: An error is generated if `/td` isn't provided while time stamping.|
|`/tp` *index*|Time stamps the signature at *index*.|
|`/tr` *URL*|Specifies the URL of the RFC 3161 time stamp server. The file being time stamped must have previously been signed. Either the `/tr` or the `/t` option is required.|

## Verify command options

|Verify option|Description|
|----|----|
| `/a` | Specifies that all methods can be used to verify the file. First, SignTool searches the catalog databases to determine whether the file is signed in a catalog. If the file isn't signed in any catalog, SignTool attempts to verify the file's embedded signature. We recommend this option when verifying files that might or might not be signed in a catalog. Examples of files that might or might not be signed include Windows files or drivers. |
| `/ad` | Finds the catalog by using the default catalog database. |
| `/all` | Verifies all signatures in a file with multiple signatures. |
| `/as` | Finds the catalog by using the system component (driver) catalog database. |
| `/ag` *CatDBGUID* | Finds the catalog in the catalog database identified by the GUID. |
| `/c` *CatFile* | Specifies the catalog file by name. |
| `/d` | Prints the description and description URL. Windows Vista and earlier: This flag isn't supported. |
| `/ds` *Index* | Verifies the signature at a certain position. |
| `/hash`{*SHA1*\|*SHA256*} | Specifies an optional hash algorithm to use when searching for a file in a catalog. |
| `/kp` | Performs the verification by using the x64 kernel-mode driver signing policy. |
| `/ms` | Uses multiple verification semantics. This behavior is the default of a [WinVerifyTrust](/windows/desktop/api/Wintrust/nf-wintrust-winverifytrust) call. |
| `/o` *Version* | Verifies the file by operating system version. The version parameter is of the form: \<PlatformID>:\,VerMajor>.\<VerMinor>.\<BuildNumber>. We recommend the use of the `/o` switch. If `/o` isn't specified, SignTool might return unexpected results. For example, if you don't include `/o`, then system catalogs that validate correctly on an older operating system might not validate correctly on a newer operating system. |
| `/p7` | Verifies PKCS \#7 files. No existing policies are used for PKCS \#7 validation. SignTool checks the signature and builds a chain for the signing certificate. |
| `/pa` | Specifies that the Default Authentication Verification Policy is used. If the `/pa` option isn't specified, SignTool uses the Windows Driver Verification Policy. This option can't be used with the `catdb` options. |
| `/pg` *PolicyGUID* | Specifies a verification policy by GUID. The GUID corresponds to the ActionID of the verification policy. This option can't be used with the `catdb` options. |
| `/ph` | Print and verify page hash values. Windows Vista and earlier: This flag isn't supported. |
| `/r` *RootSubjectName* | Specifies the name of the subject of the root certificate that the signing certificate must chain to. This value can be a substring of the entire subject name of the root certificate. |
| `/tw` | Specifies that a warning is generated if the signature isn't time stamped.|

The SignTool `verify` command determines whether the signing certificate was issued by a trusted authority, whether the signing certificate has been revoked, and, optionally, whether the signing certificate is valid for a specific policy.

The SignTool `verify` command outputs the embedded signature status unless an option is specified to search a catalog (`/a`, `/ad`, `/as`, `/ag`, `/c`).

## Return value

SignTool returns one of the following exit codes when it terminates.

|Exit code|Description|
|----|----|
|0|Execution was successful.|
|1|Execution has failed.|
|2|Execution has completed with warnings.|

## Examples

The following command adds the catalog file *MyCatalogFileName.cat* to the system component and driver database. The `/u` option generates a unique name if necessary to prevent replacing an existing catalog file named *MyCatalogFileName.cat*.

```console
signtool catdb /v /u MyCatalogFileName.cat
```

The following command signs a file automatically by using the best certificate.

```console
signtool sign /a /fd SHA256 MyFile.exe 
```

The following command digitally signs a file by using a certificate stored in a password-protected PFX file.

```console
signtool sign /f MyCert.pfx /p MyPassword /fd SHA256 MyFile.exe 
```

The following command digitally signs and time stamps a file. The certificate used to sign the file is stored in a PFX file.

```console
signtool sign /f MyCert.pfx /t http://timestamp.digicert.com /fd SHA256 MyFile.exe 
```

The following command signs a file by using a certificate located in the `My` store that has a subject name of `My Company Certificate`.

```console
signtool sign /n "My Company Certificate" /fd SHA256 MyFile.exe 
```

The following command signs an ActiveX control and provides information that is displayed in a browser when the user is prompted to install the control.

```console
signtool sign /f MyCert.pfx /d: "MyControl" /du http://www.example.com/MyControl/info.html /fd SHA256 MyControl.exe 
```

The following command time stamps a file that has already been digitally signed.

```console
signtool timestamp /t http://timestamp.digicert.com MyFile.exe
```

The following command time stamps a file using an RFC 3161 time stamp server.

```console
signtool timestamp /tr http://timestamp.digicert.com /td SHA256 MyFile.exe
```

The following command verifies that a file has been signed.

```console
signtool verify MyFile.exe
```

The following command verifies a system file that can be signed in a catalog.

```console
signtool verify /a SystemFile.dll
```

The following command verifies a system file that is signed in a catalog named `MyCatalog.cat`.

```console
signtool verify /c MyCatalog.cat SystemFile.dll
```
