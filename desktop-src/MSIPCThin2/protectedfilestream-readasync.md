---
title: ProtectedFileStream.ReadAsync method
description: Returns an asynchronous byte reader object.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: MMicrosoft.RightsManagement.ProtectedFileStream.ReadAsync(Windows.Storage.Streams.IBuffer,System.UInt32,Windows.Storage.Streams.InputStreamOptions)
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- ReadAsync method
- ReadAsync method, ProtectedFileStream class
- ProtectedFileStream class, ReadAsync method
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.ProtectedFileStream.ReadAsync
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ProtectedFileStream.ReadAsync method

Returns an asynchronous byte reader object. Implements the [IInputStream.ReadAsync](https://msdn.microsoft.com/library/windows/apps/windows.storage.streams.iinputstream.readasync.aspx) method.

## Syntax


```C++
public:
virtual IAsyncOperationWithProgress<IBuffer, UInt32>^ ReadAsync(
  IBuffer^ buffer, 
  unsigned int count, 
  InputStreamOptions options
)
```



## Parameters

<dl> <dt>

*buffer* 
</dt> <dd>

Type: [IBuffer](https://msdn.microsoft.com/library/windows/apps/windows.storage.streams.iinputstream.aspx)

The buffer into which the asynchronous read operation places the bytes that are read.

</dd> <dt>

*count* 
</dt> <dd>

Type: [UInt32](https://msdn.microsoft.com/library/system.uint32.aspx)

The number of bytes to read that is less than or equal to the capacity of the buffer.

</dd> <dt>

*options* 
</dt> <dd>

Type: [InputStreamOptions](https://msdn.microsoft.com/library/windows/apps/windows.storage.streams.inputstreamoptions.aspx)

Specifies the type of the asynchronous read operation.

</dd> </dl>

## Return value

Type: [IAsyncOperationWithProgress&lt;IBuffer, UInt32&gt;](https://msdn.microsoft.com/library/windows/apps/br206594.aspx)

The asynchronous operation.

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

 

 





