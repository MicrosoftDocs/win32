---
title: MSAuthenticationParameters class
description: Properties used for the authentication process.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 3922C2A6-FD40-45FB-BC76-3698C17F421D
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- MSAuthenticationParameters class
topic_type:
- apiref
api_name:
- MSAuthenticationParameters class
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSAuthenticationParameters class

Properties used for the authentication process. See [**MSAuthenticationCallback**](msauthenticationcallback-protocol-objc.md) for more information.

## Signature

``` syntax
@interface MSAuthenticationParameters : NSObject
```

## Properties



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th>Definition</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>authority<br/></td>
<td><pre class="syntax" data-space="preserve"><code>@property (strong, readonly) NSString *authority;</code></pre>
<br/></td>

</tr>
<tr class="even">
<td>resource<br/></td>
<td><pre class="syntax" data-space="preserve"><code>@property (strong, readonly) NSString *resource;</code></pre>
<br/></td>

</tr>
<tr class="odd">
<td>scope<br/></td>
<td><pre class="syntax" data-space="preserve"><code>@property (strong, readonly) NSString *scope;</code></pre>
<br/></td>

</tr>
<tr class="even">
<td>userId<br/></td>
<td><pre class="syntax" data-space="preserve"><code>@property (strong, readonly) NSString *userId;</code></pre>
<br/></td>

</tr>
</tbody>
</table>



 

## Defined in

MSAuthenticationParameters.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

## Thread Safety

Members of this class are not guaranteed to be thread safe.

 

 





