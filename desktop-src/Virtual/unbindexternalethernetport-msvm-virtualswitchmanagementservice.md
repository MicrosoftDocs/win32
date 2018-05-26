---
title: UnbindExternalEthernetPort method of the Msvm\_VirtualSwitchManagementService class
description: Unbinds an external Ethernet port to the Microsoft Windows Virtualization network subsystem.
ms.assetid: fa81e80e-060b-41a8-bc0c-95e165b44cef
keywords:
- UnbindExternalEthernetPort method Hyper-V
- UnbindExternalEthernetPort method Hyper-V , Msvm_VirtualSwitchManagementService class
- Msvm_VirtualSwitchManagementService class Hyper-V , UnbindExternalEthernetPort method
topic_type:
- apiref
api_name:
- Msvm_VirtualSwitchManagementService.UnbindExternalEthernetPort
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

# UnbindExternalEthernetPort method of the Msvm\_VirtualSwitchManagementService class

Unbinds an external Ethernet port to the Microsoft Windows Virtualization network subsystem. After this call is made, virtual machines cannot use the external Ethernet port to send data out over the physical network.

## Syntax


```mof
uint32 UnbindExternalEthernetPort(
  [in] Msvm_ExternalEthernetPort REF ExternalEthernetPort
);
```



## Parameters

<dl> <dt>

*ExternalEthernetPort* \[in\]
</dt> <dd>

Type: **Msvm\_ExternalEthernetPort**

A reference to the external Ethernet port to be unbound. See [**Msvm\_ExternalEthernetPort**](msvm-externalethernetport.md).

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

The following C# sample unbinds an external Ethernet port. The referenced utilities can be found in [Common Utilities for the Virtualization Samples](common-utilities-for-the-virtualization-samples.md).


```CSharp
using System;
using System.Management;

namespace HyperVSamples
{
    class UnbindExternalEthernetPortClass
    {
        static ManagementObject GetExternalEthernetPort(ManagementScope scope, string externalEthernetPortFriendlyName)
        {
            ManagementObject externalEthernetPort = null;
            string hostName = System.Environment.MachineName;

            ManagementObject computerSystem = Utility.GetTargetComputer(hostName, scope);

            //get external port
            ManagementObjectCollection externalPorts = computerSystem.GetRelated("msvm_ExternalEthernetPort");
            foreach (ManagementObject port in externalPorts)
            {
                if (port["ElementName"].ToString().ToLower() == externalEthernetPortFriendlyName.ToLower())
                {
                    externalEthernetPort = port;
                    break;
                }
            }

            return externalEthernetPort;
        }

        static void UnbindExternalEthernetPort(string externalEthernetPortFriendlyName)
        {
            ManagementScope scope = new ManagementScope(@"root\virtualization", null);
            ManagementObject switchService = Utility.GetServiceObject(scope, "Msvm_VirtualSwitchManagementService");

            ManagementObject externalEthernetPort = GetExternalEthernetPort(scope, externalEthernetPortFriendlyName);
            ManagementBaseObject inParams = switchService.GetMethodParameters("UnbindExternalEthernetPort");
            inParams["ExternalEthernetPort"] = externalEthernetPort.Path.Path;
            ManagementBaseObject outParams = switchService.InvokeMethod("UnbindExternalEthernetPort", inParams, null);
            if ((UInt32)outParams["ReturnValue"] == ReturnCode.Completed)
            {
                Console.WriteLine("{0} is unbound successfully", externalEthernetPort["Name"]);
            }
            else
            {
                Console.WriteLine("Failed to unbind {0} external Ethernet port.", externalEthernetPort["Name"]);
            }
        }

        static void main(string[] args)
        {
            if (args != null &amp;&amp; args.Length != 1)
            {
                Console.WriteLine("Usage:\nUnbindExternalEthernetPort ExternalEthernetPortFriendlyName");
                Console.WriteLine("Example:\nUnbindExternalEthernetPort \"Intel(R) PRO/1000 PM Network Connection\"");
                return;
            }

            UnbindExternalEthernetPort(args[0]);
        }

    }
}
```



The following VBScript sample unbinds an external Ethernet port.


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
    dim computer, objArgs, externalEthernetPort, friendlyName

    set objArgs = WScript.Arguments
    if WScript.Arguments.Count = 1 then
       friendlyName = objArgs.Unnamed.Item(0)
    else
       WScript.Echo "usage: cscript UnbindExternalEthernetPort ExternalEthernetPortFriendlyName"
       WScript.Echo "Example: UnbindExternalEthernetPort ""Intel(R) PRO/1000 PM Network Connection""" 
       WScript.Quit(1)
    end if     
    
    set fileSystem = Wscript.CreateObject("Scripting.FileSystemObject")
    computer = "." 
    
    set objWMIService = GetObject("winmgmts:\\" & computer & "\root\virtualization")
    set switchService = objWMIService.ExecQuery("select * from Msvm_VirtualSwitchManagementService").ItemIndex(0)
    
    
    set externalEthernetPort = GetExternalEthernetPort(friendlyName)
    
    if (externalEthernetPort Is Nothing) then
       WriteLog Format1("Unable to find external Ethernet Port {0}", friendlyName)
       WScript.Quit(1)
    end if

    if BindExternalEthernetPort(externalEthernetPort) then
        WriteLog "Done"
        WScript.Quit(0)
    else
        WriteLog("BindExternalEthernetPort failed")
        WScript.Quit(1)
    end if
End Sub


'-----------------------------------------------------------------
' Retrieve the external Ethernet port 
'-----------------------------------------------------------------
Function GetExternalEthernetPort(externalEthernetPortFriendlyName)
    
    dim objNTInfo, computerName, query, computer
    dim externalEthernetPort, externalEthernetPorts
    
    set GetExternalEthernetPort = Nothing
    set objNTInfo = CreateObject("WinNTSystemInfo")
    computerName = lcase(objNTInfo.ComputerName)

    query = Format1("select * from Msvm_ComputerSystem where Name = '{0}'", computerName)
    set computer = objWMIService.ExecQuery(query).ItemIndex(0)
    
    query = Format1("ASSOCIATORS OF {{0}} WHERE resultClass = Msvm_ExternalEthernetPort", computer.Path_.Path)
    set externalEthernetPorts = objWMIService.ExecQuery(query)
    for each externalEthernetPort in externalEthernetPorts
        if lcase(externalEthernetPort.ElementName) = lcase(externalEthernetPortFriendlyName) then
            set GetExternalEthernetPort = externalEthernetPort
            Exit Function
        end if
    next

End Function

'-----------------------------------------------------------------
' Unbind the External Ethernet Port by calling UnbindExternalEthernetPort
'-----------------------------------------------------------------
Function UnbindExternalEthernetPort(externalEthernetPort)
    dim objInParam, objOutParams
    
    UnbindExternalEthernetPort = false
    set objInParam = switchService.Methods_("UnbindExternalEthernetPort").InParameters.SpawnInstance_()
    objInParam.ExternalEthernetPort = externalEthernetPort.Path_.Path

    set objOutParams = switchService.ExecMethod_("UnbindExternalEthernetPort", objInParam)

    if objOutParams.ReturnValue = wmiSuccessful then
        UnbindExternalEthernetPort = true
    else
        WriteLog Format1("UnbindExternalEthernetPort failed with error code {0}", objOutParams.ReturnValue)
    end if

End Function

'-----------------------------------------------------------------
' Create the console log files.
'-----------------------------------------------------------------
Sub WriteLog(line)
    dim fileStream
    set fileStream = fileSystem.OpenTextFile(".\UnbindExternalEthernetPort.log", 8, true)
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

 

 





