---
description: When patching files having variable content, it may be necessary to retain selected regions of the target file to prevent the lost of critical information.
ms.assetid: 4a610588-556e-489f-ac14-73e5e6b776fe
title: Patching Selected Regions of a File
ms.topic: article
ms.date: 05/31/2018
---

# Patching Selected Regions of a File

When patching files having variable content, it may be necessary to retain selected regions of the target file to prevent the lost of critical information. For example, some applications stamp user information into the executable file. Because the contents of the target file might depend upon the computer on which the application is installed, it becomes difficult to determine whether a particular file is a valid target for the patch. User information written in the target file can also be overwritten by a patch.

When you generate a patch creation properties (PCP) file with [Msimsp.exe](msimsp-exe.md) and [PATCHWIZ.DLL](patchwiz-dll.md), you can specify that the information in certain regions of the target file be ignored during patching. You can also specify that information in other regions of the target file be retained and copied to an offset location in the updated file. You specify which regions of the target file to ignore and which regions to retain when authoring the [TargetFiles OptionalData](targetfiles-optionaldata-table-patchwiz-dll-.md), [ExternalFiles](externalfiles-table-patchwiz-dll-.md), and [FamilyFileRanges](familyfileranges-table-patchwiz-dll-.md) tables.

Use the RetainOffsets column of the [TargetFiles OptionalData](targetfiles-optionaldata-table-patchwiz-dll-.md) table and the RetainOffsets and RetainLengths columns of the [FamilyFileRanges](familyfileranges-table-patchwiz-dll-.md) table to copy a range of information from the target file to an offset range in the updated file. The information in this range is retained. Specify the length of the range using the RetainLengths columns of the FamilyFileRanges table. The length of the retained range is the same in the target and updated files. Specify the offset of the range in the target file using the RetainOffsets column of the TargetFiles OptionalData table. Specify the offset of the range in the updated file using the RetainOffsets column of the FamilyFileRanges table. The range of the target file retained is therefore the value of RetainOffsets in the TargetFiles OptionalData table plus RetainLengths. This information gets copied to the update file in the range given by the value of RetainOffsets in the FamilyFileRanges tables plus RetainLengths. You can specify multiple ranges but the order of the lengths must match the order of the offsets.

Use the [TargetFiles OptionalData](targetfiles-optionaldata-table-patchwiz-dll-.md) table to ignore a range of the target file. Information in this range of the target file can still be overwritten by the patch. Specify the offset of the range in the IgnoreOffsets column and its length in the IgnoreLengths column. You can specify multiple ranges but the order of the lengths must match the order of the offsets.

The values in the lengths and offsets columns can be decimal or hexadecimal. [PATCHWIZ.DLL](patchwiz-dll.md) treats the value as hexadecimal if it is prefixed by "0x". The columns are string columns, so PATCHWIZ.DLL converts the values to ULONGs. The length column specifies the length in bytes.

 

 



