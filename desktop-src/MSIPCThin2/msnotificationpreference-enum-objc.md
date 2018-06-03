---
title: MSNotificationPreference enum
description: Document tracking notification preference.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 49F54F9A-4DA1-42E8-B26C-C9EE2A20973A
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- MSNotificationPreference enum
topic_type:
- apiref
api_name:
- MSNotificationPreference enum
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSNotificationPreference enum

Document tracking notification preference.

## Signature

``` syntax
typedef NS_ENUM(NSUInteger, MSNotificationPreference) {
    NotificationPrefDefault = 0,
    NotificationPrefDigest = 1
};
```

## Members



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Member</th>
<th>Value</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>NotificationPrefDefault</strong><br/></td>
<td>0<br/></td>
<td>Email notifications sent per access.<br/></td>
</tr>
<tr class="even">
<td><strong>NotificationPrefDigest</strong><br/></td>
<td>1<br/></td>
<td>Email notifications sent as a digest once per day.<br/>
<blockquote>
[!Note]<br />
Digest mode is a server side enabled feature which is not yet available.
</blockquote>
<br/> <br/></td>
</tr>
</tbody>
</table>



 

## Defined in

MSMSLicenseMetadata.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

 

 





