---
description: Creates a typical C/C++ byte array.
ms.assetid: 915e8cca-2a0f-409e-a6df-54fa73bdc305
title: ISCardTypeConv::CreateByteArray method (Scarddat.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCardTypeConv.CreateByteArray
api_type: 
- COM
api_location: 
- Scardssp.dll
---

# ISCardTypeConv::CreateByteArray method

\[The **CreateByteArray** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **CreateByteArray** method creates a typical C/C++ byte array.

## Syntax


```C++
HRESULT CreateByteArray(
  [in]  DWORD  dwAllocSize,
  [out] LPBYTE *ppbyArray
);
```



## Parameters

<dl> <dt>

*dwAllocSize* \[in\]
</dt> <dd>

Size (in bytes) of the memory to be allocated for the array.

</dd> <dt>

*ppbyArray* \[out\]
</dt> <dd>

Pointer to the byte array to be returned.

</dd> </dl>

## Return value

The method returns one of the following possible values:



| Return code                                                                                   | Description                                                                                      |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Memory allocated successfully.<br/>                                                        |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | There is something wrong with one or more of the parameters passed into the function.<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Not enough free memory to satisfy request.<br/>                                            |



 

## Remarks

To create a universal buffer of bytes mapped into an **IStream** ([**IByteBuffer**](ibytebuffer.md)) object, call [**CreateByteBuffer**](iscardtypeconv-createbytebuffer.md).

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

[**CreateByteBuffer**](iscardtypeconv-createbytebuffer.md)
</dt> <dt>

[**CreateSafeArray**](iscardtypeconv-createsafearray.md)
</dt> </dl>

 

 
