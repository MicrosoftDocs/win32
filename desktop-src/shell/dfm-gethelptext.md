---
Description: Allows the callback object to specify a help text string.
title: DFM\_GETHELPTEXT message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DFM\_GETHELPTEXT message

Allows the callback object to specify a help text string.


```C++
DFM_GETHELPTEXT 

    wParam = (WPARAM)(int) idCmd,cchMax;

    lParam = (LPARAM)(LPTSTR) pszText;

            
```



## Parameters

<dl> <dt>

*idCmd\_cchMax* \[in\]
</dt> <dd>

The low-order word of this parameter holds the command ID. The high-order word holds the number of characters in the *pszText* buffer.

</dd> <dt>

*pszText* \[out\]
</dt> <dd>

A null-terminated ANSI string containing the help text.

</dd> </dl>

## Remarks

This message is sent to either the callback function or the callback object depending on how the default context menu object is constructed. There are two APIs for its construction, [**CDefFolderMenu\_Create2**](/windows/win32/shlobj_core/nf-shlobj_core-cdeffoldermenu_create2?branch=master), [**SHCreateDefaultContextMenu**](/windows/win32/shlobj_core/nf-shlobj_core-shcreatedefaultcontextmenu?branch=master).

[**DFM\_INVOKECOMMANDEX**](dfm-invokecommandex.md) is an extended version of this message and provides more information to the callback. Use **DFM\_INVOKECOMMANDEX** if the additional information provided by that interface is needed in your implementation.

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **DFM\_GETHELPTEXT** (ANSI)<br/>                                              |



 

 




