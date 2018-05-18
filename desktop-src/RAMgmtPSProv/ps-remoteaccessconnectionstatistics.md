---
title: PS\_RemoteAccessConnectionStatistics class
description: Refers to the real-time connection stats and stats based on accounting data.
audience: developer
ms.assetid: 'f91eab49-e009-49b3-a3ac-69486b990ba7'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PS_RemoteAccessConnectionStatistics class", "PS_RemoteAccessConnectionStatistics class, described"]
topic_type:
- apiref
api_name:
- PS_RemoteAccessConnectionStatistics
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
---

# PS\_RemoteAccessConnectionStatistics class

Refers to the real-time connection stats and stats based on accounting data.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("2.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class PS_RemoteAccessConnectionStatistics
{
};
```

## Members

The **PS\_RemoteAccessConnectionStatistics** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_RemoteAccessConnectionStatistics** class has these methods.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;">Method</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;">[<strong>GetByAccountingStatistics</strong>](getbyaccountingstatistics-ps-remoteaccessconnectionstatistics.md)</td>
<td style="text-align: left;">This cmdlet displays the following:<br/>
<ul>
<li>Statistics of current (real-time) active DirectAccess and VPN connections.</li>
<li>Statistics of DirectAccess and VPN historical connections for a specified time duration.</li>
</ul></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>GetByActiveStatistics</strong>](getbyactivestatistics-ps-remoteaccessconnectionstatistics.md)</td>
<td style="text-align: left;">This cmdlet displays the following:<br/>
<ul>
<li>Statistics of current (real-time) active DirectAccess and VPN connections.</li>
<li>Statistics of DirectAccess and VPN historical connections for a specified time duration.</li>
</ul></td>
</tr>
</tbody>
</table>



 

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





