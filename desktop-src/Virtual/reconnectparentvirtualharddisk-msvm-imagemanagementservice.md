---
title: ReconnectParentVirtualHardDisk method of the Msvm\_ImageManagementService class
description: Fixes broken links between parent and child disk image files.
ms.assetid: e0b403f6-3e0e-4eee-b8eb-2552ad71ee30
keywords:
- ReconnectParentVirtualHardDisk method Hyper-V
- ReconnectParentVirtualHardDisk method Hyper-V , Msvm_ImageManagementService class
- Msvm_ImageManagementService class Hyper-V , ReconnectParentVirtualHardDisk method
topic_type:
- apiref
api_name:
- Msvm_ImageManagementService.ReconnectParentVirtualHardDisk
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

# ReconnectParentVirtualHardDisk method of the Msvm\_ImageManagementService class

Fixes broken links between parent and child disk image files.

## Syntax


```mof
uint32 ReconnectParentVirtualHardDisk(
  [in]  string              ChildPath,
  [in]  string              ParentPath,
  [in]  boolean             Force,
  [out] CIM_ConcreteJob REF Job
);
```



## Parameters

<dl> <dt>

*ChildPath* \[in\]
</dt> <dd>

Type: **string**

A fully qualified path that specifies the location of the child disk image file.

</dd> <dt>

*ParentPath* \[in\]
</dt> <dd>

Type: **string**

A fully qualified path that specifies the location of the parent virtual hard disk file.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Type: **boolean**

This parameter has no effect.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

Type: **CIM\_ConcreteJob**

A reference to the job (can be **NULL** if the task is completed).

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

The following C# example reconnects links between the specified parent and child. The referenced utilities can be found in [Common Utilities for the Virtualization Samples](common-utilities-for-the-virtualization-samples.md).


```CSharp
using System;
using System.Management;
namespace HyperVSamples
{
    class ReconnectVHD
    {
        static void ReconnectParentVirtualHardDisk(string childPath, string parentPath, bool force)
        {
            ManagementScope scope = new ManagementScope(@"root\virtualization", null);
            ManagementObject imageService = Utility.GetServiceObject(scope, "Msvm_ImageManagementService");

            ManagementBaseObject inParams = imageService.GetMethodParameters("ReconnectParentVirtualHardDisk");
            inParams["ParentPath"] = parentPath;
            inParams["ChildPath"] = childPath;
            inParams["Force"] = force;
            ManagementBaseObject outParams = imageService.InvokeMethod("ReconnectParentVirtualHardDisk", inParams, null);
            
            if ((UInt32)outParams["ReturnValue"] == ReturnCode.Completed)
            {
                Console.WriteLine("{0} was reconnected successfully.", inParams["ChildPath"]);
            }
            else
            {
                Console.WriteLine("Unable to reconnect {0}", inParams["ChildPath"]);
            }
            
            inParams.Dispose();
            outParams.Dispose();
            imageService.Dispose();
        }


        static void Main(string[] args)
        {
            if (args != null &amp;&amp; args.Length != 3)
            {
                Console.WriteLine("Usage: ReconnectVHD ChildPath, ParentPath, Force");
                Console.WriteLine("Force: True|False");
                return;
            }
            string childPath = args[0];
            string parentPath = args[1];
            bool force = bool.Parse(args[2]);
            ReconnectParentVirtualHardDisk(childPath, parentPath, force);
        }
    }
}
```



The following VBScript example reconnects links between the specified parent and child.


```VB
option explicit 

dim objWMIService
dim managementService
dim fileSystem

const wmiSuccessful = 0

Main()

'-----------------------------------------------------------------
' Main routine
'-----------------------------------------------------------------
Sub Main()

    dim computer, childPath, parentPath, force, objArgs
    
    set fileSystem = Wscript.CreateObject("Scripting.FileSystemObject")

    computer = "."
    set objWMIService = GetObject("winmgmts:\\" & computer & "\root\virtualization")
    set managementService = objWMIService.ExecQuery("Select * from Msvm_ImageManagementService").ItemIndex(0)

    set objArgs = WScript.Arguments
    if WScript.Arguments.Count = 3 then
        childPath = objArgs.Unnamed.Item(0)
        parentPath = objArgs.Unnamed.Item(1)
        force = objArgs.Unnamed.Item(2)
    else
        WScript.Echo "usage: cscript ReconnectVHD.vbs ChildPath ParentPath Force"
        WScript.Echo "Force: true|false"
        WScript.Quit(1)
    end if

    if ReconnectParentVirtualHardDisk(childPath, parentPath, force) then
        WriteLog "Done"
        WScript.Quit(0)
    else
        WriteLog "ReconnectVHD failed."
        WScript.Quit(1)
    end if

End Sub

'-----------------------------------------------------------------
' Execute ReconnectParentVirtualHardDisk
'-----------------------------------------------------------------
Function ReconnectParentVirtualHardDisk(childPath, parentPath, force)
    WriteLog Format2("Sub ReconnectParentVirtualHardDisk({0}, {1})",  childPath, parentPath)
    
    dim objInParam, objOutParams

    ReconnectParentVirtualHardDisk = false

    set objInParam = managementService.Methods_("ReconnectParentVirtualHardDisk").InParameters.SpawnInstance_()
    objInParam.ChildPath = childPath
    objInParam.ParentPath = parentPath
    objInParam.Force = force

    set objOutParams = managementService.ExecMethod_("ReconnectParentVirtualHardDisk", objInParam)

    if objOutParams.ReturnValue = wmiSuccessful then
        WriteLog Format2("'{0}' was successfully reconnected to the parent '{1}'.", ChildPath, ParentPath)
        ReconnectParentVirtualHardDisk = true
    else
        WriteLog Format1("ReconnectParentVirtualHardDisk operation failed with error {0}", objOutParams.ReturnValue)
    end if

End Function

'-----------------------------------------------------------------
' Create the console log files.
'-----------------------------------------------------------------
Sub WriteLog(line)
    dim fileStream
    set fileStream = fileSystem.OpenTextFile(".\ReconnectVHD.log", 8, true)
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

[**SetParentVirtualHardDisk (V2)**](https://msdn.microsoft.com/library/windows/desktop/hh850298)
</dt> <dt>

[**CIM\_ConcreteJob**](https://msdn.microsoft.com/library/cc136808)
</dt> <dt>

[**Msvm\_ImageManagementService**](msvm-imagemanagementservice.md)
</dt> </dl>

 

 





