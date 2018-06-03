---
title: PolicyDescriptor class
description: Information required for custom protection.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: T:Microsoft.RightsManagement.PolicyDescriptor
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- PolicyDescriptor class
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.PolicyDescriptor
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PolicyDescriptor class

Information required for custom protection.

## Syntax


```C++
public ref class PolicyDescriptor sealed 
```



## Members

The **PolicyDescriptor** class inherits from [IInspectable](https://msdn.microsoft.com/library/windows/apps/br205821). **PolicyDescriptor** also has these types of members:

-   [Constructors](#constructors)
-   [Properties](#properties)

### Constructors

The **PolicyDescriptor** class has these constructors.



| Constructor                                                                                  | Description                                                                               |
|:---------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------|
| [**PolicyDescriptor(userRightsList)**](policydescriptor-policydescriptor-userrightslist.md) | Constructor for PolicyDescriptor which initializes the object with a list of user rights. |
| [**PolicyDescriptor(userRolesList)**](policydescriptor-policydescriptor-userroleslist.md)   | Constructor for PolicyDescriptor which initializes the object with a list of user roles.  |



 

### Properties

The **PolicyDescriptor** class has these properties.



| Property                                                                                     | Access type           | Description                                                          |
|:---------------------------------------------------------------------------------------------|:----------------------|:---------------------------------------------------------------------|
| [**ContentValidUntil**](policydescriptor-contentvaliduntil.md)<br/>                   | Read/write<br/> | Gets or sets the date that the content is valid until.               |
| [**Description**](policydescriptor-description.md)<br/>                               | Read/write<br/> | Gets or sets the description of the PolicyDescriptor.                |
| [**EncryptedAppData**](userroles-encryptedappdata.md)<br/>                            | Read/write<br/> | Gets or sets the encrypted app data.                                 |
| [**Name**](policydescriptor-name.md)<br/>                                             | Read/write<br/> | Gets or sets the name of the PolicyDescriptor.                       |
| [**OfflineCacheLifetimeInDays**](policydescriptor-offlinecachelifetimeindays.md)<br/> | Read/write<br/> | Gets or sets the time a user policy can be cached offline (in days). |
| [**Referrer**](policydescriptor-referrer.md)<br/>                                     | Read/write<br/> | Gets or sets the referral URI of the PolicyDescriptor.               |
| [**SignedAppData**](userroles-signedappdata.md)<br/>                                  | Read/write<br/> | Gets or sets the signed app data.                                    |
| [**UserRightsList**](policydescriptor-userrightslist.md)<br/>                         | Read-only<br/>  | Gets the UserRightsList for the PolicyDescriptor.                    |
| [**UserRolesList**](userroles-userroleslist.md)<br/>                                  | Read-only<br/>  | Gets the user's roles list.                                          |



 

## Requirements



|                                     |                                                                                                             |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                                   |
| Minimum supported server<br/> | None supported<br/>                                                                                   |
| Minimum supported phone<br/>  | Windows Phone 8.1<br/>                                                                                |
| Namespace<br/>                | Microsoft::RightsManagement<br/>                                                                      |
| Metadata<br/>                 | <dl> <dt>Microsoft.RightsManagement.winmd</dt> </dl> |



## See also

<dl> <dt>

[IInspectable](https://msdn.microsoft.com/library/windows/apps/br205821)
</dt> </dl>

 

 





