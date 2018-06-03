---
title: Event Tracing in LDAP Applications
description: Windows Server 2008 and Windows Vista introduce Event Tracing for applications that use Lightweight Directory Access Protocol.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 4ef640de-a563-434f-b89a-80554b4fbc60
ms.prod: windows-server-dev
ms.technology: active-directory-lightweight-directory-services
ms.tgt_platform: multiple
keywords:
- event tracing LDAP
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Event Tracing in LDAP Applications

Windows Server 2008 and Windows Vista introduce [Event Tracing](https://msdn.microsoft.com/library/windows/desktop/bb968803) for applications that use [Lightweight Directory Access Protocol](lightweight-directory-access-protocol-ldap-api.md). Certain areas of the LDAP Provider have an underlying implementation that is complex or that involves a sequence of steps that makes diagnosis of problems in these areas more difficult. Event Tracing can be a valuable troubleshooting tool.

To turn on LDAP client tracing, create the following registry key:

**HKEY\_LOCAL\_MACHINE**\\**System**\\**CurrentControlSet**\\**Services**\\**ldap**\\**Tracing**\\***ProcessName***

*ProcessName* is the full name of the process that you want to trace, including its extension (for example, "Svchost.exe"). Inside this key, you can place an optional value of type DWORD that is named "PID". If this optional value is set to a process ID, only the instance of the application with this process ID will be traced.

To start a tracing session, execute the following command:

**tracelog.exe -start** *SessionName* **-guid \#***GUIDforLDAPTracingProvider* **-f** *FileName* **-flag &lt;***TraceFlags***&gt;**

*SessionName* is an arbitrary identifier that is used to label the tracing session (you will need to refer to this session name later when you stop the tracing session). The GUID for the LDAP tracing provider is "099614a5-5dd7-4788-8bc9-e29f43db28fc". *FileName* specifies the log file to which events will be written. *TraceFlags* should be one or more of the following values.



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Flag name</th>
<th>Flag value</th>
<th>Flag description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>DEBUG_SEARCH</strong><br/></td>
<td>0x00000001<br/></td>
<td>Logs search requests and the parameters passed to them. Responses are not logged here, only the search requests. (Responses to search requests can be logged by using <strong>DEBUG_SPEWSEARCH</strong>.)<br/> <strong>Windows Server 2008 and Windows Vista:</strong> The flag name was <strong>DEBUG_TRACE1</strong>.<br/></td>
</tr>
<tr class="even">
<td><strong>DEBUG_WRITE</strong><br/></td>
<td>0x00000002<br/></td>
<td>Logs write requests and the parameters passed to them. This includes the operations: add, delete, modify, and extended.<br/> <strong>Windows Server 2008 and Windows Vista:</strong> The flag name was <strong>DEBUG_TRACE2</strong>.<br/></td>
</tr>
<tr class="odd">
<td><strong>DEBUG_REFCNT</strong><br/></td>
<td>0x00000004<br/></td>
<td>Logs reference counting data and operations for connections and requests.<br/></td>
</tr>
<tr class="even">
<td><strong>DEBUG_HEAP</strong><br/></td>
<td>0x00000008<br/></td>
<td>Logs all memory allocations and memory frees.<br/></td>
</tr>
<tr class="odd">
<td><strong>DEBUG_CACHE</strong><br/></td>
<td>0x00000010<br/></td>
<td>Logs cache activity. This includes adds, removes, hits, misses, and so on.<br/></td>
</tr>
<tr class="even">
<td><strong>DEBUG_SSL</strong><br/></td>
<td>0x00000020<br/></td>
<td>Logs SSL information and errors.<br/></td>
</tr>
<tr class="odd">
<td><strong>DEBUG_SPEWSEARCH</strong><br/></td>
<td>0x00000040<br/></td>
<td>Logs all server responses to search requests. This includes attributes requested, as well as all data that was received.<br/> <strong>Windows Server 2008 and Windows Vista:</strong> Only available in debug builds.<br/></td>
</tr>
<tr class="even">
<td><strong>DEBUG_SERVERDOWN</strong><br/></td>
<td>0x00000080<br/></td>
<td>Logs server down and connection errors.<br/></td>
</tr>
<tr class="odd">
<td><strong>DEBUG_CONNECT</strong><br/></td>
<td>0x00000100<br/></td>
<td>Logs data related to establishing a connection.<br/>
<blockquote>
[!Note]<br />
Other connection related data will be logged in <strong>DEBUG_CONNECTION</strong>.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td><strong>DEBUG_RECONNECT</strong><br/></td>
<td>0x00000200<br/></td>
<td>Logs automatic reconnect activity. This includes reconnect attempts, failures, and related errors.<br/></td>
</tr>
<tr class="odd">
<td><strong>DEBUG_RECEIVEDATA</strong><br/></td>
<td>0x00000400<br/></td>
<td>Logs info related to receiving messages from the server. This includes events such as response received from server, waiting on response from server, and so on.<br/></td>
</tr>
<tr class="even">
<td><strong>DEBUG_BYTES_SENT</strong><br/></td>
<td>0x00000800<br/></td>
<td>Logs all data sent by the LDAP client to the server. This is essentially packet logging, but it always logs unencrypted data. (If a packet is sent over SSL, this logs the unencrypted packet.) This can be verbose and is probably best used on its own (or with <strong>DEBUG_BYTES_RECEIVED</strong>).<br/></td>
</tr>
<tr class="odd">
<td><strong>DEBUG_EOM</strong><br/></td>
<td>0x00001000<br/></td>
<td>Logs events related to reaching the end of a message list. This includes things like message list cleared and so on.<br/></td>
</tr>
<tr class="even">
<td><strong>DEBUG_BER</strong><br/></td>
<td>0x00002000<br/></td>
<td>Logs Basic Encoding Rules (BER) operations and errors. This includes problems with encoding, buffer size problems, and so on.<br/></td>
</tr>
<tr class="odd">
<td><strong>DEBUG_OUTMEMORY</strong><br/></td>
<td>0x00004000<br/></td>
<td>Logs failures to allocate memory. Generally logs any failure to compute the required memory as well, for example, overflow when computing the required buffer size.<br/></td>
</tr>
<tr class="even">
<td><strong>DEBUG_CONTROLS</strong><br/></td>
<td>0x00008000<br/></td>
<td>Logs data related to controls. This includes inserting controls, problems with controls, mandatory controls on a connection, and so on.<br/></td>
</tr>
<tr class="odd">
<td><strong>DEBUG_BYTES_RECEIVED</strong><br/></td>
<td>0x00010000<br/></td>
<td>Logs all data received by the LDAP client. This is essentially packet logging, but it always logs unencrypted data. (If a packet is sent over SSL, this logs the unencrypted packet.) This can be verbose and is probably best used on its own (or with <strong>DEBUG_BYTES_SENT</strong>).<br/></td>
</tr>
<tr class="even">
<td><strong>DEBUG_CLDAP</strong><br/></td>
<td>0x00020000<br/></td>
<td>Logs events specific to UDP and connectionless LDAP.<br/></td>
</tr>
<tr class="odd">
<td><strong>DEBUG_FILTER</strong><br/></td>
<td>0x00040000<br/></td>
<td>Logs events and errors encountered when constructing a search filter.<br/>
<blockquote>
[!Note]<br />
This only logs client events during filter construction. No responses from the server regarding a filter are included here.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td><strong>DEBUG_BIND</strong><br/></td>
<td>0x00080000<br/></td>
<td>Logs bind events and errors. This includes negotiation information, bind success, bind fail, and so on.<br/></td>
</tr>
<tr class="odd">
<td><strong>DEBUG_NETWORK_ERRORS</strong><br/></td>
<td>0x00100000<br/></td>
<td>Logs general network errors. This includes send and receive errors.<br/>
<blockquote>
[!Note]<br />
If a connection is lost or the server cannot be reached, <strong>DEBUG_SERVERDOWN</strong> is the preferred tag.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td><strong>DEBUG_VERBOSE</strong><br/></td>
<td>0x00200000<br/></td>
<td>Logs general messages. This should be used for any messages that tend to generate a large amount of output, for example: end of message reached, server has not responded yet, and so on. This is also useful for generic messages.<br/> <strong>Windows Server 2008 and Windows Vista:</strong> The flag name was <strong>DEBUG_SCRATCH</strong>.<br/></td>
</tr>
<tr class="odd">
<td><strong>DEBUG_PARSE</strong><br/></td>
<td>0x00400000<br/></td>
<td>Logs general message and packet parsing and encoding events and errors.<br/></td>
</tr>
<tr class="even">
<td><strong>DEBUG_REFERRALS</strong><br/></td>
<td>0x00800000<br/></td>
<td>Logs data about referrals and chasing referrals.<br/></td>
</tr>
<tr class="odd">
<td><strong>DEBUG_REQUEST</strong><br/></td>
<td>0x01000000<br/></td>
<td>Logs tracking of requests.<br/></td>
</tr>
<tr class="even">
<td><strong>DEBUG_CONNECTION</strong><br/></td>
<td>0x02000000<br/></td>
<td>Logs general connection data and errors.<br/></td>
</tr>
<tr class="odd">
<td><strong>DEBUG_INIT_TERM</strong><br/></td>
<td>0x04000000<br/></td>
<td>Logs module initialization and cleanup (DLL Main, and so on).<br/></td>
</tr>
<tr class="even">
<td><strong>DEBUG_API_ERRORS</strong><br/></td>
<td>0x08000000<br/></td>
<td>Supports logging improper use of the API, for example, if bind is called twice on the same connection.<br/></td>
</tr>
<tr class="odd">
<td><strong>DEBUG_ERRORS</strong><br/></td>
<td>0x10000000<br/></td>
<td>Logs general errors. Most fall into one of the following categories: module initialization errors, SSL errors, or overflow or underflow errors.<br/></td>
</tr>
</tbody>
</table>



 

You can combine flags by combining the appropriate bits in the *TraceFlags* argument. For example, to specify the **DEBUG\_SEARCH** and **DEBUG\_CACHE** flags, the appropriate *TraceFlags* value would be 0x00000011.

To terminate tracing, run the following command:

**tracelog.exe -stop** *SessionName*

In this example, *SessionName* is the same name as the one that was provided with the command that started the tracing section.

## Example Scenario

Imagine that an administrator sees an unexpected error in an application that sets passwords for user accounts, so the administrator decides to enable tracing for App1.exe. They would take the following steps to fix the problem using event tracing.

1.  Create the registry key

    **HKEY\_LOCAL\_MACHINE**\\**System**\\**CurrentControlSet**\\**Services**\\**ldap**\\**Tracing**\\**App1.exe**

    and then start a tracing session using the following command:

    **tracelog.exe -start ldaptrace -guid \#099614a5-5dd7-4788-8bc9-e29f43db28fc -f .\\ldap.etl -flag 0x80000**

2.  After this command has started, **DEBUG\_BIND** tracing messages will be written to .\\ldap.etl. Execute App1.exe and reproduce the unexpected behavior.

3.  Shut down the tracing session as follows:

    **tracelog.exe -stop ldaptrace**

4.  Delete the registry key

    **HKEY\_LOCAL\_MACHINE**\\**System**\\**CurrentControlSet**\\**Services**\\**ldap**\\**Tracing**\\**App1.exe**

    so that no other users can trace App1.exe.

5.  Use a [Trace Consumer](http://go.microsoft.com/fwlink/p/?linkid=83876) such as Tracerpt.exe to review the information in the trace log:

    **tracerpt.exe .\\ldap.etl -o -report**

 

 





