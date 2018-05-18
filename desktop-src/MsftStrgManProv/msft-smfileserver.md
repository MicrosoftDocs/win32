---
title: MSFT\_SMFileServer class
description: Represents a file server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '4c75965b-1d58-4411-ae46-c69e7ba6578e'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_SMFileServer class", "MSFT_SMFileServer class, described"]
topic_type:
- apiref
api_name:
- MSFT_SMFileServer
- MSFT_SMFileServer.ObjectId
- MSFT_SMFileServer.Identifier
- MSFT_SMFileServer.FriendlyName
- MSFT_SMFileServer.Names
- MSFT_SMFileServer.HealthStatus
- MSFT_SMFileServer.OperationalStatus
- MSFT_SMFileServer.OtherOperationalStatusDescription
- MSFT_SMFileServer.SupportsFileShareCreation
- MSFT_SMFileServer.SupportsContinuouslyAvailableFileShare
- MSFT_SMFileServer.FileSharingProtocols
- MSFT_SMFileServer.FileSharingProtocolVersions
api_location:
- StorageService.dll
api_type:
- DllExport
---

# MSFT\_SMFileServer class

Represents a file server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

**Windows Server 2012 R2 and Windows Server 2012:** This class does not inherit from [**MSFT\_SMStorageObject**](msft-smstorageobject.md) which is new for Windows Server 2016.

## Syntax

``` syntax
[dynamic, provider("WMIStorage"), AMENDMENT]
class MSFT_SMFileServer : MSFT_SMStorageObject
{
  String  ObjectId;
  String  Identifier;
  String  FriendlyName;
  String  Names[];
  UInt16  HealthStatus;
  UInt16  OperationalStatus[];
  String  OtherOperationalStatusDescription;
  Boolean SupportsFileShareCreation;
  Boolean SupportsContinuouslyAvailableFileShare;
  uint16  FileSharingProtocols[];
  string  FileSharingProtocolVersions[];
};
```

## Members

The **MSFT\_SMFileServer** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_SMFileServer** class has these methods.



| Method                                                       | Description                      |
|:-------------------------------------------------------------|:---------------------------------|
| [**CreateFileShare**](createfileshare-msft-smfileserver.md) | Creates a file share.<br/> |



 

### Properties

The **MSFT\_SMFileServer** class has these properties.

<dl> <dt>

**FileSharingProtocols**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array that contains indicators of the file sharing protocols that are supported by the file server.

The possible values are.

<dt>

<span id="NFS"></span><span id="nfs"></span>

**NFS** (2)


</dt> <dd></dd> <dt>

<span id="SMB"></span><span id="smb"></span>

**SMB** (3)


</dt> <dd></dd> </dl>

</dd> <dt>

**FileSharingProtocolVersions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array that contains the version numbers of the files sharing protocols that are specified in **FileSharingProtocols**.

</dd> <dt>

**FriendlyName**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

A user-friendly string representing the name of the file server.

</dd> <dt>

**HealthStatus**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed")
</dt> </dl>

The current status of the file server.

The possible values are.

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

**Names**
</dt> <dd> <dl> <dt>

Data type: **String** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

An array that contains the names by which the file server is accessible on the network.

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

**OperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **UInt16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array that contains indicators to the operational status of the file server.

</dd> <dt>

**OtherOperationalStatusDescription**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string representation of the vendor defined operational status when the **OperationalStatus** property is **Other**.

</dd> <dt>

**SupportsContinuouslyAvailableFileShare**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**True** if the server supports continuously available file shares; otherwise, **False**.

</dd> <dt>

**SupportsFileShareCreation**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**True** if the server supports file share creation; otherwise, **False**.

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

 

 





