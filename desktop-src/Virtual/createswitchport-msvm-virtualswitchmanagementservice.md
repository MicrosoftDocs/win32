---
title: CreateSwitchPort method of the Msvm\_VirtualSwitchManagementService class
description: Creates a new port on a virtual switch.
ms.assetid: 1ff23885-1ba3-43bd-9517-b32931888e52
keywords:
- CreateSwitchPort method Hyper-V
- CreateSwitchPort method Hyper-V , Msvm_VirtualSwitchManagementService class
- Msvm_VirtualSwitchManagementService class Hyper-V , CreateSwitchPort method
topic_type:
- apiref
api_name:
- Msvm_VirtualSwitchManagementService.CreateSwitchPort
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

# CreateSwitchPort method of the Msvm\_VirtualSwitchManagementService class

Creates a new port on a virtual switch.

## Syntax


```mof
uint32 CreateSwitchPort(
  [in]  Msvm_VirtualSwitch REF VirtualSwitch,
  [in]  string                 Name,
  [in]  string                 FriendlyName,
  [in]  string                 ScopeOfResidence,
  [out] Msvm_SwitchPort    REF CreatedSwitchPort
);
```



## Parameters

<dl> <dt>

*VirtualSwitch* \[in\]
</dt> <dd>

Type: **Msvm\_VirtualSwitch**

The switch on which the port is to be created. See [**Msvm\_VirtualSwitch**](msvm-virtualswitch.md).

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Type: **string**

The name of the port. This name must be unique among all ports.

</dd> <dt>

*FriendlyName* \[in\]
</dt> <dd>

Type: **string**

A user-readable name for the port.

</dd> <dt>

*ScopeOfResidence* \[in\]
</dt> <dd>

Type: **string**

The authorization scope to be used for the access control policy of this virtual switch port.

</dd> <dt>

*CreatedSwitchPort* \[out\]
</dt> <dd>

Type: **Msvm\_SwitchPort**

Upon successful completion of this method, this parameter contains the created switch port. See [**Msvm\_SwitchPort**](msvm-switchport.md).

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

The following C# sample creates a port on a virtual switch. The referenced utilities can be found in [Common Utilities for the Virtualization Samples](common-utilities-for-the-virtualization-samples.md).


```CSharp
using System;
using System.Management;


namespace HyperVSamples
{
    class CreateSwitchPortClass
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

        static ManagementObject CreateSwitchPort(string switchName, string name, string friendlyName)
        {
            ManagementScope scope = new ManagementScope(@"root\virtualization", null);
            ManagementObject switchService = Utility.GetServiceObject(scope, "Msvm_VirtualSwitchManagementService");

            ManagementObject createdSwitchPort = null;

            ManagementBaseObject inParams = switchService.GetMethodParameters("CreateSwitchPort");

            ManagementObject virtualSwitch = GetVirtualSwitch(switchName, scope);

            inParams["FriendlyName"] = friendlyName;
            inParams["Name"] = name;
            inParams["VirtualSwitch"] = virtualSwitch.Path.Path;
            inParams["ScopeofResidence"] = null;
            ManagementBaseObject outParams = switchService.InvokeMethod("CreateSwitchPort", inParams, null);
            if ((UInt32)outParams["ReturnValue"] == ReturnCode.Completed)
            {
                createdSwitchPort = new ManagementObject(outParams["CreatedSwitchPort"].ToString());
                Console.WriteLine("{0} was created successfully", inParams["Name"]);
            }
            else
            {
                Console.WriteLine("Failed to create {0} switch port.", inParams["Name"]);
            }

            inParams.Dispose();
            outParams.Dispose();

            return createdSwitchPort;
        }


        static void Main(string[] args)
        {
            if (args != null &amp;&amp; args.Length != 3)
            {
                Console.WriteLine("Usage: CreateSwitchPort SwitchName, Name, FriendlyName");
                Console.WriteLine("Example: CreateSwitchPort \"{0}\" {1} {2}",
                    "First_VirtalSwitch",
                    "FirstVirtualSwitchPort",
                    "First VirtualSwitch Port"
                    );
                return;
            }
            CreateSwitchPort(args[0], args[1], args[2]);
        }
    }
}
```



The following VBScript sample creates a port on a virtual switch.


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
    dim switch, switchName,  name, friendlyName, createdSwitchPort
    
    set fileSystem = Wscript.CreateObject("Scripting.FileSystemObject")
    computer = "."

    set objWMIService = GetObject("winmgmts:\\" & computer & "\root\virtualization")
    set switchService = objWMIService.ExecQuery("select * from Msvm_VirtualSwitchManagementService").ItemIndex(0)
    
    set objArgs = WScript.Arguments
    if WScript.Arguments.Count = 3 then
       switchName = objArgs.Unnamed.Item(0)
       name = objArgs.Unnamed.Item(1)
       friendlyName = objArgs.Unnamed.Item(2)
    else
       WScript.Echo "usage: cscript CreateSwitchPort SwitchName Name FriendlyName"
       WScript.Echo "Example: CreateSwitchPort MyFirstSwitch FirstVirtualSwitchPort ""First VirtualSwitch Port""" 
       WScript.Quit(1)
    end if
        
    set switch = GetVirtualSwitch(switchName)
    if Not (switch Is Nothing) then
        set createdSwitchPort = CreateSwitchPort(switch, name, friendlyName)
        if Not(createdSwitchPort Is Nothing) then
            WriteLog "Done"
            WScript.Quit(0)
        End if
    else
        WriteLog "CreateSwitchPort failed"
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
' Create a virtual switch by calling CreateSwitch WMI method
'-----------------------------------------------------------------
Function CreateSwitchPort(virtualSwitch, name, friendlyName)
    dim objInParam, objOutParams
    
    set CreateSwitchPort = Nothing
    set objInParam = switchService.Methods_("CreateSwitchPort").InParameters.SpawnInstance_()
    objInParam.FriendlyName = friendlyName
    objInParam.Name = name
    objInParam.VirtualSwitch = virtualSwitch.Path_.Path
    objInParam.ScopeofResidence = null

    set objOutParams = switchService.ExecMethod_("CreateSwitchPort", objInParam)
    
    if objOutParams.ReturnValue = wmiSuccessful then
        set CreateSwitchPort = objWMIService.Get(objOutParams.CreatedSwitchPort)
    else
        WriteLog Format1("CreateSwitchPort failed with error code {0}", objOutParams.ReturnValue)
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

 

 





