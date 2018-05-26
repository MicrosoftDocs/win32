---
Description: Occurs when the stylus leaves the physical detection range (proximity) of the tablet.
ms.assetid: ded01278-126d-415d-9a7b-1e6fe3650a37
title: ITabletEventSinkCursorOutOfRange method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ITabletEventSink::CursorOutOfRange method

Occurs when the stylus leaves the physical detection range (proximity) of the tablet.

## Syntax


```C++
HRESULT CursorOutOfRange(
  [in] TABLET_CONTEXT_ID tcid,
       t                 cid
);
```



## Parameters

<dl> <dt>

*tcid* \[in\]
</dt> <dd>

The identifier of the tablet.

</dd> <dt>

*cid* 
</dt> <dd>

The identifier of the stylus.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                            | Description                               |
|----------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>   | Success.<br/>                       |
| <dl> <dt>**E\_FAIL**</dt> </dl> | An unspecified error occurred.<br/> |



 

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | None supported<br/>                                                              |
| Library<br/>                  | <dl> <dt>Wisptis.exe</dt> </dl> |



## See also

<dl> <dt>

[**ITabletEventSink Interface**](itableteventsink.md)
</dt> </dl>

 

 




