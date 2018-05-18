---
title: CustomProtectedStream.CloneStream method
description: Creates a new instance of CustomProtectedStream over the protected content.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'M:Microsoft.RightsManagement.CustomProtection.CustomProtectedStream.CloneStream'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["CloneStream method", "CloneStream method, CustomProtectedStream class", "CustomProtectedStream class, CloneStream method"]
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.CustomProtectedStream.CloneStream
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
---

# CustomProtectedStream.CloneStream method

Creates a new instance of [**CustomProtectedStream**](customprotectedstream.md) over the protected content. Implements the [IRandomAccessStream.CloneStream](https://msdn.microsoft.com/library/windows/apps/windows.storage.streams.irandomaccessstream.clonestream.aspx) method.

## Syntax


```C++
public:
virtual IRandomAccessStream^ CloneStream()
```



## Parameters

This method has no parameters.

## Return value

Type: [IRandomAccessStream](https://msdn.microsoft.com/library/windows/apps/windows.storage.streams.irandomaccessstream)

A [**CustomProtectedStream**](customprotectedstream.md) object that represents the new stream. The initial, internal position of the stream is 0 (zero). The internal position and lifetime of the new stream are independent from the position and lifetime of the cloned stream.

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

 

 





