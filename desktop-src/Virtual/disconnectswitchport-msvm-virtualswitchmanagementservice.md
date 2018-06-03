---
title: DisconnectSwitchPort method of the Msvm\_VirtualSwitchManagementService class
description: Disconnects a virtual switch port.
ms.assetid: 1a13e3fe-e7ea-4fea-a73d-f9f2bd022229
keywords:
- DisconnectSwitchPort method Hyper-V
- DisconnectSwitchPort method Hyper-V , Msvm_VirtualSwitchManagementService class
- Msvm_VirtualSwitchManagementService class Hyper-V , DisconnectSwitchPort method
topic_type:
- apiref
api_name:
- Msvm_VirtualSwitchManagementService.DisconnectSwitchPort
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

# DisconnectSwitchPort method of the Msvm\_VirtualSwitchManagementService class

Disconnects a virtual switch port.

## Syntax


```mof
uint32 DisconnectSwitchPort(
  [in] Msvm_SwitchPort REF SwitchPort
);
```



## Parameters

<dl> <dt>

*SwitchPort* \[in\]
</dt> <dd>

Type: **Msvm\_SwitchPort**

The switch port to be disconnected. See [**Msvm\_SwitchPort**](msvm-switchport.md).

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

The following C# sample disconnects a switch port. The referenced utilities can be found in [Common Utilities for the Virtualization Samples](common-utilities-for-the-virtualization-samples.md).


```CSharp
using System;
using System.Management;

namespace HyperVSamples
{
    class DisconnectSwitchPortClass
    {
        ManagementScope scope = null;
        ManagementObject switchService = null;

        DisconnectSwitchPortClass()
        {
            scope = new ManagementScope(@"root\virtualization", null);
            switchService = Utility.GetServiceObject(scope, "Msvm_VirtualSwitchManagementService");
        }


        ManagementObject GetVirtualSwitch(string switchName)
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


        ManagementObject GetVirtualSwitchPort(ManagementObject virtualSwitch, string switchPortName)
        {
            ManagementObjectCollection switchPorts = virtualSwitch.GetRelated
             (
                 "Msvm_SwitchPort",
                 "Msvm_HostedAccessPoint",
                 null,
                 null,
                 "Dependent",
                 "Antecedent",
                 false,
                 null
             );

            ManagementObject switchPort = null;

            foreach (ManagementObject instance in switchPorts)
            {
                if (instance["ElementName"].ToString().ToLower() == switchPortName.ToLower())
                {
                    switchPort = instance;
                    break;
                }
            }

            return switchPort;
        }

        void DisconnectSwitchPort(ManagementObject switchPort)
        {

            ManagementBaseObject inParams = switchService.GetMethodParameters("DisconnectSwitchPort");

            inParams["SwitchPort"] = switchPort.Path.Path;
            ManagementBaseObject outParams = switchService.InvokeMethod("DisconnectSwitchPort", inParams, null);
            if ((UInt32)outParams["ReturnValue"] == ReturnCode.Completed)
            {
                Console.WriteLine("{0} was disconnected successfully", switchPort.Path.Path);
            }
            else
            {
                Console.WriteLine("Failed to disconnect {0} switch port.", switchPort.Path.Path);
            }
            inParams.Dispose();
            outParams.Dispose();
        }

        void Close()
        {
            this.switchService.Dispose();
        }

        static void Main(string[] args)
        {
            if (args != null &amp;&amp; args.Length != 2)
            {
                Console.WriteLine("DisconnectSwitchPort switchFriendlyName switchPortFriendlyName");
                Console.WriteLine("Example: DisconnectSwitchPort MyFirstSwitch \"My Switch Port\"");
                return;
            }

            DisconnectSwitchPortClass disconnectSwitchPort = new DisconnectSwitchPortClass();
            ManagementObject virtualSwitch = disconnectSwitchPort.GetVirtualSwitch(args[0]);
            ManagementObject virtualSwitchPort = disconnectSwitchPort.GetVirtualSwitchPort(virtualSwitch, args[1]);
            disconnectSwitchPort.DisconnectSwitchPort(virtualSwitchPort);
            virtualSwitch.Dispose();
            virtualSwitchPort.Dispose();
            disconnectSwitchPort.Close();
        }
    }
}
```



The following VBScript sample disconnects a switch port.


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
    dim computer, objArgs, friendlyName
    dim switchFriendlyName, switchPortFriendlyName
    dim switch, switchPort

    set objArgs = WScript.Arguments
    if WScript.Arguments.Count = 2 then
       switchFriendlyName = objArgs.Unnamed.Item(0)
       switchPortFriendlyName = objArgs.Unnamed.Item(1)
    else
       WScript.Echo "usage: cscript DisconnectSwitchPort SwitchFriendlyName SwitchPortFriendlyName"
       WScript.Echo "Example: DisconnectSwitchPort ""My First Switch"" ""First VirtualSwitch Port""" 
       WScript.Quit(1)
    end if     
    
    set fileSystem = Wscript.CreateObject("Scripting.FileSystemObject")
    computer = "."    

    set objWMIService = GetObject("winmgmts:\\" & computer & "\root\virtualization")
    set switchService = objWMIService.ExecQuery("select * from Msvm_VirtualSwitchManagementService").ItemIndex(0)

    set switch = GetVirtualSwitch(switchFriendlyName)
    
    if (switch Is Nothing) then
        WriteLog Format1("Unable to find switch '{0}'.", switchFriendlyName)
        WScript.Quit(1)   
    end if
    
    set switchPort = GetVirtualSwitchPort(switch, switchPortFriendlyName)

    if (switchPort Is Nothing) then
        WriteLog Format1("Unable to find switchPort '{0}'.", switchPortFriendlyName)
        WScript.Quit(1)   
    end if    
    
    if DisconnectSwitchPort(switchPort) then
        WriteLog "Done"
        WScript.Quit(0)
    else
        WriteLog "DisconnectSwitchPort failed"
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
' Retrieve VirtualSwitchPort
'-----------------------------------------------------------------
Function GetVirtualSwitchPort(switch, switchPortFriendlyName)
    dim query, switchPort, switchPorts
    set GetVirtualSwitchPort = Nothing
    query = Format1("ASSOCIATORS OF {{0}} WHERE resultClass = Msvm_SwitchPort", switch.Path_.Path)
    set switchPorts= objWMIService.ExecQuery(query)
    for each switchPort in switchPorts
        if lcase(switchPort.ElementName) = lcase(switchPortFriendlyName) then
            set GetVirtualSwitchPort = switchPort
        end if
    next
End Function

'-----------------------------------------------------------------
' Disconnect a virtual switch by calling DisconnectSwitchPort WMI method
'-----------------------------------------------------------------
Function DisconnectSwitchPort(virtualSwitchPort)
    dim objInParam, objOutParams
    
    DisconnectSwitchPort = false
    set objInParam = switchService.Methods_("DisconnectSwitchPort").InParameters.SpawnInstance_()
    objInParam.SwitchPort = virtualSwitchPort.Path_.Path

    set objOutParams = switchService.ExecMethod_("DisconnectSwitchPort", objInParam)

    if objOutParams.ReturnValue = wmiSuccessful then
        DisconnectSwitchPort = true
    else
        WriteLog Format1("DisconnectSwitchPort failed with error code {0}", objOutParams.ReturnValue)
    end if

End Function

'-----------------------------------------------------------------
' Create the console log files.
'-----------------------------------------------------------------
Sub WriteLog(line)
    dim fileStream
    set fileStream = fileSystem.OpenTextFile(".\DisconnectSwitchPort.log", 8, true)
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

 

 





