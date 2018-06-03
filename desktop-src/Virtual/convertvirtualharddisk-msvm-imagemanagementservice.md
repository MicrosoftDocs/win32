---
title: ConvertVirtualHardDisk method of the Msvm\_ImageManagementService class
description: Converts the type of an existing virtual hard disk.
ms.assetid: bd424b72-4b08-47b4-931e-ad80ef85bdc8
keywords:
- ConvertVirtualHardDisk method Hyper-V
- ConvertVirtualHardDisk method Hyper-V , Msvm_ImageManagementService class
- Msvm_ImageManagementService class Hyper-V , ConvertVirtualHardDisk method
topic_type:
- apiref
api_name:
- Msvm_ImageManagementService.ConvertVirtualHardDisk
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

# ConvertVirtualHardDisk method of the Msvm\_ImageManagementService class

Converts the type of an existing virtual hard disk.

## Syntax


```mof
uint32 ConvertVirtualHardDisk(
  [in]  string              SourcePath,
  [in]  string              DestinationPath,
  [in]  uint16              Type,
  [out] CIM_ConcreteJob REF Job
);
```



## Parameters

<dl> <dt>

*SourcePath* \[in\]
</dt> <dd>

Type: **string**

A fully qualified path that specifies the location of the virtual hard disk file. This file will not be modified as a result of this operation.

</dd> <dt>

*DestinationPath* \[in\]
</dt> <dd>

Type: **string**

A fully qualified path that specifies the location of the destination virtual hard disk file.

</dd> <dt>

*Type* \[in\]
</dt> <dd>

Type: **uint16**

The type of the new virtual hard disk file.

<dt>

<span id="Fixed"></span><span id="fixed"></span><span id="FIXED"></span>

**Fixed** (2)


</dt> <dd></dd> <dt>

<span id="Dynamic"></span><span id="dynamic"></span><span id="DYNAMIC"></span>

**Dynamic** (3)


</dt> <dd></dd> <dt>

<span id="PhysicalDrive"></span><span id="physicaldrive"></span><span id="PHYSICALDRIVE"></span>

**PhysicalDrive** (5)


</dt> <dd></dd> </dl> </dd> <dt>

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

The following C# example converts a virtual hard disk. The referenced utilities can be found in [Common Utilities for the Virtualization Samples](common-utilities-for-the-virtualization-samples.md).


```CSharp
using System;
using System.Management;

namespace HyperVSamples
{
    class ConvertVHD
    {
        enum DiskType
        {
            Fixed = 2,
            Dynamic = 3,
            PhysicalDrive = 5
        }
            
        static void ConvertVirtualHardDisk(string sourcePath, string destinationPath, string diskTypeName)
        {
            ManagementScope scope = new ManagementScope(@"root\virtualization", null);
            ManagementObject imageService = Utility.GetServiceObject(scope, "Msvm_ImageManagementService");
            DiskType diskType = (DiskType)Enum.Parse(typeof(DiskType), diskTypeName, true);

            ManagementBaseObject inParams = imageService.GetMethodParameters("ConvertVirtualHardDisk");
            inParams["SourcePath"] = sourcePath;
            inParams["DestinationPath"] = destinationPath;
            inParams["Type"] = diskType;
            ManagementBaseObject outParams = imageService.InvokeMethod("ConvertVirtualHardDisk", inParams, null);
            if ((UInt32)outParams["ReturnValue"] == ReturnCode.Started)
            {
                if (Utility.JobCompleted(outParams, scope))
                {
                    Console.WriteLine("{0} was converted successfully.", inParams["SourcePath"]);
                }
                else
                {
                    Console.WriteLine("Unable to convert {0}", inParams["SourcePath"]);
                }
            }

            inParams.Dispose();
            outParams.Dispose();
            imageService.Dispose();
        }

        static void Main(string[] args)
        {
            if (args != null &amp;&amp; args.Length != 3)
            {
                Console.WriteLine("Usage: ConvertVHD SourcePath, DestinationPath, Type");
                Console.WriteLine("Type:Fixed|Dynamic|PhysicalDrive");
                return;
            }
            ConvertVirtualHardDisk(args[0], args[1], args[2]);
        }
    }
}
```



The following VBScript example converts a virtual hard disk.


```VB
option explicit
 
dim objWMIService
dim vhdPath
dim managementService
dim fileSystem


const JobStarting = 3
const JobRunning = 4
const JobCompleted = 7
const wmiStarted = 4096

'targetVHD type
const Fixed = 2
const Dynamic = 3
const PhysicalDrive = 5

Main()

'-----------------------------------------------------------------
' Main
'-----------------------------------------------------------------
Sub Main()

    dim computer, objArgs, sourcePath, destinationPath, vhdTypeName

    set fileSystem = Wscript.CreateObject("Scripting.FileSystemObject")

    computer = "."
    set objWMIService = GetObject("winmgmts:\\" & computer & "\root\virtualization")
    set managementService = objWMIService.ExecQuery("Select * from Msvm_ImageManagementService").ItemIndex(0)    

    set objArgs = WScript.Arguments
    if WScript.Arguments.Count = 3 then
       sourcePath = objArgs.Unnamed.Item(0)
       destinationPath = objArgs.Unnamed.Item(1)
       vhdTypeName = objArgs.Unnamed.Item(2)
    else
       Usage
    end if

    if ExecuteConvertVHD(sourcePath, destinationPath, vhdTypeName) then
        WriteLog "Done"
        WScript.Quit(0)
    else
        WriteLog "ConvertVHD failed"
        WScript.Quit(1)
    end if
End Sub


'-----------------------------------------------------------------
' Display Script Usage
'-----------------------------------------------------------------
Sub Usage()
    WScript.Echo "usage: cscript ConvertVHD.vbs SourcePath DestinationPath Type"
    WScript.Echo "Type:Fixed|Dynamic|PhysicalDrive"
    WScript.Quit(1)
End Sub

'-----------------------------------------------------------------
' set target disk type
'-----------------------------------------------------------------
Function DiskTypeValue(TypeName)
    if LCase(TypeName) = "fixed" then
        DiskTypeValue = Fixed
    elseif LCase(TypeName) = "dynamic" then
        DiskTypeValue = Dynamic
    elseif LCase(TypeName) = "physicaldrive" then
        DiskTypeValue = PhysicalDrive
    else
        Usage
    end if
End Function

'-----------------------------------------------------------------
' Execute ConvertVirtualHardDisk
'-----------------------------------------------------------------
Function ExecuteConvertVHD(sourcePath, destination, vhdTypeName)
    WriteLog Format3("Sub ExecuteConvertVHD({0}, {1}, {2})",  sourcePath, destination, vhdTypeName)

    dim objInParam, objOutParams
    
    ExecuteConvertVHD = false
    set objInParam = managementService.Methods_("ConvertVirtualHardDisk").InParameters.SpawnInstance_()
    objInParam.Type = DiskTypeValue(vhdTypeName)
    objInParam.SourcePath = sourcePath
    objInParam.DestinationPath = destination

    set objOutParams = managementService.ExecMethod_("ConvertVirtualHardDisk", objInParam)

    if (WMIMethodStarted(objOutParams)) then
        if (WMIJobCompleted(objOutParams)) then
            WriteLog Format3("VHD {0} was converted to {1} as a {2} VHD successfully.", sourcePath, destination, vhdTypeName)
            ExecuteConvertVHD = true
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
            WriteLog Format1("Convert VHD with error {0}", wmiStatus)
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
    set fileStream = fileSystem.OpenTextFile(".\ConvertVHD.log", 8, true)
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

[**ConvertVirtualHardDisk (V2)**](https://msdn.microsoft.com/library/windows/desktop/hh850035)
</dt> <dt>

[**CIM\_ConcreteJob**](https://msdn.microsoft.com/library/cc136808)
</dt> <dt>

[**Msvm\_ImageManagementService**](msvm-imagemanagementservice.md)
</dt> </dl>

 

 





