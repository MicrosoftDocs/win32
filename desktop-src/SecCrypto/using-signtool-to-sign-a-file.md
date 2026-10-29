---
description: Use SignTool to digitally sign and time stamp executable files, scripts, catalogs, and other supported file types.
ms.assetid: fa8ee4d3-8927-4f7d-a09e-dbcf75a164d3
title: Use SignTool to sign a file
ms.topic: how-to
ms.date: 10/28/2026
# customer intent: As a Windows developer, I want to sign every executable artifact that I distribute so that customers can verify its publisher and integrity.
---

# Use SignTool to sign a file

Use SignTool to digitally sign and time stamp the executable artifacts that your application builds, installs, downloads, or runs. These artifacts can include executable files, DLLs, installers, scripts, modules, plug-ins, helper tools, update components, uninstallers, and catalog files. Signing lets Windows and customers verify the publisher and detect changes made after signing.

Sign every supported executable artifact instead of signing only the primary executable or installer. For scripts and other files that don't contain PE version resources, add authenticated metadata so that application-control systems can identify the file by its name, product, and version.

## Prerequisites

- SignTool from the [Windows SDK](https://developer.microsoft.com/windows/downloads/windows-sdk).
- A code-signing certificate and access to its private key. Keep private keys in a protected certificate store, hardware security module, or managed signing service.
- An RFC 3161 time stamp service if signatures must remain verifiable after the signing certificate expires.
- Windows SDK build 10.0.25231.0 or later to use the named authenticated metadata options for scripts and non-PE files.

## Sign and time stamp a file

The following procedure automatically selects an eligible code-signing certificate from the current user's `My` certificate store and applies an RFC 3161 time stamp.

1. Open a command prompt where `signtool.exe` is available.

1. Sign the file by using SHA256 for the file digest and time stamp digest:

   ```console
   signtool sign /a /fd SHA256 /tr http://timestamp.digicert.com /td SHA256 MyApplication.exe
   ```

1. Verify the signature by using the default Authenticode verification policy:

   ```console
   signtool verify /pa /v MyApplication.exe
   ```

SignTool returns exit code `0` for success, `1` for failure, and `2` when the operation completes with warnings. Treat warnings as failures in release automation unless the warning is explicitly reviewed and accepted.

## Select a signing certificate

Choose one certificate-selection method for each signing operation.

### Select a certificate automatically

Use `/a` when the certificate store contains only certificates that are appropriate for the release:

```console
signtool sign /a /fd SHA256 MyApplication.exe
```

### Select a certificate by subject name

Use `/n` to select a certificate from the current user's `My` store by subject name:

```console
signtool sign /n "Contoso Software" /fd SHA256 MyApplication.exe
```

Use `/sm` to search the local computer certificate store instead:

```console
signtool sign /sm /n "Contoso Software" /fd SHA256 MyApplication.exe
```

### Select a certificate by SHA1 thumbprint

Use `/sha1` when multiple certificates have similar subject names:

```console
signtool sign /sha1 certificate-thumbprint /fd SHA256 MyApplication.exe
```

### Use a certificate file

Use `/f` to specify a PFX file:

```console
signtool sign /f MySigningCertificate.pfx /fd SHA256 MyApplication.exe
```

If the PFX file has a password, `/p` supplies it to SignTool. Avoid exposing passwords in command history, logs, response files, or build arguments. Prefer a protected certificate store, hardware-backed key, or managed signing service for production signing.

### Use a hardware-backed private key

If the certificate is installed and its private key is managed by a cryptographic provider, select the certificate from the store:

```console
signtool sign /n "Contoso Hardware-Protected Certificate" /fd SHA256 MyApplication.exe
```

If the certificate file doesn't contain the private key, use `/csp` and `/kc` to specify the cryptographic service provider and private key container:

```console
signtool sign /f ContosoSigning.cer /csp "Contoso Cryptographic Provider" /kc "ContosoSigningKey" /fd SHA256 MyApplication.exe
```

## Sign scripts and non-PE files

SignTool uses the SIP registered for a file type to create an embedded signature. For scripts and other non-PE files, add authenticated metadata to provide file identity and version information that would otherwise come from PE version resources.

For the complete procedure and metadata recommendations, see [Sign scripts and non-PE files with SignTool](sign-scripts-and-non-pe-files.md).

## Sign and verify a catalog

A signed catalog can protect a collection of files without modifying each file. Catalogs are useful when files don't support embedded signatures or when an existing application can't be rebuilt to add signatures. The catalog must be regenerated and signed whenever a covered file changes.

1. Create a catalog that contains the hashes of the files. For more information, see [MakeCat](makecat.md).

1. Sign and time stamp the catalog:

   ```console
   signtool sign /a /fd SHA256 /tr http://timestamp.digicert.com /td SHA256 MyApplication.cat
   ```

1. Verify the catalog signature:

   ```console
   signtool verify /pa /v MyApplication.cat
   ```

1. Verify a file against the signed catalog:

   ```console
   signtool verify /pa /c MyApplication.cat MyScript.ps1
   ```

Catalog trust also depends on certificate trust and how the catalog is registered or deployed on the destination device. A catalog signature isn't a universal replacement for embedded signing on unmanaged devices.

## Automate signing with a response file

Response files keep long SignTool commands consistent across build and release jobs. Don't store passwords or other secrets in a response file.

1. Create a file named `signing-commands.txt` that contains one argument per line:

   ```text
   sign
   /n "Contoso Software"
   /fd SHA256
   /tr http://timestamp.digicert.com
   /td SHA256
   MyApplication.exe

   verify
   /pa
   /v
   MyApplication.exe
   ```

1. Run the commands:

   ```console
   signtool @signing-commands.txt
   ```

## Related content

- [SignTool](signtool.md)
- [Sign scripts and non-PE files with SignTool](sign-scripts-and-non-pe-files.md)
- [Use SignTool to verify a file signature](using-signtool-to-verify-a-file-signature.md)
- [Add time stamps to previously signed files](adding-time-stamps-to-previously-signed-files.md)
