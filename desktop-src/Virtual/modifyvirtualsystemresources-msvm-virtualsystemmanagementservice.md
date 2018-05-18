---
title: ModifyVirtualSystemResources method of the Msvm\_VirtualSystemManagementService class
description: Modifies the setting data for existing resources on a virtual computer system.
ms.assetid: 'bb81b95c-927d-49da-809a-b4ca2b05b6e5'
keywords: ["ModifyVirtualSystemResources method Hyper-V", "ModifyVirtualSystemResources method Hyper-V , Msvm_VirtualSystemManagementService class", "Msvm_VirtualSystemManagementService class Hyper-V , ModifyVirtualSystemResources method"]
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemManagementService.ModifyVirtualSystemResources
api_location:
- Root\Virtualization
api_type:
- COM
---

# ModifyVirtualSystemResources method of the Msvm\_VirtualSystemManagementService class

Modifies the setting data for existing resources on a virtual computer system.

## Syntax


```mof
uint32 ModifyVirtualSystemResources(
  [in]  CIM_ComputerSystem REF ComputerSystem,
  [in]  string                 ResourceSettingData[],
  [out] CIM_ConcreteJob    REF Job
);
```



## Parameters

<dl> <dt>

*ComputerSystem* \[in\]
</dt> <dd>

Type: **CIM\_ComputerSystem**

A reference to the virtual computer system whose resources are to be modified.

</dd> <dt>

*ResourceSettingData* \[in\]
</dt> <dd>

Type: **string\[\]**

An array of embedded instances of the [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) class that describe the resources to be modified on the virtual computer system.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

Type: **CIM\_ConcreteJob**

An optional reference that is returned if the operation is executed asynchronously. If present, the returned reference to an instance of [**CIM\_ConcreteJob**](https://msdn.microsoft.com/library/cc136808) can be used to monitor progress and to obtain the result of the method.

</dd> </dl>

## Return value

Type: **uint32**

If this method is executed synchronously, it returns 0 if it succeeds. If this method is executed asynchronously, it returns 4096 and the *Job* output parameter can be used to track the progress of the asynchronous operation. Any other return value indicates an error.

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

**System is in used** (32774)
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

The following C# sample modifies the settings for the resources of a virtual system. The referenced utilities can be found in [Common Utilities for the Virtualization Samples](common-utilities-for-the-virtualization-samples.md).

> \[!Important\]  
> To function correctly, the following code must be run on the VM host server, and must be run with Administrator privileges.

 


```CSharp
using System;
using System.Management;

namespace HyperVSamples
{
    class ModifyVirtualSystemResourcesClass
    {
        ManagementObject virtualSystemService = null;
        ManagementScope scope = null;

        ModifyVirtualSystemResourcesClass()
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

        void ModifyVirtualSystemResources(string vmName, string syntheticNicName, string address)
        {

            ManagementObject vm = Utility.GetTargetComputer(vmName, scope);
            ManagementObject vmSetting = Utility.GetVirtualSystemSettingData(vm);

            ManagementObject syntheticNicPortSetting = GetVirtualSystemEthernetPortSetting(vmSetting, syntheticNicName);

            if (address == null)
            {
                syntheticNicPortSetting["StaticMacAddress"] = false;
            }
            else
            {
                syntheticNicPortSetting["StaticMacAddress"] = true;
                syntheticNicPortSetting["Address"] = address;
            }

            string[] resources = new string[1];
            resources[0] = syntheticNicPortSetting.GetText(TextFormat.CimDtd20);

            ManagementBaseObject inParams = virtualSystemService.GetMethodParameters("ModifyVirtualSystemResources");

            inParams["ComputerSystem"] = vm.Path.Path;
            inParams["ResourcesettingData"] = resources;

            ManagementBaseObject outParams = virtualSystemService.InvokeMethod("ModifyVirtualSystemResources", inParams, null);

            if ((UInt32)outParams["ReturnValue"] == ReturnCode.Started)
            {
                if (Utility.JobCompleted(outParams, scope))
                {
                    Console.WriteLine("SyntheticNic was modified successfully.");

                }
                else
                {
                    Console.WriteLine("Failed to modify SyntheticNic.");
                }
            }
            else if ((UInt32)outParams["ReturnValue"] == ReturnCode.Completed)
            {
                Console.WriteLine("SyntheticNic was modified successfully.");
            }
            else
            {
                Console.WriteLine("Modify SyntheticNic failed with error : {0}", outParams["ReturnValue"]);
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
            if (args != null &amp;&amp; args.Length != 2 &amp;&amp; args.Length != 3)
            {
                Console.WriteLine("Usage: AddVirtualSystemResources vmName syntheticNicName MACAddress");
                Console.WriteLine("MACAddress: Optional. Static MAC address is used if it's specified.");
                Console.WriteLine("Example: AddVirtualSystemResources MyFirstVM myStaticNic 00155D02B317");
                return;
            }

            string address = null;

            if (args.Length == 3)
            {
                address = args[2];

            }
            ModifyVirtualSystemResourcesClass modifyResource = new ModifyVirtualSystemResourcesClass();

            modifyResource.ModifyVirtualSystemResources(args[0], args[1], address);
            modifyResource.Close();
        }
    }
}
```



The following VBScript sample modifies the settings for the resources of a virtual system.

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

    set objArgs = WScript.Arguments
    if WScript.Arguments.Count = 3 then
        vmName = objArgs.Unnamed.Item(0)
        nicName = objArgs.Unnamed.Item(1)
        MACAddress = objArgs.Unnamed.Item(2)
    elseif WScript.Arguments.Count = 2 then
        vmName = objArgs.Unnamed.Item(0)
        nicName = objArgs.Unnamed.Item(1)
        MACAddress = NULL
    else
        WScript.Echo "usage: cscript ModifyVirtualSystemResource vmName syntheticNicName [MACAddress]"
        WScript.Echo "Example: MyFirstVM myStaticNic 00155D02B302"
        WScript.Quit(1)
    end if

    set fileSystem = Wscript.CreateObject("Scripting.FileSystemObject")
    computer = "."
    set objWMIService = GetObject("winmgmts:\\" & computer & "\root\virtualization")
    set managementService = objWMIService.ExecQuery("select * from Msvm_VirtualSystemManagementService").ItemIndex(0)
 
    set vm = GetComputerSystem(vmName)

    if ModifyVirtualSystemResources(vm, nicName, MACAddress) then
        WriteLog "Done"
        WScript.Quit(0)
    else
        WriteLog "ModifyVirtualSystemResources failed."
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
' ModifyVirtualSystemResources
'-----------------------------------------------------------------
Function ModifyVirtualSystemResources(computerSystem, nicName, MACAddress)

    dim query, virtualSystemSetting, ethernetsettingData
    dim resourcesettings, objInParam, objOutParams
    
    ModifyVirtualSystemResources = false
    
    query = Format1("ASSOCIATORS OF {{0}} WHERE resultClass = Msvm_VirtualSystemsettingData", computerSystem.Path_.Path)
    set virtualSystemSetting = objWMIService.ExecQuery(query).ItemIndex(0)
    
    set ethernetsettingData = GetSyntheticEthernetPortSetting(virtualSystemSetting, nicName)
    
    if (ethernetsettingData Is Nothing) then
        WriteLog Format1("'{0}' does not exist.", nicName)
        exit function
    end if
    
    if IsNull(MACAddress) then
        ethernetsettingData.StaticMacAddress = false
    else
        ethernetsettingData.StaticMacAddress = true
        ethernetsettingData.Address = MACAddress
    end if
    
    resourcesettings = Array(1)
    resourcesettings(0) = ethernetsettingData.GetText_(1)
    
    set objInParam = managementService.Methods_("ModifyVirtualSystemResources").InParameters.SpawnInstance_()
    objInParam.ComputerSystem = computerSystem.Path_.Path
    objInParam.ResourcesettingData = resourcesettings
    
    set objOutParams = managementService.ExecMethod_("ModifyVirtualSystemResources", objInParam)

    if objOutParams.ReturnValue = wmiStarted then
        if (WMIJobCompleted(objOutParams)) then
            WriteLog ("Nic Controller was Modify successfully.")
            ModifyVirtualSystemResources = true
        end if
    elseif  objOutParams.ReturnValue = wmiSuccessful then
        ModifyVirtualSystemResources = true
    else
        WriteLog Format1("Modify synthetic Ethernet failed with error:{0}", outParams.ReturnValue)
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
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012<br/>                                                                       |
| Namespace<br/>                | Root\\Virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**ModifyResourceSettings (V2)**](https://msdn.microsoft.com/library/windows/desktop/hh850099)
</dt> <dt>

[**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md)
</dt> </dl>

 

 





