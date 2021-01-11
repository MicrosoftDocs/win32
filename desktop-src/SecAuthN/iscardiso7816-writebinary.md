---
description: The WriteBinary method constructs an application protocol data unit (APDU) command that writes binary values into an elementary file.
ms.assetid: e38273d5-4eb0-4c0b-829a-c78e511a38bc
title: ISCardISO7816::WriteBinary method (Scardssp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCardISO7816.WriteBinary
api_type: 
- COM
api_location: 
- Scardssp.dll
---

# ISCardISO7816::WriteBinary method

\[The **WriteBinary** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **WriteBinary** method constructs an [*application protocol data unit*](../secgloss/a-gly.md) (APDU) command that writes binary values into an elementary file.

Depending upon the file attributes, the command performs one of the following operations:

-   The logical OR of the bits already present in the card with the bits given in the command APDU (logical erased state of the bits of the file is 0).
-   The logical AND of the bits already present in the card with the bits given in the command APDU (logical erased state of the bits of the file is 1).
-   The one-time write in the card of the bits given in the command APDU.

When no indication is given in the data coding byte, the logical OR behavior applies.

## Syntax


```C++
HRESULT WriteBinary(
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

Offset to the write location from the beginning of the binary file (EF). If b8=1 in P1, then b7 and b6 of P1 are set to zero (RFU bits), b5 to b1 of P1 are a short EF identifier and P2 is the offset of the first byte to be written in data units from the beginning of the file. If b8=0 in P1, then P1\|\|P2 is the offset of the first byte to be written in data units from the beginning of the file.

</dd> <dt>

*byP2* \[in\]
</dt> <dd>

Offset to the write location from the beginning of the binary file (EF). If b8=1 in P1, then b7 and b6 of P1 are set to zero (RFU bits), b5 to b1 of P1 are a short EF identifier and P2 is the offset of the first byte to be written in data units from the beginning of the file. If b8=0 in P1, then P1\|\|P2 is the offset of the first byte to be written in data units from the beginning of the file.

</dd> <dt>

*pData* \[in\]
</dt> <dd>

Pointer to the string of data units to be written.

</dd> <dt>

*ppCmd* \[in, out\]
</dt> <dd>

On input, a pointer to an [**ISCardCmd**](iscardcmd.md) interface object or **NULL**.

On return, it is filled with the APDU command constructed by this operation. If *ppCmd* was set to **NULL**, a [*smart card*](../secgloss/s-gly.md) [**ISCardCmd**](iscardcmd.md) object is internally created and returned via the *ppCmd* pointer.

</dd> </dl>

## Return value

The method returns one of the following possible values.



| Return code                                                                                   | Description                                  |
|-----------------------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Operation completed successfully.<br/> |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Invalid parameter.<br/>                |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | A bad pointer was passed in.<br/>      |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Out of memory.<br/>                    |



 

## Remarks

The encapsulated command can only be performed if the security status of the [*smart card*](../secgloss/s-gly.md) satisfies the security attributes of the elementary file being processed.

When the command contains a valid short elementary identifier, it sets the file as current elementary file.

When a write binary operation has been applied to a data unit of a one-time write EF, any further write operation referring to this data unit will be aborted if the content of the data unit or the logical erased state indicator (if any) attached to this data unit is different from the logical erased state.

Elementary files without a transparent structure cannot be written to. The encapsulated command aborts if applied to an elementary file without a transparent structure.

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

[**EraseBinary**](iscardiso7816-erasebinary.md)
</dt> <dt>

[**ISCardISO7816**](iscardiso7816.md)
</dt> <dt>

[**ReadBinary**](iscardiso7816-readbinary.md)
</dt> <dt>

[**UpdateBinary**](iscardiso7816-updatebinary.md)
</dt> </dl>

 

 
