---
title: ExportVirtualSystem method of the Msvm\_VirtualSystemManagementService class
description: Exports a virtual computer system in the \ 0034;powered off \ 0034; state to a file.
ms.assetid: 'dab296f1-76e3-4bc8-ba2e-29777a3d480c'
keywords: ["ExportVirtualSystem method Hyper-V", "ExportVirtualSystem method Hyper-V , Msvm_VirtualSystemManagementService class", "Msvm_VirtualSystemManagementService class Hyper-V , ExportVirtualSystem method"]
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemManagementService.ExportVirtualSystem
api_location:
- Root\Virtualization
api_type:
- COM
---

# ExportVirtualSystem method of the Msvm\_VirtualSystemManagementService class

Beginning with Windows Server 2008 R2 this method is deprecated. Use the [**ExportVirtualSystemEx**](msvm-virtualsystemmanagementservice-exportvirtualsystemex.md) method.

**Windows Server 2008:** Exports a virtual computer system in the "powered off" state to a file. The virtual computer system, its associated configuration settings, and its associated resource settings will be preserved in the resulting file.

## Syntax


```mof
uint32 ExportVirtualSystem(
  [in]  CIM_ComputerSystem REF ComputerSystem,
  [in]  boolean                CopyVmState,
  [in]  string                 ExportDirectory,
  [out] CIM_ConcreteJob    REF Job
);
```



## Parameters

<dl> <dt>

*ComputerSystem* \[in\]
</dt> <dd>

Type: **CIM\_ComputerSystem**

A reference to a [**CIM\_ComputerSystem**](https://msdn.microsoft.com/library/aa387219) that represents the virtual computer system to be exported.

</dd> <dt>

*CopyVmState* \[in\]
</dt> <dd>

Type: **boolean**

Indicates whether the state, such as virtual hard disks, saved state files, and memory content files, will be exported.

</dd> <dt>

*ExportDirectory* \[in\]
</dt> <dd>

Type: **string**

The fully qualified path of the directory to which the virtual computer system is to be exported. This directory can be reused for exporting multiple virtual machines. This method places each virtual computer system definition in a separate subdirectory under this path.

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

The following C# sample exports a virtual system. The referenced utilities can be found in [Common Utilities for the Virtualization Samples](common-utilities-for-the-virtualization-samples.md).

> \[!Important\]  
> To function correctly, the following code must be run on the VM host server, and must be run with Administrator privileges.

 


```CSharp
using System;
using System.IO;
using System.Management;

namespace HyperVSamples
{
    class ExportVirtualSystemClass
    {
        static void ExportVirtualSystem(string vmName, string exportDirectory)
        {
            ManagementScope scope = new ManagementScope(@"root\virtualization", null);
            ManagementObject virtualSystemService = Utility.GetServiceObject(scope, "Msvm_VirtualSystemManagementService");

            ManagementBaseObject inParams = virtualSystemService.GetMethodParameters("ExportVirtualSystem");

            ManagementObject vm = Utility.GetTargetComputer(vmName, scope);
            inParams["ComputerSystem"] = vm.Path.Path;
            inParams["CopyVmState"] = true;

            if (!Directory.Exists(exportDirectory))
            {
                Directory.CreateDirectory(exportDirectory);
            }
            inParams["ExportDirectory"] = exportDirectory;


            ManagementBaseObject outParams = virtualSystemService.InvokeMethod("ExportVirtualSystem", inParams, null);

            if ((UInt32)outParams["ReturnValue"] == ReturnCode.Started)
            {
                if (Utility.JobCompleted(outParams, scope))
                {
                    Console.WriteLine("VM '{0}' were exported successfully.", vm["ElementName"]);

                }
                else
                {
                    Console.WriteLine("Failed to export VM");
                }
            }
            else if ((UInt32)outParams["ReturnValue"] == ReturnCode.Completed)
            {
                Console.WriteLine("VM '{0}' were exported successfully.", vm["ElementName"]);
            }
            else
            {
                Console.WriteLine("Export virtual system failed with error {0}", outParams["ReturnValue"]);
            }

            inParams.Dispose();
            outParams.Dispose();
            vm.Dispose();
            virtualSystemService.Dispose();

        }

        static void Main(string[] args)
        {
            if (args != null &amp;&amp; args.Length != 2)
            {
                Console.WriteLine("Usage: ExportVirtualSystem vmName exportDirectory");
                return;
            }
            ExportVirtualSystem(args[0], args[1]);
        }
    }
}
```



The following VBScript sample exports a virtual system.

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

    dim computer, objArgs, vmName, vm, exportDirectory
    
    set fileSystem = Wscript.CreateObject("Scripting.FileSystemObject")
    computer = "."
    set objWMIService = GetObject("winmgmts:\\" & computer & "\root\virtualization")
    set managementService = objWMIService.ExecQuery("select * from Msvm_VirtualSystemManagementService").ItemIndex(0)
    
    set objArgs = WScript.Arguments
    if WScript.Arguments.Count = 2 then
        vmName = objArgs.Unnamed.Item(0)
        exportDirectory = objArgs.Unnamed.Item(1)
    else
        WScript.Echo "usage: cscript ExportVirtualSystem.vbs vmName exportDirectoryName"
        WScript.Quit(1)
    end if
    
    set vm = GetComputerSystem(vmName)

    if ExportVirtualSystem(vm, exportDirectory) then
        WriteLog "Done"
        WScript.Quit(0)
    else
        WriteLog "ExportVirtualSystem Failed."
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
' Export a virtual system
'-----------------------------------------------------------------
Function ExportVirtualSystem(computerSystem, exportDirectory)

    dim objInParam, objOutParams 
    ExportVirtualSystem = false
    
    if Not fileSystem.FolderExists(exportDirectory) then
        fileSystem.CreateFolder(exportDirectory)
    end if
    
    set objInParam = managementService.Methods_("ExportVirtualSystem").InParameters.SpawnInstance_()
    objInParam.ComputerSystem = computerSystem.Path_.Path
    objInParam.CopyVmState = true
    objInParam.ExportDirectory = exportDirectory
    
    set objOutParams = managementService.ExecMethod_("ExportVirtualSystem", objInParam)

    if objOutParams.ReturnValue = wmiStarted then
        if (WMIJobCompleted(objOutParams)) then
            ExportVirtualSystem = true
        end if
    elseif (objOutParams.ReturnValue = wmiSuccessful) then
        ExportVirtualSystem = true
    else
        WriteLog Format1("ExportVirtualSystem failed with ReturnValue {0}", wmiStatus)
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
</dt> <dt>

[**ExportVirtualSystemEx**](msvm-virtualsystemmanagementservice-exportvirtualsystemex.md)
</dt> </dl>

 

 





