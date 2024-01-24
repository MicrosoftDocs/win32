---
description: Msistuff.exe is a command line utility that can be used to display or configure the resources in the Setup.exe bootstrap executable.
ms.assetid: df79574c-d0e7-45e3-97c1-d62f700260ce
title: Msistuff.exe
ms.topic: article
ms.date: 05/31/2018
---

# Msistuff.exe

Msistuff.exe is a command line utility that can be used to display or configure the resources in the Setup.exe bootstrap executable.

This tool is only available in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md).

## Syntax

**msistuff setup.exe** *option{value}*

If no data is specified following an option, that resource is removed.

## Command Line Options

Msistuff.exe uses the following case-insensitive command line options. A slash delimiter may also be used in place of a dash. If an option is listed multiple times, only the last occurrence is used.



| Option               | Resource ID                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|----------------------|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| no options specified |                              | Display configurable resources in Setup.exe.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **-u**               | ISETUPPROPNAME\_BASEURL      | Set BaseURL, the base URL location of Setup.exe. If no value is present, the location of Setup.exe defaults to removable media. Only URL based installs are subject to a check with [**WinVerifyTrust**](/windows/win32/api/wintrust/nf-wintrust-winverifytrust). The trailing slash on the URL is optional. This option may be omitted.                                                                                                                                                                                                                     |
| **-d**               | ISETUPPROPNAME\_DATABASE     | Set Msi, the name of the .msi file. This is a relative path to the .msi file in relation to the location of the Setup.exe program. This option is required if the -m option is not specified. The -d and -m options are mutually exclusive. They cannot both be specified.                                                                                                                                                                                                                                                    |
| **-m**               | ISETUPPROPNAME\_PATCH        | Set Msp, the name of the .msp file. This is a relative path to the .msp file in relation to the location of the Setup.exe program. This option is required if the -d option is not specified. The -m and -d options are mutually exclusive. They cannot both be specified.                                                                                                                                                                                                                                                    |
| **-n**               | ISETUPPROPNAME\_PRODUCTNAME  | Set Product Name, the name of the product. This provides the name used in the banner text for the downloaded user interface. This option may be omitted. If omitted, the default is "the product".                                                                                                                                                                                                                                                                                                                            |
| **-o**               | ISETUPPROPNAME\_OPERATION    | Specify the type of operation to perform. The valid values are INSTALL, MINPATCH, MAJPATCH and INSTALLUPD. For additional information on these options, see [Internet Download Bootstrapping](internet-download-bootstrapping.md).                                                                                                                                                                                                                                                                                           |
| **-v**               | ISETUPPROPNAME\_MINIMUM\_MSI | Set Minimum Msi Version, the minimum version of Windows Installer required on the computer. If the minimum version of the Windows Installer is not present on the machine, the appropriate [Instmsi.exe](instmsi-exe.md) is installed to upgrade the Windows Installer. The value of this property has the same format as the PID\_PAGECOUNT value. See [**Page Count Summary**](page-count-summary.md) Property. The value must be at least 200, the value for the Windows Installer version 2.0. This option is required. |
| **-i**               | ISETUPPROPNAME\_INSTLOCATION | Set InstMsi URL Location, the base URL location of Windows Installer upgrade executables. If this value is missing, the location of the upgrade executables defaults to the location of Setup.exe. This option may be omitted.                                                                                                                                                                                                                                                                                                |
| **-a**               | ISETUPPROPNAME\_INSTMSIA     | Set InstMsiA, the name of the ANSI version of Windows Installer upgrade executable. This is a relative path to the ANSI version of Instmsi.exe relative to the location specified by ISETUPPROPNAME\_INSTLOCATION. This option is required.                                                                                                                                                                                                                                                                                   |
| **-w**               | ISETUPPROPNAME\_INSTMSIW     | Set InstMsiW, the name of the Unicode version of Windows Installer upgrade executable. This is a relative path to the Unicode version of Instmsi.exe relative to the location specified by ISETUPPROPNAME\_INSTLOCATION. This option is required.                                                                                                                                                                                                                                                                             |
| **-p**               | ISETUPPROPNAME\_PROPERTIES   | Set the PROPERTY=VALUE strings. These are the PROPERTY=VALUE pairs to include on the command line. This option may be omitted. This option cannot be listed multiple times, and it must be listed last on the command line. All of the command line following -p is considered as a part of the {value}.                                                                                                                                                                                                                      |



 

## Related topics

<dl> <dt>

[Windows Installer Development Tools](windows-installer-development-tools.md)
</dt> <dt>

[Internet Download Bootstrapping](internet-download-bootstrapping.md)
</dt> <dt>

[A URL Based Windows Installer Installation Example](a-url-based-windows-installer-installation-example.md)
</dt> <dt>

[Released Versions, Tools, and Redistributables](released-versions-tools-and-redistributables.md)
</dt> </dl>

 

 
