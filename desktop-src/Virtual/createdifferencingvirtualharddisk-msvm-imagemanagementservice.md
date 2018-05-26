---
title: CreateDifferencingVirtualHardDisk method of the Msvm\_ImageManagementService class
description: Creates a differencing virtual hard disk (.vhd) file.
ms.assetid: bc0194f8-8751-421a-b5e4-6c327e97fc6d
keywords:
- CreateDifferencingVirtualHardDisk method Hyper-V
- CreateDifferencingVirtualHardDisk method Hyper-V , Msvm_ImageManagementService class
- Msvm_ImageManagementService class Hyper-V , CreateDifferencingVirtualHardDisk method
topic_type:
- apiref
api_name:
- Msvm_ImageManagementService.CreateDifferencingVirtualHardDisk
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

# CreateDifferencingVirtualHardDisk method of the Msvm\_ImageManagementService class

Creates a differencing virtual hard disk (.vhd) file.

## Syntax


```mof
uint32 CreateDifferencingVirtualHardDisk(
  [in]  string              Path,
  [in]  string              ParentPath,
  [out] CIM_ConcreteJob REF Job
);
```



## Parameters

<dl> <dt>

*Path* \[in\]
</dt> <dd>

Type: **string**

A fully qualified path that specifies the location of the new file.

</dd> <dt>

*ParentPath* \[in\]
</dt> <dd>

Type: **string**

A fully qualified path that specifies the location of the parent virtual hard disk file.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

Type: **[**CIM\_ConcreteJob**](https://msdn.microsoft.com/library/cc136808)**

A reference to the job (can be null if the task is completed).

</dd> </dl>

## Return value

Type: **uint32**

This method can return one of the following values.

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
</dt> <dt>

**File not found** (32779)
</dt> </dl>

## Remarks

Access to the [**Msvm\_ImageManagementService**](msvm-imagemanagementservice.md) class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Examples

The following C# example creates a differencing virtual hard disk file. The referenced utilities can be found in [Common Utilities for the Virtualization Samples](common-utilities-for-the-virtualization-samples.md).


```CSharp
using System;
using System.Management;

namespace HyperVSamples
{
    class CreateDiffVHD
    {
        static void CreateDifferencingVirtualHardDisk(string path, string parentPath)
        {
            ManagementScope scope = new ManagementScope(@"root\virtualization", null);
            ManagementObject imageService = Utility.GetServiceObject(scope, "Msvm_ImageManagementService");

            ManagementBaseObject inParams = imageService.GetMethodParameters("CreateDifferencingVirtualHardDisk");
            inParams["ParentPath"] = parentPath;
            inParams["Path"] = path;
            ManagementBaseObject outParams = imageService.InvokeMethod("CreateDifferencingVirtualHardDisk", inParams, null);
            if ((UInt32)outParams["ReturnValue"] == ReturnCode.Started)
            {
                if (Utility.JobCompleted(outParams, scope))
                {
                    Console.WriteLine("{0} was created successfully.", inParams["Path"]);
                }
                else
                {
                    Console.WriteLine("Unable to create {0}", inParams["Path"]);
                }
            }

            inParams.Dispose();
            outParams.Dispose();
            imageService.Dispose();
        }

        static void Main(string[] args)
        {
            if (args != null &amp;&amp; args.Length != 2)
            {
                Console.WriteLine("Usage: CreateDiffVHD path, parentPath");
                return;
            }
            CreateDifferencingVirtualHardDisk(args[0], args[1]);
        }
    }
}

```



The following VBScript example creates a differencing virtual hard disk file.


```VB
option explicit 

dim objWMIService
dim computerName
dim managementService
dim fileSystem

const JobStarting = 3
const JobRunning = 4
const JobCompleted = 7
const wmiStarted = 4096



const method = "CreateDifferencingVirtualHardDisk"

Main()

'-----------------------------------------------------------------
' Main routine
'-----------------------------------------------------------------
Sub Main()

    dim path, parentPath, computer, objArgs
    
    set fileSystem = Wscript.CreateObject("Scripting.FileSystemObject")

    computer = "."
    set objWMIService = GetObject("winmgmts:\\" & computer & "\root\virtualization")
    set managementService = objWMIService.ExecQuery("Select * from Msvm_ImageManagementService").ItemIndex(0)

    set objArgs = WScript.Arguments
    if WScript.Arguments.Count = 2 then
       path = objArgs.Unnamed.Item(0)
       parentPath = objArgs.Unnamed.Item(1)
    else
       WScript.Echo "usage: cscript CreateDiffVHD.vbs path ParentPath"
       WScript.Quit(1)
    end if

    if ExecuteCreateDiffVHD(path, parentPath) then
       WriteLog "Done"
       WScript.Quit(0)
    else
        WriteLog "CreateDiffVHD failed"
        WScript.Quit(1)
    end if
End Sub


'-----------------------------------------------------------------
' Execute CreateDifferencingVirtualHardDisk
'-----------------------------------------------------------------
Function ExecuteCreateDiffVHD(path, parentPath)
    WriteLog Format2("Sub ExecuteCreateDiffVHD({0}, {1})",  Path, ParentPath)
    
    dim objInParam, objOutParams
    
    ExecuteCreateDiffVHD = false

    set objInParam = managementService.Methods_("CreateDifferencingVirtualHardDisk").InParameters.SpawnInstance_()
    objInParam.Path = path
    objInParam.ParentPath = parentPath

    set objOutParams = managementService.ExecMethod_("CreateDifferencingVirtualHardDisk", objInParam)

    if (WMIMethodStarted(objOutParams)) then
        if (WMIJobCompleted(objOutParams)) then
            WriteLog Format2("'{0}' was created as a differencing disk of '{1}' .", Path, ParentPath)
            ExecuteCreateDiffVHD = true
        end if
    end if

End Function


'-----------------------------------------------------------------
' Handle wmi return values
'-----------------------------------------------------------------
Function WMIMethodStarted(outParam)
    WriteLog "Function WMIMethodStarted"
    
    dim wmiStatus
    
    WMIMethodStarted = false

    if Not IsNull(outParam) then
        wmiStatus = outParam.ReturnValue

        if  wmiStatus = wmiStarted then
            WMIMethodStarted = true
        else
            WriteLog Format3("Failed to create differencing disk {0} for {1} with error {2}", Path, ParentPath, wmiStatus)
        end if
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

    while jobState= JobRunning or jobState = JobStarting
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
    set fileStream = fileSystem.OpenTextFile(".\CreateDiffVHD.log", 8, true)
    WScript.Echo line
    fileStream.WriteLine line
    fileStream.Close

End Sub

'------------------------------------------------------------------------------
' The string formatting functions to avoid string concatenation.
'------------------------------------------------------------------------------
Function Format3(myString, arg0, arg1, arg2)

    Format3 = Format2(myString, arg0, arg1)
    Format3 = Replace(Format3, "{2}", arg2)

End Function

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

[**CreateVirtualHardDisk (V2)**](https://msdn.microsoft.com/library/windows/desktop/hh850039)
</dt> <dt>

[**CIM\_ConcreteJob**](https://msdn.microsoft.com/library/cc136808)
</dt> <dt>

[**Msvm\_ImageManagementService**](msvm-imagemanagementservice.md)
</dt> </dl>

 

 





