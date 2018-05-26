---
title: Unmount method of the Msvm\_ImageManagementService class
description: Unmounts an existing virtual disk image file in loopback mode.
ms.assetid: 8e633651-7600-4439-9e46-274c94bbb3a3
keywords:
- Unmount method Hyper-V
- Unmount method Hyper-V , Msvm_ImageManagementService class
- Msvm_ImageManagementService class Hyper-V , Unmount method
topic_type:
- apiref
api_name:
- Msvm_ImageManagementService.Unmount
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

# Unmount method of the Msvm\_ImageManagementService class

\[The **Unmount** method is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, use the [**Unmount**](msvm-mountedstorageimage-unmount.md) method of the [**Msvm\_MountedStorageImage**](msvm-mountedstorageimage.md) class.\]

Unmounts an existing virtual disk image file in loopback mode.

## Syntax


```mof
uint32 Unmount(
  [in] string Path
);
```



## Parameters

<dl> <dt>

*Path* \[in\]
</dt> <dd>

Type: **string**

A fully qualified path that specifies the location of the virtual disk image file.

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
<td><dl> <dt><strong>Failed</strong></dt> <dt>32768</dt> </dl></td>

</tr>
<tr class="odd">
<td><dl> <dt><strong>Access Denied</strong></dt> <dt>32769</dt> </dl></td>

</tr>
<tr class="even">
<td><dl> <dt><strong>Not Supported</strong></dt> <dt>32770</dt> </dl></td>

</tr>
<tr class="odd">
<td><dl> <dt><strong>Status is unknown</strong></dt> <dt>32771</dt> </dl></td>

</tr>
<tr class="even">
<td><dl> <dt><strong>Timeout</strong></dt> <dt>32772</dt> </dl></td>

</tr>
<tr class="odd">
<td><dl> <dt><strong>Invalid parameter</strong></dt> <dt>32773</dt> </dl></td>

</tr>
<tr class="even">
<td><dl> <dt><strong>System is in used</strong></dt> <dt>32774</dt> </dl></td>

</tr>
<tr class="odd">
<td><dl> <dt><strong>Invalid state for this operation</strong></dt> <dt>32775</dt> </dl></td>

</tr>
<tr class="even">
<td><dl> <dt><strong>Incorrect data type</strong></dt> <dt>32776</dt> </dl></td>

</tr>
<tr class="odd">
<td><dl> <dt><strong>System is not available</strong></dt> <dt>32777</dt> </dl></td>

</tr>
<tr class="even">
<td><dl> <dt><strong>Out of memory</strong></dt> <dt>32778</dt> </dl></td>

</tr>
<tr class="odd">
<td><dl> <dt><strong>File not found</strong></dt> <dt>32779</dt> </dl></td>
<td><blockquote>
[!Note]<br />
Added in Windows Server 2012 R2.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

## Remarks

Access to the [**Msvm\_ImageManagementService**](msvm-imagemanagementservice.md) class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Examples

The following C# example unmounts a virtual disk image file. The referenced utilities can be found in [Common Utilities for the Virtualization Samples](common-utilities-for-the-virtualization-samples.md).


```CSharp
using System;
using System.Management;

namespace HyperVSamples
{
    class UnmountVHD
    {
        static void Unmount(string vhdPath)
        {
            ManagementScope scope = new ManagementScope(@"root\virtualization", null);
            ManagementObject imageService = Utility.GetServiceObject(scope, "Msvm_ImageManagementService");

            ManagementBaseObject inParams = imageService.GetMethodParameters("Unmount");
            inParams["Path"] = vhdPath;
            ManagementBaseObject outParams = imageService.InvokeMethod("Unmount", inParams, null);
            if ((UInt32)outParams["ReturnValue"] == ReturnCode.Completed)
            {
                Console.WriteLine("{0} was unmounted successfully.", inParams["Path"]);
            }
            else
            {
                Console.WriteLine("Unmount operation for {0} failed with error {1}.", vhdPath, outParams["ReturnValue"]);
            }

            inParams.Dispose();
            outParams.Dispose();
            imageService.Dispose();
        }

        static void Main(string[] args)
        {
            if (args != null &amp;&amp; args.Length != 1)
            {
                Console.WriteLine("Usage: UnmountVHD vhdPath");
                return;
            }
            Unmount(args[0]);
        }
    }
}
```



The following VBScript example unmounts a virtual disk image file.


```VB
option explicit 

dim objWMIService
dim vhdPath
dim managementService
dim fileSystem

const wmiCompleted = 0

Main()

'-----------------------------------------------------------------
' Main
'-----------------------------------------------------------------
Sub Main()

    dim objArgs, computer
    set fileSystem = Wscript.CreateObject("Scripting.FileSystemObject")

    computer = "."
    set objWMIService = GetObject("winmgmts:\\" & computer & "\root\virtualization")
    set managementService = objWMIService.ExecQuery("Select * from Msvm_ImageManagementService").ItemIndex(0)

    set objArgs = WScript.Arguments
    if WScript.Arguments.Count = 1 then
        vhdPath = objArgs.Unnamed.Item(0)
    else
        WScript.Echo "usage: cscript unmountVHD.vbs vhdPath"
        WScript.Quit(1)
    end if


    if ExecuteUnmountVHD then
        WriteLog "Done"
        WScript.Quit(0)
    else
        WriteLog "Unmount operation failed."
        WScript.Quit(1)
    end if

End Sub

'-----------------------------------------------------------------
' ExecuteUnmountVHD
'-----------------------------------------------------------------
Function ExecuteUnmountVHD ()

    WriteLog Format1("Sub ExecuteUnmountVHD ({0})",  vhdPath)
    
    dim objInParam, objOutParams

    ExecuteUnmountVHD = false

    set objInParam = managementService.Methods_("Unmount").InParameters.SpawnInstance_()
    objInParam.Path = vhdPath

    set objOutParams = managementService.ExecMethod_("Unmount", objInParam)

    if  objOutParams.ReturnValue = wmiCompleted then
        ExecuteUnmountVHD = true
        WriteLog Format1("{0} was unmounted successfully.", vhdPath)
    else
        WriteLog Format2("Unmount operation for {0} failed with error {1}", vhdPath, objOutParams.ReturnValue)
    end if
    
End Function

'-----------------------------------------------------------------
' Create the console log files.
'-----------------------------------------------------------------
Sub WriteLog(line)
    dim fileStream
    set fileStream = fileSystem.OpenTextFile(".\UnmountVHD.log", 8, true)
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

[**DetachVirtualHardDisk (V2)**](https://msdn.microsoft.com/library/windows/desktop/hh850046)
</dt> <dt>

[**Msvm\_ImageManagementService**](msvm-imagemanagementservice.md)
</dt> </dl>

 

 





