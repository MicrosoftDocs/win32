---
title: CustomProtectedStream.Position property
description: Gets the current file position in bytes.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: P:Microsoft.RightsManagement.CustomProtection.CustomProtectedStream.Position
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- Position property
- Position property, CustomProtectedStream class
- CustomProtectedStream class, Position property
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.CustomProtectedStream.Position
- Microsoft.RightsManagement.CustomProtectedStream.
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CustomProtectedStream.Position property

Gets the current file position in bytes. Implements the [IRandomAccessStream.Position](https://msdn.microsoft.com/library/windows/apps/windows.storage.streams.irandomaccessstream.position.aspx) property.

## Syntax


```C++
public:
virtual property unsigned long long Position { 
   unsigned long long get();
}
```



## Property value

Type: [UInt64](https://msdn.microsoft.com/library/system.uint64.aspx)

The current file position in bytes.

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

 

 





