---
Description: 'Note  This interface is deprecated. New applications should not use it. The GetMediaStream method retrieves a media stream, specified by purpose ID.'
ms.assetid: 'd85cde4f-99f4-4641-b75f-13ca6dc7f21e'
title: 'IMultiMediaStream::GetMediaStream method'
---

# IMultiMediaStream::GetMediaStream method

> [!Note]  
> This interface is deprecated. New applications should not use it.

 

The `GetMediaStream` method retrieves a media stream, specified by purpose ID.

## Syntax


```C++
HRESULT GetMediaStream(
   REFMSPID     idPurpose,
   IMediaStream **ppMediaStream
);
```



## Parameters

<dl> <dt>

*idPurpose* 
</dt> <dd>

Reference to an [**MSPID**](mspid.md) that identifies the media stream to retrieve.

</dd> <dt>

*ppMediaStream* 
</dt> <dd>

Address of variable that receives an [**IMediaStream**](imediastream.md) interface pointer.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include the following.



| Return code                                                                                    | Description                        |
|------------------------------------------------------------------------------------------------|------------------------------------|
| <dl> <dt>**E\_POINTER**</dt> </dl>      | **NULL** pointer valid.<br/> |
| <dl> <dt>**MS\_E\_NOSTREAM**</dt> </dl> | No matching stream.<br/>     |
| <dl> <dt>**S\_OK**</dt> </dl>           | Success.<br/>                |



 

## Remarks

If the method succeeds, the caller must release the **IMediaStream** interface.

## See also

<dl> <dt>

[**IMultiMediaStream Interface**](imultimediastream.md)
</dt> </dl>

 

 




