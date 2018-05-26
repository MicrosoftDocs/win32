---
title: ProtectedFileStream.CanWrite property
description: Gets a value that indicates whether the file can be written to. Implements the IRandomAccessStream.CanWrite property.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: PMicrosoft.RightsManagement.ProtectedFileStream.CanWrite
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- CanWrite property
- CanWrite property, ProtectedFileStream class
- ProtectedFileStream class, CanWrite property
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.ProtectedFileStream.CanWrite
- Microsoft.RightsManagement.ProtectedFileStream.
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ProtectedFileStream.CanWrite property

Gets a value that indicates whether the file can be written to. Implements the [IRandomAccessStream.CanWrite](https://msdn.microsoft.com/library/windows/apps/windows.storage.streams.irandomaccessstream.canwrite.aspx) property.

## Syntax


```C++
public:
virtual property bool CanWrite { 
   bool get();
}
```



## Property value

Type: [Boolean](https://msdn.microsoft.com/library/system.boolean.aspx)

**True** if the file can be written to; otherwise **false**.

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

 

 





