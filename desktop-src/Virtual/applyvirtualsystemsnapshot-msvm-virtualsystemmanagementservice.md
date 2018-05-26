---
title: ApplyVirtualSystemSnapshot method of the Msvm\_VirtualSystemManagementService class
description: Applies the disk state, runtime state, and configuration values for a snapshot to the virtual computer system.
ms.assetid: a82d2190-15cc-45f8-b8bc-e87c1db4d5aa
keywords:
- ApplyVirtualSystemSnapshot method Hyper-V
- ApplyVirtualSystemSnapshot method Hyper-V , Msvm_VirtualSystemManagementService class
- Msvm_VirtualSystemManagementService class Hyper-V , ApplyVirtualSystemSnapshot method
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemManagementService.ApplyVirtualSystemSnapshot
api_location:
- Root\Virtualization
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ApplyVirtualSystemSnapshot method of the Msvm\_VirtualSystemManagementService class

Applies the disk state, runtime state, and configuration values for a snapshot to the virtual computer system. This information serves as the starting point for the virtual computer system when it is next activated. Any disk state, runtime state, or configuration values currently associated with the virtual computer system will be lost.

## Syntax


```mof
uint32 ApplyVirtualSystemSnapshot(
  [in] CIM_ComputerSystem           REF ComputerSystem,
  [in] CIM_VirtualSystemSettingData REF SnapshotSettingData
);
```



## Parameters

<dl> <dt>

*ComputerSystem* \[in\]
</dt> <dd>

Type: **CIM\_ComputerSystem**

A reference to the [**CIM\_ComputerSystem**](https://msdn.microsoft.com/library/aa387219) instance to which the snapshot should be applied.

</dd> <dt>

*SnapshotSettingData* \[in\]
</dt> <dd>

Type: **CIM\_VirtualSystemSettingData**

A reference to the [**CIM\_VirtualSystemSettingData**](https://msdn.microsoft.com/library/cc136954) instance that represents the snapshot to be applied.

</dd> </dl>

## Return value

Type: **uint32**

If this method is executed synchronously, it returns 0 if it succeeds. Any other return value indicates an error.

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

The following C# sample applies a virtual system snapshot. The referenced utilities can be found in [Common Utilities for the Virtualization Samples](common-utilities-for-the-virtualization-samples.md).

> \[!Important\]  
> To function correctly, the following code must be run on the VM host server, and must be run with Administrator privileges.

 


```CSharp
using System;
using System.Management;

namespace HyperVSamples
{
    class ApplyVirtualSystemSnapshotClass
    {
        static ManagementObject GetLastVirtualSystemSnapshot(ManagementObject vm)
        {
            ManagementObjectCollection settings = vm.GetRelated(
                "Msvm_VirtualSystemsettingData",
                "Msvm_PreviousSettingData",
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

        static void ApplyVirtualSystemSnapshot(string vmName)
        {
            ManagementScope scope = new ManagementScope(@"root\virtualization", null);
            ManagementObject virtualSystemService = Utility.GetServiceObject(scope, "Msvm_VirtualSystemManagementService");

            ManagementBaseObject inParams = virtualSystemService.GetMethodParameters("ApplyVirtualSystemSnapshot");

            ManagementObject vm = Utility.GetTargetComputer(vmName, scope);

            ManagementObject vmSnapshot = GetLastVirtualSystemSnapshot(vm);

            inParams["SnapshotSettingData"] = vmSnapshot.Path.Path;

            inParams["ComputerSystem"] = vm.Path.Path;

            ManagementBaseObject outParams = virtualSystemService.InvokeMethod("ApplyVirtualSystemSnapshot", inParams, null);

            if ((UInt32)outParams["ReturnValue"] == ReturnCode.Started)
            {
                if (Utility.JobCompleted(outParams, scope))
                {
                    Console.WriteLine("Snapshot was applied successfully.");

                }
                else
                {
                    Console.WriteLine("Failed to apply snapshot.");
                }
            }
            else if ((UInt32)outParams["ReturnValue"] == ReturnCode.Completed)
            {
                Console.WriteLine("Snapshot was applied successfully.");
            }
            else
            {
                Console.WriteLine("Apply virtual system snapshot failed with error {0}", outParams["ReturnValue"]);
            }

            inParams.Dispose();
            outParams.Dispose();
            vmSnapshot.Dispose();
            vm.Dispose();
            virtualSystemService.Dispose();
        }

        static void Main(string[] args)
        {
            if (args != null &amp;&amp; args.Length != 1)
            {
                Console.WriteLine("Usage: ApplyVirtualSystemSnapshot vmName");
                return;
            }
            
            ApplyVirtualSystemSnapshot(args[0]);
        }
    }
}
```



The following VBScript sample applies a virtual system snapshot.

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
        WScript.Echo "usage: cscript ApplyVirtualSystemSnapshot.vbs vmName"
        WScript.Quit(1)
    end if
 
    set vm = GetComputerSystem(vmName)
    set snapshotSetting = GetComputerSystemSnapshotSettings(vm)

    if ApplyVirtualSystemSnapshot(vm, snapshotSetting) then
        WriteLog "Done"
        WScript.Quit(0)
    else
        WriteLog "RemoveVirtualSystemSnapshot failed."
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
' Retrieve the latest Msvm_VirtualComputerSystem snapshot
'-----------------------------------------------------------------
Function GetComputerSystemSnapshotSettings(computerSystem)
    On Error Resume Next
    dim query
    query = Format1("ASSOCIATORS OF {{0}} WHERE resultClass = Msvm_VirtualSystemsettingData AssocClass = Msvm_PreviousSettingData", computerSystem.Path_.Path)
    set GetComputerSystemSnapshotSettings = objWMIService.ExecQuery(query).ItemIndex(0)
    if (Err.Number <> 0) then
        WriteLog Format1("Err.Number: {0}", Err.Number)
        WriteLog Format1("Err.Description:{0}",Err.Description)
        WScript.Quit(1)
    end if
End Function

'-----------------------------------------------------------------
' Apply a virtual system Snapshot
'-----------------------------------------------------------------
Function ApplyVirtualSystemSnapshot(vm, snapshotSettingData)

    dim objInParam, objOutParams
    
    ApplyVirtualSystemSnapshot = false
    set objInParam = managementService.Methods_("ApplyVirtualSystemSnapshot").InParameters.SpawnInstance_()
    objInParam.ComputerSystem = vm.Path_.Path
    objInParam.SnapshotSettingData = snapshotSettingData.Path_.Path
    
    set objOutParams = managementService.ExecMethod_("ApplyVirtualSystemSnapshot", objInParam)

    if objOutParams.ReturnValue = wmiStarted then
        if (WMIJobCompleted(objOutParams)) then
            ApplyVirtualSystemSnapshot = true
        end if
    elseif objOutParams.ReturnValue = wmiSuccessful then
        ApplyVirtualSystemSnapshot = true
    else
        WriteLog Format1("ApplyVirtualSystemSnapshot failed with ReturnValue: {0}", objOutParams.ReturnValue)
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
    set fileStream = fileSystem.OpenTextFile(".\ApplyVirtualSystemSnapshot.log", 8, true)
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
</dt> <dt>

[**ApplyVirtualSystemSnapshotEx**](msvm-virtualsystemmanagementservice-applyvirtualsystemsnapshotex.md)
</dt> <dt>

[**ApplySnapshot (V2)**](https://msdn.microsoft.com/library/windows/desktop/hh850022)
</dt> </dl>

 

 





