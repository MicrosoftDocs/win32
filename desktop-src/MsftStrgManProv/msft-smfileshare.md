---
title: MSFT\_SMFileShare class
description: Represents a file share.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'acd8a570-8c02-47e3-9435-1909bd8894d9'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_SMFileShare class", "MSFT_SMFileShare class, described"]
topic_type:
- apiref
api_name:
- MSFT_SMFileShare
- MSFT_SMFileShare.ObjectId
- MSFT_SMFileShare.Identifier
- MSFT_SMFileShare.Name
- MSFT_SMFileShare.Description
- MSFT_SMFileShare.Path
- MSFT_SMFileShare.IsContinuouslyAvailable
- MSFT_SMFileShare.FileSharingProtocol
- MSFT_SMFileShare.State
- MSFT_SMFileShare.DefaultReadWrite
- MSFT_SMFileShare.HealthStatus
- MSFT_SMFileShare.HealthStatusDescription
api_location:
- StorageService.dll
api_type:
- DllExport
---

# MSFT\_SMFileShare class

Represents a file share.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

**Windows Server 2012 R2 and Windows Server 2012:** This class does not inherit from [**MSFT\_SMStorageObject**](msft-smstorageobject.md) which is new for Windows Server 2016.

## Syntax

``` syntax
[dynamic, provider("WMIStorage"), AMENDMENT]
class MSFT_SMFileShare : MSFT_SMStorageObject
{
  String  ObjectId;
  String  Identifier;
  String  Name;
  String  Description;
  String  Path;
  Boolean IsContinuouslyAvailable;
  UInt16  FileSharingProtocol;
  UInt16  State;
  UInt16  DefaultReadWrite;
  uint16  HealthStatus;
  string  HealthStatusDescription;
};
```

## Members

The **MSFT\_SMFileShare** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_SMFileShare** class has these methods.



| Method                                                | Description                                                          |
|:------------------------------------------------------|:---------------------------------------------------------------------|
| [**Delete**](delete-msft-smfileshare.md)             | Deletes a file share.<br/>                                     |
| [**Diagnose**](diagnose-msft-smfileshare.md)         | Runs diagnostics on the file share.<br/>                       |
| [**GrantAccess**](grantaccess-msft-smfileshare.md)   | Grants the specified users access to the file share.<br/>      |
| [**RevokeAccess**](revokeaccess-msft-smfileshare.md) | Revokes access to the file share for the specified users.<br/> |



 

### Properties

The **MSFT\_SMFileShare** class has these properties.

<dl> <dt>

**DefaultReadWrite**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

An indicator of the default read/write setting for the file share.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user configurable description of the file share.

</dd> <dt>

**FileSharingProtocol**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The file sharing protocol used by the share.

The possible values are.

<dt>

<span id="NFS"></span><span id="nfs"></span>

**NFS** (2)


</dt> <dd></dd> <dt>

<span id="SMB"></span><span id="smb"></span>

**SMB** (3)


</dt> <dd></dd> </dl>

</dd> <dt>

**HealthStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed")
</dt> </dl>

Indicates the current status of the file share. Various operational statuses are defined.

<dt>

<span id="Healthy"></span><span id="healthy"></span><span id="HEALTHY"></span>

**Healthy** (0)


</dt> <dd></dd> <dt>

<span id="Warning"></span><span id="warning"></span><span id="WARNING"></span>

**Warning** (1)


</dt> <dd></dd> <dt>

<span id="Unhealthy"></span><span id="unhealthy"></span><span id="UNHEALTHY"></span>

**Unhealthy** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**HealthStatusDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the current status of the file share in a string format.

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

**Windows Server 2012 R2 and Windows Server 2012:** This property is present, but is not inherited from [**MSFT\_SMStorageObject**](msft-smstorageobject.md) .

</dd> <dt>

**IsContinuouslyAvailable**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the file server is continuously available.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

A human-readable string used to identify the file share. This name must be unique within the scope of the owning file server.

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

**Windows Server 2012 R2 and Windows Server 2012:** This property is present, but is not inherited from [**MSFT\_SMStorageObject**](msft-smstorageobject.md) .

</dd> <dt>

**Path**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The volume-relative path to the directory that is shared.

</dd> <dt>

**State**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

An indicator of the state of the file share.

<dl><span id="Pending"></span><span id="pending"></span><span id="PENDING"></span><dt>

**Pending**
</dt><span id="Online"></span><span id="online"></span><span id="ONLINE"></span><dt>

**Online**
</dt><span id="Offline"></span><span id="offline"></span><span id="OFFLINE"></span><dt>

**Offline**
</dt> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_SMStorageObject**](msft-smstorageobject.md)
</dt> <dt>

[Windows Storage Management WMI Provider](windows-storage-management-wmi-provider-portal.md)
</dt> </dl>

 

 





