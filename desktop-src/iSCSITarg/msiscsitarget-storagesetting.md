---
title: MSISCSITARGET\_StorageSetting class
description: Defines a set of properties that are related to the configuration of a storage volume.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'acfef8d0-d439-4516-9351-8e3706896910'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSISCSITARGET_StorageSetting class iSCSI Software Target API", "MSISCSITARGET_StorageSetting class iSCSI Software Target API , described"]
topic_type:
- apiref
api_name:
- MSISCSITARGET_StorageSetting
- MSISCSITARGET_StorageSetting.Caption
- MSISCSITARGET_StorageSetting.Description
- MSISCSITARGET_StorageSetting.InstanceID
- MSISCSITARGET_StorageSetting.ElementName
- MSISCSITARGET_StorageSetting.NoSinglePointOfFailure
- MSISCSITARGET_StorageSetting.DataRedundancyMax
- MSISCSITARGET_StorageSetting.DataRedundancyMin
- MSISCSITARGET_StorageSetting.DataRedundancyGoal
- MSISCSITARGET_StorageSetting.PackageRedundancyMax
- MSISCSITARGET_StorageSetting.PackageRedundancyMin
- MSISCSITARGET_StorageSetting.PackageRedundancyGoal
- MSISCSITARGET_StorageSetting.DeltaReservationMax
- MSISCSITARGET_StorageSetting.DeltaReservationMin
- MSISCSITARGET_StorageSetting.DeltaReservationGoal
- MSISCSITARGET_StorageSetting.ChangeableType
- MSISCSITARGET_StorageSetting.ExtentStripeLength
- MSISCSITARGET_StorageSetting.ExtentStripeLengthMin
- MSISCSITARGET_StorageSetting.ExtentStripeLengthMax
- MSISCSITARGET_StorageSetting.ParityLayout
- MSISCSITARGET_StorageSetting.UserDataStripeDepth
- MSISCSITARGET_StorageSetting.UserDataStripeDepthMin
- MSISCSITARGET_StorageSetting.UserDataStripeDepthMax
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
---

# MSISCSITARGET\_StorageSetting class

Defines a set of properties that are related to the configuration of a storage volume.

A **MSISCSITARGET\_StorageSetting** instance is roughly equivalent to a service-level agreement (SLA). A storage setting defines properties in two categories:

The quality of service (QoS) properties.

-   **PackageRedundancyGoal**
-   **DataRedundancyGoal**
-   **NoSinglePointOfFailure**

The detailed redundant array of independent disks (RAID) properties.

-   **ExtentStripeLength**
-   **ParityLayout**
-   **UserDataStripeDepth**

The use of these properties differs depending on whether the **MSISCSITARGET\_StorageSetting** instance is used as a goal for a storage configuration service operation or whether it is used as a service-level agreement (SLA) for a created storage volume. In a storage setting that is used as a goal, the QoS properties are required as a set. The detailed RAID properties, if supported, can be used optionally in any combination. In a storage setting that is used as a service-level agreement for a volume, the QoS properties reflect the SLA, with a goal, a minimum, and a maximum. The actual current service level is indicated by corresponding properties in the [**MSISCSITARGET\_StorageVolume**](msiscsitarget-storagevolume.md) instance.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("MSiSCSITargetProv"), Version("1.0.0")]
class MSISCSITARGET_StorageSetting : CIM_StorageSetting
{
  string  Caption;
  string  Description;
  string  InstanceID;
  string  ElementName;
  boolean NoSinglePointOfFailure;
  uint16  DataRedundancyMax;
  uint16  DataRedundancyMin;
  uint16  DataRedundancyGoal;
  uint16  PackageRedundancyMax;
  uint16  PackageRedundancyMin;
  uint16  PackageRedundancyGoal;
  uint8   DeltaReservationMax;
  uint8   DeltaReservationMin;
  uint8   DeltaReservationGoal;
  uint16  ChangeableType;
  uint16  ExtentStripeLength;
  uint16  ExtentStripeLengthMin;
  uint16  ExtentStripeLengthMax;
  uint16  ParityLayout;
  uint64  UserDataStripeDepth;
  uint64  UserDataStripeDepthMin;
  uint64  UserDataStripeDepthMax;
};
```

## Members

The **MSISCSITARGET\_StorageSetting** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSISCSITARGET\_StorageSetting** class has these properties.

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

**ChangeableType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Enumeration indicating the type of setting. "Fixed - Not Changeable" settings are primordial. These setting are defined at the implementor of the class. "Changeable - Transient" is the type of setting produced by the "CreateSetting" method. A client can subsequently request that the implementation persist the generated and potentially modified setting indefinately. Only a "Changeable - Transient" setting SHALL be converted to a "Changeable = Persistent" setting; the setting SHALL NOT be changed back.

This property is inherited from [**CIM\_StorageSetting**](cim-storagesetting.md).

<dt>

<span id="Fixed_-_Not_Changeable"></span><span id="fixed_-_not_changeable"></span><span id="FIXED_-_NOT_CHANGEABLE"></span>

**Fixed - Not Changeable** (0)


</dt> <dd></dd> <dt>

<span id="Changeable_-_Transient"></span><span id="changeable_-_transient"></span><span id="CHANGEABLE_-_TRANSIENT"></span>

**Changeable - Transient** (1)


</dt> <dd></dd> <dt>

<span id="Changeable_-_Persistent"></span><span id="changeable_-_persistent"></span><span id="CHANGEABLE_-_PERSISTENT"></span>

**Changeable - Persistent** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**DataRedundancyGoal**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) (1), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageSetting.DataRedundancyMax", "CIM\_StorageSetting.DataRedundancyMin")
</dt> </dl>

DataRedundancyGoal describes the desired number of complete copies of data to be maintained. Examples would be RAID 5 where 1 copy is maintained and RAID 1 where 2 or more copies are maintained. Possible values are 1 to n. The bounds (max and min) for redundancy are defined using the properties, DataRedundancyMax and DataRedundancyMin.

This property is inherited from [**CIM\_StorageSetting**](cim-storagesetting.md).

</dd> <dt>

**DataRedundancyMax**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) (1), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageSetting.DataRedundancyMin", "CIM\_StorageSetting.DataRedundancyGoal")
</dt> </dl>

DataRedundancyMax describes the maximum number of complete copies of data to be maintained. Examples would be RAID 5 where 1 copy is maintained and RAID 1 where 2 or more copies are maintained. Possible values are 1 to n. The desired redundancy is specified using DataRedundancyGoal, while the minimum is defined by DataRedundancyMin.

This property is inherited from [**CIM\_StorageSetting**](cim-storagesetting.md).

</dd> <dt>

**DataRedundancyMin**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) (1), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageSetting.DataRedundancyMax", "CIM\_StorageSetting.DataRedundancyGoal")
</dt> </dl>

DataRedundancyMin describes the minimum number of complete copies of data to be maintained. Examples would be RAID 5 where 1 copy is maintained and RAID 1 where 2 or more copies are maintained. Possible values are 1 to n. The desired redundancy is specified using DataRedundancyGoal, while the maximum is defined by DataRedundancyMax.

This property is inherited from [**CIM\_StorageSetting**](cim-storagesetting.md).

</dd> <dt>

**DeltaReservationGoal**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("Percentage"), [**MinValue**](https://msdn.microsoft.com/library/aa393650) (1), [**MaxValue**](https://msdn.microsoft.com/library/aa393650) (100), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageSetting.DeltaReservationMin", "CIM\_StorageSetting.DeltaReservationMax")
</dt> </dl>

DeltaReservationGoal is a number between 1 (1%) and a 100 (100%) which specifies the desired amount of space that should be reserved in a replica for caching changes. For a complete copy this would be 100%. The bounds (max and min) for the reservation are defined using the properties, DeltaReservationMax and DeltaReservationMin.

This property is inherited from [**CIM\_StorageSetting**](cim-storagesetting.md).

</dd> <dt>

**DeltaReservationMax**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("Percentage"), [**MinValue**](https://msdn.microsoft.com/library/aa393650) (1), [**MaxValue**](https://msdn.microsoft.com/library/aa393650) (100), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageSetting.DeltaReservationMin", "CIM\_StorageSetting.DeltaReservationGoal")
</dt> </dl>

DeltaReservationMax is a number between 1 (1%) and a 100 (100%) which specifies the maximum amount of space that should be reserved in a replica for caching changes. For a complete copy this would be 100%. The desired reservation is specified using DeltaReservationGoal, while the minimum is defined by DeltaReservationMin.

This property is inherited from [**CIM\_StorageSetting**](cim-storagesetting.md).

</dd> <dt>

**DeltaReservationMin**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("Percentage"), [**MinValue**](https://msdn.microsoft.com/library/aa393650) (1), [**MaxValue**](https://msdn.microsoft.com/library/aa393650) (100), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageSetting.DeltaReservationMax", "CIM\_StorageSetting.DeltaReservationGoal")
</dt> </dl>

DeltaReservationMin is a number between 1 (1%) and a 100 (100%) which specifies the minimum amount of space that should be reserved in a replica for caching changes. For a complete copy this would be 100%. The desired reservation is specified using DeltaReservationGoal, while the maximum is defined by DeltaReservationMax.

This property is inherited from [**CIM\_StorageSetting**](cim-storagesetting.md).

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

The user-friendly name for this instance of SettingData. In addition, the user-friendly name can be used as an index property for a search or query. (Note: The name does not have to be unique within a namespace.)

This property is inherited from [**CIM\_SettingData**](cim-settingdata.md).

</dd> <dt>

**ExtentStripeLength**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) (1), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageSetting.ExtentStripeLengthMax", "CIM\_StorageSetting.ExtentStripeLengthMin")
</dt> </dl>

ExtentStripeLength describes the number of underlying StorageExtents across which data is striped in the common striping-based storage organizations. This is also known as the number of 'members' or 'columns'. When used in a goal setting instance, ExtentStripeLength is the optimal desired value. The bounds (max and min) for Stripe Length are defined using the properties ExtentStripeLengthMax and ExtentStripeLengthMin. ExtentStripeLength MUST be set to NULL if the scoping StorageCapablities indicates that it is not supported in this context. ExtentStripeLength can be used in conjunction with CreateOrModifyElementFromELements to explicitly configure storage. An example would be RAID 0+1 with mirroring two stripe sets, each set being three wide. In this case CreateOrModifyElementFromElements would be passed a goal setting with DataRedundancy = 2 and ExtentStripeLength = 3. The size of the InElements array would be 6 and would contain the StorageExtents to be used to construct the StorageElement as a RAID 0+1. ExtentStripeLengthMin and ExtentStripeLengthMax are meaningless and wouldbe set to NULL. If the property is supported, and is part of StorageSettingWithHints it MAY be set to NULL. If used it will constrain the effects of Hint selections. When used in a Setting instance associated to a Volume, this property indicates the specific value that the Volume was created with, and ExtentStripeLengthMin and ExtentStripeLengthMax will be set to the same specific value.

This property is inherited from [**CIM\_StorageSetting**](cim-storagesetting.md).

</dd> <dt>

**ExtentStripeLengthMax**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) (1), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageSetting.ExtentStripeLengthMin", "CIM\_StorageSetting.ExtentStripeLength")
</dt> </dl>

ExtentStripeLength describes the number of underlying StorageExtents across which data is striped in the common striping-based storage organizations. This is also known as the number of 'members' or 'columns'. When used in a goal setting instance, ExtentStripeLengthMax is the maximum acceptable value. The desired Stripe Length is specified using ExtentStripeLength, while the minimum is defined by ExtentStripeLengthMin. ExtentStripeLengthMax MUST be set to NULL if the scoping StorageCapablities indicates that it is not supported in this context. If the property is supported, and is part of StorageSettingWithHints it MAY be set to NULL. If used it will constrain the effects of Hint selections. When used in a Setting instance associated to a Volume, this property is set to the specific value of ExtentStripeLength.

This property is inherited from [**CIM\_StorageSetting**](cim-storagesetting.md).

</dd> <dt>

**ExtentStripeLengthMin**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MinValue**](https://msdn.microsoft.com/library/aa393650) (1), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageSetting.ExtentStripeLengthMax", "CIM\_StorageSetting.ExtentStripeLength")
</dt> </dl>

ExtentStripeLength describes the number of underlying StorageExtents across which data is striped in the common striping-based storage organizations. This is also known as the number of 'members' or 'columns'. When used in a goal setting instance, ExtentStripeLengthMin is the minimum acceptable value. The desired Stripe Length is specified using ExtentStripeLength, while the maximum is defined by ExtentStripeLengthMax. ExtentStripeLengthMin MUST be set to NULL if the scoping StorageCapablities indicates that it is not supported in this context. If the property is supported, and is part of StorageSettingWithHints it MAY be set to NULL. If used it will constrain the effects of Hint selections. When used in a Setting instance associated to a Volume, this property is set to the specific value of ExtentStripeLength.

This property is inherited from [**CIM\_StorageSetting**](cim-storagesetting.md).

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Within the scope of the instantiating Namespace, InstanceID opaquely and uniquely identifies an instance of this class. To ensure uniqueness within the NameSpace, the value of InstanceID should be constructed using the following "preferred" algorithm:

&lt;OrgID&gt;:&lt;LocalID&gt;

Where &lt;OrgID&gt; and &lt;LocalID&gt; are separated by a colon (:), and where &lt;OrgID&gt; must include a copyrighted, trademarked, or otherwise unique name that is owned by the business entity that is creating or defining the InstanceID or that is a registered ID assigned to the business entity by a recognized global authority. (This requirement is similar to the &lt;Schema Name&gt;\_&lt;Class Name&gt; structure of Schema class names.) In addition, to ensure uniqueness, &lt;OrgID&gt; must not contain a colon (:). When using this algorithm, the first colon to appear in InstanceID must appear between &lt;OrgID&gt; and &lt;LocalID&gt;.

&lt;LocalID&gt; is chosen by the business entity and should not be reused to identify different underlying (real-world) elements. If the above "preferred" algorithm is not used, the defining entity must assure that the resulting InstanceID is not reused across any InstanceIDs produced by this or other providers for the NameSpace of this instance.

For DMTF-defined instances, the "preferred" algorithm must be used with the &lt;OrgID&gt; set to CIM.

This property is inherited from [**CIM\_SettingData**](cim-settingdata.md).

</dd> <dt>

**NoSinglePointOfFailure**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates the desired value for No Single Point of Failure. Possible values are false = single point of failure, and true = no single point of failure.

This property is inherited from [**CIM\_StorageSetting**](cim-storagesetting.md).

</dd> <dt>

**PackageRedundancyGoal**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageSetting.PackageRedundancyMax", "CIM\_StorageSetting.PackageRedundancyMin")
</dt> </dl>

PackageRedundancyGoal describes the desired number of redundant packages to be used. For example, in the storage domain, package redundancy describes how many disk spindles can fail without data loss including, at most, one spare. An example would be RAID5 with a spare disk which would have a PackageRedundancy of 2. Possible values are 0 to n. The bounds (max and min) for redundancy are defined using the properties, PackageRedundancyMax and PackageRedundancyMin.

This property is inherited from [**CIM\_StorageSetting**](cim-storagesetting.md).

</dd> <dt>

**PackageRedundancyMax**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageSetting.PackageRedundancyMin", "CIM\_StorageSetting.PackageRedundancyGoal")
</dt> </dl>

PackageRedundancyMax describes the maximum number of redundant packages to be used. For example, in the storage domain, package redundancy describes how many disk spindles can fail without data loss including, at most, one spare. An example would be RAID5 with a spare disk which would have a PackageRedundancy of 2. Possible values are 0 to n. The desired redundancy is specified using PackageRedundancyGoal, while the minimum is defined by PackageRedundancyMin.

This property is inherited from [**CIM\_StorageSetting**](cim-storagesetting.md).

</dd> <dt>

**PackageRedundancyMin**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageSetting.PackageRedundancyMax", "CIM\_StorageSetting.PackageRedundancyGoal")
</dt> </dl>

PackageRedundancyMin describes the minimum number of redundant packages to be used. For example, in the storage domain, package redundancy describes how many disk spindles can fail without data loss including, at most, one spare. An example would be RAID5 with a spare disk which would have a PackageRedundancy of 2. Possible values are 0 to n. The desired redundancy is specified using PackageRedundancyGoal, while the maximum is defined by PackageRedundancyMax.

This property is inherited from [**CIM\_StorageSetting**](cim-storagesetting.md).

</dd> <dt>

**ParityLayout**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

ParityLayout specifies whether a parity-based storage organization is using rotated or non-rotated parity. When used in a goal setting instance, ParityLayout is the desired value. It MUST be set to NULL if the scoping StorageCapablities indicates that it is not supported in this context. If the property is supported, and is part of StorageSettingWithHints it MAY be set to NULL. If used it will constrain the effects of Hint selections. When used in a Setting instance associated to a Volume, this property indicates the specific value that the Volume was created with.

This property is inherited from [**CIM\_StorageSetting**](cim-storagesetting.md).

<dt>

<span id="Non-rotated_Parity"></span><span id="non-rotated_parity"></span><span id="NON-ROTATED_PARITY"></span>

**Non-rotated Parity** (1)


</dt> <dd></dd> <dt>

<span id="Rotated_Parity"></span><span id="rotated_parity"></span><span id="ROTATED_PARITY"></span>

**Rotated Parity** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**UserDataStripeDepth**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("Bytes"), [**MinValue**](https://msdn.microsoft.com/library/aa393650) (1), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageSetting.UserDataStripeDepthMax", "CIM\_StorageSetting.UserDataStripeDepthMin")
</dt> </dl>

UserDataStripeDepth describes the number of bytes forming a strip in common striping-based storage organizations. The strip is defined as the size of the portion of a stripe that lies on one extent. Thus, ExtentStripeLength \* UserDataStripeDepth will yield the size of one stripe of user data. When used in a goal setting instance, UserDataStripeDepth is the optimal desired value. The bounds (max and min) for Stripe Depth are defined using the properties UserDataStripeDepthMax and UserDataStripeDepthMin. UserDataStripeDepth MUST be set to NULL if the scoping StorageCapablities indicates that it is not supported in this context. If the property is supported, and is part of StorageSettingWithHints it MAY be set to NULL. If used it will constrain the effects of Hint selections. When used in a Setting instance associated to a Volume, this property indicates the specific value that the Volume was created with, and UserDataStripeDepthMin and UserDataStripeDepthMax will be set to the same specific value.

This property is inherited from [**CIM\_StorageSetting**](cim-storagesetting.md).

</dd> <dt>

**UserDataStripeDepthMax**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("Bytes"), [**MinValue**](https://msdn.microsoft.com/library/aa393650) (1), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageSetting.UserDataStripeDepthMin", "CIM\_StorageSetting.UserDataStripeDepth")
</dt> </dl>

UserDataStripeDepth describes the number of bytes forming a strip in common striping-based storage organizations. The strip is defined as the size of the portion of a stripe that lies on one extent. Thus, ExtentStripeLength \* UserDataStripeDepth will yield the size of one stripe of user data. When used in a goal setting instance, UserDataStripeDepthMax is the maximum acceptable value. The desired Stripe Depth is specified using UserDataStripeDepthGoal, while the minimum is defined by UserDataStripeDepthMin. UserDataStripeDepthMax MUST be set to NULL if the scoping StorageCapablities indicates that it is not supported in this context. If the property is supported, and is part of StorageSettingwWithHints it MAY be set to NULL. If used it will constrain the effects of Hint selections. When used in a Setting instance associated to a Volume, this property is set to the specific value of UserDataStripeDepth.

This property is inherited from [**CIM\_StorageSetting**](cim-storagesetting.md).

</dd> <dt>

**UserDataStripeDepthMin**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("Bytes"), [**MinValue**](https://msdn.microsoft.com/library/aa393650) (1), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageSetting.UserDataStripeDepthMax", "CIM\_StorageSetting.UserDataStripeDepth")
</dt> </dl>

UserDataStripeDepth describes the number of bytes forming a strip in common striping-based storage organizations. The strip is defined as the size of the portion of a stripe that lies on one extent. Thus, ExtentStripeLength \* UserDataStripeDepth will yield the size of one stripe of user data. When used in a goal setting instance, UserDataStripeDepthMin is the minimum acceptable value. The desired Stripe Depth is specified using UserDataStripeDepth, while the maximum is defined by UserDataStripeDepthMax. UserDataStripeDepthMin MUST be set to NULL if the scoping StorageCapablities indicates that it is not supported in this context. If the property is supported, and is part of StorageSettingWithHints it MAY be set to NULL. If used it will constrain the effects of Hint selections. When used in a Setting instance associated to a Volume, this property is set to the specific value of UserDataStripeDepth.

This property is inherited from [**CIM\_StorageSetting**](cim-storagesetting.md).

</dd> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_StorageSetting**](cim-storagesetting.md)
</dt> <dt>

[iSCSI Target Server Reference](https://msdn.microsoft.com/library/hh830439)
</dt> <dt>

[**MSISCSITARGET\_StorageCapabilities**](msiscsitarget-storagecapabilities.md)
</dt> <dt>

[**MSISCSITARGET\_StorageConfigurationService**](msiscsitarget-storageconfigurationservice.md)
</dt> <dt>

[**MSISCSITARGET\_StorageVolume**](msiscsitarget-storagevolume.md)
</dt> </dl>

 

 





