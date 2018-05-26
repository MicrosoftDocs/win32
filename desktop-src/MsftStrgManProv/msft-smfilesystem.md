---
title: MSFT\_SMFileSystem class
description: Represents a file system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6fe5cd14-08c4-426b-8b26-72dd64efa985
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_SMFileSystem class
- MSFT_SMFileSystem class, described
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_SMFileSystem class

Represents a file system.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

**Windows Server 2012 R2 and Windows Server 2012:** This class does not inherit from [**MSFT\_SMStorageObject**](msft-smstorageobject.md) which is new for Windows Server 2016.

## Syntax

``` syntax
[dynamic, provider("WMIStorage"), AMENDMENT]
class MSFT_SMFileSystem : MSFT_SMStorageObject
{
  String  ObjectId;
  String  Identifier;
  UInt16  HealthStatus;
  String  FileSystem;
  String  Name;
  String  FriendlyName;
  UInt64  Size;
  UInt64  SizeRemaining;
  Boolean IsReadOnly;
  UInt16  FileSystemType;
  Boolean IsDeduplicationEnabled;
  UInt16  DeduplicationWorkload;
};
```

## Members

The **MSFT\_SMFileSystem** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_SMFileSystem** class has these methods.



| Method                                             | Description                                     |
|:---------------------------------------------------|:------------------------------------------------|
| [**Delete**](delete-msft-smfilesystem.md)         | Deletes the file system.<br/>             |
| [**Diagnose**](diagnose-msft-smfilesystem.md)     | Runs diagnostics on the file system.<br/> |
| [**ModifySize**](modifysize-msft-smfilesystem.md) | Resizes the file system.<br/>             |



 

### Properties

The **MSFT\_SMFileSystem** class has these properties.

<dl> <dt>

**DeduplicationWorkload**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The de-duplication workload for the volume.

The possible values are.

<dt>

<span id="VDI"></span><span id="vdi"></span>

**VDI** (1)


</dt> <dd></dd> <dt>

<span id="GPFS"></span><span id="gpfs"></span>

**GPFS** (2)


</dt> <dd></dd> <dt>

<span id="Custom"></span><span id="custom"></span><span id="CUSTOM"></span>

**Custom** (32768)


</dt> <dd></dd> </dl>

</dd> <dt>

**FileSystem**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> <dt>

**FileSystemType**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The underlying file system on the volume.

</dd> <dt>

**FriendlyName**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The user-friendly name of the file system.

</dd> <dt>

**HealthStatus**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the health status of the file system.

</dd> <dt>

**Identifier**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The ID of the logical instance of the object. This ID must be unique within the scope of the storage system.

This property is inherited from [**MSFT\_SMStorageObject**](msft-smstorageobject.md).

**Windows Server 2012 R2 and Windows Server 2012:** This property is present, but is not inherited from [**MSFT\_SMStorageObject**](msft-smstorageobject.md) .

</dd> <dt>

**IsDeduplicationEnabled**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**True** if de-duplication is enabled on the volume; otherwise, **False**.

</dd> <dt>

**IsReadOnly**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**True** the volume is read only; otherwise, **False**.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The label of the file system.

</dd> <dt>

**ObjectId**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The ID of this class instance. This ID must be unique within the scope of the Windows Storage Management server that hosts the provider object.

This property is inherited from [**MSFT\_SMStorageObject**](msft-smstorageobject.md).

**Windows Server 2012 R2 and Windows Server 2012:** This property is present, but is not inherited from [**MSFT\_SMStorageObject**](msft-smstorageobject.md) .

</dd> <dt>

**Size**
</dt> <dd> <dl> <dt>

Data type: **UInt64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total size of the file system, in bytes.

</dd> <dt>

**SizeRemaining**
</dt> <dd> <dl> <dt>

Data type: **UInt64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The unused size of the unused portion of file system, in bytes.

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_SMStorageObject**](msft-smstorageobject.md)
</dt> <dt>

[Windows Storage Management WMI Provider](windows-storage-management-wmi-provider-portal.md)
</dt> </dl>

 

 





