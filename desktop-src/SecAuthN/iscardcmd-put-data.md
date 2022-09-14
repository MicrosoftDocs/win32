---
description: Sets the data field in the application protocol data unit (APDU).
ms.assetid: 4508e00c-2b1d-4be5-b3a7-083b367a2158
title: ISCardCmd::put_Data method (Scarddat.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCardCmd.put_Data
api_type: 
- COM
api_location: 
- Scardssp.dll
---

# ISCardCmd::put\_Data method

\[The **put\_Data** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **put\_Data** method sets the data field in the [*application protocol data unit*](../secgloss/a-gly.md) (APDU).

## Syntax


```C++
HRESULT put_Data(
  [in] LPBYTEBUFFER pData
);
```



## Parameters

<dl> <dt>

*pData* \[in\]
</dt> <dd>

Pointer to the byte buffer object (**IStream**) to be copied into the APDU data field.

</dd> </dl>

## Return value

The method returns one of the following possible values.



| Return code                                                                                   | Description                                     |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Operation completed successfully.<br/>    |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | The *pData* parameter is not valid.<br/>  |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | A bad pointer was passed in *pData*.<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Out of memory.<br/>                       |



 

## Remarks

When you set a new data portion of the message, the length of the data field is calculated and stored in the P3 parameter of the APDU. To retrieve the length of the data field, call [**get\_P3**](iscardcmd-get-p3.md).

To retrieve the data field from the APDU, call [**get\_Data**](iscardcmd-get-data.md).

## Examples

The following example shows how to set the data field in the [*application protocol data unit*](../secgloss/a-gly.md) (APDU). The example assumes that pIByteData is a valid pointer to an instance of the [**IByteBuffer**](ibytebuffer.md) interface, and that pISCardCmd is a valid pointer to an instance of the [**ISCardCmd**](iscardcmd.md) interface.


```C++
HRESULT    hr;

// pIByteData is a pointer to an instance of IByteBuffer.
// Set the data.
hr = pISCardCmd->put_Data(pIByteData);
if (FAILED(hr)) 
{
    printf("Failed put_Data.\n");
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

[**get\_Data**](iscardcmd-get-data.md)
</dt> <dt>

[**get\_P3**](iscardcmd-get-p3.md)
</dt> <dt>

[**ISCardCmd**](iscardcmd.md)
</dt> </dl>

 

 
