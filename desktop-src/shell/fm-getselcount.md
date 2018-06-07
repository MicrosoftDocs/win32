---
Description: Sent by a File Manager extension to retrieve a count of the selected files in the active File Manager window (either the directory window or the Search Results window).
title: FM\_GETSELCOUNT message
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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



|                                     |                                                                                    |
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

 

 




