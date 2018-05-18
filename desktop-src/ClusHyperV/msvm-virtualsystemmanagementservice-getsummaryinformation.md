---
title: GetSummaryInformation method of the Msvm\_VirtualSystemManagementService class
description: Returns summary information for VMs and VM snapshots.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'c0a9b0d0-fa09-4fd2-8a7f-7d5716d866e6'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetSummaryInformation method", "GetSummaryInformation method, Msvm_VirtualSystemManagementService class", "Msvm_VirtualSystemManagementService class, GetSummaryInformation method"]
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemManagementService.GetSummaryInformation
api_location:
- VMMS.exe
api_type:
- COM
---

# GetSummaryInformation method of the Msvm\_VirtualSystemManagementService class

Returns summary information for VMs and VM snapshots.

## Syntax


```mof
uint32 GetSummaryInformation(
  [in]  CIM_VirtualSystemSettingData REF SettingData[],
  [in]  uint32                           RequestedInformation[],
  [out] Msvm_SummaryInformationBase      SummaryInformation[]
);
```



## Parameters

<dl> <dt>

*SettingData* \[in\]
</dt> <dd>

An array that contains references to [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md) instances that specify setting data for the VMs and VM snapshots. If this parameter is **NULL**, information for all VMs is retrieved.

</dd> <dt>

*RequestedInformation* \[in\]
</dt> <dd>

An array that indicates the settings to retrieve in the **SettingData** array. Values in the 0-99 range apply to both VMs and snapshots. Values in the 100-199 range apply to VMs only, and will be ignored for elements of **SettingData** that represent snapshots. Values in the 200-299 range apply to snapshots only, and will be ignored for elements of **SettingData** that represent virtual machines.

The possible return values are:

<dt>

<span id="Name"></span><span id="name"></span><span id="NAME"></span>

**Name** (0)


</dt> <dd></dd> <dt>

<span id="Element_Name"></span><span id="element_name"></span><span id="ELEMENT_NAME"></span>

**Element Name** (1)


</dt> <dd></dd> <dt>

<span id="Creation_Time"></span><span id="creation_time"></span><span id="CREATION_TIME"></span>

**Creation Time** (2)


</dt> <dd></dd> <dt>

<span id="Notes"></span><span id="notes"></span><span id="NOTES"></span>

**Notes** (3)


</dt> <dd></dd> <dt>

<span id="Number_of_Processors"></span><span id="number_of_processors"></span><span id="NUMBER_OF_PROCESSORS"></span>

**Number of Processors** (4)


</dt> <dd></dd> <dt>

<span id="Small_Thumbnail_Image__80x60_"></span><span id="small_thumbnail_image__80x60_"></span><span id="SMALL_THUMBNAIL_IMAGE__80X60_"></span>

**Small Thumbnail Image (80x60)** (5)


</dt> <dd></dd> <dt>

<span id="Medium_Thumbnail_Image__160x120_"></span><span id="medium_thumbnail_image__160x120_"></span><span id="MEDIUM_THUMBNAIL_IMAGE__160X120_"></span>

**Medium Thumbnail Image (160x120)** (6)


</dt> <dd></dd> <dt>

<span id="Large_Thumbnail_Image__320x240_"></span><span id="large_thumbnail_image__320x240_"></span><span id="LARGE_THUMBNAIL_IMAGE__320X240_"></span>

**Large Thumbnail Image (320x240)** (7)


</dt> <dd></dd> <dt>

<span id="AllocatedGPU"></span><span id="allocatedgpu"></span><span id="ALLOCATEDGPU"></span>

**AllocatedGPU** (8)


</dt> <dd></dd> <dt>

<span id="VirtualSwitchNames"></span><span id="virtualswitchnames"></span><span id="VIRTUALSWITCHNAMES"></span>

**VirtualSwitchNames** (9)


</dt> <dd></dd> <dt>

<span id="Version"></span><span id="version"></span><span id="VERSION"></span>

**Version** (10)


</dt> <dd></dd> <dt>

<span id="Shielded"></span><span id="shielded"></span><span id="SHIELDED"></span>

**Shielded** (11)


</dt> <dd></dd> <dt>

<span id="EnabledState"></span><span id="enabledstate"></span><span id="ENABLEDSTATE"></span>

**EnabledState** (100)


</dt> <dd></dd> <dt>

<span id="ProcessorLoad"></span><span id="processorload"></span><span id="PROCESSORLOAD"></span>

**ProcessorLoad** (101)


</dt> <dd></dd> <dt>

<span id="ProcessorLoadHistory"></span><span id="processorloadhistory"></span><span id="PROCESSORLOADHISTORY"></span>

**ProcessorLoadHistory** (102)


</dt> <dd></dd> <dt>

<span id="MemoryUsage"></span><span id="memoryusage"></span><span id="MEMORYUSAGE"></span>

**MemoryUsage** (103)


</dt> <dd></dd> <dt>

<span id="Heartbeat"></span><span id="heartbeat"></span><span id="HEARTBEAT"></span>

**Heartbeat** (104)


</dt> <dd></dd> <dt>

<span id="Uptime"></span><span id="uptime"></span><span id="UPTIME"></span>

**Uptime** (105)


</dt> <dd></dd> <dt>

<span id="GuestOperatingSystem"></span><span id="guestoperatingsystem"></span><span id="GUESTOPERATINGSYSTEM"></span>

**GuestOperatingSystem** (106)


</dt> <dd></dd> <dt>

<span id="Snapshots"></span><span id="snapshots"></span><span id="SNAPSHOTS"></span>

**Snapshots** (107)


</dt> <dd></dd> <dt>

<span id="AsynchronousTasks"></span><span id="asynchronoustasks"></span><span id="ASYNCHRONOUSTASKS"></span>

**AsynchronousTasks** (108)


</dt> <dd></dd> <dt>

<span id="HealthState"></span><span id="healthstate"></span><span id="HEALTHSTATE"></span>

**HealthState** (109)


</dt> <dd></dd> <dt>

<span id="OperationalStatus"></span><span id="operationalstatus"></span><span id="OPERATIONALSTATUS"></span>

**OperationalStatus** (110)


</dt> <dd></dd> <dt>

<span id="StatusDescriptions"></span><span id="statusdescriptions"></span><span id="STATUSDESCRIPTIONS"></span>

**StatusDescriptions** (111)


</dt> <dd></dd> <dt>

<span id="MemoryAvailable"></span><span id="memoryavailable"></span><span id="MEMORYAVAILABLE"></span>

**MemoryAvailable** (112)


</dt> <dd></dd> <dt>

<span id="AvailableMemoryBuffer"></span><span id="availablememorybuffer"></span><span id="AVAILABLEMEMORYBUFFER"></span>

**AvailableMemoryBuffer** (113)


</dt> <dd></dd> <dt>

<span id="Replication_Mode"></span><span id="replication_mode"></span><span id="REPLICATION_MODE"></span>

**Replication Mode** (114)


</dt> <dd></dd> <dt>

<span id="Replication_State"></span><span id="replication_state"></span><span id="REPLICATION_STATE"></span>

**Replication State** (115)


</dt> <dd></dd> <dt>

<span id="Replication_HealthTest_Replica_System"></span><span id="replication_healthtest_replica_system"></span><span id="REPLICATION_HEALTHTEST_REPLICA_SYSTEM"></span>

**Replication HealthTest Replica System** (116)


</dt> <dd></dd> <dt>

<span id="Application_Health"></span><span id="application_health"></span><span id="APPLICATION_HEALTH"></span>

**Application Health** (117)


</dt> <dd></dd> <dt>

<span id="SwapFilesInUse"></span><span id="swapfilesinuse"></span><span id="SWAPFILESINUSE"></span>

**SwapFilesInUse** (120)


</dt> <dd></dd> <dt>

<span id="IntegrationServicesVersionState"></span><span id="integrationservicesversionstate"></span><span id="INTEGRATIONSERVICESVERSIONSTATE"></span>

**IntegrationServicesVersionState** (121)


</dt> <dd></dd> <dt>

<span id="MemorySpansPhysicalNumaNodes"></span><span id="memoryspansphysicalnumanodes"></span><span id="MEMORYSPANSPHYSICALNUMANODES"></span>

**MemorySpansPhysicalNumaNodes** (123)


</dt> <dd></dd> <dt>

<span id="OtherEnabledState"></span><span id="otherenabledstate"></span><span id="OTHERENABLEDSTATE"></span>

**OtherEnabledState** (132)


</dt> <dd></dd> </dl> </dd> <dt>

*SummaryInformation* \[out\]
</dt> <dd>

An array of [**Msvm\_SummaryInformationBase**](msvm-summaryinformationbase.md) instances that contain the requested summary information. Properties that are not specified in the **RequestedInformation** parameter are set to **NULL**.

</dd> </dl>

## Return value

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Failed** (32768)
</dt> <dt>

**Access Denied** (32769)
</dt> <dt>

**Not Supported** (32770)
</dt> <dt>

**Status is unknown** (32771)
</dt> <dt>

**Timeout** (32772)
</dt> <dt>

**Invalid parameter** (32773)
</dt> <dt>

**System is in use** (32774)
</dt> <dt>

**Invalid state for this operation** (32775)
</dt> <dt>

**Incorrect data type** (32776)
</dt> <dt>

**System is not available** (32777)
</dt> <dt>

**Out of memory** (32778)
</dt> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md)
</dt> <dt>

[**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md)
</dt> <dt>

[**Msvm\_SummaryInformationBase**](msvm-summaryinformationbase.md)
</dt> </dl>

 

 





