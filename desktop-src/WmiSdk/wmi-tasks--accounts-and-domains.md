---
Description: Account and domain administrative tasks obtain information such as the computer domain or the currently logged-on user.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1a9cc44b-c366-465d-a0d0-536d5dc818b5
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: 'WMI Tasks: Accounts and Domains'
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WMI Tasks: Accounts and Domains

Account and domain administrative tasks obtain information such as the computer domain or the currently logged-on user. Many of these tasks are best performed with [ADSI](https://msdn.microsoft.com/library/aa772170) scripts. For more information and other examples, see the TechNet [ScriptCenter](http://go.microsoft.com/fwlink/p/?linkid=46710) Script Repository.

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
<td>...determine the domain in which a computer belongs?</td>
<td>Use the [<strong>Win32_ComputerSystem</strong>](https://msdn.microsoft.com/library/aa394102) class and check the value of the <strong>Domain</strong> property. You can also use the <strong>DNSDomain</strong> property in [<strong>Win32_NetworkAdapterConfiguration</strong>](https://msdn.microsoft.com/library/aa394217).<br/> <span data-codelanguage="VisualBasic"></span>
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
Set objWMIService = GetObject(&quot;winmgmts:{impersonationLevel=impersonate}!\\&quot; &amp; strComputer &amp; &quot;\root\cimv2&quot;)
Set colSettings = objWMIService.ExecQuery(&quot;Select * from Win32_ComputerSystem&quot;)

For Each objComputer in colSettings 
    Wscript.Echo &quot;System Name: &quot; &amp; objComputer.Name
    Wscript.Echo &quot;Domain: &quot; &amp; objComputer.Domain
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
<td><pre><code>$computer = Get-WmiObject -Class Win32_ComputerSystem
&quot;System Name: {0}&quot; -f $computer.name
&quot;Domain : {0}&quot; -f $computer.domain</code></pre></td>
</tr>
</tbody>
</table>
<span data-codelanguage="CSharp"></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C#</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>using Microsoft.Management.Infrastructure;
...
CimSession session = CimSession.Create(&quot;localHost&quot;);
IEnumerable&lt;CimInstance&gt; queryInstance = session.QueryInstances(@&quot;root\cimv2&quot;, &quot;WQL&quot;, &quot;SELECT * FROM Win32_ComputerSystem&quot;);

foreach (CimInstance cimObj in queryInstance)
{
   Console.WriteLine(cimObj.CimInstanceProperties[&quot;Name&quot;].ToString());
   Console.WriteLine(cimObj.CimInstanceProperties[&quot;Domain&quot;].ToString());
}</code></pre></td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr class="even">
<td>...determine whether a computer is a server or a workstation?</td>
<td><p>Use the [<strong>Win32_ComputerSystem</strong>](https://msdn.microsoft.com/library/aa394102) class and the <strong>DomainRole</strong> property.</p>
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
Set objWMIService = GetObject(&quot;winmgmts:{impersonationLevel=impersonate}!\\&quot; &amp; strComputer &amp; &quot;\root\cimv2&quot;)
Set colComputers = objWMIService.ExecQuery(&quot;Select DomainRole from Win32_ComputerSystem&quot;)
For Each objComputer in colComputers
    Select Case objComputer.DomainRole 
        Case 0 
            strComputerRole = &quot;Standalone Workstation&quot;
        Case 1        
            strComputerRole = &quot;Member Workstation&quot;
        Case 2
            strComputerRole = &quot;Standalone Server&quot;
        Case 3
            strComputerRole = &quot;Member Server&quot;
        Case 4
            strComputerRole = &quot;Backup Domain Controller&quot;
        Case 5
            strComputerRole = &quot;Primary Domain Controller&quot;
    End Select
    Wscript.Echo strComputerRole
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
<td><pre><code>$Computer = Get-WmiObject -Class Win32_ComputerSystem 

&quot;Computer `&quot;{0}.{1}`&quot; is a: &quot;-f $Computer.Name,$computer.domain

switch  ($computer.DomainRole) {
    0 {&quot;Standalone Workstation&quot;}
    1 {&quot;Member Workstation&quot;}
    2 {&quot;Standalone Server&quot;}
    3 {&quot;Member Server&quot;}
    4 {&quot;Backup Domain Controller&quot;}
    5 {&quot;Primary Domain Controller&quot;}
}</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="odd">
<td>...determine the computer name?</td>
<td><p>Use the [<strong>Win32_ComputerSystem</strong>](https://msdn.microsoft.com/library/aa394102) class and the <strong>Name</strong> property. You can also use the <strong>DNSHostName</strong> property in [<strong>Win32_NetworkAdapterConfiguration</strong>](https://msdn.microsoft.com/library/aa394217).</p>
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
Set objWMIService = GetObject(&quot;winmgmts:{impersonationLevel=impersonate}!\\&quot; &amp; strComputer &amp; &quot;\root\cimv2&quot;)
Set colItems = objWMIService.ExecQuery(&quot;Select * from Win32_ComputerSystem&quot;)
For Each objItem in colItems
    Wscript.Echo &quot;Computer Name: &quot; &amp; objItem.Name
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
<td><pre><code>$Computer = Get-WmiObject -Class Win32_ComputerSystem
&quot;Computer Name is: {0}&quot; -f $Computer.Name</code></pre></td>
</tr>
</tbody>
</table>
<span data-codelanguage="CSharp"></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C#</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>using Microsoft.Management.Infrastructure;
...
CimSession session = CimSession.Create(&quot;localHost&quot;);
IEnumerable&lt;CimInstance&gt; queryInstance = session.QueryInstances(@&quot;root\cimv2&quot;, &quot;WQL&quot;, &quot;SELECT * FROM Win32_ComputerSystem&quot;);

foreach (CimInstance cimObj in queryInstance)
{
   Console.WriteLine(cimObj.CimInstanceProperties[&quot;Name&quot;].ToString());
}</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="even">
<td>...find the name of the person currently logged on to a computer?</td>
<td><p>Use the [<strong>Win32_ComputerSystem</strong>](https://msdn.microsoft.com/library/aa394102) class and the <strong>UserName</strong> property.</p>
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
Set objWMIService = GetObject(&quot;winmgmts:{impersonationLevel=impersonate}!\\&quot; &amp; strComputer &amp; &quot;\root\cimv2&quot;) 
Set colComputer = objWMIService.ExecQuery(&quot;Select * from Win32_ComputerSystem&quot;)
 
For Each objComputer in colComputer
    Wscript.Echo &quot;User Name = &quot; &amp; objComputer.UserName &amp; VBNewLine &amp; &quot;Computer Name = &quot; &amp; objComputer.Name
WScript.Echo objComputer.UserName
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
<td><pre><code>$computers = Get-WmiObject -Class Win32_ComputerSystem 
&quot;Logged on user(s):&quot;
foreach($computer in $computers) {
   &quot;User: {0}&quot; -f $computer.UserName
}</code></pre></td>
</tr>
</tbody>
</table>
<span data-codelanguage="CSharp"></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C#</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>using Microsoft.Management.Infrastructure;
...
CimSession session = CimSession.Create(&quot;localHost&quot;);
IEnumerable&lt;CimInstance&gt; queryInstance = session.QueryInstances(@&quot;root\cimv2&quot;, &quot;WQL&quot;, &quot;SELECT * FROM Win32_ComputerSystem&quot;);

foreach (CimInstance cimObj in queryInstance)
{
   Console.WriteLine(&quot;User Name: &quot; + cimObj.CimInstanceProperties[&quot;UserName&quot;].ToString());
}</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="odd">
<td>...rename a computer?</td>
<td><p>Use the [<strong>Win32_ComputerSystem</strong>](https://msdn.microsoft.com/library/aa394102) class, and the <strong>Rename</strong> method.</p>
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
Set colComputers = objWMIService.ExecQuery(&quot;Select * from Win32_ComputerSystem&quot;)
For Each objComputer in colComputers
    errReturn = ObjComputer.Rename(&quot;NewName&quot;)
    WScript.Echo &quot;Computer name is now &quot; &amp; objComputer.Name
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
<td><pre><code>param (
[$String] $NewName = &#39;NewName&#39;,
[$string] $Comp = &quot;.&quot;
}

# Get computer object
$Computer = Get-WmiObject -Class Win32_ComputerSystem -ComputerName $comp

#Rename the Computer
$Return  = $Computer.Rename($NewName)

if ($return.ReturnValue -eq 0) {
   &quot;Computer name is now: $NewName&quot;
   &quot; but you need to reboot first&quot;
} else {
&quot;  RenameFailed, return code: {0}&quot; -f $return.ReturnValue
}</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="even">
<td>...retrieve only local groups using WMI?</td>
<td><p>Use the [<strong>Win32_Group</strong>](https://msdn.microsoft.com/library/aa394151) class and include the following <strong>WHERE</strong> clause in your [WQL](querying-with-wql.md) query.</p>
<p><code>Where LocalAccount = True</code></p>
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
Set objWMIService = GetObject( _
    &quot;winmgmts:\\&quot; &amp; strComputer &amp; &quot;\root\cimv2&quot;)
Set colItems = objWMIService.ExecQuery _
    (&quot;Select * from Win32_Group  Where LocalAccount = True&quot;)
For Each objItem in colItems
    Wscript.Echo &quot;Local Account: &quot; &amp; objItem.LocalAccount &amp; VBNewLine _
        &amp; &quot;Name: &quot; &amp; objItem.Name &amp; VBNewLine _
        &amp; &quot;SID: &quot; &amp; objItem.SID &amp; VBNewLine _
        &amp; &quot;SID Type: &quot; &amp; objItem.SIDType &amp; VBNewLine _
        &amp; &quot;Status: &quot; &amp; objItem.Status &amp; VBNewLine
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
<td><pre><code>$Accts=Get-WMIObjectWin32_Group|where {$_.LocalAccount}
$accts |ftName, Sid, SidType, Status-autosize</code></pre></td>
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

 

 




