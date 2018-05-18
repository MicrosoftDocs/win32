---
title: PS\_DAAppServer class
description: Represents the application servers in a DA deployment.
audience: developer
ms.assetid: 'fc828e53-ebc3-489b-a4bc-5fbaeacca1a4'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PS_DAAppServer class", "PS_DAAppServer class, described"]
topic_type:
- apiref
api_name:
- PS_DAAppServer
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
---

# PS\_DAAppServer class

Represents the application servers in a DA deployment.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class PS_DAAppServer
{
};
```

## Members

The **PS\_DAAppServer** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DAAppServer** class has these methods.



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
<td style="text-align: left;">[<strong>AddByAppServerSGGpo</strong>](addbyappserversggpo-ps-daappserver.md)</td>
<td style="text-align: left;">This cmdlet performs the following operations:<br/>
<ul>
<li>Adds a new application server security group to the DA deployment.</li>
<li>Adds an application servers to an application server security group that is already part of the DA deployment.</li>
<li>Adds application server GPO in a domain.</li>
</ul>
This cmdlet is not applicable when DirectAccess is deployed only for the management of remote clients.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>AddByAppServerToSGGpo</strong>](addbyappservertosggpo-ps-daappserver.md)</td>
<td style="text-align: left;">This cmdlet performs the following operations:<br/>
<ul>
<li>Adds a new application server security group to the DA deployment.</li>
<li>Adds an application servers to an application server security group that is already part of the DA deployment.</li>
<li>Adds application server GPO in a domain.</li>
</ul>
This cmdlet is not applicable when DirectAccess is deployed only for the management of remote clients.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>Get</strong>](get-ps-daappserver.md)</td>
<td style="text-align: left;">This cmdlet displays the list of application server security groups that are part of the DA deployment and the properties of the connections made to them. This cmdlet is not applicable when DirectAccess is deployed only for the management of remote clients.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>RemoveByAppServerFromSGGpo</strong>](removebyappserverfromsggpo-ps-daappserver.md)</td>
<td style="text-align: left;">This cmdlet performs the following operations:<br/>
<ul>
<li>Removes the specified lit of application server Security groups from the DA deployment.</li>
<li>Removes the specified application servers from the specified DA application server security group.</li>
<li>Removes the application server GPOs in the specified domains.</li>
</ul>
This cmdlet is not applicable when DirectAccess is deployed only for the management of remote clients.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>RemoveByAppServerSGGpo</strong>](removebyappserversggpo-ps-daappserver.md)</td>
<td style="text-align: left;">This cmdlet performs the following operations:<br/>
<ul>
<li>Removes the specified lit of application server Security groups from the DA deployment.</li>
<li>Removes the specified application servers from the specified DA application server security group.</li>
<li>Removes the application server GPOs in the specified domains.</li>
</ul>
This cmdlet is not applicable when DirectAccess is deployed only for the management of remote clients.<br/></td>
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



 

 





