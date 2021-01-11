---
description: Retrieves the data field from the application protocol data unit (APDU), placing it in a byte buffer object.
ms.assetid: fbffeeeb-56e5-4484-b294-8b6f59c919eb
title: ISCardCmd::get_Data method (Scarddat.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCardCmd.get_Data
api_type: 
- COM
api_location: 
- Scardssp.dll
---

# ISCardCmd::get\_Data method

\[The **get\_Data** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **get\_Data** method retrieves the data field from the [*application protocol data unit*](../secgloss/a-gly.md) (APDU), placing it in a byte buffer object.

## Syntax


```C++
HRESULT get_Data(
  [out] LPBYTEBUFFER *ppData
);
```



## Parameters

<dl> <dt>

*ppData* \[out\]
</dt> <dd>

Pointer to the byte buffer object (**IStream**) that holds the APDU data field on return.

</dd> </dl>

## Return value

The method returns one of the following possible values.



| Return code                                                                                   | Description                                      |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Operation completed successfully.<br/>     |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | The *ppData* parameter is not valid.<br/>  |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | A bad pointer was passed in *ppData*.<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Out of memory.<br/>                        |



 

## Remarks

To set the data field of the APDU, call [**put\_Data**](iscardcmd-put-data.md).

For a list of all the methods provided by this interface, see [**ISCardCmd**](iscardcmd.md).

In addition to the COM error codes listed above, this interface may return a [*smart card*](../secgloss/s-gly.md) error code if a smart card function was called to complete the request. For more information, see [Smart Card Return Values](authentication-return-values.md).

## Examples

The following example shows how to retrieve the data field of the [*application protocol data unit*](../secgloss/a-gly.md) (APDU). The example assumes that pIByteData is a valid pointer to an instance of the [**IByteBuffer**](ibytebuffer.md) interface, and that pISCardCmd is a valid pointer to an instance of the [**ISCardCmd**](iscardcmd.md) interface.


```C++
HRESULT    hr;

// pIByteData is a pointer to an instance of IByteBuffer.
// Retrieve the data.
hr = pISCardCmd->get_Data(&pIByteData);
if (FAILED(hr)) 
{
    printf("Failed get_Data.\n");
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

[**ISCardCmd**](iscardcmd.md)
</dt> <dt>

[**put\_Data**](iscardcmd-put-data.md)
</dt> </dl>

 

 
