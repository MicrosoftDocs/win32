---
title: ProtectedFileStream.WriteAsync method
description: Writes data asynchronously to the protected file.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'M:Microsoft.RightsManagement.ProtectedFileStream.WriteAsync(Windows.Storage.Streams.IBuffer)'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["WriteAsync method", "WriteAsync method, ProtectedFileStream class", "ProtectedFileStream class, WriteAsync method"]
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.ProtectedFileStream.WriteAsync
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
---

# ProtectedFileStream.WriteAsync method

Writes data asynchronously to the protected file. Implements the [IOutputStream.WriteAsync](https://msdn.microsoft.com/library/windows/apps/windows.storage.streams.ioutputstream.writeasync.aspx) method.

## Syntax


```C++
public:
virtual IAsyncOperationWithProgress<IBuffer, UInt32>^ WriteAsync(
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

Type: [IAsyncOperationWithProgress&lt;IBuffer, UInt32&gt;](https://msdn.microsoft.com/library/windows/apps/br206594.aspx)

The byte writer operation.

## Remarks

> \[!Warning\]  
> To avoid data loss and/or corruption, [**FlushAsync**](protectedfilestream-flushasync.md) must be called if you modify the created stream or before object disposal.

 

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

 

 





