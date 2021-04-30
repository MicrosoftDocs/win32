---
description: The CopyTo method copies a specified number of bytes from the current seek pointer in the object to the current seek pointer in another object.
ms.assetid: 2044965f-665f-4aa1-abc0-42f5278dd647
title: IByteBuffer::CopyTo method (Scardssp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IByteBuffer.CopyTo
api_type: 
- COM
api_location: 
- Scardssp.dll
---

# IByteBuffer::CopyTo method

\[The **CopyTo** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [**IStream**](/windows/desktop/api/objidl/nn-objidl-istream) interface provides similar functionality.\]

The **CopyTo** method copies a specified number of bytes from the current seek pointer in the object to the current seek pointer in another object.

## Syntax


```C++
HRESULT CopyTo(
  [in]  LPBYTEBUFFER *pByteBuffer,
  [in]  LONG         cb,
  [out] LONG         *pcbRead,
  [out] LONG         *pcbWritten
);
```



## Parameters

<dl> <dt>

*pByteBuffer* \[in\]
</dt> <dd>

Points to the destination stream. The stream pointed to by *pByteBuffer* can be a new stream or a clone of the source stream.

</dd> <dt>

*cb* \[in\]
</dt> <dd>

Number of bytes to copy from the source stream.

</dd> <dt>

*pcbRead* \[out\]
</dt> <dd>

Pointer to the location where this method writes the actual number of bytes read from the source. You can set this pointer to **NULL** to indicate that you are not interested in this value. In this case, this method does not provide the actual number of bytes read.

</dd> <dt>

*pcbWritten* \[out\]
</dt> <dd>

Pointer to the location where this method writes the actual number of bytes written to the destination. You can set this pointer to **NULL** to indicate that you are not interested in this value. In this case, this method does not provide the actual number of bytes written.

</dd> </dl>

## Return value

The return value is an **HRESULT**. A value of S\_OK indicates the call was successful.

## Remarks

This method copies the specified bytes from one stream to another. It can also be used to copy a stream to itself. The seek pointer in each stream instance is adjusted for the number of bytes read or written.

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



 

