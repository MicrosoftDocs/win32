---
title: DefineVirtualSystem method of the Msvm\_VirtualSystemManagementService class
description: Creates a new virtual computer system instance.
ms.assetid: beade060-2495-4a21-be74-0a710276521b
keywords:
- DefineVirtualSystem method Hyper-V
- DefineVirtualSystem method Hyper-V , Msvm_VirtualSystemManagementService class
- Msvm_VirtualSystemManagementService class Hyper-V , DefineVirtualSystem method
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemManagementService.DefineVirtualSystem
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

# DefineVirtualSystem method of the Msvm\_VirtualSystemManagementService class

Creates a new virtual computer system instance. Properties that are not specified will be populated with default values.

## Syntax


```mof
uint32 DefineVirtualSystem(
  [in]  string                           SystemSettingData,
  [in]  string                           ResourceSettingData[],
  [in]  CIM_VirtualSystemSettingData REF SourceSetting,
  [out] CIM_ComputerSystem           REF DefinedSystem,
  [out] CIM_ConcreteJob              REF Job
);
```



## Parameters

<dl> <dt>

*SystemSettingData* \[in\]
</dt> <dd>

Type: **string**

An embedded instance of the [**Msvm\_VirtualSystemGlobalSettingData**](msvm-virtualsystemglobalsettingdata.md) class. This parameter is required.

</dd> <dt>

*ResourceSettingData* \[in\]
</dt> <dd>

Type: **string\[\]**

An optional parameter that contains a number of embedded instances of the [**Msvm\_ResourceAllocationSettingData**](msvm-resourceallocationsettingdata.md) class (or derived classes thereof). Together these instances describe the virtual resources of the virtual computer system. A default set of devices will be created for the virtual system regardless of whether this parameter is set. For example, processor and memory are automatically created and configured with default values.

</dd> <dt>

*SourceSetting* \[in\]
</dt> <dd>

Type: **CIM\_VirtualSystemSettingData**

A reference to an existing instance of [**Msvm\_VirtualSystemSettingData**](msvm-virtualsystemsettingdata.md) to use as a template for the new virtual computer system. The settings described in this object, as well as those in the associated [**Msvm\_ResourceAllocationSettingData**](msvm-resourceallocationsettingdata.md) instances (via the [**Msvm\_VirtualSystemSettingDataComponent**](msvm-virtualsystemsettingdatacomponent.md) association), will be reflected in the new virtual computer system.

</dd> <dt>

*DefinedSystem* \[out\]
</dt> <dd>

Type: **CIM\_ComputerSystem**

A reference to the newly created virtual computer system.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

Type: **CIM\_ConcreteJob**

An optional reference that is returned if the operation is executed asynchronously. If present, the returned reference to an instance of [**Msvm\_ConcreteJob**](msvm-concretejob.md) can be used to monitor progress and to obtain the result of the method.

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

The following C# sample creates a virtual system. The referenced utilities can be found in [Common Utilities for the Virtualization Samples](common-utilities-for-the-virtualization-samples.md).

> \[!Important\]  
> To function correctly, the following code must be run on the VM host server, and must be run with Administrator privileges.

 


```CSharp
using System;
using System.Management;

namespace HyperVSamples
{
    class DefineVirtualSystemClass
    {
        static string GetVirtualSystemGlobalSettingDataInstance(ManagementScope scope)
        {
            ManagementPath settingPath = new ManagementPath("Msvm_VirtualSystemGlobalsettingData");

            ManagementClass globalSettingClass = new ManagementClass(scope, settingPath, null);
            ManagementObject globalSettingData = globalSettingClass.CreateInstance();
            globalSettingData["ElementName"] = "My First VM";

            string settingData = globalSettingData.GetText(TextFormat.CimDtd20);

            globalSettingData.Dispose();
            globalSettingClass.Dispose();

            return settingData;
        }

        static ManagementObject DefineVirtualSystem(string vmName)
        {
            ManagementObject definedSystem = null;
            ManagementScope scope = new ManagementScope(@"root\virtualization", null);
            ManagementObject virtualSystemService = Utility.GetServiceObject(scope, "Msvm_VirtualSystemManagementService");

            ManagementBaseObject inParams = virtualSystemService.GetMethodParameters("DefineVirtualSystem");
            inParams["ResourcesettingData"] = null;
            inParams["Sourcesetting"] = null;
            inParams["SystemsettingData"] = GetVirtualSystemGlobalSettingDataInstance(scope);

            ManagementBaseObject outParams = virtualSystemService.InvokeMethod("DefineVirtualSystem", inParams, null);

            if ((UInt32)outParams["ReturnValue"] == ReturnCode.Started)
            {
                if (Utility.JobCompleted(outParams, scope))
                {
                    definedSystem = new ManagementObject(outParams["DefinedSystem"].ToString());
                    Console.WriteLine("{0} was created successfully.", definedSystem["ElementName"]);
                }
                else
                {
                    Console.WriteLine("Failed to define virtual system");
                }
            }
            else if ((UInt32)outParams["ReturnValue"] == ReturnCode.Completed)
            {
                definedSystem = new ManagementObject(outParams["DefinedSystem"].ToString());
                Console.WriteLine("{0} was created successfully.", definedSystem["ElementName"]);
            }
            else
            {
                Console.WriteLine("Define virtual system failed with error {0}", outParams["ReturnValue"]);
            }

            inParams.Dispose();
            outParams.Dispose();
            virtualSystemService.Dispose();

            return definedSystem;
        }

        static void Main(string[] args)
        {
            if (args != null &amp;&amp; args.Length != 1)
            {
                Console.WriteLine("Usage: CreateVirtualSystemSnapshot vmName");
                return;
            }
            DefineVirtualSystem(args[0]);
        }
    }
}
```



The following VBScript sample creates a virtual system.

> \[!Important\]  
> To function correctly, the following code must be run on the VM host server, and must be run with Administrator privileges.

 


```VB
option explicit 

dim objWMIService
dim managementService
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
    
    dim computer, objArgs, vmName
    set fileSystem = Wscript.CreateObject("Scripting.FileSystemObject")
    computer = "."
    set objWMIService = GetObject("winmgmts:\\" & computer & "\root\virtualization")
    set managementService = objWMIService.ExecQuery("select * from Msvm_VirtualSystemManagementService").ItemIndex(0)

    set objArgs = WScript.Arguments
    if WScript.Arguments.Count = 1 then
        vmName = objArgs.Unnamed.Item(0)
    else
        WScript.Echo "usage: cscript DefineVirtualSystem.vbs vmName"
        WScript.Quit(1)
    end if

    if DefineVirtualSystem(vmName) then
        WriteLog "Done"
        WScript.Quit(0)
    else
        WriteLog "DefineVirtualSystem failed."
        WScript.Quit(1)
    end if

End Sub

'-----------------------------------------------------------------
' Define a virtual system
'-----------------------------------------------------------------
Function DefineVirtualSystem(vmName)

    dim globalsettingData, objInParam, objOutParams, wmiStatus
    
    DefineVirtualSystem = false
    set globalsettingData = objWMIService.Get("Msvm_VirtualSystemGlobalsettingData").SpawnInstance_()
    globalsettingData.ElementName = vmName
    set objInParam = managementService.Methods_("DefineVirtualSystem").InParameters.SpawnInstance_()
    objInParam.ResourcesettingData = null
    objInParam.Sourcesetting = null
    objInParam.SystemsettingData = globalsettingData.GetText_(1)
    
    set objOutParams = managementService.ExecMethod_("DefineVirtualSystem", objInParam)
    
    wmiStatus = objOutParams.ReturnValue

    if objOutParams.ReturnValue = wmiStarted then
        if (WMIJobCompleted(objOutParams)) then
            DefineVirtualSystem = true
        end if
    elseif (objOutParams.ReturnValue = wmiSuccessful) then
        DefineVirtualSystem = true
    else
        WriteLog Format1("DefineVirtualSystem failed with ReturnValue {0}", objOutParams.ReturnValue)
    end if

End Function

'-----------------------------------------------------------------
' Handle wmi Job object
'-----------------------------------------------------------------
Function WMIJobCompleted(outParam)
    WriteLog "Function WMIJobCompleted"
    
    dim WMIJob, jobState

    set WMIJob = objWMIService.Get(outParam.Job)

    WMIJobCompleted = true

    jobState = WMIJob.JobState

    while jobState = JobRunning or jobState = JobStarting
        WriteLog Format1("In progress... {0}% completed.",WMIJob.PercentComplete)
        WScript.Sleep(1000)
        set WMIJob = objWMIService.Get(outParam.Job)
        jobState = WMIJob.JobState
    wend

    if (jobState <> JobCompleted) then
        WriteLog Format1("ErrorCode:{0}", WMIJob.ErrorCode)
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

[**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md)
</dt> </dl>

 

 





