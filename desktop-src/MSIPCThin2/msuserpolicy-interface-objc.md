---
title: MSUserPolicy class
description: Represents a user policy.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'cbf457cb-e73a-4d37-a29a-6e1dc53c95a1'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["MSUserPolicy class"]
topic_type:
- apiref
api_name:
- MSUserPolicy class
api_type:
- NA
---

# MSUserPolicy class

Represents a user policy.

## Signature

``` syntax
@interface MSUserPolicy : NSSecureCodableObject
```

## Properties



| Name                                                                                                 | Description                                                                                                                                |
|------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| [**allowAuditedExtract**](msuserpolicy-allowauditedextract-property-objc.md)<br/>             | Checks if the user can perform and audited extract of the policy<br/>                                                                |
| [**contentId**](msuserpolicy-contentid-property-objc.md)<br/>                                 | The unique ID associated with the protected content.<br/>                                                                            |
| [**contentValidUntil**](msuserpolicy-contentvaliduntil-property-objc.md)<br/>                 | The date until which the content license is valid.<br/>                                                                              |
| [**policyDescription**](msuserpolicy-description-property-objc.md)<br/>                       | The description of the user policy.<br/>                                                                                             |
| [**doesUseDeprecatedAlgorithm**](msuserpolicy-doesusedeprecatedalgorithm-method-objc.md)<br/> | A flag that indicates whether [*Deprecated Algorithms*](terms.md), (ECB) mode, was used to protect the content for the policy.<br/> |
| [**encryptedAppData**](msuserpolicy-appdata-property-objc.md)<br/>                            | The encrypted application specific data.<br/>                                                                                        |
| [**isIssuedToOwner**](msuserpolicy-isissuedtoowner-property-objc.md)<br/>                     | Is the current user the original owner?<br/>                                                                                         |
| [**issuedTo**](msuserpolicy-issuedto-property-objc.md)<br/>                                   | The email address of the original content owner.<br/>                                                                                |
| [**policyName**](msuserpolicy-name-property-objc.md)<br/>                                     | Name of the user policy.<br/>                                                                                                        |
| [**owner**](msuserpolicy-owner-property-objc.md)<br/>                                         | The email address of the current content owner.<br/>                                                                                 |
| [**policyDescriptor**](msuserpolicy-policydescriptor-property-objc.md)<br/>                   | The custom policy used to protect the content.<br/>                                                                                  |
| [**referrer**](msuserpolicy-referrer-property-objc.md)<br/>                                   | The referral information<br/>                                                                                                        |
| [**serializedPolicy**](msuserpolicy-serializedpolicy-method-objc.md)<br/>                     | The serialized policy<br/>                                                                                                           |
| [**signedAppData**](msuserpolicy-signedappdata-property-objc.md)<br/>                         | Application specific data, signed.<br/>                                                                                              |
| [**templateDescriptor**](msuserpolicy-templatedescriptor-property-objc.md)<br/>               | The template used to protect the content.<br/>                                                                                       |
| [**type**](msuserpolicy-type-property-objc.md)<br/>                                           | Policy type, template based or custom.<br/>                                                                                          |



 

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
<td>[<strong>accessCheck</strong>](msuserpolicy-accesscheck-method-objc.md)<br/></td>
<td>Returns a value that indicates whether the current user has the specified right.<br/></td>
</tr>
<tr class="even">
<td>[<strong>registerForDocTracking</strong>](msuserpolicy-registerfordoctracking-userid-authenticationcallback-completionblock-method-objc.md)<br/></td>
<td>Registers the content and user with the document tracking service.<br/>
<blockquote>
[!Note]<br />
Document tracking is only supported for RMSO scenarios.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>revokeSerializedPolicyWithUserId</strong>](msipcthin2-msuserpolicy_revokeserializedpolicywithuserid_method)<br/></td>
<td>Use to revoke published content.<br/></td>
</tr>
<tr class="even">
<td>[<strong>userPolicyWithSerializedPolicy</strong>](msuserpolicy-protectionpolicywithserializedpolicy-userid-authenticationcallback-options-completionblock-method-objc.md)<br/></td>
<td>Creates a user policy based on the supplied serialized policy<br/></td>
</tr>
<tr class="odd">
<td>[<strong>userPolicyWithTemplateDescriptor</strong>](msuserpolicy-protectionpolicywithtemplatedescriptor-userid-authenticationcallback-options-completionblock-method-objc.md)<br/></td>
<td>Creates a user policy based on the supplied template descriptor<br/></td>
</tr>
<tr class="even">
<td>[<strong>userPolicyWithPolicyDescriptor</strong>](msuserpolicy-protectionpolicywithpolicydescriptor-userid-authenticationcallback-options-completionblock-method-objc.md)<br/></td>
<td>Creates a user policy based on the supplied policy descriptor<br/></td>
</tr>
</tbody>
</table>



 

## Defined in

MSUserPolicy.h

## Supported Platforms



|                                             |                                  |
|---------------------------------------------|----------------------------------|
| **Minimum supported OS version**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

## Remarks

An **MSUserPolicy** object defines the policy that is associated with the protected content. It can be used to examine the rights of the current user as well as to protect or unprotect content.

## Thread Safety

Members of this class are not guaranteed to be thread safe.

 

 





