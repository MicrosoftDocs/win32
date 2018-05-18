---
title: MSProtectedData protectedDataWithProtectedFile completionBlock method
description: Asynchronously creates and returns a protected file data object that can be used to read (and decrypt) data from the specified file, which is protected to Microsoft Protected File format.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'd09639f8-aa03-42f0-bf72-02953b3ec9ae'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["MSProtectedData protectedDataWithProtectedFile completionBlock method"]
topic_type:
- apiref
api_name:
- MSProtectedData protectedDataWithProtectedFile completionBlock method
api_type:
- NA
---

# MSProtectedData protectedDataWithProtectedFile:completionBlock method

Asynchronously creates and returns a protected file data object that can be used to read (and decrypt) data from the specified file, which is protected to Microsoft Protected File format.

## Signature

``` syntax
+ (MSAsyncControl *)protectedDataWithProtectedFile:(NSString *)path
                                            userId:(NSString *)userId
                            authenticationCallback:(id<MSAuthenticationCallback>)authenticationCallback
                                   consentCallback:(id<MSConsentCallback>)consentCallback
                                           options:(MSPolicyAcquisitionOptions)options
                                   completionBlock:(void(^)(MSProtectedData *data, NSError *error))completionBlock;
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
<td><em>path</em><br/></td>
<td><strong>NSString</strong> *<br/></td>
<td>Required. The absolute path of the protected file from which to read data.<br/></td>
</tr>
<tr class="even">
<td><em>userId</em><br/></td>
<td><strong>NSString</strong> *<br/></td>

</tr>
<tr class="odd">
<td><em>authenticationCallback</em><br/></td>
<td>id&lt;[<strong>MSAuthenticationCallback</strong>](msauthenticationcallback-protocol-objc.md)&gt;<br/></td>

</tr>
<tr class="even">
<td><em>consentCallback</em><br/></td>
<td>id&lt;[<strong>MSConsentCallback</strong>](https://msdn.microsoft.com/library/windows/desktop/dn833525)&gt;<br/></td>

</tr>
<tr class="odd">
<td><em>options</em><br/></td>
<td>[<strong>MSPolicyAcquisitionOptions</strong>](mspolicyacquisitionoptions-enum-objc.md)<br/></td>

</tr>
<tr class="even">
<td><em>completionBlock</em><br/></td>
<td>void(^)([<strong>MSProtectedData</strong>](msprotecteddata-interface-objc.md) *data, <strong>NSError</strong> *error)) <br/></td>
<td>Required. Called when the method is completed with the following parameters:<br/> <em>data</em> The protected file data object.<br/> <em>error</em> If there is an error creating the data object, contains an <strong>NSError</strong> object that describes the problem.<br/>
<blockquote>
[!Note]<br />
If the user cancels the operation, both the <em>data</em> and <em>error</em> parameters will be <strong>NIL</strong>.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

## Returns

Returns an [**MSAsyncControl**](msasynccontrol-class.md) object allowing you to cancel asynchronous SDK operations including closing all opened UI.

## Defined in

MSProtectedData.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

## Remarks

The [**userPolicy**](msprotecteddata-userpolicy-property-objc.md) property is set based on the policy that applies to the specified file.

 

 





