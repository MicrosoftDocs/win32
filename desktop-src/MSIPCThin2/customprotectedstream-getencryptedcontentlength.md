---
title: CustomProtectedStream.GetEncryptedContentLength method
description: Calculates the length of the encrypted content from the length of the clear content.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: M:Microsoft.RightsManagement.CustomProtectedStream.GetEncryptedContentLength(Microsoft.RightsManagement.UserPolicy,System.UInt64)
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- GetEncryptedContentLength method
- GetEncryptedContentLength method, CustomProtectedStream class
- CustomProtectedStream class, GetEncryptedContentLength method
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.CustomProtectedStream.GetEncryptedContentLength
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CustomProtectedStream.GetEncryptedContentLength method

Calculates the length of the encrypted content from the length of the clear content.

## Syntax


```C++
public:
static unsigned long long GetEncryptedContentLength(
  UserPolicy^ policy, 
  unsigned long long clearContentLength
)
```



## Parameters

<dl> <dt>

*policy* 
</dt> <dd>

Type: [**UserPolicy**](userpolicy.md)

</dd> <dt>

*clearContentLength* 
</dt> <dd>

Type: [UInt64](https://msdn.microsoft.com/library/system.uint64.aspx)

</dd> </dl>

## Return value

Type: [UInt64](https://msdn.microsoft.com/library/system.uint64.aspx)

The content length.

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

[**CustomProtectedStream**](customprotectedstream.md)
</dt> </dl>

 

 





