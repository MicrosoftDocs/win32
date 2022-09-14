---
description: Constructs an application protocol data unit (APDU) command that initiates the comparison (in the card) of the verification data sent from the interface device with the reference data stored in the card (for example, password).
ms.assetid: a0837c39-d741-42eb-88b2-87c4e043e64f
title: ISCardISO7816::Verify method (Scardssp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCardISO7816.Verify
api_type: 
- COM
api_location: 
- Scardssp.dll
---

# ISCardISO7816::Verify method

\[The **Verify** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **Verify** method constructs an [*application protocol data unit*](../secgloss/a-gly.md) (APDU) command that initiates the comparison (in the card) of the verification data sent from the interface device with the reference data stored in the card (for example, password).

## Syntax


```C++
HRESULT Verify(
  [in]      BYTE         byRefCtrl,
  [in]      LPBYTEBUFFER pData,
  [in, out] LPSCARDCMD   *ppCmd
);
```



## Parameters

<dl> <dt>

*byRefCtrl* \[in\]
</dt> <dd>

A quantifier of the reference data. Coding of the reference control P2 follows.

When the body is empty, the command may be used either to retrieve the number 'X' of further allowed retries (SW1-SW2=63CX) or to check whether the verification is not required (SW1-SW2=9000).



| Value                                                                                                                                                                                    | Meaning                                                                                                                                                                                           |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="No_Info"></span><span id="no_info"></span><span id="NO_INFO"></span><dl> <dt>**No Info**</dt> </dl>                     | Bit position: 00000000<br/> P2=00 is reserved to indicate that no particular qualifier is used in those cards where the verify command references the secret data unambiguously.<br/> |
| <span id="Global_Ref"></span><span id="global_ref"></span><span id="GLOBAL_REF"></span><dl> <dt>**Global Ref**</dt> </dl>         | Bit position: 0-------<br/> An example of Global Ref would be a password.<br/>                                                                                                        |
| <span id="Specific_Ref"></span><span id="specific_ref"></span><span id="SPECIFIC_REF"></span><dl> <dt>**Specific Ref**</dt> </dl> | Bit position: 1-------<br/> An example of Specific Ref is DF specific password.<br/>                                                                                                  |
| <span id="RFU"></span><span id="rfu"></span><dl> <dt>**RFU**</dt> </dl>                                                           | Bit position: -xx-----<br/>                                                                                                                                                                 |
| <span id="Ref_Data__"></span><span id="ref_data__"></span><span id="REF_DATA__"></span><dl> <dt>**Ref Data \#**</dt> </dl>        | Bit position: ---xxxxx<br/> The reference data number may be, for example, a password number or a short EF identifier.<br/>                                                           |



 

</dd> <dt>

*pData* \[in\]
</dt> <dd>

A pointer to the verification data. This parameter can be **NULL**. The default value is **NULL**.

</dd> <dt>

*ppCmd* \[in, out\]
</dt> <dd>

On input, a pointer to an [**ISCardCmd**](iscardcmd.md) interface object or **NULL**.

On return, it is filled with the APDU command constructed by this operation. If *ppCmd* was set to **NULL**, a [*smart card*](../secgloss/s-gly.md) [**ISCardCmd**](iscardcmd.md) object is internally created and returned by using the *ppCmd* pointer.

</dd> </dl>

## Return value

The method returns one of the following possible values.



| Return code                                                                                   | Description                                        |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | The operation completed successfully.<br/>   |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | A parameter that is not valid was used.<br/> |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | A bad pointer was passed in.<br/>            |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Out of memory.<br/>                          |



 

## Remarks

The security status may be modified as a result of a comparison. Unsuccessful comparisons may be recorded in the card (for example, to limit the number of further attempts of the use of the reference data).

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
</dt> </dl>

 

 
