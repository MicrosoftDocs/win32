---
Description: 'Note  This interface is deprecated. New applications should not use it. Retrieves the stream''s purpose ID and media type.'
ms.assetid: 'e4ecae45-e2bf-44dd-8901-0892c02d708c'
title: 'IMediaStream::GetInformation method'
---

# IMediaStream::GetInformation method

> [!Note]  
> This interface is deprecated. New applications should not use it.

 

Retrieves the stream's purpose ID and media type.

## Syntax


```C++
HRESULT GetInformation(
  [out] MSPID       *pPurposeId,
  [out] STREAM_TYPE *pType
);
```



## Parameters

<dl> <dt>

*pPurposeId* \[out\]
</dt> <dd>

Pointer to an **MSPID** value that will contain the stream's purpose ID (see [Multimedia Streaming Data Types](multimedia-streaming-data-types.md)). If this parameter is **NULL** on entry, the method won't retrieve the purpose ID.

</dd> <dt>

*pType* \[out\]
</dt> <dd>

Pointer to a [**STREAM\_TYPE**](stream-type.md) enumerated data type value that will contain the stream's media type. If this parameter is **NULL** on entry, the method won't retrieve the media type.

</dd> </dl>

## Return value

Returns S\_OK if successful or E\_POINTER if one of the parameters is invalid.

## Remarks

The value retrieved in the *pPurposeId* parameter will usually be either MSPID\_PrimaryVideo, which identifies the primary video stream, or MSPID\_PrimaryAudio, which identifies the primary audio stream; however, you can define other values if necessary.

## See also

<dl> <dt>

[**IMediaStream Interface**](imediastream.md)
</dt> </dl>

 

 



