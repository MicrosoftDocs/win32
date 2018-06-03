---
title: SetupSwitch method of the Msvm\_VirtualSwitchManagementService class
description: Sets up a switch such that the existing network architecture is maintained.
ms.assetid: 787e5def-cdd1-4a80-be33-94a33b91e6b5
keywords:
- SetupSwitch method Hyper-V
- SetupSwitch method Hyper-V , Msvm_VirtualSwitchManagementService class
- Msvm_VirtualSwitchManagementService class Hyper-V , SetupSwitch method
topic_type:
- apiref
api_name:
- Msvm_VirtualSwitchManagementService.SetupSwitch
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

# SetupSwitch method of the Msvm\_VirtualSwitchManagementService class

Sets up a switch such that the existing network architecture is maintained.

## Syntax


```mof
uint32 SetupSwitch(
  [in]  Msvm_SwitchPort           REF ExternalSwitchPort,
  [in]  Msvm_SwitchPort           REF InternalSwitchPort,
  [in]  Msvm_ExternalEthernetPort REF ExternalEthernetPort,
  [in]  string                        InternalEthernetPortName,
  [in]  string                        InternalEthernetPortFriendlyName,
  [out] Msvm_NetworkJob           REF Job
);
```



## Parameters

<dl> <dt>

*ExternalSwitchPort* \[in\]
</dt> <dd>

Type: **Msvm\_SwitchPort**

The switch port to which the external Ethernet port is to be connected. See [**Msvm\_SwitchPort**](msvm-switchport.md).

</dd> <dt>

*InternalSwitchPort* \[in\]
</dt> <dd>

Type: **Msvm\_SwitchPort**

The switch port to which the internal Ethernet port is to be connected.

</dd> <dt>

*ExternalEthernetPort* \[in\]
</dt> <dd>

Type: **Msvm\_ExternalEthernetPort**

A reference to the external Ethernet port that is to be bound. See [**Msvm\_ExternalEthernetPort**](msvm-externalethernetport.md).

</dd> <dt>

*InternalEthernetPortName* \[in\]
</dt> <dd>

Type: **string**

The name of the internal Ethernet port. This name must be unique among Ethernet ports.

</dd> <dt>

*InternalEthernetPortFriendlyName* \[in\]
</dt> <dd>

Type: **string**

A user-readable name for the internal Ethernet port.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

Type: **Msvm\_NetworkJob**

The work for setting up the switch is always an asynchronous background task because of the possibility of a network disconnection. This job reference can be used to find the result after and during the task. See [**Msvm\_NetworkJob**](msvm-networkjob.md).

</dd> </dl>

## Return value

Type: **uint32**

If this method returns 4096, then the method is being executed asynchronously, and the *Job* output parameter may be used to track the progress of the asynchronous operation. Any other return value indicates an error.

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

The following C# sample sets up a switch. The referenced utilities can be found in [Common Utilities for the Virtualization Samples](common-utilities-for-the-virtualization-samples.md).


```CSharp
using System;
using System.Management;

namespace HyperVSamples
{
    class SetupSwitchClass
    {
        ManagementObject switchService = null;
        ManagementScope scope = null;

        SetupSwitchClass()
        {
            scope = new ManagementScope(@"root\virtualization", null);
            switchService = Utility.GetServiceObject(scope, "Msvm_VirtualSwitchManagementService");
        }

        ManagementObject GetExternalEthernetPort(string externalEthernetPortName)
        {
            ManagementObject externalEthernetPort = Utility.GetHostSystemDevice("Msvm_ExternalEthernetPort", externalEthernetPortName, scope);
            return externalEthernetPort;
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
                if (instance["ElementName"].ToString() == switchPortName)
                {
                    switchPort = instance;
                    break;
                }
            }

            return switchPort;
        }

        ManagementObject CreateSwitchPort(string friendlyName, string name, ManagementObject virtualSwitch)
        {

            ManagementObject createdSwitchPort = null;

            ManagementBaseObject inParams = switchService.GetMethodParameters("CreateSwitchPort");

            inParams["FriendlyName"] = friendlyName;
            inParams["Name"] = name;
            inParams["VirtualSwitch"] = virtualSwitch.Path.Path;
            inParams["ScopeofResidence"] = null;
            ManagementBaseObject outParams = switchService.InvokeMethod("CreateSwitchPort", inParams, null);
            if ((UInt32)outParams["ReturnValue"] == ReturnCode.Completed)
            {
                createdSwitchPort = new ManagementObject(outParams["CreatedSwitchPort"].ToString());
                Console.WriteLine("{0} is created successfully", inParams["Name"]);
            }
            else
            {
                Console.WriteLine("Failed to create {0} switch port.", inParams["Name"]);
            }

            inParams.Dispose();
            outParams.Dispose();

            return createdSwitchPort;
        }


        void SetupSwitch
        (
            ManagementObject externalSwitchPort,
            ManagementObject internalSwitchPort,
            ManagementObject externalEthernetPort,
            string internalEthernetPortName,
            string internalEthernetPortFriendlyName

            )
        {
            ManagementBaseObject inParams = switchService.GetMethodParameters("SetupSwitch");
            inParams["InternalSwitchPort"] = internalSwitchPort.Path.Path;
            inParams["ExternalSwitchPort"] = externalSwitchPort.Path.Path;
            inParams["ExternalEthernetPort"] = externalEthernetPort.Path.Path;
            inParams["internalEthernetPortName"] = internalEthernetPortName;
            inParams["InternalEthernetPortFriendlyName"] = internalEthernetPortFriendlyName;

            ManagementBaseObject outParams = switchService.InvokeMethod("SetupSwitch", inParams, null);

            if ((UInt32)outParams["ReturnValue"] == ReturnCode.Started)
            {
                if (Utility.JobCompleted(outParams, scope))
                {
                    Console.WriteLine("SetupSwitch passed.");
                }
                else
                {
                    Console.WriteLine("SetupSwitch failed.");
                }
            }
            else if ((UInt32)outParams["ReturnValue"] == ReturnCode.Completed)
            {
                Console.WriteLine("SetupSwitch passed.");
            }
            else
            {
                Console.WriteLine("SetupSwitch failed.");
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
            if (args != null &amp;&amp; args.Length != 6)
            {
                Console.WriteLine("Usage:\nSetupSwitch switchName internalSwitchPortFriendlyName");
                Console.WriteLine("       externalSwitchPortFriendlyName externalEthernetPortFriendlyName");
                Console.WriteLine("       internalEthernetPortName internalEthernetPortFriendlyName");
                Console.WriteLine("Example:\nSetupSwitch {0} {1} {2} {3} {4} {5} {6} \"{7}\"",
                    "FirstSwitch",
                    "MyInternalSwitchPort",
                    "MyExternalSwitchPort",
                    "Intel(R) PRO/1000 PM Network Connection",
                    "InternalEthernetPortName",
                    "MyInternalEthernetPortName"
                    );
                return;
            }
            string switchName = args[0];
            string internalSwitchPortFriendlyName = args[1];
            string externalSwitchPortFriendlyName = args[2];
            string externalEthernetPortFriendlyName = args[3];
            string internalEthernetPortName = args[4];
            string internalEthernetPortFriendlyName = args[5];
            SetupSwitchClass setupSwitchClass = new SetupSwitchClass();
            ManagementObject virtualSwitch = setupSwitchClass.GetVirtualSwitch(switchName);
            if (virtualSwitch == null)
            {
                Console.WriteLine("Unable to find virtual switch '{0}'}", switchName);
                return;
            }

            ManagementObject internetSwitchPort = setupSwitchClass.GetVirtualSwitchPort(virtualSwitch, internalSwitchPortFriendlyName);
            if (internetSwitchPort == null)
            {
                Console.WriteLine("Unable to find switch port '{0}'}", internalSwitchPortFriendlyName);
            }

            ManagementObject externalSwitchPort = setupSwitchClass.GetVirtualSwitchPort(virtualSwitch, externalSwitchPortFriendlyName);
            if (internetSwitchPort == null)
            {
                Console.WriteLine("Unable to find switch port '{0}'}", externalSwitchPortFriendlyName);
            }

            ManagementObject externalEthernetPort = setupSwitchClass.GetExternalEthernetPort(externalEthernetPortFriendlyName);

            if (externalEthernetPort == null)
            {
                Console.WriteLine("Unable to find external Ethernet port'{0}'}", externalEthernetPortFriendlyName);
            }

            setupSwitchClass.SetupSwitch
            (
                externalSwitchPort,
                internetSwitchPort,
                externalEthernetPort,
                internalEthernetPortName,
                internalEthernetPortFriendlyName
            );

            externalSwitchPort.Dispose();
            internetSwitchPort.Dispose();
            externalEthernetPort.Dispose();
            virtualSwitch.Dispose();

            setupSwitchClass.Close();

        }
    }
}
```



The following VBScript sample sets up a switch.


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
    dim switchFriendlyName, internalSwitchPortFriendlyName
    dim externalSwitchPortFriendlyName, externalEthernetPortFriendlyName
    dim internalEthernetPortName, internalEthernetPortFriendlyName
    dim switch, internalSwitchPort, externalSwitchPort, externalEthernetPort

    set objArgs = WScript.Arguments
    if WScript.Arguments.Count = 6 then
       switchFriendlyName = objArgs.Unnamed.Item(0)
       internalSwitchPortFriendlyName = objArgs.Unnamed.Item(1)
       externalSwitchPortFriendlyName = objArgs.Unnamed.Item(2)
       externalEthernetPortFriendlyName = objArgs.Unnamed.Item(3)
       internalEthernetPortName = objArgs.Unnamed.Item(4)
       internalEthernetPortFriendlyName = objArgs.Unnamed.Item(5)
    else
       WScript.Echo "usage: cscript SetupSwitch " &amp;_
                            "switchName " &amp;_
                            "internalSwitchPortFriendlyName " &amp;_
                            "externalSwitchPortFriendlyName " &amp;_
                            "externalEthernetPortFriendlyName " &amp;_
                            "internalEthernetPortName " &amp;_
                            "internalEthernetPortFriendlyName"
       WScript.Echo "Example: SetupSwitch " &amp;_
                              "FirstSwitch " &amp;_
                              "MyInternalSwitchPort " &amp;_
                              "MyExternalSwitchPort " &amp;_
                              """Intel(R) PRO/1000 PM Network Connection"" " &amp;_
                              "InternalEthernetPortName " &amp;_
                              "MyInternalEthernetPortName "
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
    
    set internalSwitchPort = GetVirtualSwitchPort(switch, internalSwitchPortFriendlyName)
    if (internalSwitchPort Is Nothing) then
        WriteLog Format1("Unable to find switchPort '{0}'.", internalSwitchPortFriendlyName)
        WScript.Quit(1)   
    end if 
    
    
    set externalSwitchPort = GetVirtualSwitchPort(switch, externalSwitchPortFriendlyName)
    if (externalSwitchPort Is Nothing) then
        WriteLog Format1("Unable to find switchPort '{0}'.", externalSwitchPortFriendlyName)
        WScript.Quit(1)   
    end if 
        
    set externalEthernetPort = GetExternalEthernetPort(externalEthernetPortFriendlyName)
    if (externalEthernetPort Is Nothing) then
       WriteLog Format1("Unable to find external Ethernet Port {0}", externalEthernetPortFriendlyName)
       WScript.Quit(1)
    end if    
    
    if SetupSwitch( _
        externalSwitchPort, _
        internalSwitchPort, _
        externalEthernetPort, _ 
        internalEthernetPortName, _ 
        internalEthernetPortFriendlyName _
        ) _
    then
        WriteLog "Done"
        WScript.Quit(0)
    else
        WriteLog "SetupSwitch failed"
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
' setup a virtual switch by calling SetupSwitch WMI method
'-----------------------------------------------------------------
Function SetupSwitch( _
    externalSwitchPort, _
    internalSwitchPort, _
    externalEthernetPort, _ 
    internalEthernetPortName, _ 
    internalEthernetPortFriendlyName _
) 
    dim objInParam, objOutParams
    
    SetupSwitch = false
    set objInParam = switchService.Methods_("SetupSwitch").InParameters.SpawnInstance_()

    objInParam.ExternalSwitchPort = externalSwitchPort.Path_.Path
    objInParam.InternalSwitchPort = internalSwitchPort.Path_.Path
    objInParam.ExternalEthernetPort = externalEthernetPort.Path_.Path
    objInParam.InternalEthernetPortName = internalEthernetPortName
    objInParam.InternalEthernetPortFriendlyName = internalEthernetPortFriendlyName

    set objOutParams = switchService.ExecMethod_("SetupSwitch", objInParam)

    if objOutParams.ReturnValue = wmiStarted then
        if (WMIJobCompleted(objOutParams)) then
            SetupSwitch = true
        end if
    elseif (objOutParams.ReturnValue = wmiSuccessful) then
        SetupSwitch = true
    else
        WriteLog Format1("SetupSwitch failed with error {0}", objOutParams.ReturnValue)
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
    set fileStream = fileSystem.OpenTextFile(".\SetupSwitch.log", 8, true)
    WScript.Echo line
    fileStream.WriteLine line
    fileStream.Close

End Sub

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

 

 





