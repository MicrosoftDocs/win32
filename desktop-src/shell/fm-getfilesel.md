---
Description: 'Sent by a File Manager extension to retrieve information about a selected file from the active File Manager window (either the directory window or the Search Results window).'
title: 'FM\_GETFILESEL message'
---

# FM\_GETFILESEL message

Sent by a File Manager extension to retrieve information about a selected file from the active File Manager window (either the directory window or the Search Results window).

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

An extension can use the [**FM\_GETSELCOUNT**](fm-getselcount.md) message to retrieve the count of selected files.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wfext.h</dt> </dl> |



## See also

<dl> <dt>

[**FMExtensionProc**](fmextensionproc.md)
</dt> <dt>

[**FM\_GETFILESELLFN**](fm-getfilesellfn.md)
</dt> <dt>

[**FM\_GETSELCOUNTLFN**](fm-getselcountlfn.md)
</dt> </dl>

 

 




