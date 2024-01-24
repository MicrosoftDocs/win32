---
description: Determines the size, in bytes, of the IStream COM interface.
ms.assetid: 8c2f081d-cc41-409e-a868-bcf834e1f128
title: ISCardTypeConv::SizeOfIStream method (Scarddat.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCardTypeConv.SizeOfIStream
api_type: 
- COM
api_location: 
- Scardssp.dll
---

# ISCardTypeConv::SizeOfIStream method

\[The **SizeOfIStream** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **SizeOfIStream** method determines the size, in bytes, of the **IStream** COM interface.

## Syntax


```C++
HRESULT SizeOfIStream(
  [in]  LPSTREAM       pStrm,
  [out] ULARGE_INTEGER *puliSize
);
```



## Parameters

<dl> <dt>

*pStrm* \[in\]
</dt> <dd>

A pointer to the **IStream** COM interface.

</dd> <dt>

*puliSize* \[out\]
</dt> <dd>

A pointer to the unsigned large integer that can hold the entire 64-bit sizeof value of the **IStream** COM interface.

</dd> </dl>

## Return value

The method returns one of the following possible values.



| Return code                                                                                  | Description                                                                                             |
|----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | The function succeeded and *\*puliSize* is the size, in bytes, of the IStream COM interface.<br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>       | Unspecified failure occurred.<br/>                                                                |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | The *puliSize* parameter is incorrect.<br/>                                                       |
| <dl> <dt>**E\_POINTER**</dt> </dl>    | The *pStrm* parameter is incorrect.<br/>                                                          |
| <dl> <dt>**E\_UNEXPECTED**</dt> </dl> | Unexpected error occurred.<br/>                                                                   |



 

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

 

 
