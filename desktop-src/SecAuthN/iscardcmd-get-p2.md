---
description: Retrieves the second parameter (P2) byte from the application protocol data unit (APDU).
ms.assetid: c719786f-0f50-472e-a92e-a64c333fc255
title: ISCardCmd::get_P2 method (Scarddat.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCardCmd.get_P2
api_type: 
- COM
api_location: 
- Scardssp.dll
---

# ISCardCmd::get\_P2 method

\[The **get\_P2** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **get\_P2** method retrieves the second parameter (P2) byte from the [*application protocol data unit*](../secgloss/a-gly.md) (APDU).

## Syntax


```C++
HRESULT get_P2(
  [out] BYTE *pbyP2
);
```



## Parameters

<dl> <dt>

*pbyP2* \[out\]
</dt> <dd>

Pointer to the byte that is the P2 from the APDU on return.

</dd> </dl>

## Return value

The method returns one of the following possible values.



| Return code                                                                                   | Description                                     |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Operation completed successfully.<br/>    |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | The *pbyP2* parameter is not valid.<br/>  |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | A bad pointer was passed in *pbyP2*.<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Out of memory.<br/>                       |



 

## Remarks

To set the P2 parameter to a new value, call [**put\_P2**](iscardcmd-put-p2.md).

To get the P1 or P3 parameters, call [**get\_P1**](iscardcmd-get-p1.md) and [**get\_P3**](iscardcmd-get-p3.md) respectively.

For a list of all the methods provided by this interface, see [**ISCardCmd**](iscardcmd.md).

In addition to the COM error codes listed above, this interface may return a [*smart card*](../secgloss/s-gly.md) error code if a smart card function was called to complete the request. For more information, see [Smart Card Return Values](authentication-return-values.md).

## Examples

The following example shows how to retrieve the second parameter (P2) byte from the [*application protocol data unit*](../secgloss/a-gly.md) (APDU). The example assumes that pISCardCmd is a valid pointer to an instance of the [**ISCardCmd**](iscardcmd.md) interface.


```C++
BYTE  byP2;
HRESULT  hr;

// Retrieve the P2 byte.
hr = pISCardCmd->get_P2(&byP2);
if (FAILED(hr))
{
  printf("Failed get_P2\n");
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

[**get\_P1**](iscardcmd-get-p1.md)
</dt> <dt>

[**get\_P3**](iscardcmd-get-p3.md)
</dt> <dt>

[**ISCardCmd**](iscardcmd.md)
</dt> <dt>

[**put\_P2**](iscardcmd-put-p2.md)
</dt> </dl>

 

 
