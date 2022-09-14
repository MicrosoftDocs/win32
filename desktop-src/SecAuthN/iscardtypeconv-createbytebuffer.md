---
description: Creates a universal buffer of bytes mapped into an IStream (IByteBuffer) object.
ms.assetid: 8015c7e8-2cbb-4ba8-9bd0-2f84751840f1
title: ISCardTypeConv::CreateByteBuffer method (Scarddat.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCardTypeConv.CreateByteBuffer
api_type: 
- COM
api_location: 
- Scardssp.dll
---

# ISCardTypeConv::CreateByteBuffer method

\[The **CreateByteBuffer** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **CreateByteBuffer** method creates a universal buffer of bytes mapped into an **IStream** ([**IByteBuffer**](ibytebuffer.md)) object.

The byte buffer created is a stream mapped over a memory block. To access or manage the buffer, use the methods provided by the **IStream** interface. A unique feature about this array implementation is that when you call the **IStream::Release** method, the underlying memory will be released for you.

## Syntax


```C++
HRESULT CreateByteBuffer(
  [in]  DWORD        dwAllocSize,
  [out] LPBYTEBUFFER *ppbyBuff
);
```



## Parameters

<dl> <dt>

*dwAllocSize* \[in\]
</dt> <dd>

Size in bytes of the memory to be allocated for the array.

</dd> <dt>

*ppbyBuff* \[out\]
</dt> <dd>

Pointer to the IStream object to be returned.

</dd> </dl>

## Return value

The possible return values are the following:



| Return code                                                                                   | Description                                                                                      |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Memory allocated successfully.<br/>                                                        |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | There is something wrong with one or more of the parameters passed into the function.<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Not enough free memory to satisfy request.<br/>                                            |



 

## Remarks

Memory allocated is movable. Use the **IStream::Release** method to free the memory.

To create a typical C/C++ byte array, call [**CreateByteArray**](iscardtypeconv-createbytearray.md).

To create an Automation SAFEARRAY of unsigned characters (bytes), call [**CreateSafeArray**](iscardtypeconv-createsafearray.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| End of client support<br/>    | Windows XP<br/>                                                                   |
| End of server support<br/>    | Windows Server 2003<br/>                                                          |
| Header<br/>                   | <dl> <dt>Scarddat.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Scarddat.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Scardssp.dll</dt> </dl> |
| IID<br/>                      | IID\_ISCardTypeConv is defined as 53B6AA63-3F56-11D0-916B-00AA00C18068<br/>       |



## See also

<dl> <dt>

[**ISCardTypeConv**](iscardtypeconv.md)
</dt> <dt>

[Smart Card Return Values](authentication-return-values.md)
</dt> <dt>

[**CreateByteArray**](iscardtypeconv-createbytearray.md)
</dt> <dt>

[**CreateSafeArray**](iscardtypeconv-createsafearray.md)
</dt> </dl>

 

 
