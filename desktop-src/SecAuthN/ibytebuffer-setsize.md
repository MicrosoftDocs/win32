---
description: The SetSize method changes the size of the stream object.
ms.assetid: e4027a98-fce4-4db4-a9fe-e7e7436b5147
title: IByteBuffer::SetSize method (Scardssp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IByteBuffer.SetSize
api_type: 
- COM
api_location: 
- Scardssp.dll
---

# IByteBuffer::SetSize method

\[The **SetSize** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [**IStream**](/windows/desktop/api/objidl/nn-objidl-istream) interface provides similar functionality.\]

The **SetSize** method changes the size of the stream object.

## Syntax


```C++
HRESULT SetSize(
  [in] LONG libNewSize
);
```



## Parameters

<dl> <dt>

*libNewSize* \[in\]
</dt> <dd>

New size of the stream as a number of bytes

</dd> </dl>

## Return value

The return value is an **HRESULT**. A value of S\_OK indicates the call was successful.

## Remarks

The **IByteBuffer::SetSize** method changes the size of the stream object. Call this method to preallocate space for the stream. If the *libNewSize* parameter is larger than the current stream size, the stream is extended to the indicated size by filling the intervening space with bytes of undefined value. This operation is similar to the [**IByteBuffer::Write**](ibytebuffer-write.md) method if the seek pointer is past the current end-of-stream.

If the *libNewSize* parameter is smaller than the current stream, then the stream is truncated to the indicated size.

The seek pointer is not affected by the change in stream size.

Calling **IByteBuffer::SetSize** can be an effective way of trying to obtain a large chunk of contiguous space.

## Examples

The following example shows setting the buffer size.


```C++
LONG     lNewSize = 256;
HRESULT  hr;

// Change the buffer size.
hr = pIByteBuff->SetSize(lNewSize);
if (FAILED(hr))
  printf("Failed IByteBuffer::SetSize\n");
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



 

