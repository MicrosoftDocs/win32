---
description: A Cyclic Redundancy Check (CRC) of files is available with Windows Installer.
ms.assetid: c895488b-6e60-4175-8865-4ba4b0cb2d9a
title: CRC Checking During an Installation
ms.topic: article
ms.date: 05/31/2018
---

# CRC Checking During an Installation

A Cyclic Redundancy Check (CRC) of files is available with Windows Installer. CRC checking is an error-checking mechanism, similar to a checksum, that enables an application to determine whether the information in a file has been modified. After the Windows Installer finishes copying a file, it gets a CRC value from both the source and destination files. The installer checks the original CRC stamped into the file and compares this to the CRC calculated from the copy. The CRC check fails if the original CRC value is non-null and is different from the CRC calculated on the copy. If the original CRC is null, no check occurs.

The Windows Installer does a CRC check on a file in the following cases:

-   If the [MSICHECKCRCS property](msicheckcrcs.md) is set and **msidbFileAttributesChecksum** is included in the Attributes field of the file's record in the [File table](file-table.md). The installer does the CRC check once after installing, duplicating, or moving the file.
-   If the [MSICHECKCRCS property](msicheckcrcs.md) is set and **msidbFileAttributesChecksum** is included in the Attributes field of the file's record in the [File table](file-table.md), the installer does a CRC check after patching the file.
-   If the **msidbFileAttributesChecksum** is included in the Attributes field of the file's record in the [File table](file-table.md), the installer does a CRC check before binding images.

If the check fails before binding an image, the installer reports the following two errors in the log file and continues the installation without binding the file.



| Code | Message                                               |
|------|-------------------------------------------------------|
| 2941 | Unable to compute the CRC for file \[2\].             |
| 2942 | BindImage action has not been executed on \[2\] file. |



 

If the check fails after an uncompressed file had been copied, duplicated, or patched, the installer reports the following error. This error is also reported if the check fails after a compressed file is copied. If the file has the **msidbFileAttributesVital** attribute, the file is considered vital to the installation and the user gets the option to retry or cancel the installation. If the file is marked as nonvital in the Attributes column of the [File table](file-table.md), the user may ignore the error and continue, retry, or cancel the installation.



| Code | Message                                         |
|------|-------------------------------------------------|
| 1331 | Failed to correctly copy \[2\] file: CRC error. |



 

Note that only uncompressed files are moved. If the check fails after an uncompressed file is moved, the installer displays the following error. If the file has the **msidbFileAttributesVital** attribute, the file is considered vital to the installation and the installation fails. If the file is marked as nonvital in the Attributes column of the [File table](file-table.md), the user gets the option to cancel or to ignore the error and continue the installation.



| Code | Message                                         |
|------|-------------------------------------------------|
| 1332 | Failed to correctly move \[2\] file: CRC error. |



 

If the check fails after an uncompressed file is patched, the installer displays the following error. If the file has the **msidbFileAttributesVital** attribute, the file is considered vital to the installation and the installation fails. If the file is marked as nonvital in the Attributes column of the [File table](file-table.md), the user gets the option to cancel or to ignore the error and continue the installation.



| Code | Message                                          |
|------|--------------------------------------------------|
| 1333 | Failed to correctly patch \[2\] file: CRC error. |



 

 

 



