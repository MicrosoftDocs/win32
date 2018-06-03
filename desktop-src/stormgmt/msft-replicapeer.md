---
title: MSFT\_ReplicaPeer class
description: An enumerable object that represents an object in a target subsystem for which there is a replication relationship.
ms.assetid: 5DE51AC0-E84A-4DD9-9F9B-E8A3F6948E9F
keywords:
- MSFT_ReplicaPeer class Windows Storage Management API
- MSFT_ReplicaPeer class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_ReplicaPeer
- MSFT_ReplicaPeer.PeerObjectType
- MSFT_ReplicaPeer.PeerObjectId
- MSFT_ReplicaPeer.PeerObjectName
- MSFT_ReplicaPeer.PeerUniqueId
- MSFT_ReplicaPeer.PeerSubsystemName
- MSFT_ReplicaPeer.PeerProviderURI
- MSFT_ReplicaPeer.IsPrimary
- MSFT_ReplicaPeer.PeerObject
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_ReplicaPeer class

An enumerable object that represents an object in a target subsystem for which there is a replication relationship.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_ReplicaPeer : MSFT_StorageObject
{
  UInt16  PeerObjectType;
  String  PeerObjectId;
  String  PeerObjectName;
  String  PeerUniqueId;
  String  PeerSubsystemName;
  String  PeerProviderURI;
  Boolean IsPrimary;
  String  PeerObject;
};
```

## Members

The **MSFT\_ReplicaPeer** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_ReplicaPeer** class has these properties.

<dl> <dt>

**IsPrimary**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the replica peer is primary; that is, it is a System Element and not a Synced Element.

</dd> <dt>

**PeerObject**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Write-only
</dt> </dl>

A string that contains an embedded [**MSFT\_StorageObject**](msft-storageobject.md) object, populated when *PeerObjectType* has the value of "EmbeddedInstance".

</dd> <dt>

**PeerObjectId**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The object Id of the replica peer within the replica's storage subsystem.

</dd> <dt>

**PeerObjectName**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the replica peer within the replica's storage subsystem.

</dd> <dt>

**PeerObjectType**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The object type of this replica peer.

<dl> <dt>

<span id="VirtualDisk"></span><span id="virtualdisk"></span><span id="VIRTUALDISK"></span>**VirtualDisk** (4)
</dt> <dt>

<span id="Volume"></span><span id="volume"></span><span id="VOLUME"></span>**Volume** (5)
</dt> <dt>

<span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span>**Microsoft Reserved** (..)
</dt> <dt>

<span id="Partition"></span><span id="partition"></span><span id="PARTITION"></span>**Partition** (0x8000)
</dt> <dt>

<span id="ReplicationGroup"></span><span id="replicationgroup"></span><span id="REPLICATIONGROUP"></span>**ReplicationGroup** (0x8001)
</dt> <dt>

<span id="StorageSubSystem"></span><span id="storagesubsystem"></span><span id="STORAGESUBSYSTEM"></span>**StorageSubSystem** (0x8002)
</dt> </dl>

</dd> <dt>

**PeerProviderURI**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If the [**MSFT\_StorageProvider**](msft-storageprovider.md) is of type 2 ("SMI-S"), this field contains the protocol, computer host name, and port of the SMI-S server. Otherwise, this field will be NULL.

</dd> <dt>

**PeerSubsystemName**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The subsystem name of the replica peer within the replica's storage subsystem.

</dd> <dt>

**PeerUniqueId**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The unique Id of the replica peer within the replica's storage subsystem.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StorageObject**](msft-storageobject.md)
</dt> </dl>

 

 





