---
description: The Initialize method prepares the IByteBuffer object for use. This method must be called prior to calling any other methods in the IByteBuffer interface.
ms.assetid: 1b22e693-0add-4b80-a2c4-925ebd3ab3a6
title: IByteBuffer::Initialize method (Scardssp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IByteBuffer.Initialize
api_type: 
- COM
api_location: 
- Scardssp.dll
---

# IByteBuffer::Initialize method

\[The **Initialize** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later. The [**IStream**](/windows/desktop/api/objidl/nn-objidl-istream) interface provides similar functionality.\]

The **Initialize** method prepares the [**IByteBuffer**](ibytebuffer.md) object for use. This method must be called prior to calling any other methods in the **IByteBuffer** interface.

## Syntax


```C++
HRESULT Initialize(
  [in] LONG lSize,
  [in] BYTE *pData
);
```



## Parameters

<dl> <dt>

*lSize* \[in\]
</dt> <dd>

Initial size, in bytes, of the data the stream is to contain.

</dd> <dt>

*pData* \[in\]
</dt> <dd>

If not **NULL**, the initial data to write to the stream.

</dd> </dl>

## Return value

The return value is an **HRESULT**. A value of S\_OK indicates the call was successful.

## Remarks

When using a new [**IByteBuffer**](ibytebuffer.md) stream, call this method prior to using any of the other **IByteBuffer** methods.

## Examples

The following example shows initializing the [**IByteBuffer**](ibytebuffer.md) object.


```C++
UCHAR    ucFileName[] = {0x3f, 0x00};    // Master File (MF)
HRESULT  hr;

// pIByteRequest is a pointer to an instantiated IByteBuffer object.
hr = pIByteRequest->Initialize(2, ucFileName);
if (FAILED(hr))
    printf("Failed IByteBuffer::Initialize\n");
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



 

