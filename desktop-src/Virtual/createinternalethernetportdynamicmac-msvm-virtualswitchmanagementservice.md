---
title: CreateInternalEthernetPortDynamicMac method of the Msvm\_VirtualSwitchManagementService class
description: Creates a new internal Ethernet port. Its almost the same as CreateInternalEthernetPort expect for the new internal Ethernet ports MAC address is created dynamically instead of being passed as a parameter.
ms.assetid: afe5b876-5b88-4bdc-b197-c0dce6d6cbbf
keywords:
- CreateInternalEthernetPortDynamicMac method Hyper-V
- CreateInternalEthernetPortDynamicMac method Hyper-V , Msvm_VirtualSwitchManagementService class
- Msvm_VirtualSwitchManagementService class Hyper-V , CreateInternalEthernetPortDynamicMac method
topic_type:
- apiref
api_name:
- Msvm_VirtualSwitchManagementService.CreateInternalEthernetPortDynamicMac
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

# CreateInternalEthernetPortDynamicMac method of the Msvm\_VirtualSwitchManagementService class

Creates a new internal Ethernet port. It's almost the same as [**CreateInternalEthernetPort**](createinternalethernetport-msvm-virtualswitchmanagementservice.md) expect for the new internal Ethernet port's MAC address is created dynamically instead of being passed as a parameter.

## Syntax


```mof
uint32 CreateInternalEthernetPortDynamicMac(
  [in]  string                        Name,
  [in]  string                        FriendlyName,
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

*CreatedInternalEthernetPort* \[out\]
</dt> <dd>

Type: **Msvm\_InternalEthernetPort**

Upon successful completion of this method, this parameter contains the created switch port. See [**Msvm\_InternalEthernetPort**](msvm-internalethernetport.md).

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

The following C# sample creates an internal Ethernet port with a dynamic MAC address. The referenced utilities can be found in [Common Utilities for the Virtualization Samples](common-utilities-for-the-virtualization-samples.md).


```CSharp
using System;
using System.Management;

namespace HyperVSamples
{
    class CreateInternalEthernetPortDynamicMacClass
    {
        static ManagementObject CreateInternalEthernetPortDynamicMac(string friendlyName, string name)
        {
            ManagementScope scope = new ManagementScope(@"root\virtualization", null);
            ManagementObject switchService = Utility.GetServiceObject(scope, "Msvm_VirtualSwitchManagementService");

            ManagementObject createdInternalEthernetPort = null;

            ManagementBaseObject inParams = switchService.GetMethodParameters("CreateInternalEthernetPortDynamicMac");
            inParams["FriendlyName"] = friendlyName;
            inParams["Name"] = name;
            ManagementBaseObject outParams = switchService.InvokeMethod("CreateInternalEthernetPortDynamicMac", inParams, null);
            if ((UInt32)outParams["ReturnValue"] == ReturnCode.Completed)
            {
                createdInternalEthernetPort = new ManagementObject(outParams["CreateInternalEthernetPortDynamicMac"].ToString());
                Console.WriteLine("{0} was created successfully", inParams["Name"]);
            }
            else
            {
                Console.WriteLine("Failed to create {0} switch.", inParams["Name"]);
            }
            return createdInternalEthernetPort;
        }

        static void Main(string[] args)
        {
            if (args != null &amp;&amp; args.Length != 2)
            {
                Console.WriteLine("Usage: CreateInternalEthernetPortDynamicMac FriendlyName Name");
                Console.WriteLine("Example: CreateInternalEthernetPort \"{0}\" {1}",
                    "First internal Ethernet Port",
                    "FirstInternalEthernetPort");
                return;
            }
            CreateInternalEthernetPortDynamicMac(args[0], args[1]);
        }
    }
}
```



The following VBScript sample creates an internal Ethernet port with a dynamic MAC address.


```VB
dim objWMIService
dim switchService
dim fileSystem

const wmiSuccessful = 0

Main()

'-----------------------------------------------------------------
' Main
'-----------------------------------------------------------------
Sub Main()
    set fileSystem = Wscript.CreateObject("Scripting.FileSystemObject")
    strComputer = "."

    set objWMIService = GetObject("winmgmts:\\" & strComputer & "\root\virtualization")
    GetVirtualSwitchManagementServiceInstance
    set createdInternalEthernetPort = CreateInternalEthernetPortDynamicMac
    if Not (createdInternalEthernetPort Is Nothing) then
        WriteLog "Done"
        WScript.Quit(0)
    else
        WriteLog Format1("Err.Number: {0}", Err.Number)
        WriteLog Format1("Err.Description:{0}",Err.Description)
        WScript.Quit(1)
    end if
End Sub

'-----------------------------------------------------------------
' Retrieve GetVirtualSwitchManagementServiceInstance from WMI
'-----------------------------------------------------------------
Sub GetVirtualSwitchManagementServiceInstance()

    query = "select * from Msvm_VirtualSwitchManagementService"
    set managementServiceCol= objWMIService.ExecQuery(query)
    For Each instance in managementServiceCol
        set switchService = instance
    Next

End Sub


'-----------------------------------------------------------------
' Create a virtual switch by calling CreateSwitch WMI method
'-----------------------------------------------------------------
Function CreateInternalEthernetPortDynamicMac()
    set CreateInternalEthernetPortDynamicMac = Nothing
    set objInParam = switchService.Methods_("CreateInternalEthernetPortDynamicMac").InParameters.SpawnInstance_()
    objInParam.FriendlyName = "First Internal Ethernet Dynamic Mac Port"
    objInParam.Name = "FirstInternalDynamicMacPort"

    set objOutParams = switchService.ExecMethod_("CreateInternalEthernetPortDynamicMac", objInParam)

    if objOutParams.ReturnValue = wmiSuccessful then
        set CreateInternalEthernetPortDynamicMac = objWMIService.Get(objOutParams.CreatedInternalEthernetPort)
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

 

 





