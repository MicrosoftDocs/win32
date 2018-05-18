---
title: MSMutableCustomProtectedData customProtectorWithProtectionPolicy backingData protectedContentOffset completionBlock method
description: Asynchronously creates an MSMutableCustomProtectedData object that can be used to protect plaintext data and write to the specified backing NSMutableData object.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'a8dfaa1b-0bde-4c2a-b944-3e79e834da9a'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["MSMutableCustomProtectedData customProtectorWithProtectionPolicy backingData protectedContentOffset completionBlock method"]
topic_type:
- apiref
api_name:
- MSMutableCustomProtectedData customProtectorWithProtectionPolicy backingData protectedContentOffset completionBlock method
api_type:
- NA
---

# MSMutableCustomProtectedData customProtectorWithProtectionPolicy:backingData:protectedContentOffset:completionBlock method

Asynchronously creates an [**MSMutableCustomProtectedData**](msmutablecustomprotecteddata-interface-objc.md) object that can be used to protect plaintext data and write to the specified backing **NSMutableData** object.

> \[!Important\]  
> Rights Management SDK 4.2 based applications that use [**MSMutableCustomProtectedData**](msmutablecustomprotecteddata-interface-objc.md) may be incompatible with SharePoint, Exchange, and other RMS-enabled applications. For most applications, it is recommended that you use [**MSMutableProtectedData**](msmutableprotecteddata-interface-objc.md) instead.

 

## Signature

``` syntax
+ (void)customProtectorWithProtectionPolicy:(MSUserPolicy *)userPolicy
                                backingData:(NSMutableData *)backingData
                     protectedContentOffset:(NSUInteger)protectedContentOffset
                            completionBlock:(void(^)(MSMutableCustomProtectedData *customProtectedData,
                                                     NSError *error))completionBlock;
```

## Parameters



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th>Datatype</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><em>userPolicy</em><br/></td>
<td>[<strong>MSUserPolicy</strong>](msuserpolicy-interface-objc.md) *<br/></td>
<td>Required.<br/></td>
</tr>
<tr class="even">
<td><em>backingData</em><br/></td>
<td><strong>NSMutableData</strong> *<br/></td>
<td>Required. The backing <strong>NSMutableData</strong> object that will be filled with the protected content.<br/></td>
</tr>
<tr class="odd">
<td><em>protectedContentOffset</em><br/></td>
<td><strong>NSUInteger</strong><br/></td>
<td>Required. Specifies the position in the <em>backingData</em> at which the protected content should start.<br/></td>
</tr>
<tr class="even">
<td><em>completionBlock</em><br/></td>
<td>void(^)([<strong>MSMutableCustomProtectedData</strong>](msmutablecustomprotecteddata-interface-objc.md) *customProtectedData, <strong>NSError</strong> *error) <br/></td>
<td>Required. Called with the following parameters when the method is completed:<br/> <em>customProtecedData</em> – protected data object, or NIL if the method fails.<br/> <em>error</em> – If there is an error protecting the data object, <em>error</em> points to an <strong>NSError</strong> object that describes the problem.<br/>
<blockquote>
[!Note]<br />
If the user cancels the operation, both the <em>customProtectedData</em> and <em>error</em> parameters will be <strong>NIL</strong>.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

## Defined in

MSMutableCustomProtectedData.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

## Remarks

If there is no existing content in the backing data (for example, this is a new file), you should specify 0 for the *encryptedContentSize*.

When publishing content, apps are required to call [**-\[MSMutableCustomProtectedData close\]**](msmutableprotecteddata-close--method-objc.md) when they are done writing content to the [**MSMutableCustomProtectedData**](msmutablecustomprotecteddata-interface-objc.md) object. If **close** is not called the framework cannot guarantee that all the encrypted data is stored to the backing stream.

## See also

<dl> <dt>

[**MSMutableCustomProtectedData**](msmutablecustomprotecteddata-interface-objc.md)
</dt> </dl>

 

 





