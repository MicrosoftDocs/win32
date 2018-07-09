---
Description: Sent by a File Manager extension to retrieve drive information from the active File Manager window.
title: FM\_GETDRIVEINFO message
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FM_GETDRIVEINFO
api_type: 
- HeaderDef
api_location: 
- Wfext.h
---

# FM\_GETDRIVEINFO message

Sent by a File Manager extension to retrieve drive information from the active File Manager window.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lpfmsgdi* 
</dt> <dd>

The address of an [**FMS\_GETDRIVEINFO**](fms-getdriveinfo.md) structure that receives drive information.

</dd> </dl>

## Return value

Returns nonzero.

## Remarks

If 0xFFFFFFFF is returned in the **dwTotalSpace** or **dwFreeSpace** member of the [**FMS\_GETDRIVEINFO**](fms-getdriveinfo.md) structure, the extension library must compute the value or values.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wfext.h</dt> </dl> |



## See also

<dl> <dt>

[**FMExtensionProc**](fmextensionproc.md)
</dt> </dl>

 

 




