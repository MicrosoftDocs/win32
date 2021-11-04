---
description: Windows Installer can use digital signatures as a means to detect corrupted resources.
ms.assetid: fc982813-583b-4fcd-88d8-9de227994e7b
title: Msicert.exe
ms.topic: article
ms.date: 05/31/2018
---

# Msicert.exe

Windows Installer can use digital signatures as a means to detect corrupted resources. A signer certificate may be compared to the signer certificate of an external resource to be installed by the package. For more information, see [Digital Signatures and Windows Installer](digital-signatures-and-windows-installer.md).

MsiCert.exe is a command line utility that can be used to populate the [MsiDigitalSignature table](msidigitalsignature-table.md) and [MsiDigitalCertificate table](msidigitalcertificate-table.md) with the digital signature information of an external cabinet file. The cabinet file must by digitally signed and listed in the [Media table](media-table.md). MsiCert.exe uses the signer certificate information from the digitally signed cabinet and will create and add the MsiDigitalSignature and MsiDigitalCertificate tables to the database if they do not already exist.

## Syntax

**msicert -d** *{database}* **-m** *{media entry}* **-c** *{cabinet}* **\[-h\]**

## Command Line Options

The command line options are case-insensitive and slash delimiters may be used instead of a dash.



| Option | Parameter        | Description                                                                                             |
|--------|------------------|---------------------------------------------------------------------------------------------------------|
| -d     | &lt;database&gt; | The database (.msi file) that is being updated.                                                         |
| -m     | <media Id> | The entry in the DiskId field of the [Media table](media-table.md) in the record for the cabinet file. |
| -c     | &lt;cabinet&gt;  | The path to the digitally signed cabinet file.                                                          |
| -h     |                  | Include the hash of the digital signature. This is optional.                                            |



 

This tool is only available in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md).

## Related topics

<dl> <dt>

[Windows Installer Development Tools](windows-installer-development-tools.md)
</dt> <dt>

[Released Versions, Tools, and Redistributables](released-versions-tools-and-redistributables.md)
</dt> </dl>

 

 



