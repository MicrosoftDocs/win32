---
description: "Learn more about: Extensible Storage Engine System Parameters"
title: Extensible Storage Engine System Parameters
TOCTitle: Extensible Storage Engine System Parameters
ms:assetid: f95c2e87-b25e-4be5-8c17-8486ba37dad4
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294139(v=EXCHG.10)
ms:contentKeyID: 32765753
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

# Extensible Storage Engine System Parameters


_**Applies to:** Windows | Windows Server_

## Extensible Storage Engine System Parameters

The following constants are used as values for the *paramid* parameter of the [JetGetSystemParameter](./jetgetsystemparameter-function.md) and [JetSetSystemParameter](./jetsetsystemparameter-function.md) functions.

  - [Backup and Restore Parameters](./backup-and-restore-parameters.md)

  - [Callback Parameters](./callback-parameters.md)

  - [Database Parameters](./database-parameters.md)

  - [Database Cache Parameters](./database-cache-parameters.md)

  - [Error Handling Parameters](./error-handling-parameters.md)

  - [Event Log Parameters](./event-log-parameters.md)

  - [I/O Parameters](./i-o-parameters.md)

  - [Index Parameters](./index-parameters.md)

  - [Informational Parameters](./informational-parameters.md)

  - [Meta Parameters](./meta-parameters.md)

  - [Resource Parameters](./resource-parameters.md)

  - [Temporary Database Parameters](./temporary-database-parameters.md)

  - [Transaction Log Parameters](./transaction-log-parameters.md)

### System Parameter Description Format

Each system parameter will be described using the following format:

JET_paramX

Description of the JET_paramX system parameter.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Default Value:</p></td>
<td><p>The default value of the parameter.</p></td>
</tr>
<tr class="even">
<td><p>Type:</p></td>
<td><p>The data type of the parameter.</p></td>
</tr>
<tr class="odd">
<td><p>Valid Range:</p></td>
<td><p>The legal values for the parameter.</p></td>
</tr>
<tr class="even">
<td><p>Scope:</p></td>
<td><p>Is the parameter Global or per Instance?</p></td>
</tr>
<tr class="odd">
<td><p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p></td>
<td><p>Can the parameter be set if any instances exist?</p></td>
</tr>
<tr class="even">
<td><p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p></td>
<td><p>Can the parameter be set when initialized?</p></td>
</tr>
<tr class="odd">
<td><p>Affects Physical Layout:</p></td>
<td><p>Does the parameter affect the files on disk?</p></td>
</tr>
<tr class="even">
<td><p>Affects Reliability:</p></td>
<td><p>Does the parameter affect engine reliability?</p></td>
</tr>
<tr class="odd">
<td><p>Affects Performance:</p></td>
<td><p>Does the parameter affect engine performance?</p></td>
</tr>
<tr class="even">
<td><p>Affects Resources:</p></td>
<td><p>Does the parameter affect engine resources?</p></td>
</tr>
<tr class="odd">
<td><p>Availability:</p></td>
<td><p>Releases of Windows that support the parameter.</p></td>
</tr>
</tbody>
</table>
