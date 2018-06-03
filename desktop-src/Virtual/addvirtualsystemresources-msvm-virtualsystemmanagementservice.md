---
title: AddVirtualSystemResources method of the Msvm\_VirtualSystemManagementService class
description: Adds resources to an existing virtual system.
ms.assetid: 569478b5-2722-4f6c-b7e6-5398fac5284c
keywords:
- AddVirtualSystemResources method Hyper-V
- AddVirtualSystemResources method Hyper-V , Msvm_VirtualSystemManagementService class
- Msvm_VirtualSystemManagementService class Hyper-V , AddVirtualSystemResources method
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemManagementService.AddVirtualSystemResources
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

# AddVirtualSystemResources method of the Msvm\_VirtualSystemManagementService class

Adds resources to an existing virtual system.

## Syntax


```mof
uint32 AddVirtualSystemResources(
  [in]  CIM_ComputerSystem                REF TargetSystem,
  [in]  string                                ResourceSettingData[],
  [out] CIM_ResourceAllocationSettingData REF NewResources[],
  [out] CIM_ConcreteJob                   REF Job
);
```



## Parameters

<dl> <dt>

*TargetSystem* \[in\]
</dt> <dd>

Type: **CIM\_ComputerSystem**

A reference to the computer system instance to which the resource is to be added.

</dd> <dt>

*ResourceSettingData* \[in\]
</dt> <dd>

Type: **string\[\]**

An array of strings representing embedded instances of class [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) that describe the resources to be added.

</dd> <dt>

*NewResources* \[out\]
</dt> <dd>

Type: **CIM\_ResourceAllocationSettingData\[\]**

An optional reference to an array of instances of [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) that describe the setting data for the newly created resources.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

Type: **CIM\_ConcreteJob**

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

The following C# sample adds resources to a virtual system. The referenced utilities can be found in [Common Utilities for the Virtualization Samples](common-utilities-for-the-virtualization-samples.md).

> \[!Important\]  
> To function correctly, the following code must be run on the VM host server, and must be run with Administrator privileges.

 


```CSharp
using System;
using System.Management;

namespace HyperVSamples
{
    class AddVirtualSystemReourcesClass
    {
        ManagementObject virtualSystemService = null;
        ManagementScope scope = null;

        AddVirtualSystemReourcesClass()
        {
            scope = new ManagementScope(@"root\virtualization", null);
            virtualSystemService = Utility.GetServiceObject(scope, "Msvm_VirtualSystemManagementService");
        }

        ManagementObject AddVirtualSystemReources(String vmName, string nicName, string address)
        {
            ManagementObject syntheticNic = null;
            ManagementObject vm = Utility.GetTargetComputer(vmName, scope);
            ManagementBaseObject inParams = virtualSystemService.GetMethodParameters("AddVirtualSystemResources");

            ManagementObject SyntheticNicDefault = Utility.GetResourceAllocationsettingDataDefault(scope, ResourceType.EthernetAdapter, ResourceSubType.EthernetSynthetic, null);

            if (address != null)
            {
                SyntheticNicDefault["StaticMacAddress"] = true;
                SyntheticNicDefault["Address"] = address;
            }
            else
            {
                SyntheticNicDefault["StaticMacAddress"] = false;
            }

            SyntheticNicDefault["ElementName"] = nicName;

            String[] identifiers = new String[1];
            identifiers[0] = string.Format("{{{0}}}", Guid.NewGuid());
            SyntheticNicDefault["VirtualSystemIdentifiers"] = identifiers;

            string[] RASDs = new string[1];
            RASDs[0] = SyntheticNicDefault.GetText(TextFormat.CimDtd20);

            inParams["ResourcesettingData"] = RASDs;
            inParams["TargetSystem"] = vm.Path.Path;

            ManagementBaseObject outParams = virtualSystemService.InvokeMethod("AddVirtualSystemResources", inParams, null);

            string[] addedResources = null;

            if ((UInt32)outParams["ReturnValue"] == ReturnCode.Started)
            {
                if (Utility.JobCompleted(outParams, scope))
                {
                    addedResources = (string[])outParams["NewResources"];
                    syntheticNic = new ManagementObject(addedResources[0]);
                    Console.WriteLine("Resources were added successfully.");

                }
                else
                {
                    Console.WriteLine("Failed to add resources");
                }
            }
            else if ((UInt32)outParams["ReturnValue"] == ReturnCode.Completed)
            {
                addedResources = (string[])outParams["NewResources"];
                syntheticNic = new ManagementObject(addedResources[0]);
                Console.WriteLine("Resources were added successfully.");
            }
            else
            {
                Console.WriteLine("Add virtual system synthetic Ethernet failed with error:{0}", outParams["ReturnValue"]);
            }

            inParams.Dispose();
            outParams.Dispose();
            vm.Dispose();
            SyntheticNicDefault.Dispose();

            return syntheticNic;
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
                Console.WriteLine("Example: AddVirtualSystemResources MyFirstVM myStaticNic 00155D02B302");
                return;
            }

            string address = null;

            if (args.Length == 3)
            {
                address = args[2];

            }

            AddVirtualSystemReourcesClass addResource = new AddVirtualSystemReourcesClass();

            ManagementObject NicAdded = addResource.AddVirtualSystemReources(args[0], args[1], address);
            Console.WriteLine("Synthetic Ethernet card was added with {0} as its MAC address.", NicAdded["address"]);
            addResource.Close();
        }
    }
}
```



The following VBScript sample adds resources to a virtual system.

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

    dim computer, objArgs, vmName, vm, nicName, MACAddress
    
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
        WScript.Echo "usage: cscript AddVirtualSystemResource vmName syntheticNicName MACAddress"
        WScript.Echo "MyFirstVM myStaticNic 00155D02B302"
        WScript.Quit(1)
    end if


    set fileSystem = Wscript.CreateObject("Scripting.FileSystemObject")
    computer = "."
    set objWMIService = GetObject("winmgmts:\\" & computer & "\root\virtualization")
    set managementService = objWMIService.ExecQuery("select * from Msvm_VirtualSystemManagementService").ItemIndex(0)
 
    set vm = GetComputerSystem(vmName)

    if AddVirtualSystemResources(vm, nicName, MACAddress) then
        WriteLog "Done"
        WScript.Quit(0)
    else
        WriteLog "AddVirtualSystemResources Failed."
        WScript.Quit(1)
    end if
    
End Sub

'-----------------------------------------------------------------
' Retrieve Msvm_ResourceAllocationsettingData from WMI
'-----------------------------------------------------------------
Function GetRASDDefaultInstance(resourceType, resourceSubType)
    dim query, poolResource, capabilities, settings, setting, capability
    query = "select * from Msvm_ResourcePool where ResourceType = '{0}' and ResourceSubType ='{1}'"
    query = Format2(query, resourceType, resourceSubType)
                             
    set poolResource = objWMIService.ExecQuery(query).ItemIndex(0)
     
    query = Format1("ASSOCIATORS OF {{0}} WHERE resultClass = Msvm_AllocationCapabilities", poolResource.Path_.Path)
    set capabilities = objWMIService.ExecQuery(query)
    
    for each capability in capabilities
        query = Format1("REFERENCES  OF {{0}} WHERE resultClass = Msvm_SettingsDefineCapabilities", capability.Path_.Path)
        set settings = objWMIService.ExecQuery(query)
        for each setting in settings
            if setting.ValueRole = 0 then
               set GetRASDDefaultInstance = objWMIService.Get(setting.PartComponent)
               exit function
            end if
        next
    next
End Function


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
' Add Synthetic Ethernet card
'-----------------------------------------------------------------
Function AddVirtualSystemResources(computerSystem, nicName, MACAddress)

    dim nicRasdDefault, objInParam, objOutParams, identifiers, embeddedXml
    AddVirtualSystemResources = false
    set nicRasdDefault = GetRASDDefaultInstance("10", "Microsoft Synthetic Ethernet Port")

    set objInParam = managementService.Methods_("AddVirtualSystemResources").InParameters.SpawnInstance_()
    objInParam.TargetSystem = computerSystem.Path_.Path
    if IsNull(MACAddress) then
        nicRasdDefault.StaticMacAddress = false
    else
        nicRasdDefault.StaticMacAddress = true
        nicRasdDefault.Address = MACAddress
    end if
    nicRasdDefault.ElementName = nicName
    identifiers = Array(1)
    identifiers(0) = createobject("scriptlet.typelib").GUID
    nicRasdDefault.VirtualSystemIdentifiers = identifiers

    embeddedXml = Array(1)
    embeddedXml(0) = nicRasdDefault.GetText_(1)

    objInParam.ResourcesettingData = embeddedXml
    
    set objOutParams = managementService.ExecMethod_("AddVirtualSystemResources", objInParam)

    if objOutParams.ReturnValue = wmiStarted then
        if (WMIJobCompleted(objOutParams)) then
            WriteLog Format1("NIC controller is added to {0} successfully.", vmName)
            AddVirtualSystemResources = true
        end if
    elseif  objOutParams.ReturnValue = wmiSuccessful then
        AddVirtualSystemResources = true
    else
        WriteLog Format1("Add virtual system synthetic Ethernet failed with error:{0}", outParams.ReturnValue)
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
    set fileStream = fileSystem.OpenTextFile(".\AddVirtualSystemResources.log", 8, true)
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
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012<br/>                                                                       |
| Namespace<br/>                | Root\\Virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214)
</dt> <dt>

[**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md)
</dt> </dl>

 

 





