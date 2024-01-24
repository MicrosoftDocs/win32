---
description: Retrieves the current resource manager context handle. This method returns (\*pContext) == NULL if no context has been established.
ms.assetid: c031f53d-4670-4d48-934c-a1550f21c23a
title: ISCard::get_Context method (Scardmgr.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCard.get_Context
api_type: 
- COM
api_location: 
- Scardssp.dll
---

# ISCard::get\_Context method

\[The **get\_Context** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **get\_Context** method retrieves the current [*resource manager context*](../secgloss/r-gly.md) handle. This method returns (\**pContext*) == **NULL** if no context has been established.

## Syntax


```C++
HRESULT get_Context(
  [out] HSCARDCONTEXT *pContext
);
```



## Parameters

<dl> <dt>

*pContext* \[out\]
</dt> <dd>

Pointer to the context handle on return.

</dd> </dl>

## Return value

The method returns one of the following possible values.



| Return code                                                                                  | Description                                        |
|----------------------------------------------------------------------------------------------|----------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Operation completed successfully.<br/>       |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | The *pContext* parameter is not valid.<br/>  |
| <dl> <dt>**E\_POINTER**</dt> </dl>    | A bad pointer was passed in *pContext*.<br/> |



 

## Remarks

The resource manager context is set by calling the [*smart card*](../secgloss/s-gly.md) function [**SCardEstablishContext**](/windows/desktop/api/Winscard/nf-winscard-scardestablishcontext).

In addition to the COM error codes listed above, this interface may return a smart card error code if a smart card function was called to complete the request. For more information, see [Smart Card Return Values](authentication-return-values.md).

## Examples

The following example shows retrieving the current [*resource manager context*](../secgloss/r-gly.md) handle.


```C++
HSCARDCONTEXT  hCtx;
HRESULT        hr;

// Retrieve the smart card context.
hr = pISCard->get_Context(&hCtx);
if (FAILED(hr))
{
   printf("Failed get_Context\n");
   // Take other error handling action as needed.
}
// Use smart card context as needed.
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

[**get\_CardHandle**](iscard-get-cardhandle.md)
</dt> <dt>

[**get\_Protocol**](iscard-get-protocol.md)
</dt> <dt>

[**get\_Status**](iscard-get-status.md)
</dt> <dt>

[**ISCard**](iscard.md)
</dt> <dt>

[**SCardEstablishContext**](/windows/desktop/api/Winscard/nf-winscard-scardestablishcontext)
</dt> </dl>

 

 
