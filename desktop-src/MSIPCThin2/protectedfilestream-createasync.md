---
title: ProtectedFileStream.CreateAsync method
description: Creates a ProtectedFileStream from a UserPolicy object and a backing stream.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'M:Microsoft.RightsManagement.ProtectedFileStream.CreateAsync(Windows.Storage.Streams.IRandomAccessStream,Microsoft.RightsManagement.ProtectionOperationOptions)'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["CreateAsync method", "CreateAsync method, ProtectedFileStream class", "ProtectedFileStream class, CreateAsync method"]
topic_type:
- apiref
api_name:
- Microsoft.Protection.ProtectedFileStream.CreateAsync
api_location:
- Microsoft.Protection.dll
api_type:
- Assembly
---

# ProtectedFileStream.CreateAsync method

Creates a [**ProtectedFileStream**](protectedfilestream.md) from a [**UserPolicy**](userpolicy.md) object and a backing stream.

This method is used to create a protected file. The protected file is written to the specified backing stream. The policy used to protect the protected file is defined by the specified [**UserPolicy**](userpolicy.md) object. The resulting [**ProtectedFileStream**](protectedfilestream.md) can be used to write the actual content of the protected file (as a regular IRandomAccessStream).

> \[!Warning\]  
> To avoid data loss and/or corruption, [**FlushAsync**](protectedfilestream-flushasync.md) must be called if you modify the created stream or before object disposal.

 

> \[!Warning\]  
> This method must be called on a UI thread. Calling it on a worker thread may result in an unexpected behavior.

 

## Syntax


```C++
public:
static IAsyncOperation<ProtectedFileStream> CreateAsync(
  UserPolicy^ policy, 
  IRandomAccessStream^ inputStream, 
  String^ originalFileExtension
)
```



## Parameters

<dl> <dt>

*policy* 
</dt> <dd>

Type: [**UserPolicy**](userpolicy.md)

The [**UserPolicy**](userpolicy.md) object that defines the policy used to protect the created PFILE.

</dd> <dt>

*inputStream* 
</dt> <dd>

Type: [IRandomAccessStream](https://msdn.microsoft.com/library/windows/apps/windows.storage.streams.irandomaccessstream)

The stream from which the protected file is loaded.

</dd> <dt>

*originalFileExtension* 
</dt> <dd>

Type: **String**

The original (i.e. unprotected) file extension.

</dd> </dl>

## Return value

Type: [IAsyncOperation&lt;ProtectedFileStream&gt;](https://msdn.microsoft.com/library/windows/apps/br206598.aspx)

The asynchronous operation. Upon completion, **IAsyncOperation.GetResults** returns a [**ProtectedFileStream**](protectedfilestream.md) object that can be used to write content to the protected file.

## Remarks

The [**Policy**](protectedfilestream-policy.md) property of the new [**ProtectedFileStream**](protectedfilestream.md) object is populated from the protected file.

> \[!Warning\]  
> To avoid data loss and/or corruption, [**FlushAsync**](protectedfilestream-flushasync.md) must be called if you modify the created stream or before object disposal.

 

> \[!Warning\]  
> This method must be called on a UI thread. Calling it on a worker thread may result in an unexpected behavior.

 

## Requirements



|                                     |                                                                                                             |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                                   |
| Minimum supported server<br/> | None supported<br/>                                                                                   |
| Minimum supported phone<br/>  | Windows Phone 8.1<br/>                                                                                |
| Namespace<br/>                | Microsoft::Protection<br/>                                                                            |
| Metadata<br/>                 | <dl> <dt>Microsoft.RightsManagement.winmd</dt> </dl> |



## See also

<dl> <dt>

[**ProtectedFileStream**](protectedfilestream.md)
</dt> </dl>

 

 





