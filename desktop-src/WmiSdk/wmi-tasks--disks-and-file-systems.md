---
Description: WMI tasks for disks and file systems obtain information about disk drive hardware state and logical volumes. For other examples, see the TechNet ScriptCenter at http://www.microsoft.com/technet.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d310e5e6-3b67-41bc-b5f2-cea33d0a7a2b
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: 'WMI Tasks: Disks and File Systems'
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WMI Tasks: Disks and File Systems

WMI tasks for disks and file systems obtain information about disk drive hardware state and logical volumes. For other examples, see the TechNet ScriptCenter at [http://www.microsoft.com/technet](Http://go.microsoft.com/fwlink/p/?linkid=84103).

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
<td>...find out how much disk space each user is currently using on a computer?</td>
<td>If you are using disk quotas, then use the [<strong>Win32_DiskQuota</strong>](https://msdn.microsoft.com/library/aa394136) class and retrieve the values of the <strong>User</strong> and <strong>DiskSpaceUsed</strong> properties.<br/> <span data-codelanguage="VisualBasic"></span>
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
Set colQuotas = objWMIService.ExecQuery (&quot;Select * from Win32_DiskQuota&quot;)
For each objQuota in colQuotas
    Wscript.Echo &quot;Volume: &quot;&amp; vbTab &amp;  objQuota.QuotaVolume
    Wscript.Echo &quot;User: &quot;&amp; vbTab &amp;  objQuota.User      
    Wscript.Echo &quot;Disk Space Used: &quot; &amp; vbTab &amp;  objQuota.DiskSpaceUsed
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
$colItems = Get-WmiObject -Class Win32_DiskQuota -ComputerName $strComputer
foreach ($objQuota in $colItems) 
{ 
    &quot;Volume: &quot; + $objQuota.QuotaVolume
    &quot;User: &quot; + $objQuota.User      
    &quot;Disk Space Used: &quot; + $objQuota.DiskSpaceUsed
}</code></pre></td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr class="even">
<td>...determine when a removable drive has been added to or removed from a computer?</td>
<td><p>Use a monitoring script that queries the [<strong>Win32_VolumeChangeEvent</strong>](https://msdn.microsoft.com/library/aa394516) class.</p>
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
Set colMonitoredEvents = objWMIService. ExecNotificationQuery( &quot;Select * from Win32_VolumeChangeEvent&quot;)
Do
    Set objLatestEvent = colMonitoredEvents.NextEvent
    Wscript.Echo objLatestEvent.DriveName
    Wscript.Echo objLatestEvent.EventType
    Wscript.Echo objLatestEvent.Time_Created
Loop</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="odd">
<td>...determine if a CD is in a CD-ROM drive?</td>
<td><p>Use the [<strong>Win32_CDROMDrive</strong>](https://msdn.microsoft.com/library/aa394081) class and the <strong>MediaLoaded</strong> property.</p>
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
Set objWMIService = GetObject(&quot;winmgmts:\\&quot; &amp; strComputer &amp; &quot;\root\cimv2&quot;)
Set colItems = objWMIService.ExecQuery( &quot;Select * from Win32_CDROMDrive&quot;)
For Each objItem in colItems
    Wscript.Echo &quot;Device ID: &quot; &amp; objItem.DeviceID
    Wscript.Echo &quot;Media Loaded: &quot; &amp; objItem.MediaLoaded
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
$colItems = Get-WmiObject -Class Win32_CDROMDrive -ComputerName $strComputer
foreach ($objItem in $colItems)
{
    &quot;Device ID: &quot; + $objItem.DeviceID
    &quot;MediaLoaded: &quot; + $objItem.MediaLoaded
}</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="even">
<td>...determine if a disk is in the floppy drive?</td>
<td><p>Use the [<strong>Win32_LogicalDisk</strong>](https://msdn.microsoft.com/library/aa394173) class and check the <strong>FreeSpace</strong> property. If the value is Null, then no disk is in the drive.</p>
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
Set objWMIService = GetObject( &quot;winmgmts:\\&quot; &amp; strComputer &amp; &quot;\root\cimv2&quot;)
Set colItems = objWMIService.ExecQuery (&quot;Select * From Win32_LogicalDisk Where DeviceID = &#39;A:&#39;&quot;)

For Each objItem in colItems
    intFreeSpace = objItem.FreeSpace
    If IsNull(intFreeSpace) Then
        Wscript.Echo &quot;There is no disk in the floppy drive.&quot;
    Else
        Wscript.Echo &quot;There is a disk in the floppy drive.&quot;
    End If
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
$colItems = Get-WmiObject -Class Win32_LogicalDisk -Namespace &quot;root\cimv2&quot; -ComputerName $strComputer | `
    Where-Object { $_.DeviceID -eq &quot;A:&quot; }

foreach ($objItem in $colItems)
{
    $intFreeSpace = $objItem.FreeSpace
    if ($intFreeSpace -eq $null) { &quot;There is no disk in the floppy drive.&quot; }
    else { &quot;There is a disk in the floppy drive.&quot; }
}</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="odd">
<td>...distinguish between a fixed hard disk and a removable hard disk?</td>
<td><p>Use the [<strong>Win32_LogicalDisk</strong>](https://msdn.microsoft.com/library/aa394173) class and check the value of the <strong>DriveType</strong> property.</p>
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
Set colDisks = objWMIService.ExecQuery _
    (&quot;Select * from Win32_LogicalDisk&quot;)
For Each objDisk in colDisks
    Wscript.Echo &quot;DeviceID: &quot;&amp; vbTab _
        &amp;  objDisk.DeviceID       
    Select Case objDisk.DriveType
        Case 1
            Wscript.Echo &quot;No root directory. &quot; &amp; &quot;Drive type could not be &quot; &amp; &quot;determined.&quot;
        Case 2
            Wscript.Echo &quot;DriveType: &quot;&amp; vbTab &amp;  &quot;Removable drive.&quot;
        Case 3
            Wscript.Echo &quot;DriveType: &quot;&amp; vbTab &amp;  &quot;Local hard disk.&quot;
        Case 4
            Wscript.Echo &quot;DriveType: &quot;&amp; vbTab &amp;  &quot;Network disk.&quot;      
        Case 5
            Wscript.Echo &quot;DriveType: &quot;&amp; vbTab &amp;  &quot;Compact disk.&quot;      
        Case 6
            Wscript.Echo &quot;DriveType: &quot;&amp; vbTab &amp;  &quot;RAM disk.&quot;   
        Case Else
            Wscript.Echo &quot;Drive type could not be&quot; &amp; &quot; determined.&quot;
    End Select
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
$colDisks = Get-WmiObject -Class Win32_LogicalDisk -ComputerName $strComputer 

foreach ($objDisk in $colDisks)
{
    &quot;DeviceID: &quot; + $objDisk.deviceID
    switch ($objDisk.DriveType)
    {
        &#39;1&#39; { &quot;No root directory. Drive type could not be determined.&quot; }
        &#39;2&#39; { &quot;DriveType: Removable drive.&quot; }
        &#39;3&#39; { &quot;DriveType: Local hard disk.&quot; }
        &#39;4&#39; { &quot;DriveType: Network disk.&quot; }
        &#39;5&#39; { &quot;DriveType: Compact disk.&quot; }
        &#39;6&#39; { &quot;DriveType: RAM disk.&quot; }
        default: { &quot;Drive type could not be determined.&quot; }

    }
}</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="even">
<td>...determine what file system is in use on a drive?</td>
<td><p>Use the [<strong>Win32_LogicalDisk</strong>](https://msdn.microsoft.com/library/aa394173) class and the <strong>FileSystem</strong> property.</p>
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
Set colDisks = objWMIService.ExecQuery (&quot;Select * from Win32_LogicalDisk&quot;)
For Each objDisk in colDisks
    Wscript.Echo &quot;DeviceID: &quot; &amp; objDisk.DeviceID       
    Wscript.Echo &quot;File System: &quot; &amp; objDisk.FileSystem
Next</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="odd">
<td>...determine how much free space is available on a drive?</td>
<td><p>Use the [<strong>Win32_LogicalDisk</strong>](https://msdn.microsoft.com/library/aa394173) class and the <strong>FreeSpace</strong> property.</p>
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
Set colDisks = objWMIService.ExecQuery (&quot;Select * from Win32_LogicalDisk&quot;)
For Each objDisk in colDisks
    Wscript.Echo &quot;DeviceID: &quot; &amp; objDisk.DeviceID       
    Wscript.Echo &quot;Free Disk Space: &quot; &amp; objDisk.FreeSpace
Next</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="even">
<td>...determine the size of a drive?</td>
<td><p>Use the [<strong>Win32_LogicalDisk</strong>](https://msdn.microsoft.com/library/aa394173) class, and the <strong>Size</strong> property.</p>
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
Set colDisks = objWMIService.ExecQuery (&quot;Select * from Win32_LogicalDisk&quot;)
For Each objDisk in colDisks
    Wscript.Echo &quot;DeviceID: &quot; &amp; objDisk.DeviceID       
    Wscript.Echo &quot;Disk Size: &quot; &amp; objDisk.Size
Next</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="odd">
<td>...find out what drives are mapped on a computer?</td>
<td><p>Use the [<strong>Win32_MappedLogicalDisk</strong>](https://msdn.microsoft.com/library/aa394194) class.</p>
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
Set colDisks = objWMIService. ExecQuery(&quot;Select * from Win32_MappedLogicalDisk&quot;)
For Each objDisk in colDisks
    Wscript.Echo &quot;Device ID: &quot; &amp; objDisk.DeviceID
    Wscript.Echo &quot;Name: &quot; &amp; objDisk.Name
    Wscript.Echo &quot;Free Space: &quot; &amp; objDisk.FreeSpace
    Wscript.Echo &quot;Size: &quot; &amp; objDisk.Size
Next</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="even">
<td>...defragment a hard disk?</td>
<td><p>Use the [<strong>Win32_Volume</strong>](https://msdn.microsoft.com/library/aa394515) class and the [<strong>Defrag</strong>](https://msdn.microsoft.com/library/aa389832) method.</p>
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
Set objWMIService = GetObject(&quot;winmgmts:\\&quot; &amp; strComputer &amp; &quot;\root\cimv2&quot;)
Set colVolumes = objWMIService.ExecQuery (&quot;Select * from Win32_Volume Where Name = &#39;K:\\&#39;&quot;)
For Each objVolume in colVolumes
     errResult = objVolume.Defrag()
Next</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="odd">
<td>...detect which drive letter is associated with a logical disk partition?</td>
<td><ol>
<li>Start with the [<strong>Win32_DiskDrive</strong>](https://msdn.microsoft.com/library/aa394132) class and query for instances of [<strong>Win32_DiskPartition</strong>](https://msdn.microsoft.com/library/aa394135) using the <strong>DeviceID</strong> property and the [<strong>Win32_DiskDriveToDiskPartition</strong>](https://msdn.microsoft.com/library/aa394134) association class. Now you have a collection of the partitions on the physical drive.</li>
<li>Query for the [<strong>Win32_LogicalDisk</strong>](https://msdn.microsoft.com/library/aa394173) that represents the partition using the [<strong>Win32_DiskPartition.DeviceID</strong>](https://msdn.microsoft.com/library/aa394135) property and [<strong>Win32_LogicalDiskToPartition</strong>](https://msdn.microsoft.com/library/aa394175) association class.</li>
<li>Get the drive letter from the [<strong>Win32_LogicalDisk.DeviceID</strong>](https://msdn.microsoft.com/library/aa394173).</li>
</ol>
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
<td><pre><code>ComputerName = &quot;.&quot;
Set wmiServices  = GetObject ( _
    &quot;winmgmts:{impersonationLevel=Impersonate}!//&quot; &amp; ComputerName)
&#39; Get physical disk drive
Set wmiDiskDrives =  wmiServices.ExecQuery ( &quot;SELECT Caption, DeviceID FROM Win32_DiskDrive&quot;)

For Each wmiDiskDrive In wmiDiskDrives
    WScript.Echo &quot;Disk drive Caption: &quot; &amp; wmiDiskDrive.Caption &amp; VbNewLine &amp; &quot;DeviceID: &quot; &amp; &quot; (&quot; &amp; wmiDiskDrive.DeviceID &amp; &quot;)&quot;

    &#39;Use the disk drive device id to
    &#39; find associated partition
    query = &quot;ASSOCIATORS OF {Win32_DiskDrive.DeviceID=&#39;&quot; _
        &amp; wmiDiskDrive.DeviceID &amp; &quot;&#39;} WHERE AssocClass = Win32_DiskDriveToDiskPartition&quot;    
    Set wmiDiskPartitions = wmiServices.ExecQuery(query)

    For Each wmiDiskPartition In wmiDiskPartitions
        &#39;Use partition device id to find logical disk
        Set wmiLogicalDisks = wmiServices.ExecQuery _
            (&quot;ASSOCIATORS OF {Win32_DiskPartition.DeviceID=&#39;&quot; _
             &amp; wmiDiskPartition.DeviceID &amp; &quot;&#39;} WHERE AssocClass = Win32_LogicalDiskToPartition&quot;) 

        For Each wmiLogicalDisk In wmiLogicalDisks
            WScript.Echo &quot;Drive letter associated&quot; _
                &amp; &quot; with disk drive = &quot; _ 
                &amp; wmiDiskDrive.Caption _
                &amp; wmiDiskDrive.DeviceID _
                &amp; VbNewLine &amp; &quot; Partition = &quot; _
                &amp; wmiDiskPartition.DeviceID _
                &amp; VbNewLine &amp; &quot; is &quot; _
                &amp; wmiLogicalDisk.DeviceID
        Next      
    Next
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

 

 



`
