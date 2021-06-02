---
description: The Read method reads a specified number of bytes from the buffer object into memory starting at the current seek pointer.
ms.assetid: 98c4de75-9ecf-4c57-9075-9d0e3675079f
title: IByteBuffer::Read method (Scardssp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IByteBuffer.Read
api_type: 
- COM
api_location: 
- Scardssp.dll
---

# IByteBuffer::Read method

\[The **Read** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [**IStream**](/windows/desktop/api/objidl/nn-objidl-istream) interface provides similar functionality.\]

The **Read** method reads a specified number of bytes from the buffer object into memory starting at the current seek pointer.

## Syntax


```C++
HRESULT Read(
  [out] BYTE *pByte,
  [in]  LONG cb,
  [out] LONG *pcbRead
);
```



## Parameters

<dl> <dt>

*pByte* \[out\]
</dt> <dd>

Points to the buffer into which the stream data is read. If an error occurs, this value is **NULL**.

</dd> <dt>

*cb* \[in\]
</dt> <dd>

Number of bytes of data to attempt to read from the stream object.

</dd> <dt>

*pcbRead* \[out\]
</dt> <dd>

Address of a **LONG** variable that receives the actual number of bytes read from the stream object. You can set this pointer to **NULL** to indicate that you are not interested in this value. In this case, this method does not provide the actual number of bytes read.

</dd> </dl>

## Return value

The return value is an **HRESULT**. A value of S\_OK indicates the call was successful.

## Remarks

This method reads bytes from this stream object into memory. The stream object must be opened in STGM\_READ mode. This method adjusts the seek pointer by the actual number of bytes read.

The number of bytes actually read is also returned in the *pcbRead* parameter.

Notes to Callers

The actual number of bytes read can be fewer than the number of bytes requested if an error occurs or if the end of the stream is reached during the read operation.

Some implementations might return an error if the end of the stream is reached during the read. You must be prepared to deal with the error return or S\_OK return values on end of stream reads.

## Examples

The following example shows reading bytes from the buffer.


```C++
BYTE     byAtr[32];
long     lBytesRead, i;
HRESULT  hr;

// pAtr is a pointer to a previously instantiated IByteBuffer.
// It was used in an earlier call by ISCard::get_Atr.
// Use IByteBuffer::Read to access the retrieved ATR bytes.
hr = pAtr->Read(byAtr, 32, &lBytesRead);
// Use the ATR value. (This example merely displays the bytes.)
for ( i = 0; i < lBytesRead; i++)
    printf("%c", *(byAtr + i));
printf("\n");
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



 

