---
title: DeleteSwitch method of the Msvm\_VirtualSwitchManagementService class
description: Deletes a virtual switch.
ms.assetid: '1464c2e1-11a0-47fa-b29b-6156e564d8a1'
keywords: ["DeleteSwitch method Hyper-V", "DeleteSwitch method Hyper-V , Msvm_VirtualSwitchManagementService class", "Msvm_VirtualSwitchManagementService class Hyper-V , DeleteSwitch method"]
topic_type:
- apiref
api_name:
- Msvm_VirtualSwitchManagementService.DeleteSwitch
api_location:
- Root\Virtualization
api_type:
- COM
---

# DeleteSwitch method of the Msvm\_VirtualSwitchManagementService class

Deletes a virtual switch.

## Syntax


```mof
uint32 DeleteSwitch(
  [in] Msvm_VirtualSwitch REF VirtualSwitch
);
```



## Parameters

<dl> <dt>

*VirtualSwitch* \[in\]
</dt> <dd>

Type: **Msvm\_VirtualSwitch**

A reference to the switch to be deleted. See [**Msvm\_VirtualSwitch**](msvm-virtualswitch.md).

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

The following C# sample deletes a virtual switch. The referenced utilities can be found in [Common Utilities for the Virtualization Samples](common-utilities-for-the-virtualization-samples.md).


```CSharp
using System;
using System.Management;

namespace HyperVSamples
{
    class DeleteSwitchClass
    {
        static ManagementObject GetVirtualSwitch(string switchName, ManagementScope scope)
        {
            string query = string.Format("select * from Msvm_VirtualSwitch where ElementName = '{0}'", switchName);

            ManagementObjectSearcher searcher = new ManagementObjectSearcher(scope, new ObjectQuery(query));

            ManagementObjectCollection virtualSwitchs = searcher.Get();

            ManagementObject virtualSwitch = null;

            foreach (ManagementObject instance in virtualSwitchs)
            {
                virtualSwitch = instance;
                break;
            }

            searcher.Dispose();
            return virtualSwitch;
        }

        static void DeleteSwitch(string switchFriendlyName)
        {
            ManagementScope scope = new ManagementScope(@"root\virtualization", null);
            ManagementObject switchService = Utility.GetServiceObject(scope, "Msvm_VirtualSwitchManagementService");

            ManagementBaseObject inParams = switchService.GetMethodParameters("DeleteSwitch");

            ManagementObject virtualSwitch = GetVirtualSwitch(switchFriendlyName, scope); 
            inParams["VirtualSwitch"] = virtualSwitch.Path.Path;
            ManagementBaseObject outParams = switchService.InvokeMethod("DeleteSwitch", inParams, null);
            if ((UInt32)outParams["ReturnValue"] == ReturnCode.Completed)
            {
                Console.WriteLine("{0} was deleted successfully", virtualSwitch["Name"]);
            }
            else
            {
                Console.WriteLine("Failed to delete {0} virtual switch. Error {1}.", virtualSwitch["Name"], outParams["ReturnValue"]);
            }
        }

        static void Main(string[] args)
        {
            if (args != null &amp;&amp; args.Length != 3)
            {
                Console.WriteLine("Usage: DeleteSwitch FriendlyName");
                Console.WriteLine("Example: DeleteSwitch \"My First Switch\"");
                return;
            }
            DeleteSwitch(args[0]);
        }
    }
}
```



The following VBScript sample deletes a virtual switch.


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
    dim computer, objArgs, friendlyName, createdSwitch

    set objArgs = WScript.Arguments
    if WScript.Arguments.Count = 1 then
       friendlyName = objArgs.Unnamed.Item(0)
    else
       WScript.Echo "usage: cscript DeleteSwitch FriendlyName"
       WScript.Echo "Example: DeleteSwitch ""My First Switch""" 
       WScript.Quit(1)
    end if     
    
    set fileSystem = Wscript.CreateObject("Scripting.FileSystemObject")
    computer = "."    

    set objWMIService = GetObject("winmgmts:\\" & computer & "\root\virtualization")
    set switchService = objWMIService.ExecQuery("select * from Msvm_VirtualSwitchManagementService").ItemIndex(0)
        
    set createdSwitch = GetVirtualSwitch(friendlyName)
    if Not (createdSwitch Is Nothing) then
        if DeleteSwitch(createdSwitch) then
            WriteLog "Done"
            WScript.Quit(0)
        End if
    else
        WriteLog "DeleteSwitch Failed"
        WScript.Quit(1)
    end if

End Sub

'-----------------------------------------------------------------
' Retrieve VirtualSwitch 
'-----------------------------------------------------------------
Function GetVirtualSwitch(friendlyName)
    dim query
    set GetVirtualSwitch = Nothing
    query = Format1("select * from Msvm_VirtualSwitch where ElementName = '{0}'", friendlyName)
    set GetVirtualSwitch= objWMIService.ExecQuery(query).ItemIndex(0)
End Function

'-----------------------------------------------------------------
' Delete a virtual switch by calling DeleteSwitch WMI method
'-----------------------------------------------------------------
Function DeleteSwitch(virtualSwitch)
    dim objInParam, objOutParams 
    DeleteSwitch = false
    set objInParam = switchService.Methods_("DeleteSwitch").InParameters.SpawnInstance_()
    objInParam.VirtualSwitch = virtualSwitch.Path_.Path

    set objOutParams = switchService.ExecMethod_("DeleteSwitch", objInParam)
    
    if objOutParams.ReturnValue = wmiSuccessful then
        DeleteSwitch = true
    else
        WriteLog Format1("Delete failed with error code {0}", objOutParams.ReturnValue)
    end if

End Function

'-----------------------------------------------------------------
' Create the console log files.
'-----------------------------------------------------------------
Sub WriteLog(line)
    dim fileStream
    set fileStream = fileSystem.OpenTextFile(".\DeleteSwitch.log", 8, true)
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
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012<br/>                                                                       |
| Namespace<br/>                | Root\\Virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**Msvm\_VirtualSwitchManagementService**](msvm-virtualswitchmanagementservice.md)
</dt> </dl>

 

 





