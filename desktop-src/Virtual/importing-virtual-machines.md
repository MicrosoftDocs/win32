---
title: Importing Virtual Machines
description: The following C\ and VBScript samples import a virtual machine (VM).
ms.assetid: 453f053f-ecc8-42e3-9551-55c815c92eeb
keywords:
- Importing Virtual Machines Hyper-V
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Importing Virtual Machines

The following C# and VBScript samples import a virtual machine (VM).

**C#:** The referenced utilities can be found in [Common Utilities for the Virtualization Samples](common-utilities-for-the-virtualization-samples.md).


```CSharp
using System;
using System.IO;
using System.Management;

namespace HyperVSamples
{
    class ImportVirtualSystemExMoreGranularClass
    {

        static ManagementObject CreateSwitch(ManagementScope scope, string name, string friendlyName, int learnableAddress)
        {            
            ManagementObject switchService = Utility.GetServiceObject(scope, "Msvm_VirtualSwitchManagementService");
            ManagementObject createdSwitch = null;

            ManagementBaseObject inParams = switchService.GetMethodParameters("CreateSwitch");
            inParams["FriendlyName"] = friendlyName;
            inParams["Name"] = name;
            inParams["NumLearnableAddresses"] = learnableAddress;
            inParams["ScopeofResidence"] = null;
            ManagementBaseObject outParams = switchService.InvokeMethod("CreateSwitch", inParams, null);
            if ((UInt32)outParams["ReturnValue"] == ReturnCode.Completed)
            {
                Console.WriteLine("{0} was created successfully", inParams["Name"]);
                createdSwitch = new ManagementObject(outParams["CreatedVirtualSwitch"].ToString());
            }
            else
            {
                Console.WriteLine("Failed to create {0} switch.", inParams["Name"]);
            }
            return createdSwitch;
        }
        

        static ManagementBaseObject GetVirtualSystemImportSettingData(ManagementScope scope, string importDirectory, string rootDirectoryToCopy)
        {
            string targetVhdResourcePath = importDirectory + "\\Temp.vhd"; //Directories specified should exist
            ManagementObject virtualSystemService = Utility.GetServiceObject(scope, "Msvm_VirtualSystemManagementService");
            ManagementBaseObject importSettingData = null;
            ManagementBaseObject inParams = virtualSystemService.GetMethodParameters("GetVirtualSystemImportSettingData");
            inParams["ImportDirectory"] = importDirectory;

            ManagementBaseObject outParams = virtualSystemService.InvokeMethod("GetVirtualSystemImportSettingData", inParams, null);

            if ((UInt32)outParams["ReturnValue"] == ReturnCode.Started)
            {
                if (Utility.JobCompleted(outParams, scope))
                {
                    importSettingData = (ManagementBaseObject)outParams["ImportSettingData"];
                    Console.WriteLine("Import Setting Data for the ImportDirectory '{0}' was retrieved successfully.", importDirectory);
                }
                else
                {
                    Console.WriteLine("Failed to get the Import Setting Data");                    
                }
            }
            else if ((UInt32)outParams["ReturnValue"] == ReturnCode.Completed)
            {
                importSettingData = (ManagementBaseObject)outParams["ImportSettingData"];
                Console.WriteLine("Import Setting Data for the ImportDirectory '{0}' was retrieved successfully.", importDirectory);
            }
            else
            {
                Console.WriteLine("Failed to get the Import Setting Data for the Import Directory :{0}", (UInt32)outParams["ReturnValue"]);
            }

            inParams.Dispose();
            outParams.Dispose();
            virtualSystemService.Dispose();

            importSettingData["GenerateNewId"] = true;
            importSettingData["CreateCopy"] = true;
            importSettingData["Name"] = "NewSampleVM";
            importSettingData["TargetResourcePaths"] = new string[] { (targetVhdResourcePath) };
            ManagementObject newSwitch = CreateSwitch(scope, "Switch_For_Import_Export_Sample", "Switch_For_Import_Export_Sample", 1024);
            importSettingData["TargetNetworkConnections"] = new string[] { (newSwitch.GetPropertyValue("Name").ToString())};
                        
            return importSettingData;
        }

        static void ImportVirtualSystemEx(string importDirectory)
        {
            string importCopyDirectory = importDirectory + "\\NewCopy";
            ManagementScope scope = new ManagementScope(@"root\virtualization", null);
            ManagementObject virtualSystemService = Utility.GetServiceObject(scope, "Msvm_VirtualSystemManagementService");

            ManagementBaseObject importSettingData = GetVirtualSystemImportSettingData(scope, importDirectory, importCopyDirectory);

            ManagementBaseObject inParams = virtualSystemService.GetMethodParameters("ImportVirtualSystemEx");
            inParams["ImportDirectory"] = importDirectory;
            inParams["ImportSettingData"] = importSettingData.GetText(TextFormat.CimDtd20);

            ManagementBaseObject outParams = virtualSystemService.InvokeMethod("ImportVirtualSystemEx", inParams, null);

            if ((UInt32)outParams["ReturnValue"] == ReturnCode.Started)
            {
                if (Utility.JobCompleted(outParams, scope))
                {
                    Console.WriteLine("VM were Imported successfully.");

                }
                else
                {
                    Console.WriteLine("Failed to Imported VM");
                }
            }
            else if ((UInt32)outParams["ReturnValue"] == ReturnCode.Completed)
            {
                Console.WriteLine("VM were Imported successfully.");
            }
            else
            {
                Console.WriteLine("Import virtual system failed with error:{0}", outParams["ReturnValue"]);
            }

            inParams.Dispose();
            outParams.Dispose();
            virtualSystemService.Dispose();
        }

        static void Main(string[] args)
        {
            if (args != null &amp;&amp; args.Length != 1)
            {
                Console.WriteLine("Usage: ImportVirtualSystemExMoreGranular importDirectory");                
                return;
            }
            ImportVirtualSystemEx(args[0]);
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
dim switchService
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
    dim computer, objArgs, importDirectory, generateNewID
    
    set fileSystem = Wscript.CreateObject(&quot;Scripting.FileSystemObject&quot;)
    computer = &quot;.&quot;
    set objWMIService = GetObject(&quot;winmgmts:\\&quot; &amp; computer &amp; &quot;\root\virtualization&quot;)
    set managementService = objWMIService.ExecQuery(&quot;select * from Msvm_VirtualSystemManagementService&quot;).ItemIndex(0)
    set switchService = objWMIService.ExecQuery(&quot;select * from Msvm_VirtualSwitchManagementService&quot;).ItemIndex(0)

    
    set objArgs = WScript.Arguments
    if WScript.Arguments.Count = 1 then
        importDirectory = objArgs.Unnamed.Item(0)
    else
        WScript.Echo &quot;usage: cscript ImportVirtualSystemEx-MoreGranular.vbs importDirectoryName&quot;
        WScript.Quit(1)
    end if
   
    if ImportVirtualSystemEx(importDirectory) then
        WriteLog &quot;Done&quot;
        WScript.Quit(0)
    else
        WriteLog &quot;ImportVirtualSystemEx Failed.&quot;
        WScript.Quit(1)
    end if
End Sub

&#39;-----------------------------------------------------------------
&#39; Create a virtual switch by calling CreateSwitch WMI method
&#39;-----------------------------------------------------------------
Function CreateSwitch(name, friendlyName, learnableAddress)

    dim objInParam, objOutParams
    
    set CreateSwitch = Nothing
    set objInParam = switchService.Methods_(&quot;CreateSwitch&quot;).InParameters.SpawnInstance_()
    objInParam.FriendlyName = friendlyName
    objInParam.Name = name
    objInParam.NumLearnableAddresses = learnableAddress
    objInParam.ScopeofResidence = null

    set objOutParams = switchService.ExecMethod_(&quot;CreateSwitch&quot;, objInParam)
    
    if objOutParams.ReturnValue = wmiSuccessful then
        set CreateSwitch = objWMIService.Get(objOutParams.CreatedVirtualSwitch)
    else
        WriteLog Format1(&quot;CreateSwitch failed with error code {0}&quot;, objOutParams.ReturnValue)
    end if

End Function


&#39;-----------------------------------------------------------------
&#39; GetVirtualSystemImportSettingData from a directory
&#39;-----------------------------------------------------------------
Function GetVirtualSystemImportSettingData(importDirectory)

    dim objInParam, objOutParams    

    set objInParam = managementService.Methods_(&quot;GetVirtualSystemImportSettingData&quot;).InParameters.SpawnInstance_()
    objInParam.ImportDirectory = importDirectory

    set objOutParams = managementService.ExecMethod_(&quot;GetVirtualSystemImportSettingData&quot;, objInParam)
    
    if objOutParams.ReturnValue = wmiStarted then
        if (WMIJobCompleted(objOutParams)) then
            set GetVirtualSystemImportSettingData = objOutParams.ImportSettingData
        end if
    elseif objOutParams.ReturnValue = wmiSuccessful then
        set GetVirtualSystemImportSettingData = objOutParams.ImportSettingData
    else
        WriteLog Format1(&quot;GetVirtualSystemImportSettingData failed with ReturnValue {0}&quot;, objOutParams.ReturnValue)
    end if

End Function
&#39;-----------------------------------------------------------------
&#39; ImportVirtualSystem from a directory
&#39;-----------------------------------------------------------------
Function ImportVirtualSystemEx(importDirectory)

    dim objInParam, objOutParams
    dim newDataRoot
    dim importSettingData
    dim newTargetResourcePaths, newTargetNetworkConnections, newSwitch    

    newTargetResourcePaths = Array(1)
    &#39;Folders in newTargetResourcePaths should be existing
    newTargetResourcePaths(0) = importDirectory &amp; &quot;\Temp.vhd&quot;

    newTargetNetworkConnections = Array(1)
    newTargetNetworkConnections(0) = &quot;Switch_For_Import_Export_Sample&quot;

    set newSwitch = CreateSwitch(newTargetNetworkConnections(0), newTargetNetworkConnections(0), 1024)

    ImportVirtualSystemEx = false
    set objInParam = managementService.Methods_(&quot;ImportVirtualSystemEx&quot;).InParameters.SpawnInstance_()
    objInParam.ImportDirectory = importDirectory

    set importSettingData = GetVirtualSystemImportSettingData(importDirectory)
    importSettingData.GenerateNewId = true
    importSettingData.CreateCopy = true
    importSettingData.Name = &quot;NewSampleVM-WithFixups&quot;
    importSettingData.TargetResourcePaths = newTargetResourcePaths
    importSettingData.TargetNetworkConnections = newTargetNetworkConnections
    importSettingData.Put_

    objInParam.ImportSettingData = importSettingData.GetText_(1)
    
    set objOutParams = managementService.ExecMethod_(&quot;ImportVirtualSystemEx&quot;, objInParam)

    if objOutParams.ReturnValue = wmiStarted then
        if (WMIJobCompleted(objOutParams)) then
            ImportVirtualSystemEx = true
        end if
    elseif objOutParams.ReturnValue = wmiSuccessful then
        ImportVirtualSystemEx = true
    else
        WriteLog Format1(&quot;ImportVirtualSystemEx failed with ReturnValue {0}&quot;, objOutParams.ReturnValue)
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
    set fileStream = fileSystem.OpenTextFile(&quot;.\ImportVirtualSystemEx-MoreGranular.log&quot;, 8, true)
    WScript.Echo line
    fileStream.WriteLine line
    fileStream.Close

End Sub

&#39;------------------------------------------------------------------------------
&#39; The string formatting functions to avoid string concatenation.
&#39;------------------------------------------------------------------------------
Function Format1(myString, arg0)
    Format1 = Replace(myString, &quot;{0}&quot;, arg0)
End Function</code></pre></td>
</tr>
</tbody>
</table>



 

 




