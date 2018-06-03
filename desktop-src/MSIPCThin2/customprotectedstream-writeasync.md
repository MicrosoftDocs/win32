---
title: CustomProtectedStream.WriteAsync method
description: Writes data asynchronously to the backing file.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: M:Microsoft.RightsManagement.CustomProtection.CustomProtectedStream.WriteAsync(Windows.Storage.Streams.IBuffer)
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- WriteAsync method
- WriteAsync method, CustomProtectedStream class
- CustomProtectedStream class, WriteAsync method
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.CustomProtectedStream.WriteAsync
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CustomProtectedStream.WriteAsync method

Writes data asynchronously to the backing file.

Implements the [IOutputStream.WriteAsync](https://msdn.microsoft.com/library/windows/apps/windows.storage.streams.ioutputstream.writeasync.aspx) method.

## Syntax


```C++
public:
virtual 
      IAsyncOperationWithProgress<uint32, uint32>
      WriteAsync(
  IBuffer^ buffer
)
```



## Parameters

<dl> <dt>

*buffer* 
</dt> <dd>

Type: [IBuffer](https://msdn.microsoft.com/library/windows/apps/windows.storage.streams.iinputstream.aspx)

The buffer into which the asynchronous write operation writes.

</dd> </dl>

## Return value

Type: **IAsyncOperationWithProgress&lt;uint32, uint32&gt;**

The byte writer operation.

## Remarks

Data written to the stream must be 16-byte aligned.

> \[!Warning\]  
> To avoid data loss and/or corruption, [**FlushAsync**](customprotectedstream-flushasync.md) must be called if you modify the created stream or before object disposal.

 

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

 

 





