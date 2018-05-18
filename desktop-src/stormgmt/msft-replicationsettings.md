---
title: MSFT\_ReplicationSettings class
description: Represents the settings to be configured on a group or sync pair.
ms.assetid: '0C78E4F9-C420-47B3-9E4E-7EAADCF21A06'
keywords: ["MSFT_ReplicationSettings class Windows Storage Management API", "MSFT_ReplicationSettings class Windows Storage Management API , described"]
topic_type:
- apiref
api_name:
- MSFT_ReplicationSettings
- MSFT_ReplicationSettings.TargetElementSupplier
- MSFT_ReplicationSettings.ThinProvisioningPolicy
- MSFT_ReplicationSettings.LogDevices
- MSFT_ReplicationSettings.LogSizeInBytes
- MSFT_ReplicationSettings.ReplicationQuorum
- MSFT_ReplicationSettings.SyncMode
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
---

# MSFT\_ReplicationSettings class

Represents the settings to be configured on a group or sync pair.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_ReplicationSettings
{
  UInt16 TargetElementSupplier;
  UInt16 ThinProvisioningPolicy;
  String LogDevices[];
  UInt64 LogSizeInBytes;
  UInt16 ReplicationQuorum;
  UInt16 SyncMode;
};
```

## Members

The **MSFT\_ReplicationSettings** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_ReplicationSettings** class has these properties.

<dl> <dt>

**LogDevices**
</dt> <dd> <dl> <dt>

Data type: **String** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array of strings that contain embedded [**MSFT\_Volume**](msft-volume.md) objects representing a set of volumes where the replication journal for the replication group is hosted.

</dd> <dt>

**LogSizeInBytes**
</dt> <dd> <dl> <dt>

Data type: **UInt64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) (Bytes)
</dt> </dl>

Size of the replication journal in units of bytes. The size must be in multiples of gigabytes.

</dd> <dt>

**ReplicationQuorum**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Minimum number of synchronous replication partnerships that are in synchronous replication state for I/O to continue on the source replication group.

</dd> <dt>

**SyncMode**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Describes whether the target elements will be updated synchronously or asynchronously. If **NULL**, the implementation decides the mode.

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Synchronous"></span><span id="synchronous"></span><span id="SYNCHRONOUS"></span>**Synchronous** (2)
</dt> <dt>

<span id="Asynchronous"></span><span id="asynchronous"></span><span id="ASYNCHRONOUS"></span>**Asynchronous** (3)
</dt> <dt>

<span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span>**Microsoft Reserved** (..)
</dt> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>**Vendor Specific** (32768..65535)
</dt> </dl>

</dd> <dt>

**TargetElementSupplier**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

</dd> <dt>

**ThinProvisioningPolicy**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



 

 





