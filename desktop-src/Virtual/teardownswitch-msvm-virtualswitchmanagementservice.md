---
title: TeardownSwitch method of the Msvm\_VirtualSwitchManagementService class
description: Deletes the internal port for a switch and unbinds the external adapter, reversing the work done by SetupSwitch. The external Ethernet port and the internal Ethernet port must be bound to the same switch.
ms.assetid: de963065-5e93-4435-b391-9e0f16acded6
keywords:
- TeardownSwitch method Hyper-V
- TeardownSwitch method Hyper-V , Msvm_VirtualSwitchManagementService class
- Msvm_VirtualSwitchManagementService class Hyper-V , TeardownSwitch method
topic_type:
- apiref
api_name:
- Msvm_VirtualSwitchManagementService.TeardownSwitch
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

# TeardownSwitch method of the Msvm\_VirtualSwitchManagementService class

Deletes the internal port for a switch and unbinds the external adapter, reversing the work done by [**SetupSwitch**](setupswitch-msvm-virtualswitchmanagementservice.md). The external Ethernet port and the internal Ethernet port must be bound to the same switch.

## Syntax


```mof
uint32 TeardownSwitch(
  [in]  Msvm_ExternalEthernetPort REF ExternalEthernetPort,
  [in]  Msvm_InternalEthernetPort REF InternalEthernetPort,
  [out] Msvm_NetworkJob           REF Job
);
```



## Parameters

<dl> <dt>

*ExternalEthernetPort* \[in\]
</dt> <dd>

Type: **Msvm\_ExternalEthernetPort**

A reference to the external Ethernet port to be unbound. See [**Msvm\_ExternalEthernetPort**](msvm-externalethernetport.md).

</dd> <dt>

*InternalEthernetPort* \[in\]
</dt> <dd>

Type: **Msvm\_InternalEthernetPort**

A reference to the internal Ethernet port to be deleted. See [**Msvm\_InternalEthernetPort**](msvm-internalethernetport.md). If no port is provided, there must not be an internal NIC attached to the switch and there must be an external NIC attached. The physical NIC is disconnected and no protocols are rebound.

**Windows Server 2008:** The **InternalEthernetPort** parameter is not optional

</dd> <dt>

*Job* \[out\]
</dt> <dd>

Type: **Msvm\_NetworkJob**

The work for tearing down the switch is always an asynchronous background task because of the possibility of a network disconnection. This job reference can be used to find the result after and during the task. See [**Msvm\_NetworkJob**](msvm-networkjob.md).

</dd> </dl>

## Return value

Type: **uint32**

This method returns one of the following values.

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

The following C# sample tears down a switch. The referenced utilities can be found in [Common Utilities for the Virtualization Samples](common-utilities-for-the-virtualization-samples.md).


```CSharp
using System;
using System.Management;


namespace HyperVSamples
{
    class TeardownSwitchClass
    {
        ManagementObject switchService = null;
        ManagementScope scope = null;

        TeardownSwitchClass()
        {
            scope = new ManagementScope(@"root\virtualization", null);
            switchService = Utility.GetServiceObject(scope, "Msvm_VirtualSwitchManagementService");
        }


        void TeardownSwitch(string externalEthernetPortName, string internalEthernetPortName)
        {
            ManagementObject externalEthernetPort = Utility.GetHostSystemDevice("Msvm_ExternalEthernetPort", externalEthernetPortName, scope);
            ManagementObject internalEthernetPort = Utility.GetHostSystemDevice("Msvm_InternalEthernetPort", internalEthernetPortName, scope);

            ManagementBaseObject inParams = switchService.GetMethodParameters("TeardownSwitch");
            inParams["ExternalEthernetPort"] = externalEthernetPort.Path.Path;
            inParams["InternalEthernetPort"] = internalEthernetPort.Path.Path;

            ManagementBaseObject outParams = switchService.InvokeMethod("TeardownSwitch", inParams, null);

            if ((UInt32)outParams["ReturnValue"] == ReturnCode.Started)
            {
                if (Utility.JobCompleted(outParams, scope))
                {
                    Console.WriteLine("TeardownSwitch passed.");
                }
                else
                {
                    Console.WriteLine("TeardownSwitch failed.");
                }
            }
            else if ((UInt32)outParams["ReturnValue"] == ReturnCode.Completed)
            {
                Console.WriteLine("TeardownSwitch passed.");
            }
            else
            {
                Console.WriteLine("TeardownSwitch failed.");
            }

            inParams.Dispose();
            outParams.Dispose();
        }

        static void Main(string[] args)
        {
            if (args != null &amp;&amp; args.Length != 2)
            {
                Console.WriteLine("Usage:\nTearDownSwitch ExternalEthernetPortFriendlyName internalEthernetPortFriendlyName");
                Console.WriteLine("Example:\nTearDownSwitch \"Intel(R) PRO/1000 PM Network Connection\" MyInternalEthernetPortName");
                return;
            }

            TeardownSwitchClass teardownSwitch = new TeardownSwitchClass();
            teardownSwitch.TeardownSwitch(args[0], args[1]);
        }
    }
}
```



The following VBScript sample tears down a switch.


```VB
option explicit 

dim objWMIService
dim switchService
dim fileSystem

const JobStarting = 3
const JobRunning = 4
const JobCompleted = 7
const wmiStarted = 4096
const wmiSuccessful = 0

Main()

'-----------------------------------------------------------------
' Main
'-----------------------------------------------------------------
Sub Main()
    dim computer, objArgs 
    dim externalEthernetPortFriendlyName, internalEthernetPortFriendlyName
    dim internalEthernetPort, externalEthernetPort

    set objArgs = WScript.Arguments
    if WScript.Arguments.Count = 2 then
       externalEthernetPortFriendlyName = objArgs.Unnamed.Item(0)
       internalEthernetPortFriendlyName = objArgs.Unnamed.Item(1)
    else
       WScript.Echo "usage: cscript TeardownSwitch " &amp;_
                            "externalEthernetPortFriendlyName " &amp;_
                            "internalEthernetPortFriendlyName" 
       
       WScript.Echo "Example: TeardownSwitch " &amp;_
                              """Intel(R) PRO/1000 PM Network Connection"" " &amp;_
                              "MyInternalEthernetPortName "
       WScript.Quit(1)
    end if     
    
    set fileSystem = Wscript.CreateObject("Scripting.FileSystemObject")
    computer = "."    

    set objWMIService = GetObject("winmgmts:\\" & computer & "\root\virtualization")
    set switchService = objWMIService.ExecQuery("select * from Msvm_VirtualSwitchManagementService").ItemIndex(0)

    set externalEthernetPort = GetEthernetPort(externalEthernetPortFriendlyName, "Msvm_ExternalEthernetPort")
    if (externalEthernetPort Is Nothing) then
       WriteLog Format1("Unable to find external Ethernet Port {0}", externalEthernetPortFriendlyName)
       WScript.Quit(1)
    end if 
    
    set internalEthernetPort = GetEthernetPort(internalEthernetPortFriendlyName, "Msvm_InternalEthernetPort")
    if (internalEthernetPort Is Nothing) then
       WriteLog Format1("Unable to find internal Ethernet Port {0}", internalEthernetPortFriendlyName)
       WScript.Quit(1)
    end if          
    
    if TeardownSwitch(externalEthernetPort, internalEthernetPort) then
        WriteLog "Done"
        WScript.Quit(0)
    else
        WriteLog "Teardown switch failed"
        WScript.Quit(1)
    end if
End Sub

'-----------------------------------------------------------------
' Retrieve an Ethernet port 

rnetPort, EthernetPorts
    
    set GetEthernetPort = Nothing
    set objNTInfo = CreateObject("WinNTSystemInfo")
    computerName = lcase(objNTInfo.ComputerName)

    query = Format1("select * from Msvm_ComputerSystem where Name = '{0}'", computerName)
    set computer = objWMIService.ExecQuery(query).ItemIndex(0)
    
    query = Format2("ASSOCIATORS OF {{0}} WHERE resultClass = {1}", _
            computer.Path_.Path, EthernetPortClassName)
            
    set EthernetPorts = objWMIService.ExecQuery(query)
    for each EthernetPort in EthernetPorts
        if lcase(EthernetPort.ElementName) = lcase(EthernetPortFriendlyName) then
            set GetEthernetPort = EthernetPort
            Exit Function
        end if
    next
End Function

'-----------------------------------------------------------------
' teardown a virtual switch by calling TeardownSwitch sw WMI method
'-----------------------------------------------------------------
Function TeardownSwitch(externalEthernetPort, internalEthernetPort)
    dim objInParam, objOutParams
    
    TeardownSwitch = false
    set objInParam = switchService.Methods_("TeardownSwitch").InParameters.SpawnInstance_()

    objInParam.ExternalEthernetPort = externalEthernetPort.Path_.Path
    objInParam.InternalEthernetPort = internalEthernetPort.Path_.Path

    set objOutParams = switchService.ExecMethod_("TeardownSwitch", objInParam)

    if objOutParams.ReturnValue = wmiStarted then
        if (WMIJobCompleted(objOutParams)) then
            TeardownSwitch = true
        end if
    elseif (objOutParams.ReturnValue = wmiSuccessful) then
        TeardownSwitch = true
    else
        WriteLog Format1("TeardownSwitch failed with error {0}", objOutParams.ReturnValue)
    end if
End Function

'-----------------------------------------------------------------
' Handle wmi Job object
'-----------------------------------------------------------------
Function WMIJobCompleted(outParam)
    
    dim WMIJob, jobState
    WMIJobCompleted = true

    set WMIJob = objWMIService.Get(outParam.Job)
    
    jobState = WMIJob.JobState

    while jobState = JobRunning or jobState = JobStarting
        WriteLog Format1("In progress... {0}% completed.",WMIJob.PercentComplete)
        WScript.Sleep(1000)
        set WMIJob = objWMIService.Get(outParam.Job)
        jobState = WMIJob.JobState
    wend

    if (WMIJob.JobState <> JobCompleted) then
        WriteLog Format1("ErrorDescription:{0}", WMIJob.ErrorDescription)
        WriteLog Format1("ErrorCode:{0}", WMIJob.ErrorCode)
        WMIJobCompleted = false
    end if
    
End Function
'-----------------------------------------------------------------
' Create the console log files.
'-----------------------------------------------------------------
Sub WriteLog(line)
    dim fileStream
    set fileStream = fileSystem.OpenTextFile(".\TeardownSwitch.log", 8, true)
    WScript.Echo line
    fileStream.WriteLine line
    fileStream.Close

End Sub

'------------------------------------------------------------------------------
' The string formatting functions to avoid string concatenation.
'------------------------------------------------------------------------------
Function Format2(myString, arg0, arg1)
    Format2 = Format1(myString, arg0)

    if IsNull(arg1) then
        Format2 = Replace(myString, "{1}", "NULL")
    else
        Format2 = Replace(Format2, "{1}", arg1)
    end if
End Function

'------------------------------------------------------------------------------
' The string formatting functions to avoid string concatenation.
'------------------------------------------------------------------------------
Function Format1(myString, arg0)
    if IsNull(arg0) then
        Format1 = Replace(myString, "{0}", "NULL")
    else
        Format1 = Replace(myString, "{0}", arg0)
    end if
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

 

 





