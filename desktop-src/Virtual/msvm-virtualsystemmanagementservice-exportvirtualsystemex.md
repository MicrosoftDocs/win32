---
title: ExportVirtualSystemEx method of the Msvm\_VirtualSystemManagementService class
description: Exports a virtual computer system, or a snapshot of a virtual computer system, in the \ 0034;powered off \ 0034; or \ 0034;saved \ 0034; state to a file.
ms.assetid: cb88394e-97ae-448c-b43f-1c6bcfe0054d
keywords:
- ExportVirtualSystemEx method Hyper-V
- ExportVirtualSystemEx method Hyper-V , Msvm_VirtualSystemManagementService class
- Msvm_VirtualSystemManagementService class Hyper-V , ExportVirtualSystemEx method
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemManagementService.ExportVirtualSystemEx
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

# ExportVirtualSystemEx method of the Msvm\_VirtualSystemManagementService class

Exports a virtual computer system, or a snapshot of a virtual computer system, in the "powered off" or "saved" state to a file. The virtual computer system, its associated configuration settings, and its associated resource settings will be preserved in the resulting file.

## Syntax


```mof
uint32 ExportVirtualSystemEx(
  [in]  CIM_ComputerSystem REF ComputerSystem,
  [in]  string                 ExportDirectory,
  [in]  string                 ExportSettingData,
  [out] CIM_ConcreteJob    REF Job
);
```



## Parameters

<dl> <dt>

*ComputerSystem* \[in\]
</dt> <dd>

Type: **CIM\_ComputerSystem**

A reference to a [**CIM\_ComputerSystem**](https://msdn.microsoft.com/library/aa387219) that represents the virtual computer system to be exported.

</dd> <dt>

*ExportDirectory* \[in\]
</dt> <dd>

Type: **string**

The fully qualified path of the directory to which the virtual computer system is to be exported. If the **CreateVmExportSubdirectory** property in the *ExportSettingData* parameter is set to **True** then this directory can be reused for exporting multiple virtual machines and this method places each virtual computer system definition in a separate subdirectory under this path.

</dd> <dt>

*ExportSettingData* \[in\]
</dt> <dd>

Type: **string**

An instance of the [**Msvm\_VirtualSystemExportSettingData**](msvm-virtualsystemexportsettingdata.md) class that represents the virtual computer system.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

Type: **CIM\_ConcreteJob**

An optional reference that is returned if the operation is executed asynchronously. If present, the returned reference to an instance of [**CIM\_ConcreteJob**](https://msdn.microsoft.com/library/cc136808) can be used to monitor progress and to obtain the result of the method.

</dd> </dl>

## Return value

Type: **uint32**

If this method is executed synchronously, it returns 0 if it succeeds. If this method is executed asynchronously, it returns 4096 (Method Parameters Checked - Job Started) and the *Job* output parameter can be used to track the progress of the asynchronous operation. Any other return value indicates an error. The return value can be one of the following values.

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
    class ExportVirtualSystemExClass
    {
        static string GetVirtualSystemExportSettingDataInstance(ManagementScope scope)
        {
            ManagementPath settingPath = new ManagementPath("Msvm_VirtualSystemExportSettingData");

            ManagementClass exportSettingDataClass = new ManagementClass(scope, settingPath, null);
            ManagementObject exportSettingData = exportSettingDataClass.CreateInstance();

            exportSettingData["CopySnapshotConfiguration"] = 0;
            exportSettingData["CopyVmRuntimeInformation"] = true;
            exportSettingData["CopyVmStorage"] = true;
            exportSettingData["CreateVmExportSubdirectory"] = true;

            string settingData = exportSettingData.GetText(TextFormat.CimDtd20);

            exportSettingData.Dispose();
            exportSettingDataClass.Dispose();

            return settingData;
        }


        static void ExportVirtualSystemEx(string vmName, string exportDirectory)
        {
            ManagementScope scope = new ManagementScope(@"root\virtualization", null);
            ManagementObject virtualSystemService = Utility.GetServiceObject(scope, "Msvm_VirtualSystemManagementService");

            ManagementBaseObject inParams = virtualSystemService.GetMethodParameters("ExportVirtualSystemEx");

            ManagementObject vm = Utility.GetTargetComputer(vmName, scope);
            inParams["ComputerSystem"] = vm.Path.Path;
            
            if (!Directory.Exists(exportDirectory))
            {
                Directory.CreateDirectory(exportDirectory);
            }
            inParams["ExportDirectory"] = exportDirectory;
            inParams["ExportSettingData"] = GetVirtualSystemExportSettingDataInstance(scope);

            ManagementBaseObject outParams = virtualSystemService.InvokeMethod("ExportVirtualSystemEx", inParams, null);

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
                Console.WriteLine("Export virtual system failed with error:{0}", outParams["ReturnValue"]);
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
                Console.WriteLine("Usage: ExportVirtualSystemEx vmName exportDirectory");
                return;
            }
            ExportVirtualSystemEx(args[0], args[1]);
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
        WScript.Echo "usage: cscript ExportVirtualSystemEx.vbs vmName exportDirectoryName"
        WScript.Quit(1)
    end if
    
    set vm = GetComputerSystem(vmName)

    if ExportVirtualSystemEx(vm, exportDirectory) then
        WriteLog "Done"
        WScript.Quit(0)
    else
        WriteLog "ExportVirtualSystemEx Failed."
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
Function ExportVirtualSystemEx(computerSystem, exportDirectory)

    dim objInParam, objOutParams 
    dim query
    dim computer
    dim exportSettingData
 
    ExportVirtualSystemEx = false
    
    if Not fileSystem.FolderExists(exportDirectory) then
        fileSystem.CreateFolder(exportDirectory)
    end if
    
    set objInParam = managementService.Methods_("ExportVirtualSystemEx").InParameters.SpawnInstance_()
    objInParam.ComputerSystem = computerSystem.Path_.Path

    query = Format1("ASSOCIATORS OF {{0}} WHERE resultClass = Msvm_VirtualSystemExportSettingData", computerSystem.Path_.Path)
    set exportSettingData = objWMIService.ExecQuery(query).ItemIndex(0)
    exportSettingData.CopyVmStorage = true
    exportSettingData.CopyVmRuntimeInformation = true
    exportSettingData.CreateVmExportSubdirectory = true
    exportSettingData.CopySnapshotConfiguration = 0
    objInParam.ExportSettingData = exportSettingData.GetText_(1)

    objInParam.ExportDirectory = exportDirectory
    
    set objOutParams = managementService.ExecMethod_("ExportVirtualSystemEx", objInParam)

    if objOutParams.ReturnValue = wmiStarted then
        if (WMIJobCompleted(objOutParams)) then
            ExportVirtualSystemEx = true
        end if
    elseif (objOutParams.ReturnValue = wmiSuccessful) then
        ExportVirtualSystemEx = true
    else
        WriteLog Format1("ExportVirtualSystemEx failed with ReturnValue {0}", objOutParams.ReturnValue)
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
    set fileStream = fileSystem.OpenTextFile(".\ExportVirtualSystemExLog.log", 8, true)
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



For more examples demonstrating the **ExportVirtualSystemEx** method, see [Exporting a Snapshot of a Virtual Machine](exporting-virtual-machines.md).

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                                    |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012<br/>                                                                       |
| Namespace<br/>                | Root\\Virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md)
</dt> <dt>

[**ExportVirtualSystem**](exportvirtualsystem-msvm-virtualsystemmanagementservice.md)
</dt> </dl>

 

 





