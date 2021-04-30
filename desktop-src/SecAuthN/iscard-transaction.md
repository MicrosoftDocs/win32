---
description: Executes a write and read operation on the smart card command (application protocol data unit) object.
ms.assetid: 4dc8ed56-97e0-4c05-a70a-ea2ffd976d47
title: ISCard::Transaction method (Scardmgr.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCard.Transaction
api_type: 
- COM
api_location: 
- Scardssp.dll
---

# ISCard::Transaction method

\[The **Transaction** method is available for use in the operating systems specified in the Requirements section. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **Transaction** method executes a write and read operation on the [*smart card*](../secgloss/s-gly.md) command ([*application protocol data unit*](../secgloss/a-gly.md)) object. The reply string from the smart card for the command string defined in the card that was sent to the smart card will be accessible after this function returns.

## Syntax


```C++
HRESULT Transaction(
  [in, out] LPSCARDCMD *ppCmd
);
```



## Parameters

<dl> <dt>

*ppCmd* \[in, out\]
</dt> <dd>

A pointer to the smart card command object.

</dd> </dl>

## Return value

The method returns one of the following possible values.



| Return code                                                                                   | Description                                              |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | The operation completed successfully.<br/>         |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | The *ppCmd* parameter is not valid.<br/>           |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | A bad pointer was passed in *ppCmd*.<br/>          |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Memory to satisfy the request is unavailable.<br/> |



 

## Remarks

In addition to the COM error codes listed above, this interface may return a smart card error code if a smart card function was called to complete the request. For more information, see [Smart Card Return Values](authentication-return-values.md).

## Examples

The following example shows executing a write and read operation on the smart card command object.


```C++
HRESULT    hr;

// pISCard is a pointer to an instance of ISCard.
// pISCardCmd is a pointer to an instance of ISCardCmd,
// and ISCardCmd::BuildCmd has already been called.
hr = pISCard->Transaction(&pISCardCmd);
if (FAILED(hr))
{
    printf("Failed ISCard::Transaction\n");
    // Take other error handling action as needed.
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

[**Detach**](iscard-detach.md)
</dt> <dt>

[**get\_Atr**](iscard-get-atr.md)
</dt> <dt>

[**get\_CardHandle**](iscard-get-cardhandle.md)
</dt> <dt>

[**get\_Context**](iscard-get-context.md)
</dt> <dt>

[**get\_Protocol**](iscard-get-protocol.md)
</dt> <dt>

[**get\_Status**](iscard-get-status.md)
</dt> <dt>

[**ISCard**](iscard.md)
</dt> <dt>

[**LockSCard**](iscard-lockscard.md)
</dt> <dt>

[**ReAttach**](iscard-reattach.md)
</dt> <dt>

[**UnlockSCard**](iscard-unlockscard.md)
</dt> </dl>

 

 
