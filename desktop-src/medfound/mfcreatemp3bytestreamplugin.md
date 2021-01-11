---
description: Creates a byte-stream handler for the MP3 media source.
ms.assetid: A213BAEF-D98F-485B-8840-BE131E9B26C0
title: MFCreateMP3ByteStreamPlugin function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MFCreateMP3ByteStreamPlugin
api_type: 
- NA
api_location: 
---

# MFCreateMP3ByteStreamPlugin function

\[This API is not supported and may be altered or unavailable in the future. Instead, applications should use the [Source Resolver](source-resolver.md) to create the MP3 media source.\]

Creates a byte-stream handler for the MP3 media source.

## Syntax


```C++
HRESULT __stdcall MFCreateMP3ByteStreamPlugin(
  _In_  REFIID riid,
  _Out_ LPVOID *ppvHandler
);
```



## Parameters

<dl> <dt>

*riid* \[in\]
</dt> <dd>

The interface identifier (IID) of the requested interface. Set this parameter to **IID\_IMFByteStreamHandler** to receive a pointer to the [**IMFByteStreamHandler**](/windows/desktop/api/mfidl/nn-mfidl-imfbytestreamhandler) interface.

</dd> <dt>

*ppvHandler* \[out\]
</dt> <dd>

Receives a pointer to the interface. The caller must release the interface.

</dd> </dl>

## Return value

If this function succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

This function has no associated import library. To call this function, you must use the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions to dynamically link to mf.dll.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |
| End of client support<br/>    | Windows Vista<br/>                             |
| End of server support<br/>    | Windows Server 2008<br/>                       |



## See also

<dl> <dt>

[Media Foundation Functions](media-foundation-functions.md)
</dt> <dt>

[Scheme Handlers and Byte-Stream Handlers](scheme-handlers-and-byte-stream-handlers.md)
</dt> <dt>

[Source Resolver](source-resolver.md)
</dt> </dl>

 

 
