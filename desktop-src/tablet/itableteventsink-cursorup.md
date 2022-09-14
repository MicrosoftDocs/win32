---
description: Occurs when the user has raised the stylus from the tablet digitizer surface.
ms.assetid: 34dc7e6b-101a-4edd-8c3c-9aafb85cf58b
title: ITabletEventSink::CursorUp method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ITabletEventSink.CursorUp
api_type: 
- COM
api_location: 
- wisptis.exe
- wisptis.exe.dll
---

# ITabletEventSink::CursorUp method

Occurs when the user has raised the stylus from the tablet digitizer surface.

## Syntax


```C++
HRESULT CursorUp(
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

The stylus data indicating the location where the stylus was lifted from the tablet.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

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

 

 




