---
title: MSCustomProtectedData customProtectedDataWithPolicy protectedData contentStartPosition contentSize completionBlock method
description: Asynchronously creates an MSCustomProtectedData object that can be used to read the specified block of protected data.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '0a792395-2f4c-4d55-afaa-f9c4c3011860'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["MSCustomProtectedData customProtectedDataWithPolicy protectedData contentStartPosition contentSize completionBlock method"]
topic_type:
- apiref
api_name:
- MSCustomProtectedData customProtectedDataWithPolicy protectedData contentStartPosition contentSize completionBlock method
api_type:
- NA
---

# MSCustomProtectedData customProtectedDataWithPolicy:protectedData:contentStartPosition:contentSize:completionBlock method

Asynchronously creates an [**MSCustomProtectedData**](mscustomprotecteddata-interface-objc.md) object that can be used to read the specified block of protected data.

## Signature

``` syntax
+ (void)customProtectedDataWithPolicy:(MSUserPolicy *)policy
                        protectedData:(NSData *)protectedData
                 contentStartPosition:(NSUInteger)contentStartPosition
                          contentSize:(NSUInteger)contentSize
                      completionBlock:(void(^)(MSCustomProtectedData *customProtectedData,NSError *error))completionBlock;
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
<td><em>policy</em><br/></td>
<td>[<strong>MSUserPolicy</strong>](msuserpolicy-interface-objc.md) *<br/></td>
<td>Required. <br/></td>
</tr>
<tr class="even">
<td><em>protectedData</em><br/></td>
<td><strong>NSData</strong> *<br/></td>
<td>Required. The data to be read from.<br/></td>
</tr>
<tr class="odd">
<td><em>contentStartPosition</em><br/></td>
<td><strong>NSUInteger</strong><br/></td>
<td>Required. Specifies theposition to begin reading in the <em>protectedData</em>.<br/></td>
</tr>
<tr class="even">
<td><em>contentSize</em><br/></td>
<td><strong>NSUInteger</strong><br/></td>
<td>Required. Specifies the size, in bytes, of the content to be read.<br/></td>
</tr>
<tr class="odd">
<td><em>completionBlock</em><br/></td>
<td>void(^)([<strong>MSCustomProtectedData</strong>](mscustomprotecteddata-interface-objc.md) *customProtectedData, <strong>NSError</strong> *error) <br/></td>
<td><blockquote>
[!Note]<br />
If the user cancels the operation, both the <em>customProtectedData</em> and <em>error</em> parameters will be <strong>NIL</strong>.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

## Defined in

MSCustomProtectedData.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 





 

## Remarks

You specify a range (*contentStartPosition*, *contentSize*) where the encrypted content is located in the protected **NSData** (*protectedData*).

-   If the existing content ends at the end of the backing **NSData**, you can specify **NSUIntegerMax** for *contentSize*.
-   The *contentSize* parameter is needed only for the cases when there is non-encrypted app-specific content after the encrypted content. This is because the framework needs to know where the encrypted content ends when performing decryption.
-   The *contentSize* parameter is specified in terms of the encrypted content; for example, it does include the size of the CBC padding. You can use the [**getEncryptedContentLength**](mscustomprotecteddata-getencryptedcontentlengthwithpolicy-protectionpolicy-contentlength.md) method to determine the size of the encrypted content from the size of the original, unencrypted content.
-   If the range defined by the parameters *contentStartPosition* and *contentSize* is not empty (for example, *contentSize* != 0), it must address an entire segment of encrypted content; that is, it must start from block 0 and must have a final block in the CBC case or should be 16-byte aligned in the ECB case.

 

 





