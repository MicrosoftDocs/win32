---
title: ProtectedFileStream.Position property
description: Gets the current file position in bytes.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: PMicrosoft.RightsManagement.ProtectedFileStream.Position
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- Position property
- Position property, ProtectedFileStream class
- ProtectedFileStream class, Position property
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.ProtectedFileStream.Position
- Microsoft.RightsManagement.ProtectedFileStream.
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ProtectedFileStream.Position property

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

[**ProtectedFileStream**](protectedfilestream.md)
</dt> </dl>

 

 





