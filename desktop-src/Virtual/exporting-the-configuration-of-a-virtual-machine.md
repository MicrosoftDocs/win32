---
title: Exporting the Configuration of a Virtual Machine
description: The following C\ and VBScript samples demonstrate exporting the configuration of a virtual machine (VM).
ms.assetid: f6fa3220-9f48-437d-91e0-89b40f0a40f4
keywords:
- Exporting the configuration of a Virtual Machine Hyper-V
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Exporting the Configuration of a Virtual Machine

The following C# and VBScript samples demonstrate exporting the configuration of a virtual machine (VM). Samples that demonstrate exporting a virtual machine can be found on the [**ExportVirtualSystemEx**](msvm-virtualsystemmanagementservice-exportvirtualsystemex.md) and [Exporting a snapshot of a Virtual Machine](exporting-virtual-machines.md) topics.

**C#:** The referenced utilities can be found in [Common Utilities for the Virtualization Samples](common-utilities-for-the-virtualization-samples.md).


```CSharp
using System;
using System.IO;
using System.Management;

namespace HyperVSamples
{
    class ExportVirtualSystemExConfigOnlyClass
    {
        static string GetConfigOnlyVirtualSystemExportSettingDataInstance(ManagementScope scope)
        {
            ManagementPath settingPath = new ManagementPath("Msvm_VirtualSystemExportSettingData");

            ManagementClass exportSettingDataClass = new ManagementClass(scope, settingPath, null);
            ManagementObject exportSettingData = exportSettingDataClass.CreateInstance();

            // Do not copy VHDs and AVHDs but copy the Snapshot configuration and Saved State information (Runtime information) if present
            exportSettingData["CopySnapshotConfiguration"] = 0;
            exportSettingData["CopyVmRuntimeInformation"] = true;
            exportSettingData["CopyVmStorage"] = false;
            exportSettingData["CreateVmExportSubdirectory"] = true;

            string settingData = exportSettingData.GetText(TextFormat.CimDtd20);

            exportSettingData.Dispose();
            exportSettingDataClass.Dispose();

            return settingData;
        }


        static void ExportVirtualSystemExConfigOnly(string vmName, string exportDirectory)
        {
            ManagementScope scope = new ManagementScope(@"root\virtualization", null);
            ManagementObject virtualSystemService = Utility.GetServiceObject(scope, "Msvm_VirtualSystemManagementService");

            ManagementBaseObject inParams = virtualSystemService.GetMethodParameters("ExportVirtualSystemEx");

            ManagementObject vm = Utility.GetTargetComputer(vmName, scope);
            inParams["ComputerSystem"] = vm.Path.Path;
            
            if (!Directory.Exists(exportDirectory))
            {
                Directory.CreateDirectory(exportDirectory);
            }
            inParams["ExportDirectory"] = exportDirectory;
            inParams["ExportSettingData"] = GetConfigOnlyVirtualSystemExportSettingDataInstance(scope);

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
                Console.WriteLine("Usage: ExportVirtualSystemEx vmName exportDirectory");
                return;
            }
            ExportVirtualSystemExConfigOnly(args[0], args[1]);
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
        WScript.Echo &quot;usage: cscript ExportVirtualSystemEx.vbs vmName exportDirectoryName&quot;
        WScript.Quit(1)
    end if
    
    set vm = GetComputerSystem(vmName)

    if ExportVirtualSystemEx(vm, exportDirectory) then
        WriteLog &quot;Done&quot;
        WScript.Quit(0)
    else
        WriteLog &quot;ExportVirtualSystemEx Failed.&quot;
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
&#39; Export a virtual system
&#39;-----------------------------------------------------------------
Function ExportVirtualSystemEx(computerSystem, exportDirectory)

    dim objInParam, objOutParams 
    dim query
    dim computer
    dim exportSettingData
 
    ExportVirtualSystemEx = false
    
    if Not fileSystem.FolderExists(exportDirectory) then
        fileSystem.CreateFolder(exportDirectory)
    end if
    
    set objInParam = managementService.Methods_(&quot;ExportVirtualSystemEx&quot;).InParameters.SpawnInstance_()
    objInParam.ComputerSystem = computerSystem.Path_.Path

    query = Format1(&quot;ASSOCIATORS OF {{0}} WHERE resultClass = Msvm_VirtualSystemExportSettingData&quot;, computerSystem.Path_.Path)
    set exportSettingData = objWMIService.ExecQuery(query).ItemIndex(0)

    &#39;Do not copy the VHDs and AVHDs, but copy the Saved state information and Snapshot configurations if present
    exportSettingData.CopyVmStorage = false
    exportSettingData.CopyVmRuntimeInformation = true
    exportSettingData.CreateVmExportSubdirectory = true
    exportSettingData.CopySnapshotConfiguration = 0

    objInParam.ExportSettingData = exportSettingData.GetText_(1)

    objInParam.ExportDirectory = exportDirectory
    
    set objOutParams = managementService.ExecMethod_(&quot;ExportVirtualSystemEx&quot;, objInParam)

    if objOutParams.ReturnValue = wmiStarted then
        if (WMIJobCompleted(objOutParams)) then
            ExportVirtualSystemEx = true
        end if
    elseif (objOutParams.ReturnValue = wmiSuccessful) then
        ExportVirtualSystemEx = true
    else
        WriteLog Format1(&quot;ExportVirtualSystemEx failed with ReturnValue {0}&quot;, objOutParams.ReturnValue)
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
    set fileStream = fileSystem.OpenTextFile(&quot;.\ExportVirtualSystemExLog.log&quot;, 8, true)
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

[Exporting a snapshot of a Virtual Machine](exporting-virtual-machines.md)
</dt> <dt>

[**ExportVirtualSystem**](exportvirtualsystem-msvm-virtualsystemmanagementservice.md)
</dt> <dt>

[**ExportVirtualSystemEx**](msvm-virtualsystemmanagementservice-exportvirtualsystemex.md)
</dt> </dl>

 

 




