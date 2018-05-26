---
Description: Sent by a File Manager extension (or another application) to cause File Manager to reload all extension DLLs listed in the \[AddOns\] section of the Winfile.ini file.
ms.assetid: 5103a986-5f45-4deb-aaae-c6e87cb60051
title: FM\_RELOAD\_EXTENSIONS message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FM\_RELOAD\_EXTENSIONS message

Sent by a File Manager extension (or another application) to cause File Manager to reload all extension DLLs listed in the \[AddOns\] section of the Winfile.ini file.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

Must be zero.

</dd> </dl>

## Return value

No return value.

## Remarks

Other applications can use the [**PostMessage**](winmsg.postmessage) function to send this message to File Manager. To obtain the appropriate File Manager window handle, an application can specify "WFS\_Frame" as the *lpszClassName* parameter in a call to the [**FindWindow**](winmsg.findwindow) function.

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

 

 




