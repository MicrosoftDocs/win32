---
title: GetSummaryInformation method of the Msvm\_VirtualSystemManagementService class
description: Returns VM summary information.
ms.assetid: 'ebfbf3c1-07b4-41be-a041-09b173b241d8'
keywords: ["GetSummaryInformation method Hyper-V", "GetSummaryInformation method Hyper-V , Msvm_VirtualSystemManagementService class", "Msvm_VirtualSystemManagementService class Hyper-V , GetSummaryInformation method"]
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemManagementService.GetSummaryInformation
api_location:
- Root\Virtualization
api_type:
- COM
---

# GetSummaryInformation method of the Msvm\_VirtualSystemManagementService class

Returns virtual machine (VM) summary information.

## Syntax


```mof
uint32 GetSummaryInformation(
  [in]  CIM_VirtualSystemSettingData REF SettingData[],
  [in]  uint32                           RequestedInformation[],
  [out] Msvm_SummaryInformation          SummaryInformation[]
);
```



## Parameters

<dl> <dt>

*SettingData* \[in\]
</dt> <dd>

Type: **CIM\_VirtualSystemSettingData\[\]**

An array of [**CIM\_VirtualSystemSettingData**](https://msdn.microsoft.com/library/cc136954) instances that specifies the VMs and/or snapshots for which information is to be retrieved. If this parameter is **NULL**, information for all VMs is retrieved.

</dd> <dt>

*RequestedInformation* \[in\]
</dt> <dd>

Type: **uint32\[\]**

An array of enumeration values (which correspond to the properties in the [**Msvm\_SummaryInformation**](msvm-summaryinformation.md) class) that specifies the data to retrieve for the VMs and/or snapshots specified in the *SettingData* array. Values from 0 through 99 apply to both VMs and snapshots. Values from 100 through 199 apply to VMs only and are ignored for elements of *SettingData* that represent snapshots. Values from 200 through 299 are ignored.

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


</dt> <dd></dd> <dt>

<span id="Medium_Thumbnail_Image__160x120_"></span><span id="medium_thumbnail_image__160x120_"></span><span id="MEDIUM_THUMBNAIL_IMAGE__160X120_"></span>

<span id="Medium_Thumbnail_Image__160x120_"></span><span id="medium_thumbnail_image__160x120_"></span><span id="MEDIUM_THUMBNAIL_IMAGE__160X120_"></span>**Medium Thumbnail Image (160x120)** (6)


</dt> <dd></dd> <dt>

<span id="Large_Thumbnail_Image__320x240_"></span><span id="large_thumbnail_image__320x240_"></span><span id="LARGE_THUMBNAIL_IMAGE__320X240_"></span>

<span id="Large_Thumbnail_Image__320x240_"></span><span id="large_thumbnail_image__320x240_"></span><span id="LARGE_THUMBNAIL_IMAGE__320X240_"></span>**Large Thumbnail Image (320x240)** (7)


</dt> <dd></dd> <dt>

<span id="AllocatedGPU"></span><span id="allocatedgpu"></span><span id="ALLOCATEDGPU"></span>

<span id="AllocatedGPU"></span><span id="allocatedgpu"></span><span id="ALLOCATEDGPU"></span>**AllocatedGPU** (8)


</dt> <dd></dd> <dt>

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

**Windows Server 2008:** This value is not supported before Windows Server 2008 R2.

</dd> <dt>

<span id="StatusDescriptions"></span><span id="statusdescriptions"></span><span id="STATUSDESCRIPTIONS"></span>

<span id="StatusDescriptions"></span><span id="statusdescriptions"></span><span id="STATUSDESCRIPTIONS"></span>**StatusDescriptions** (111)


</dt> <dd>

This corresponds to the **StatusDescriptions** property of the [**Msvm\_SummaryInformation**](msvm-summaryinformation.md) class.

**Windows Server 2008:** This value is not supported before Windows Server 2008 R2.

</dd> <dt>

<span id="MemoryAvailable"></span><span id="memoryavailable"></span><span id="MEMORYAVAILABLE"></span>

<span id="MemoryAvailable"></span><span id="memoryavailable"></span><span id="MEMORYAVAILABLE"></span>**MemoryAvailable** (112)


</dt> <dd>

This corresponds to the **MemoryAvailable** property of the [**Msvm\_SummaryInformation**](msvm-summaryinformation.md) class.

**Windows Server 2008 R2 and Windows Server 2008:** This value is not supported before Windows Server 2008 R2 with SP1.

</dd> <dt>

<span id="AvailableMemoryBuffer"></span><span id="availablememorybuffer"></span><span id="AVAILABLEMEMORYBUFFER"></span>

<span id="AvailableMemoryBuffer"></span><span id="availablememorybuffer"></span><span id="AVAILABLEMEMORYBUFFER"></span>**AvailableMemoryBuffer** (113)


</dt> <dd>

This corresponds to the **AvailableMemoryBuffer** property of the [**Msvm\_SummaryInformation**](msvm-summaryinformation.md) class.

**Windows Server 2008 R2 and Windows Server 2008:** This value is not supported before Windows Server 2008 R2 with SP1.

</dd> </dl> </dd> <dt>

*SummaryInformation* \[out\]
</dt> <dd>

Type: **Msvm\_SummaryInformation\[\]**

An array of [**Msvm\_SummaryInformation**](msvm-summaryinformation.md) instances containing the requested information for the VMs and/or snapshots specified in the *SettingData* array. Properties not specified in the *RequestedInformation* parameter will have a **NULL** value.

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

Access to the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Examples

The following C# sample displays summary information. The referenced utilities can be found in [Common Utilities for the Virtualization Samples](common-utilities-for-the-virtualization-samples.md).

> \[!Important\]  
> To function correctly, the following code must be run on the VM host server, and must be run with Administrator privileges.

 


```CSharp
using System;
using System.Management;

namespace HyperVSamples
{
    class GetSummaryInformationClass
    {
        ManagementObject virtualSystemService = null;
        ManagementScope scope = null;

        GetSummaryInformationClass()
        {
            scope = new ManagementScope(@"root\virtualization", null);
            virtualSystemService = Utility.GetServiceObject(scope, "Msvm_VirtualSystemManagementService");
        }

        ManagementObject GetVirtualSystemSetting(string vmName)
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

        void GetSummaryInformation(ManagementObject[] virtualSystemSettings, UInt32[] requestedInformation)
        {
            ManagementBaseObject inParams = virtualSystemService.GetMethodParameters("GetSummaryInformation");
            string[] settingPaths = new string[virtualSystemSettings.Length];
            for (int i = 0; i < settingPaths.Length; ++i)
            {
                settingPaths[i] = virtualSystemSettings[i].Path.Path;
            }

            inParams["SettingData"] = settingPaths;
            inParams["RequestedInformation"] = requestedInformation;

            ManagementBaseObject outParams = virtualSystemService.InvokeMethod("GetSummaryInformation", inParams, null);

            if ((UInt32)outParams["ReturnValue"] == ReturnCode.Completed)
            {
                Console.WriteLine("Summary information was retrieved successfully.");

                ManagementBaseObject[] summaryInformationArray = (ManagementBaseObject[])outParams["SummaryInformation"];

                foreach (ManagementBaseObject summaryInformation in summaryInformationArray)
                {
                    Console.WriteLine("\nVirtual System Summary Information:");
                    foreach (UInt32 requested in requestedInformation)
                    {
                        switch (requested)
                        {
                            case 0:
                                Console.WriteLine("\n\tName: {0}", summaryInformation["Name"].ToString());
                                break;

                            case 1:
                                Console.WriteLine("\tElement Name: {0}", summaryInformation["ElementName"].ToString());
                                break;

                            case 2:
                                Console.WriteLine("\tCreation Time: {0}", summaryInformation["CreationTime"].ToString());
                                break;

                            case 3:
                                Console.WriteLine("\tNotes: {0}", summaryInformation["Notes"].ToString());
                                break;

                            case 4:
                                Console.WriteLine("\tNumber of Processors: {0}", summaryInformation["NumberofProcessors"].ToString());
                                break;
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
        }

        void Close()
        {
            this.virtualSystemService.Dispose();
        }

        static void Main(string[] args)
        {
            if (args != null &amp;&amp; (args.Length < 2 || args.Length > 6))
            {
                Console.WriteLine("GetSummaryInformation vmName value1 value2...");
                Console.WriteLine("value:");
                Console.WriteLine("\t0:Name");
                Console.WriteLine("\t1:Element Name");
                Console.WriteLine("\t2:Creation Time");
                Console.WriteLine("\t3:Notes");
                Console.WriteLine("\t4:Number of Processors");
                Console.WriteLine("\nExample: GetSummaryInformation MyfirstVM 0 1 4");
                return;
            }

            GetSummaryInformationClass getSummaryInfo = new GetSummaryInformationClass();
            string vmName = args[0];
            ManagementObject virtualSystemSetting = getSummaryInfo.GetVirtualSystemSetting(vmName);
            ManagementObject[] settings = new ManagementObject[1];
            settings[0] = virtualSystemSetting;

            UInt32[] requestedInfo = new UInt32[args.Length - 1];

            for (int i = 1; i < args.Length; ++i)
            {
                requestedInfo[i - 1] = UInt32.Parse(args[i]);
            }
            getSummaryInfo.GetSummaryInformation(settings, requestedInfo);
            getSummaryInfo.Close();

            virtualSystemSetting.Dispose();
        }
    }
}
```



The following VBScript sample displays summary information.

> \[!Important\]  
> To function correctly, the following code must be run on the VM host server, and must be run with Administrator privileges.

 


```VB
option explicit 

dim objWMIService
dim managementService
dim fileSystem

const wmiSuccessful = 0

Main()


'-----------------------------------------------------------------
' Main
'-----------------------------------------------------------------
Sub Main()

    dim computer, objArgs, vmName, vm, requestedInformation, vmSetting, vmSettings, i
    
    set fileSystem = Wscript.CreateObject("Scripting.FileSystemObject")
    computer = "."
    set objWMIService = GetObject("winmgmts:\\" & computer & "\root\virtualization")
    set managementService = objWMIService.ExecQuery("select * from Msvm_VirtualSystemManagementService").ItemIndex(0)
    
    set objArgs = WScript.Arguments
    if WScript.Arguments.Count > 1 and WScript.Arguments.Count < 7 then
        vmName = objArgs.Unnamed.Item(0)
        redim requestedInformation(WScript.Arguments.Count - 2)
        for i = 1 to WScript.Arguments.Count - 1
            requestedInformation(i-1) = objArgs(i)
        next
        
    else
        WScript.Echo "usage: cscript GetSummaryInformation.vbs vmName value1 value2..."
        WScript.Echo "value:"
        WScript.Echo "0:Name"
        WScript.Echo "1:Element Name"
        WScript.Echo "2:Creation Time"
        WScript.Echo "3:Notes"
        WScript.Echo "4:Number of Processors"
        WScript.Quit(1)
    end if
    
    set vmSetting = GetVirtualSystemSetting(vmName)
    
    vmSettings = Array(1)
    vmSettings(0) = vmSetting.Path_.Path
    
    if GetSummaryInformation(vmSettings, requestedInformation) then
        WriteLog "Done"
        WScript.Quit(0)
     End if
    
    WriteLog "GetSummaryInformation Failed."
    WScript.Quit(1)
    
End Sub

'-----------------------------------------------------------------
' Retrieve Msvm_VirtualComputerSystem from base on its ElementName
'-----------------------------------------------------------------
Function GetComputerSystem(vmElementName)
    On Error Resume Next
    dim query
    query = Format1("select * from Msvm_ComputerSystem where ElementName = '{0}'", vmElementName)
    set GetComputerSystem = objWMIService.ExecQuery(query).ItemIndex(0)
    if (Err.Number <> 0) then
        WriteLog Format1("Err.Number: {0}", Err.Number)
        WriteLog Format1("Err.Description:{0}",Err.Description)
        WScript.Quit(1)
    end if
End Function

'-----------------------------------------------------------------
' Retrieve Msvm_VirtualSystemSettingData Msvm_ComputerSystem object
'-----------------------------------------------------------------
Function GetVirtualSystemSetting(vmElementName)
    dim query, computerSystem
    set computerSystem = GetComputerSystem(vmElementName)
    query = Format1("ASSOCIATORS OF {{0}} WHERE resultClass = Msvm_VirtualSystemsettingData", computerSystem.Path_.Path)
    set GetVirtualSystemSetting = objWMIService.ExecQuery(query).ItemIndex(0)
End Function

'-----------------------------------------------------------------
' GetSummaryInformation
'-----------------------------------------------------------------
Function GetSummaryInformation(settings, requestedInformation)
    dim query, objInParam, objOutParams, summaryInformation, requested
    
    set objInParam = managementService.Methods_("GetSummaryInformation").InParameters.SpawnInstance_()

    objInParam.SettingData = settings
    objInParam.RequestedInformation = requestedInformation
    
    set objOutParams = managementService.ExecMethod_("GetSummaryInformation", objInParam)
    
    if objOutParams.ReturnValue = wmiSuccessful then
        GetSummaryInformation = true
        for each summaryInformation in objOutParams.SummaryInformation
        
           WriteLog "Virtual System Summary Information:"
           for each requested in requestedInformation
              select case requested
                  case 0:
                      WriteLog Format1("Name: {0}", summaryInformation.Name)
                  case 1:
                      WriteLog Format1("Element Name: {0}", summaryInformation.ElementName)
                  case 2:
                      WriteLog Format1("Creation Time: {0}", summaryInformation.CreationTime)
                  case 3:
                      WriteLog Format1("Notes: {0}", summaryInformation.Notes)
                  case 4:
                      WriteLog Format1("Number of Processors: {0}", summaryInformation.NumberofProcessors)
              end select
          next
      next
    else
        WriteLog Format1("GetSummaryInformation failed with ReturnValue: {0}", objOutParams.ReturnValue)
    end if

End Function

'-----------------------------------------------------------------
' Create the console log files.
'-----------------------------------------------------------------
Sub WriteLog(line)
    dim fileStream
    set fileStream = fileSystem.OpenTextFile(".\GetVirtualSystemThumbnailImage.log", 8, true)
    WScript.Echo line
    fileStream.WriteLine line
    fileStream.Close

End Sub


'------------------------------------------------------------------------------
' The string formatting functions to avoid string concatenation.
'------------------------------------------------------------------------------
Function Format2(myString, arg0, arg1)
    Format2 = Format1(myString, arg0)
    Format2 = Replace(Format2, "{1}", arg1)
End Function


'------------------------------------------------------------------------------
' The string formatting functions to avoid string concatenation.
'------------------------------------------------------------------------------
Function Format1(myString, arg0)
    Format1 = Replace(myString, "{0}", arg0)
End Function
```



## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012<br/>                                                                       |
| Namespace<br/>                | Root\\Virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md)
</dt> <dt>

[**CIM\_VirtualSystemSettingData**](https://msdn.microsoft.com/library/cc136954)
</dt> <dt>

[**Msvm\_SummaryInformation**](msvm-summaryinformation.md)
</dt> </dl>

 

 





