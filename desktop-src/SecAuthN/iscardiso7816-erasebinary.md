---
description: Constructs an application protocol data unit (APDU) command that sequentially sets part of the content of an elementary file to its logical erased state, starting from a given offset.
ms.assetid: 89e2371e-e27d-475b-9427-bbf6d614c473
title: ISCardISO7816::EraseBinary method (Scardssp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCardISO7816.EraseBinary
api_type: 
- COM
api_location: 
- Scardssp.dll
---

# ISCardISO7816::EraseBinary method

\[The **EraseBinary** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **EraseBinary** method constructs an [*application protocol data unit*](../secgloss/a-gly.md) (APDU) command that sequentially sets part of the content of an elementary file to its logical erased state, starting from a given offset.

## Syntax


```C++
HRESULT EraseBinary(
  [in]      BYTE         byP1,
  [in]      BYTE         byP2,
  [in]      LPBYTEBUFFER pData,
  [in, out] LPSCARDCMD   *ppCmd
);
```



## Parameters

<dl> <dt>

*byP1* \[in\]
</dt> <dd>

RFU position.

If b8=1 in P1, then b7 and b6 of P1 are set to zero (RFU bits), b5 to b1 of P1 are a short EF identifier and P2 is the offset of the first byte to be erased (in data units) from the beginning of the file.

If b8=0 in P1, then P1 \|\| P2 is the offset of the first byte to be erased (in data units) from the beginning of the file.

If the data field is present, it codes the offset of the first data unit not to be erased. This offset shall be higher than the one coded in P1-P2. When the data field is empty, the command erases up to the end of the file.

</dd> <dt>

*byP2* \[in\]
</dt> <dd>

RFU position.

If b8=1 in P1, then b7 and b6 of P1 are set to zero (RFU bits), b5 to b1 of P1 are a short EF identifier and P2 is the offset of the first byte to be erased (in data units) from the beginning of the file.

If b8=0 in P1, then P1 \|\| P2 is the offset of the first byte to be erased (in data units) from the beginning of the file.

If the data field is present, it codes the offset of the first data unit not to be erased. This offset shall be higher than the one coded in P1-P2. When the data field is empty, the command erases up to the end of the file.

</dd> <dt>

*pData* \[in\]
</dt> <dd>

A pointer to the data that specifies the erase range. This parameter may be **NULL**.

</dd> <dt>

*ppCmd* \[in, out\]
</dt> <dd>

On input, a pointer to an [**ISCardCmd**](iscardcmd.md) interface object or **NULL**.

On return, it is filled with the APDU command constructed by this operation. If *ppCmd* was set to **NULL**, a [*smart card*](../secgloss/s-gly.md) [**ISCardCmd**](iscardcmd.md) object is internally created and returned by using the *ppCmd* pointer.

</dd> </dl>

## Return value

The method returns one of the following possible values.



| Return code                                                                                   | Description                                          |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | The operation completed successfully.<br/>     |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | A parameter that is not valid was passed.<br/> |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | A bad pointer was passed in.<br/>              |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Out of memory.<br/>                            |



 

## Remarks

The encapsulated command can only be performed if the security status of the [*smart card*](../secgloss/s-gly.md) satisfies the security attributes of the elementary file being processed.

When the command contains a valid short elementary identifier, it sets the file as current elementary file.

Elementary files without a transparent structure cannot be erased. The encapsulated command aborts if applied to an elementary file without a transparent structure.

For a list of all the methods provided by this interface, see [**ISCardISO7816**](iscardiso7816.md).

In addition to the COM error codes listed above, this interface may return a smart card error code if a smart card function was called to complete the request. For more information, see [Smart Card Return Values](authentication-return-values.md).

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
</dt> <dt>

[**ReadBinary**](iscardiso7816-readbinary.md)
</dt> <dt>

[**UpdateBinary**](iscardiso7816-updatebinary.md)
</dt> <dt>

[**WriteBinary**](iscardiso7816-writebinary.md)
</dt> </dl>

 

 
