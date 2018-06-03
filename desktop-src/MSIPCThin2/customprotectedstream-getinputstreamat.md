---
title: CustomProtectedStream.GetInputStreamAt method
description: Returns an input stream at the specified position in the protected file.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: M:Microsoft.RightsManagement.CustomProtection.CustomProtectedStream.GetInputStreamAt(System.UInt64)
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- GetInputStreamAt method
- GetInputStreamAt method, CustomProtectedStream class
- CustomProtectedStream class, GetInputStreamAt method
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.CustomProtectedStream.GetInputStreamAt
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CustomProtectedStream.GetInputStreamAt method

Returns an input stream at the specified position in the protected file. Implements the [IRandomAccessStream.GetInputStreamAt](https://msdn.microsoft.com/library/windows/apps/windows.storage.streams.irandomaccessstream.getinputstreamat.aspx) method.

## Syntax


```C++
public:
virtual IInputStream^ GetInputStreamAt(
  unsigned long long position
)
```



## Parameters

<dl> <dt>

*position* 
</dt> <dd>

Type: [UInt64](https://msdn.microsoft.com/library/system.uint64.aspx)

The position at which to start reading the protected content in bytes.

</dd> </dl>

## Return value

Type: [IInputStream](https://msdn.microsoft.com/library/windows/apps/br241718.aspx)

The input stream.

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

 

 





