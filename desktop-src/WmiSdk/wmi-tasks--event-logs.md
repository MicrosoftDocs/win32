---
Description: 'WMI tasks for event logs obtain event data from event log files and perform operations like backing up or clearing log files. For other examples, see the TechNet ScriptCenter at http://www.microsoft.com/technet.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: 'f6d4e68e-d757-44aa-be74-3b26168626b8'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'WMI Tasks: Event Logs'
---

# WMI Tasks: Event Logs

WMI tasks for event logs obtain event data from event log files and perform operations like backing up or clearing log files. For other examples, see the TechNet ScriptCenter at [http://www.microsoft.com/technet](Http://go.microsoft.com/fwlink/p/?linkid=84103).

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
<td>...retrieve information about the Security event log?</td>
<td>Include the [Security](privilege-constants.md) privilege when connecting to the [<strong>Win32_NTEventlogFile</strong>](https://msdn.microsoft.com/library/aa394225) class. For more information, see [Executing Privileged Operations Using VBScript](executing-privileged-operations-using-vbscript.md).<br/> <span data-codelanguage="VisualBasic"></span>
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
    &amp; &quot;{impersonationLevel=impersonate,(Security)}!\\&quot; &amp; _
        strComputer &amp; &quot;\root\cimv2&quot;)
Set colLogFiles = objWMIService.ExecQuery _
    (&quot;Select * from Win32_NTEventLogFile &quot; _
        &amp; &quot;Where LogFileName=&#39;Security&#39;&quot;)
For Each objLogFile in colLogFiles
    Wscript.Echo objLogFile.NumberOfRecords
    Wscript.Echo &quot;Maximum Size: &quot; _
    &amp;  objLogfile.MaxFileSize 
Next</code></pre></td>
</tr>
</tbody>
</table>
<span data-codelanguage="PowerShell"></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>PowerShell</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>$strComputer = &quot;.&quot;
$colLogFiles = Get-WmiObject -Class Win32_NTEventLogFile -ComputerName $strComputer | Where-Object {$_.LogFileName -eq &#39;security&#39;}
foreach ($objLogFile in $colLogFiles) 
{ 
    &quot;Record Number: &quot; + $objLogFile.NumberOfRecords
    &quot;Maximum Size: &quot; + $objLogFile.MaxFileSize
}</code></pre></td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr class="even">
<td>...back up an event log?</td>
<td><p>Use the [<strong>Win32_NTEventlogFile</strong>](https://msdn.microsoft.com/library/aa394225) class and the [<strong>BackupEventLog</strong>](https://msdn.microsoft.com/library/aa384808) method. You may need to include the [Backup](privilege-constants.md) privilege when connecting to WMI. For more information, see [Executing Privileged Operations Using VBScript](executing-privileged-operations-using-vbscript.md).</p>
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
Set objWMIService = GetObject(&quot;winmgmts:&quot; &amp; &quot;{impersonationLevel=impersonate,(Backup)}!\\&quot; &amp; strComputer &amp; &quot;\root\cimv2&quot;)
Set colLogFiles = objWMIService.ExecQuery (&quot;Select * from Win32_NTEventLogFile &quot; &amp; &quot;Where LogFileName=&#39;Application&#39;&quot;)
For Each objLogfile in colLogFiles
    errBackupLog = objLogFile.BackupEventLog(&quot;c:\scripts\application.evt&quot;)
    WScript.Echo &quot;File saved as c:\scripts\applications.evt&quot;
Next</code></pre></td>
</tr>
</tbody>
</table>
<span data-codelanguage="PowerShell"></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>PowerShell</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>$strComputer = &quot;.&quot;
$colLogFiles = Get-WmiObject -Class Win32_NTEventLogFile -ComputerName $strComputer | Where-Object {$_.LogFileName -eq &#39;Application&#39;}

foreach ($objLogFile in $colLogFiles) 
{ 
    [void]$objLogFile.BackupEventlog(&quot;c:\scripts\applications.evt&quot;)
    &quot;File saved as c:\scripts\applications.evt&quot;
}</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="odd">
<td>...back up an event log more than once?</td>
<td><p>Ensure that the backup file has a unique name before using the [<strong>Win32_NTEventlogFile</strong>](https://msdn.microsoft.com/library/aa394225) and the [<strong>BackupEventLog</strong>](https://msdn.microsoft.com/library/aa384808) method. The operating system does not allow you to overwrite an existing backup file; you must either move the backup file or rename it before you can run the script again. You may need to include the [Backup](privilege-constants.md) privilege when connecting to WMI. For more information, see [Executing Privileged Operations Using VBScript](executing-privileged-operations-using-vbscript.md).</p>
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
<td><pre><code>dtmThisDay = Day(Date)
dtmThisMonth = Month(Date)
dtmThisYear = Year(Date)
strBackupName = dtmThisYear &amp; &quot;_&quot; &amp; dtmThisMonth &amp; &quot;_&quot; &amp; dtmThisDay
strComputer = &quot;.&quot;
Set objWMIService = GetObject(&quot;winmgmts:&quot; &amp; &quot;{impersonationLevel=impersonate,(Backup)}!\\&quot; &amp; strComputer &amp; &quot;\root\cimv2&quot;)
Set colLogFiles = objWMIService.ExecQuery (&quot;Select * from Win32_NTEventLogFile &quot; &amp; &quot;Where LogFileName=&#39;Application&#39;&quot;)
For Each objLogfile in colLogFiles
    objLogFile.BackupEventLog(&quot;c:\scripts\&quot; &amp; strBackupName &amp; &quot;_application.evt&quot;)
    objLogFile.ClearEventLog()
    WScript.Echo &quot;File saved: &quot; &amp; strBackupName &amp; &quot;_application.evt&quot;
Next</code></pre></td>
</tr>
</tbody>
</table>
<span data-codelanguage="PowerShell"></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>PowerShell</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>$CurDate = Get-Date
$strBackupName = $curDate.Year.ToString() + &quot;_&quot; + $curDate.Month.ToString() + &quot;_&quot; + $CurDate.Day.ToString()

$strComputer = &quot;.&quot;
$colLogFiles = Get-WmiObject -Class Win32_NTEventLogFile -ComputerName $strComputer | Where-Object {$_.LogFileName -eq &#39;Application&#39;}
foreach ($objLogFile in $colLogFiles) 
{ 
    $BackupFile = $objLogFile.BackupEventlog(&quot;c:\scripts\&quot; + $strBackupName + &quot;_application.evt&quot;)
    &quot;File saved: c:\scripts\&quot; + $strBackupName + &quot;_application.evt&quot;
}</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="even">
<td>...determine the number of records in an event log?</td>
<td><p>Use the [<strong>Win32_NTEventlogFile</strong>](https://msdn.microsoft.com/library/aa394225) class and check the value of the <strong>NumberOfRecords</strong> property.</p>
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
Set objWMIService = GetObject(&quot;winmgmts:&quot; &amp; &quot;{impersonationLevel=impersonate}!\\&quot; &amp; strComputer &amp; &quot;\root\cimv2&quot;)
Set colLogFiles = objWMIService.ExecQuery (&quot;Select * from Win32_NTEventLogFile &quot; &amp; &quot;Where LogFileName=&#39;System&#39;&quot;)
For Each objLogFile in colLogFiles
    Wscript.Echo objLogFile.NumberOfRecords
Next</code></pre></td>
</tr>
</tbody>
</table>
<span data-codelanguage="PowerShell"></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>PowerShell</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>$strComputer = &quot;.&quot;
$colLogFiles = Get-WmiObject -Class Win32_NTEventLogFile -ComputerName $strComputer | Where-Object {$_.LogFileName -eq &#39;System&#39;}

foreach ($objLogFile in $colLogFiles) 
{ 
    $objLogFile.NumberOfRecords
}</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="odd">
<td>...clear my event logs?</td>
<td><p>Use the [<strong>Win32_NTEventlogFile</strong>](https://msdn.microsoft.com/library/aa394225) class and the [<strong>ClearEventLog</strong>](https://msdn.microsoft.com/library/aa389229) method.</p>
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
Set objWMIService = GetObject(&quot;winmgmts:&quot; &amp; &quot;{impersonationLevel=impersonate,(Backup, Security)}!\\&quot; &amp; strComputer &amp; &quot;\root\cimv2&quot;)
Set colLogFiles = objWMIService.ExecQuery (&quot;Select * from Win32_NTEventLogFile &quot; &amp; &quot;Where LogFileName=&#39;Application&#39;&quot;)
For Each objLogfile in colLogFiles
    objLogFile.ClearEventLog()
    WScript.Echo &quot;Cleared application event log file&quot;
Next</code></pre></td>
</tr>
</tbody>
</table>
<span data-codelanguage="PowerShell"></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>PowerShell</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>$strComputer = &quot;.&quot;
$colLogFiles = Get-WmiObject -Class Win32_NTEventLogFile -ComputerName $strComputer | Where-Object {$_.LogFileName -eq &#39;System&#39;}

foreach ($objLogFile in $colLogFiles) 
{ 
    [void]$objLogFile.ClearEventlog()
    &quot;Cleared application event log file&quot;
}</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="even">
<td>...read events from the event logs?</td>
<td><p>Use the [<strong>Win32_NTLogEvent</strong>](https://msdn.microsoft.com/library/aa394226) class.</p>
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
Set colLoggedEvents = objWMIService.ExecQuery _
    (&quot;Select * from Win32_NTLogEvent &quot; _
        &amp; &quot;Where Logfile = &#39;System&#39;&quot;)
For Each objEvent in colLoggedEvents
    Wscript.Echo &quot;Category: &quot; &amp; objEvent.Category &amp; VBNewLine _
    &amp; &quot;Computer Name: &quot; &amp; objEvent.ComputerName &amp; VBNewLine _
    &amp; &quot;Event Code: &quot; &amp; objEvent.EventCode &amp; VBNewLine _
    &amp; &quot;Message: &quot; &amp; objEvent.Message &amp; VBNewLine _
    &amp; &quot;Record Number: &quot; &amp; objEvent.RecordNumber &amp; VBNewLine _
    &amp; &quot;Source Name: &quot; &amp; objEvent.SourceName &amp; VBNewLine _
    &amp; &quot;Time Written: &quot; &amp; objEvent.TimeWritten &amp; VBNewLine _
    &amp; &quot;Event Type: &quot; &amp; objEvent.Type &amp; VBNewLine _
    &amp; &quot;User: &quot; &amp; objEvent.User
Next</code></pre></td>
</tr>
</tbody>
</table>
<span data-codelanguage="PowerShell"></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>PowerShell</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>$strComputer = &quot;.&quot;
$colLogFiles = Get-WmiObject -Class Win32_NTLogEvent -ComputerName $strComputer | Where-Object {$_.LogFile -eq &#39;System&#39;}

foreach ($objEvent in $colLoggedEvents) 
{ 
    &quot;Category: &quot; + $objEvent.Category
    &quot;Computer Name: &quot; + $objEvent.ComputerName
    &quot;Event Code: &quot; + $objEvent.EventCode
    &quot;Message: &quot; + $objEvent.Message
    &quot;Record Number: &quot; + $objEvent.RecordNumber
    &quot;Source Name: &quot; + $objEvent.SourceName
    &quot;Time Written: &quot; + $objEvent.TimeWritten
    &quot;Event Type: &quot; + $objEvent.Type
    &quot;User: &quot; + $objEvent.Use
}</code></pre></td>
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

 

 




