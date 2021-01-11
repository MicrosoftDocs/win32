---
description: Constructs an APDU command that initiates one of the listed operations.
ms.assetid: 2ce313b9-ccd7-4be0-a91f-d0747e35fab8
title: ISCardISO7816::WriteRecord method (Scardssp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCardISO7816.WriteRecord
api_type: 
- COM
api_location: 
- Scardssp.dll
---

# ISCardISO7816::WriteRecord method

\[The **WriteRecord** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **WriteRecord** method constructs an [*application protocol data unit*](../secgloss/a-gly.md) (APDU) command that initiates one of the following operations:

-   The write once of a record.
-   The logical **OR** of the data bytes of a record already present in the card with the data bytes of the record given in the command APDU.
-   The logical AND of the data bytes of a record already present in the card with the data bytes of the record given in the command APDU.

When no indication is given in the data coding byte, the logical OR behavior applies.

> [!Note]  
> When using current record addressing, the command sets the record pointer on the successfully updated record.

 

## Syntax


```C++
HRESULT WriteRecord(
  [in]      BYTE         byRecordId,
  [in]      BYTE         byRefCtrl,
  [in]      LPBYTEBUFFER pData,
  [in, out] LPSCARDCMD   *ppCmd
);
```



## Parameters

<dl> <dt>

*byRecordId* \[in\]
</dt> <dd>

Record identification. This is the P1 value:

P1 = '00' designates the current record.

P1 != '00' is the number of the specified record.

</dd> <dt>

*byRefCtrl* \[in\]
</dt> <dd>

Coding of the reference control P2.



| Value                                                                                                                                                                                                | Meaning                                                             |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| <span id="Current_EF"></span><span id="current_ef"></span><span id="CURRENT_EF"></span><dl> <dt>**Current EF**</dt> </dl>                     | Bit position: 00000---<br/> Currently selected EF.<br/> |
| <span id="Short_EF_ID"></span><span id="short_ef_id"></span><span id="SHORT_EF_ID"></span><dl> <dt>**Short EF ID**</dt> </dl>                 | Bit position: xxxxx---<br/> Short EF identifier.<br/>   |
| <span id="First_Record"></span><span id="first_record"></span><span id="FIRST_RECORD"></span><dl> <dt>**First Record**</dt> </dl>             | Bit position: -----000<br/>                                   |
| <span id="Last_Record"></span><span id="last_record"></span><span id="LAST_RECORD"></span><dl> <dt>**Last Record**</dt> </dl>                 | Bit position: -----001<br/>                                   |
| <span id="Next_Record"></span><span id="next_record"></span><span id="NEXT_RECORD"></span><dl> <dt>**Next Record**</dt> </dl>                 | Bit position: -----010<br/>                                   |
| <span id="Previous_Record"></span><span id="previous_record"></span><span id="PREVIOUS_RECORD"></span><dl> <dt>**Previous Record**</dt> </dl> | Bit position: -----011<br/>                                   |
| <span id="Record___in_P1"></span><span id="record___in_p1"></span><span id="RECORD___IN_P1"></span><dl> <dt>**Record \# in P1**</dt> </dl>    | Bit position: -----100<br/>                                   |



 

</dd> <dt>

*pData* \[in\]
</dt> <dd>

Pointer to the record to be written.

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

When the command contains a valid short elementary identifier, it sets the file as current elementary file. If another elementary file is currently selected at the time of issuing this command, this command may be processed without identification of the currently selected file.

If the encapsulated command applies to a linear-fixed or cyclic-structured elementary file, it will abort if the record length is different from the length of the existing record. If it applies to a linear-variable structured elementary file, it may be carried out when the record length is different from the length of the existing record.

If P2=xxxxx011 and the elementary file is cyclic file, this command has the same behavior a command constructed using [**AppendRecord**](iscardiso7816-appendrecord.md).

Elementary files without a record structure cannot be written to. The constructed command aborts if applied to an elementary file without a record structure.

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

[**AppendRecord**](iscardiso7816-appendrecord.md)
</dt> <dt>

[**ISCardISO7816**](iscardiso7816.md)
</dt> <dt>

[**ReadRecord**](iscardiso7816-readrecord.md)
</dt> <dt>

[**UpdateRecord**](iscardiso7816-updaterecord.md)
</dt> </dl>

 

 
