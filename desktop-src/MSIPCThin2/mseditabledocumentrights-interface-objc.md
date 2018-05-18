---
title: MSEditableDocumentRights Class
description: Rights that apply to editable documents.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '0bb6a5e2-7c94-46ee-982e-585574728b71'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["MSEditableDocumentRights Class"]
topic_type:
- apiref
api_name:
- MSEditableDocumentRights Class
api_type:
- NA
---

# MSEditableDocumentRights Class

Rights that apply to editable documents.

## Signature

``` syntax
@interface MSEditableDocumentRights : NSObject
```

## Methods



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>+(<strong>NSString</strong>) edit;<br/></td>
<td>Specifies a right that allows the protected content to be edited and saved to the same protected format.<br/></td>
</tr>
<tr class="even">
<td>+(<strong>NSString</strong>) exportable;<br/></td>
<td>Specifies a right that allows content to be extracted from a protected format and placed in a different AD RMS-protected format.<br/></td>
</tr>
<tr class="odd">
<td>+(<strong>NSString</strong>) extract;<br/></td>
<td>Specifies a right that allows content to be extracted from a protected format and placed in an unprotected, or a different protected format. Same value as [<strong>[MSEmailRights extract]</strong>](msemailrights-interface-objc.md).<br/></td>
</tr>
<tr class="even">
<td>+(<strong>NSString</strong>) print;<br/></td>
<td>Specifies a right that allows protected content to be printed. Same value as [<strong>[MSEmailRights print]</strong>](msemailrights-interface-objc.md).<br/></td>
</tr>
<tr class="odd">
<td>+(<strong>NSString</strong>) comment;<br/></td>
<td>Specifies a right that allows protected content to have comments added.<br/></td>
</tr>
<tr class="even">
<td>+(<strong>NSArray</strong>) all;<br/></td>
<td>Specifies a list of all of the rights that apply to editable documents.<br/>
<blockquote>
[!Note]<br />

</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

## Defined in

MSRight.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

## Remarks

For more information about the built-in rights and the usage restrictions associated with them that apps should observe, see [Built-in Rights Usage Restriction Reference](built-in-rights-usage-restriction-reference.md).

## Thread Safety

Members of this class are not guaranteed to be thread safe.

 

 





