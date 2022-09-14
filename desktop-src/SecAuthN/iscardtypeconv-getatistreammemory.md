---
description: Acquires a byte pointer to the HGLOBAL memory block that is managed by the IStream COM interface.
ms.assetid: ea25eb98-b841-4f5e-b428-3d9cb8176142
title: ISCardTypeConv::GetAtIStreamMemory method (Scarddat.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCardTypeConv.GetAtIStreamMemory
api_type: 
- COM
api_location: 
- Scardssp.dll
---

# ISCardTypeConv::GetAtIStreamMemory method

\[The **GetAtIStreamMemory** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **GetAtIStreamMemory** method acquires a byte pointer to the HGLOBAL memory block that is managed by the **IStream** COM interface.

This is a way to get at the memory under the **IStream** without having to get the sizeof value for the memory block in bytes and read the bytes into a temporary byte array using the **IStream** interface.

## Syntax


```C++
HRESULT GetAtIStreamMemory(
  [in]  LPSTREAM    pStrm,
  [out] LPBYTEARRAY *ppMem
);
```



## Parameters

<dl> <dt>

*pStrm* \[in\]
</dt> <dd>

A pointer to the **IStream** COM interface that manages the HGLOBAL memory block.

</dd> <dt>

*ppMem* \[out\]
</dt> <dd>

A pointer to the first byte of the HGLOBAL memory block if successful; else, **NULL** if operation fails.

</dd> </dl>

## Return value

The method returns one of the following possible values.



| Return code                                                                                   | Description                                                                                      |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Memory allocated successfully.<br/>                                                        |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | There is something wrong with one or more of the parameters passed into the function.<br/> |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | A parameter of pointer type was incorrect.<br/>                                            |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Not enough free memory to satisfy request.<br/>                                            |



 

## Remarks

The **IStream** reference count will be incremented for each *ppMem* pointer acquired.

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

 

 
