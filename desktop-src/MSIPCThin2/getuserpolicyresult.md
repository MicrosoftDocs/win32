---
title: GetUserPolicyResult class
description: Provides access for the referrer.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'T:Microsoft.RightsManagement.GetUserPolicyResult'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["GetUserPolicyResult class"]
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.GetUserPolicyResult
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
---

# GetUserPolicyResult class

Provides access for the referrer. This class implements a workaround for Rights Management SDK 4.2 for Windows RT and Windows Phone by creating a structure for getting the referrer.

On other supported operating systems, *UserPolicy.AcquireAsync()* directly returns a *UserPolicy* and returns the referrer via a custom "no rights" exception or whatever error handling mechanism is used for the platform (ex. NSError in iOS/OS X).

## Syntax


```C++
public ref class GetUserPolicyResult sealed 
```



## Members

The **GetUserPolicyResult** class inherits from [IInspectable](https://msdn.microsoft.com/library/windows/apps/br205821). **GetUserPolicyResult** also has these types of members:

-   [Properties](#properties)

### Properties

The **GetUserPolicyResult** class has these properties.



| Property                                                    | Access type          | Description                                  |
|:------------------------------------------------------------|:---------------------|:---------------------------------------------|
| [**Policy**](getuserpolicyresult-policy.md)<br/>     | Read-only<br/> | The protection policy if the call succeeded. |
| [**Referrer**](getuserpolicyresult-referrer.md)<br/> | Read-only<br/> | Referral info.                               |
| [**Status**](getuserpolicyresult-status.md)<br/>     | Read-only<br/> | The return code                              |



 

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

 

 





