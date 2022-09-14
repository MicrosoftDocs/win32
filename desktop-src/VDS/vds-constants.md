---
description: VDS Constants
ms.assetid: a3a8b549-51bc-48eb-9215-04c7311e03a3
title: VDS Constants
ms.topic: article
ms.date: 05/31/2018
---

# VDS Constants

\[Beginning with Windows 8 and Windows Server 2012, the [Virtual Disk Service](virtual-disk-service-portal.md) COM interface is superseded by the [Windows Storage Management API](/previous-versions/windows/desktop/stormgmt/windows-storage-management-api-portal).\]

VDS constants are categorized as follows:

-   [Object Status Constants](#object-status-constants)
-   [Automagic Hints Constants](#automagic-hints-constants)
-   [Miscellaneous Constants](#miscellaneous-constants)

### Object Status Constants



| Constant           | Value |
|--------------------|-------|
| STATUS\_UNKNOWN    | 0     |
| STATUS\_ONLINE     | 1     |
| STATUS\_NOT\_READY | 2     |
| STATUS\_NO\_MEDIA  | 3     |
| STATUS\_OFFLINE    | 4     |
| STATUS\_FAILED     | 5     |
| STATUS\_MISSING    | 6     |



 

### Automagic Hints Constants



| Constant                               | Value   |
|----------------------------------------|---------|
| VDS\_HINT\_MOSTLYREADS                 | 0x0002L |
| VDS\_HINT\_OPTIMIZEFORSEQUENTIALREADS  | 0x0004L |
| VDS\_HINT\_OPTIMIZEFORSEQUENTIALWRITES | 0x0008L |
| VDS\_HINT\_REMAPENABLED                | 0x0020L |
| VDS\_HINT\_WRITETHROUGHCACHINGENABLED  | 0x0040L |
| VDS\_HINT\_HARDWARECHECKSUMENABLED     | 0x0080L |
| VDS\_HINT\_ISYANKABLE                  | 0x0100L |



 

### Miscellaneous Constants



| Constant                     | Value      |
|------------------------------|------------|
| VDS\_REBUILD\_PRIORITY\_MIN  | 0x0001L    |
| VER\_VDS\_LUN\_INFORMATION   | 1          |
| MAX\_COMPUTERNAME\_LENGTH    | 15         |
| MAX\_PROVIDERNAME\_LENGTH    | 200        |
| MAX\_VERSIONSTRING\_LENGTH   | 16         |
| DRIVE\_LETTER\_PROP          | N/A        |
| MAX\_FS\_NAME\_SIZE          | 8          |
| INVALID\_MEMBER\_IDX         | 0xFFFFFFFF |
| GPT\_PARTITION\_NAME\_LENGTH | 36         |
| MAX\_PATH                    | 260        |



 

## Related topics

<dl> <dt>

[VDS Reference](vds-reference.md)
</dt> </dl>

 

 
