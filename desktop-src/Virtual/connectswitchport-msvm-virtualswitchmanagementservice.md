---
title: ConnectSwitchPort method of the Msvm\_VirtualSwitchManagementService class
description: Connects a switch port to a LAN endpoint. Upon success of the connection, an active connection instance will be created that associates the port with the LAN endpoint.
ms.assetid: 47aa6954-972f-474c-8514-90838ffb7d50
keywords:
- ConnectSwitchPort method Hyper-V
- ConnectSwitchPort method Hyper-V , Msvm_VirtualSwitchManagementService class
- Msvm_VirtualSwitchManagementService class Hyper-V , ConnectSwitchPort method
topic_type:
- apiref
api_name:
- Msvm_VirtualSwitchManagementService.ConnectSwitchPort
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

# ConnectSwitchPort method of the Msvm\_VirtualSwitchManagementService class

Connects a switch port to a LAN endpoint. Upon success of the connection, an active connection instance will be created that associates the port with the LAN endpoint.

## Syntax


```mof
uint32 ConnectSwitchPort(
  [in]  Msvm_SwitchPort       REF SwitchPort,
  [in]  CIM_LANEndpoint       REF LANEndpoint,
  [out] Msvm_ActiveConnection REF ActiveConnection
);
```



## Parameters

<dl> <dt>

*SwitchPort* \[in\]
</dt> <dd>

Type: **Msvm\_SwitchPort**

The switch port to be connected to the LAN endpoint. See [**Msvm\_SwitchPort**](msvm-switchport.md).

</dd> <dt>

*LANEndpoint* \[in\]
</dt> <dd>

Type: **CIM\_LANEndpoint**

The LAN endpoint to be connected to the switch port. See [**CIM\_LANEndpoint**](https://msdn.microsoft.com/library/cc136865).

</dd> <dt>

*ActiveConnection* \[out\]
</dt> <dd>

Type: **Msvm\_ActiveConnection**

Upon successful completion of this method, this parameter contains the created connection association. See [**Msvm\_ActiveConnection**](msvm-activeconnection.md).

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

The following C# sample connects a switch port. The referenced utilities can be found in [Common Utilities for the Virtualization Samples](common-utilities-for-the-virtualization-samples.md).


```CSharp
using System;
using System.Management;

namespace HyperVSamples
{
    class ConnectSwitchPortClass
    {
        ManagementObject switchService = null;
        ManagementScope scope = null;

        ConnectSwitchPortClass()
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


        ManagementObject GetVMEthernetPort(string vmName, string vmEthernetPortClass)
        {
            ManagementObject vmEthernetPort = null;
            ManagementObject computerSystem = Utility.GetTargetComputer(vmName, scope);

            ManagementObjectCollection vmEthernetPorts = computerSystem.GetRelated
            (
                vmEthernetPortClass,
                "Msvm_SystemDevice",
                null,
                null,
                "PartComponent",
                "GroupComponent",
                false,
                null
            );

            foreach (ManagementObject instance in vmEthernetPorts)
            {
                vmEthernetPort = instance;
                break;

            }

            return vmEthernetPort;
        }

        ManagementObject GetVMLanEndPoint(ManagementObject vmEthernetPort)
        {
            ManagementObjectCollection vmEndPoints = vmEthernetPort.GetRelated
             (
                 "Msvm_VMLanEndPoint",
                 "Msvm_DeviceSAPImplementation",
                 null,
                 null,
                 "Dependent",
                 "Antecedent",
                 false,
                 null
             );

            ManagementObject vmEndPoint = null;

            foreach (ManagementObject instance in vmEndPoints)
            {
                vmEndPoint = instance;
                break;
            }

            return vmEndPoint;
        }

        void ConnectSwitchPort(ManagementObject switchPort, ManagementObject LanEndPoint)
        {
            ManagementBaseObject inParams = switchService.GetMethodParameters("ConnectSwitchPort");

            inParams["SwitchPort"] = switchPort.Path.Path;
            inParams["LANEndpoint"] = LanEndPoint.Path.Path;
            ManagementBaseObject outParams = switchService.InvokeMethod("ConnectSwitchPort", inParams, null);
            if ((UInt32)outParams["ReturnValue"] == ReturnCode.Completed)
            {
                Console.WriteLine("{0} was connected successfully", switchPort.Path.Path);
            }
            else
            {
                Console.WriteLine("Failed to connect {0} switch port.", switchPort.Path.Path);
            }
            inParams.Dispose();
            outParams.Dispose();
            switchPort.Dispose();
            switchService.Dispose();
        }

        static void Usage()
        {
            Console.WriteLine("Usage: ConnectSwitchPort SwitchName SwitchPortName vmName vmNicType");
            Console.WriteLine("vmNicType: Synthetic|Emulated");
            Console.WriteLine("Example: ConnectSwitchPort {0} \"{1}\" {2} {3}",
                "MyFirstSwitch",
                "VM Switch Port",
                "MyFirstVM",
                "Emulated"
                );
        }

        static void Main(string[] args)
        {
            if (args != null &amp;&amp; args.Length != 4)
            {
                Usage();
                return;
            }

            string switchName = args[0];
            string switchPortName = args[1];
            string vmName = args[2];
            string vmNicType = args[3];

            string vmNicClassName = null;

            if (vmNicType.ToLower() == "emulated")
            {
                vmNicClassName = "Msvm_EmulatedEthernetPort";
            }
            else if (vmNicType.ToLower() == "synthetic")
            {
                vmNicClassName = "Msvm_SyntheticEthernetPort";
            }
            else
            {
                Usage();
            }


            ConnectSwitchPortClass connectSwitchPort = new ConnectSwitchPortClass();
            ManagementObject virtualSwitch = connectSwitchPort.GetVirtualSwitch(switchName);
            ManagementObject virtualSwitchPort = connectSwitchPort.GetVirtualSwitchPort(virtualSwitch, switchPortName);
            ManagementObject vmNic = connectSwitchPort.GetVMEthernetPort(vmName, vmNicClassName);
            ManagementObject vmLanEndPoint = connectSwitchPort.GetVMLanEndPoint(vmNic);
            connectSwitchPort.ConnectSwitchPort(virtualSwitchPort, vmLanEndPoint);

            virtualSwitch.Dispose();
            virtualSwitchPort.Dispose();
            vmNic.Dispose();
            vmLanEndPoint.Dispose();
        }
    }
}
```



The following VBScript sample connects a switch port.


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
    dim computer, objArgs
    dim switchFriendlyName, switchPortFriendlyName, switch, switchPort
    dim vmName, vmEthernetPortType, vmEthernetPortClassName
    dim vmEthernetPort, vmEthernetPortEndPoint

    set objArgs = WScript.Arguments
    if WScript.Arguments.Count = 4 then
       switchFriendlyName = objArgs.Unnamed.Item(0)
       switchPortFriendlyName = objArgs.Unnamed.Item(1)
       vmName = objArgs.Unnamed.Item(2)
       vmEthernetPortType = objArgs.Unnamed.Item(3)
       vmEthernetPortClassName = GetEthernetPortClassName(vmEthernetPortType)
    else
       Usage()
    end if     
    
    set fileSystem = Wscript.CreateObject("Scripting.FileSystemObject")
    computer = "."    

    set objWMIService = GetObject("winmgmts:\\" & computer & "\root\virtualization")
    set switchService = objWMIService.ExecQuery("select * from Msvm_VirtualSwitchManagementService").ItemIndex(0)
    
    set switch = GetVirtualSwitch(switchFriendlyName)
    if (switch Is Nothing) then
        WriteLog Format1("Unable to find switch {0}", switchFriendlyName)
        WScript.Quit(1)   
    end if
    
    set switchPort = GetVirtualSwitchPort(switch, switchPortFriendlyName)

    if (switchPort Is Nothing) then
        WriteLog Format1("Unable to find switchPort '{0}'", switchPortFriendlyName)
        WScript.Quit(1)   
    end if  
    
    set vmEthernetPort = GetVMEthernetPort(vmName, vmEthernetPortClassName) 
    if (vmEthernetPort Is Nothing) then
        WriteLog Format1("Unable to find VM {0} instance.", vmEthernetPortClassName)
        WScript.Quit(1)
    end if

    set vmEthernetPortEndPoint = GetVMEthernetPortEndPoint(vmEthernetPort)
    if (vmEthernetPortEndPoint Is Nothing) then
        WriteLog Format1("Unable to find VM {0} endpoint.", vmEthernetPortClassName)
        WScript.Quit(1)
    end if
    
    if ConnectSwitchPort(switchPort, vmEthernetPortEndPoint) then
        WriteLog "Done"
        WScript.Quit(0)
    else
        WriteLog "ConnectSwitchPort failed"
        WScript.Quit(1)
    end if

End Sub

'-----------------------------------------------------------------
' Display command line help
'-----------------------------------------------------------------
Sub Usage()

    WScript.Echo "usage: cscript ConnectSwitchPort SwitchFriendlyName" &amp;_
                  "SwitchPortFriendlyName vmFriendlyName" &amp;_
                  "vmEthernetPortType"
    WScript.Echo "vmEthernetPortType: Synthetic | Emulated" & vbcrlf 
    
    WScript.Echo "Example: cscript ConnectSwitchPort ""First VirtualSwitch"" " &amp;_
                 """First VirtualSwitch Port"" MyFirstVM Emulated"
    WScript.Quit(1)

End Sub

'-----------------------------------------------------------------
' Get vm Ethernet port WMI class name
'-----------------------------------------------------------------
Function GetEthernetPortClassName(vmEthernetportType)

    if lcase(vmEthernetPortType) = "emulated" then
       GetEthernetPortClassName = "Msvm_EmulatedEthernetPort"
    elseif lcase(vmEthernetPortType) = "synthetic" then
       GetEthernetPortClassName = "Msvm_SyntheticEthernetPort"
    else
       usage()
    end if 

End Function

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
' Get VM Ethernet port
'-----------------------------------------------------------------
Function GetVMEthernetPort(vmName, vmEthernetPortClass)
    dim query, vmEthernetPort, vm
    set GetVMEthernetPort = Nothing
    
    query = Format1("select * from Msvm_ComputerSystem where ElementName = '{0}'", vmName)
    set vm= objWMIService.ExecQuery(query).ItemIndex(0)
    
    if (vm Is Nothing) then
        WriteLog Format1("Unable to find specified VM {0}", vmName)
        WScript.Quit(1)   
    end if 
    
    query = Format2("ASSOCIATORS OF {{0}} WHERE resultClass = {1}", vm.Path_.Path, vmEthernetPortClass)
    set GetVMEthernetPort = objWMIService.ExecQuery(query).itemIndex(0)
    
End Function

'-----------------------------------------------------------------
' Get VM Ethernet port endpoint
'-----------------------------------------------------------------
Function GetVMEthernetPortEndPoint(vmEthernetPort)
    dim query, vmEthernetPorts, vm
    set GetVMEthernetPortEndPoint = Nothing
    
    query = Format1("ASSOCIATORS OF {{0}} WHERE resultClass = Msvm_VmLANEndpoint", vmEthernetPort.Path_.Path)
    set GetVMEthernetPortEndPoint = objWMIService.ExecQuery(query).ItemIndex(0)
End Function

'-----------------------------------------------------------------
' Connect switch port with  vm Ethernet endpoint
'-----------------------------------------------------------------
Function ConnectSwitchPort(switchPort, lanEndpoint)
    dim objInParam, objOutParams
    ConnectSwitchPort = false
    set objInParam = switchService.Methods_("ConnectSwitchPort").InParameters.SpawnInstance_()
    objInParam.LANEndPoint = lanEndpoint.Path_.Path
    objInParam.SwitchPort = switchPort.Path_.Path

    set objOutParams = switchService.ExecMethod_("ConnectSwitchPort", objInParam)
    
    if objOutParams.ReturnValue = wmiSuccessful then
        ConnectSwitchPort = true
    else
        WriteLog Format1("ConnectSwitchPort failed with error code {0}", objOutParams.ReturnValue)
    end if

End Function

'-----------------------------------------------------------------
' Create the console log files.
'-----------------------------------------------------------------
Sub WriteLog(line)
    dim fileStream
    set fileStream = fileSystem.OpenTextFile(".\ConnectSwitchPort.log", 8, true)
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

[**Msvm\_VirtualSwitchManagementService**](msvm-virtualswitchmanagementservice.md)
</dt> </dl>

 

 





