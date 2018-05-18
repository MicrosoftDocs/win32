---
title: MSMutableProtectedData protectedDataWithPolicy path completionBlock method
description: Asynchronously creates and returns an empty MSMutableProtectedData object that can be used to write and protect data to the specified file.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '782bb32c-1e3e-4e31-8d5e-3ccd8bdc93e0'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["MSMutableProtectedData protectedDataWithPolicy path completionBlock method"]
topic_type:
- apiref
api_name:
- MSMutableProtectedData protectedDataWithPolicy path completionBlock method
api_type:
- NA
---

# MSMutableProtectedData protectedDataWithPolicy:path:completionBlock method

Asynchronously creates and returns an empty [**MSMutableProtectedData**](msmutableprotecteddata-interface-objc.md) object that can be used to write and protect data to the specified file. The file will be protected using the specified policy and saved in Microsoft Protected File format.

## Signature

``` syntax
+ (void)protectedDataWithPolicy:(MSUserPolicy *)userPolicy
          originalFileExtension:(NSString *)originalFileExtension
                           path:(NSString *)path
                completionBlock:(void(^)(MSMutableProtectedData *data, NSError *error))completionBlock;
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
<td><em>protectionPolicy</em><br/></td>
<td>[<strong>MSUserPolicy</strong>](msuserpolicy-interface-objc.md) *<br/></td>
<td>Required.<br/></td>
</tr>
<tr class="even">
<td><em>originalFileExtension</em><br/></td>
<td><strong>NSString</strong> *<br/></td>
<td>Used to store the original file type, before protection.<br/></td>
</tr>
<tr class="odd">
<td><em>path</em><br/></td>
<td><strong>NSString</strong> *<br/></td>
<td>Required. The absolute path to the new protected file.<br/></td>
</tr>
<tr class="even">
<td><em>completionBlock</em><br/></td>
<td>void(^)([<strong>MSMutableProtectedData</strong>](msmutableprotecteddata-interface-objc.md) *data, <strong>NSError</strong> *error) <br/></td>
<td>Required. Called with the following parameters when the method is completed:<br/> <em>data</em> - The protected file object.<br/> <em>error</em> - If there is an error creating the data object, contains an <strong>NSError</strong> object that describes the problem.<br/>
<blockquote>
[!Note]<br />
If the user cancels the operation, both the <em>data</em> and <em>error</em> parameters will be <strong>NIL</strong>.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

## Defined in

MSMutableProtectedData.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

## See also

<dl> <dt>

[**MSMutableProtectedData**](msmutableprotecteddata-interface-objc.md)
</dt> </dl>

 

 





