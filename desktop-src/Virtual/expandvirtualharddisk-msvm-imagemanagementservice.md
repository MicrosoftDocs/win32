---
title: ExpandVirtualHardDisk method of the Msvm\_ImageManagementService class
description: Expands an existing virtual hard disk (.vhd) file.
ms.assetid: 12ee1f8f-7e88-4177-8652-d7c93cb98882
keywords:
- ExpandVirtualHardDisk method Hyper-V
- ExpandVirtualHardDisk method Hyper-V , Msvm_ImageManagementService class
- Msvm_ImageManagementService class Hyper-V , ExpandVirtualHardDisk method
topic_type:
- apiref
api_name:
- Msvm_ImageManagementService.ExpandVirtualHardDisk
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

# ExpandVirtualHardDisk method of the Msvm\_ImageManagementService class

Expands an existing virtual hard disk (.vhd) file. If the disk image is already attached to the virtual machine, it will send notifications to the running virtual machine about disk expansion.

## Syntax


```mof
uint32 ExpandVirtualHardDisk(
  [in]  string              Path,
  [in]  uint64              MaxInternalSize,
  [out] CIM_ConcreteJob REF Job
);
```



## Parameters

<dl> <dt>

*Path* \[in\]
</dt> <dd>

Type: **string**

A fully qualified path that specifies the location of the disk image file.

</dd> <dt>

*MaxInternalSize* \[in\]
</dt> <dd>

Type: **uint64**

The maximum size of the virtual hard disk as viewable by the virtual machine, in bytes. *MaxInternalSize* minimum value is *DiskSize* + 512 - (*DiskSize* mod 512). *DiskSize* is the disk image file in number of bytes. The InvalidParameter error (32773) is returned if the *MaxInternalSize* value specified is less than the minimum value.

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

The following C# example expands a virtual hard disk file. The referenced utilities can be found in [Common Utilities for the Virtualization Samples](common-utilities-for-the-virtualization-samples.md).


```CSharp
using System;
using System.Management;
namespace HyperVSamples
{
    public class ExpandVirtualHardDiskClass
    {
        const UInt64 Size1G = 0x40000000;

        public static void ExpandVirtualHardDisk(string path, UInt64 maxInternalSize)
        {
            ManagementScope scope = new ManagementScope(@"root\virtualization", null);
            ManagementObject imageService = Utility.GetServiceObject(scope, "Msvm_ImageManagementService");

            ManagementBaseObject inParams = imageService.GetMethodParameters("ExpandVirtualHardDisk");
            inParams["Path"] = path;
            inParams["MaxInternalSize"] = maxInternalSize * Size1G;
            ManagementBaseObject outParams = imageService.InvokeMethod("ExpandVirtualHardDisk", inParams, null);
            if ((UInt32)outParams["ReturnValue"] == ReturnCode.Started)
            {
                if (Utility.JobCompleted(outParams, scope))
                {
                    Console.WriteLine("{0} was expanded successfully.", inParams["Path"]);
                }
                else
                {
                    Console.WriteLine("Unable to expand {0}", inParams["Path"]);
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
                Console.WriteLine("Usage: ExpandVHD path, maxInternalSize");
                Console.WriteLine("maxInternalSize: unit in 1 gigabyte");
                return;
            }
            string path = args[0];
            UInt64 maxInternalSize = UInt64.Parse(args[1]);
            ExpandVirtualHardDisk(path, maxInternalSize);
        }
    }
}
```



The following VBScript example expands a virtual hard disk file.


```VB
option explicit

dim objWMIService
dim managementService
dim fileSystem

const Size1G = &amp;H40000000

const JobStarting = 3
const JobRunning = 4
const JobCompleted = 7
const wmiStarted = 4096


Main()

'-----------------------------------------------------------------
' Main
'-----------------------------------------------------------------
Sub Main()

    dim path, maxInternalSize, objArgs, computer
    
    set fileSystem = Wscript.CreateObject("Scripting.FileSystemObject")

    computer = "."
    set objWMIService = GetObject("winmgmts:\\" & computer & "\root\virtualization")
    set managementService = objWMIService.ExecQuery("Select * from Msvm_ImageManagementService").ItemIndex(0)

    set objArgs = WScript.Arguments
    if WScript.Arguments.Count = 2 then
       path = objArgs.Unnamed.Item(0)
       maxInternalSize = objArgs.Unnamed.Item(1)
    else
       WScript.Echo "usage: cscript ExpandVHD.vbs Path MaxInternalSize"
       WScript.Echo "MaxInternalSize: unit in Gigabytes"
       WScript.Quit(1)
    end if

    if ExpandVirtualHardDisk(path, maxInternalSize) then
        WriteLog "Done"
        WScript.Quit(0)
    else
        WriteLog "ExpandVHD failed"
        WScript.Quit(1)
    end if


End Sub


'-----------------------------------------------------------------
' Execute ExpandVirtualHardDisk
'-----------------------------------------------------------------
Function ExpandVirtualHardDisk(path, maxInternalSize)
    WriteLog Format2("Sub ExpandVirtualHardDisk({0}, {1})",  Path, maxInternalSize)

    dim objInParam, objOutParams
    
    ExpandVirtualHardDisk = false

    set objInParam = managementService.Methods_("ExpandVirtualHardDisk").InParameters.SpawnInstance_()
    objInParam.Path = Path
    objInParam.MaxInternalSize = maxInternalSize * Size1G

    set objOutParams = managementService.ExecMethod_("ExpandVirtualHardDisk", objInParam)

    if (WMIMethodStarted(objOutParams)) then
        if (WMIJobCompleted(objOutParams)) then
            WriteLog Format2("{0} was expected to {1} gigabytes.", Path, MaxInternalSize)
            ExpandVirtualHardDisk = true
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
            WriteLog Format3("Expand VHD {0} to {1} failed. The operation was not able to create ConcreteJob object. Error {2}", Path, MaxInternalSize, wmiStatus)
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
    set fileStream = fileSystem.OpenTextFile(".\ExpandVHD.log", 8, true)
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

[**ResizeVirtualHardDisk (V2)**](https://msdn.microsoft.com/library/windows/desktop/hh850285)
</dt> <dt>

[**CIM\_ConcreteJob**](https://msdn.microsoft.com/library/cc136808)
</dt> <dt>

[**Msvm\_ImageManagementService**](msvm-imagemanagementservice.md)
</dt> </dl>

 

 





