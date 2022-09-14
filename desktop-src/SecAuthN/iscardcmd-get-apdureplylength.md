---
description: Determines the length (in bytes) of the application protocol data unit (APDU).
ms.assetid: 25011db1-a037-4764-b700-8ad2200419da
title: ISCardCmd::get_ApduReplyLength method (Scarddat.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCardCmd.get_ApduReplyLength
api_type: 
- COM
api_location: 
- Scardssp.dll
---

# ISCardCmd::get\_ApduReplyLength method

\[The **get\_ApduReplyLength** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **get\_ApduReplyLength** method determines the length (in bytes) of the [*application protocol data unit*](../secgloss/a-gly.md) (APDU).

## Syntax


```C++
HRESULT get_ApduReplyLength(
  [out] LONG *plSize
);
```



## Parameters

<dl> <dt>

*plSize* \[out\]
</dt> <dd>

Pointer to the size of the reply APDU message.

</dd> </dl>

## Return value

The method returns one of the following possible values.



| Return code                                                                                   | Description                                      |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Operation completed successfully.<br/>     |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | The *plSize* parameter is not valid.<br/>  |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | A bad pointer was passed in *plSize*.<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Out of memory.<br/>                        |



 

## Remarks

To get an existing reply APDU, call [**get\_ApduReply**](iscardcmd-get-apdureply.md).

For a list of all the methods provided by this interface, see [**ISCardCmd**](iscardcmd.md).

In addition to the COM error codes listed above, this interface may return a smart card error code if a smart card function was called to complete the request. For more information, see [Smart Card Return Values](authentication-return-values.md).

## Examples

The following example shows how to retrieve the length of the [*reply APDU*](../secgloss/r-gly.md). The example assumes that pISCardCmd is a valid pointer to an instance of the [**ISCardCmd**](iscardcmd.md) interface.


```C++
LONG    lLen;
HRESULT hr;

// Retrieve the APDU reply length.
hr = pISCardCmd->get_ApduReplyLength(&lLen);
if (FAILED(hr))
{
    printf("Failed get_ApduReplyLength\n");
    // Take other error handling action.
}
else
    printf("Length returned is %d\n", lLen);
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

[**get\_ApduReply**](iscardcmd-get-apdureply.md)
</dt> <dt>

[**ISCardCmd**](iscardcmd.md)
</dt> <dt>

[**put\_ApduReply**](iscardcmd-put-apdureply.md)
</dt> </dl>

 

 
