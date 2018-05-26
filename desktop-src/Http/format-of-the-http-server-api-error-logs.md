---
title: Format of the HTTP Server API Error Logs
description: In general, HTTP Server API error log files have the same format as W3C error logs except that HTTP Server API error log files do not contain column headings.
ms.assetid: 436f898c-9063-4aee-b276-e6ab935e3606
keywords:
- HTTP Server API, error log format
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Format of the HTTP Server API Error Logs

In general, HTTP Server API error log files have the same format as W3C error logs except that HTTP Server API error log files do not contain column headings. Each line of an HTTP Server API error log records one error with fields in a specific order. Each field is separated from the preceding field by a single space character (0x0020). Within each field, space characters, tabs, and unprintable control characters are replaced by plus signs (0x002B).

The following table identifies the fields and the order of the fields in an error log record.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><span id="Date"></span><span id="date"></span><span id="DATE"></span>Date<br/></td>
<td>The Date field follows the W3C format and is based on Coordinated Universal Time (UTC).The Date field is always 10 characters in the form of &quot;YYYY-MM-DD&quot;. For example, May 1, 2003 is expressed as &quot;2003-05-01&quot;.<br/></td>
</tr>
<tr class="even">
<td><span id="Time"></span><span id="time"></span><span id="TIME"></span>Time<br/></td>
<td>The Time field follows the W3C format and is based on UTC. The time field is always 8 characters in the form of &quot;MM:HH:SS&quot;. For example, 5:30 PM (UTC) is expressed as &quot;17:30:00&quot;.<br/></td>
</tr>
<tr class="odd">
<td><span id="Client_IP_Address"></span><span id="client_ip_address"></span><span id="CLIENT_IP_ADDRESS"></span>Client IP Address<br/></td>
<td>The IP address of the affected client that can be either an IPv4 address or an IPv6 address. If the client IP address is an IPv6 address, the ScopeId field is also included in the address.<br/></td>
</tr>
<tr class="even">
<td><span id="Client_Port"></span><span id="client_port"></span><span id="CLIENT_PORT"></span>Client Port<br/></td>
<td>The port number for the affected client.<br/></td>
</tr>
<tr class="odd">
<td><span id="Server_IP_Address"></span><span id="server_ip_address"></span><span id="SERVER_IP_ADDRESS"></span>Server IP Address<br/></td>
<td>The IP address of the affected server that can be either an IPv4 address or an IPv6 address. If the server IP address is an IPv6 address, the ScopeId field is also included in the address.<br/></td>
</tr>
<tr class="even">
<td><span id="Server_Port"></span><span id="server_port"></span><span id="SERVER_PORT"></span>Server Port<br/></td>
<td>The port number of the affected server.<br/></td>
</tr>
<tr class="odd">
<td><span id="Protocol_Version"></span><span id="protocol_version"></span><span id="PROTOCOL_VERSION"></span>Protocol Version<br/></td>
<td>The version of the protocol that is being used. <br/>
<ul>
<li>If the connection has not been parsed enough to determine the protocol version, then a hyphen (0x002D) is used as a placeholder for the empty field.</li>
<li>If either the major or minor version number parsed is greater than or equal to 10, the version is logged as &quot;HTTP/?.?&quot;.</li>
</ul></td>
</tr>
<tr class="even">
<td><span id="Verb"></span><span id="verb"></span><span id="VERB"></span>Verb<br/></td>
<td>The verb state passed by the last request parsed. Unknown verbs are included, but any verb that is more than 255 bytes is truncated to this length. If a verb is not available, a hyphen (0x002D) is used as a placeholder for the empty field.<br/></td>
</tr>
<tr class="odd">
<td><span id="CookedURL___Query"></span><span id="cookedurl___query"></span><span id="COOKEDURL___QUERY"></span>CookedURL + Query<br/></td>
<td>The URL and any query associated with it are logged as one field, separated by a question mark (0x3F). This field is truncated at its length limit of 4096 bytes.
<ul>
<li>If this URL has been parsed (&quot;cooked&quot;), it is logged with local code page conversion, and is treated as a Unicode field.</li>
<li>If this URL has not been parsed (&quot;cooked&quot;) at the time of logging, it is copied exactly, without any Unicode conversion.</li>
<li>If the HTTP Server API cannot parse this URL, a hyphen (0x002D) is used as a placeholder for the empty field.</li>
</ul>
<br/></td>
</tr>
<tr class="even">
<td><span id="Protocol_Status"></span><span id="protocol_status"></span><span id="PROTOCOL_STATUS"></span>Protocol Status<br/></td>
<td>The protocol status cannot exceed 999. <br/>
<ul>
<li>If the protocol status of the response to a request is available, it is logged in this field.</li>
<li>If the protocol status is not available, a hyphen (0x002D) is used as a placeholder for the empty field.</li>
</ul></td>
</tr>
<tr class="odd">
<td><span id="SiteId"></span><span id="siteid"></span><span id="SITEID"></span>SiteId<br/></td>
<td>Not used in this version of the HTTP Server API. A placeholder hyphen (0x002D) always appears in this field.<br/></td>
</tr>
<tr class="even">
<td><span id="Reason_Phrase"></span><span id="reason_phrase"></span><span id="REASON_PHRASE"></span>Reason Phrase<br/></td>
<td>This field contains a string that identifies the kind of error that is being logged. It is never left empty.<br/></td>
</tr>
</tbody>
</table>



 

The following sample lines are from an HTTP Server API error log:

``` syntax
2002-07-05 18:45:09 172.31.77.6 2094 172.31.77.6 80 
                    HTTP/1.1 GET /qos/1kbfile.txt 503 - ConnLimit
2002-07-05 19:51:59 127.0.0.1 2780 127.0.0.1 80 
                    HTTP/1.1 GET /ThisIsMyUrl.htm 400 - Hostname
2002-07-05 19:53:00 127.0.0.1 2894 127.0.0.1 80 
                    HTTP/2.0 GET / 505 - Version_N/S
2002-07-05 20:06:01 172.31.77.6 64388 127.0.0.1 80 
                    - - - - - Timer_MinBytesPerSecond
```

 

 





