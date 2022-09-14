---
description: The SetDefaultClassId method assigns a standard class identifier byte that will be used in all operations when constructing an ISO 7816-4 command application protocol data unit (APDU). By default, the standard class identifier byte is 0x00.
ms.assetid: 5a53d5f1-7986-4c4c-9512-f592cd398d1c
title: ISCardISO7816::SetDefaultClassId method (Scardssp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCardISO7816.SetDefaultClassId
api_type: 
- COM
api_location: 
- Scardssp.dll
---

# ISCardISO7816::SetDefaultClassId method

\[The **SetDefaultClassId** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **SetDefaultClassId** method assigns a standard class identifier byte that will be used in all operations when constructing an ISO 7816-4 command [*application protocol data unit*](../secgloss/a-gly.md) (APDU). By default, the standard class identifier byte is 0x00.

## Syntax


```C++
HRESULT SetDefaultClassId(
  [in] BYTE byClass
);
```



## Parameters

<dl> <dt>

*byClass* \[in\]
</dt> <dd>

Class ID byte.

</dd> </dl>

## Return value

The possible return values are the following:



| Return code                                                                          | Description                                  |
|--------------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | Operation completed successfully.<br/> |



 

For a list of all the methods provided by the [**ISCardISO7816**](iscardiso7816.md) interface, see **ISCardISO7816**.

In addition to the COM error codes listed above, this interface may return a [*smart card*](../secgloss/s-gly.md) error code if a smart card function was called to complete the request. For information about smart card error codes, see [Smart Card Return Values](authentication-return-values.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| End of client support<br/>    | Windows XP<br/>                                                                   |
| End of server support<br/>    | Windows Server 2003<br/>                                                          |
| Header<br/>                   | <dl> <dt>Scardssp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Scardsrv.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Scardssp.dll</dt> </dl> |
| IID<br/>                      | IID\_ISCardISO7816 is defined as 53B6AA68-3F56-11D0-916B-00AA00C18068<br/>        |



## See also

<dl> <dt>

[**ISCardISO7816**](iscardiso7816.md)
</dt> </dl>

 

 
