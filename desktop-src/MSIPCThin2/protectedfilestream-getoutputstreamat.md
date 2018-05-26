---
title: ProtectedFileStream.GetOutputStreamAt method
description: Returns an output stream at the specified location in the protected file.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: MMicrosoft.RightsManagement.ProtectedFileStream.GetOutputStreamAt(System.UInt64)
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- GetOutputStreamAt method
- GetOutputStreamAt method, ProtectedFileStream class
- ProtectedFileStream class, GetOutputStreamAt method
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.ProtectedFileStream.GetOutputStreamAt
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ProtectedFileStream.GetOutputStreamAt method

Returns an output stream at the specified location in the protected file. Implements the [IRandomAccessStream.GetOutputStreamAt](https://msdn.microsoft.com/library/windows/apps/windows.storage.streams.irandomaccessstream.getoutputstreamat.aspx) method.

## Syntax


```C++
public:
virtual IOutputStream^ GetOutputStreamAt(
  unsigned long long position
)
```



## Parameters

<dl> <dt>

*position* 
</dt> <dd>

Type: [UInt64](https://msdn.microsoft.com/library/system.uint64.aspx)

The position at which to start writing to the protected file in bytes.

</dd> </dl>

## Return value

Type: [IOutputStream](https://msdn.microsoft.com/library/windows/apps/windows.storage.streams.ioutputstream.aspx)

The output stream.

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

 

 





