---
Description: 'Note  This interface is deprecated. New applications should not use it. The EnumMediaStreams method retrieves a media stream object, specified by index.'
ms.assetid: '2fb51794-83ac-44c5-b388-d7b945870324'
title: 'IMultiMediaStream::EnumMediaStreams method'
---

# IMultiMediaStream::EnumMediaStreams method

> [!Note]  
> This interface is deprecated. New applications should not use it.

 

The `EnumMediaStreams` method retrieves a media stream object, specified by index.

## Syntax


```C++
HRESULT EnumMediaStreams(
  [in]  long         Index,
  [out] IMediaStream **ppMediaStream
);
```



## Parameters

<dl> <dt>

*Index* \[in\]
</dt> <dd>

Zero-based index of the media stream to retrieve.

</dd> <dt>

*ppMediaStream* \[out\]
</dt> <dd>

Address of a variable that receives an [**IMediaStream**](imediastream.md) interface pointer.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include the following.



| Return code                                                                               | Description                           |
|-------------------------------------------------------------------------------------------|---------------------------------------|
| <dl> <dt>**E\_POINTER**</dt> </dl> | **NULL** pointer argument.<br/> |
| <dl> <dt>**S\_FALSE**</dt> </dl>   | Index is out of range.<br/>     |
| <dl> <dt>**S\_OK**</dt> </dl>      | Success.<br/>                   |



 

## Remarks

If the return value is S\_OK, the caller must release the **IMediaStream** interface.

## See also

<dl> <dt>

[**IMultiMediaStream Interface**](imultimediastream.md)
</dt> </dl>

 

 




