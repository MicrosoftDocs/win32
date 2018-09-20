---
title: Extensible Storage Engine System Parameters
TOCTitle: Extensible Storage Engine System Parameters
ms:assetid: f95c2e87-b25e-4be5-8c17-8486ba37dad4
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/Gg294139(v=EXCHG.10)
ms:contentKeyID: 32765753
ms.date: 04/11/2016
mtps_version: v=EXCHG.10
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

The following constants are used as values for the *paramid* parameter of the [JetGetSystemParameter](gg269291\(v=exchg.10\).md) and [JetSetSystemParameter](gg294044\(v=exchg.10\).md) functions.

  - [Backup and Restore Parameters](gg269236\(v=exchg.10\).md)

  - [Callback Parameters](gg269310\(v=exchg.10\).md)

  - [Database Parameters](gg269337\(v=exchg.10\).md)

  - [Database Cache Parameters](gg269293\(v=exchg.10\).md)

  - [Error Handling Parameters](gg269173\(v=exchg.10\).md)

  - [Event Log Parameters](gg294086\(v=exchg.10\).md)

  - [I/O Parameters](gg269260\(v=exchg.10\).md)

  - [Index Parameters](gg294119\(v=exchg.10\).md)

  - [Informational Parameters](gg269241\(v=exchg.10\).md)

  - [Meta Parameters](gg269346\(v=exchg.10\).md)

  - [Resource Parameters](gg269201\(v=exchg.10\).md)

  - [Temporary Database Parameters](gg294140\(v=exchg.10\).md)

  - [Transaction Log Parameters](gg269235\(v=exchg.10\).md)

### System Parameter Description Format

Each system parameter will be described using the following format:

JET\_paramX

Description of the JET\_paramX system parameter.

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

