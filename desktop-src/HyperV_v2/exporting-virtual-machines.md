---
description: The following C# and Visual Basic Scripting Edition (VBScript) samples demonstrate exporting a snapshot of a virtual machine.
ms.assetid: 4DEC4962-99E1-42BB-81B1-8530BF9C4B92
title: Exporting a snapshot of a virtual machine
ms.topic: article
ms.date: 05/31/2018
---

# Exporting a snapshot of a virtual machine

The following C# and Visual Basic Scripting Edition (VBScript) samples demonstrate exporting a snapshot of a virtual machine. Samples that demonstrate exporting a virtual machine can be found on the [**ExportSystemDefinition**](exportsystemdefinition-msvm-virtualsystemmanagementservice.md) topic.

The referenced C# utilities can be found in [Common utilities for the virtualization samples (V2)](common-utilities-for-the-virtualization-samples-v2.md).


```CSharp
using System;
using System.IO;
using System.Management;

namespace HyperVSamples
{
    class ExportSystemDefinitionSnapshotsClass
    {

        static ManagementObject GetLastVirtualSystemSnapshot(ManagementObject vm)
        {
            ManagementObjectCollection settings = vm.GetRelated(
                "Msvm_VirtualSystemSettingData",
                "Msvm_MostCurrentSnapshotInBranch",
                null,
                null,
                "Dependent",
                "Antecedent",
                false,
                null);


            ManagementObject virtualSystemsetting = null;
            foreach (ManagementObject setting in settings)
            {
                Console.WriteLine(setting.Path.Path);
                Console.WriteLine(setting["ElementName"]);
                virtualSystemsetting = setting;
            }
            return virtualSystemsetting;
        }


        static string GetVirtualSystemExportSettingDataInstance(ManagementScope scope, ManagementObject snapshotSettingData)
        {
            ManagementPath settingPath = new ManagementPath("Msvm_VirtualSystemExportSettingData");

            ManagementClass exportSettingDataClass = new ManagementClass(scope, settingPath, null);
            ManagementObject exportSettingData = exportSettingDataClass.CreateInstance();

            exportSettingData["CopySnapshotConfiguration"] = 2;
            exportSettingData["CreateVmExportSubdirectory"] = true;
            exportSettingData["SnapshotVirtualSystem"] = snapshotSettingData.Path.Path;

            string settingData = exportSettingData.GetText(TextFormat.CimDtd20);

            exportSettingData.Dispose();
            exportSettingDataClass.Dispose();

            return settingData;
        }


        static void ExportSystemDefinitionSnapshots(string vmName, string exportDirectory)
        {
            ManagementScope scope = new ManagementScope(@"root\virtualization\v2", null);
            ManagementObject virtualSystemService = Utility.GetServiceObject(scope, "Msvm_VirtualSystemManagementService");

            ManagementBaseObject inParams = virtualSystemService.GetMethodParameters("ExportSystemDefinition");

            ManagementObject vm = Utility.GetTargetComputer(vmName, scope);
            ManagementObject snapshotSettingData = GetLastVirtualSystemSnapshot(vm);

            if ( snapshotSettingData == null )
            {
                Console.WriteLine("There are not snapshots in the VM to be exported...");
                return;
            }

            inParams["ComputerSystem"] = vm.Path.Path;
            
            if (!Directory.Exists(exportDirectory))
            {
                Directory.CreateDirectory(exportDirectory);
            }
            inParams["ExportDirectory"] = exportDirectory;
            inParams["ExportSettingData"] = GetVirtualSystemExportSettingDataInstance(scope, snapshotSettingData);

            ManagementBaseObject outParams = virtualSystemService.InvokeMethod("ExportSystemDefinition", inParams, null);

            if ((UInt32)outParams["ReturnValue"] == ReturnCode.Started)
            {
                if (Utility.JobCompleted(outParams, scope))
                {
                    Console.WriteLine("VM '{0}' were exported successfully.", vm["ElementName"]);
                }
                else
                {
                    Console.WriteLine("Failed to export VM");
                }
            }
            else if ((UInt32)outParams["ReturnValue"] == ReturnCode.Completed)
            {
                Console.WriteLine("VM '{0}' were exported successfully.", vm["ElementName"]);
            }
            else
            {
                Console.WriteLine("Export virtual system failed with error:{0}", outParams["ReturnValue"]);
            }

            inParams.Dispose();
            outParams.Dispose();
            vm.Dispose();
            virtualSystemService.Dispose();
        }

        static void Main(string[] args)
        {
            if (args != null && args.Length != 2)
            {
                Console.WriteLine("Usage: ExportSystemDefinitionSnapshots vmName exportDirectory");
                return;
            }
            ExportSystemDefinitionSnapshots(args[0], args[1]);
        }
    }
}
```


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

    dim computer, objArgs, vmName, vm, exportDirectory
    
    set fileSystem = Wscript.CreateObject("Scripting.FileSystemObject")
    computer = "."
    set objWMIService = GetObject("winmgmts:\\" & computer & "\root\virtualization\v2")
    set managementService = objWMIService.ExecQuery("select * from Msvm_VirtualSystemManagementService").ItemIndex(0)
    
    set objArgs = WScript.Arguments
    if WScript.Arguments.Count = 2 then
        vmName = objArgs.Unnamed.Item(0)
        exportDirectory = objArgs.Unnamed.Item(1)
    else
        WScript.Echo "usage: cscript ExportSystemDefinitionSnapshots.vbs vmName exportDirectoryName"
        WScript.Quit(1)
    end if
    
    set vm = GetComputerSystem(vmName)

    if ExportSystemDefinitionSnapshots(vm, exportDirectory) then
        WriteLog "Done"
        WScript.Quit(0)
    else
        WriteLog "ExportSystemDefinitionSnapshots Failed."
        WScript.Quit(1)
    end if
End Sub

'-----------------------------------------------------------------
' Retrieve Msvm_VirtualComputerSystem from base on its ElementName
'-----------------------------------------------------------------
Function GetComputerSystem(vmElementName)
    On Error Resume Next
    dim query
    query = Format1("select * from Msvm_ComputerSystem where ElementName = '{0}'", vmElementName)
    set GetComputerSystem = objWMIService.ExecQuery(query).ItemIndex(0)
    if (Err.Number <> 0) then
        WriteLog Format1("Err.Number: {0}", Err.Number)
        WriteLog Format1("Err.Description:{0}",Err.Description)
        WScript.Quit(1)
    end if
End Function

'-----------------------------------------------------------------
' Get Last Snapshot of a Virtual System
'-----------------------------------------------------------------
Function GetLastVirtualSystemSnapshot(computerSystem, snapshot)

    dim objVSSDs, vssd
    dim query 

    GetLastVirtualSystemSnapshot = false

    query = Format1("ASSOCIATORS OF {{0}} WHERE resultClass = Msvm_VirtualSystemsettingData", computerSystem.Path_.Path)
    set objVSSDs = objWMIService.ExecQuery(query)
    
    for each vssd in objVSSDs
    if vssd.SettingType = 5 then 'SettingType = 5 means it is a snapshot
            GetLastVirtualSystemSnapshot = true
        set snapshot = vssd
    end if
    next
End Function

'-----------------------------------------------------------------
' Export a virtual system
'-----------------------------------------------------------------
Function ExportSystemDefinitionSnapshots(computerSystem, exportDirectory)

    dim objInParam, objOutParams 
    dim query
    dim computer
    dim exportSettingData
    dim lastSnapshot
    dim isSnapshotPresent

    ExportSystemDefinitionSnapshots = false
    
    if Not fileSystem.FolderExists(exportDirectory) then
        fileSystem.CreateFolder(exportDirectory)
    end if
    
    set objInParam = managementService.Methods_("ExportSystemDefinition").InParameters.SpawnInstance_()
    objInParam.ComputerSystem = computerSystem.Path_.Path

    query = Format1("ASSOCIATORS OF {{0}} WHERE resultClass = Msvm_VirtualSystemExportSettingData", computerSystem.Path_.Path)
    set exportSettingData = objWMIService.ExecQuery(query).ItemIndex(0)
    exportSettingData.CopyVmStorage = true
    exportSettingData.CopyVmRuntimeInformation = true
    exportSettingData.CreateVmExportSubdirectory = true
    exportSettingData.CopySnapshotConfiguration = 2
    isSnapshotPresent = GetLastVirtualSystemSnapshot(computerSystem, lastSnapshot)
    if isSnapshotPresent = false then
        WriteLog "No snapshots were found on the VM when trying to export snapshot as VM."
        ExportSystemDefinitionSnapshots = false
    Exit Function
    end if

    exportSettingData.SnapshotVirtualSystem = lastSnapshot.Path_.Path
    objInParam.ExportSettingData = exportSettingData.GetText_(1)

    objInParam.ExportDirectory = exportDirectory
    
    set objOutParams = managementService.ExecMethod_("ExportSystemDefinition", objInParam)

    if objOutParams.ReturnValue = wmiStarted then
        if (WMIJobCompleted(objOutParams)) then
            ExportSystemDefinitionSnapshots = true
        end if
    elseif (objOutParams.ReturnValue = wmiSuccessful) then
        ExportSystemDefinitionSnapshots = true
    else
        WriteLog Format1("ExportSystemDefinitionSnapshots failed with ReturnValue {0}", objOutParams.ReturnValue)
    end if

End Function

'-----------------------------------------------------------------
' Handle wmi Job object
'-----------------------------------------------------------------
Function WMIJobCompleted(outParam)
    
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
    set fileStream = fileSystem.OpenTextFile(".\ExportSystemDefinition-ExportSnapshot.log", 8, true)
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





## Related topics

[Exporting the configuration of a virtual machine](exporting-the-configuration-of-a-virtual-machine.md)

[**ExportSystemDefinition**](exportsystemdefinition-msvm-virtualsystemmanagementservice.md)
