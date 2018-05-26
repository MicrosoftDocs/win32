---
title: MSFT\_ResiliencySetting class
description: Represents a storage pools resiliency settings.
ms.assetid: 8F8981DB-50D7-424D-BD5B-C646FD8E434F
keywords:
- MSFT_ResiliencySetting class Windows Storage Management API
- MSFT_ResiliencySetting class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_ResiliencySetting
- MSFT_ResiliencySetting.Name
- MSFT_ResiliencySetting.Description
- MSFT_ResiliencySetting.NumberOfDataCopiesMin
- MSFT_ResiliencySetting.NumberOfDataCopiesMax
- MSFT_ResiliencySetting.NumberOfDataCopiesDefault
- MSFT_ResiliencySetting.PhysicalDiskRedundancyMin
- MSFT_ResiliencySetting.PhysicalDiskRedundancyMax
- MSFT_ResiliencySetting.PhysicalDiskRedundancyDefault
- MSFT_ResiliencySetting.NumberOfColumnsMin
- MSFT_ResiliencySetting.NumberOfColumnsMax
- MSFT_ResiliencySetting.NumberOfColumnsDefault
- MSFT_ResiliencySetting.InterleaveMin
- MSFT_ResiliencySetting.InterleaveMax
- MSFT_ResiliencySetting.InterleaveDefault
- MSFT_ResiliencySetting.ParityLayout
- MSFT_ResiliencySetting.RequestNoSinglePointOfFailure
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSFT\_ResiliencySetting class

Represents a storage pool's resiliency settings.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
class MSFT_ResiliencySetting : MSFT_StorageObject
{
  String  Name;
  String  Description;
  UInt16  NumberOfDataCopiesMin;
  UInt16  NumberOfDataCopiesMax;
  UInt16  NumberOfDataCopiesDefault;
  UInt16  PhysicalDiskRedundancyMin;
  UInt16  PhysicalDiskRedundancyMax;
  UInt16  PhysicalDiskRedundancyDefault;
  UInt16  NumberOfColumnsMin;
  UInt16  NumberOfColumnsMax;
  UInt16  NumberOfColumnsDefault;
  UInt64  InterleaveMin;
  UInt64  InterleaveMax;
  UInt64  InterleaveDefault;
  UInt16  ParityLayout;
  Boolean RequestNoSinglePointOfFailure;
};
```

## Members

The **MSFT\_ResiliencySetting** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_ResiliencySetting** class has these methods.



| Method                                                    | Description                                                                                               |
|:----------------------------------------------------------|:----------------------------------------------------------------------------------------------------------|
| [**SetDefaults**](msft-resiliencysetting-setdefaults.md) | Allows a user to modify the default property values of the **MSFT\_ResiliencySetting** object.<br/> |



 

### Properties

The **MSFT\_ResiliencySetting** class has these properties.

<dl> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A system-set description of the capabilities of the resiliency setting, including (but not limited to) when a setting should be used, its strengths and drawbacks, performance information, and any other information that the vendor feels is helpful to the user.

</dd> <dt>

**InterleaveDefault**
</dt> <dd> <dl> <dt>

Data type: **UInt64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Units** (Bytes)
</dt> </dl>

The desired number of bytes that can form a strip in common striping-based resiliency settings. The strip is defined as the size of the portion of a stripe that lies on one physical disk. Thus, **Interleave** \* **NumberOfColumns** will yield the size of one stripe of user data.

</dd> <dt>

**InterleaveMax**
</dt> <dd> <dl> <dt>

Data type: **UInt64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Units** (Bytes)
</dt> </dl>

The maximum number of bytes that can form a strip in common striping-based resiliency settings. The strip is defined as the size of the portion of a stripe that lies on one physical disk.

</dd> <dt>

**InterleaveMin**
</dt> <dd> <dl> <dt>

Data type: **UInt64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Units** (Bytes)
</dt> </dl>

The minimum number of bytes that can form a strip in common striping-based resiliency settings. The strip is defined as the size of the portion of a stripe that lies on one physical disk.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

A system-set, user-friendly, display-oriented string that describes the resiliency setting.

</dd> <dt>

**NumberOfColumnsDefault**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-settable preference for the maximum number of underlying physical disks across which data should be striped.

</dd> <dt>

**NumberOfColumnsMax**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum number of underlying physical disks across which data can be striped in the common striping-based resiliency settings.

</dd> <dt>

**NumberOfColumnsMin**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The minimum number of underlying physical disks across which data can be striped in the common striping-based resiliency settings.

</dd> <dt>

**NumberOfDataCopiesDefault**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-settable preference for the number of complete data copies to maintain. The value of this parameter must be within the range defined by *NumberofDataCopiesMin* and *NumberOfDataCopiesMax* (inclusive). For new concrete pools, the default should be inherited from the corresponding primordial pool's capability. In the case of the primordial pool, the initial value for this field is left to the Storage Management Provider software.

</dd> <dt>

**NumberOfDataCopiesMax**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum number of complete copies of data that can be maintained by the storage pool.

</dd> <dt>

**NumberOfDataCopiesMin**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The minimum number of complete copies of data that can be maintained by the storage pool.

</dd> <dt>

**ParityLayout**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies whether a parity-based resiliency setting is using a rotated or non-rotated parity layout. If the resiliency setting is not parity based, this property must be set to NULL.



| Value                                                                                                                                                                                                                                                                   | Meaning                                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| <span id="Non-rotated_Parity"></span><span id="non-rotated_parity"></span><span id="NON-ROTATED_PARITY"></span><dl> <dt>**Non-rotated Parity**</dt> <dt>1</dt> </dl> | The parity-based resiliency setting uses a non-rotated parity layout.<br/> |
| <span id="Rotated_Parity"></span><span id="rotated_parity"></span><span id="ROTATED_PARITY"></span><dl> <dt>**Rotated Parity**</dt> <dt>2</dt> </dl>                 | The parity-based resiliency setting uses a rotated parity layout.<br/>     |



 

</dd> <dt>

**PhysicalDiskRedundancyDefault**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-settable preference for how many physical disk failures a virtual disk should be able to withstand before data loss occurs.

</dd> <dt>

**PhysicalDiskRedundancyMax**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum number of tolerable physical disk failures that can occur before data loss would occur.

</dd> <dt>

**PhysicalDiskRedundancyMin**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The minimum number of tolerable physical disk failures that can occur before data loss would occur.

</dd> <dt>

**RequestNoSinglePointOfFailure**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Set to **TRUE** to request no single point of failure.

</dd> </dl>

## Remarks

**MSFT\_ResiliencySetting** is a detailed description of the resiliency capabilities offered by a storage pool. A storage pool can have one or more of these settings. The **MSFT\_ResiliencySetting** object specifies a series of properties, each with a minimum, maximum, and default value. The minimum and maximum values may not reflect the current capabilities of the storage pool, but rather the ideal range of capabilities offered by the subsystem. The default values will be used when creating new virtual disks unless overridden.

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StorageObject**](msft-storageobject.md)
</dt> </dl>

 

 





