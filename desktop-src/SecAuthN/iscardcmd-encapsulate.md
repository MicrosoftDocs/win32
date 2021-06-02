---
description: The Encapsulate method encapsulates the given command application protocol data unit (APDU) into another command APDU for transmission to a smart card.
ms.assetid: dfffad09-046b-46cb-b6fd-286a4bbf1066
title: ISCardCmd::Encapsulate method (Scarddat.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCardCmd.Encapsulate
api_type: 
- COM
api_location: 
- Scardssp.dll
---

# ISCardCmd::Encapsulate method

\[The **Encapsulate** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **Encapsulate** method encapsulates the given command [*application protocol data unit*](../secgloss/a-gly.md) (APDU) into another command APDU for transmission to a [*smart card*](../secgloss/s-gly.md).

## Syntax


```C++
HRESULT Encapsulate(
  [in] LPBYTEBUFFER  pApdu,
  [in] ISO_APDU_TYPE ApduType
);
```



## Parameters

<dl> <dt>

*pApdu* \[in\]
</dt> <dd>

Pointer to the APDU to be encapsulated.

</dd> <dt>

*ApduType* \[in\]
</dt> <dd>

ISO 7816-4 case for [*T=0*](../secgloss/t-gly.md) transmissions.

<dl><span id="ISO_CASE_1"></span><span id="iso_case_1"></span><dt>

**ISO\_CASE\_1**
</dt><span id="ISO_CASE_2"></span><span id="iso_case_2"></span><dt>

**ISO\_CASE\_2**
</dt><span id="ISO_CASE_3"></span><span id="iso_case_3"></span><dt>

**ISO\_CASE\_3**
</dt><span id="ISO_CASE_4"></span><span id="iso_case_4"></span><dt>

**ISO\_CASE\_4**
</dt> </dl> </dd> </dl>

## Return value

The method returns one of the following possible values.



| Return code                                                                                   | Description                                     |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Operation completed successfully.<br/>    |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Invalid parameter.<br/>                   |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | A bad pointer was passed in *pApdu*.<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Out of memory.<br/>                       |



 

## Remarks

To build a command APDU, call [**BuildCmd**](iscardcmd-buildcmd.md).

For a list of all the methods provided by this interface, see [**ISCardCmd**](iscardcmd.md).

In addition to the COM error codes listed above, this interface may return a smart card error code if a smart card function was called to complete the request. For more information, see [Smart Card Return Values](authentication-return-values.md).

## Examples

The following example shows how to encapsulate a command APDU. The example assumes that pIByteApdu is a valid pointer to an instance of the [**IByteBuffer**](ibytebuffer.md) interface.


```C++
HRESULT    hr;

// pIByteApdu is a pointer to an instance of IByteBuffer.
// Encapsulate the APDU.
hr = pISCardCmd->Encapsulate(pIByteApdu, ISO_CASE_1);
if (FAILED(hr)) 
{
    printf("Failed Encapsulate.\n");
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
| Header<br/>                   | <dl> <dt>Scarddat.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Scarddat.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Scardssp.dll</dt> </dl> |
| IID<br/>                      | IID\_ISCardCmd is defined as D5778AE3-43DE-11D0-9171-00AA00C18068<br/>            |



## See also

<dl> <dt>

[**BuildCmd**](iscardcmd-buildcmd.md)
</dt> <dt>

[**ISCardCmd**](iscardcmd.md)
</dt> </dl>

 

 
