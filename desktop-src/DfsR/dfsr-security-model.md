---
title: DFSR Security Model
description: The Distributed File System Replication (DFSR) service provides two types of security Active Directory security and WMI security.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 696a6ef6-2714-4064-8c5d-f5596adc8143
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-replication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Distributed File System Replication Files , security model
- security model for Distributed File System Replication Files
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DFSR Security Model

The Distributed File System Replication (DFSR) service provides two types of security:

-   Active Directory security
-   WMI security

During startup and polling cycles, DFSR downloads configuration information from the Active Directory, creates corresponding registry keys (if they do not already exist), and maintains the access-control lists (ACL) on the registry keys. Hence the security and delegation model is managed through Active Directory security and cached locally to be imposed by the WMI interfaces.

## Active Directory Security

Every object and every attribute in the Active Directory can have an associated security descriptor. DFSR simplifies security delegation by taking advantage of the Active Directory security model as well as ACL inheritance. Each class of DFSR objects in the Active Directory is grouped under a container object.

The default Active Directory object allows the following access.



<table>
<thead>
<tr class="header">
<th>User</th>
<th>Access</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Authenticated users<br/></td>
<td><dl> ADS_RIGHT_DS_READ_PROP<br />
ADS_RIGHT_ACTRL_DS_LIST<br />
ADS_RIGHT_DS_LIST_OBJECT<br />
ADS_RIGHT_READ_CONTROL<br />
</dl></td>
</tr>
<tr class="even">
<td>Domain administrators<br/> Creator/owner<br/> LocalSystem account<br/></td>
<td><dl> ADS_RIGHT_DS_READ_PROP<br />
ADS_RIGHT_DS_WRITE_PROP<br />
ADS_RIGHT_DS_CONTROL_ACCESS<br />
ADS_RIGHT_ACTRL_DS_LIST<br />
ADS_RIGHT_DS_LIST_OBJECT<br />
ADS_RIGHT_DS_CREATE_CHILD<br />
ADS_RIGHT_DS_DELETE_CHILD<br />
ADS_RIGHT_DS_READ_CONTROL<br />
ADS_RIGHT_DS_WRITE_DAC<br />
ADS_RIGHT_DS_WRITE_OWNER<br />
ADS_RIGHT_DS_DELETE_TREE<br />
ADS_RIGHT_DS_SELF<br />
</dl></td>
</tr>
</tbody>
</table>



 

## WMI Security

The WMI interface provides security through the registry interface. Any operation on a replication group or one of its replicated folders is verified with an access check on the corresponding registry key.

The following table summarizes the categories of operations provided by the DFSR WMI classes and the required permissions that must be granted to the registry key.



| Operation                | Permissions |
|--------------------------|-------------|
| Read configuration data  | READ        |
| Write configuration data | WRITE       |
| Read monitoring data     | SPECIAL     |
| Write monitoring data    | WRITE       |



 

The following table summarizes the relationship between the DFSR permissions to AD objects and the related registry key access masks.



| DFSR access | Key access  | Active directory access         |
|-------------|-------------|---------------------------------|
| READ        | KEY\_READ   | ADS\_RIGHT\_DS\_READ\_PROP      |
| WRITE       | KEY\_WRITE  | ADS\_RIGHT\_DS\_WRITE\_PROP     |
| SPECIAL     | KEY\_NOTIFY | ADS\_RIGHT\_DS\_CONTROL\_ACCESS |



 

 

 





