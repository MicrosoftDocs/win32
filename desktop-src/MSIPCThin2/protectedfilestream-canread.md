---
title: ProtectedFileStream.CanRead property
description: Gets a value that indicates whether the file can be read from. Implements the IRandomAccessStream.CanRead property.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: P:Microsoft.RightsManagement.ProtectedFileStream.CanRead
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- CanRead property
- CanRead property, ProtectedFileStream class
- ProtectedFileStream class, CanRead property
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.ProtectedFileStream.CanRead
- Microsoft.RightsManagement.ProtectedFileStream.
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ProtectedFileStream.CanRead property

Gets a value that indicates whether the file can be read from. Implements the [IRandomAccessStream.CanRead](https://msdn.microsoft.com/library/windows/apps/windows.storage.streams.irandomaccessstream.canread.aspx) property.

## Syntax


```C++
public:
virtual property bool CanRead { 
   bool get();
}
```



## Property value

Type: [Boolean](https://msdn.microsoft.com/library/system.boolean.aspx)

**True** if the file can be read from; otherwise **false**.

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

 

 





