---
title: MSISCSITARGET\_StorageCapabilities class
description: Defines the capabilities of a storage service or MSISCSITARGET\_StoragePool.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6874998b-eb10-4973-b716-66ad22331b66
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSISCSITARGET_StorageCapabilities class iSCSI Software Target API
- MSISCSITARGET_StorageCapabilities class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- MSISCSITARGET_StorageCapabilities
- MSISCSITARGET_StorageCapabilities.Caption
- MSISCSITARGET_StorageCapabilities.Description
- MSISCSITARGET_StorageCapabilities.InstanceID
- MSISCSITARGET_StorageCapabilities.ElementName
- MSISCSITARGET_StorageCapabilities.ElementType
- MSISCSITARGET_StorageCapabilities.NoSinglePointOfFailure
- MSISCSITARGET_StorageCapabilities.NoSinglePointOfFailureDefault
- MSISCSITARGET_StorageCapabilities.DataRedundancyMax
- MSISCSITARGET_StorageCapabilities.DataRedundancyMin
- MSISCSITARGET_StorageCapabilities.DataRedundancyDefault
- MSISCSITARGET_StorageCapabilities.PackageRedundancyMax
- MSISCSITARGET_StorageCapabilities.PackageRedundancyMin
- MSISCSITARGET_StorageCapabilities.PackageRedundancyDefault
- MSISCSITARGET_StorageCapabilities.DeltaReservationMax
- MSISCSITARGET_StorageCapabilities.DeltaReservationMin
- MSISCSITARGET_StorageCapabilities.DeltaReservationDefault
- MSISCSITARGET_StorageCapabilities.ExtentStripeLengthDefault
- MSISCSITARGET_StorageCapabilities.ParityLayoutDefault
- MSISCSITARGET_StorageCapabilities.UserDataStripeDepthDefault
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSISCSITARGET\_StorageCapabilities class

Defines the capabilities of a storage service or [**MSISCSITARGET\_StoragePool**](msiscsitarget-storagepool.md). For example, an instance of **MSISCSITARGET\_StorageCapabilities** could be associated with either a [**MSISCSITARGET\_StorageConfigurationService**](msiscsitarget-storageconfigurationservice.md) or [**MSISCSITARGET\_StoragePool**](msiscsitarget-storagepool.md) by using [**MSISCSITARGET\_ElementCapabilities**](msiscsitarget-elementcapabilities.md).

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("MSiSCSITargetProv"), Version("1.0.0")]
class MSISCSITARGET_StorageCapabilities : CIM_StorageCapabilities
{
  string  Caption;
  string  Description;
  string  InstanceID;
  string  ElementName;
  uint16  ElementType;
  boolean NoSinglePointOfFailure;
  boolean NoSinglePointOfFailureDefault;
  uint16  DataRedundancyMax;
  uint16  DataRedundancyMin;
  uint16  DataRedundancyDefault;
  uint16  PackageRedundancyMax;
  uint16  PackageRedundancyMin;
  uint16  PackageRedundancyDefault;
  uint16  DeltaReservationMax;
  uint16  DeltaReservationMin;
  uint16  DeltaReservationDefault;
  uint16  ExtentStripeLengthDefault;
  uint16  ParityLayoutDefault;
  uint64  UserDataStripeDepthDefault;
};
```

## Members

The **MSISCSITARGET\_StorageCapabilities** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSISCSITARGET\_StorageCapabilities** class has these methods.



| Method                                                                                                   | Description                                                                                                                                                                                                                                                |
|:---------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateSetting**](createsetting-msiscsitarget-storagecapabilities.md)                                 | Creates and populates a [**MSISCSITARGET\_StorageSetting**](msiscsitarget-storagesetting.md) instance from a **MSISCSITARGET\_StorageCapabilities** instance.<br/> This method is inherited from the **CIM\_StorageCapabilities** class.<br/> |
| [**GetSupportedParityLayouts**](getsupportedparitylayouts-msiscsitarget-storagecapabilities.md)         | Retrieves the supported parity layouts for systems that support parity-based storage organizations for volume or pool creation.<br/> This method is inherited from the **CIM\_StorageCapabilities** class.<br/>                                |
| [**GetSupportedStripeDepthRange**](getsupportedstripedepthrange-msiscsitarget-storagecapabilities.md)   | Retrieves the supported stripe depth range for systems that support a range of user data stripe depths.<br/> This method is inherited from the **CIM\_StorageCapabilities** class.<br/>                                                        |
| [**GetSupportedStripeDepths**](getsupportedstripedepths-msiscsitarget-storagecapabilities.md)           | Retrieves a list of supported values for systems that support discrete user data stripe depths.<br/> This method is inherited from the **CIM\_StorageCapabilities** class.<br/>                                                                |
| [**GetSupportedStripeLengthRange**](getsupportedstripelengthrange-msiscsitarget-storagecapabilities.md) | Retrieves the supported range of extent stripe lengths for systems that support a range of lengths.<br/> This method is inherited from the **CIM\_StorageCapabilities** class.<br/>                                                            |
| [**GetSupportedStripeLengths**](getsupportedstripelengths-msiscsitarget-storagecapabilities.md)         | Retrieves a list of supported extent stripe lengths for systems that support discrete lengths.<br/> This method is inherited from the **CIM\_StorageCapabilities** class.<br/>                                                                 |



 

### Properties

The **MSISCSITARGET\_StorageCapabilities** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

The Caption property is a short textual description (one- line string) of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**DataRedundancyDefault**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) (1), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageCapabilities.DataRedundancyMax", "CIM\_StorageCapabilities.DataRedundancyMin")
</dt> </dl>

DataRedundancyDefault describes the default number of complete copies of data that can be maintained. Examples would be RAID 5 where 1 copy is maintained and RAID 1 where 2 or more copies are maintained. Possible values are 1 to n. The bounds for the redundancy (max and min) are defined by DataRedundancyMax and DataRedundancyMin.

This property is inherited from [**CIM\_StorageCapabilities**](cim-storagecapabilities.md).

</dd> <dt>

**DataRedundancyMax**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) (1), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageCapabilities.DataRedundancyMin", "CIM\_StorageCapabilities.DataRedundancyDefault")
</dt> </dl>

DataRedundancyMax describes the maximum number of complete copies of data that can be maintained. Examples would be RAID 5 (where 1 copy is maintained) and RAID 1 (where 2 or more copies are maintained). Possible values are 1 to n. The default redundancy is specified using DataRedundancyDefault, while the minimum is defined by DataRedundancyMin.

This property is inherited from [**CIM\_StorageCapabilities**](cim-storagecapabilities.md).

</dd> <dt>

**DataRedundancyMin**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) (1), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageCapabilities.DataRedundancyMax", "CIM\_StorageCapabilities.DataRedundancyDefault")
</dt> </dl>

DataRedundancyMin describes the minimum number of complete copies of data that can be maintained. Examples would be RAID 5 where 1 copy is maintained and RAID 1 where 2 or more copies are maintained). Possible values are 1 to n. The default redundancy is specified using DataRedundancyDefault, while the maximum is defined by DataRedundancyMax.

This property is inherited from [**CIM\_StorageCapabilities**](cim-storagecapabilities.md).

</dd> <dt>

**DeltaReservationDefault**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Punit** ("percent"), [**Units**](https://msdn.microsoft.com/library/aa393650) ("Percentage"), [**MinValue**](https://msdn.microsoft.com/library/aa393650) (0), [**MaxValue**](https://msdn.microsoft.com/library/aa393650) (100), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageCapabilities.DeltaReservationMax", "CIM\_StorageCapabilities.DeltaReservationMin")
</dt> </dl>

Delta reservation is a number between 1 (1%) and a 100 (100%) that specifies how much space should be reserved by default in a replica for caching changes. For a complete copy this would be 100%, but it can be lower in some implementations. This parameter sets the default value, while DeletaReservationMax and DeltReservationMin set the upper and lower bounds.

This property is inherited from [**CIM\_StorageCapabilities**](cim-storagecapabilities.md).

</dd> <dt>

**DeltaReservationMax**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Punit** ("percent"), [**Units**](https://msdn.microsoft.com/library/aa393650) ("Percentage"), [**MinValue**](https://msdn.microsoft.com/library/aa393650) (0), [**MaxValue**](https://msdn.microsoft.com/library/aa393650) (100), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageCapabilities.DeltaReservationMin", "CIM\_StorageCapabilities.DeltaReservationDefault")
</dt> </dl>

DeltaReservatioMax is a number between 1 (1%) and a 100 (100%) that specifies the maximum amount of space reserved in a replica for caching changes. For a complete copy this would be 100%, but it can be lower in some implementations. This parameter sets the upper limit, while DeltaReservationMin sets the lower limit.

This property is inherited from [**CIM\_StorageCapabilities**](cim-storagecapabilities.md).

</dd> <dt>

**DeltaReservationMin**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Punit** ("percent"), [**Units**](https://msdn.microsoft.com/library/aa393650) ("Percentage"), [**MinValue**](https://msdn.microsoft.com/library/aa393650) (0), [**MaxValue**](https://msdn.microsoft.com/library/aa393650) (100), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageCapabilities.DeltaReservationMax", "CIM\_StorageCapabilities.DeltaReservationDefault")
</dt> </dl>

DeltaReservationMin is a number between 1 (1%) and a 100 (100%) that specifies the minimum amount of space that should be reserved in a replica for caching changes. For a complete copy this would be 100%, but it can be lower in some implementations. This parameter sets the lower limit, while DeltaReservationMax sets the upper limit.

This property is inherited from [**CIM\_StorageCapabilities**](cim-storagecapabilities.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Contains a textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The user friendly name for this instance of Capabilities. In addition, the user friendly name can be used as a index property for a search of query. (Note: Name does not have to be unique within a namespace.)

This property is inherited from [**CIM\_Capabilities**](cim-capabilities.md).

</dd> <dt>

**ElementType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Enumeration indicating the type of element to which this StorageCapabilities applies.

This property is inherited from [**CIM\_StorageCapabilities**](cim-storagecapabilities.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Reserved"></span><span id="reserved"></span><span id="RESERVED"></span>

**Reserved** (1)


</dt> <dd></dd> <dt>

<span id="Any_Type"></span><span id="any_type"></span><span id="ANY_TYPE"></span>

**Any Type** (2)


</dt> <dd></dd> <dt>

<span id="StorageVolume"></span><span id="storagevolume"></span><span id="STORAGEVOLUME"></span>

**StorageVolume** (3)


</dt> <dd></dd> <dt>

<span id="StorageExtent"></span><span id="storageextent"></span><span id="STORAGEEXTENT"></span>

**StorageExtent** (4)


</dt> <dd></dd> <dt>

<span id="StoragePool"></span><span id="storagepool"></span><span id="STORAGEPOOL"></span>

**StoragePool** (5)


</dt> <dd></dd> <dt>

<span id="StorageConfigurationService"></span><span id="storageconfigurationservice"></span><span id="STORAGECONFIGURATIONSERVICE"></span>

**StorageConfigurationService** (6)


</dt> <dd></dd> <dt>

<span id="LogicalDisk"></span><span id="logicaldisk"></span><span id="LOGICALDISK"></span>

**LogicalDisk** (7)


</dt> <dd></dd> </dl>

</dd> <dt>

**ExtentStripeLengthDefault**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

Extent Stripe Length describes the number of underlying StorageExtents across which data is striped in the common striping-based storage organizations. This is also known as the number of 'members' or 'columns'.

A NULL value for ExtentStripeLengthDefault indicates that the system does not support configuration of storage by specifying Stripe Length.

If Extent Stripe Length is supported, and this Capabilities instance is associated with a pool that was created with a range of QOS then ExtentStripeLengthDefault represents the default value. Other available values(such as min, max, and discrete values) can be determined by using the 'GetSupportedStripeLengths' and 'GetSupportedStripeLengthRange' methods.

If Extent Stripe Length is supported and the pool was created with a single specific QOS, representing a Raid group, set, or rank, then this property represents the current/fixed value for the pool, and Extent Stripe Length is not supported in subsequent creation of elements from this pool. Consequently, the 'GetSupportedStripeLength' methods cannot be used, and in a StorageSetting instance used as a goal when creating or modifying a child element of the pool, ExtentStripeLengthGoal, ExtentStripeLengthMin, and ExtentStripeLengthMax MUST be set to NULL.

This property is inherited from [**CIM\_StorageCapabilities**](cim-storagecapabilities.md).

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Within the scope of the instantiating Namespace, InstanceID opaquely and uniquely identifies an instance of this class. In order to ensure uniqueness within the NameSpace, the value of InstanceID SHOULD be constructed using the following 'preferred' algorithm: &lt;OrgID&gt;:&lt;LocalID&gt; Where &lt;OrgID&gt; and &lt;LocalID&gt; are separated by a colon ':', and where &lt;OrgID&gt; MUST include a copyrighted, trademarked or otherwise unique name that is owned by the business entity creating/defining the InstanceID, or is a registered ID that is assigned to the business entity by a recognized global authority (This is similar to the &lt;Schema Name&gt;\_&lt;Class Name&gt; structure of Schema class names.) In addition, to ensure uniqueness &lt;OrgID&gt; MUST NOT contain a colon (':'). When using this algorithm, the first colon to appear in InstanceID MUST appear between &lt;OrgID&gt; and &lt;LocalID&gt;. &lt;LocalID&gt; is chosen by the business entity and SHOULD not be re-used to identify different underlying (real-world) elements. If the above 'preferred' algorithm is not used, the defining entity MUST assure that the resultant InstanceID is not re-used across any InstanceIDs produced by this or other providers for this instance's NameSpace. For DMTF defined instances, the 'preferred' algorithm MUST be used with the &lt;OrgID&gt; set to 'CIM'.

This property is inherited from [**CIM\_Capabilities**](cim-capabilities.md).

</dd> <dt>

**NoSinglePointOfFailure**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageCapabilities.NoSinglePointOfFailureDefault")
</dt> </dl>

Indicates whether or not the associated element supports no single point of failure. Values are: FALSE = does not support no single point of failure, and TRUE = supports no single point of failure.

This property is inherited from [**CIM\_StorageCapabilities**](cim-storagecapabilities.md).

</dd> <dt>

**NoSinglePointOfFailureDefault**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageCapabilities.NoSinglePointOfFailure")
</dt> </dl>

Indicates the default value for the NoSinglePointOfFailure property.

This property is inherited from [**CIM\_StorageCapabilities**](cim-storagecapabilities.md).

</dd> <dt>

**PackageRedundancyDefault**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageCapabilities.PackageRedundancyMin", "CIM\_StorageCapabilities.PackageRedundancyMax")
</dt> </dl>

PackageRedundancyDefault describes the default number of redundant packages that will be used. For example, in the storage domain, package redundancy describes how many disk spindles can fail without data loss including, at most, one spare. An example would be RAID5 with a spare disk which would have a PackageRedundancy of 2. Possible values are 0 to n. The bounds for redundancy are specified using the properties, PackageRedundancyMax and PackageRedundancyMin.

This property is inherited from [**CIM\_StorageCapabilities**](cim-storagecapabilities.md).

</dd> <dt>

**PackageRedundancyMax**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageCapabilities.PackageRedundancyMin", "CIM\_StorageCapabilities.PackageRedundancyDefault")
</dt> </dl>

PackageRedundancyMax describes the maximum number of redundant packages that can be used. For example, in the storage domain, package redundancy describes how many disk spindles can fail without data loss including, at most, one spare. An example would be RAID5 with a spare disk which would have a PackageRedundancy of 2. Possible values are 0 to n. The default redundancy is specified using PackageRedundancyDefault, while the maximum is defined by PackageRedundancyMax.

This property is inherited from [**CIM\_StorageCapabilities**](cim-storagecapabilities.md).

</dd> <dt>

**PackageRedundancyMin**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageCapabilities.PackageRedundancyMax", "CIM\_StorageCapabilities.PackageRedundancyDefault")
</dt> </dl>

PackageRedundancyMin describes the minimum number of redundant packages that can be used. For example, in the storage domain, package redundancy describes how many disk spindles can fail without data loss including, at most, one spare. An example would be RAID5 with a spare disk which would have a PackageRedundancy of 2. Possible values are 0 to n. The default redundancy is specified using PackageRedundancyDefault, while the minimum is defined by PackageRedundancyMin.

This property is inherited from [**CIM\_StorageCapabilities**](cim-storagecapabilities.md).

</dd> <dt>

**ParityLayoutDefault**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

ParityLayout specifies whether a parity-based storage organization is using rotated or non-rotated parity. If this capabilities instance is associated with a pool that was created with a range of QOS then ParityLayoutDefault represents the default value. Other available values can be determined by using the 'GetSupportedParityLayouts' method. If the pool was created with a single specific QOS, representing a Raid group, set, or rank, then this property represents the current/fixed value for the pool, and ParityLayout is not supported in subsequent creation of elements from this pool. Consequently, the 'GetSupportedParityLayouts' method cannot be used, and the ParityLayoutGoal property in StorageSetting instances used in child element operations on this pool MUST be set to NULL. A NULL value for ParityLayoutDefault indicates that the system does not support configuration of storage by specifying ParityLayout.

This property is inherited from [**CIM\_StorageCapabilities**](cim-storagecapabilities.md).

<dt>

<span id="Non-Rotated_Parity"></span><span id="non-rotated_parity"></span><span id="NON-ROTATED_PARITY"></span>

**Non-Rotated Parity** (2)


</dt> <dd></dd> <dt>

<span id="Rotated_Parity"></span><span id="rotated_parity"></span><span id="ROTATED_PARITY"></span>

**Rotated Parity** (3)


</dt> <dd></dd> </dl>

</dd> <dt>

**UserDataStripeDepthDefault**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Punit** ("byte"), [**Units**](https://msdn.microsoft.com/library/aa393650) ("Bytes"), [**MinValue**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

User Data Stripe Depth describes the number of bytes forming a strip in common striping-based storage organizations. The strip is defined as the size of the portion of a stripe that lies on one extent. Thus, ExtentStripeLength \* UserDataStripeDepth will yield the size of one stripe of user data. A NULL value for UserDataStripeDepthDefault indicates that the system does not support configuration of storage by specifying Stripe Depth.

If User Data Stripe Depth is supported, and this Capabilities instance is associated with a pool that was created with a range of QOS then UserDataStripeDepthDefault represents the default value. Other available values(such as min, max, and discrete values) can be determined by using the 'GetSupportedStripeDepths' and 'GetSupportedStripeDepthRange' methods.

If User Data Stripe Depth is supported and the pool was created with a single specific QOS, representing a Raid group, set, or rank, then this property represents the current/fixed value for the pool, and User Data Stripe Depth is not supported in subsequent creation of elements from this pool. Consequently, the 'GetSupportedStripeDepth' methods cannot be used, and in a StorageSetting instance used as a goal when creating or modifying a child element of the pool, UserDataStripeDepthGoal, UserDataStripeDepthMin, and UserDataStripeDepthMax MUST be set to NULL.

This property is inherited from [**CIM\_StorageCapabilities**](cim-storagecapabilities.md).

</dd> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_StorageCapabilities**](cim-storagecapabilities.md)
</dt> <dt>

[iSCSI Target Server Reference](https://msdn.microsoft.com/library/hh830439)
</dt> <dt>

[**MSISCSITARGET\_StoragePool**](msiscsitarget-storagepool.md)
</dt> <dt>

[**MSISCSITARGET\_StorageSetting**](msiscsitarget-storagesetting.md)
</dt> </dl>

 

 





