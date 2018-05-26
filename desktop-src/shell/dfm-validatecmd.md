---
Description: Sent to verify the existence of a menu command.
title: DFM\_VALIDATECMD message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DFM\_VALIDATECMD message

Sent to verify the existence of a menu command.


```C++
DFM_INVOKECOMMAND

    wParam = (WPARAM)(WPARAM) idCmd;            

    lParam = (LPARAM)(LPARAM) lParam = 0;

            
```



## Parameters

<dl> <dt>

*idCmd* 
</dt> <dd>The menu command identifier offset.</dd> <dt>

*lParam* 
</dt> <dd>Not used. Must be zero.</dd> </dl>

## Return value

Returns S\_OK if the command exists, or S\_FALSE otherwise.

## Remarks

This message is sent to either the callback function or the callback object depending on how the default context menu object is constructed. There are two APIs for its construction, [**CDefFolderMenu\_Create2**](/windows/win32/shlobj_core/nf-shlobj_core-cdeffoldermenu_create2?branch=master), [**SHCreateDefaultContextMenu**](/windows/win32/shlobj_core/nf-shlobj_core-shcreatedefaultcontextmenu?branch=master).

[**DFM\_INVOKECOMMANDEX**](dfm-invokecommandex.md) is an extended version of this message and provides more information to the callback. Use **DFM\_INVOKECOMMANDEX** if the additional information provided by that interface is needed in your implementation.

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 




