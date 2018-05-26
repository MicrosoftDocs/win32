---
title: MSFT\_SMReplicaPeer class
description: Represents a replica peer, which is an object that has a replication relationship in the subsystem.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a15c5ed5-73e3-4c06-a378-bce4e7dea5d2
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_SMReplicaPeer class
- MSFT_SMReplicaPeer class, described
topic_type:
- apiref
api_name:
- MSFT_SMReplicaPeer
- MSFT_SMReplicaPeer.ObjectId
- MSFT_SMReplicaPeer.Identifier
- MSFT_SMReplicaPeer.PeerObjectType
- MSFT_SMReplicaPeer.PeerObjectId
- MSFT_SMReplicaPeer.PeerObjectName
- MSFT_SMReplicaPeer.PeerUniqueId
- MSFT_SMReplicaPeer.PeerSystemName
- MSFT_SMReplicaPeer.PeerProviderURI
- MSFT_SMReplicaPeer.IsCIMReplicationEntityBased
- MSFT_SMReplicaPeer.IsPrimary
- MSFT_SMReplicaPeer.Element
api_location:
- StorageService.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_SMReplicaPeer class

Represents a replica peer, which is an object that has a replication relationship in the subsystem.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("WMIStorage"), AMENDMENT]
class MSFT_SMReplicaPeer : MSFT_SMStorageObject
{
  String               ObjectId;
  String               Identifier;
  UInt16               PeerObjectType;
  String               PeerObjectId;
  String               PeerObjectName;
  String               PeerUniqueId;
  String               PeerSystemName;
  String               PeerProviderURI;
  Boolean              IsCIMReplicationEntityBased;
  Boolean              IsPrimary;
  MSFT_SMStorageObject Element;
};
```

## Members

The **MSFT\_SMReplicaPeer** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SMReplicaPeer** class has these properties.

<dl> <dt>

**Element**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_SMStorageObject**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("MSFT\_SMReplicaPeer.PeerObjectType")
</dt> </dl>

The storage object that indicates the object type of the replica peer when the **PeerObjectType** property is set to "Embedded Instance".

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

</dd> <dt>

**IsCIMReplicationEntityBased**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the origin of the replication.

</dd> <dt>

**IsPrimary**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**True** of the replica peer is a primary replica; otherwise, **False**.

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

</dd> <dt>

**PeerObjectId**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The object ID of the replica peer.

</dd> <dt>

**PeerObjectName**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the replica peer within the storage subsystem.

</dd> <dt>

**PeerObjectType**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The object type of the replica peer.

The possible values are:

<dt>

<span id="StorageVolume"></span><span id="storagevolume"></span><span id="STORAGEVOLUME"></span>

**StorageVolume** (4)


</dt> <dd></dd> <dt>

<span id="Volume"></span><span id="volume"></span><span id="VOLUME"></span>

**Volume** (5)


</dt> <dd></dd> <dt>

<span id="Reserved"></span><span id="reserved"></span><span id="RESERVED"></span>

**Reserved**


</dt> <dd>6 32767</dd> <dt>

<span id="Partition"></span><span id="partition"></span><span id="PARTITION"></span>

**Partition** (32768)


</dt> <dd></dd> <dt>

<span id="ReplicationGroup"></span><span id="replicationgroup"></span><span id="REPLICATIONGROUP"></span>

**ReplicationGroup** (32769)


</dt> <dd></dd> <dt>

<span id="StorageSystem"></span><span id="storagesystem"></span><span id="STORAGESYSTEM"></span>

**StorageSystem** (32770)


</dt> <dd></dd> </dl>

</dd> <dt>

**PeerProviderURI**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The URI of the SMI-S provider. The URI includes the protocol, computer host name, and port of the SMI-S server.

</dd> <dt>

**PeerSystemName**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The subsystem name of the replica peer within the storage subsystem.

</dd> <dt>

**PeerUniqueId**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The unique ID of the replica peer within the storage subsystem.

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

 

 





