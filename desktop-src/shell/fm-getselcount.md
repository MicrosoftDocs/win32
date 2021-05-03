---
description: Sent by a File Manager extension to retrieve a count of the selected files in the active File Manager window (either the directory window or the Search Results window).
title: FM_GETSELCOUNT message (Wfext.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FM_GETSELCOUNT
api_type: 
- HeaderDef
api_location: 
- Wfext.h
ms.assetid: 0d43bf37-863c-45cc-94ea-5b2aedba5353

---

# FM\_GETSELCOUNT message

Sent by a File Manager extension to retrieve a count of the selected files in the active File Manager window (either the directory window or the Search Results window).

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the number of selected files.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wfext.h</dt> </dl> |



## See also

<dl> <dt>

[**FM\_GETFILESEL**](fm-getfilesel.md)
</dt> <dt>

[**FM\_GETFILESELLFN**](fm-getfilesellfn.md)
</dt> <dt>

[**FM\_GETSELCOUNTLFN**](fm-getselcountlfn.md)
</dt> </dl>

 

 




