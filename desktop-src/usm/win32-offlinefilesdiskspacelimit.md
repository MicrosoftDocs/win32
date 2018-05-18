---
title: Win32\_OfflineFilesDiskSpaceLimit class
description: Represents the maximum disk space that can be used by the Offline Files feature.
ms.assetid: 'cf0a6e0c-799f-4417-a1d4-0afcfbb77883'
keywords: ["Win32_OfflineFilesDiskSpaceLimit class User State Manageability API", "Win32_OfflineFilesDiskSpaceLimit class User State Manageability API , described"]
topic_type:
- apiref
api_name:
- Win32_OfflineFilesDiskSpaceLimit
- Win32_OfflineFilesDiskSpaceLimit.TotalSizeInMB
- Win32_OfflineFilesDiskSpaceLimit.AutoCacheSizeInMB
api_location:
- Root\CIMv2
api_type:
- Schema
---

# Win32\_OfflineFilesDiskSpaceLimit class

Represents the maximum disk space that can be used by the Offline Files feature.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class Win32_OfflineFilesDiskSpaceLimit
{
  uint32 TotalSizeInMB;
  uint32 AutoCacheSizeInMB;
};
```

## Members

The **Win32\_OfflineFilesDiskSpaceLimit** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_OfflineFilesDiskSpaceLimit** class has these properties.

<dl> <dt>

**AutoCacheSizeInMB**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **Max** (100000000)
</dt> </dl>

The maximum total size, in megabytes (MB), of all files that reside on network shares and are marked to be cached automatically, that can be cached by the Offline Files feature.

</dd> <dt>

**TotalSizeInMB**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **Max** (100000000)
</dt> </dl>

The total amount of disk space, in megabytes (MB), that can be used by the Offline Files feature.

</dd> </dl>

## Requirements



|                                     |                                                                                                                     |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2<br/>                                                                                              |
| MOF<br/>                      | <dl> <dt>OfflineFilesConfigurationWmiProvider.mof</dt> </dl> |



 

 





