---
description: Notes about the use of Authenticode signing of executable files
ms.assetid: df71ff3b-2bed-4089-bbf7-2d2509182f92
title: Best Practices for the Security APIs
ms.topic: best-practice
ms.date: 07/24/2025
---
# Understanding Executable File Signing
In Windows, a file’s digital signature may be stored in either a catalog signature, an embedded signature, or both. Catalog Signatures are
files that contain signatures for one or more other files, while embedded signatures are stored in file-format-specific structures that allow
embedding a signature within the bytes of the file itself. For example, the Windows [Portable Executable (PE) File Format](/windows/win32/debug/pe-format)
allows embedding a Certificate Table in the Data directory section; the signature data contains signed hashes of the code components of the file.

## Signature Calculations
The specific bytes protected by a file’s signature vary based upon the Subject Interface Package (SIP) used to generate and later verify a
signature for a given file type. Windows’ signing infrastructure is extensible, allowing third-parties to [register additional SIPs](/windows/win32/api/mssip/) to support
signing of additional file types beyond the signable formats included by Windows.

In the case of file types for which no SIP is installed, the entire content of the file may be hashed (as in the case of a text file) and
stored in a Catalog file.

For filetypes that are supported by a SIP, like Windows Portable Executable (PE) files, the SIP may exclude some sections of the file from
the hash calculation, and may store the resulting signature within the file itself or within a separate Catalog file. In a Windows PE file,
digital signatures can be "embedded" in a location specified by the Certificate Table entry in Optional Header Data Directories. When
Authenticode is used to sign a Windows PE file, the algorithm that calculates the file's hash value excludes certain PE fields. When embedding
the signature in the file, the signing process can modify these fields without affecting the file's hash value.

After the to-be-signed content’s hash is generated, it is signed using a signing certificate, allowing future validation that the hash is
unmodified and that the hashed portion of the file's content remains unchanged since signing.

## Security Implications
The Software Publisher Trust Provider SIP for PE files hashes the executable content of the file, but necessarily omits the file’s checksum
(which changes when a signature is embedded) and the Certificate Table directory (which is populated by the file’s signatures during signing).
 
The fact that the Software Publisher Trust Provider SIP does not hash all of the bytes of the file (i.e. it’s not a “flat file hash”) when 
calculating the signature means that it is possible to embed additional content into a signed PE file without breaking its signature. For
example, some services will [embed metadata into already-signed](/archive/blogs/ieinternals/caveats-for-authenticode-code-signing) software installers,
either by storing the metadata in an PKCS#7 padding area in the WIN_CERTIFICATE structure, by adding unvalidated attributes to a signature,
or by adding an extra signature signed with a self-signed certificate. Each of these techniques introduces risk. While the injected content
is not directly executable, a vulnerable application might incorrectly expect it to be trustworthy (because the rest of the file is correctly
signed) and act upon it.

This unsigned-embedding capability was exploited in attacks dating back to 2013, leading to the introduction of the [`EnableCertPaddingCheck`](/security-updates/SecurityAdvisories/2014/2915720)
registry override introduced for CVE-2013-3900. When the EnableCertPaddingCheck DWORD is present and set to 1, 
[WinVerifyTrust](/windows/win32/api/wintrust/nf-wintrust-winverifytrust) will validate that all PKCS#7 padding bytes in the WIN_CERTIFICATE
structure are set to 0. If other values are found, the SIP will deem the signature invalid. 

## Notes on Catalog Signatures
Catalog signature verification does not support every SIP. When verifying a Catalog-signed file, the SIP is loaded only for signing
and validating the PE and CAB file types. Other file types are signed and validated using a flat file hash.

Enabling the EnableCertPaddingCheck registry key does not impact WinVerifyTrust’s evaluation of a Catalog-signed PE file. If an executable
file is Catalog-signed, the embedded signature is not checked and thus the certificate padding is not evaluated for unexpected content
even when the EnableCertPaddingCheck registry key is set.
