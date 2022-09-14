---
description: WMI provides a standardized system management infrastructure that can be leveraged by a number of different clients.
ms.assetid: 7aa0ead7-010c-4ad2-b6ba-0ef84263d5c6
ms.tgt_platform: multiple
title: Creating WMI Clients
ms.topic: article
ms.date: 05/31/2018
---

# Creating WMI Clients

WMI provides a standardized system management infrastructure that can be leveraged by a number of different clients. These clients range from the wmic.exe command line tool to System Center Operations Manager. You can write your own WMI clients by using either the WMI Scripting API, the native C++ API or by using the types in the System.Management .NET Framework class library namespace.

## How to create a WMI client

The core functionality of WMI consists of retrieving objects from the WMI repository and examining the properties of those objects. You can also choose to update those properties, or call methods on those properties. The following examples show how to perform a basic WMI administration task: retrieving the name of the local computer.



<table>
<colgroup>
<col  />
<col  />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><span id="Creating_a_client_with_PowerShell"></span><span id="creating_a_client_with_powershell"></span><span id="CREATING_A_CLIENT_WITH_POWERSHELL"></span>Creating a client with PowerShell<br/></td>
<td>WMI and PowerShell are tightly integrated; as such, retrieving WMI objects with PowerShell is simply a matter of calling the Get-WmiObject cmdlet. Note that for consistency, the first code snippet explicitly states many of the default values; the second assumes that the default values are correct.<br/> <span data-codelanguage="PowerShell"></span>
<table>
<colgroup>
<col  />
</colgroup>
<thead>
<tr class="header">
<th>PowerShell</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>#explicitly states many of the default parameters
$myComputer = Get-WmiObject -ComputerName &quot;.&quot; -Namespace &quot;root\cimv2&quot; -Query &quot;SELECT * FROM Win32_ComputerSystem&quot;
foreach ($computer in $myComputer)
{ &quot;System Name: &quot; + $computer.name }

#assumes the default values are correct
Get-WmiObject Win32_ComputerSystem | Format-Table &quot;Name&quot;</code></pre></td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr class="even">
<td><p><span id="Creating_a_client_with_VBScript"></span><span id="creating_a_client_with_vbscript"></span><span id="CREATING_A_CLIENT_WITH_VBSCRIPT"></span>Creating a client with VBScript</p></td>
<td><p>VBScript was the original scripting language that had common use with WMI. While PowerShell has become more popular, many of the existing code samples in this documentation are written in VBScript. Note that this particular VBScript sample explicitly states both the local machine path as well as the impersonation level; this is not required, but is often a best practice.</p>
<div class="code">
<span data-codelanguage="VisualBasic"></span>
<table>
<colgroup>
<col  />
</colgroup>
<thead>
<tr class="header">
<th>VB</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>strComputer = &quot;.&quot;
Set objWMIService = GetObject(&quot;winmgmts:{impersonationLevel=impersonate}!\\&quot; & strComputer & &quot;\root\cimv2&quot;)
Set colItems = objWMIService.ExecQuery(&quot;Select * from Win32_ComputerSystem&quot;)
For Each objItem in colItems
    Wscript.Echo &quot;Computer Name: &quot; & objItem.Name
Next</code></pre></td>
</tr>
</tbody>
</table>

</div></td>
</tr>
<tr class="odd">
<td><p><span id="Creating_a_client_with_C___Microsoft.Management.Infrastructure_"></span><span id="creating_a_client_with_c___microsoft.management.infrastructure_"></span><span id="CREATING_A_CLIENT_WITH_C___MICROSOFT.MANAGEMENT.INFRASTRUCTURE_"></span>Creating a client with C# (<a href="/previous-versions/windows/desktop/wmi_v2/mi-managed-api/hh832958(v=vs.85)">Microsoft.Management.Infrastructure</a>)</p></td>
<td><p>This namespace contains the current solution for accessing WMI with managed code, and is known as the Windows Management Infrastructure (MI, or WMIv2). Currently, MI is the supported technology for creating managed management clients. For more information, see <a href="/previous-versions/windows/desktop/wmi_v2/how-to-implement-a-managed-mi-client">How to Implement a Managed MI Client</a> and <a href="/previous-versions/windows/desktop/wmi_v2/how-to-implement-a-native-mi-client">How to Implement a Native MI Client</a>.</p>
<div class="code">
<span data-codelanguage="CSharp"></span>
<table>
<colgroup>
<col  />
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
<td><p><span id="Creating_a_client_with_C___System.Management_"></span><span id="creating_a_client_with_c___system.management_"></span><span id="CREATING_A_CLIENT_WITH_C___SYSTEM.MANAGEMENT_"></span>Creating a client with C# (<a href="/dotnet/api/system.management">System.Management</a>)</p></td>
<td><p>This namespace contains the original solution for accessing WMI with managed code. While the <a href="/dotnet/api/system.management">System.Management</a> classes are still available, the <a href="/previous-versions/windows/desktop/wmi_v2/mi-managed-api/hh832958(v=vs.85)">Microsoft.Management.Infrastructure</a> classes are generally more efficient and scale better. As such, it is recommended that you use the MI classes, rather than the original WMI classes.</p>
<div class="code">
<span data-codelanguage="CSharp"></span>
<table>
<colgroup>
<col  />
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
</tbody>
</table>



 

The following table lists the topics covered in this section.



| Topic                                                                                                        | Description                                                                                                                                                                                    |
|--------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Connecting to WMI on a Remote Computer](connecting-to-wmi-on-a-remote-computer.md)                         | Describes a number of issues that arise when clients use the WMI infrastructure on a remote computer.                                                                                          |
| [WMI Tasks for Scripts and Applications](wmi-tasks-for-scripts-and-applications.md)                         | Shows example WMI client code.                                                                                                                                                                 |
| [Creating a WMI Application or Script](creating-a-wmi-application-or-script.md)                             | Provides information about creating various WMI clients.                                                                                                                                       |
| [Monitoring Performance Data](monitoring-performance-data.md)                                               | Describes how to use WMI to monitor performance data.                                                                                                                                          |
| [Receiving a WMI Event](receiving-a-wmi-event.md)                                                           | Describes how to view WMI events.                                                                                                                                                              |
| [Monitoring Events](monitoring-events.md)                                                                   | Describes how to monitor WMI events.                                                                                                                                                           |
| [Querying with WQL](querying-with-wql.md)                                                                   | Introduces the WMI Query Language (WQL).                                                                                                                                                       |
| [Querying the Status of Optional Features](querying-the-status-of-optional-features.md)                     | In Windows 7, WMI implemented the [**Win32\_OptionalFeature**](/windows/desktop/CIMWin32Prov/win32-optionalfeature) class. This class retrieves the status of the optional features that are present on a computer. |
| [Describing the Location of a WMI Object](describing-the-location-of-a-wmi-object.md)                       | Focuses on the syntax for describing the location of a WMI managed entity.                                                                                                                     |
| [Accessing Other Operating System Features with WMI](accessing-other-operating-system-features-with-wmi.md) | Describes how to write WMI clients that access device drivers, Active Directory, and SNMP devices.                                                                                             |
| [Accessing Data in the Interop Namespace](accessing-data-in-the-interop-namespace.md)                       | Association providers enable Windows Management Instrumentation (WMI) clients to traverse and retrieve profiles and associated class instances from different namespaces.                      |
| [Manipulating Class and Instance Information](manipulating-class-and-instance-information.md)               | Describes the common tasks that WMI clients must perform.                                                                                                                                      |
| [Linking Classes Together](linking-classes-together.md)                                                     | Discusses the view provider and how it can be used to bring together information from multiple WMI classes.                                                                                    |
| [Modifying the System Registry](modifying-the-system-registry.md)                                           | Describes how WMI clients can use WMI to manage system registry information.                                                                                                                   |



 

