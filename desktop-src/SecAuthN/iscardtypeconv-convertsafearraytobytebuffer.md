---
description: Converts a byte array defined as a SAFEARRAY into a universal buffer of bytes (IStream object).
ms.assetid: faa07bb5-cfdb-4181-b86a-f82a9c6b251a
title: ISCardTypeConv::ConvertSafeArrayToByteBuffer method (Scarddat.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCardTypeConv.ConvertSafeArrayToByteBuffer
api_type: 
- COM
api_location: 
- Scardssp.dll
---

# ISCardTypeConv::ConvertSafeArrayToByteBuffer method

\[The **ConvertSafeArrayToByteBuffer** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **ConvertSafeArrayToByteBuffer** method converts a byte array defined as a SAFEARRAY into a universal buffer of bytes (**IStream** object).

The byte buffer created is a stream mapped over a memory block. To access or manage the buffer, use the methods provided by the **IStream** interface. A unique feature about this array implementation is that when you call the **IStream::Release** method, the underlying memory will be released for you.

## Syntax


```C++
HRESULT ConvertSafeArrayToByteBuffer(
  [in]  LPSAFEARRAY  pbyArray,
  [out] LPBYTEBUFFER *ppbyBuff
);
```



## Parameters

<dl> <dt>

*pbyArray* \[in\]
</dt> <dd>

Pointer to the SAFEARRAY to be converted.

</dd> <dt>

*ppbyBuff* \[out\]
</dt> <dd>

Pointer to the **IStream** object to be returned.

</dd> </dl>

## Return value

The method returns one of the following possible values:



| Return code                                                                                   | Description                                                                                      |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Memory allocated successfully.<br/>                                                        |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | There is something wrong with one or more of the parameters passed into the function.<br/> |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | A parameter of pointer type was incorrect.<br/>                                            |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Not enough free memory to satisfy request.<br/>                                            |



 

## Remarks

Memory allocated is moveable. Use the **IStream::Release** method to free the memory.

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
</dt> </dl>

 

 
