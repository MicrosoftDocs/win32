---
title: MSFT\_SMPoolSetting class
description: Represents settings for a storage pool.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '47e749d8-6224-4b69-b985-6a2cdac4a359'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_SMPoolSetting class", "MSFT_SMPoolSetting class, described"]
---

# MSFT\_SMPoolSetting class

Represents settings for a storage pool.

**Windows Server 2012 R2 and Windows Server 2012:** This class does not inherit from [**MSFT\_SMStorageObject**](msft-smstorageobject.md) which is new for Windows Server 2016.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("WMIStorage"), AMENDMENT]
class MSFT_SMPoolSetting : MSFT_SMStorageObject
{
  String  ObjectId;
  String  Identifier;
  String  DisplayName;
  boolean NoSinglePointOfFailure;
  uint16  DataRedundancyMin;
  uint16  DataRedundancyMax;
  uint16  DataRedundancyGoal;
  uint16  PackageRedundancyMin;
  uint16  PackageRedundancyMax;
  uint16  PackageRedundancyGoal;
  uint16  ChangeableType;
  uint16  ExtentStripeLength;
  uint16  ExtentStripeLengthMin;
  uint16  ExtentStripeLengthMax;
  uint16  ParityLayout;
  uint64  UserDataStripeDepth;
  uint64  UserDataStripeDepthMin;
  uint64  UserDataStripeDepthMax;
  uint16  ThinProvisionedPoolType;
  string  ThinProvisionedPoolTypeDescription;
};
```

## Members

The **MSFT\_SMPoolSetting** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SMPoolSetting** class has these properties.

<dl> <dt>

**ChangeableType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> <dt>

**DataRedundancyGoal**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> <dt>

**DataRedundancyMax**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> <dt>

**DataRedundancyMin**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> <dt>

**DisplayName**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The user-friendly name of the storage pool.

</dd> <dt>

**ExtentStripeLength**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> <dt>

**ExtentStripeLengthMax**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> <dt>

**ExtentStripeLengthMin**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

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

**NoSinglePointOfFailure**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

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

**PackageRedundancyGoal**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> <dt>

**PackageRedundancyMax**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> <dt>

**PackageRedundancyMin**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> <dt>

**ParityLayout**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> <dt>

**ThinProvisionedPoolType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The type of thin provisioned pool used when StorageSetting is used as a goal for creating a thin provisioned pool.

The possible values are.

<dt>

<span id="ThinlyProvisionedAllocatedStoragePool"></span><span id="thinlyprovisionedallocatedstoragepool"></span><span id="THINLYPROVISIONEDALLOCATEDSTORAGEPOOL"></span>

**ThinlyProvisionedAllocatedStoragePool** (7)


</dt> <dd></dd> <dt>

<span id="ThinlyProvisionedQuotaStoragePool"></span><span id="thinlyprovisionedquotastoragepool"></span><span id="THINLYPROVISIONEDQUOTASTORAGEPOOL"></span>

**ThinlyProvisionedQuotaStoragePool** (8)


</dt> <dd></dd> <dt>

<span id="ThinlyProvisionedLimitlessStoragePool"></span><span id="thinlyprovisionedlimitlessstoragepool"></span><span id="THINLYPROVISIONEDLIMITLESSSTORAGEPOOL"></span>

**ThinlyProvisionedLimitlessStoragePool** (9)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>10–2047</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>2048–65535</dd> </dl>

</dd> <dt>

**ThinProvisionedPoolTypeDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> <dt>

**UserDataStripeDepth**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> <dt>

**UserDataStripeDepthMax**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> <dt>

**UserDataStripeDepthMin**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TBD

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



 

 





