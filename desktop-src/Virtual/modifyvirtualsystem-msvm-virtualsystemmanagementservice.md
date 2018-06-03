---
title: ModifyVirtualSystem method of the Msvm\_VirtualSystemManagementService class
description: Modifies the settings for an existing virtual computer system.
ms.assetid: a002cac7-f441-4427-ba04-790a470c9985
keywords:
- ModifyVirtualSystem method Hyper-V
- ModifyVirtualSystem method Hyper-V , Msvm_VirtualSystemManagementService class
- Msvm_VirtualSystemManagementService class Hyper-V , ModifyVirtualSystem method
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemManagementService.ModifyVirtualSystem
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

# ModifyVirtualSystem method of the Msvm\_VirtualSystemManagementService class

Modifies the settings for an existing virtual computer system.

## Syntax


```mof
uint32 ModifyVirtualSystem(
  [in]  CIM_ComputerSystem           REF ComputerSystem,
  [in]  string                           SystemSettingData,
  [out] CIM_VirtualSystemSettingData REF ModifiedSettingData,
  [out] CIM_ConcreteJob              REF Job
);
```



## Parameters

<dl> <dt>

*ComputerSystem* \[in\]
</dt> <dd>

Type: **CIM\_ComputerSystem**

A reference to the virtual computer system to be modified.

</dd> <dt>

*SystemSettingData* \[in\]
</dt> <dd>

Type: **string**

An embedded instance of the [**CIM\_VirtualSystemSettingData**](https://msdn.microsoft.com/library/cc136954) class that describes the modified setting values for the virtual computer system.

</dd> <dt>

*ModifiedSettingData* \[out\]
</dt> <dd>

Type: **CIM\_VirtualSystemSettingData**

A reference to the [**CIM\_VirtualSystemSettingData**](https://msdn.microsoft.com/library/cc136954) instance that represents the object that was modified.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

Type: **CIM\_ConcreteJob**

An optional reference that is returned if the operation is executed asynchronously. If present, the returned reference to an instance of [**CIM\_ConcreteJob**](https://msdn.microsoft.com/library/cc136808) can be used to monitor progress and to obtain the result of the method.

</dd> </dl>

## Return value

Type: **uint32**

If this method is executed synchronously, it returns 0 if it succeeds. If this method is executed asynchronously, it returns 4096 and the *Job* output parameter can be used to track the progress of the asynchronous operation. Any other return value indicates an error.

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

Access to the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Examples

The following C# sample modifies the settings for a virtual system. The referenced utilities can be found in [Common Utilities for the Virtualization Samples](common-utilities-for-the-virtualization-samples.md).

> \[!Important\]  
> To function correctly, the following code must be run on the VM host server, and must be run with Administrator privileges.

 


```CSharp
using System;
using System.Management;

namespace HyperVSamples
{
    class ModifyVirtualSystemClass
    {
        static void ModifyVirtualSystem(string vmName, string vmNewName)
        {
            ManagementScope scope = new ManagementScope(@"root\virtualization", null);
            ManagementObject virtualSystemService = Utility.GetServiceObject(scope, "Msvm_VirtualSystemManagementService");

            ManagementBaseObject inParams = virtualSystemService.GetMethodParameters("ModifyVirtualSystem");

            ManagementObject vm = Utility.GetTargetComputer(vmName, scope);
            inParams["ComputerSystem"] = vm.Path.Path;

            ManagementObject           settingData  = null;
            ManagementObjectCollection settingsData = vm.GetRelated( "Msvm_VirtualSystemSettingData",
                                                                     "Msvm_SettingsDefineState",
                                                                     null,
                                                                     null,
                                                                     "SettingData",
                                                                     "ManagedElement",
                                                                     false,
                                                                     null);

            foreach (ManagementObject data in settingsData)
            {
                settingData = data;
            }

            settingData["ElementName"] = vmNewName;

            inParams["SystemsettingData"] = settingData.GetText(TextFormat.CimDtd20);

            ManagementBaseObject outParams = virtualSystemService.InvokeMethod("ModifyVirtualSystem", inParams, null);

            if ((UInt32)outParams["ReturnValue"] == ReturnCode.Started)
            {
                if (Utility.JobCompleted(outParams, scope))
                {
                    Console.WriteLine("VM '{0}' was renamed successfully.", vm["ElementName"]);

                }
                else
                {
                    Console.WriteLine("Failed to Modify VM");
                }
            }
            else if ((UInt32)outParams["ReturnValue"] == ReturnCode.Completed)
            {
                Console.WriteLine("VM '{0}' was renamed successfully.", vm["ElementName"]);
            }
            else
            {
                Console.WriteLine("Failed to modify VM. Error {0}", outParams["ReturnValue"]);
            }

            inParams.Dispose();
            outParams.Dispose();
            vm.Dispose();
            virtualSystemService.Dispose();
        }

        static void Main(string[] args)
        {
            if (args != null &amp;&amp; args.Length != 2)
            {
                Console.WriteLine("Usage: ModifyVirtualSystem vmName vmNewName");
                return;
            }
            ModifyVirtualSystem(args[0], args[1]);
        }
    }
}
```



The following VBScript sample modifies the settings for a virtual system.

> \[!Important\]  
> To function correctly, the following code must be run on the VM host server, and must be run with Administrator privileges.

 


```VB
dim objWMIService
dim managementService
dim fileSystem


const JobStarting = 3
const JobRunning = 4
const JobCompleted = 7
const wmiStarted = 4096
const wmiSuccessful = 0
const Saved = 32769

'VM Operational Status
const VMRunning = 2
const VMStopped = 10
const VMSaved = 15

Main()


'-----------------------------------------------------------------
' Main
'-----------------------------------------------------------------
Sub Main()
    set fileSystem = Wscript.CreateObject("Scripting.FileSystemObject")
    strComputer = "."
    set objWMIService = GetObject("winmgmts:\\" & strComputer & "\root\virtualization")
    GetManagmentServiceInstance
    set MyFirstVM = GetComputerSystem("My first VM")

    if ModifyVirtualSystem(MyFirstVM) then
        WriteLog "Done"
        WScript.Quit(0)
    else
        WriteLog "Failed"
        WScript.Quit(1)
    end if
End Sub


'-----------------------------------------------------------------
' Retrieve Msvm_VirtualSystemManagementService from WMI
'-----------------------------------------------------------------
Sub GetManagmentServiceInstance()
    query = "select * from Msvm_VirtualSystemManagementService"
    set managementService = objWMIService.ExecQuery(query).ItemIndex(0)
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
' Modify a virtual system
'-----------------------------------------------------------------
Function ModifyVirtualSystem(computerSystem)

    ModifyVirtualSystem = false
    set objInParam = managementService.Methods_("ModifyVirtualSystem").InParameters.SpawnInstance_()
    
    query = Format1("ASSOCIATORS OF {{0}} WHERE AssocClass = Msvm_SettingsDefineState resultClass = Msvm_VirtualSystemsettingData", computerSystem.Path_.Path)
    set virtualSystemsetting = objWMIService.ExecQuery(query).ItemIndex(0)
    virtualSystemsetting.ElementName = "Renamed VM"
    
    objInParam.ComputerSystem = computerSystem.Path_.Path
    objInParam.SystemsettingData = virtualSystemsetting.GetText_(1)
    
    set objOutParams = managementService.ExecMethod_("ModifyVirtualSystem", objInParam)

    if (WMIMethodStarted(objOutParams)) then
        if (WMIJobCompleted(objOutParams)) then
            ModifyVirtualSystem = true
        end if
    else
        if (wmiStatus = wmiSuccessful) then
            ModifyVirtualSystem = true
        else
            WriteLog Format1("ModifyVirtualSystem failed with ReturnValue {0}", wmiStatus)
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
        WriteLog Format1("WMI API return code: {0}", wmiStatus)

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
    WMIJobCompleted = true

    set WMIJob = objWMIService.Get(outParam.Job)

    while jobState = JobRunning or jobState = JobStarting

        WScript.Sleep(1000)
        set WMIJob = objWMIService.Get(outParam.Job)

    wend

    if (WMIJob.JobState <> JobCompleted) then
        WriteLog Format1("ErrorDescription:{0}", WMIJob.ErrorDescription)
        WMIJobCompleted = false
    end if

End Function

'-----------------------------------------------------------------
' Create the console log files.
'-----------------------------------------------------------------
Sub WriteLog(line)
    dim fileStream
    set fileStream = fileSystem.OpenTextFile(".\ADDSCSIContoller.log", 8, true)
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

[**ModifySystemSettings (V2)**](https://msdn.microsoft.com/library/windows/desktop/hh850104)
</dt> <dt>

[**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md)
</dt> </dl>

 

 





