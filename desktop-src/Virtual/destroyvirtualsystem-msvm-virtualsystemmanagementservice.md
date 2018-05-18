---
title: DestroyVirtualSystem method of the Msvm\_VirtualSystemManagementService class
description: Removes the previously defined virtual computer system from the management scope of the host system.
ms.assetid: 'd25938d8-d7f0-4691-8ac5-5d27134404d0'
keywords: ["DestroyVirtualSystem method Hyper-V", "DestroyVirtualSystem method Hyper-V , Msvm_VirtualSystemManagementService class", "Msvm_VirtualSystemManagementService class Hyper-V , DestroyVirtualSystem method"]
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemManagementService.DestroyVirtualSystem
api_location:
- Root\Virtualization
api_type:
- COM
---

# DestroyVirtualSystem method of the Msvm\_VirtualSystemManagementService class

Removes the previously defined virtual computer system from the management scope of the host system. Any associated resource definitions will also be removed. The virtual computer system must be in the powered off or saved state prior to calling this method.

## Syntax


```mof
uint32 DestroyVirtualSystem(
  [in]  CIM_ComputerSystem REF ComputerSystem,
  [out] CIM_ConcreteJob    REF Job
);
```



## Parameters

<dl> <dt>

*ComputerSystem* \[in\]
</dt> <dd>

Type: **CIM\_ComputerSystem**

A reference to the virtual computer system instance to be destroyed.

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

The following C# sample removes a virtual system. The referenced utilities can be found in [Common Utilities for the Virtualization Samples](common-utilities-for-the-virtualization-samples.md).

> \[!Important\]  
> To function correctly, the following code must be run on the VM host server, and must be run with Administrator privileges.

 


```CSharp
using System;
using System.Management;

namespace HyperVSamples
{
    public class DestroyVirtualSystemClass
    {
        public static void DestroyVirtualSystem(string vmName)
        {
            ManagementScope scope = 
                new ManagementScope(@"root\virtualization", null);
            ManagementObject virtualSystemService = 
                Utility.GetServiceObject(scope, "Msvm_VirtualSystemManagementService");

            ManagementBaseObject inParams = 
                virtualSystemService.GetMethodParameters("DestroyVirtualSystem");

            ManagementObject vm = Utility.GetTargetComputer(vmName, scope);

            inParams["ComputerSystem"] = vm.Path.Path;

            ManagementBaseObject outParams = 
                virtualSystemService.InvokeMethod("DestroyVirtualSystem", inParams, null);

            if ((UInt32)outParams["ReturnValue"] == ReturnCode.Started)
            {
                if (Utility.JobCompleted(outParams, scope))
                {
                    Console.WriteLine("VM '{0}' were deleted successfully.", 
                        vm["ElementName"]);

                }
                else
                {
                    Console.WriteLine("Failed to delete VM");
                }
            }
            else if ((UInt32)outParams["ReturnValue"] == ReturnCode.Completed)
            {
                Console.WriteLine("VM '{0}' were deleted successfully.", 
                    vm["ElementName"]);
            }
            else
            {
                Console.WriteLine("Destroy virtual system failed with error {0}", 
                    outParams["ReturnValue"]);
            }

            inParams.Dispose();
            outParams.Dispose();
            vm.Dispose();
            virtualSystemService.Dispose();
        }

        public static void Main(string[] args)
        {
            if (args != null &amp;&amp; args.Length != 1)
            {
                Console.WriteLine("Usage: DestroyVirtualSystem vmName");
                return;
            }

            DestroyVirtualSystem(args[0]);
        }
    }
}
```



The following VBScript sample removes a virtual system.

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
    
    dim computer, vmName, vm, objArgs
    
    set fileSystem = Wscript.CreateObject("Scripting.FileSystemObject")
    computer = "."
    set objWMIService = GetObject("winmgmts:\\" & computer & "\root\virtualization")
    set managementService = objWMIService.ExecQuery("select * from Msvm_VirtualSystemManagementService").ItemIndex(0)
    
    set objArgs = WScript.Arguments
    if WScript.Arguments.Count = 1 then
        vmName = objArgs.Unnamed.Item(0)
    else
        WScript.Echo "usage: cscript DestroyVirtualSystem.vbs vmName"
        WScript.Quit(1)
    end if
    
    set vm = GetComputerSystem(vmName)

    if DestroyVirtualSystem(vm) then
        WriteLog "Done"
        WScript.Quit(0)
    else
        WriteLog "Failed"
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
' Destroy a virtual system
'-----------------------------------------------------------------
Function DestroyVirtualSystem(computerSystem)
    
    dim objInParam, objOutParams
    
    DestroyVirtualSystem = false
    set objInParam = managementService.Methods_("DestroyVirtualSystem").InParameters.SpawnInstance_()
    objInParam.ComputerSystem = computerSystem.Path_.Path
    
    set objOutParams = managementService.ExecMethod_("DestroyVirtualSystem", objInParam)

    if (objOutParams.ReturnValue = wmiStarted) then
        if (WMIJobCompleted(objOutParams)) then
            DestroyVirtualSystem = true
        end if
    elseif (objOutParams.ReturnValue = wmiSuccessful) then
        DestroyVirtualSystem = true
    else
        WriteLog Format1("DestroyVirtualSystem failed with ReturnValue {0}", objOutParams.ReturnValue)
    end if

End Function

'-----------------------------------------------------------------
' Handle wmi Job object
'-----------------------------------------------------------------
Function WMIJobCompleted(outParam)
    
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
    set fileStream = fileSystem.OpenTextFile(".\ADDSCSIContoller.log", 8, true)
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
</dt> </dl>

 

 





