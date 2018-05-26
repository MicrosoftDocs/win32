---
title: ProtectedFileStream.CloneStream method
description: Creates a new instance of ProtectedFileStream over the protected file.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: MMicrosoft.RightsManagement.ProtectedFileStream.CloneStream
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- CloneStream method
- CloneStream method, ProtectedFileStream class
- ProtectedFileStream class, CloneStream method
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.ProtectedFileStream.CloneStream
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ProtectedFileStream.CloneStream method

Creates a new instance of [**ProtectedFileStream**](protectedfilestream.md) over the protected file. Implements the [IRandomAccessStream.CloneStream](https://msdn.microsoft.com/library/windows/apps/windows.storage.streams.irandomaccessstream.clonestream.aspx) method.

## Syntax


```C++
public:
virtual IRandomAccessStream^ CloneStream()
```



## Parameters

This method has no parameters.

## Return value

Type: [IRandomAccessStream](https://msdn.microsoft.com/library/windows/apps/windows.storage.streams.irandomaccessstream)

A [**ProtectedFileStream**](protectedfilestream.md) object that represents the new stream. The initial, internal position of the stream is 0. The internal position and lifetime of the new stream are independent from the position and lifetime of the cloned stream.

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

 

 





