---
description: Use the WMI classes that obtain data from performance counters to access and refresh data about computer performance.
ms.assetid: 4c88de96-992e-4d34-ba93-35d2b6e73c1d
ms.tgt_platform: multiple
title: 'WMI Tasks: Performance Monitoring'
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# WMI Tasks: Performance Monitoring

Use the WMI classes that obtain data from performance counters to access and refresh data about computer performance. For other examples, see the TechNet ScriptCenter at [https://www.microsoft.com/technet](https://technet.microsoft.com/default.aspx). For more information, see [Performance Libraries and WMI](performance-libraries-and-wmi.md) and [Monitoring Performance Data](monitoring-performance-data.md).

The script examples shown in this topic obtain data only from the local computer. For more information about how to use the script to obtain data from remote computers, see [Connecting to WMI on a Remote Computer](connecting-to-wmi-on-a-remote-computer.md).


The following procedure describes how to run a script.

**To run a script**

1.  Copy the code and save it in a file with a .vbs extension, such as *filename.vbs*. Ensure that your text editor does not add a .txt extension to the file.
2.  Open a command prompt window and navigate to the directory where you saved the file.
3.  Type **cscript filename.vbs** at the command prompt.
4.  If you cannot access an event log, check to see if you are running from an Elevated command prompt. Some Event Log, such as the Security Event Log, may be protected by User Access Controls (UAC).

> [!Note]  
> By default, cscript displays the output of a script in the command prompt window. Because WMI scripts can produce large amounts of output, you might want to redirect the output to a file. Type **cscript filename.vbs > outfile.txt** at the command prompt to redirect the output of the *filename.vbs* script to *outfile.txt*.

 

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
<td>Use classes that have names that begin with &quot;<a href="/windows/desktop/CIMWin32Prov/performance-counter-classes">Win32_PerfFormattedData</a>&quot;, for example <a href="/windows/desktop/WmiSdk/retrieving-raw-and-formatted-performance-data"><strong>Win32_PerfFormattedData_PerfProc_Process</strong></a>. Properties with names like <strong>PageFileBytes</strong> correspond to performance counters you see in Perfmon. The &quot;Win32_PerfFormattedData&quot; classes calculate the final values of counters for you.<br/></td>
</tr>
<tr class="even">
<td>...get on-going performance data for a single process, disk drive, and other data?</td>
<td>Use the <a href="/windows/desktop/WmiSdk/retrieving-raw-and-formatted-performance-data"><strong>Win32_PerfFormattedData_PerfProc_Process</strong></a> or the appropriate formatted <a href="/windows/desktop/CIMWin32Prov/performance-counter-classes">Performance Counter Class</a> and the <a href="swbemobjectex-refresh-.md"><strong>SWbemObjectEx.Refresh_</strong></a> method. For more information, see <a href="scripting-with-swbemobject.md">Scripting with SWbemObject</a>.<br/> In C++, use <a href="/windows/desktop/api/Wbemcli/nf-wbemcli-iwbemconfigurerefresher-addobjectbypath"><strong>IWbemConfigureRefresher::AddObjectByPath</strong></a> and <a href="/windows/desktop/api/Wbemcli/nf-wbemcli-iwbemrefresher-refresh"><strong>IWbemRefresher::Refresh</strong></a>. For more information, see <a href="monitoring-performance-data.md">Monitoring Performance Data</a>.<br/> The following script runs until the computer is restarted, WMI is stopped, or the script is stopped. To stop the script manually, use Task Manager to stop the process. To stop it programmatically, use the <a href="/windows/desktop/CIMWin32Prov/terminate-method-in-class-win32-process"><strong>Terminate</strong></a> method in the <a href="/windows/desktop/CIMWin32Prov/win32-process"><strong>Win32_Process</strong></a> class.<br/> <span data-codelanguage="VisualBasic"></span>
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
    & &quot;{impersonationLevel=impersonate}!\\&quot; _
    & strComputer & &quot;\root\cimv2&quot;)
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
<td><p>Use classes that have names that begin with &quot;Win32_PerfFormattedData&quot; and an <a href="swbemrefresher.md"><strong>SWbemRefresher</strong></a> object. The refresher holds the objects so you do not need to get the collection repeatedly. A minimum of two values are needed to calculate performance data because most counters are rate counters. The first time you display the refresher data it is empty.</p>
<p>The following script runs indefinitely until the computer is rebooted, WMI is stopped, or the script is stopped. To stop the script manually, use Task Manager to stop the process. To stop it programmatically, use the <a href="/windows/desktop/CIMWin32Prov/terminate-method-in-class-win32-process"><strong>Terminate</strong></a> method in the <a href="/windows/desktop/CIMWin32Prov/win32-process"><strong>Win32_Process</strong></a> class.</p>
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
    & &quot;{impersonationLevel=impersonate}!\\&quot; _
    & strComputer & &quot;\root\cimv2&quot;)
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
<td><p>Use the &quot;Win32_PerfRawData&quot; classes, such as <a href="/windows/desktop/WmiSdk/retrieving-raw-and-formatted-performance-data"><strong>Win32_PerfRawData_PerfProc_Process</strong></a>. Get the property data, such as <strong>PercentProcessorTime</strong>, twice for a specific process. Look up the formula specified in the <a href="countertype-qualifier.md"><strong>CounterType</strong></a> qualifier for the property and calculate. The CounterType in the example is <a href="/previous-versions/windows/it-pro/windows-server-2003/cc785636(v=ws.10)">PERF_100NSEC_TIMER_INV</a>. For more information, see <a href="monitoring-performance-data.md">Monitoring Performance Data</a>.</p>
<p>The following script runs indefinitely until the computer is rebooted, WMI is stopped, or the script is stopped. To stop the script manually, use Task Manager to stop the process. To stop it programmatically, use the <a href="/windows/desktop/CIMWin32Prov/terminate-method-in-class-win32-process"><strong>Terminate</strong></a> method in the <a href="/windows/desktop/CIMWin32Prov/win32-process"><strong>Win32_Process</strong></a> class.</p>
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
    & &quot;{impersonationLevel=impersonate}!\\&quot; _
    & strComputer & &quot;\root\cimv2&quot;)

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

[TechNet ScriptCenter](https://www.microsoft.com/technet/scriptcenter)
</dt> </dl>
