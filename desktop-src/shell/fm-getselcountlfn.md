---
description: Sent by a File Manager extension to retrieve the number of selected files in the active File Manager window (either the directory window or the Search Results window). The count includes files that have long file names.
title: FM_GETSELCOUNTLFN message (Wfext.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FM_GETSELCOUNTLFN
api_type: 
- HeaderDef
api_location: 
- Wfext.h
ms.assetid: d0815afc-5356-48a7-a90d-5f48dae6bee5

---

# FM\_GETSELCOUNTLFN message

Sent by a File Manager extension to retrieve the number of selected files in the active File Manager window (either the directory window or the Search Results window). The count includes files that have long file names.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the number of selected files.

## Remarks

Only extensions that support long file names (for example, network-aware extensions) should use this message.

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

[**FM\_GETSELCOUNT**](fm-getselcount.md)
</dt> </dl>

 

 




