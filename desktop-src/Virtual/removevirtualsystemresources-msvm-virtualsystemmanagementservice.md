---
title: RemoveVirtualSystemResources method of the Msvm\_VirtualSystemManagementService class
description: Removes resources from an existing virtual system.
ms.assetid: e12cd0b8-e4a9-4924-9e00-4f5d74bccc66
keywords:
- RemoveVirtualSystemResources method Hyper-V
- RemoveVirtualSystemResources method Hyper-V , Msvm_VirtualSystemManagementService class
- Msvm_VirtualSystemManagementService class Hyper-V , RemoveVirtualSystemResources method
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemManagementService.RemoveVirtualSystemResources
api_location:
- Root\Virtualization
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RemoveVirtualSystemResources method of the Msvm\_VirtualSystemManagementService class

Removes resources from an existing virtual system.

## Syntax


```mof
uint32 RemoveVirtualSystemResources(
  [in]  CIM_ComputerSystem                REF TargetSystem,
  [in]  CIM_ResourceAllocationSettingData REF ResourceSettingData[],
  [out] CIM_ConcreteJob                   REF Job
);
```



## Parameters

<dl> <dt>

*TargetSystem* \[in\]
</dt> <dd>

Type: **[**CIM\_ComputerSystem**](https://msdn.microsoft.com/library/aa387219)**

A reference to the virtual computer system whose resources are to be removed.

</dd> <dt>

*ResourceSettingData* \[in\]
</dt> <dd>

Type: **[**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214)\[\]**

A reference to an array of instances of [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) the describe the resources to be removed.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

Type: **[**CIM\_ConcreteJob**](https://msdn.microsoft.com/library/cc136808)**

An optional parameter for monitoring progress of the operation, which is used if the method could not be executed synchronously. If the operation is executing asynchronously, the return value is 4096.

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

The following C# sample removes resources from a virtual system. The referenced utilities can be found in [Common Utilities for the Virtualization Samples](common-utilities-for-the-virtualization-samples.md).

> \[!Important\]  
> To function correctly, the following code must be run on the VM host server, and must be run with Administrator privileges.

 


```CSharp
using System;
using System.Management;

namespace HyperVSamples
{
    class RemoveVirtualSystemResourcesClass
    {
        ManagementObject virtualSystemService = null;
        ManagementScope scope = null;

        RemoveVirtualSystemResourcesClass()
        {
            scope = new ManagementScope(@"root\virtualization", null);
            virtualSystemService = Utility.GetServiceObject(scope, "Msvm_VirtualSystemManagementService");
        }

        ManagementObject GetVirtualSystemEthernetPortSetting(ManagementObject vmSetting, string SyntheticNicElementName)
        {
            ManagementObject SyntheticNicSetting = null;
            ManagementObjectCollection SyntheticNicSettings = vmSetting.GetRelated
            (
                "Msvm_SyntheticEthernetPortSettingData",
                "Msvm_VirtualSystemSettingDataComponent",
                null,
                null,
                "PartComponent",
                "GroupComponent",
                false,
                null
            );

            foreach (ManagementObject instance in SyntheticNicSettings)
            {
                if (instance["ElementName"].ToString().ToLower() == SyntheticNicElementName.ToLower())
                {
                    SyntheticNicSetting = instance;
                    break;
                }
            }

            return SyntheticNicSetting;

        }

        void RemoveVirtualSystemResources(string vmName, string syntheticNicName)
        {

            ManagementObject vm = Utility.GetTargetComputer(vmName, scope);
            ManagementObject vmSetting = Utility.GetVirtualSystemSettingData(vm);

            ManagementObject syntheticNicPortSetting = GetVirtualSystemEthernetPortSetting(vmSetting, syntheticNicName);

            ManagementBaseObject inParams = virtualSystemService.GetMethodParameters("RemoveVirtualSystemResources");
            inParams["TargetSystem"] = vm.Path.Path;
            string[] resources = new string[1];
            resources[0] = syntheticNicPortSetting.Path.Path;

            inParams["ResourcesettingData"] = resources;

            ManagementBaseObject outParams = virtualSystemService.InvokeMethod("RemoveVirtualSystemResources", inParams, null);

            if ((UInt32)outParams["ReturnValue"] == ReturnCode.Started)
            {
                if (Utility.JobCompleted(outParams, scope))
                {
                    Console.WriteLine("SyntheticNic was removed successfully.");

                }
                else
                {
                    Console.WriteLine("Failed to remove SyntheticNic from VM");
                }
            }
            else if ((UInt32)outParams["ReturnValue"] == ReturnCode.Completed)
            {
                Console.WriteLine("SyntheticNic was removed successfully.");
            }
            else
            {
                Console.WriteLine("Remove SyntheticNic failed with error : {0}", outParams["ReturnValue"]);
            }

            inParams.Dispose();
            outParams.Dispose();
            vm.Dispose();
            vmSetting.Dispose();
            syntheticNicPortSetting.Dispose();
        }

        void Close()
        {
            this.virtualSystemService.Dispose();
        }

        static void Main(string[] args)
        {
            if (args != null &amp;&amp; args.Length != 2)
            {
                Console.WriteLine("Usage: RemoveVirtualSystemResources vmName syntheticNicName");
                Console.WriteLine("Example: RemoveVirtualSystemResources MyFirstVM myStaticNic");
                return;
            }

            RemoveVirtualSystemResourcesClass removeResource = new RemoveVirtualSystemResourcesClass();
            removeResource.RemoveVirtualSystemResources(args[0], args[1]);
            removeResource.Close();
        }
    }
}
```



The following VBScript sample removes resources from a virtual system.

> \[!Important\]  
> To function correctly, the following code must be run on the VM host server, and must be run with Administrator privileges.

 


```VB
option explicit 

dim objWMIService
dim managementService
dim fileSystem


const JobStarting = 3
const JobRunning = 4
const JobCompleted = 7
const wmiStarted = 4096
const wmiSuccessful = 0

Main()


'-----------------------------------------------------------------
' Main
'-----------------------------------------------------------------
Sub Main()

    dim objArgs, vmName, nicName, MACAddress, computer, vm
    
    set objArgs = WScript.Arguments

    if WScript.Arguments.Count = 2 then
        vmName = objArgs.Unnamed.Item(0)
        nicName = objArgs.Unnamed.Item(1)
        MACAddress = NULL
    else
        WScript.Echo "usage: cscript RemoveVirtualSystemResource vmName syntheticNicName"
        WScript.Echo "MyFirstVM myStaticNic"
        WScript.Quit(1)
    end if

    set fileSystem = Wscript.CreateObject("Scripting.FileSystemObject")
    computer = "."
    set objWMIService = GetObject("winmgmts:\\" & computer & "\root\virtualization")
    set managementService = objWMIService.ExecQuery("select * from Msvm_VirtualSystemManagementService").ItemIndex(0)
 
    set vm = GetComputerSystem(vmName)

    if RemoveVirtualSystemResources(vm, nicName) then
        WriteLog "Done"
        WScript.Quit(0)
    else
        WriteLog "RemoveVirtualSystemResources failed."
        WScript.Quit(1)
    end if


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
' GetSyntheticEthernetPortSetting
'-----------------------------------------------------------------
Function GetSyntheticEthernetPortSetting(vmSetting, nicName)
    dim query, ethernetsettingsData, instance
    set GetSyntheticEthernetPortSetting = Nothing
    query = Format1("ASSOCIATORS OF {{0}} WHERE " &amp;_
                    "resultClass = Msvm_SyntheticEthernetPortsettingData " &amp;_
                    "AssocClass = Msvm_VirtualSystemSettingDataComponent " &amp;_
                    "ResultRole = PartComponent " &amp;_
                    "Role = GroupComponent", vmSetting.Path_.Path)
                    
    set ethernetsettingsData = objWMIService.ExecQuery(query)
    
    for each instance in ethernetsettingsData
        if lcase(instance.ElementName) = lcase(nicName) then
            set GetSyntheticEthernetPortSetting = instance   
            exit function 
        end if
    next

End Function


'-----------------------------------------------------------------
' RemoveVirtualSystemResource
'-----------------------------------------------------------------
Function RemoveVirtualSystemResources(computerSystem, nicName)

    dim query, virtualSystemSetting, ethernetsettingData
    dim resourcesettings, objInParam, objOutParams
    
    RemoveVirtualSystemResources = false
    
    query = Format1("ASSOCIATORS OF {{0}} WHERE resultClass = Msvm_VirtualSystemsettingData", computerSystem.Path_.Path)
    set virtualSystemSetting = objWMIService.ExecQuery(query).ItemIndex(0)
    
    set ethernetsettingData = GetSyntheticEthernetPortSetting(virtualSystemSetting, nicName)
    
    if (ethernetsettingData Is Nothing) then
        WriteLog Format1("'{0}' does not exist.", nicName)
        exit function
    end if
    
    resourcesettings = Array(1)
    resourcesettings(0) = ethernetsettingData.Path_.Path
    
    set objInParam = managementService.Methods_("RemoveVirtualSystemResources").InParameters.SpawnInstance_()
    objInParam.TargetSystem = computerSystem.Path_.Path
    objInParam.ResourcesettingData = resourcesettings
    
    set objOutParams = managementService.ExecMethod_("RemoveVirtualSystemResources", objInParam)

    if objOutParams.ReturnValue = wmiStarted then
        if (WMIJobCompleted(objOutParams)) then
            WriteLog ("Nic Controller was removed successfully.")
            RemoveVirtualSystemResources = true
        end if
    elseif  objOutParams.ReturnValue = wmiSuccessful then
        RemoveVirtualSystemResources = true
    else
        WriteLog Format1("Remove virtual system synthetic Ethernet failed with error:{0}", outParams.ReturnValue)
    end if
End Function


'-----------------------------------------------------------------
' Handle wmi Job object
'-----------------------------------------------------------------
Function WMIJobCompleted(outParam)

    dim WMIJob, jobState
    WMIJobCompleted = true

    set WMIJob = objWMIService.Get(outParam.Job)
    
    jobState = WMIJob.JobState

    while jobState = JobRunning or jobState = JobStarting
        WriteLog Format1("In progress... {0}% completed.",WMIJob.PercentComplete)
        WScript.Sleep(1000)
        set WMIJob = objWMIService.Get(outParam.Job)
        jobState = WMIJob.JobState
    wend

    if (WMIJob.JobState <> JobCompleted) then
        WriteLog Format1("ErrorDescription:{0}", WMIJob.ErrorDescription)
        WriteLog Format1("ErrorCode:{0}", WMIJob.ErrorCode)
        WMIJobCompleted = false
    end if

End Function
'-----------------------------------------------------------------
' Create the console log files.
'-----------------------------------------------------------------
Sub WriteLog(line)
    dim fileStream
    set fileStream = fileSystem.OpenTextFile(".\ADDSCSIContoller.log", 8, true)
    WScript.Echo line
    fileStream.WriteLine line
    fileStream.Close

End Sub

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
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012<br/>                                                                       |
| Namespace<br/>                | Root\\Virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md)
</dt> </dl>

 

 





