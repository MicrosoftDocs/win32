---
description: Sent by a File Manager extension to retrieve information about a selected file from the active File Manager window (either the directory window or the Search Results window). The selected file can have a long file name.
title: FM_GETFILESELLFN message (Wfext.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FM_GETFILESELLFN
api_type: 
- HeaderDef
api_location: 
- Wfext.h
ms.assetid: 461fd171-d47f-41d6-953e-8e497e023ab1
api_name: 
 - FM_GETFILESELLFN
api_type: 
 - HeaderDef
api_location: 
 - Wfext.h
topic_type: 
 - APIRef
 - kbSyntax

---

# FM\_GETFILESELLFN message

Sent by a File Manager extension to retrieve information about a selected file from the active File Manager window (either the directory window or the Search Results window). The selected file can have a long file name.

## Parameters

<dl> <dt>

*index* 
</dt> <dd>

The zero-based index of the selected file to retrieve.

</dd> <dt>

*lpfmsgfs* 
</dt> <dd>

The address of an [**FMS\_GETFILESEL**](fms-getfilesel.md) structure that receives information about the selection.

</dd> </dl>

## Return value

Returns the zero-based index of the selected file that was retrieved.

## Remarks

Only extensions that support long file names (for example, network-aware extensions) should use this message.

An extension can use the [**FM\_GETSELCOUNTLFN**](fm-getselcountlfn.md) message to retrieve the count of selected files.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wfext.h</dt> </dl> |



## See also

<dl> <dt>

[**FMExtensionProc**](fmextensionproc.md)
</dt> <dt>

[**FM\_GETFILESEL**](fm-getfilesel.md)
</dt> <dt>

[**FM\_GETSELCOUNT**](fm-getselcount.md)
</dt> </dl>

 

 




