---
description: In the summary information of an installation package, the Word Count Summary property indicates the type of source file image.
ms.assetid: 1eeece25-4f24-4efe-879d-66ebbb6a9391
title: Word Count Summary property
ms.topic: reference
ms.date: 05/31/2018
---

# Word Count Summary property

In the summary information of an installation package, the **Word Count Summary** property indicates the type of source file image. If this property is not present, it defaults to zero (0).

This property is a bit field. New bits may be added in the future. At present the following bits are available.



| Bit   | Value          | Description                                                                                                                                                                                                                                      |
|-------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bit 0 | 0 1<br/> | Long file names. Short file names.<br/>                                                                                                                                                                                                    |
| Bit 1 | 0 2<br/> | Source is uncompressed. Source is compressed.<br/>                                                                                                                                                                                         |
| Bit 2 | 0 4<br/> | Source is original media. Source is a administrative image created by an administrative installation.<br/>                                                                                                                                 |
| Bit 3 | 0 8<br/> | Elevated privileges can be required to install this package. Elevated privileges are not required to install this package.<br/> Available starting with Windows Installer version 4.0 and Windows Vista or Windows Server 2008.<br/> |



 

These are combined to give the **Word Count Summary** property one of the following values that indicate a type of source file image.



| Value | Type                                                                                                                                                                                                                                                                                            |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0     | Original source using long file names. Matches tree in [Directory Table](directory-table.md). Elevated privileges can be required to install this package.                                                                                                                                     |
| 1     | Original source using short file names. Matches tree in [Directory Table](directory-table.md). Elevated privileges can be required to install this package.                                                                                                                                    |
| 2     | Compressed source files using long file names. Matches cabinets and files in the [Media Table](media-table.md). Elevated privileges can be required to install this package.                                                                                                                   |
| 3     | Compressed source files using short file names. Matches cabinets and files in the [Media Table](media-table.md). Elevated privileges can be required to install this package.                                                                                                                  |
| 4     | Administrative image using long file names. Matches tree in [Directory Table](directory-table.md). Elevated privileges can be required to install this package.                                                                                                                                |
| 5     | Administrative image using short file names. Matches tree in [Directory Table](directory-table.md). Elevated privileges can be required to install this package.                                                                                                                               |
| 8     | Elevated privileges are not required to install this package. Use this value when [Authoring Packages without the UAC Dialog Box](authoring-packages-without-the-uac-dialog-box.md).Available starting with Windows Installer version 4.0 and Windows Vista or Windows Server 2008.<br/> |



 

Note that if the package is marked as compressed (Bit 1 is set), the Windows Installer only installs files located at the root of the source. In this case, even files marked as uncompressed in the [File Table](file-table.md) must be located at the root to be installed. To specify a source image that has both a cabinet file (compressed files) and uncompressed files that match the tree in the [Directory Table](directory-table.md), mark the package as uncompressed by leaving Bit 1 unset (value=0) in the **Word Count Summary** property and set **msidbFileAttributesCompressed** (value=16384) in the Attributes column of the [File Table](file-table.md) for each file in the cabinet.

In a transform, the **Word Count Summary** property should be Null.

In the summary information stream of a patch package, the **Word Count Summary** property indicates the minimum Windows Installer version that is required to install the patch.



| Value | Meaning                                                                                                                                                                              |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | The default value, which indicates that MSPATCH was used to create the patch.                                                                                                        |
| 2     | Requires at minimum Windows Installer 1.2 for the patch to be applied. A patch with a Word Count of "2" fails immediately if used with a Windows Installer version earlier than 1.2. |
| 3     | Requires at minimum Windows Installer 2.0 for the patch to be applied. A patch with a Word Count of "3" fails immediately if used with a Windows Installer version earlier than 2.0. |
| 4     | Requires at minimum Windows Installer 3.0 for the patch to be applied. A patch with a Word Count of "4" fails if used with a Windows Installer version earlier than 3.0.             |
| 5     | Requires at minimum Windows Installer 3.1 for the patch to be applied.                                                                                                               |



 

This summary property is REQUIRED.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |



## See also

<dl> <dt>

[Summary Property Descriptions](summary-property-descriptions.md)
</dt> </dl>

 

 




