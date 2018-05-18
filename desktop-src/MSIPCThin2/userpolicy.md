---
title: UserPolicy class
description: Represents the policy associated with protected content.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'T:Microsoft.RightsManagement.UserPolicy'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["UserPolicy class"]
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.UserPolicy
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
---

# UserPolicy class

Represents the policy associated with protected content.

## Syntax


```C++
public ref class UserPolicy sealed 
```



## Members

The **UserPolicy** class inherits from [IInspectable](https://msdn.microsoft.com/library/windows/apps/br205821). **UserPolicy** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **UserPolicy** class has these methods. It also inherits methods from the **Object** class.



| Method                                                                                    | Description                                                                      |
|:------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------|
| [**AccessCheck**](userpolicy-accesscheck.md)                                             | Returns a value that indicates whether the current user has the specified right. |
| [**AcquireAsync**](userpolicy-acquireasync.md)                                           | Acquire a policy.                                                                |
| [**CreateAsync**](userpolicy-createasync.md)                                             | Create a custom protection policy.                                               |
| [**CreateFromTemplateDescriptorAsync**](userpolicy-createfromtemplatedescriptorasync.md) | Publishing using templates                                                       |



 

### Properties

The **UserPolicy** class has these properties.



| Property                                                                                 | Access type          | Description                                                            |
|:-----------------------------------------------------------------------------------------|:---------------------|:-----------------------------------------------------------------------|
| [**ContentId**](userpolicy-contentid.md)<br/>                                     | Read-only<br/> | Gets the unique content ID associated with the protected document.     |
| [**ContentValidUntil**](userpolicy-contentvaliduntil.md)<br/>                     | Read-only<br/> | The date the content is valid until.                                   |
| [**Description**](userpolicy-description.md)<br/>                                 | Read-only<br/> | Gets the policy description.                                           |
| [**DoesUseDeprecatedAlgorithms**](userpolicy-doesusedeprecatedalgorithms.md)<br/> | Read-only<br/> | Gets the deprecated algorithms flag.                                   |
| [**EncryptedAppData**](userpolicy-encryptedappdata.md)<br/>                       | Read-only<br/> | Gets the app specific data                                             |
| [**IsAuditedExtractAllowed**](userpolicy-isauditedextractallowed.md)<br/>         | Read-only<br/> | Gets property for allowance of audited extraction.                     |
| [**IsIssuedToOwner**](userpolicy-isissuedtoowner.md)<br/>                         | Read-only<br/> | Gets the flag indicating if the current user the is the content owner. |
| [**IssuedTo**](userpolicy-issuedto.md)<br/>                                       | Read-only<br/> | Gets the user associated with the protection policy.                   |
| [**Name**](userpolicy-name.md)<br/>                                               | Read-only<br/> | Gets the name of the policy.                                           |
| [**Owner**](userpolicy-owner.md)<br/>                                             | Read-only<br/> | Gets the email address of the content owner.                           |
| [**PolicyDescriptor**](userpolicy-policydescriptor.md)<br/>                       | Read-only<br/> | Gets the policy descriptor.                                            |
| [**SerializedPolicy**](userpolicy-serializedpolicy.md)<br/>                       | Read-only<br/> | Gets the serialized policy.                                            |
| [**SignedAppData**](userpolicy-signedappdata.md)<br/>                             | Read-only<br/> | Gets app specific data.                                                |
| [**TemplateDescriptor**](userpolicy-templatedescriptor.md)<br/>                   | Read-only<br/> | Gets the template used to publish the content.                         |
| [**Type**](userpolicy-type.md)<br/>                                               | Read-only<br/> | Gets the policy type; template based or custom.                        |



 

## Remarks

A **UserPolicy** object defines the policy that is associated with the protected content. It can be used to examine the rights of the current user as well as to protect or unprotect content.

## Thread Safety

Members of this class are not guaranteed to be thread safe.

## Requirements



|                                     |                                                                                                             |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                                   |
| Minimum supported server<br/> | None supported<br/>                                                                                   |
| Minimum supported phone<br/>  | Windows Phone 8.1<br/>                                                                                |
| Namespace<br/>                | Microsoft::RightsManagement<br/>                                                                      |
| Metadata<br/>                 | <dl> <dt>Microsoft.RightsManagement.winmd</dt> </dl> |



 

 





