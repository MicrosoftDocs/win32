---
title: Exporting a Snapshot of a Virtual Machine
description: The following C\ and VBScript samples demonstrate exporting a snapshot of a virtual machine (VM).
ms.assetid: 45429c07-ab31-487f-863c-994e92d5a626
keywords:
- Exporting Virtual Machines Hyper-V
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Exporting a Snapshot of a Virtual Machine

The following C# and VBScript samples demonstrate exporting a snapshot of a virtual machine (VM). Samples that demonstrate exporting a virtual machine can be found on the [**ExportVirtualSystemEx**](msvm-virtualsystemmanagementservice-exportvirtualsystemex.md) topic.

**C#:** The referenced utilities can be found in [Common Utilities for the Virtualization Samples](common-utilities-for-the-virtualization-samples.md).


```CSharp
using System;
using System.IO;
using System.Management;

namespace HyperVSamples
{
    class ExportVirtualSystemExSnapshotsClass
    {

        static ManagementObject GetLastVirtualSystemSnapshot(ManagementObject vm)
        {
            ManagementObjectCollection settings = vm.GetRelated(
                "Msvm_VirtualSystemsettingData",
                "Msvm_PreviousSettingData",
                null,
                null,
                "SettingData",
                "ManagedElement",
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


        static void ExportVirtualSystemExSnapshots(string vmName, string exportDirectory)
        {
            ManagementScope scope = new ManagementScope(@"root\virtualization", null);
            ManagementObject virtualSystemService = Utility.GetServiceObject(scope, "Msvm_VirtualSystemManagementService");

            ManagementBaseObject inParams = virtualSystemService.GetMethodParameters("ExportVirtualSystemEx");

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

            ManagementBaseObject outParams = virtualSystemService.InvokeMethod("ExportVirtualSystemEx", inParams, null);

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
            if (args != null &amp;&amp; args.Length != 2)
            {
                Console.WriteLine("Usage: ExportVirtualSystemExSnapshots vmName exportDirectory");
                return;
            }
            ExportVirtualSystemExSnapshots(args[0], args[1]);
        }
    }
}
```

<span codelanguage="VisualBasic"></span>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>VB</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>option explicit 

dim objWMIService
dim managementService
dim fileSystem

const JobStarting = 3
const JobRunning = 4
const JobCompleted = 7
const wmiStarted = 4096
const wmiSuccessful = 0

Main()


&#39;-----------------------------------------------------------------
&#39; Main
&#39;-----------------------------------------------------------------
Sub Main()

    dim computer, objArgs, vmName, vm, exportDirectory
    
    set fileSystem = Wscript.CreateObject(&quot;Scripting.FileSystemObject&quot;)
    computer = &quot;.&quot;
    set objWMIService = GetObject(&quot;winmgmts:\\&quot; &amp; computer &amp; &quot;\root\virtualization&quot;)
    set managementService = objWMIService.ExecQuery(&quot;select * from Msvm_VirtualSystemManagementService&quot;).ItemIndex(0)
    
    set objArgs = WScript.Arguments
    if WScript.Arguments.Count = 2 then
        vmName = objArgs.Unnamed.Item(0)
        exportDirectory = objArgs.Unnamed.Item(1)
    else
        WScript.Echo &quot;usage: cscript ExportVirtualSystemExSnapshots.vbs vmName exportDirectoryName&quot;
        WScript.Quit(1)
    end if
    
    set vm = GetComputerSystem(vmName)

    if ExportVirtualSystemExSnapshots(vm, exportDirectory) then
        WriteLog &quot;Done&quot;
        WScript.Quit(0)
    else
        WriteLog &quot;ExportVirtualSystemExSnapshots Failed.&quot;
        WScript.Quit(1)
    end if
End Sub

&#39;-----------------------------------------------------------------
&#39; Retrieve Msvm_VirtualComputerSystem from base on its ElementName
&#39;-----------------------------------------------------------------
Function GetComputerSystem(vmElementName)
    On Error Resume Next
    dim query
    query = Format1(&quot;select * from Msvm_ComputerSystem where ElementName = &#39;{0}&#39;&quot;, vmElementName)
    set GetComputerSystem = objWMIService.ExecQuery(query).ItemIndex(0)
    if (Err.Number &lt;&gt; 0) then
        WriteLog Format1(&quot;Err.Number: {0}&quot;, Err.Number)
        WriteLog Format1(&quot;Err.Description:{0}&quot;,Err.Description)
        WScript.Quit(1)
    end if
End Function

&#39;-----------------------------------------------------------------
&#39; Get Last Snapshot of a Virtual System
&#39;-----------------------------------------------------------------
Function GetLastVirtualSystemSnapshot(computerSystem, snapshot)

    dim objVSSDs, vssd
    dim query 

    GetLastVirtualSystemSnapshot = false

    query = Format1(&quot;ASSOCIATORS OF {{0}} WHERE resultClass = Msvm_VirtualSystemsettingData&quot;, computerSystem.Path_.Path)
    set objVSSDs = objWMIService.ExecQuery(query)
    
    for each vssd in objVSSDs
    if vssd.SettingType = 5 then &#39;SettingType = 5 means it is a snapshot
            GetLastVirtualSystemSnapshot = true
        set snapshot = vssd
    end if
    next
End Function

&#39;-----------------------------------------------------------------
&#39; Export a virtual system
&#39;-----------------------------------------------------------------
Function ExportVirtualSystemExSnapshots(computerSystem, exportDirectory)

    dim objInParam, objOutParams 
    dim query
    dim computer
    dim exportSettingData
    dim lastSnapshot
    dim isSnapshotPresent

    ExportVirtualSystemExSnapshots = false
    
    if Not fileSystem.FolderExists(exportDirectory) then
        fileSystem.CreateFolder(exportDirectory)
    end if
    
    set objInParam = managementService.Methods_(&quot;ExportVirtualSystemEx&quot;).InParameters.SpawnInstance_()
    objInParam.ComputerSystem = computerSystem.Path_.Path

    query = Format1(&quot;ASSOCIATORS OF {{0}} WHERE resultClass = Msvm_VirtualSystemExportSettingData&quot;, computerSystem.Path_.Path)
    set exportSettingData = objWMIService.ExecQuery(query).ItemIndex(0)
    exportSettingData.CopyVmStorage = true
    exportSettingData.CopyVmRuntimeInformation = true
    exportSettingData.CreateVmExportSubdirectory = true
    exportSettingData.CopySnapshotConfiguration = 2
    isSnapshotPresent = GetLastVirtualSystemSnapshot(computerSystem, lastSnapshot)
    if isSnapshotPresent = false then
        WriteLog &quot;No snapshots were found on the VM when trying to export snapshot as VM.&quot;
        ExportVirtualSystemExSnapshots = false
    Exit Function
    end if

    exportSettingData.SnapshotVirtualSystem = lastSnapshot.Path_.Path
    objInParam.ExportSettingData = exportSettingData.GetText_(1)

    objInParam.ExportDirectory = exportDirectory
    
    set objOutParams = managementService.ExecMethod_(&quot;ExportVirtualSystemEx&quot;, objInParam)

    if objOutParams.ReturnValue = wmiStarted then
        if (WMIJobCompleted(objOutParams)) then
            ExportVirtualSystemExSnapshots = true
        end if
    elseif (objOutParams.ReturnValue = wmiSuccessful) then
        ExportVirtualSystemExSnapshots = true
    else
        WriteLog Format1(&quot;ExportVirtualSystemExSnapshots failed with ReturnValue {0}&quot;, objOutParams.ReturnValue)
    end if

End Function

&#39;-----------------------------------------------------------------
&#39; Handle wmi Job object
&#39;-----------------------------------------------------------------
Function WMIJobCompleted(outParam)
    
    dim WMIJob, jobState

    set WMIJob = objWMIService.Get(outParam.Job)

    WMIJobCompleted = true

    jobState = WMIJob.JobState

    while jobState = JobRunning or jobState = JobStarting
        WriteLog Format1(&quot;In progress... {0}% completed.&quot;,WMIJob.PercentComplete)
        WScript.Sleep(1000)
        set WMIJob = objWMIService.Get(outParam.Job)
        jobState = WMIJob.JobState
    wend

    if (jobState &lt;&gt; JobCompleted) then
        WriteLog Format1(&quot;ErrorCode:{0}&quot;, WMIJob.ErrorCode)
        WriteLog Format1(&quot;ErrorDescription:{0}&quot;, WMIJob.ErrorDescription)
        WMIJobCompleted = false
    end if

End Function

&#39;-----------------------------------------------------------------
&#39; Create the console log files.
&#39;-----------------------------------------------------------------
Sub WriteLog(line)
    dim fileStream
    set fileStream = fileSystem.OpenTextFile(&quot;.\ExportVirtualSystemEx-ExportSnapshot.log&quot;, 8, true)
    WScript.Echo line
    fileStream.WriteLine line
    fileStream.Close

End Sub

&#39;------------------------------------------------------------------------------
&#39; The string formatting functions to avoid string concatenation.
&#39;------------------------------------------------------------------------------
Function Format2(myString, arg0, arg1)
    Format2 = Format1(myString, arg0)
    Format2 = Replace(Format2, &quot;{1}&quot;, arg1)
End Function

&#39;------------------------------------------------------------------------------
&#39; The string formatting functions to avoid string concatenation.
&#39;------------------------------------------------------------------------------
Function Format1(myString, arg0)
    Format1 = Replace(myString, &quot;{0}&quot;, arg0)
End Function</code></pre></td>
</tr>
</tbody>
</table>



## Related topics

<dl> <dt>

[Exporting the configuration of a Virtual Machine](exporting-the-configuration-of-a-virtual-machine.md)
</dt> <dt>

[**ExportVirtualSystem**](exportvirtualsystem-msvm-virtualsystemmanagementservice.md)
</dt> <dt>

[**ExportVirtualSystemEx**](msvm-virtualsystemmanagementservice-exportvirtualsystemex.md)
</dt> </dl>

 

 




