---
title: CustomProtectedStream.Seek method
description: Sets the current position to the specified number of bytes from the start of the file.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: M:Microsoft.RightsManagement.CustomProtection.CustomProtectedStream.Seek(System.UInt64)
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- Seek method
- Seek method, CustomProtectedStream class
- CustomProtectedStream class, Seek method
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.CustomProtectedStream.Seek
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CustomProtectedStream.Seek method

Sets the current position to the specified number of bytes from the start of the file. Implements the [IRandomAccessStream.Seek](https://msdn.microsoft.com/library/windows/apps/windows.storage.streams.irandomaccessstream.seek.aspx) method .

## Syntax


```C++
public:
virtual void Seek(
  unsigned long long position
)
```



## Parameters

<dl> <dt>

*position* 
</dt> <dd>

Type: [UInt64](https://msdn.microsoft.com/library/system.uint64.aspx)

The number of bytes from the start of the file at which to set the position.

</dd> </dl>

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
</dt> <dt>

[**Position**](customprotectedstream-position.md)
</dt> </dl>

 

 





