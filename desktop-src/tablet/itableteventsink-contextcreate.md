---
description: Occurs when a new tablet context is created.
ms.assetid: 64e1f778-90c1-417d-a80b-37aeecffd411
title: ITabletEventSink::ContextCreate method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ITabletEventSink.ContextCreate
api_type: 
- COM
api_location: 
- wisptis.exe
- wisptis.exe.dll
---

# ITabletEventSink::ContextCreate method

Occurs when a new tablet context is created.

## Syntax


```C++
HRESULT ContextCreate(
  [in] TABLET_CONTEXT_ID tcid
);
```



## Parameters

<dl> <dt>

*tcid* \[in\]
</dt> <dd>

The identifier of the tablet context being created.

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

 

 




