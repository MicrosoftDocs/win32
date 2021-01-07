---
description: "Learn more about: Event Log Parameters"
title: Event Log Parameters
TOCTitle: Event Log Parameters
ms:assetid: c660f555-2627-4d25-8f1c-8c1dc8a3a381
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294086(v=EXCHG.10)
ms:contentKeyID: 32765701
ms.date: 04/11/2016
ms.topic: reference
api_name: 
topic_type: 
- apiref
- kbArticle
api_type: 
- COM
api_location: 
ROBOTS: INDEX,FOLLOW

---

# Event Log Parameters


_**Applies to:** Windows | Windows Server_

## Event Log Parameters

This topic contains parameters that are used for the event log.

JET_paramEventLogCache  
This parameter controls the size (in bytes) of an eventlog message cache that will hold eventlog messages emitted by the database engine while the eventlog service is stopped. These cached messages will be flushed to the eventlog when the service becomes operational. Any messages that overflow the cache will be dropped.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Default Value:</p></td>
<td><p>0</p></td>
</tr>
<tr class="even">
<td><p>Type:</p></td>
<td><p>Integer</p></td>
</tr>
<tr class="odd">
<td><p>Valid Range:</p></td>
<td><p>0 – 2147483647</p></td>
</tr>
<tr class="even">
<td><p>Scope:</p></td>
<td><p>Global</p></td>
</tr>
<tr class="odd">
<td><p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p></td>
<td><p>No</p></td>
</tr>
<tr class="even">
<td><p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p></td>
<td><p>No</p></td>
</tr>
<tr class="odd">
<td><p>Affects Physical Layout:</p></td>
<td><p>No</p></td>
</tr>
<tr class="even">
<td><p>Affects Reliability:</p></td>
<td><p>No</p></td>
</tr>
<tr class="odd">
<td><p>Affects Performance:</p></td>
<td><p>No</p></td>
</tr>
<tr class="even">
<td><p>Affects Resources:</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="odd">
<td><p>Availability:</p></td>
<td><p>All</p></td>
</tr>
</tbody>
</table>


*JET_paramEventLoggingLevel*  
  
This parameter configures the detail level of eventlog messages that are emitted to the eventlog by the database engine. Higher numbers will result in more detailed eventlog messages.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Default Value:</p></td>
<td><p>JET_EventLoggingLevelMax</p></td>
</tr>
<tr class="even">
<td><p>Type:</p></td>
<td><p>Integer</p></td>
</tr>
<tr class="odd">
<td><p>Valid Range:</p></td>
<td><p>JET_EventLoggingDisable – JET_EventLoggingLevelMax</p></td>
</tr>
<tr class="even">
<td><p>Scope:</p></td>
<td><p>Instance</p></td>
</tr>
<tr class="odd">
<td><p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p></td>
<td><p>No</p></td>
</tr>
<tr class="odd">
<td><p>Affects Physical Layout:</p></td>
<td><p>No</p></td>
</tr>
<tr class="even">
<td><p>Affects Reliability:</p></td>
<td><p>No</p></td>
</tr>
<tr class="odd">
<td><p>Affects Performance:</p></td>
<td><p>No</p></td>
</tr>
<tr class="even">
<td><p>Affects Resources:</p></td>
<td><p>No</p></td>
</tr>
<tr class="odd">
<td><p>Availability:</p></td>
<td><p>Windows XP and later releases</p></td>
</tr>
</tbody>
</table>


*JET_paramEventSource*  
4  

This parameter supplies an application specific string that will be added to any event log messages that are emitted by the database engine. This allows easy correlation of event log messages with the source application. If an empty string is specified (as is the default) then the host application executable name will be used.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Default Value:</p></td>
<td><p>&quot;&quot;</p></td>
</tr>
<tr class="even">
<td><p>Type:</p></td>
<td><p>String</p></td>
</tr>
<tr class="odd">
<td><p>Valid Range:</p></td>
<td><p>0 – 259 characters</p></td>
</tr>
<tr class="even">
<td><p>Scope:</p></td>
<td><p>Instance</p></td>
</tr>
<tr class="odd">
<td><p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p></td>
<td><p>No</p></td>
</tr>
<tr class="odd">
<td><p>Affects Physical Layout:</p></td>
<td><p>No</p></td>
</tr>
<tr class="even">
<td><p>Affects Reliability:</p></td>
<td><p>No</p></td>
</tr>
<tr class="odd">
<td><p>Affects Performance:</p></td>
<td><p>No</p></td>
</tr>
<tr class="even">
<td><p>Affects Resources:</p></td>
<td><p>No</p></td>
</tr>
<tr class="odd">
<td><p>Availability:</p></td>
<td><p>All</p></td>
</tr>
</tbody>
</table>


*JET_paramEventSourceKey*  
49  

This parameter can be used to control which event log the database engine uses for its event log messages. By default, all event log messages will go to the Application event log. If the registry key name for another event log is configured then the event log messages will go there instead.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Default Value:</p></td>
<td><p>&quot;&quot;</p></td>
</tr>
<tr class="even">
<td><p>Type:</p></td>
<td><p>String</p></td>
</tr>
<tr class="odd">
<td><p>Valid Range:</p></td>
<td><p>0 – 259 characters</p></td>
</tr>
<tr class="even">
<td><p>Scope:</p></td>
<td><p>Instance</p></td>
</tr>
<tr class="odd">
<td><p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p></td>
<td><p>No</p></td>
</tr>
<tr class="odd">
<td><p>Affects Physical Layout:</p></td>
<td><p>No</p></td>
</tr>
<tr class="even">
<td><p>Affects Reliability:</p></td>
<td><p>No</p></td>
</tr>
<tr class="odd">
<td><p>Affects Performance:</p></td>
<td><p>No</p></td>
</tr>
<tr class="even">
<td><p>Affects Resources:</p></td>
<td><p>No</p></td>
</tr>
<tr class="odd">
<td><p>Availability:</p></td>
<td><p>All</p></td>
</tr>
</tbody>
</table>


*JET_paramNoInformationEvent*  
50  

When this parameter is true, informational event log messages that would ordinarily be generated by the database engine will be suppressed.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Default Value:</p></td>
<td><p>False</p></td>
</tr>
<tr class="even">
<td><p>Type:</p></td>
<td><p>Boolean</p></td>
</tr>
<tr class="odd">
<td><p>Valid Range:</p></td>
<td><p>False, True</p></td>
</tr>
<tr class="even">
<td><p>Scope:</p></td>
<td><p>Instance</p></td>
</tr>
<tr class="odd">
<td><p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p></td>
<td><p>Yes</p></td>
</tr>
<tr class="even">
<td><p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p></td>
<td><p>No</p></td>
</tr>
<tr class="odd">
<td><p>Affects Physical Layout:</p></td>
<td><p>No</p></td>
</tr>
<tr class="even">
<td><p>Affects Reliability:</p></td>
<td><p>No</p></td>
</tr>
<tr class="odd">
<td><p>Affects Performance:</p></td>
<td><p>No</p></td>
</tr>
<tr class="even">
<td><p>Affects Resources:</p></td>
<td><p>No</p></td>
</tr>
<tr class="odd">
<td><p>Availability:</p></td>
<td><p>All</p></td>
</tr>
</tbody>
</table>


### Requirements

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Client</strong></p></td>
<td><p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p></td>
</tr>
<tr class="even">
<td><p><strong>Server</strong></p></td>
<td><p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Header</strong></p></td>
<td><p>Declared in Esent.h.</p></td>
</tr>
</tbody>
</table>


### See Also

[JetCreateInstance](./jetcreateinstance-function.md)  
[JetInit](./jetinit-function.md)
