---
description: Requests that the state of the virtual machine be changed to the specified value.
ms.assetid: 87BE4C7D-604B-4F8D-B4DC-89BD563E3999
title: RequestStateChange method of the Msvm_ComputerSystem class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_ComputerSystem.RequestStateChange
api_type: 
- COM
api_location: 
- vmms.exe
---

# RequestStateChange method of the Msvm\_ComputerSystem class

Requests that the state of the virtual machine be changed to the specified value. Invoking the **RequestStateChange** method multiple times could result in earlier requests being overwritten or lost. This method is only supported for instances of the [**Msvm\_ComputerSystem**](msvm-computersystem.md) class that represent a virtual machine.

While the state change is in progress, the **RequestedState** property is changed to the value of the *RequestedState* parameter.

## Syntax


```mof
uint32 RequestStateChange(
  [in]  uint16              RequestedState,
  [out] CIM_ConcreteJob REF Job,
  [in]  datetime            TimeoutPeriod
);
```



## Parameters

<dl> <dt>

*RequestedState* \[in\]
</dt> <dd>

Type: **uint16**

The new state. Values that are greater than 32767 are **DMTF** proposed values and are subject to change.

Here are possible values:

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)


</dt> <dd>

Corresponds to [**CIM\_EnabledLogicalElement.EnabledState**](/previous-versions//cc136818(v=vs.85)) = Other.

</dd> <dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>**Enabled** (2)


</dt> <dd>

Corresponds to [**CIM\_EnabledLogicalElement.EnabledState**](/previous-versions//cc136818(v=vs.85)) = Enabled.

</dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>**Disabled** (3)


</dt> <dd>

Corresponds to [**CIM\_EnabledLogicalElement.EnabledState**](/previous-versions//cc136818(v=vs.85)) = Disabled.

</dd> <dt>

<span id="Shut_Down"></span><span id="shut_down"></span><span id="SHUT_DOWN"></span>

<span id="Shut_Down"></span><span id="shut_down"></span><span id="SHUT_DOWN"></span>**Shut Down** (4)


</dt> <dd>

Valid in version 1 (V1) of Hyper-V only. The virtual machine is shutting down via the shutdown service. Corresponds to [**CIM\_EnabledLogicalElement.EnabledState**](/previous-versions//cc136818(v=vs.85)) = ShuttingDown.

</dd> <dt>

<span id="Offline"></span><span id="offline"></span><span id="OFFLINE"></span>

<span id="Offline"></span><span id="offline"></span><span id="OFFLINE"></span>**Offline** (6)


</dt> <dd>

Corresponds to [**CIM\_EnabledLogicalElement.EnabledState**](/previous-versions//cc136818(v=vs.85)) = Enabled but offline.

</dd> <dt>

<span id="Test"></span><span id="test"></span><span id="TEST"></span>

<span id="Test"></span><span id="test"></span><span id="TEST"></span>**Test** (7)


</dt> <dd></dd> <dt>

<span id="Defer"></span><span id="defer"></span><span id="DEFER"></span>

<span id="Defer"></span><span id="defer"></span><span id="DEFER"></span>**Defer** (8)


</dt> <dd></dd> <dt>

<span id="Quiesce"></span><span id="quiesce"></span><span id="QUIESCE"></span>

<span id="Quiesce"></span><span id="quiesce"></span><span id="QUIESCE"></span>**Quiesce** (9)


</dt> <dd>

Corresponds to [**CIM\_EnabledLogicalElement.EnabledState**](/previous-versions//cc136818(v=vs.85)) = Quiesce, Enabled but paused.

</dd> <dt>

<span id="Reboot"></span><span id="reboot"></span><span id="REBOOT"></span>

<span id="Reboot"></span><span id="reboot"></span><span id="REBOOT"></span>**Reboot** (10)


</dt> <dd>

State transition from **Off** or **Saved** to **Running**.

</dd> <dt>

<span id="Reset"></span><span id="reset"></span><span id="RESET"></span>

<span id="Reset"></span><span id="reset"></span><span id="RESET"></span>**Reset** (11)


</dt> <dd>

Reset the virtual machine. Corresponds to [**CIM\_EnabledLogicalElement.EnabledState**](/previous-versions//cc136818(v=vs.85)) = Reset.

</dd> <dt>

<span id="Saving"></span><span id="saving"></span><span id="SAVING"></span>

<span id="Saving"></span><span id="saving"></span><span id="SAVING"></span>**Saving** (32773)


</dt> <dd>

In version 1 (V1) of Hyper-V, corresponds to **EnabledStateSaving**.

</dd> <dt>

<span id="Pausing"></span><span id="pausing"></span><span id="PAUSING"></span>

<span id="Pausing"></span><span id="pausing"></span><span id="PAUSING"></span>**Pausing** (32776)


</dt> <dd>

In version 1 (V1) of Hyper-V, corresponds to **EnabledStatePausing**.

</dd> <dt>

<span id="Resuming"></span><span id="resuming"></span><span id="RESUMING"></span>

<span id="Resuming"></span><span id="resuming"></span><span id="RESUMING"></span>**Resuming** (32777)


</dt> <dd>

In version 1 (V1) of Hyper-V, corresponds to **EnabledStateResuming**. State transition from **Paused** to **Running**.

</dd> <dt>

<span id="FastSaved"></span><span id="fastsaved"></span><span id="FASTSAVED"></span>

<span id="FastSaved"></span><span id="fastsaved"></span><span id="FASTSAVED"></span>**FastSaved** (32779)


</dt> <dd>

Corresponds to **EnabledStateFastSuspend**.

</dd> <dt>

<span id="FastSaving"></span><span id="fastsaving"></span><span id="FASTSAVING"></span>

<span id="FastSaving"></span><span id="fastsaving"></span><span id="FASTSAVING"></span>**FastSaving** (32780)


</dt> <dd>

Corresponds to **EnabledStateFastSuspending**. State transition from **Running** to **FastSaved**.

</dd> </dl>

These values represent critical states:

<dt>

<span id="RunningCritical"></span><span id="runningcritical"></span><span id="RUNNINGCRITICAL"></span>

**RunningCritical** (32781)


</dt> <dd></dd> <dt>

<span id="OffCritical"></span><span id="offcritical"></span><span id="OFFCRITICAL"></span>

**OffCritical** (32782)


</dt> <dd></dd> <dt>

<span id="StoppingCritical"></span><span id="stoppingcritical"></span><span id="STOPPINGCRITICAL"></span>

**StoppingCritical** (32783)


</dt> <dd></dd> <dt>

<span id="SavedCritical"></span><span id="savedcritical"></span><span id="SAVEDCRITICAL"></span>

**SavedCritical** (32784)


</dt> <dd></dd> <dt>

<span id="PausedCritical"></span><span id="pausedcritical"></span><span id="PAUSEDCRITICAL"></span>

**PausedCritical** (32785)


</dt> <dd></dd> <dt>

<span id="StartingCritical"></span><span id="startingcritical"></span><span id="STARTINGCRITICAL"></span>

**StartingCritical** (32786)


</dt> <dd></dd> <dt>

<span id="ResetCritical"></span><span id="resetcritical"></span><span id="RESETCRITICAL"></span>

**ResetCritical** (32787)


</dt> <dd></dd> <dt>

<span id="SavingCritical"></span><span id="savingcritical"></span><span id="SAVINGCRITICAL"></span>

**SavingCritical** (32788)


</dt> <dd></dd> <dt>

<span id="PausingCritical"></span><span id="pausingcritical"></span><span id="PAUSINGCRITICAL"></span>

**PausingCritical** (32789)


</dt> <dd></dd> <dt>

<span id="ResumingCritical"></span><span id="resumingcritical"></span><span id="RESUMINGCRITICAL"></span>

**ResumingCritical** (32790)


</dt> <dd></dd> <dt>

<span id="FastSavedCritical"></span><span id="fastsavedcritical"></span><span id="FASTSAVEDCRITICAL"></span>

**FastSavedCritical** (32791)


</dt> <dd></dd> <dt>

<span id="FastSavingCritical"></span><span id="fastsavingcritical"></span><span id="FASTSAVINGCRITICAL"></span>

**FastSavingCritical** (32792)


</dt> <dd></dd> </dl> </dd> <dt>

*Job* \[out\]
</dt> <dd>

Type: **[**CIM\_ConcreteJob**](/previous-versions//cc136808(v=vs.85))**

An optional reference to a [**Msvm\_ConcreteJob**](msvm-concretejob.md) object that is returned if the operation is executed asynchronously. If present, the returned reference can be used to monitor progress and obtain the result of the method.

</dd> <dt>

*TimeoutPeriod* \[in\]
</dt> <dd>

Type: **datetime**

This parameter is not used.

</dd> </dl>

## Return value

Type: **uint32**

This method returns one of the following values.



| Return code/value                                                                                                                                                                       | Description                                                                        |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| <dl> <dt>**Completed with No Error**</dt> <dt>0</dt> </dl>                           | Success.<br/>                                                                |
| <dl> <dt>**Method Parameters Checked - Transition Started**</dt> <dt>4096</dt> </dl> | The transition is asynchronous.<br/>                                         |
| <dl> <dt>**Access Denied**</dt> <dt>32769</dt> </dl>                                 | Access denied.<br/>                                                          |
| <dl> <dt></dt> <dt>32768</dt> </dl>                                                  |                                                                                    |
| <dl> <dt></dt> <dt>32770</dt> </dl>                                                  |                                                                                    |
| <dl> <dt></dt> <dt>32771</dt> </dl>                                                  |                                                                                    |
| <dl> <dt></dt> <dt>32772</dt> </dl>                                                  |                                                                                    |
| <dl> <dt></dt> <dt>32773</dt> </dl>                                                  |                                                                                    |
| <dl> <dt></dt> <dt>32774</dt> </dl>                                                  |                                                                                    |
| <dl> <dt>**Invalid state for this operation**</dt> <dt>32775</dt> </dl>              | The value specified in the *RequestedState* parameter is not supported.<br/> |
| <dl> <dt></dt> <dt>32776</dt> </dl>                                                  |                                                                                    |
| <dl> <dt></dt> <dt>32777</dt> </dl>                                                  |                                                                                    |
| <dl> <dt></dt> <dt>32778</dt> </dl>                                                  |                                                                                    |



 

## Remarks

Access to the [**Msvm\_ComputerSystem**](msvm-computersystem.md) class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](/windows/desktop/WmiSdk/user-account-control-and-wmi).

## Examples

The following C# example starts or disables a virtual machine. The referenced utilities can be found in [Common utilities for the virtualization samples (V2)](common-utilities-for-the-virtualization-samples-v2.md).

> [!IMPORTANT]
> To function correctly, the following code must be run on the virtual machine host server, and must be run with administrator privileges.

 


```CSharp
using System;
using System.Management;

namespace HyperVSamples
{
    public class RequestStateChangeClass
    {
        public static void RequestStateChange(string vmName, string action)
        {
            ManagementScope scope = new ManagementScope(@"\\.\root\virtualization\v2", null);
            ManagementObject vm = Utility.GetTargetComputer(vmName, scope);

            if (null == vm)
            {
                throw new ArgumentException(
                    string.Format(
                    "The virtual machine '{0}' could not be found.", 
                    vmName));
            }

            ManagementBaseObject inParams = vm.GetMethodParameters("RequestStateChange");

            const int Enabled = 2;
            const int Disabled = 3;

            if (action.ToLower() == "start")
            {
                inParams["RequestedState"] = Enabled;
            }
            else if (action.ToLower() == "stop")
            {
                inParams["RequestedState"] = Disabled;
            }
            else
            {
                throw new Exception("Wrong action is specified");
            }

            ManagementBaseObject outParams = vm.InvokeMethod(
                "RequestStateChange", 
                inParams, 
                null);

            if ((UInt32)outParams["ReturnValue"] == ReturnCode.Started)
            {
                if (Utility.JobCompleted(outParams, scope))
                {
                    Console.WriteLine(
                        "{0} state was changed successfully.", 
                        vmName);
                }
                else
                {
                    Console.WriteLine("Failed to change virtual system state");
                }
            }
            else if ((UInt32)outParams["ReturnValue"] == ReturnCode.Completed)
            {
                Console.WriteLine(
                    "{0} state was changed successfully.", 
                    vmName);
            }
            else
            {
                Console.WriteLine(
                    "Change virtual system state failed with error {0}", 
                    outParams["ReturnValue"]);
            }

        }

        public static void Main(string[] args)
        {
            if (args != null && args.Length != 2)
            {
                Console.WriteLine("Usage: <application> vmName action");
                Console.WriteLine("action: start|stop");
                return;
            }

            RequestStateChange(args[0], args[1]);
        }

    }
}
```



The following Visual Basic Scripting Edition (VBScript) example starts or disables a virtual machine.

> [!IMPORTANT]
> To function correctly, the following code must be run on the virtual machine host server, and must be run with administrator privileges.

 


```VB
dim objWMIService
dim fileSystem

const JobStarting = 3
const JobRunning = 4
const JobCompleted = 7
const wmiStarted = 4096
const Enabled = 2
const Disabled = 3



Main()

'-----------------------------------------------------------------
' Main routine
'-----------------------------------------------------------------
Sub Main()
    set fileSystem = Wscript.CreateObject("Scripting.FileSystemObject")

    strComputer = "."
    set objWMIService = GetObject("winmgmts:\\" & strComputer & "\root\virtualization\v2")

    set objArgs = WScript.Arguments
    if WScript.Arguments.Count = 2 then
       vmName= objArgs.Unnamed.Item(0)
       action = objArgs.Unnamed.Item(1)
    else
       WScript.Echo "usage: cscript StartVM.vbs vmName start|stop"
       WScript.Quit
    end if
    
    set computerSystem = GetComputerSystem(vmName)

    if RequestStateChange(computerSystem, action) then

        WriteLog "Done"
        WScript.Quit(0)
    else
        WriteLog "RequestStateChange failed"
        WScript.Quit(1)
    end if

End Sub

'-----------------------------------------------------------------
' Retrieve Msvm_VirtualComputerSystem from base on its ElementName
' 
'-----------------------------------------------------------------
Function GetComputerSystem(vmElementName)
    On Error Resume Next
    query = Format1("select * from Msvm_ComputerSystem where ElementName = '{0}'", vmElementName)
    set GetComputerSystem = objWMIService.ExecQuery(query).ItemIndex(0)
    if (Err.Number <> 0) then
        WriteLog Format1("Err.Number: {0}", Err.Number)
        WriteLog Format1("Err.Description:{0}",Err.Description)
        WScript.Quit(1)
    end if
End Function


'-----------------------------------------------------------------
' Turn on a virtual machine
'-----------------------------------------------------------------
Function RequestStateChange(computerSystem, action)
    WriteLog Format2("RequestStateChange({0}, {1})", computerSystem.ElementName, action)

    RequestStateChange = false
    set objInParam = computerSystem.Methods_("RequestStateChange").InParameters.SpawnInstance_()
    
    if action = "start" then
        objInParam.RequestedState = Enabled
    else
        objInParam.RequestedState = Disabled
    end if

    set objOutParams = computerSystem.ExecMethod_("RequestStateChange", objInParam)

    if (WMIMethodStarted(objOutParams)) then
        if (WMIJobCompleted(objOutParams)) then
            WriteLog Format1("VM {0} was started successfully", computerSystem.ElementName)
            RequestStateChange = true
        end if
    end if

End Function


'-----------------------------------------------------------------
' Handle wmi return values
'-----------------------------------------------------------------
Function WMIMethodStarted(outParam)

    WMIMethodStarted = false

    if Not IsNull(outParam) then
        wmiStatus = outParam.ReturnValue

        if  wmiStatus = wmiStarted then
            WMIMethodStarted = true
        end if

    end if

End Function


'-----------------------------------------------------------------
' Handle wmi Job object
'-----------------------------------------------------------------
Function WMIJobCompleted(outParam)
    dim WMIJob

    set WMIJob = objWMIService.Get(outParam.Job)

    WMIJobCompleted = true

    jobState = WMIJob.JobState

    while jobState = JobRunning or jobState = JobStarting

        WScript.Sleep(1000)
        set WMIJob = objWMIService.Get(outParam.Job)
        jobState = WMIJob.JobState

    wend


    if (jobState <> JobCompleted) then
        WriteLog Format1("ErrorDescription:{0}", WMIJob.ErrorDescription)
        WMIJobCompleted = false
    end if

End Function

'-----------------------------------------------------------------
' Create the console log files.
'-----------------------------------------------------------------
Sub WriteLog(line)
    dim fileStream
    set fileStream = fileSystem.OpenTextFile(".\StartVM.log", 8, true)
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



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**Msvm\_ComputerSystem**](msvm-computersystem.md)
</dt> </dl>

 

