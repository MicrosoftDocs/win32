---
title: MergeVirtualHardDisk method of the Msvm\_ImageManagementService class
description: Merges a differencing virtual hard disk file with its parents.
ms.assetid: '63052435-ee95-41f3-8107-edabda5a333e'
keywords: ["MergeVirtualHardDisk method Hyper-V", "MergeVirtualHardDisk method Hyper-V , Msvm_ImageManagementService class", "Msvm_ImageManagementService class Hyper-V , MergeVirtualHardDisk method"]
topic_type:
- apiref
api_name:
- Msvm_ImageManagementService.MergeVirtualHardDisk
api_location:
- Root\Virtualization
api_type:
- COM
---

# MergeVirtualHardDisk method of the Msvm\_ImageManagementService class

Merges a differencing virtual hard disk file with its parents. If the user executing this function does not have permission to update the virtual machines, then this function will fail.

## Syntax


```mof
uint32 MergeVirtualHardDisk(
  [in]  string              SourcePath,
  [in]  string              DestinationPath,
  [out] CIM_ConcreteJob REF Job
);
```



## Parameters

<dl> <dt>

*SourcePath* \[in\]
</dt> <dd>

Type: **string**

A fully qualified path that specifies the location of the merging file.

</dd> <dt>

*DestinationPath* \[in\]
</dt> <dd>

Type: **string**

A fully qualified path that specifies the location of the parent disk image file into which data is to be merged. This could be the immediate parent virtual disk image of the merging file or parent disk image few levels up the differencing drive chain.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

Type: **[**CIM\_ConcreteJob**](https://msdn.microsoft.com/library/cc136808)**

A reference to the job (can be **null** if the task is completed).

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

The following C# example merges a differencing virtual hard disk file. The referenced utilities can be found in [Common Utilities for the Virtualization Samples](common-utilities-for-the-virtualization-samples.md).


```CSharp
using System;
using System.Management;

namespace HyperVSamples
{
    class MergeVHD
    {
        static void MergeVirtualHardDisk(string sourcePath, string destinationPath)
        {

            ManagementScope scope = new ManagementScope(@"root\virtualization", null);
            ManagementObject imageService = Utility.GetServiceObject(scope, "Msvm_ImageManagementService");

            ManagementBaseObject inParams = imageService.GetMethodParameters("MergeVirtualHardDisk");
            inParams["SourcePath"] = sourcePath;
            inParams["DestinationPath"] = destinationPath;
            ManagementBaseObject outParams = imageService.InvokeMethod("MergeVirtualHardDisk", inParams, null);
            if ((UInt32)outParams["ReturnValue"] == ReturnCode.Started)
            {
                if (Utility.JobCompleted(outParams, scope))
                {
                    Console.WriteLine("{0} was merged successfully.", inParams["SourcePath"]);
                }
                else
                {
                    Console.WriteLine("Unable to merge {0}", inParams["SourcePath"]);
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
                Console.WriteLine("Usage: MergeVHD SourcePath, DestinationPath");
                return;
            }
            MergeVirtualHardDisk(args[0], args[1]);
        }
    }
}

```



The following VBScript example merges a differencing virtual hard disk file.


```VB
option explicit

dim objWMIService
dim managementService
dim fileSystem

const JobStarting = 3
const JobRunning = 4
const JobCompleted = 7
const wmiStarted = 4096

const method = ""

Main()

'-----------------------------------------------------------------
' Main
'-----------------------------------------------------------------
Sub Main()
    
    dim sourcePath, destinationPath, computer, objArgs
    
    set fileSystem = Wscript.CreateObject("Scripting.FileSystemObject")

    computer = "."
    set objWMIService = GetObject("winmgmts:\\" & computer & "\root\virtualization")
    set managementService = objWMIService.ExecQuery("Select * from Msvm_ImageManagementService").ItemIndex(0)


    set objArgs = WScript.Arguments
    if WScript.Arguments.Count = 2 then
       sourcePath = objArgs.Unnamed.Item(0)
       destinationPath = objArgs.Unnamed.Item(1)
    else
       WScript.Echo "usage: cscript ConvertVHD.vbs sourcePath destinationPath"
       WScript.Quit(1)
    end if

    if MergeVirtualHardDisk(sourcePath, destinationPath)  then
        WriteLog "Done"
        WScript.Quit(0)
    else
        WriteLog "ConvertVHD failed"
        WScript.Quit(1)
    end if


End Sub

'-----------------------------------------------------------------
' Execute MergeVirtualHardDisk
'-----------------------------------------------------------------
Function MergeVirtualHardDisk(sourcePath, destinationPath)
    WriteLog Format2("Sub MergeVirtualHardDisk({0}, {1})",  sourcePath, DestinationPath)
    
    dim objInParam, objOutParams

    MergeVirtualHardDisk = false

    set objInParam = managementService.Methods_("MergeVirtualHardDisk").InParameters.SpawnInstance_()
    objInParam.SourcePath = SourcePath
    objInParam.DestinationPath = DestinationPath

    set objOutParams = managementService.ExecMethod_("MergeVirtualHardDisk", objInParam)

    if (WMIMethodStarted(objOutParams)) then
        if (WMIJobCompleted(objOutParams)) then
            WriteLog Format2("'{0}' was successfully merged into '{1}'.", sourcePath, destinationPath)
            MergeVirtualHardDisk = true
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
            WriteLog Format1("Merge operation failed to create ConcreteJob with error {2}",  wmiStatus)
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
    set fileStream = fileSystem.OpenTextFile(".\MergeVHD.log", 8, true)
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
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012<br/>                                                                       |
| Namespace<br/>                | Root\\Virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**MergeVirtualHardDisk (V2)**](https://msdn.microsoft.com/library/windows/desktop/hh850091)
</dt> <dt>

[**CIM\_ConcreteJob**](https://msdn.microsoft.com/library/cc136808)
</dt> <dt>

[**Msvm\_ImageManagementService**](msvm-imagemanagementservice.md)
</dt> </dl>

 

 





