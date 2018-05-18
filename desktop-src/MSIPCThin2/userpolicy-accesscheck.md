---
title: UserPolicy.AccessCheck method
description: Returns a value that indicates whether the current user has the specified right.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'M:Microsoft.RightsManagement.UserPolicy.AccessCheck(Microsoft.RightsManagement.Right)'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["AccessCheck method", "AccessCheck method, UserPolicy class", "UserPolicy class, AccessCheck method"]
topic_type:
- apiref
api_name:
- Microsoft.Protection.UserPolicy.AccessCheck
api_location:
- Microsoft.Protection.dll
api_type:
- Assembly
---

# UserPolicy.AccessCheck method

Returns a value that indicates whether the current user has the specified right.

## Syntax


```C++
public:
bool AccessCheck(
  String^ right
)
```



## Parameters

<dl> <dt>

*right* 
</dt> <dd>

Type: **String^**

The right to check.

</dd> </dl>

## Return value

Type: [Boolean](https://msdn.microsoft.com/library/system.boolean.aspx)

**True** if the current user has the right; otherwise **false**.

> [!Note]  
> When called on behalf of the content owner, returns **True** for any right that is specified.

 

## Requirements



|                                     |                                                                                                             |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                                   |
| Minimum supported server<br/> | None supported<br/>                                                                                   |
| Minimum supported phone<br/>  | Windows Phone 8.1<br/>                                                                                |
| Namespace<br/>                | Microsoft::Protection<br/>                                                                            |
| Metadata<br/>                 | <dl> <dt>Microsoft.RightsManagement.winmd</dt> </dl> |



## See also

<dl> <dt>

[**UserPolicy**](userpolicy.md)
</dt> </dl>

 

 





