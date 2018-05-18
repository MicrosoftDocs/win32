---
title: Mount method of the Msvm\_ImageManagementService class
description: Mounts a virtual disk image file in loopback mode.
ms.assetid: '87e949f0-2b48-42c2-9c31-88fec829b325'
keywords: ["Mount method Hyper-V", "Mount method Hyper-V , Msvm_ImageManagementService class", "Msvm_ImageManagementService class Hyper-V , Mount method"]
topic_type:
- apiref
api_name:
- Msvm_ImageManagementService.Mount
api_location:
- vds.h
api_type:
- COM
---

# Mount method of the Msvm\_ImageManagementService class

Mounts a virtual disk image file in loopback mode.

## Syntax


```mof
uint32 Mount(
  [in]  string              Path,
  [out] CIM_ConcreteJob REF Job
);
```



## Parameters

<dl> <dt>

*Path* \[in\]
</dt> <dd>

Type: **string**

A fully qualified path that specifies the location of the virtual disk image file.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

Type: **[**CIM\_ConcreteJob**](https://msdn.microsoft.com/library/cc136808)**

A reference to the job, represented by a [**CIM\_ConcreteJob**](https://msdn.microsoft.com/library/cc136808) object (can be **null** if the task is completed).

</dd> </dl>

## Return value

Type: **uint32**

This method can return one of the following values.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Return code/value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><dl> <dt><strong>Completed with No Error</strong></dt> <dt>0</dt> </dl></td>

</tr>
<tr class="even">
<td><dl> <dt><strong>Method Parameters Checked - Job Started</strong></dt> <dt>4096</dt> </dl></td>

</tr>
<tr class="odd">
<td><dl> <dt><strong>Failed</strong></dt> <dt>32768</dt> </dl></td>

</tr>
<tr class="even">
<td><dl> <dt><strong>Access Denied</strong></dt> <dt>32769</dt> </dl></td>

</tr>
<tr class="odd">
<td><dl> <dt><strong>Not Supported</strong></dt> <dt>32770</dt> </dl></td>

</tr>
<tr class="even">
<td><dl> <dt><strong>Status is unknown</strong></dt> <dt>32771</dt> </dl></td>

</tr>
<tr class="odd">
<td><dl> <dt><strong>Timeout</strong></dt> <dt>32772</dt> </dl></td>

</tr>
<tr class="even">
<td><dl> <dt><strong>Invalid parameter</strong></dt> <dt>32773</dt> </dl></td>

</tr>
<tr class="odd">
<td><dl> <dt><strong>System is in used</strong></dt> <dt>32774</dt> </dl></td>

</tr>
<tr class="even">
<td><dl> <dt><strong>Invalid state for this operation</strong></dt> <dt>32775</dt> </dl></td>

</tr>
<tr class="odd">
<td><dl> <dt><strong>Incorrect data type</strong></dt> <dt>32776</dt> </dl></td>

</tr>
<tr class="even">
<td><dl> <dt><strong>System is not available</strong></dt> <dt>32777</dt> </dl></td>

</tr>
<tr class="odd">
<td><dl> <dt><strong>Out of memory</strong></dt> <dt>32778</dt> </dl></td>

</tr>
<tr class="even">
<td><dl> <dt><strong>File not found</strong></dt> <dt>32779</dt> </dl></td>
<td><blockquote>
[!Note]<br />
Added in Windows Server 2012 R2.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

## Remarks

Access to the [**Msvm\_ImageManagementService**](msvm-imagemanagementservice.md) class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Examples

The following C# example mounts a virtual disk image file. The referenced utilities can be found in [Common Utilities for the Virtualization Samples](common-utilities-for-the-virtualization-samples.md).


```CSharp
using System;
using System.Management;

namespace HyperVSamples
{
    class MountVHD
    {
        static void Mount(string path)
        {
            ManagementScope scope = new ManagementScope(@"root\virtualization", null);
            ManagementObject imageService = Utility.GetServiceObject(scope, "Msvm_ImageManagementService");

            ManagementBaseObject inParams = imageService.GetMethodParameters("Mount");
            inParams["Path"] = path;
            ManagementBaseObject outParams = imageService.InvokeMethod("Mount", inParams, null);
            if ((UInt32)outParams["ReturnValue"] == ReturnCode.Started)
            {
                if (Utility.JobCompleted(outParams, scope))
                {
                    Console.WriteLine("{0} was mounted successfully.", inParams["Path"]);
                }
                else
                {
                    Console.WriteLine("Unable to mount {0}", inParams["Path"]);
                }
            }
            inParams.Dispose();
            outParams.Dispose();
            imageService.Dispose();
        }

        static void Main(string[] args)
        {
            if (args != null &amp;&amp; args.Length != 1)
            {
                Console.WriteLine("Usage: MountVHD vhdPath");
                return;
            }
            Mount(args[0]);
        }
    }
}

```



The following VBScript example mounts a virtual disk image file.


```VB
option explicit 

dim objWMIService
dim managementService
dim fileSystem

const JobStarting = 3
const JobRunning = 4
const JobCompleted = 7
const wmiStarted = 4096

dim vhdPath

Main()

'-----------------------------------------------------------------
' Main
'-----------------------------------------------------------------
Sub Main()

    dim computer, objArgs
    set fileSystem = Wscript.CreateObject("Scripting.FileSystemObject")

    computer = "."
    set objWMIService = GetObject("winmgmts:\\" & computer & "\root\virtualization")
    set managementService = objWMIService.ExecQuery("Select * from Msvm_ImageManagementService").ItemIndex(0)

    set objArgs = WScript.Arguments
    if WScript.Arguments.Count = 1 then
        vhdPath = objArgs.Unnamed.Item(0)
    else
        WScript.Echo "usage: cscript MountVHD.vbs VHDFilePath"
        WScript.Quit(1)
    end if

    if ExecuteMountVHD then
        WriteLog "Done"
        WScript.Quit(0)
    else
        WriteLog "Mount failed"
        WScript.Quit(1)
    end if
End Sub

'-----------------------------------------------------------------
' Execute Mount
'-----------------------------------------------------------------
Function ExecuteMountVHD()
    WriteLog Format1("Sub ExecuteMountVHD({0})",  vhdPath)
    
    dim objInParam, objOutParams

    ExecuteMountVHD = false
    set objInParam = managementService.Methods_("Mount").InParameters.SpawnInstance_()
    objInParam.Path = vhdPath

    set objOutParams = managementService.ExecMethod_("Mount", objInParam)

    if (WMIMethodStarted(objOutParams)) then
        if (WMIJobCompleted(objOutParams)) then
            WriteLog Format1("VHD {0} was mounted successfully!", vhdPath)
            ExecuteMountVHD = true
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
            WriteLog Format2("Mount operation for VHD {0} failed to create ConcreteJob with error {1}", vhdPath, wmiStatus)
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
    set fileStream = fileSystem.OpenTextFile(".\MountVHD.log", 8, true)
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
| Header<br/>                   | <dl> <dt>Vds.h</dt> </dl>                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**AttachVirtualHardDisk (V2)**](https://msdn.microsoft.com/library/windows/desktop/hh850023)
</dt> <dt>

[**CIM\_ConcreteJob**](https://msdn.microsoft.com/library/cc136808)
</dt> <dt>

[**Msvm\_ImageManagementService**](msvm-imagemanagementservice.md)
</dt> </dl>

 

 





