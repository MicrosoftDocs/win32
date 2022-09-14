---
description: Occurs when the stylus tip contacts the digitizing tablet surface.
ms.assetid: 7f4a441d-00d2-4120-8a8d-d3496cdc7e58
title: ITabletEventSink::CursorDown method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ITabletEventSink.CursorDown
api_type: 
- COM
api_location: 
- wisptis.exe
- wisptis.exe.dll
---

# ITabletEventSink::CursorDown method

Occurs when the stylus tip contacts the digitizing tablet surface.

## Syntax


```C++
HRESULT CursorDown(
  [in] TABLET_CONTEXT_ID tcid,
  [in] CURSOR_ID         cid,
  [in] ULONG             nSerialNumber,
  [in] ULONG             cbPkt,
  [in] BYTE              *pbPkt
);
```



## Parameters

<dl> <dt>

*tcid* \[in\]
</dt> <dd>

The identifier of the tablet.

</dd> <dt>

*cid* \[in\]
</dt> <dd>

The identifier of the stylus.

</dd> <dt>

*nSerialNumber* \[in\]
</dt> <dd>

The serial number of the stylus.

</dd> <dt>

*cbPkt* \[in\]
</dt> <dd>

The number of bytes in a stylus data packet.

</dd> <dt>

*pbPkt* \[in\]
</dt> <dd>

The stylus data indicating the location where the stylus touched the tablet.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                            | Description                               |
|----------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>   | Success.<br/>                       |
| <dl> <dt>**E\_FAIL**</dt> </dl> | An unspecified error occurred.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | None supported<br/>                                                              |
| Library<br/>                  | <dl> <dt>Wisptis.exe</dt> </dl> |



## See also

<dl> <dt>

[**ITabletEventSink Interface**](itableteventsink.md)
</dt> </dl>

 

 




