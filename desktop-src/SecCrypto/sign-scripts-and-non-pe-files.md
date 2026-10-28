---
description: Use SignTool authenticated metadata attributes to sign PowerShell scripts and other non-PE files.
title: Sign scripts and non-PE files with SignTool
ms.topic: how-to
ms.date: 10/28/2026
# customer intent: As a Windows developer, I want to sign scripts and non-PE files with identity and version metadata so that Windows and application-control systems can identify and trust them.
---

# Sign scripts and non-PE files with SignTool

Scripts and other non-Portable Executable (non-PE) files usually lack version resources that identify an executable's original file name, product, and version. The absence of that data is particularly concerning for organizations using [App Control for Business](/windows/security/application-security/application-control/app-control-for-business.md) to control what code runs on the organization's endpoints. SignTool can add this information to an embedded signature as authenticated metadata. Because the metadata is part of the signature, changing either the file or its signed metadata invalidates the signature.

This procedure signs a PowerShell script, but the same metadata options apply to other file types for which Windows has a registered Subject Interface Package (SIP).

## Prerequisites

- SignTool from Windows SDK build 10.0.25231.0 or later. Build 10.0.25231.0 was a preview SDK. The first stable release confirmed to contain the named metadata options is the Windows 11, version 24H2 SDK (build 10.0.26100.0; SDK build tools package version 10.0.26100.1).
- A code-signing certificate and access to its private key.
- An RFC 3161 time stamp service.
- A registered SIP that supports an embedded signature for the target file type.

## Choose authenticated metadata

Use stable values that remain consistent across releases. Consistent metadata lets application-control policies identify a product while allowing expected version changes.

1. Assign an internal name and original file name that uniquely identify the script within the product.

1. Assign file and product versions that follow the version scheme used by the release pipeline.

1. Assign a product name and description that distinguish the script from other components published by the same signer.

The following table lists the friendly SignTool options:

| Option | Purpose | Example |
|--------|---------|---------|
| `/InternalName` | Stable internal identity for the file | `Contoso.Deploy` |
| `/FileVersion` | Version of the individual file | `2.1.0` |
| `/FileDescription` | Human-readable description of the file | `Contoso deployment script` |
| `/Product` | Product or application name | `Contoso Tools` |
| `/ProductVersion` | Version of the product | `2.1` |
| `/OriginalFilename` | Original file name | `Deploy.ps1` |
| `/Language` | Language identifier or name used by the publisher | `en-US` |
| `/Author` | Author or publishing organization | `Contoso Software` |
| `/PublishTime` | Publishing time value used by the publisher | `2026-10-28T12:00:00Z` |
| `/SourceURL` | Authoritative source location for the file | `https://www.example.com/downloads/Deploy.ps1` |

`/FileDescription` adds a signed metadata attribute. It differs from `/d`, which sets the Authenticode description of the signed content.

## Sign a PowerShell script

1. Open a command prompt where `signtool.exe` is available.

1. Sign and time stamp the script:

   ```console
   signtool sign /a /fd SHA256 /tr http://timestamp.digicert.com /td SHA256 /InternalName "Contoso.Deploy" /FileVersion "2.1.0" /FileDescription "Contoso deployment script" /Product "Contoso Tools" /ProductVersion "2.1" /OriginalFilename "Deploy.ps1" /Language "en-US" /Author "Contoso Software" /PublishTime "2026-10-28T12:00:00Z" /SourceURL "https://www.example.com/downloads/Deploy.ps1" Deploy.ps1
   ```

1. Verify the embedded signature:

   ```console
   signtool verify /pa /v Deploy.ps1
   ```

The verification result confirms the cryptographic signature and certificate policy. It doesn't confirm that a specific application-control product uses every authenticated metadata field.

## Add metadata by OID

Use `/sa` when automation stores metadata as OID-value pairs or when a friendly option isn't appropriate. SignTool encodes each value as an ASN.1 UTF-8 string. Repeat `/sa` to add multiple attributes.

1. Map each value to its OID:

   | Metadata | OID |
   |----------|-----|
   | Internal name | `1.3.6.1.4.1.311.2.7.1` |
   | File version | `1.3.6.1.4.1.311.2.7.2` |
   | File description | `1.3.6.1.4.1.311.2.7.3` |
   | Product | `1.3.6.1.4.1.311.2.7.4` |
   | Product version | `1.3.6.1.4.1.311.2.7.5` |
   | Original file name | `1.3.6.1.4.1.311.2.7.6` |
   | Language | `1.3.6.1.4.1.311.2.7.7` |
   | Author | `1.3.6.1.4.1.311.2.7.8` |
   | Publish time | `1.3.6.1.4.1.311.2.7.9` |
   | Source URL | `1.3.6.1.4.1.311.2.7.10` |

1. Sign the script and repeat `/sa` for each attribute:

   ```console
   signtool sign /a /fd SHA256 /tr http://timestamp.digicert.com /td SHA256 /sa 1.3.6.1.4.1.311.2.7.1 "Contoso.Deploy" /sa 1.3.6.1.4.1.311.2.7.2 "2.1.0" /sa 1.3.6.1.4.1.311.2.7.4 "Contoso Tools" /sa 1.3.6.1.4.1.311.2.7.6 "Deploy.ps1" Deploy.ps1
   ```

1. Verify the signature:

   ```console
   signtool verify /pa /v Deploy.ps1
   ```

## Sign another non-PE file

1. Confirm that a SIP is registered for the file type.

1. Run the same signing command and specify the target file:

   ```console
   signtool sign /a /fd SHA256 /tr http://timestamp.digicert.com /td SHA256 /InternalName "Contoso.Startup" /FileVersion "2.1.0" /Product "Contoso Tools" /ProductVersion "2.1" /OriginalFilename "Startup.js" Startup.js
   ```

1. Verify the signature:

   ```console
   signtool verify /pa /v Startup.js
   ```

If the file type doesn't support an embedded signature, create and sign a catalog that contains the file hash. For the catalog procedure, see [Use SignTool to sign a file](using-signtool-to-sign-a-file.md#sign-and-verify-a-catalog).

## Related content

- [SignTool](signtool.md)
- [Use SignTool to sign a file](using-signtool-to-sign-a-file.md)
- [Use SignTool to verify a file signature](using-signtool-to-verify-a-file-signature.md)
- [Signing files and checking signatures](signing-files-and-checking-signatures.md)
