---
description: The Write method writes a specified number from bytes into the stream object starting at the current seek pointer.
ms.assetid: 0019cd10-8f8a-4190-bae4-e134e7b76882
title: IByteBuffer::Write method (Scardssp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IByteBuffer.Write
api_type: 
- COM
api_location: 
- Scardssp.dll
---

# IByteBuffer::Write method

\[The **Write** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [**IStream**](/windows/desktop/api/objidl/nn-objidl-istream) interface provides similar functionality.\]

The **Write** method writes a specified number from bytes into the stream object starting at the current seek pointer.

## Syntax


```C++
HRESULT Write(
  [in]  BYTE *pByte,
  [in]  LONG cb,
  [out] LONG *pcbWritten
);
```



## Parameters

<dl> <dt>

*pByte* \[in\]
</dt> <dd>

Address of the buffer containing the data that is to be written to the stream. A valid pointer must be provided for this parameter even when *cb* is zero.

</dd> <dt>

*cb* \[in\]
</dt> <dd>

Number of bytes of data to attempt to write into the stream. This parameter can be zero.

</dd> <dt>

*pcbWritten* \[out\]
</dt> <dd>

Address of a **LONG** variable where this method writes the actual number of bytes written to the stream object. The caller can set this pointer to **NULL**, in which case, this method does not provide the actual number of bytes written.

</dd> </dl>

## Return value

The return value is an **HRESULT**. A value of S\_OK indicates the call was successful.

## Remarks

The **IByteBuffer::Write** method writes the specified data to a stream object. The seek pointer is adjusted for the number of bytes actually written. The number of bytes actually written is returned in the *pcbWritten* parameter. If the byte count is zero bytes, the write operation has no effect.

If the seek pointer is currently past the end of the stream and the byte count is nonzero, this method increases the size of the stream to the seek pointer and writes the specified bytes starting at the seek pointer. The fill bytes written to the stream are not initialized to any particular value. This is the same as the end-of-file behavior in the MS-DOS FAT file system.

With a zero byte count and a seek pointer past the end of the stream, this method does not create the fill bytes to increase the stream to the seek pointer. In this case, you must call the [**IByteBuffer::SetSize**](ibytebuffer-setsize.md) method to increase the size of the stream and write the fill bytes.

The *pcbWritten* parameter can have a value even if an error occurs.

In the COM-provided implementation, stream objects are not sparse. Any fill bytes are eventually allocated on the disk and assigned to the stream.

## Examples

The following example shows writing bytes into the stream object.


```C++
LONG     lWrite;
HRESULT  hr;

// Write to the buffer.
// byData is an array of 64 bytes.
hr = pIByteBuff->Write(byData,
                       64,
                       &lWrite);
if (FAILED(hr))
  printf("Failed IByteBuffer::Write\n");
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



 

