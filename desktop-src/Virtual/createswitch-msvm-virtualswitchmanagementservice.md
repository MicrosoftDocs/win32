---
title: CreateSwitch method of the Msvm\_VirtualSwitchManagementService class
description: Creates a new virtual switch.
ms.assetid: 12bd0baa-5ac0-4ce1-8582-0c572849b98a
keywords:
- CreateSwitch method Hyper-V
- CreateSwitch method Hyper-V , Msvm_VirtualSwitchManagementService class
- Msvm_VirtualSwitchManagementService class Hyper-V , CreateSwitch method
topic_type:
- apiref
api_name:
- Msvm_VirtualSwitchManagementService.CreateSwitch
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

# CreateSwitch method of the Msvm\_VirtualSwitchManagementService class

Creates a new virtual switch.

## Syntax


```mof
uint32 CreateSwitch(
  [in]  string                 Name,
  [in]  string                 FriendlyName,
  [in]  uint32                 NumLearnableAddresses,
  [in]  string                 ScopeOfResidence,
  [out] Msvm_VirtualSwitch REF CreatedVirtualSwitch
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

Type: **string**

The name of the switch. This name must be unique to all virtual switches in the system.

</dd> <dt>

*FriendlyName* \[in\]
</dt> <dd>

Type: **string**

A user-readable name for the switch.

</dd> <dt>

*NumLearnableAddresses* \[in\]
</dt> <dd>

Type: **uint32**

The maximum number of MAC addresses that can be learned by the switch.

</dd> <dt>

*ScopeOfResidence* \[in\]
</dt> <dd>

Type: **string**

The initial scope of the switch.

</dd> <dt>

*CreatedVirtualSwitch* \[out\]
</dt> <dd>

Type: **Msvm\_VirtualSwitch**

Upon successful completion of this method, this parameter contains the created switch. See [**Msvm\_VirtualSwitch**](msvm-virtualswitch.md).

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

The following C# sample creates a virtual switch. The referenced utilities can be found in [Common Utilities for the Virtualization Samples](common-utilities-for-the-virtualization-samples.md).


```CSharp
using System;
using System.Management;

namespace HyperVSamples
{
    class CreateSwitchClass
    {
        static ManagementObject CreateSwitch(string name, string friendlyName, int learnableAddress)
        {
            ManagementScope scope = new ManagementScope(@"root\virtualization", null);
            ManagementObject switchService = Utility.GetServiceObject(scope, "Msvm_VirtualSwitchManagementService");

            ManagementObject createdSwitch = null;

            ManagementBaseObject inParams = switchService.GetMethodParameters("CreateSwitch");
            inParams["FriendlyName"] = friendlyName;
            inParams["Name"] = name;
            inParams["NumLearnableAddresses"] = learnableAddress;
            inParams["ScopeofResidence"] = null;
            ManagementBaseObject outParams = switchService.InvokeMethod("CreateSwitch", inParams, null);
            if ((UInt32)outParams["ReturnValue"] == ReturnCode.Completed)
            {
                Console.WriteLine("{0} was created successfully", inParams["Name"]);
                createdSwitch = new ManagementObject(outParams["CreatedVirtualSwitch"].ToString());
            }
            else
            {
                Console.WriteLine("Failed to create {0} switch.", inParams["Name"]);
            }
            return createdSwitch;
        }

        static void Main(string[] args)
        {
            if (args != null &amp;&amp; args.Length != 3)
            {
                Console.WriteLine("Usage: CreateSwitch name friendlyName NumLearnableAddresses");
                Console.WriteLine("Example: CreateSwitch FirstSwitch \"My First Switch\" 1024");
                return;
            }
            CreateSwitch(args[0], args[1], int.Parse(args[2]));
        }
    }
}
```



The following VBScript sample creates a virtual switch.


```VB
option explicit 

dim objWMIService
dim switchService
dim fileSystem

const wmiStarted = 4096
const wmiSuccessful = 0

Main()

'-----------------------------------------------------------------
' Main
'-----------------------------------------------------------------
Sub Main()

    dim name, friendlyName, learnableAddress
    dim computer, objArgs, createdSwitch

    set objArgs = WScript.Arguments
    if WScript.Arguments.Count = 3 then
       name = objArgs.Unnamed.Item(0)
       friendlyName = objArgs.Unnamed.Item(1)
       learnableAddress = objArgs.Unnamed.Item(2)
    else
       WScript.Echo "usage: cscript CreateSwitch.vbs name friendlyName learnableAddress"
       WScript.Echo "Example: CreateSwitch FirstSwitch ""My First Switch"" 1024"
       WScript.Quit(1)
    end if
    
    set fileSystem = Wscript.CreateObject("Scripting.FileSystemObject")
    computer = "."

    set objWMIService = GetObject("winmgmts:\\" & computer & "\root\virtualization")
    set switchService = objWMIService.ExecQuery("select * from Msvm_VirtualSwitchManagementService").ItemIndex(0)
        
    set createdSwitch = CreateSwitch(name, friendlyName, learnableAddress)
    
    if createdSwitch Is Nothing then
        WriteLog "CreateSwitch failed."
        WScript.Quit(1)
    else
        WriteLog "Done"
        WScript.Quit(0)
    end if

End Sub

'-----------------------------------------------------------------
' Create a virtual switch by calling CreateSwitch WMI method
'-----------------------------------------------------------------
Function CreateSwitch(name, friendlyName, learnableAddress)

    dim objInParam, objOutParams
    
    set CreateSwitch = Nothing
    set objInParam = switchService.Methods_("CreateSwitch").InParameters.SpawnInstance_()
    objInParam.FriendlyName = friendlyName
    objInParam.Name = name
    objInParam.NumLearnableAddresses = learnableAddress
    objInParam.ScopeofResidence = null

    set objOutParams = switchService.ExecMethod_("CreateSwitch", objInParam)
    
    if objOutParams.ReturnValue = wmiSuccessful then
        set CreateSwitch = objWMIService.Get(objOutParams.CreatedVirtualSwitch)
    else
        WriteLog Format1("CreateSwitch failed with error code {0}", objOutParams.ReturnValue)
    end if

End Function

'-----------------------------------------------------------------
' Create the console log files.
'-----------------------------------------------------------------
Sub WriteLog(line)
    dim fileStream
    set fileStream = fileSystem.OpenTextFile(".\CreateSwitch.log", 8, true)
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
</dt> <dt>

[**Msvm\_VirtualSwitch**](msvm-virtualswitch.md)
</dt> </dl>

 

 





