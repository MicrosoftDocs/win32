---
description: Returns virtual machine summary information.
ms.assetid: CDDC2B5A-8172-4E6D-A206-CEAB9E54C69A
title: GetSummaryInformation method of the Msvm_VirtualSystemManagementService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_VirtualSystemManagementService.GetSummaryInformation
api_type: 
- COM
api_location: 
- vmms.exe
---

# GetSummaryInformation method of the Msvm\_VirtualSystemManagementService class

Returns virtual machine summary information.

## Syntax


```mof
uint32 GetSummaryInformation(
  [in]  CIM_VirtualSystemSettingData REF SettingData[],
  [in]  uint32                           RequestedInformation[],
  [out] Msvm_SummaryInformationBase      SummaryInformation[]
);
```



## Parameters

<dl> <dt>

*SettingData* \[in\]
</dt> <dd>

Type: **CIM\_VirtualSystemSettingData\[\]**

An array of [**CIM\_VirtualSystemSettingData**](/previous-versions//cc136954(v=vs.85)) instances that specify the virtual machines or snapshots for which information is to be retrieved. If this parameter is **Null**, information for all virtual machines is retrieved.

</dd> <dt>

*RequestedInformation* \[in\]
</dt> <dd>

Type: **uint32\[\]**

An array of enumeration values, which correspond to the properties in the [**Msvm\_SummaryInformation**](msvm-summaryinformation.md) class, that specify the data to retrieve for the virtual machines and snapshots specified in the *SettingData* array.

<dt>

<span id="Name"></span><span id="name"></span><span id="NAME"></span>

<span id="Name"></span><span id="name"></span><span id="NAME"></span>**Name** (0)


</dt> <dd>

This corresponds to the **Name** property of the [**Msvm\_SummaryInformation**](msvm-summaryinformation.md) class.

</dd> <dt>

<span id="Element_Name"></span><span id="element_name"></span><span id="ELEMENT_NAME"></span>

<span id="Element_Name"></span><span id="element_name"></span><span id="ELEMENT_NAME"></span>**Element Name** (1)


</dt> <dd>

This corresponds to the **ElementName** property of the [**Msvm\_SummaryInformation**](msvm-summaryinformation.md) class.

</dd> <dt>

<span id="Creation_Time"></span><span id="creation_time"></span><span id="CREATION_TIME"></span>

<span id="Creation_Time"></span><span id="creation_time"></span><span id="CREATION_TIME"></span>**Creation Time** (2)


</dt> <dd>

This corresponds to the **CreationTime** property of the [**Msvm\_SummaryInformation**](msvm-summaryinformation.md) class.

</dd> <dt>

<span id="Notes"></span><span id="notes"></span><span id="NOTES"></span>

<span id="Notes"></span><span id="notes"></span><span id="NOTES"></span>**Notes** (3)


</dt> <dd>

This corresponds to the **Notes** property of the [**Msvm\_SummaryInformation**](msvm-summaryinformation.md) class.

</dd> <dt>

<span id="Number_of_Processors"></span><span id="number_of_processors"></span><span id="NUMBER_OF_PROCESSORS"></span>

<span id="Number_of_Processors"></span><span id="number_of_processors"></span><span id="NUMBER_OF_PROCESSORS"></span>**Number of Processors** (4)


</dt> <dd>

This corresponds to the **NumberOfProcessors** property of the [**Msvm\_SummaryInformation**](msvm-summaryinformation.md) class.

</dd> <dt>

<span id="Small_Thumbnail_Image__80x60_"></span><span id="small_thumbnail_image__80x60_"></span><span id="SMALL_THUMBNAIL_IMAGE__80X60_"></span>

<span id="Small_Thumbnail_Image__80x60_"></span><span id="small_thumbnail_image__80x60_"></span><span id="SMALL_THUMBNAIL_IMAGE__80X60_"></span>**Small Thumbnail Image (80x60)** (5)


</dt> <dd>

This corresponds to the **ThumbnailImage** property of the [**Msvm\_SummaryInformation**](msvm-summaryinformation.md) class. A thumbnail image with the dimensions of 80 60 will be retrieved.

</dd> <dt>

<span id="Medium_Thumbnail_Image__160x120_"></span><span id="medium_thumbnail_image__160x120_"></span><span id="MEDIUM_THUMBNAIL_IMAGE__160X120_"></span>

<span id="Medium_Thumbnail_Image__160x120_"></span><span id="medium_thumbnail_image__160x120_"></span><span id="MEDIUM_THUMBNAIL_IMAGE__160X120_"></span>**Medium Thumbnail Image (160x120)** (6)


</dt> <dd>

This corresponds to the **ThumbnailImage** property of the [**Msvm\_SummaryInformation**](msvm-summaryinformation.md) class. A thumbnail image with the dimensions of 160 120 will be retrieved.

</dd> <dt>

<span id="Large_Thumbnail_Image__320x240_"></span><span id="large_thumbnail_image__320x240_"></span><span id="LARGE_THUMBNAIL_IMAGE__320X240_"></span>

<span id="Large_Thumbnail_Image__320x240_"></span><span id="large_thumbnail_image__320x240_"></span><span id="LARGE_THUMBNAIL_IMAGE__320X240_"></span>**Large Thumbnail Image (320x240)** (7)


</dt> <dd>

This corresponds to the **ThumbnailImage** property of the [**Msvm\_SummaryInformation**](msvm-summaryinformation.md) class. A thumbnail image with the dimensions of 320 240 will be retrieved.

</dd> <dt>

<span id="AllocatedGPU"></span><span id="allocatedgpu"></span><span id="ALLOCATEDGPU"></span>

<span id="AllocatedGPU"></span><span id="allocatedgpu"></span><span id="ALLOCATEDGPU"></span>**AllocatedGPU** (8)


</dt> <dd>

This corresponds to the **AllocatedGPU** property of the [**Msvm\_SummaryInformation**](msvm-summaryinformation.md) class.

</dd> <dt>

<span id="VirtualSwitchNames"></span><span id="virtualswitchnames"></span><span id="VIRTUALSWITCHNAMES"></span>

<span id="VirtualSwitchNames"></span><span id="virtualswitchnames"></span><span id="VIRTUALSWITCHNAMES"></span>**VirtualSwitchNames** (9)


</dt> <dd></dd> <dt>

<span id="Version"></span><span id="version"></span><span id="VERSION"></span>

<span id="Version"></span><span id="version"></span><span id="VERSION"></span>**Version** (10)


</dt> <dd>

> [!Note]  
> Added in Windows 10 and Windows Server 2016.

 

</dd> <dt>

<span id="Shielded"></span><span id="shielded"></span><span id="SHIELDED"></span>

<span id="Shielded"></span><span id="shielded"></span><span id="SHIELDED"></span>**Shielded** (11)


</dt> <dd>

> [!Note]  
> Added in Windows 10, version 1703 and Windows Server 2016.

 

</dd> <dt>

<span id="EnabledState"></span><span id="enabledstate"></span><span id="ENABLEDSTATE"></span>

<span id="EnabledState"></span><span id="enabledstate"></span><span id="ENABLEDSTATE"></span>**EnabledState** (100)


</dt> <dd>

This corresponds to the **EnabledState** property of the [**Msvm\_SummaryInformation**](msvm-summaryinformation.md) class.

</dd> <dt>

<span id="ProcessorLoad"></span><span id="processorload"></span><span id="PROCESSORLOAD"></span>

<span id="ProcessorLoad"></span><span id="processorload"></span><span id="PROCESSORLOAD"></span>**ProcessorLoad** (101)


</dt> <dd>

This corresponds to the **ProcessorLoad** property of the [**Msvm\_SummaryInformation**](msvm-summaryinformation.md) class.

</dd> <dt>

<span id="ProcessorLoadHistory"></span><span id="processorloadhistory"></span><span id="PROCESSORLOADHISTORY"></span>

<span id="ProcessorLoadHistory"></span><span id="processorloadhistory"></span><span id="PROCESSORLOADHISTORY"></span>**ProcessorLoadHistory** (102)


</dt> <dd>

This corresponds to the **ProcessorLoadHistory** property of the [**Msvm\_SummaryInformation**](msvm-summaryinformation.md) class.

</dd> <dt>

<span id="MemoryUsage"></span><span id="memoryusage"></span><span id="MEMORYUSAGE"></span>

<span id="MemoryUsage"></span><span id="memoryusage"></span><span id="MEMORYUSAGE"></span>**MemoryUsage** (103)


</dt> <dd>

This corresponds to the **MemoryUsage** property of the [**Msvm\_SummaryInformation**](msvm-summaryinformation.md) class.

</dd> <dt>

<span id="Heartbeat"></span><span id="heartbeat"></span><span id="HEARTBEAT"></span>

<span id="Heartbeat"></span><span id="heartbeat"></span><span id="HEARTBEAT"></span>**Heartbeat** (104)


</dt> <dd>

This corresponds to the **Heartbeat** property of the [**Msvm\_SummaryInformation**](msvm-summaryinformation.md) class.

</dd> <dt>

<span id="Uptime"></span><span id="uptime"></span><span id="UPTIME"></span>

<span id="Uptime"></span><span id="uptime"></span><span id="UPTIME"></span>**Uptime** (105)


</dt> <dd>

This corresponds to the **UpTime** property of the [**Msvm\_SummaryInformation**](msvm-summaryinformation.md) class.

</dd> <dt>

<span id="GuestOperatingSystem"></span><span id="guestoperatingsystem"></span><span id="GUESTOPERATINGSYSTEM"></span>

<span id="GuestOperatingSystem"></span><span id="guestoperatingsystem"></span><span id="GUESTOPERATINGSYSTEM"></span>**GuestOperatingSystem** (106)


</dt> <dd>

This corresponds to the **GuestOperatingSystem** property of the [**Msvm\_SummaryInformation**](msvm-summaryinformation.md) class.

</dd> <dt>

<span id="Snapshots"></span><span id="snapshots"></span><span id="SNAPSHOTS"></span>

<span id="Snapshots"></span><span id="snapshots"></span><span id="SNAPSHOTS"></span>**Snapshots** (107)


</dt> <dd>

This corresponds to the **Snapshots** property of the [**Msvm\_SummaryInformation**](msvm-summaryinformation.md) class.

</dd> <dt>

<span id="AsynchronousTasks"></span><span id="asynchronoustasks"></span><span id="ASYNCHRONOUSTASKS"></span>

<span id="AsynchronousTasks"></span><span id="asynchronoustasks"></span><span id="ASYNCHRONOUSTASKS"></span>**AsynchronousTasks** (108)


</dt> <dd>

This corresponds to the **AsynchronousTasks** property of the [**Msvm\_SummaryInformation**](msvm-summaryinformation.md) class.

</dd> <dt>

<span id="HealthState"></span><span id="healthstate"></span><span id="HEALTHSTATE"></span>

<span id="HealthState"></span><span id="healthstate"></span><span id="HEALTHSTATE"></span>**HealthState** (109)


</dt> <dd>

This corresponds to the **HealthState** property of the [**Msvm\_SummaryInformation**](msvm-summaryinformation.md) class.

</dd> <dt>

<span id="OperationalStatus"></span><span id="operationalstatus"></span><span id="OPERATIONALSTATUS"></span>

<span id="OperationalStatus"></span><span id="operationalstatus"></span><span id="OPERATIONALSTATUS"></span>**OperationalStatus** (110)


</dt> <dd>

This corresponds to the **OperationalStatus** property of the [**Msvm\_SummaryInformation**](msvm-summaryinformation.md) class.

</dd> <dt>

<span id="StatusDescriptions"></span><span id="statusdescriptions"></span><span id="STATUSDESCRIPTIONS"></span>

<span id="StatusDescriptions"></span><span id="statusdescriptions"></span><span id="STATUSDESCRIPTIONS"></span>**StatusDescriptions** (111)


</dt> <dd>

This corresponds to the **StatusDescriptions** property of the [**Msvm\_SummaryInformation**](msvm-summaryinformation.md) class.

</dd> <dt>

<span id="MemoryAvailable"></span><span id="memoryavailable"></span><span id="MEMORYAVAILABLE"></span>

<span id="MemoryAvailable"></span><span id="memoryavailable"></span><span id="MEMORYAVAILABLE"></span>**MemoryAvailable** (112)


</dt> <dd>

This corresponds to the **MemoryAvailable** property of the [**Msvm\_SummaryInformation**](msvm-summaryinformation.md) class.

</dd> <dt>

<span id="AvailableMemoryBuffer"></span><span id="availablememorybuffer"></span><span id="AVAILABLEMEMORYBUFFER"></span>

<span id="AvailableMemoryBuffer"></span><span id="availablememorybuffer"></span><span id="AVAILABLEMEMORYBUFFER"></span>**AvailableMemoryBuffer** (113)


</dt> <dd>

This corresponds to the **AvailableMemoryBuffer** property of the [**Msvm\_SummaryInformation**](msvm-summaryinformation.md) class.

</dd> <dt>

<span id="Replication_Mode"></span><span id="replication_mode"></span><span id="REPLICATION_MODE"></span>

<span id="Replication_Mode"></span><span id="replication_mode"></span><span id="REPLICATION_MODE"></span>**Replication Mode** (114)


</dt> <dd>

This corresponds to the **ReplicationMode** property of the [**Msvm\_SummaryInformation**](msvm-summaryinformation.md) class.

</dd> <dt>

<span id="Replication_State"></span><span id="replication_state"></span><span id="REPLICATION_STATE"></span>

<span id="Replication_State"></span><span id="replication_state"></span><span id="REPLICATION_STATE"></span>**Replication State** (115)


</dt> <dd>

This corresponds to the **ReplicationState** property of the [**Msvm\_SummaryInformation**](msvm-summaryinformation.md) class.

</dd> <dt>

<span id="Replication_HealthTest_Replica_System"></span><span id="replication_healthtest_replica_system"></span><span id="REPLICATION_HEALTHTEST_REPLICA_SYSTEM"></span>

<span id="Replication_HealthTest_Replica_System"></span><span id="replication_healthtest_replica_system"></span><span id="REPLICATION_HEALTHTEST_REPLICA_SYSTEM"></span>**Replication HealthTest Replica System** (116)


</dt> <dd>

This corresponds to the **ReplicationHealth** property of the [**Msvm\_SummaryInformation**](msvm-summaryinformation.md) class.

</dd> <dt>

<span id="Application_Health"></span><span id="application_health"></span><span id="APPLICATION_HEALTH"></span>

<span id="Application_Health"></span><span id="application_health"></span><span id="APPLICATION_HEALTH"></span>**Application Health** (117)


</dt> <dd></dd> <dt>

<span id="ReplicationStateEx"></span><span id="replicationstateex"></span><span id="REPLICATIONSTATEEX"></span>

<span id="ReplicationStateEx"></span><span id="replicationstateex"></span><span id="REPLICATIONSTATEEX"></span>**ReplicationStateEx** (118)


</dt> <dd>

This corresponds to the **ReplicationState** property of the [**Msvm\_ReplicationRelationship**](msvm-replicationrelationship.md) class. This is array for all replication state values across primary and extended relationship. 0 index value is always for primary relationship, and if extended replication is enabled, it is returned in index 1.

</dd> <dt>

<span id="ReplicationHealthEx"></span><span id="replicationhealthex"></span><span id="REPLICATIONHEALTHEX"></span>

<span id="ReplicationHealthEx"></span><span id="replicationhealthex"></span><span id="REPLICATIONHEALTHEX"></span>**ReplicationHealthEx** (119)


</dt> <dd>

This corresponds to the **ReplicationHealth** property of the [**Msvm\_ReplicationRelationship**](msvm-replicationrelationship.md) class. This is array for all replication health values across primary and extended relationship. 0 index value is always for primary relationship, and if extended replication is enabled, it is returned in index 1.

</dd> <dt>

<span id="SwapFilesInUse"></span><span id="swapfilesinuse"></span><span id="SWAPFILESINUSE"></span>

<span id="SwapFilesInUse"></span><span id="swapfilesinuse"></span><span id="SWAPFILESINUSE"></span>**SwapFilesInUse** (120)


</dt> <dd>

This corresponds to the **SwapFilesInUse** property of the [**Msvm\_SummaryInformation**](msvm-summaryinformation.md) class.

</dd> <dt>

<span id="IntegrationServicesVersionState"></span><span id="integrationservicesversionstate"></span><span id="INTEGRATIONSERVICESVERSIONSTATE"></span>

<span id="IntegrationServicesVersionState"></span><span id="integrationservicesversionstate"></span><span id="INTEGRATIONSERVICESVERSIONSTATE"></span>**IntegrationServicesVersionState** (121)


</dt> <dd></dd> <dt>

<span id="ReplicationProviderId"></span><span id="replicationproviderid"></span><span id="REPLICATIONPROVIDERID"></span>

<span id="ReplicationProviderId"></span><span id="replicationproviderid"></span><span id="REPLICATIONPROVIDERID"></span>**ReplicationProviderId** (122)


</dt> <dd>

This corresponds to the **Name** property of the [**Msvm\_ReplicationProvider**](msvm-replicationprovider.md) class.

</dd> <dt>

<span id="MemorySpansPhysicalNumaNodes"></span><span id="memoryspansphysicalnumanodes"></span><span id="MEMORYSPANSPHYSICALNUMANODES"></span>

<span id="MemorySpansPhysicalNumaNodes"></span><span id="memoryspansphysicalnumanodes"></span><span id="MEMORYSPANSPHYSICALNUMANODES"></span>**MemorySpansPhysicalNumaNodes** (123)


</dt> <dd></dd> <dt>

<span id="IntegrationServicesVersionState"></span><span id="integrationservicesversionstate"></span><span id="INTEGRATIONSERVICESVERSIONSTATE"></span>

<span id="IntegrationServicesVersionState"></span><span id="integrationservicesversionstate"></span><span id="INTEGRATIONSERVICESVERSIONSTATE"></span>**IntegrationServicesVersionState** (132)


</dt> <dd>

This corresponds to the **IntegrationServicesVersionState** property of the [**Msvm\_SummaryInformation**](msvm-summaryinformation.md) class.

</dd> <dt>

<span id="OtherEnabledState"></span><span id="otherenabledstate"></span><span id="OTHERENABLEDSTATE"></span>

<span id="OtherEnabledState"></span><span id="otherenabledstate"></span><span id="OTHERENABLEDSTATE"></span>**OtherEnabledState** (132)


</dt> <dd>

This corresponds to the **OtherEnabledState** property of the [**Msvm\_SummaryInformation**](msvm-summaryinformation.md) class.

</dd> <dt>



 (133)


</dt> <dd></dd> </dl> </dd> <dt>

*SummaryInformation* \[out\]
</dt> <dd>

Type: **[**Msvm\_SummaryInformationBase**](msvm-summaryinformationbase.md)\[\]**

An array of [**Msvm\_SummaryInformationBase**](msvm-summaryinformationbase.md) instances containing the requested information for the virtual machines and/or snapshots specified in the *SettingData* array. This array will have the same number of elements as the *SettingData* array. Each of these entries will contain the **Name** property, even if this property was not requested. If the virtual machine or snapshot cannot be found or is unavailable, the **Name** property of the corresponding summary information entry will be empty.

Properties not specified in the *RequestedInformation* parameter will have a **Null** value.

> [!Note]  
> Datatype updated from in Windows 10, version 1703 from [**Msvm\_SummaryInformation**](msvm-summaryinformation.md).

 

</dd> </dl>

## Return value

Type: **uint32**

This method returns one of the following values.

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

## Remarks

Access to the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](/windows/desktop/WmiSdk/user-account-control-and-wmi).

## Examples

The following C# sample displays summary information. The referenced utilities can be found in [Common utilities for the virtualization samples (V2)](common-utilities-for-the-virtualization-samples-v2.md).

> [!IMPORTANT]
> To function correctly, the following code must be run on the virtual machine host server, and must be run with Administrator privileges.

 


```CSharp
public class GetSummaryInformationClassV2
{
    public static void GetSummaryInformation(string[] vmNames)
    {
        ManagementScope scope = new ManagementScope(@"root\virtualization\v2", null);
        ManagementObject virtualSystemService = Utility.GetServiceObject(scope, "Msvm_VirtualSystemManagementService");
        ManagementBaseObject inParams = virtualSystemService.GetMethodParameters("GetSummaryInformation");

        ManagementObject[] virtualSystemSettings = new ManagementObject[vmNames.Length];

        for (int i = 0; i < vmNames.Length; i++)
        {
            virtualSystemSettings[i] = GetVirtualSystemSetting(vmNames[i], scope);
        }

        UInt32[] requestedInformation = new UInt32[4];
        requestedInformation[0] = 1;    // ElementName
        requestedInformation[2] = 103;  // MemoryUsage
        requestedInformation[3] = 112;  // MemoryAvailable

        inParams["SettingData"] = virtualSystemSettings;
        inParams["RequestedInformation"] = requestedInformation;

        ManagementBaseObject outParams = virtualSystemService.InvokeMethod("GetSummaryInformation", inParams, null);

        if ((UInt32)outParams["ReturnValue"] == ReturnCode.Completed)
        {
            Console.WriteLine("Summary information was retrieved successfully.");

            ManagementBaseObject[] summaryInformationArray = 
                (ManagementBaseObject[])outParams["SummaryInformation"];

            foreach (ManagementBaseObject summaryInformation in summaryInformationArray)
            {
                Console.WriteLine("\nVirtual System Summary Information:");
                if ((null == summaryInformation["Name"]) || 
                    (summaryInformation["Name"].ToString().Length == 0))
                {
                    Console.WriteLine("\tThe VM or snapshot could not be found.");
                }
                else
                {
                    Console.WriteLine("\tName: {0}", summaryInformation["Name"].ToString());
                    foreach (UInt32 requested in requestedInformation)
                    {
                        switch (requested)
                        {
                            case 1:
                                Console.WriteLine("\tElementName: {0}", summaryInformation["ElementName"].ToString());
                                break;

                            case 103:
                                Console.WriteLine("\tMemoryUsage: {0}", summaryInformation["MemoryUsage"].ToString());
                                break;

                            case 112:
                                Console.WriteLine("\tMemoryAvailable: {0}", summaryInformation["MemoryAvailable"].ToString());
                                break;
                        }
                    }
                }
            }
        }
        else
        {
            Console.WriteLine("Failed to retrieve virtual system summary information");
        }

        inParams.Dispose();
        outParams.Dispose();
        virtualSystemService.Dispose();
    }

    public static ManagementObject GetVirtualSystemSetting(string vmName, ManagementScope scope)
    {
        ManagementObject virtualSystem = Utility.GetTargetComputer(vmName, scope);

        ManagementObjectCollection virtualSystemSettings = virtualSystem.GetRelated
         (
             "Msvm_VirtualSystemSettingData",
             "Msvm_SettingsDefineState",
             null,
             null,
             "SettingData",
             "ManagedElement",
             false,
             null
         );

        ManagementObject virtualSystemSetting = null;

        foreach (ManagementObject instance in virtualSystemSettings)
        {
            virtualSystemSetting = instance;
            break;
        }

        return virtualSystemSetting;

    }
}
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md)
</dt> <dt>

[**CIM\_VirtualSystemSettingData**](/previous-versions//cc136954(v=vs.85))
</dt> <dt>

[**Msvm\_SummaryInformation**](msvm-summaryinformation.md)
</dt> </dl>

 

