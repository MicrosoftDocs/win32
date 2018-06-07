---
Description: WMI scheduled tasks create and get information about scheduled tasks. For other examples, see the TechNet ScriptCenter at http://www.microsoft.com/technet.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 62151fe8-8880-43f2-b456-628bd9c7cc1c
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: 'WMI Tasks: Scheduled Tasks'
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WMI Tasks: Scheduled Tasks

WMI scheduled tasks create and get information about scheduled tasks. For other examples, see the TechNet ScriptCenter at [http://www.microsoft.com/technet](Http://go.microsoft.com/fwlink/p/?linkid=84103).

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
<td>...create scheduled tasks using scripts?</td>
<td>Use the [<strong>Win32_ScheduledJob</strong>](https://msdn.microsoft.com/library/aa394399) class and the [<strong>Create</strong>](https://msdn.microsoft.com/library/aa389389) method. If you are having difficulty making this task work on Windows 7 or later, see the <strong>Win32_ScheduledJob</strong> Remarks section; likely your settings are preventing you from using the class.<br/> <span data-codelanguage="VisualBasic"></span>
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
Set objWMIService = GetObject(&quot;winmgmts:&quot; &amp; &quot;{impersonationLevel=impersonate}!\\&quot; &amp; strComputer &amp; &quot;\root\cimv2&quot;) 
JobID = &quot;Test&quot;
Set objNewJob = objWMIService.Get(&quot;Win32_ScheduledJob&quot;)
errJobCreate = objNewJob.Create _
    (&quot;Notepad.exe&quot;, &quot;********143000.000000-420&quot;, True , 1 OR 4 OR 16, ,True, JobId) 
If errJobCreate = 0 Then
    WScript.Echo &quot;Job created successfully: &quot; &amp; VBNewLine _
        &amp; &quot;Notepad.exe scheduled to run repeately at 14.30 (2:30 P.M.) PST&quot; &amp; VBNewLine _
        &amp; &quot;on Mon, Wed, and Fri.&quot;
Else
    WScript.Echo &quot;Job not created. Error code = &quot; &amp; errJobCreate
End If</code></pre></td>
</tr>
</tbody>
</table>

<p>In the string &quot;********143000.000000-420&quot; (used in the <em>StartTime</em> parameter value of the [<strong>Create</strong>](https://msdn.microsoft.com/library/aa389389) method), &quot;********143000.000000&quot; specifies that the task starts at 14.30 (2:30 P.M.) and &quot;-420&quot; specifies the time zone. The time zone number is the current bias of the local time translation. The bias is the difference between the UTC time and the local time. To calculate the bias for your time zone, multiply the number of hours that your time zone is ahead or behind Greenwich Mean Time (GMT) by 60 (use a positive number for the number of hours if your time zone is ahead of GMT and a negative number if your time zone is behind GMT). Add an additional 60 to your calculation if your time zone is using daylight savings time. For example, the Pacific Standard Time zone is eight hours behind GMT, therefore the bias is equals to -420 (-8 * 60 + 60) when daylight savings time is in use and -480 (-8 * 60) when daylight savings time is not in use. You can also determine the value of the bias by querying the bias property of the [<strong>Win32_TimeZone</strong>](https://msdn.microsoft.com/library/aa394498) class.</p></td>
</tr>
<tr class="even">
<td>...return a list of all the scheduled tasks on a computer?</td>
<td><p>Use the [<strong>Win32_ScheduledJob</strong>](https://msdn.microsoft.com/library/aa394399) class. Note that this class can only return jobs that are created using either a script or AT.exe. It cannot return information about jobs that are either created by or modified by the Scheduled Task wizard.</p>
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
strComputer = &quot;.&quot;
Set objWMIService = GetObject(&quot;winmgmts:&quot; &amp; &quot;{impersonationLevel=impersonate}!\\&quot; &amp; strComputer &amp; &quot;\root\cimv2&quot;)
Set colScheduledJobs = objWMIService.ExecQuery (&quot;Select * from Win32_ScheduledJob&quot;)
For Each objJob in colScheduledJobs
    Wscript.Echo &quot;Command: &quot; &amp; objJob.Command &amp; VBNewLine _
    &amp; &quot;Days Of Month: &quot; &amp; objJob.DaysOfMonth &amp; VBNewLine _
    &amp; &quot;Days Of Week: &quot; &amp; objJob.DaysOfWeek &amp; VBNewLine _
    &amp; &quot;Description: &quot; &amp; objJob.Description &amp; VBNewLine _
    &amp; &quot;Elapsed Time: &quot; &amp; objJob.ElapsedTime &amp; VBNewLine _
    &amp; &quot;Install Date: &quot; &amp; objJob.InstallDate &amp; VBNewLine _
    &amp; &quot;Interact with Desktop: &quot; &amp; objJob.InteractWithDesktop &amp; VBNewLine _
    &amp; &quot;Job ID: &quot; &amp; objJob.JobId &amp; VBNewLine _
    &amp; &quot;Job Status: &quot; &amp; objJob.JobStatus &amp; VBNewLine _
    &amp; &quot;Name: &quot; &amp; objJob.Name &amp; VBNewLine _
    &amp; &quot;Notify: &quot; &amp; objJob.Notify &amp; VBNewLine _
    &amp; &quot;Owner: &quot; &amp; objJob.Owner &amp; VBNewLine _
    &amp; &quot;Priority: &quot; &amp; objJob.Priority &amp; VBNewLine _
    &amp; &quot;Run Repeatedly: &quot; &amp; objJob.RunRepeatedly &amp; VBNewLine _
    &amp; &quot;Start Time: &quot; &amp; objJob.StartTime &amp; VBNewLine _
    &amp; &quot;Status: &quot; &amp; objJob.Status &amp; VBNewLine _
    &amp; &quot;Time Submitted: &quot; &amp; objJob.TimeSubmitted &amp; VBNewLine _
    &amp; &quot;Until Time: &quot; &amp; objJob.UntilTime
Next</code></pre></td>
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

 

 




