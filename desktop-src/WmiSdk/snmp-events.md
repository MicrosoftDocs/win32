---
description: The SNMP provider supports writing to log files and to the debugger.
ms.assetid: 66627927-2eee-4d56-a74b-f86147ad7711
ms.tgt_platform: multiple
title: SNMP Events
ms.topic: article
ms.date: 05/31/2018
---

# SNMP Events

The SNMP provider supports writing to log files and to the debugger.

> [!Note]  
> For more information about installing the provider, see [Setting up the WMI SNMP Environment](setting-up-the-wmi-snmp-environment.md).

 

A number of registry keys and values define the level and type of logging currently being generated:

-   Debugging

    The **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\MICROSOFT\\WBEM\\PROVIDERS\\LOGGING** registry key contains the logging value that indicates whether information can be written to the debugger. The logging value is set either to 0 to disable debugging output or 1 to enable it. Logging is a REG\_DWORD value.

-   Logging

    The **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\MICROSOFT\\WBEM\\PROVIDERS\\LOGGING\\WBEMSNMP** registry key holds all of the logging information specific to the SNMP provider. The following table lists the values associated with this key.



<table>
<colgroup>
<col  />
<col  />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Type</td>
<td><strong>REG_SZ</strong><br/> Takes one of the following values:<br/> &quot;File&quot; = (Default) Sends debugging output to a file.<br/> &quot;Debugger&quot; = Sends debugging output to the debugger.<br/></td>
</tr>
<tr class="even">
<td>MaxFileSize</td>
<td><strong>REG_DWORD</strong><br/> Takes integer values from 1024 to 2^32-1. The value is the maximum allowed size in bytes for the log file. If less than 1024, the logging mechanism uses a value of 1024. A minimum size of 8 KB is recommended for this value. When the file reaches the size specified by MaxFileSize, the file name is prepended with a '~' character and a new file is created. Therefore, the maximum disk space required for logging is twice this value.<br/></td>
</tr>
<tr class="odd">
<td>File</td>
<td><strong>REG_SZ</strong><br/> Defines the name of the file to which the debugging output is sent when the logging type is set to 'File'. The default value is '<WBEMLOGS>\wbemsnmp.log.' If the <WBEMLOGS> directory cannot be determined from the WMI registry section, the value defaults to 'c:\wbemsnmp.log'. If a share is used, such as \\machine\share\wbemsnmp.log or M:\wbemsnmp.log where M: is \\machine\share, the local SYSTEM account on which WMI runs must have read/write access rights to the \\machine\share.<br/></td>
</tr>
<tr class="even">
<td>Level</td>
<td><strong>REG_DWORD</strong><br/> Takes integer values from 0 through 2^32-1. The value is a logical mask consisting of 32 bits. The following bit masks are combined to define the type of debugging output generated:<br/>
<ul>
<li>0: SNMP class provider <a href="/windows/desktop/api/WbemCli/nn-wbemcli-iwbemservices"><strong>IWbemServices</strong></a> method invocations</li>
<li>1: SNMP class provider implementation</li>
<li>2: SNMP instance provider <a href="/windows/desktop/api/WbemCli/nn-wbemcli-iwbemservices"><strong>IWbemServices</strong></a> method invocations</li>
<li>3: SNMP instance provider implementation</li>
<li>4: SNMP class library</li>
<li>5: SNMP SMIR</li>
<li>6: SNMP correlator</li>
<li>7: SNMP type mapping code</li>
<li>8: SNMP threading code</li>
<li>9: SNMP event provider interfaces and implementation</li>
</ul>
Set Level to (2^0 + 2^8=) 257 for operations involving calls to the SNMP class provider <a href="/windows/desktop/api/WbemCli/nn-wbemcli-iwbemservices"><strong>IWbemServices</strong></a> methods, and operations using SNMP threading code.<br/></td>
</tr>
</tbody>
</table>



 

 

 




