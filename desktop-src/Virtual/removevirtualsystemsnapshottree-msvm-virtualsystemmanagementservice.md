---
title: RemoveVirtualSystemSnapshotTree method of the Msvm\_VirtualSystemManagementService class
description: Removes an existing snapshot and all its children of a virtual system.
ms.assetid: '7055bedf-dc9c-4023-844e-f227693afb74'
keywords: ["RemoveVirtualSystemSnapshotTree method Hyper-V", "RemoveVirtualSystemSnapshotTree method Hyper-V , Msvm_VirtualSystemManagementService class", "Msvm_VirtualSystemManagementService class Hyper-V , RemoveVirtualSystemSnapshotTree method"]
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemManagementService.RemoveVirtualSystemSnapshotTree
api_location:
- Root\Virtualization
api_type:
- COM
---

# RemoveVirtualSystemSnapshotTree method of the Msvm\_VirtualSystemManagementService class

Removes an existing snapshot and all its children of a virtual system.

## Syntax


```mof
uint32 RemoveVirtualSystemSnapshotTree(
  [in]  CIM_VirtualSystemSettingData REF SnapshotSettingData,
  [out] CIM_ConcreteJob              REF Job
);
```



## Parameters

<dl> <dt>

*SnapshotSettingData* \[in\]
</dt> <dd>

Type: **CIM\_VirtualSystemSettingData**

A reference to the [**CIM\_VirtualSystemSettingData**](https://msdn.microsoft.com/library/cc136954) instance which represents the snapshot tree to be removed.

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

The following C# sample removes a snapshot tree from a virtual system. The referenced utilities can be found in [Common Utilities for the Virtualization Samples](common-utilities-for-the-virtualization-samples.md).

> \[!Important\]  
> To function correctly, the following code must be run on the VM host server, and must be run with Administrator privileges.

 


```CSharp
using System;
using System.Management;

namespace HyperVSamples
{
    class RemoveVirtualSystemSnapshotTreeClass
    {
        static ManagementObject GetLastAppliedVirtualSystemSnapshot(ManagementObject vm)
        {
            ManagementObjectCollection settings = vm.GetRelated(
                "Msvm_VirtualSystemsettingData",
                "Msvm_LastAppliedSettingData ",
                null,
                null,
                "SettingData",
                "ManagedElement",
                false,
                null);

            ManagementObject virtualSystemsetting = null;
            foreach (ManagementObject setting in settings)
            {
                Console.WriteLine(setting.Path.Path);
                Console.WriteLine(setting["ElementName"]);
                virtualSystemsetting = setting;

            }

            return virtualSystemsetting;
        }

        static void RemoveVirtualSystemSnapshotTree(string vmName)
        {
            ManagementScope scope = new ManagementScope(@"root\virtualization", null);

            ManagementObject virtualSystemService = Utility.GetServiceObject(scope, "Msvm_VirtualSystemManagementService");

            ManagementBaseObject inParams = virtualSystemService.GetMethodParameters("RemoveVirtualSystemSnapshotTree");

            ManagementObject vm = Utility.GetTargetComputer(vmName, scope);

            ManagementObject vmSnapshot = GetLastAppliedVirtualSystemSnapshot(vm);

            inParams["SnapshotsettingData"] = vmSnapshot.Path.Path;

            ManagementBaseObject outParams = virtualSystemService.InvokeMethod("RemoveVirtualSystemSnapshotTree", inParams, null);

            if ((UInt32)outParams["ReturnValue"] == ReturnCode.Started)
            {
                if (Utility.JobCompleted(outParams, scope))
                {
                    Console.WriteLine("Snapshot tree was removed successfully.");

                }
                else
                {
                    Console.WriteLine("Failed to remove snapshot tree");
                }
            }
            else if ((UInt32)outParams["ReturnValue"] == ReturnCode.Completed)
            {
                Console.WriteLine(outParams["SnapshotsettingData"].ToString());
                Console.WriteLine("Snapshot tree was removed successfully.");
            }
            else
            {
                Console.WriteLine("Remove virtual system snapshot tree failed with error {0}", outParams["ReturnValue"]);
            }

            inParams.Dispose();
            outParams.Dispose();
            vm.Dispose();
            vmSnapshot.Dispose();
            virtualSystemService.Dispose();
        }

        static void Main(string[] args)
        {
            if (args != null &amp;&amp; args.Length != 1)
            {
                Console.WriteLine("Usage: RemoveVirtualSystemSnapshotTree vmName");
                return;
            }
            RemoveVirtualSystemSnapshotTree(args[0]);
        }
    }
}
```



The following VBScript sample removes a snapshot tree from a virtual system.

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
    dim computer, objArgs, vmName, vm, snapshotSetting
    
    set fileSystem = Wscript.CreateObject("Scripting.FileSystemObject")
    computer = "."
    set objWMIService = GetObject("winmgmts:\\" & computer & "\root\virtualization")
    set managementService = objWMIService.ExecQuery("select * from Msvm_VirtualSystemManagementService").ItemIndex(0)
    
    set objArgs = WScript.Arguments
    if WScript.Arguments.Count = 1 then
        vmName = objArgs.Unnamed.Item(0)
    else
        WScript.Echo "usage: cscript RemoveVirtualSystemSnapshottree.vbs vmName"
        WScript.Quit(1)
    end if
 
    set vm = GetComputerSystem(vmName)
    set snapshotSetting = GetComputerSystemSnapshotSettings(vm)

    if RemoveVirtualSystemSnapshottree(snapshotSetting) then
        WriteLog "Done"
        WScript.Quit(0)
    else
        WriteLog "RemoveVirtualSystemSnapshotTree failed."
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
' Retrieve the last applied Msvm_VirtualComputerSystem snapshot
'-----------------------------------------------------------------
Function GetComputerSystemSnapshotSettings(computerSystem)
    On Error Resume Next
    dim query
    query = Format1("ASSOCIATORS OF {{0}} WHERE resultClass = Msvm_VirtualSystemsettingData AssocClass = Msvm_LastAppliedSettingData", computerSystem.Path_.Path)
    set GetComputerSystemSnapshotSettings = objWMIService.ExecQuery(query).ItemIndex(0)
    if (Err.Number <> 0) then
        WriteLog Format1("Err.Number: {0}", Err.Number)
        WriteLog Format1("Err.Description:{0}",Err.Description)
        WScript.Quit(1)
    end if
End Function

'-----------------------------------------------------------------
' Remove a virtual system Snapshot
'-----------------------------------------------------------------
Function RemoveVirtualSystemSnapshottree(snapshotSettingData)

    dim objInParam, objOutParams
    
    RemoveVirtualSystemSnapshottree = false
    set objInParam = managementService.Methods_("RemoveVirtualSystemSnapshottree").InParameters.SpawnInstance_()
    objInParam.SnapshotSettingData = snapshotSettingData.Path_.Path
    
    set objOutParams = managementService.ExecMethod_("RemoveVirtualSystemSnapshottree", objInParam)

    if objOutParams.ReturnValue = wmiStarted then
        if (WMIJobCompleted(objOutParams)) then
            RemoveVirtualSystemSnapshottree = true
        end if
    elseif objOutParams.ReturnValue = wmiSuccessful then
        RemoveVirtualSystemSnapshottree = true
    else
        WriteLog Format1("RemoveVirtualSystemSnapshotTree failed with ReturnValue {0}", objOutParams.ReturnValue)
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
    set fileStream = fileSystem.OpenTextFile(".\RemoveVirtualSystemSnapshotTree.log", 8, true)
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

[**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md)
</dt> <dt>

[**CIM\_VirtualSystemSettingData**](https://msdn.microsoft.com/library/cc136954)
</dt> <dt>

[**CIM\_ConcreteJob**](https://msdn.microsoft.com/library/cc136808)
</dt> <dt>

[**DestroySnapshotTree (V2)**](https://msdn.microsoft.com/library/windows/desktop/hh850042)
</dt> </dl>

 

 





