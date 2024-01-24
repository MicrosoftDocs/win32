---
description: The AppendRecord method constructs an application protocol data unit (APDU) command that either appends a record to the end of a linear-structured elementary file (EF) or writes record number 1 in a cyclic-structured elementary file.
ms.assetid: 4dd88661-41c4-4238-88c9-279b39afb206
title: ISCardISO7816::AppendRecord method (Scardssp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCardISO7816.AppendRecord
api_type: 
- COM
api_location: 
- Scardssp.dll
---

# ISCardISO7816::AppendRecord method

\[The **AppendRecord** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **AppendRecord** method constructs an [*application protocol data unit*](../secgloss/a-gly.md) (APDU) command that either appends a record to the end of a linear-structured elementary file (EF) or writes record number 1 in a cyclic-structured elementary file.

## Syntax


```C++
HRESULT AppendRecord(
  [in]      BYTE         byRefCtrl,
  [in]      LPBYTEBUFFER pData,
  [in, out] LPSCARDCMD   *ppCmd
);
```



## Parameters

<dl> <dt>

*byRefCtrl* \[in\]
</dt> <dd>

Identifies the elementary file to be appended.



| Value                                                                                                                                                                                | Meaning                           |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| <span id="Current_EF"></span><span id="current_ef"></span><span id="CURRENT_EF"></span><dl> <dt>**Current EF**</dt> </dl>     | Bit position: 00000000<br/> |
| <span id="Short_EF_ID"></span><span id="short_ef_id"></span><span id="SHORT_EF_ID"></span><dl> <dt>**Short EF ID**</dt> </dl> | Bit position: xxxxx000<br/> |
| <span id="Reserved"></span><span id="reserved"></span><span id="RESERVED"></span><dl> <dt>**Reserved**</dt> </dl>             | Bit position: xxxxxxxx<br/> |



 

</dd> <dt>

*pData* \[in\]
</dt> <dd>

A pointer to the data to be appended to the file.



| Value                                                                                                                                                | Meaning                 |
|------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| <span id="Tn"></span><span id="tn"></span><span id="TN"></span><dl> <dt>**Tn**</dt> </dl>     | 1 byte<br/>       |
| <span id="Ln_"></span><span id="ln_"></span><span id="LN_"></span><dl> <dt>**Ln** </dt> </dl> | 1 or 3 bytes<br/> |
| <span id="data"></span><span id="DATA"></span><dl> <dt>**data**</dt> </dl>                    | Ln bytes<br/>     |



 

</dd> <dt>

*ppCmd* \[in, out\]
</dt> <dd>

On input, a pointer to an [**ISCardCmd**](iscardcmd.md) interface object or **NULL**.

On return, it is filled with the APDU command constructed by this operation. If *ppCmd* was set to **NULL**, a [*smart card*](../secgloss/s-gly.md) [**ISCardCmd**](iscardcmd.md) object is internally created and returned by using the *ppCmd* pointer.

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

The encapsulated command can only be performed if the security status of the [*smart card*](../secgloss/s-gly.md) satisfies the security attributes of the elementary file read.

If another elementary file is selected at the time of issuing this command, it may be processed without identification of the currently selected file.

Elementary files without a record structure cannot be read. The encapsulated command aborts if applied to an elementary file without a record structure.

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

[**ReadRecord**](iscardiso7816-readrecord.md)
</dt> <dt>

[**UpdateRecord**](iscardiso7816-updaterecord.md)
</dt> <dt>

[**WriteRecord**](iscardiso7816-writerecord.md)
</dt> </dl>

 

 
