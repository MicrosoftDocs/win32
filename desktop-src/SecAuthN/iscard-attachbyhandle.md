---
description: Attaches the ISCard object to an open and configured smart card handle.
ms.assetid: e735d33d-a337-404e-a760-4cf8f19d172a
title: ISCard::AttachByHandle method (Scardmgr.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCard.AttachByHandle
api_type: 
- COM
api_location: 
- Scardssp.dll
---

# ISCard::AttachByHandle method

\[The **AttachByHandle** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **AttachByHandle** method attaches the [**ISCard**](iscard.md) object to an open and configured [*smart card*](../secgloss/s-gly.md) handle.

## Syntax


```C++
HRESULT AttachByHandle(
  [in] HSCARD hCard
);
```



## Parameters

<dl> <dt>

*hCard* \[in\]
</dt> <dd>

A handle to an open connection to a smart card.

</dd> </dl>

## Return value

The method returns one of the following possible values.



| Return code                                                                                  | Description                                    |
|----------------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Operation completed successfully.<br/>   |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | The *hCard* parameter is not valid.<br/> |



 

## Remarks

In addition to the COM error codes listed above, this interface may return a smart card error code if a smart card function was called to complete the request. For more information, see [Smart Card Return Values](authentication-return-values.md).

When you have finished using the handle, release the attachment by calling the [**ISCard::Detach**](iscard-detach.md) method.

## Examples

The following example shows attaching to a smart card handle.


```C++
HRESULT  hr;

// hSC is of type HSCARD and has been previously assigned.
// Attach SCard to the smart card using the value in hSC.
hr = pISCard->AttachByHandle(hSC);
if (FAILED(hr))
{
   printf("Failed AttachByHandle\n");
   // Take other error handling action as needed.
}
// Proceed using attached reader.
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

[**AttachByReader**](iscard-attachbyreader.md)
</dt> <dt>

[**Detach**](iscard-detach.md)
</dt> <dt>

[**get\_CardHandle**](iscard-get-cardhandle.md)
</dt> <dt>

[**ISCard**](iscard.md)
</dt> <dt>

[**ReAttach**](iscard-reattach.md)
</dt> </dl>

 

 
