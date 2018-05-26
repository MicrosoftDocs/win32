---
title: MSFT\_SMSystem class
description: Represents a computer system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: da17ee78-c7c7-41ae-b496-e2047149109f
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_SMSystem class
- MSFT_SMSystem class, described
topic_type:
- apiref
api_name:
- MSFT_SMSystem
- MSFT_SMSystem.ObjectId
- MSFT_SMSystem.Identifier
- MSFT_SMSystem.DisplayName
- MSFT_SMSystem.Name
- MSFT_SMSystem.NameFormat
- MSFT_SMSystem.OtherIdentifyingInfo
- MSFT_SMSystem.IdentifyingDescriptions
- MSFT_SMSystem.ManagementServer
- MSFT_SMSystem.HealthStatus
- MSFT_SMSystem.HealthStatusDescription
- MSFT_SMSystem.OperationalStatus
- MSFT_SMSystem.StatusDescription
- MSFT_SMSystem.Manufacturer
- MSFT_SMSystem.Model
- MSFT_SMSystem.SerialNumber
- MSFT_SMSystem.Tag
- MSFT_SMSystem.FirmwareVersion
- MSFT_SMSystem.CacheLevel
api_location:
- StorageService.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_SMSystem class

Represents a computer system.

**Windows Server 2012 R2 and Windows Server 2012:** This class does not inherit from [**MSFT\_SMStorageObject**](msft-smstorageobject.md) before Windows Server 2016.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("WMIStorage"), AMENDMENT]
class MSFT_SMSystem : MSFT_SMStorageObject
{
  String ObjectId;
  String Identifier;
  String DisplayName;
  String Name;
  String NameFormat;
  String OtherIdentifyingInfo[];
  String IdentifyingDescriptions[];
  String ManagementServer;
  uint16 HealthStatus;
  string HealthStatusDescription;
  uint16 OperationalStatus[];
  string StatusDescription;
  string Manufacturer;
  string Model;
  string SerialNumber;
  string Tag;
  string FirmwareVersion;
  Uint16 CacheLevel;
};
```

## Members

The **MSFT\_SMSystem** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_SMSystem** class has these methods.



| Method                                                                                   | Description                                                                                                                                                                                                                 |
|:-----------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreatePool**](createpool-msft-smsystem.md)                                           | Creates a concrete pool.<br/>                                                                                                                                                                                         |
| [**CreateReplicationGroup**](createreplicationgroup-msft-smsystem.md)                   | Creates a replication group.<br/> **Windows Server 2012 R2 and Windows Server 2012:** This method is not available before Windows Server 2016.<br/>                                                             |
| [**CreateReplicationRelationship**](createreplicationrelationship-msft-smsystem.md)     | Creates two replication groups and then creates a replication relationship between them.<br/> **Windows Server 2012 R2 and Windows Server 2012:** This method is not available before Windows Server 2016.<br/> |
| [**CreateStorageGroup**](createstoragegroup-msft-smsystem.md)                           | Creates a storage group.<br/>                                                                                                                                                                                         |
| [**CreateStorageGroupEx**](createstoragegroupex-msft-smsystem.md)                       | Creates a storage group.<br/>                                                                                                                                                                                         |
| [**CreateStorageHardwareID**](createstoragehardwareid-msft-smsystem.md)                 | Creates a new storage hardware ID.<br/>                                                                                                                                                                               |
| [**CreateStorageVolume**](createstoragevolume-msft-smsystem.md)                         | Start a job to create a storage volume.<br/>                                                                                                                                                                          |
| [**DeleteReplicationRelationship**](deletereplicationrelationship-msft-smsystem.md)     | Deletes a replication relationship between two replication groups.<br/> **Windows Server 2012 R2 and Windows Server 2012:** This method is not available before Windows Server 2016.<br/>                       |
| [**Diagnose**](diagnose-msft-smsystem.md)                                               | Attempts to find more information about the health state of an array.<br/>                                                                                                                                            |
| [**GetPoolObjectIdFromJob**](getpoolobjectidfromjob-msft-smsystem.md)                   | Returns a object ID for the storage pool that is associated with the specified job.<br/>                                                                                                                              |
| [**GetStorageGroupObjectIDFromJob**](getstoragegroupobjectidfromjob-msft-smsystem.md)   | Returns a Storage Group Object Id based on a Job reference.<br/>                                                                                                                                                      |
| [**GetStorageVolumeNameFromJob**](getstoragevolumenamefromjob-msft-smsystem.md)         | This method is not currently available.<br/> **Windows Server 2012:** Returns a storage volume name associated with the specified job.<br/>                                                                     |
| [**GetStorageVolumeObjectIDFromJob**](getstoragevolumeobjectidfromjob-msft-smsystem.md) | Returns a storage volume object id based on a Job reference.<br/>                                                                                                                                                     |



 

### Properties

The **MSFT\_SMSystem** class has these properties.

<dl> <dt>

**CacheLevel**
</dt> <dd> <dl> <dt>

Data type: **Uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the depth of discovery of objects in cache.

The possible values are.

<dt>

<span id="Top-Level"></span><span id="top-level"></span><span id="TOP-LEVEL"></span>

**Top-Level** (0)


</dt> <dd></dd> <dt>

<span id="Mid-Level"></span><span id="mid-level"></span><span id="MID-LEVEL"></span>

**Mid-Level** (1)


</dt> <dd></dd> <dt>

<span id="AllExceptDiskDrives"></span><span id="allexceptdiskdrives"></span><span id="ALLEXCEPTDISKDRIVES"></span>

**AllExceptDiskDrives** (2)


</dt> <dd></dd> <dt>

<span id="All"></span><span id="all"></span><span id="ALL"></span>

**All** (3)


</dt> <dd></dd> </dl>

</dd> <dt>

**DisplayName**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The user-friendly name of the system.

</dd> <dt>

**FirmwareVersion**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_SoftwareIdentity**](https://msdn.microsoft.com/library/mt432317).**VersionString**")
</dt> </dl>

The version number of the system firmware.

</dd> <dt>

**HealthStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed")
</dt> </dl>

The status of the system.

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

**HealthStatusDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Describes the health status in text.

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

**IdentifyingDescriptions**
</dt> <dd> <dl> <dt>

Data type: **String** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array that contains descriptions of the format used in the custom identifiers in **OtherIdentifyingInfo**. There must be a 1:1 mapping between this array and **OtherIdentifyingInfo**.

</dd> <dt>

**ManagementServer**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the management server that manages the system.

</dd> <dt>

**Manufacturer**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_PhysicalPackage**](https://msdn.microsoft.com/library/aa387969).**Manufacturer**")
</dt> </dl>

The name of the manufacturer of the system.

</dd> <dt>

**Model**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_PhysicalPackage**](https://msdn.microsoft.com/library/aa387969).**Model**")
</dt> </dl>

The model name of the system.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The system defined name of the system.

</dd> <dt>

**NameFormat**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the format of **Name** property.

The possible values are.

<dt>



 ("Other")


</dt> <dd></dd> <dt>



 ("IP")


</dt> <dd></dd> <dt>



 ("Dial")


</dt> <dd></dd> <dt>



 ("HID")


</dt> <dd></dd> <dt>



 ("NWA")


</dt> <dd></dd> <dt>



 ("HWA")


</dt> <dd></dd> <dt>



 ("X25")


</dt> <dd></dd> <dt>



 ("ISDN")


</dt> <dd></dd> <dt>



 ("IPX")


</dt> <dd></dd> <dt>



 ("DCC")


</dt> <dd></dd> <dt>



 ("ICD")


</dt> <dd></dd> <dt>



 ("E.164")


</dt> <dd></dd> <dt>



 ("SNA")


</dt> <dd></dd> <dt>



 ("OID/OSI")


</dt> <dd></dd> <dt>



 ("WWN")


</dt> <dd></dd> <dt>



 ("NAA")


</dt> <dd></dd> </dl>

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

**OperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ComputerSystem**](https://msdn.microsoft.com/library/aa387219).**OperationalStatus**")
</dt> </dl>

An array that contains the operational status of the system.

The possible values are.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="OK"></span><span id="ok"></span>

**OK** (2)


</dt> <dd></dd> <dt>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>

**Degraded** (3)


</dt> <dd></dd> <dt>

<span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span>

**Stressed** (4)


</dt> <dd></dd> <dt>

<span id="Predictive_Failure"></span><span id="predictive_failure"></span><span id="PREDICTIVE_FAILURE"></span>

**Predictive Failure** (5)


</dt> <dd></dd> <dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>

**Error** (6)


</dt> <dd></dd> <dt>

<span id="Non-Recoverable_Error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span>

**Non-Recoverable Error** (7)


</dt> <dd></dd> <dt>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>

**Starting** (8)


</dt> <dd></dd> <dt>

<span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span>

**Stopping** (9)


</dt> <dd></dd> <dt>

<span id="Stopped"></span><span id="stopped"></span><span id="STOPPED"></span>

**Stopped** (10)


</dt> <dd></dd> <dt>

<span id="In_Service"></span><span id="in_service"></span><span id="IN_SERVICE"></span>

**In Service** (11)


</dt> <dd></dd> <dt>

<span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span>

**No Contact** (12)


</dt> <dd></dd> <dt>

<span id="Lost_Communication"></span><span id="lost_communication"></span><span id="LOST_COMMUNICATION"></span>

**Lost Communication** (13)


</dt> <dd></dd> <dt>

<span id="Aborted"></span><span id="aborted"></span><span id="ABORTED"></span>

**Aborted** (14)


</dt> <dd></dd> <dt>

<span id="Dormant"></span><span id="dormant"></span><span id="DORMANT"></span>

**Dormant** (15)


</dt> <dd></dd> <dt>

<span id="Supporting_Entity_in_Error"></span><span id="supporting_entity_in_error"></span><span id="SUPPORTING_ENTITY_IN_ERROR"></span>

**Supporting Entity in Error** (16)


</dt> <dd></dd> <dt>

<span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span>

**Completed** (17)


</dt> <dd></dd> <dt>

<span id="Power_Mode"></span><span id="power_mode"></span><span id="POWER_MODE"></span>

**Power Mode** (18)


</dt> <dd></dd> </dl>

</dd> <dt>

**OtherIdentifyingInfo**
</dt> <dd> <dl> <dt>

Data type: **String** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array that contains custom identifiers for the system. If this field is set, **IdentifyingDescriptions** must also be set.

</dd> <dt>

**SerialNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_PhysicalPackage**](https://msdn.microsoft.com/library/aa387969).**SerialNumber**")
</dt> </dl>

The serial number of the system.

</dd> <dt>

**StatusDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A description of the **OperationalStatus** value.

</dd> <dt>

**Tag**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_PhysicalPackage**](https://msdn.microsoft.com/library/aa387969).**Tag**")
</dt> </dl>

The ID tag of the system.

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_SMStorageObject**](msft-smstorageobject.md)
</dt> <dt>

[Windows Storage Management WMI Provider](windows-storage-management-wmi-provider-portal.md)
</dt> </dl>

 

 





