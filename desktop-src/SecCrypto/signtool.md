---
title: SignTool
description: Learn how to use SignTool, a command-line tool that digitally signs files, verifies the signatures in files, and time stamps files.
ms.assetid: aa59cb35-5fba-4ce8-97ea-fc767c83f88e
ms.topic: reference
ms.date: 10/28/2026
---

# SignTool

SignTool is a command-line tool that digitally signs files, verifies the signatures in files, removes the signatures from files, and time stamps files. SignTool can sign executable files, scripts, catalog files, and other file types that have a registered Subject Interface Package (SIP). For information about why signing files is important, see [Introduction to code signing](cryptography-tools.md).

SignTool is available as part of the [Windows Software Development Kit (SDK)](https://developer.microsoft.com/windows/downloads/windows-sdk). The tool is installed in the `\Bin` folder of the Windows SDK installation path, for example: `C:\Program Files (x86)\Windows Kits\10\bin\10.0.22621.0\x64\signtool.exe`.

> [!NOTE]
> The Windows SDK, [Windows Hardware Lab Kit (HLK)](/windows-hardware/test/hlk/), [Windows Driver Kit (WDK)](/windows-hardware/drivers/download-the-wdk), and [Windows Assessment and Deployment Kit (ADK)](/windows-hardware/get-started/adk-install) builds 20236 and later require that you specify the digest algorithm. The SignTool `sign` command requires the file digest algorithm option (`/fd`) and the time stamp digest algorithm option (`/td`) during signing and time stamping, respectively.
>
> If `/fd` isn't specified during signing and if `/td` isn't specified during time stamping, the command throws a warning, error code 0, initially. In later versions of SignTool, the warning becomes an error. We recommend SHA256. It's considered to be more secure than SHA1 by the industry.

## Syntax

```console
signtool [command] [options] [file_name | ...]
signtool @response_file
```

## Parameters

| Argument | Description |
|----------|-------------|
| `command` | One of five commands that specifies an operation to perform on a file: `catdb`, `remove`, `sign`, `timestamp`, or `verify`. For a description of each command, see the next table. |
| `options` | An option that modifies a command. In addition to the global `/q` and `/v` options, each command supports a unique set of options. |
| `file_name` | The path to a file on which the command operates. |
| `response_file` | The path to a response file that contains one or more SignTool commands. For more information, see [Response files](#response-files). |

SignTool supports the following commands:

| Command | Description |
|---------|-------------|
| `catdb` | Adds a catalog file to, or removes it from, a catalog database. Catalog databases are used for automatic lookup of catalog files and are identified by GUID. For a list of the options supported by the `catdb` command, see [catdb command options](#catdb-command-options). |
| `remove` | Removes a signature from a file. For a list of the options supported by the `remove` command, see [remove command options](#remove-command-options). |
| `sign` | Digitally signs files. Digital signatures protect files from tampering and enable users to verify the signer based on a signing certificate. For a list of the options supported by the `sign` command, see [sign command options](#sign-command-options). |
| `timestamp` | Time stamps files. For a list of the options supported by the `timestamp` command, see [timestamp command options](#timestamp-command-options). |
| `verify` | Verifies the digital signature of files. Determines whether the signing certificate was issued by a trusted authority, whether the signing certificate has been revoked, and, optionally, whether the signing certificate is valid for a specific policy. For a list of the options supported by the `verify` command, see [verify command options](#verify-command-options). |

The following options apply to all SignTool commands:

| Global option | Description |
|---------------|-------------|
| `/q` | Displays no output if the command runs successfully, and displays minimal output if the command fails. |
| `/v` | Displays verbose output regardless of whether the command runs successfully or fails, and displays warning messages. |
| `/debug` | Displays debugging information. |

## Response files

Use a response file to store SignTool commands for repeatable or automated operations. Specify one argument on each line. The first argument must be the command, such as `sign` or `verify`. To run multiple commands, separate them with an empty line.

For example, create a file named `commands.txt` with the following contents:

```text
sign
/n "Contoso Software"
/fd SHA256
/tr http://timestamp.digicert.com
/td SHA256
MyFile.exe

verify
/pa
/v
MyFile.exe
```

Run the commands by specifying the response file:

```console
signtool @commands.txt
```

## Catdb command options

The following table lists the options that can be used with the `catdb` command:

| Catdb option | Description |
|--------------|-------------|
| `/d` | Specifies that the default catalog database is updated. If you don't use either `/d` or `/g`, SignTool updates the system component and driver database. |
| `/g` *GUID* | Specifies that the catalog database identified by the GUID is updated.|
| `/r` | Removes the specified catalog from the catalog database. If this option isn't specified, SignTool adds the specified catalog to the catalog database.|
| `/u` | Specifies that a unique name is automatically generated for the added catalog files. If necessary, the catalog files are renamed to prevent name conflicts with existing catalog files. If this option isn't specified, SignTool overwrites any existing catalog that has the same name as the specified catalog.|

> [!NOTE]
> Catalog databases are used for automatic lookup of catalog files.

## Remove command options

The following table lists the options that can be used with the `remove` command:

| Remove option | Description |
|---------------|-------------|
| `/c` | Remove all certificates, except for the signer certificate from the signature. |
| `/q` | No output on success and minimal output on failure. As always, SignTool returns `0` on success and `1` on failure. |
| `/s` | Remove the signature entirely. |
| `/u` | Remove the unauthenticated attributes from the signature e.g. dual signatures and timestamps. |
| `/v` | Print verbose success and status messages. This may also provide slightly more information on error. |

## Sign command options

 The following table lists the options that can be used with the `sign` command:

| Sign command option | Description |
|---------------------|-------------|
| `/a` | Automatically selects the best signing certificate. SignTool finds all valid certificates that satisfy all specified conditions and selects the one that is valid for the longest time. If this option isn't present, SignTool expects to find only one valid signing certificate. |
| `/ac` *file* | Adds another certificate from *file* to the signature block. |
| `/as` | Appends this signature. If no primary signature exists, this signature is made the primary signature instead. |
| `/Author` *value* | Adds the author authenticated attribute. Equivalent to `/sa 1.3.6.1.4.1.311.2.7.8 value`. |
| `/c` *CertTemplateName* | Specifies the Certificate Template Name (a Microsoft extension) for the signing certificate. |
| `/csp` *CSPName* | Specifies the cryptographic service provider (CSP) that contains the private key container. |
| `/d` *Desc* | Specifies a description of the signed content. |
| `/dg` *Path* | Generates the digest to be signed and the unsigned PKCS7 files. The output digest and PKCS7 files are *\<Path>\\\<FileName>.dig* and *\<Path>\\\<FileName>.p7u*. To output an extra XML file, use `/dxml`. |
| `/di` *Path* | Creates the signature by ingesting the signed digest to the unsigned PKCS7 file. The input signed digest and unsigned PKCS7 files should be *\<Path>\\\<FileName>.dig.signed* and *\<Path>\\\<FileName>.p7u*. |
| `/dlib` *DLL* | Specifies the DLL that implements the `AuthenticodeDigestSign` function to sign the digest with. This option is equivalent to using SignTool separately with the `/dg`, `/ds`, and `/di` options. This option invokes all three as one atomic operation. |
| `/dmdf` *Filename* | When used with the `/dg` option, passes the file’s contents to the `AuthenticodeDigestSign` function without modification. |
| `/ds` | Signs the digest only. The input file should be the digest generated by the `/dg` option. The output file is: *\<File>.signed*. |
| `/du` *URL* | Specifies a Uniform Resource Locator (URL) for the expanded description of the signed content. |
| `/dxml` | When used with the `/dg` option, produces an XML file. The output file is: *\<Path>\\\<FileName>.dig.xml*. |
| `/f` *SignCertFile* | Specifies the signing certificate in a file. If the file is in Personal Information Exchange (PFX) format and protected by a password, use the `/p` option to specify the password. If the file doesn't contain private keys, use the `/csp` and `/kc` options to specify the CSP and private key container name. |
| `/fd` *alg* | Specifies the file digest algorithm to use for creating file signatures. **Note**: If the `/fd` option isn't specified while signing, the command generates an error. |
| `/fd certHash` | Specifying the string "certHash" causes the command to use the algorithm specified on the signing certificate. **Note**: If the `/fd` option isn't specified while signing, the command generates an error. |
| `/FileDescription` *value* | Adds the file description authenticated attribute. Equivalent to `/sa 1.3.6.1.4.1.311.2.7.3 value`. This option differs from `/d`, which sets the Authenticode description of the signed content. |
| `/FileVersion` *value* | Adds the file version authenticated attribute. Equivalent to `/sa 1.3.6.1.4.1.311.2.7.2 value`. |
| `/i` *IssuerName* | Specifies the name of the issuer of the signing certificate. This value can be a substring of the entire issuer name. |
| `/InternalName` *value* | Adds the internal name authenticated attribute. Equivalent to `/sa 1.3.6.1.4.1.311.2.7.1 value`. |
| `/kc` *PrivKeyContainerName* | Specifies the private key container name. |
| `/Language` *value* | Adds the language authenticated attribute. Equivalent to `/sa 1.3.6.1.4.1.311.2.7.7 value`. |
| `/n` *SubjectName* | Specifies the name of the subject of the signing certificate. This value can be a substring of the entire subject name. |
| `/nph` | If supported, suppresses page hashes for executable files. The default is determined by the **SIGNTOOL_PAGE_HASHES** environment variable and by the *wintrust.dll* version. This option is ignored for non-PE files. |
| `/OriginalFilename` *value* | Adds the original file name authenticated attribute. Equivalent to `/sa 1.3.6.1.4.1.311.2.7.6 value`. |
| `/p` *Password* | Specifies the password to use when opening a PFX file. Use the `/f` option to specify a PFX file. |
| `/p7` *Path* | Specifies that a Public Key Cryptography Standards (PKCS) #7 file is produced for each specified content file. PKCS #7 files are named *\<path>\\\<filename>.p7*. |
| `/p7ce` *Value* | Specifies options for the signed PKCS #7 content. Set *Value* to `Embedded` to embed the signed content in the PKCS #7 file, or to `DetachedSignedData` to produce the signed data portion of a detached PKCS #7 file. If the `/p7ce` option isn't specified, the signed content is embedded by default. |
| `/p7co` *\<OID>* | Specifies the object identifier (OID) that identifies the signed PKCS #7 content. |
| `/ph` | If supported, generates page hashes for executable files. |
| `/Product` *value* | Adds the product name authenticated attribute. Equivalent to `/sa 1.3.6.1.4.1.311.2.7.4 value`. |
| `/ProductVersion` *value* | Adds the product version authenticated attribute. Equivalent to `/sa 1.3.6.1.4.1.311.2.7.5 value`. |
| `/PublishTime` *value* | Adds the publish time authenticated attribute. Equivalent to `/sa 1.3.6.1.4.1.311.2.7.9 value`. |
| `/r` *RootSubjectName* | Specifies the name of the subject of the root certificate that the signing certificate must chain to. This value can be a substring of the entire subject name of the root certificate. |
| `/sa` *OID* *value* | Adds an authenticated attribute to the signature. SignTool encodes *value* as an ASN.1 UTF-8 string. Specify this option multiple times to add multiple attributes. |
| `/s` *StoreName* | Specifies the store to open when the command searches for the certificate. If this option isn't specified, the command opens the `My` store. |
| `/sha1` *Hash* | Specifies the SHA1 hash of the signing certificate. The SHA1 hash is commonly used when multiple certificates satisfy the criteria specified by the remaining options. |
| `/sm` | Specifies that the command uses a machine store, instead of a user store. |
| `/SourceURL` *value* | Adds the source URL authenticated attribute. Equivalent to `/sa 1.3.6.1.4.1.311.2.7.10 value`. |
| `/t` *URL* | Specifies the URL of the time stamp server. If this option or `/tr` isn't specified, the signed file isn't time stamped. If time stamping fails, the command generates a warning. This option can't be used with the `/tr` option. |
| `/td` *alg* | Used with the `/tr` option to request a digest algorithm used by the RFC 3161 time stamp server. **Note**: If `/td` isn't specified while time stamping, the command generates an error. |
| `/tr` *URL* | Specifies the URL of the RFC 3161 time stamp server. If this option or `/t` isn't specified, the signed file isn't time stamped. If the time stamping fails, the command generates a warning. This option can't be used with the `/t` option. |
| `/u` *Usage* | Specifies the enhanced key usage (EKU) that must be present in the signing certificate. The usage value can be specified by OID or string. The default usage is `Code Signing` or  `1.3.6.1.5.5.7.3.3`. |
| `/uw` | Specifies usage of `Windows System Component Verification` or `1.3.6.1.4.1.311.10.3.6`. |

### Authenticated metadata attributes

Authenticated metadata attributes provide signed file identity and version information for scripts and other files that don't have Portable Executable (PE) version resources. Policy and deployment tools can use this metadata to identify signed content.

The friendly metadata options and their equivalent OIDs are:

| SignTool option | WinTrust identifier | OID |
|-----------------|---------------------|-----|
| `/InternalName` | `szOID_SIGNED_ATTRIBUTE_INTERNAL_NAME` | `1.3.6.1.4.1.311.2.7.1` |
| `/FileVersion` | `szOID_SIGNED_ATTRIBUTE_FILE_VERSION` | `1.3.6.1.4.1.311.2.7.2` |
| `/FileDescription` | `szOID_SIGNED_ATTRIBUTE_FILE_DESCRIPTION` | `1.3.6.1.4.1.311.2.7.3` |
| `/Product` | `szOID_SIGNED_ATTRIBUTE_PRODUCT` | `1.3.6.1.4.1.311.2.7.4` |
| `/ProductVersion` | `szOID_SIGNED_ATTRIBUTE_PRODUCT_VERSION` | `1.3.6.1.4.1.311.2.7.5` |
| `/OriginalFilename` | `szOID_SIGNED_ATTRIBUTE_ORIGINAL_FILENAME` | `1.3.6.1.4.1.311.2.7.6` |
| `/Language` | `szOID_SIGNED_ATTRIBUTE_LANGUAGE` | `1.3.6.1.4.1.311.2.7.7` |
| `/Author` | `szOID_SIGNED_ATTRIBUTE_AUTHOR` | `1.3.6.1.4.1.311.2.7.8` |
| `/PublishTime` | `szOID_SIGNED_ATTRIBUTE_PUBLISH_TIME` | `1.3.6.1.4.1.311.2.7.9` |
| `/SourceURL` | `szOID_SIGNED_ATTRIBUTE_SOURCE_URL` | `1.3.6.1.4.1.311.2.7.10` |

The named metadata options are available in Windows SDK build 10.0.25231.0 and later. Build 10.0.25231.0 was a preview SDK. The first stable release confirmed to contain these options is the Windows 11, version 24H2 SDK (build 10.0.26100.0; SDK build tools package version 10.0.26100.1).

For procedures, see [Use SignTool to sign a file](using-signtool-to-sign-a-file.md) and [Sign scripts and non-PE files with SignTool](sign-scripts-and-non-pe-files.md).

## Timestamp command options

The following table lists the options that can be used with the `timestamp` command:

| Timestamp option | Description |
|------------------|-------------|
| `/p7` | Time stamps PKCS #7 files. |
| `/t` *URL* | Specifies the URL of the time stamp server. The file being time stamped must have previously been signed. Either the `/t` or the `/tr` option is required. |
| `/td` *alg* | Used with the `/tr` option to request a digest algorithm used by the RFC 3161 time stamp server. **Note**: If `/td` isn't specified while time stamping, the command generates a warning. |
| `/tp` *index* | Time stamps the signature at *index*. |
| `/tr` *URL* | Specifies the URL of the RFC 3161 time stamp server. The file being time stamped must have previously been signed. Either the `/tr` or the `/t` option is required. |

## Verify command options

The following table lists the options that can be used with the `verify` command:

| Verify option | Description |
|---------------|-------------|
| `/a` | Specifies that all methods can be used to verify the file. First, SignTool searches the catalog databases to determine whether the file is signed in a catalog. If the file isn't signed in any catalog, SignTool attempts to verify the file's embedded signature. We recommend this option when verifying files that might or might not be signed in a catalog. Examples of files that might or might not be signed include Windows files or drivers. |
| `/ad` | Finds the catalog by using the default catalog database. |
| `/all` | Verifies all signatures in a file with multiple signatures. |
| `/as` | Finds the catalog by using the system component (driver) catalog database. |
| `/ag` *CatDBGUID* | Finds the catalog in the catalog database identified by the GUID. |
| `/c` *CatFile* | Specifies the catalog file by name. |
| `/d` | Prints the description and description URL. Windows Vista and earlier: This option isn't supported. |
| `/ds` *Index* | Verifies the signature at a certain position. |
| `/hash`{*SHA1*\|*SHA256*} | Specifies an optional hash algorithm to use when searching for a file in a catalog. |
| `/kp` | Performs the verification by using the x64 kernel-mode driver signing policy. |
| `/ms` | Uses multiple verification semantics. This behavior is the default of a [WinVerifyTrust](/windows/win32/api/Wintrust/nf-wintrust-winverifytrust) call. |
| `/o` *Version* | Verifies the file by operating system version. The version parameter is of the form: *\<PlatformID>:\<VerMajor>.\<VerMinor>.\<BuildNumber>*. We recommend the use of the `/o` option. If `/o` isn't specified, SignTool might return unexpected results. For example, if you don't include `/o`, then system catalogs that validate correctly on an older operating system might not validate correctly on a newer operating system. |
| `/p7` | Verifies PKCS \#7 files. No existing policies are used for PKCS \#7 validation. SignTool checks the signature and builds a chain for the signing certificate. |
| `/pa` | Specifies that the Default Authentication Verification Policy is used. If the `/pa` option isn't specified, SignTool uses the Windows Driver Verification Policy. This option can't be used with the `catdb` options. |
| `/pg` *PolicyGUID* | Specifies a verification policy by GUID. The GUID corresponds to the `ActionID` of the verification policy. This option can't be used with the `catdb` options. |
| `/ph` | Print and verify page hash values. Windows Vista and earlier: This option isn't supported. |
| `/r` *RootSubjectName* | Specifies the name of the subject of the root certificate that the signing certificate must chain to. This value can be a substring of the entire subject name of the root certificate. |
| `/tw` | Specifies that the command generates a warning if the signature isn't time stamped.|

The SignTool `verify` command determines whether the signing certificate was issued by a trusted authority, whether the signing certificate has been revoked, and, optionally, whether the signing certificate is valid for a specific policy.

The SignTool `verify` command outputs the embedded signature status unless an option is specified to search a catalog, such as `/a`, `/ad`, `/as`, `/ag`, or `/c`.

## Return value

SignTool returns one of the following exit codes when it terminates:

| Exit code | Description |
|-----------|-------------|
| `0` | Execution was successful. |
| `1` | Execution has failed. |
| `2` | Execution has completed with warnings. |

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

The following command signs a PowerShell script and adds authenticated metadata by using the friendly metadata options.

```console
signtool sign /a /fd SHA256 /tr http://timestamp.digicert.com /td SHA256 /InternalName "Contoso.Deploy" /FileVersion "2.1.0" /FileDescription "Contoso deployment script" /Product "Contoso Tools" /ProductVersion "2.1" /OriginalFilename "Deploy.ps1" Deploy.ps1
```

The following command uses `/sa` to add the same original file name attribute by its OID.

```console
signtool sign /a /fd SHA256 /sa 1.3.6.1.4.1.311.2.7.6 "Deploy.ps1" Deploy.ps1
```

The following command signs an ActiveX control and provides information that's displayed in a browser when the user is prompted to install the control.

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

The following command verifies a system file that's signed in a catalog named `MyCatalog.cat`.

```console
signtool verify /c MyCatalog.cat SystemFile.dll
```

The following command completely removes the signature from a file.

```console
signtool remove /s MyFile.exe
```

## See also

- [Use SignTool to sign a file](using-signtool-to-sign-a-file.md)
- [Sign scripts and non-PE files with SignTool](sign-scripts-and-non-pe-files.md)
- [Introduction to code signing](cryptography-tools.md)
