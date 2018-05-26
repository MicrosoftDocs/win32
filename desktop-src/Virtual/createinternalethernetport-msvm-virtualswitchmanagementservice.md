---
title: CreateInternalEthernetPort method of the Msvm\_VirtualSwitchManagementService class
description: Creates an internal Ethernet port.
ms.assetid: e65e09d5-5767-4645-8602-2e98f9df0b44
keywords:
- CreateInternalEthernetPort method Hyper-V
- CreateInternalEthernetPort method Hyper-V , Msvm_VirtualSwitchManagementService class
- Msvm_VirtualSwitchManagementService class Hyper-V , CreateInternalEthernetPort method
topic_type:
- apiref
api_name:
- Msvm_VirtualSwitchManagementService.CreateInternalEthernetPort
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

# CreateInternalEthernetPort method of the Msvm\_VirtualSwitchManagementService class

Creates an internal Ethernet port.

## Syntax


```mof
uint32 CreateInternalEthernetPort(
  [in]  string                        Name,
  [in]  string                        FriendlyName,
  [in]  string                        MacAddress,
  [out] Msvm_InternalEthernetPort REF CreatedInternalEthernetPort
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

Type: **string**

The name of the port. This name must be unique.

</dd> <dt>

*FriendlyName* \[in\]
</dt> <dd>

Type: **string**

A user-readable name for the port.

</dd> <dt>

*MacAddress* \[in\]
</dt> <dd>

Type: **string**

The mac address to be assigned to the Ethernet port.

</dd> <dt>

*CreatedInternalEthernetPort* \[out\]
</dt> <dd>

Type: **Msvm\_InternalEthernetPort**

Upon successful completion of this method, this parameter contains the created internal Ethernet port. See [**Msvm\_InternalEthernetPort**](msvm-internalethernetport.md).

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

The following C# sample creates an internal Ethernet port. The referenced utilities can be found in [Common Utilities for the Virtualization Samples](common-utilities-for-the-virtualization-samples.md).


```CSharp
using System;
using System.Management;

namespace HyperVSamples
{
    class CreateInternalEthernetPortClass
    {
        static ManagementObject CreateInternalEthernetPort(string name, string friendlyName, string MACAddress)
        {
            ManagementScope scope = new ManagementScope(@"root\virtualization", null);
            ManagementObject switchService = Utility.GetServiceObject(scope, "Msvm_VirtualSwitchManagementService");

            ManagementObject createdInternalEthernetPort = null;

            ManagementBaseObject inParams = switchService.GetMethodParameters("CreateInternalEthernetPort");
            inParams["FriendlyName"] = friendlyName;
            inParams["Name"] = name;
            inParams["MACAddress"] = MACAddress;
            ManagementBaseObject outParams = switchService.InvokeMethod("CreateInternalEthernetPort", inParams, null);
            if ((UInt32)outParams["ReturnValue"] == ReturnCode.Completed)
            {
                createdInternalEthernetPort = new ManagementObject(outParams["CreatedInternalEthernetPort"].ToString());
                Console.WriteLine("{0} was created successfully", inParams["Name"]);
            }
            else
            {
                Console.WriteLine("Failed to create {0} internal Ethernet port.", inParams["Name"]);
            }
            return createdInternalEthernetPort;
        }

        static void Main(string[] args)
        {
            if (args != null &amp;&amp; args.Length != 3)
            {
                Console.WriteLine("Usage: CreateInternalEthernetPort Name FriendlyName MACAddress");
                Console.WriteLine("Example: CreateInternalEthernetPort {0} \"{1}\" {2}",
                    "FirstInternalEthernetPort",
                    "First Internal Ethernet Port",
                    "0003FF123456");
                return;
            }
            CreateInternalEthernetPort(args[0], args[1], args[2]);
        }
    }
}
```



The following VBScript sample creates an internal Ethernet port.


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

    dim computer, objArgs
    dim name, friendlyName, MACAddress, createdInternalEthernetPort
    
    set fileSystem = Wscript.CreateObject("Scripting.FileSystemObject")
    computer = "."

    set objWMIService = GetObject("winmgmts:\\" & computer & "\root\virtualization")
    set switchService = objWMIService.ExecQuery("select * from Msvm_VirtualSwitchManagementService").ItemIndex(0)
    
    set objArgs = WScript.Arguments
    if WScript.Arguments.Count = 3 then
       name = objArgs.Unnamed.Item(0)
       friendlyName = objArgs.Unnamed.Item(1)
       MACAddress = objArgs.Unnamed.Item(2)
    else
       WScript.Echo "usage: cscript CreateSwitchPort Name FriendlyName MACAddress"
       WScript.Echo "Example: CreateSwitchPort FirstInternalEthernetPort ""First Internal Ethernet Port"" 0003FF123456" 
       WScript.Quit(1)
    end if
        
    set createdInternalEthernetPort = CreateInternalEthernetPort(name, friendlyName, MACAddress)
    if Not (createdInternalEthernetPort Is Nothing) then
        WriteLog "Done"
        WScript.Quit(0)
    else
        WriteLog "CreateInternalEthernetPort Failed"
        WScript.Quit(1)
    end if
End Sub

'-----------------------------------------------------------------
' Create an Internal Ethernet port by calling CreateSwitch WMI method
'-----------------------------------------------------------------
Function CreateInternalEthernetPort(name, friendlyName, MACAddress)
    dim objInParam, objOutParams
    set CreateInternalEthernetPort = Nothing
    set objInParam = switchService.Methods_("CreateInternalEthernetPort").InParameters.SpawnInstance_()
    objInParam.FriendlyName = friendlyName
    objInParam.Name = name
    objInParam.MACAddress = MACAddress

    set objOutParams = switchService.ExecMethod_("CreateInternalEthernetPort", objInParam)

    if objOutParams.ReturnValue = wmiSuccessful then
        set CreateInternalEthernetPort = objWMIService.Get(objOutParams.CreatedInternalEthernetPort)
    else
        WriteLog Format1("CreateInternalEthernetPort failed with error code {0}", objOutParams.ReturnValue)
    end if

End Function

'-----------------------------------------------------------------
' Create the console log files.
'-----------------------------------------------------------------
Sub WriteLog(line)
    dim fileStream
    set fileStream = fileSystem.OpenTextFile(".\CreateSwitchPort.log", 8, true)
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

 

 





