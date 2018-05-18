---
title: CreateVirtualSystemSnapshot method of the Msvm\_VirtualSystemManagementService class
description: Creates a snapshot of a virtual computer system that is in the \ 0034;Enabled \ 0034;, \ 0034;Disabled \ 0034;, or \ 0034;Suspended \ 0034; state.
ms.assetid: 'aeb8a0a0-fed8-4a15-b752-f70997fb05ea'
keywords: ["CreateVirtualSystemSnapshot method Hyper-V", "CreateVirtualSystemSnapshot method Hyper-V , Msvm_VirtualSystemManagementService class", "Msvm_VirtualSystemManagementService class Hyper-V , CreateVirtualSystemSnapshot method"]
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemManagementService.CreateVirtualSystemSnapshot
api_location:
- Root\Virtualization
api_type:
- COM
---

# CreateVirtualSystemSnapshot method of the Msvm\_VirtualSystemManagementService class

Creates a snapshot of a virtual computer system that is in the "Enabled", "Disabled", or "Suspended" state. The result of the snapshot is a new instance of [**Msvm\_VirtualSystemSettingData**](msvm-virtualsystemsettingdata.md) representing the settings for the virtual computer system at the time that the snapshot is taken. In addition, a new instance of each [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214) object will also be created to represent the settings for the devices in the virtual system at the time that the snapshot is taken.

## Syntax


```mof
uint32 CreateVirtualSystemSnapshot(
  [in]  CIM_ComputerSystem           REF SourceSystem,
  [out] CIM_VirtualSystemSettingData REF SnapshotSettingData,
  [out] CIM_ConcreteJob              REF Job
);
```



## Parameters

<dl> <dt>

*SourceSystem* \[in\]
</dt> <dd>

Type: **CIM\_ComputerSystem**

A reference to the virtual computer system to be snapshotted.

</dd> <dt>

*SnapshotSettingData* \[out\]
</dt> <dd>

Type: **CIM\_VirtualSystemSettingData**

The [**CIM\_VirtualSystemSettingData**](https://msdn.microsoft.com/library/cc136954) instance that was created to represent the snapshot.

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

The following C# sample creates a snapshot. The referenced utilities can be found in [Common Utilities for the Virtualization Samples](common-utilities-for-the-virtualization-samples.md).

> \[!Important\]  
> To function correctly, the following code must be run on the VM host server, and must be run with Administrator privileges.

 


```CSharp
using System;
using System.Management;

namespace HyperVSamples
{
    class CreateVirtualSystemSnapshotClass
    {
        static void CreateVirtualSystemSnapshot(string vmName)
        {
            ManagementScope scope = new ManagementScope(@"root\virtualization", null);
            ManagementObject virtualSystemService = Utility.GetServiceObject(scope, "Msvm_VirtualSystemManagementService");

            ManagementObject vm = Utility.GetTargetComputer(vmName, scope);

            ManagementBaseObject inParams = virtualSystemService.GetMethodParameters("CreateVirtualSystemSnapshot");
            inParams["SourceSystem"] = vm.Path.Path;

            ManagementBaseObject outParams = virtualSystemService.InvokeMethod("CreateVirtualSystemSnapshot", inParams, null);

            if ((UInt32)outParams["ReturnValue"] == ReturnCode.Started)
            {
                if (Utility.JobCompleted(outParams, scope))
                {
                    Console.WriteLine("Snapshot was created successfully.");

                }
                else
                {
                    Console.WriteLine("Failed to create snapshot VM");
                }
            }
            else if ((UInt32)outParams["ReturnValue"] == ReturnCode.Completed)
            {
                Console.WriteLine("Snapshot was created successfully.");
            }
            else
            {
                Console.WriteLine("Create virtual system snapshot failed with error {0}", outParams["ReturnValue"]);
            }

            inParams.Dispose();
            outParams.Dispose();
            vm.Dispose();
            virtualSystemService.Dispose();
        }

        static void Main(string[] args)
        {
            if (args != null &amp;&amp; args.Length != 1)
            {
                Console.WriteLine("Usage: CreateVirtualSystemSnapshot vmName");
                return;
            }
            CreateVirtualSystemSnapshot(args[0]);
        }
    }
}
```



The following VBScript sample creates a snapshot.

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

    dim computer, objArgs, vmName, vm
    
    set fileSystem = Wscript.CreateObject("Scripting.FileSystemObject")
    computer = "."
    set objWMIService = GetObject("winmgmts:\\" & computer & "\root\virtualization")
    set managementService = objWMIService.ExecQuery("select * from Msvm_VirtualSystemManagementService").ItemIndex(0)
    
    set objArgs = WScript.Arguments
    if WScript.Arguments.Count = 1 then
        vmName = objArgs.Unnamed.Item(0)
    else
        WScript.Echo "usage: cscript CreateVirtualSystemSnapshot.vbs vmName"
        WScript.Quit(1)
    end if
    

    set vm = GetComputerSystem(vmName)

    if CreateVirtualSystemSnapshot(vm) then
        WriteLog "Done"
        WScript.Quit(0)
    else
        WriteLog "CreateVirtualSystemSnapshot Failed."
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
' Create a virtual system snapshot
'-----------------------------------------------------------------
Function CreateVirtualSystemSnapshot(vm)

    dim objInParam, objOutParams

    CreateVirtualSystemSnapshot = false
    set objInParam = managementService.Methods_("CreateVirtualSystemSnapshot").InParameters.SpawnInstance_()
    objInParam.SourceSystem = vm.Path_.Path
    
    set objOutParams = managementService.ExecMethod_("CreateVirtualSystemSnapshot", objInParam)

    if (objOutParams.ReturnValue = wmiStarted) then
        if (WMIJobCompleted(objOutParams)) then
            CreateVirtualSystemSnapshot = true
        end if
    elseif (objOutParams.ReturnValue = wmiSuccessful) then
        CreateVirtualSystemSnapshot = true
    else
        WriteLog Format1("CreateVirtualSystemSnapshot failed with ReturnValue {0}", objOutParams.ReturnValue)
    end if

End Function

'-----------------------------------------------------------------
' Handle wmi Job object
'-----------------------------------------------------------------
Function WMIJobCompleted(outParam)
    WriteLog "Function WMIJobCompleted"
    
    dim WMIJob, jobState

    set WMIJob = objWMIService.Get(outParam.Job)

    WMIJobCompleted = true

    jobState = WMIJob.JobState

    while jobState = JobRunning or jobState = JobStarting
        WriteLog Format1("In progress... {0}% completed.",WMIJob.PercentComplete)
        WScript.Sleep(1000)
        set WMIJob = objWMIService.Get(outParam.Job)
        jobState = WMIJob.JobState
    wend

    if (jobState <> JobCompleted) then
        WriteLog Format1("ErrorCode:{0}", WMIJob.ErrorCode)
        WriteLog Format1("ErrorDescription:{0}", WMIJob.ErrorDescription)
        WMIJobCompleted = false
    end if

End Function

'-----------------------------------------------------------------
' Create the console log files.
'-----------------------------------------------------------------
Sub WriteLog(line)
    dim fileStream
    set fileStream = fileSystem.OpenTextFile(".\CreateVirtualSystemSnapshot.log", 8, true)
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

[**CreateSnapshot (V2)**](https://msdn.microsoft.com/library/windows/desktop/hh850037)
</dt> </dl>

 

 





