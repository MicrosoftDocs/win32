---
title: NotificationPreference enum
description: Type of user notification preference.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '46E894FB-E424-4740-ACB4-560880893DF5'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["NotificationPreference enum"]
topic_type:
- apiref
api_name:
- NotificationPreference enum
api_type:
- NA
---

# NotificationPreference enum

Type of user notification preference.

## Signature

``` syntax
Public enum NotificationPreference
{
  NOTIFICATION_PREF_DEFAULT,
  NOTIFICATION_PREF_DIGEST
}
```

## Types



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th>Value</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>NOTIFICATION_PREF_DEFAULT</strong><br/></td>
<td>0<br/></td>
<td>Email notifications sent per access.<br/></td>
</tr>
<tr class="even">
<td><strong>NOTIFICATION_PREF_DIGEST</strong><br/></td>
<td>1<br/></td>
<td><blockquote>
[!Note]<br />
Digest mode is a server side enabled feature which is not yet available.
</blockquote>
<br/> <br/></td>
</tr>
</tbody>
</table>



 

## Defined in

NotificationPreference.java

## Supported Platforms



|                                             |                                         |
|---------------------------------------------|-----------------------------------------|
| **Minimum supported OS version**<br/> | Android 4.0.3 (API level 15)<br/> |



 

## Package

com.microsoft.rightsmanagement

 

 





