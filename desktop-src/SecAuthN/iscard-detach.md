---
description: Closes the open connection to the smart card.
ms.assetid: 7d768945-8d5d-4d29-b5bc-1b2ac5b0e114
title: ISCard::Detach method (Scardmgr.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCard.Detach
api_type: 
- COM
api_location: 
- Scardssp.dll
---

# ISCard::Detach method

\[The **Detach** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **Detach** method closes the open connection to the [*smart card*](../secgloss/s-gly.md).

## Syntax


```C++
HRESULT Detach(
  [in] SCARD_DISPOSITIONS Disposition
);
```



## Parameters

<dl> <dt>

*Disposition* \[in\]
</dt> <dd>

Indicates what should be done with the card in the connected [*reader*](../secgloss/r-gly.md).



| Value                                                                                                                                      | Meaning                                                                                                            |
|--------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| <span id="LEAVE"></span><span id="leave"></span><dl> <dt>**LEAVE**</dt> </dl>       | Leaves the smart card in the current [*state*](../secgloss/s-gly.md).<br/> |
| <span id="RESET"></span><span id="reset"></span><dl> <dt>**RESET**</dt> </dl>       | Resets the smart card to some known state.<br/>                                                              |
| <span id="UNPOWER"></span><span id="unpower"></span><dl> <dt>**UNPOWER**</dt> </dl> | Removes power from the smart card.<br/>                                                                      |
| <span id="EJECT"></span><span id="eject"></span><dl> <dt>**EJECT**</dt> </dl>       | Ejects the smart card if the reader has eject capabilities.<br/>                                             |



 

</dd> </dl>

## Return value

The method returns one of the following possible values.



| Return code                                                                                  | Description                                  |
|----------------------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Operation completed successfully.<br/> |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | *Disposition* is not valid.<br/>       |



 

## Remarks

In addition to the COM error codes listed above, this interface may return a smart card error code if a smart card function was called to complete the request. For more information, see [Smart Card Return Values](authentication-return-values.md).

## Examples

The following example shows closing the connection to the smart card.


```C++
HRESULT    hr;

// Detach the smart card.
hr = pISCard->Detach(LEAVE);
if (FAILED(hr))
{
   printf("Failed Detach\n");
   // Take error handling action as needed.
}
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| End of client support<br/>    | Windows XP<br/>                                                                   |
| End of server support<br/>    | Windows Server 2003<br/>                                                          |
| Header<br/>                   | <dl> <dt>Scardmgr.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Scardmgr.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Scardssp.dll</dt> </dl> |
| IID<br/>                      | IID\_ISCard is defined as 1461AAC3-6810-11D0-918F-00AA00C18068<br/>               |



## See also

<dl> <dt>

[**AttachByHandle**](iscard-attachbyhandle.md)
</dt> <dt>

[**AttachByReader**](iscard-attachbyreader.md)
</dt> <dt>

[**ISCard**](iscard.md)
</dt> <dt>

[**ReAttach**](iscard-reattach.md)
</dt> </dl>

 

 
