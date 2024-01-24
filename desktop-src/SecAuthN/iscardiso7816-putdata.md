---
description: The PutData method constructs an application protocol data unit (APDU) command that stores a single primitive data object or the set of data objects contained in a constructed data object, depending on the file selected.
ms.assetid: 6bad45fb-b202-4eb0-b2f4-fe0a6af64330
title: ISCardISO7816::PutData method (Scardssp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCardISO7816.PutData
api_type: 
- COM
api_location: 
- Scardssp.dll
---

# ISCardISO7816::PutData method

\[The **PutData** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **PutData** method constructs an [*application protocol data unit*](../secgloss/a-gly.md) (APDU) command that stores a single primitive data object or the set of data objects contained in a constructed data object, depending on the file selected.

How the objects are stored (writing once and/or updating and/or appending) depends on the definition or the nature of the data objects.

## Syntax


```C++
HRESULT PutData(
  [in]      BYTE         byP1,
  [in]      BYTE         byP2,
  [in]      LPBYTEBUFFER pData,
  [in, out] LPSCARDCMD   *ppCmd
);
```



## Parameters

<dl> <dt>

*byP1* \[in\]
</dt> <dd>

Coding of P1-P2.



| Value                                                                                  | Meaning                                          |
|----------------------------------------------------------------------------------------|--------------------------------------------------|
| <dl> <dt>0000 - 003F</dt> </dl> | RFU<br/>                                   |
| <dl> <dt>0040 - 00FF</dt> </dl> | BER-TLV tag (1 byte) in P2<br/>            |
| <dl> <dt>0100 - 01FF</dt> </dl> | Application data (proprietary coding)<br/> |
| <dl> <dt>0200 - 02FF</dt> </dl> | SIMPLE-TLV tag in P2<br/>                  |
| <dl> <dt>0300 - 03FF</dt> </dl> | RFU<br/>                                   |
| <dl> <dt>0400 - 04FF</dt> </dl> | BER-TLV tag (2 bytes) in P1-P2<br/>        |



 

</dd> <dt>

*byP2* \[in\]
</dt> <dd>

Coding of P1-P2.



| Value                                                                                  | Meaning                                          |
|----------------------------------------------------------------------------------------|--------------------------------------------------|
| <dl> <dt>0000 - 003F</dt> </dl> | RFU<br/>                                   |
| <dl> <dt>0040 - 00FF</dt> </dl> | BER-TLV tag (1 byte) in P2<br/>            |
| <dl> <dt>0100 - 01FF</dt> </dl> | Application data (proprietary coding)<br/> |
| <dl> <dt>0200 - 02FF</dt> </dl> | SIMPLE-TLV tag in P2<br/>                  |
| <dl> <dt>0300 - 03FF</dt> </dl> | RFU<br/>                                   |
| <dl> <dt>0400 - 04FF</dt> </dl> | BER-TLV tag (2 bytes) in P1-P2<br/>        |



 

</dd> <dt>

*pData* \[in\]
</dt> <dd>

Pointer to a byte buffer that contains the parameters and data to be written.

</dd> <dt>

*ppCmd* \[in, out\]
</dt> <dd>

On input, a pointer to an [**ISCardCmd**](iscardcmd.md) interface object or **NULL**.

On return, it is filled with the APDU command constructed by this operation. If *ppCmd* was set to **NULL**, a [*smart card*](../secgloss/s-gly.md) [**ISCardCmd**](iscardcmd.md) object is internally created and returned using the *ppCmd* pointer.

</dd> </dl>

## Return value

The method returns one of the following possible values.



| Return code                                                                                   | Description                                  |
|-----------------------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Operation completed successfully.<br/> |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Invalid parameter.<br/>                |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | A bad pointer was passed in.<br/>      |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Out of memory.<br/>                    |



 

## Remarks

The command can be performed only if the security status satisfies the security conditions defined by the application within the [*context*](../secgloss/c-gly.md) for the function.

<dl> <dt>

<span id="Store_Application_Data"></span><span id="store_application_data"></span><span id="STORE_APPLICATION_DATA"></span>Store Application Data
</dt> <dd>

When the value of P1-P2 lies in the range from 0100 to 01FF, the value of P1-P2 shall be an identifier reserved for card internal tests and for proprietary services meaningful within a given application context.

</dd> <dt>

<span id="Store_Data_Objects"></span><span id="store_data_objects"></span><span id="STORE_DATA_OBJECTS"></span>Store Data Objects
</dt> <dd>

When the value P1-P2 lies in the range from 0040 to 00FF, the value of P2 shall be a BER-TLV tag on a single byte. The value of 00FF is reserved for indicating that the data field carries BER-TLV data objects.

When the value of P1-P2 lies in the range 0200 to 02FF, the value of P2 shall be a SIMPLE-TLV tag. The value 0200 is RFU. The value 02FF is reserved for indicating that the data field carries SIMPLE-TLV data objects.

When the value of P1-P2 lies in the range from 4000 to FFFF, the value of P1-P2 shall be a BER-TLV tag on two bytes. The values 4000 to FFFF are RFU.

When a primitive data object is provided, the data field of the command message shall contain the value of the corresponding primitive data object.

When a constructed data object is provided, the data field of the command message shall contain the value of the constructed data object (that is, data objects including their tag, length, and value).

</dd> </dl>

For a list of all the methods provided by this interface, see [**ISCardISO7816**](iscardiso7816.md).

In addition to the COM error codes listed above, this interface may return a smart card error code if a smart card function was called to complete the request. For more information, see [Smart Card Return Values](authentication-return-values.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| End of client support<br/>    | Windows XP<br/>                                                                   |
| End of server support<br/>    | Windows Server 2003<br/>                                                          |
| Header<br/>                   | <dl> <dt>Scardssp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Scardsrv.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Scardssp.dll</dt> </dl> |
| IID<br/>                      | IID\_ISCardISO7816 is defined as 53B6AA68-3F56-11D0-916B-00AA00C18068<br/>        |



## See also

<dl> <dt>

[**GetData**](iscardiso7816-getdata.md)
</dt> <dt>

[**ISCardISO7816**](iscardiso7816.md)
</dt> </dl>

 

 
