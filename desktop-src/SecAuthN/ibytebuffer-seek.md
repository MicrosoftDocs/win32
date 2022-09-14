---
description: The Seek method changes the seek pointer to a new location relative to the beginning of the buffer, to the end of the buffer, or to the current seek pointer.
ms.assetid: 3541f3dd-7b92-4f72-89b7-4e04e007aaa3
title: IByteBuffer::Seek method (Scardssp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IByteBuffer.Seek
api_type: 
- COM
api_location: 
- Scardssp.dll
---

# IByteBuffer::Seek method

\[The **Seek** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [**IStream**](/windows/desktop/api/objidl/nn-objidl-istream) interface provides similar functionality.\]

The **Seek** method changes the seek pointer to a new location relative to the beginning of the buffer, to the end of the buffer, or to the current seek pointer.

## Syntax


```C++
HRESULT Seek(
  [in]  LONG dlibMove,
  [in]  LONG dwOrigin,
  [out] LONG *plibNewPosition
);
```



## Parameters

<dl> <dt>

*dlibMove* \[in\]
</dt> <dd>

Displacement to be added to the location indicated by *dwOrigin*. If *dwOrigin* is STREAM\_SEEK\_SET, this is interpreted as an unsigned value rather than signed.

</dd> <dt>

*dwOrigin* \[in\]
</dt> <dd>

Specifies the origin for the displacement specified in *dlibMove*. The origin can be one of the values in the following table.



| Value                                                                                                                                                                | Meaning                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="STREAM_SEEK_SET"></span><span id="stream_seek_set"></span><dl> <dt>**STREAM\_SEEK\_SET**</dt> </dl> | The new seek pointer is an offset relative to the beginning of the stream. In this case, the *dlibMove* parameter is the new seek position relative to the beginning of the stream.<br/> |
| <span id="STREAM_SEEK_CUR"></span><span id="stream_seek_cur"></span><dl> <dt>**STREAM\_SEEK\_CUR**</dt> </dl> | The new seek pointer is an offset relative to the current seek pointer location. In this case, the *dlibMove* parameter is the signed displacement from the current seek position.<br/>  |
| <span id="STREAM_SEEK_END"></span><span id="stream_seek_end"></span><dl> <dt>**STREAM\_SEEK\_END**</dt> </dl> | The new seek pointer is an offset relative to the end of the stream. In this case, the *dlibMove* parameter is the new seek position relative to the end of the stream.<br/>             |



 

</dd> <dt>

*plibNewPosition* \[out\]
</dt> <dd>

Pointer to the location where this method writes the value of the new seek pointer from the beginning of the stream. You can set this pointer to **NULL** to indicate that you are not interested in this value. In this case, this method does not provide the new seek pointer.

</dd> </dl>

## Return value

The return value is an **HRESULT**. A value of S\_OK indicates the call was successful.

## Remarks

The **Seek** method changes the seek pointer so subsequent read and write operations can take place at a different location in the stream object. It is an error to seek before the beginning of the stream. It is not, however, an error to seek past the end of the stream. Seeking past the end of the stream is useful for subsequent write operations, as the stream will at that time be extended to the seek position immediately before the write operation is done.

You can also use this method to obtain the current value of the seek pointer by calling this method with the *dwOrigin* parameter set to STREAM\_SEEK\_CUR and the *dlibMove* parameter set to zero so the seek pointer is not changed. The current seek pointer is returned in the *plibNewPosition* parameter.

## Examples

The following example shows positioning the seek pointer to a new location.


```C++
LONG     lNewPos;
HRESULT  hr;

// Change the seek pointer.
hr = pIByteBuff->Seek(5, STREAM_SEEK_SET, &lNewPos);
if (FAILED(hr))
  printf("Failed IByteBuffer::Seek\n");
else
  printf("New position is %x\n", lNewPos);
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| End of client support<br/>    | Windows XP<br/>                                                                   |
| End of server support<br/>    | Windows Server 2003<br/>                                                          |
| Header<br/>                   | <dl> <dt>Scardssp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Scardssp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Scardssp.dll</dt> </dl> |
| IID<br/>                      | IID\_IByteBuffer is defined as E126F8FE-A7AF-11D0-B88A-00C04FD424B9<br/>          |



 

