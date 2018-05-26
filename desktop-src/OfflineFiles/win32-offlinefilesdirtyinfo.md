---
Description: Describes the amount of information that will be synchronized when an item is synchronized.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4595f418-d838-4095-98e6-c9b9be40951e
ms.prod: windows-server-dev
ms.technology: offline-files
ms.tgt_platform: multiple
title: Win32\_OfflineFilesDirtyInfo class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Win32\_OfflineFilesDirtyInfo class

Describes the amount of information that will be synchronized when an item is synchronized.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("Win32_OfflineFilesProvider"), AMENDMENT]
class Win32_OfflineFilesDirtyInfo
{
  sint64 LocalDirtyByteCount;
  sint64 RemoteDirtyByteCount;
};
```

## Members

The **Win32\_OfflineFilesDirtyInfo** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_OfflineFilesDirtyInfo** class has these properties.

<dl> <dt>

**LocalDirtyByteCount**
</dt> <dd> <dl> <dt>

Data type: **sint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of bytes needing synchronization from the client to the server.

</dd> <dt>

**RemoteDirtyByteCount**
</dt> <dd> <dl> <dt>

Data type: **sint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of bytes needing synchronization from the server to the client.

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Namespace<br/>                | ROOT\\CIMV2<br/>                                                                                 |
| MOF<br/>                      | <dl> <dt>Offlinefileswmiprovider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CscObj.dll</dt> </dl>                  |



 

 




