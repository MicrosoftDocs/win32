---
Description: Use the WMI classes that obtain data from performance counters to access and refresh data about computer performance.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4c88de96-992e-4d34-ba93-35d2b6e73c1d
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: 'WMI Tasks: Performance Monitoring'
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# WMI Tasks: Performance Monitoring

Use the WMI classes that obtain data from performance counters to access and refresh data about computer performance. For other examples, see the TechNet ScriptCenter at [http://www.microsoft.com/technet](Http://go.microsoft.com/fwlink/p/?linkid=84103). For more information, see [Performance Libraries and WMI](performance-libraries-and-wmi.md) and [Monitoring Performance Data](monitoring-performance-data.md).

The script examples shown in this topic obtain data only from the local computer. For more information about how to use the script to obtain data from remote computers, see [Connecting to WMI on a Remote Computer](connecting-to-wmi-on-a-remote-computer.md).

## 

The following procedure describes how to run a script.

**To run a script**

1.  Copy the code and save it in a file with a .vbs extension, such as *filename.vbs*. Ensure that your text editor does not add a .txt extension to the file.
2.  Open a command prompt window and navigate to the directory where you saved the file.
3.  Type **cscript filename.vbs** at the command prompt.
4.  If you cannot access an event log, check to see if you are running from an Elevated command prompt. Some Event Log, such as the Security Event Log, may be protected by User Access Controls (UAC).

> [!Note]  
> By default, cscript displays the output of a script in the command prompt window. Because WMI scripts can produce large amounts of output, you might want to redirect the output to a file. Type **cscript filename.vbs &gt; outfile.txt** at the command prompt to redirect the output of the *filename.vbs* script to *outfile.txt*.

 

The following table lists script examples that can be used to obtain various types of data from the local computer.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>How do I...</th>
<th>WMI classes or methods</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>...obtain the performance counter data that I can see in the Perfmon utility in a script?</td>
<td>Use classes that have names that begin with &quot;[Win32_PerfFormattedData](https://msdn.microsoft.com/library/aa392738)&quot;, for example [<strong>Win32_PerfFormattedData_PerfProc_Process</strong>](https://msdn.microsoft.com/library/dn750765). Properties with names like <strong>PageFileBytes</strong> correspond to performance counters you see in Perfmon. The &quot;Win32_PerfFormattedData&quot; classes calculate the final values of counters for you.<br/></td>
</tr>
<tr class="even">
<td>...get on-going performance data for a single process, disk drive, and other data?</td>
<td>Use the [<strong>Win32_PerfFormattedData_PerfProc_Process</strong>](https://msdn.microsoft.com/library/dn750765) or the appropriate formatted [Performance Counter Class](https://msdn.microsoft.com/library/aa392738) and the [<strong>SWbemObjectEx.Refresh_</strong>](swbemobjectex-refresh-.md) method. For more information, see [Scripting with SWbemObject](scripting-with-swbemobject.md).<br/> In C++, use [<strong>IWbemConfigureRefresher::AddObjectByPath</strong>](/windows/desktop/api/Wbemcli/nf-wbemcli-iwbemconfigurerefresher-addobjectbypath) and [<strong>IWbemRefresher::Refresh</strong>](/windows/desktop/api/Wbemcli/nf-wbemcli-iwbemrefresher-refresh). For more information, see [Monitoring Performance Data](monitoring-performance-data.md).<br/> The following script runs until the computer is restarted, WMI is stopped, or the script is stopped. To stop the script manually, use Task Manager to stop the process. To stop it programmatically, use the [<strong>Terminate</strong>](https://msdn.microsoft.com/library/aa393907) method in the [<strong>Win32_Process</strong>](https://msdn.microsoft.com/library/aa394372) class.<br/> <span data-codelanguage="VisualBasic"></span>
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
<td><pre><code>strComputer = &quot;.&quot;
Set objWMIService = GetObject(&quot;winmgmts:&quot; _
    &amp; &quot;{impersonationLevel=impersonate}!\\&quot; _
    &amp; strComputer &amp; &quot;\root\cimv2&quot;)
set PerfProcess = objWMIService.Get(_
    &quot;Win32_PerfFormattedData_PerfProc_Process.Name=&#39;Idle&#39;&quot;)

While (True)
    PerfProcess.Refresh_     
    Wscript.Echo PerfProcess.PercentProcessorTime
    Wscript.Sleep 1000
Wend</code></pre></td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr class="odd">
<td>...get on-going performance data for all processes without repeated polling?</td>
<td><p>Use classes that have names that begin with &quot;Win32_PerfFormattedData&quot; and an [<strong>SWbemRefresher</strong>](swbemrefresher.md) object. The refresher holds the objects so you do not need to get the collection repeatedly. A minimum of two values are needed to calculate performance data because most counters are rate counters. The first time you display the refresher data it is empty.</p>
<p>The following script runs indefinitely until the computer is rebooted, WMI is stopped, or the script is stopped. To stop the script manually, use Task Manager to stop the process. To stop it programmatically, use the [<strong>Terminate</strong>](https://msdn.microsoft.com/library/aa393907) method in the [<strong>Win32_Process</strong>](https://msdn.microsoft.com/library/aa394372) class.</p>
<div class="code">
<span data-codelanguage="VisualBasic"></span>
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
<td><pre><code>strComputer = &quot;.&quot;
Set objWMIService = GetObject(&quot;winmgmts:&quot; _
    &amp; &quot;{impersonationLevel=impersonate}!\\&quot; _
    &amp; strComputer &amp; &quot;\root\cimv2&quot;)
set objRefresher = CreateObject(&quot;WbemScripting.Swbemrefresher&quot;)
Set objProcessor = objRefresher.AddEnum _
    (objWMIService, _
    &quot;Win32_PerfFormattedData_PerfOS_Processor&quot;).ObjectSet

While (True)
    objRefresher.Refresh
        For each RefreshItem in objRefresher
            For each objProcess in RefreshItem.ObjectSet
                Wscript.Echo objProcess.GetObjectText_
            Next
        Next
     Wscript.Sleep 5000
Wend</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="even">
<td>...get and calculate performance data for processes on Windows 2000?</td>
<td><p>Use the &quot;Win32_PerfRawData&quot; classes, such as [<strong>Win32_PerfRawData_PerfProc_Process</strong>](https://msdn.microsoft.com/library/dn750765). Get the property data, such as <strong>PercentProcessorTime</strong>, twice for a specific process. Look up the formula specified in the [<strong>CounterType</strong>](countertype-qualifier.md) qualifier for the property and calculate. The CounterType in the example is [PERF_100NSEC_TIMER_INV](http://go.microsoft.com/fwlink/p/?linkid=44341). For more information, see [Monitoring Performance Data](monitoring-performance-data.md).</p>
<p>The following script runs indefinitely until the computer is rebooted, WMI is stopped, or the script is stopped. To stop the script manually, use Task Manager to stop the process. To stop it programmatically, use the [<strong>Terminate</strong>](https://msdn.microsoft.com/library/aa393907) method in the [<strong>Win32_Process</strong>](https://msdn.microsoft.com/library/aa394372) class.</p>
<div class="code">
<span data-codelanguage="VisualBasic"></span>
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
<td><pre><code>strComputer = &quot;.&quot;
Set objWMIService = GetObject(&quot;winmgmts:&quot; _
    &amp; &quot;{impersonationLevel=impersonate}!\\&quot; _
    &amp; strComputer &amp; &quot;\root\cimv2&quot;)

While (True)
    Set object1 = objWMIService.Get( _
    &quot;Win32_PerfRawData_PerfOS_Processor.Name=&#39;_Total&#39;&quot;)
    N1 = object1.PercentProcessorTime
    D1 = object1.TimeStamp_Sys100NS
    Wscript.Sleep(1000)
    set object2 = objWMIService.Get( _
    &quot;Win32_PerfRawData_PerfOS_Processor.Name=&#39;_Total&#39;&quot;)
    N2 = object2.PercentProcessorTime
    D2 = object2.TimeStamp_Sys100NS

    &#39; CounterType - PERF_100NSEC_TIMER_INV
    &#39; Formula - (1- ((N2 - N1) / (D2 - D1))) x 100
    PercentProcessorTime = (1 - ((N2 - N1)/(D2-D1)))*100

    Wscript.Echo &quot;% Processor Time=&quot; , PercentProcessorTime

Wend</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[WMI Tasks for Scripts and Applications](wmi-tasks-for-scripts-and-applications.md)
</dt> <dt>

[WMI C++ Application Examples](wmi-c---application-examples.md)
</dt> <dt>

[TechNet ScriptCenter](http://go.microsoft.com/fwlink/p/?linkid=46710)
</dt> </dl>

 

 




