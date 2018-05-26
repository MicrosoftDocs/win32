---
title: DeleteInternalEthernetPort method of the Msvm\_VirtualSwitchManagementService class
description: Deletes an internal Ethernet port.
ms.assetid: a07ea006-0ccd-433c-ae6d-269be48e07c3
keywords:
- DeleteInternalEthernetPort method Hyper-V
- DeleteInternalEthernetPort method Hyper-V , Msvm_VirtualSwitchManagementService class
- Msvm_VirtualSwitchManagementService class Hyper-V , DeleteInternalEthernetPort method
topic_type:
- apiref
api_name:
- Msvm_VirtualSwitchManagementService.DeleteInternalEthernetPort
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

# DeleteInternalEthernetPort method of the Msvm\_VirtualSwitchManagementService class

Deletes an internal Ethernet port.

## Syntax


```mof
uint32 DeleteInternalEthernetPort(
  [in] Msvm_InternalEthernetPort REF InternalEthernetPort
);
```



## Parameters

<dl> <dt>

*InternalEthernetPort* \[in\]
</dt> <dd>

Type: **Msvm\_InternalEthernetPort**

A reference to the internal Ethernet port to be deleted. See [**Msvm\_InternalEthernetPort**](msvm-internalethernetport.md).

</dd> </dl>

## Return value

Type: **uint32**

The method returns 0 if it succeeded synchronously. Any other return value indicates an error.

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

Access to the [**Msvm\_VirtualSwitchManagementService**](msvm-virtualswitchmanagementservice.md) class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Examples

The following C# sample deletes an internal Ethernet port. The referenced utilities can be found in [Common Utilities for the Virtualization Samples](common-utilities-for-the-virtualization-samples.md).


```CSharp
using System;
using System.Management;

namespace HyperVSamples
{
    class DeleteInternalEthernetPortClass
    {
        static void DeleteInternalEthernetPort(string internalPortName)
        {
            ManagementScope scope = new ManagementScope(@"root\virtualization", null);
            ManagementObject switchService = Utility.GetServiceObject(scope, "Msvm_VirtualSwitchManagementService");

            ManagementBaseObject inParams = switchService.GetMethodParameters("DeleteInternalEthernetPort");

            ManagementObject ethernetPort = Utility.GetHostSystemDevice("Msvm_InternalEthernetPort", internalPortName, scope);
            inParams["InternalEthernetPort"] = ethernetPort.Path.Path;

            ManagementBaseObject outParams = switchService.InvokeMethod("DeleteInternalEthernetPort", inParams, null);
            if ((UInt32)outParams["ReturnValue"] == ReturnCode.Completed)
            {
                Console.WriteLine("{0} was deleted successfully", ethernetPort.Path.Path);
            }
            else
            {
                Console.WriteLine("Failed to delete {0} switch.", ethernetPort.Path.Path);
            }
        }

        static void Main(string[] args)
        {
            if (args != null &amp;&amp; args.Length != 1)
            {
                Console.WriteLine("Usage: DeleteInternalEthernetPort FriendlyName");
                Console.WriteLine("Example: DeleteInternalEthernetPort \"First internal Ethernet Port\"");
                return;
            }
            DeleteInternalEthernetPort(args[0]);
        }
    }
}

```



The following VBScript sample deletes an internal Ethernet port.


```VB
option explicit 

dim objWMIService
dim switchService
dim fileSystem

const wmiSuccessful = 0

Main()

'-----------------------------------------------------------------
' Main
'-----------------------------------------------------------------
Sub Main()

    dim computer, internalEthernetPort, friendlyName, objArgs
    set fileSystem = Wscript.CreateObject("Scripting.FileSystemObject")
    computer = "."

    set objWMIService = GetObject("winmgmts:\\" & computer & "\root\virtualization")
    set switchService = objWMIService.ExecQuery("select * from Msvm_VirtualSwitchManagementService").ItemIndex(0)
    
    set objArgs = WScript.Arguments
    if WScript.Arguments.Count = 1 then
       friendlyName = objArgs.Unnamed.Item(0)
    else
       WScript.Echo "usage: cscript DeleteInternalEthernetPort FriendlyName"
       WScript.Echo "Example: DeleteInternalEthernetPort ""First Internal Ethernet Port""" 
       WScript.Quit(1)
    end if    
    
    set internalEthernetPort = GetInternalEthernetPort(friendlyName)
    if Not (createdSwitch Is Nothing) then
        if DeleteInternalEthernetPort(internalEthernetPort) then
            WriteLog "Done"
            WScript.Quit(0)
        end if
    else
        WriteLog "DeleteInternalEthernetPort Failed"
        WScript.Quit(1)
    end if
End Sub

'-----------------------------------------------------------------
' Retrieve internalEthernetPort wmi object
'-----------------------------------------------------------------
Function GetInternalEthernetPort(friendlyName)
    dim query
    set GetInternalEthernetPort = Nothing
    query = Format1("select * from Msvm_InternalEthernetPort where ElementName = '{0}'", friendlyName)
    set GetInternalEthernetPort= objWMIService.ExecQuery(query).ItemIndex(0)
End Function

'-----------------------------------------------------------------
' Delete internal Ethernet port by calling DeleteInternalEthernetPort
'-----------------------------------------------------------------
Function DeleteInternalEthernetPort(internalEthernetPort)
    dim objInParam, objOutParams
    DeleteInternalEthernetPort = false
    set objInParam = switchService.Methods_("DeleteInternalEthernetPort").InParameters.SpawnInstance_()
    objInParam.InternalEthernetPort = internalEthernetPort.Path_.Path

    set objOutParams = switchService.ExecMethod_("DeleteInternalEthernetPort", objInParam)

    if objOutParams.ReturnValue = wmiSuccessful then
        DeleteInternalEthernetPort = true
    else
        WriteLog Format1("DeleteInternalEthernetPort failed with error code {0}", objOutParams.ReturnValue)
    end if

End Function

'-----------------------------------------------------------------
' Create the console log files.
'-----------------------------------------------------------------
Sub WriteLog(line)
    dim fileStream
    set fileStream = fileSystem.OpenTextFile(".\DeleteInternalEthernetPort.log", 8, true)
    WScript.Echo line
    fileStream.WriteLine line
    fileStream.Close

End Sub

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

[**Msvm\_VirtualSwitchManagementService**](msvm-virtualswitchmanagementservice.md)
</dt> </dl>

 

 





