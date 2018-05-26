---
title: CustomProtectedStream.CreateAsync method
description: Creates a CustomProtectedStream object based on the specified protection policy and a backing stream.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: MMicrosoft.RightsManagement.CustomProtection.CustomProtectedStream.CreateAsync(Microsoft.RightsManagement.ProtectionPolicy,Windows.Storage.Streams.IRandomAccessStream,System.UInt64)
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- CreateAsync method
- CreateAsync method, CustomProtectedStream class
- CustomProtectedStream class, CreateAsync method
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.CustomProtectedStream.CreateAsync
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CustomProtectedStream.CreateAsync method

Creates a [**CustomProtectedStream**](customprotectedstream.md) object based on the specified protection policy and a backing stream. The [**CustomProtectedStream**](customprotectedstream.md) can be used for both encrypting and decrypting content. If the backing stream already contains encrypted content, you can use the stream reading functions to decrypt the content. You can also use stream writing functions to encrypt the content and write the encrypted content to the backing stream.

> \[!Warning\]  
> To avoid data loss and/or corruption, [**FlushAsync**](customprotectedstream-flushasync.md) must be called if you modify the created stream or before object disposal.

 

## Syntax


```C++
public:
static IAsyncOperation<CustomProtectedStream> CreateAsync(
  UserPolicy^ policy, 
  IRandomAccessStream^ stream, 
  unsigned long long contentStartPosition, 
  unsigned long long contentSize
)
```



## Parameters

<dl> <dt>

*policy* 
</dt> <dd>

Type: [**UserPolicy**](userpolicy.md)

The user policy to apply to protect the content.

</dd> <dt>

*stream* 
</dt> <dd>

Type: [IRandomAccessStream](https://msdn.microsoft.com/library/windows/apps/windows.storage.streams.irandomaccessstream)

The backing stream.

</dd> <dt>

*contentStartPosition* 
</dt> <dd>

Type: [UInt64](https://msdn.microsoft.com/library/system.uint64.aspx)

The start position of the stream.

</dd> <dt>

*contentSize* 
</dt> <dd>

Type: [UInt64](https://msdn.microsoft.com/library/system.uint64.aspx)

The size of the encrypted content.

</dd> </dl>

## Return value

Type: [IAsyncOperation&lt;CustomProtectedStream&gt;](https://msdn.microsoft.com/library/windows/apps/br206598.aspx)

The asynchronous operation. Upon completion, **IAsyncOperation.GetResults** returns a [**CustomProtectedStream**](customprotectedstream.md) object that can be used to write content to the file.

## Remarks

You specify a range (*contentStartPosition*, *contentSize*) where the encrypted content is located in the backing stream.

-   If there is no existing content in the backing stream (for example, if this is a new file), specify *contentSize* as zero.
-   If the existing content ends at the end of the stream, you can specify **ulong.MaxValue** for *contentSize*.
-   The *contentSize* parameter is needed only for the cases when there is non-encrypted app-specific content after the encrypted content. This is because the framework needs to know where the encrypted content ends when performing decryption.
-   The *contentSize* parameter is specified in terms of the encrypted content for example, it does include the size of the CBC padding.
-   If the range defined by the parameters *contentStartPosition* and *contentSize* is not empty (for example, *contentSize* != 0), it must address an entire segment of encrypted content; that is, it must start from block 0 and must have a final block in the CBC case or should be 16-byte aligned in the ECB case.

> \[!Warning\]  
> To avoid data loss and/or corruption, [**FlushAsync**](customprotectedstream-flushasync.md) must be called if you modify the created stream or before object disposal.

 

> \[!Warning\]  
> This method must be called on a UI thread. Calling it on a worker thread may result in an unexpected behavior.

 

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

 

 





