---
description: Retrieves the handle for a connected smart card. This method returns (\*pHandle) == NULL if not connected.
ms.assetid: f03f8f25-b2e4-4fae-b7d2-bb0f1a7cd987
title: ISCard::get_CardHandle method (Scardmgr.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCard.get_CardHandle
api_type: 
- COM
api_location: 
- Scardssp.dll
---

# ISCard::get\_CardHandle method

\[The **get\_CardHandle** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **get\_CardHandle** method retrieves the handle for a connected [*smart card*](../secgloss/s-gly.md). This method returns (\*pHandle) == **NULL** if not connected.

## Syntax


```C++
HRESULT get_CardHandle(
  [out] HSCARD *pHandle
);
```



## Parameters

<dl> <dt>

*pHandle* \[out\]
</dt> <dd>

Pointer to the card handle on return.

</dd> </dl>

## Return value

The method returns one of the following possible values.



| Return code                                                                                  | Description                                       |
|----------------------------------------------------------------------------------------------|---------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Operation completed successfully.<br/>      |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | The *pHandle* parameter is not valid.<br/>  |
| <dl> <dt>**E\_POINTER**</dt> </dl>    | A bad pointer was passed in *pHandle*.<br/> |



 

## Remarks

In addition to the COM error codes listed above, this interface may return a smart card error code if a smart card function was called to complete the request. For more information, see [Smart Card Return Values](authentication-return-values.md).

## Examples

The following example shows retrieving the smart card handle.


```C++
HSCARD   hSC;
HRESULT  hr;

// Retrieve the card handle.
hr = pISCard->get_CardHandle(&hSC);
if (FAILED(hr))
{
   printf("Failed get_CardHandle\n");
   // Take other error handling action as needed.
}
// Use card handle as needed.
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

[**get\_Atr**](iscard-get-atr.md)
</dt> <dt>

[**get\_Context**](iscard-get-context.md)
</dt> <dt>

[**get\_Protocol**](iscard-get-protocol.md)
</dt> <dt>

[**get\_Status**](iscard-get-status.md)
</dt> <dt>

[**ISCard**](iscard.md)
</dt> </dl>

 

 
