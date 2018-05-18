---
title: ProtectedFileStream.Size property
description: Gets or sets the size of the protected data in bytes.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'P:Microsoft.RightsManagement.ProtectedFileStream.Size'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["Size property", "Size property, ProtectedFileStream class", "ProtectedFileStream class, Size property"]
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.ProtectedFileStream.Size
- Microsoft.RightsManagement.ProtectedFileStream.
- Microsoft.RightsManagement.ProtectedFileStream.
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
---

# ProtectedFileStream.Size property

Gets or sets the size of the protected data in bytes. Implements the [IRandomAccessStream.Size](https://msdn.microsoft.com/library/windows/apps/windows.storage.streams.irandomaccessstream.size.aspx) property.

## Syntax


```C++
public:
virtual property unsigned long long Size { 
   unsigned long long get();
   void set (unsigned long long value);
}
```



## Property value

Type: [UInt64](https://msdn.microsoft.com/library/system.uint64.aspx)

The size of the protected data in bytes.

## Remarks

> \[!Warning\]  
> To avoid data loss and/or corruption, [**FlushAsync**](protectedfilestream-flushasync.md) must be called if you modify the created stream or before object disposal.

 

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

[**ProtectedFileStream**](protectedfilestream.md)
</dt> </dl>

 

 





