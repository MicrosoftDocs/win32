---
title: IConsent interface
description: Used to manage types of user consent.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'T:Microsoft.RightsManagement.IConsent'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["IConsent interface"]
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.IConsent
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
---

# IConsent interface

Used to manage types of user consent.

## Syntax


```C++
public interface class IConsent : IInspectable
```



## Members

The **IConsent** interface inherits from [IInspectable](https://msdn.microsoft.com/library/windows/apps/br205821). **IConsent** also has these types of members:

-   [Properties](#properties)

### Properties

The **IConsent** interface has these properties.



| Property                                     | Access type           | Description                                         |
|:---------------------------------------------|:----------------------|:----------------------------------------------------|
| [**Domain**](iconsent-domain.md)<br/> | Read-only<br/>  | Gets the domain information.                        |
| [**Result**](iconsent-result.md)<br/> | Read/write<br/> | Gets or sets the consent result.                    |
| [**Type**](iconsent-type.md)<br/>     | Read-only<br/>  | Gets the type of consent.                           |
| [**Urls**](iconsent-urls.md)<br/>     | Read-only<br/>  | Gets the list of URLs that need to provide consent. |
| [**User**](iconsent-user.md)<br/>     | Read-only<br/>  | Gets the user ID.                                   |



 

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

 

 





