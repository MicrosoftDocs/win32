---
description: Occurs when a new stylus is added to the system.
ms.assetid: bd0f0d2a-c0d9-48fc-bc90-f63f038639f3
title: ITabletEventSink::CursorNew method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ITabletEventSink.CursorNew
api_type: 
- COM
api_location: 
- wisptis.exe
- wisptis.exe.dll
---

# ITabletEventSink::CursorNew method

Occurs when a new stylus is added to the system.

## Syntax


```C++
HRESULT CursorNew(
  [in] TABLET_CONTEXT_ID tcid,
       t                 cid
);
```



## Parameters

<dl> <dt>

*tcid* \[in\]
</dt> <dd>

The identifier of the tablet context where the new stylus was added.

</dd> <dt>

*cid* 
</dt> <dd>

The identifier of the new stylus object.

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

 

 




