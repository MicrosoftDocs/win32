---
Description: Sent by the default context menu implementation to assign a name to a menu command.
title: DFM_MAPCOMMANDNAME message
ms.topic: article
ms.date: 05/31/2018
---

# DFM\_MAPCOMMANDNAME message

Sent by the default context menu implementation to assign a name to a menu command.


```C++
DFM_MAPCOMMANDNAME

    lParam = (LPARAM)(int*) defaultID;

    wparam = (WPARAM)(LPTSTR) pszCommandName;

            
```



## Parameters

<dl> <dt>

*defaultID* \[in, out\]
</dt> <dd>

A pointer to the ID of the selected menu command.

</dd> <dt>

*pszCommandName* \[in\]
</dt> <dd>

A pointer to a Unicode string containing the name of the command.

</dd> </dl>

## Remarks

This message is sent to either the callback function or the callback object depending on how the default context menu object is implemented. There are two APIs for its implementation, [**CDefFolderMenu\_Create2**](/windows/desktop/api/shlobj_core/nf-shlobj_core-cdeffoldermenu_create2), [**SHCreateDefaultContextMenu**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shcreatedefaultcontextmenu).

[**DFM\_INVOKECOMMANDEX**](dfm-invokecommandex.md) is an extended version of this message and provides more information to the callback. Use **DFM\_INVOKECOMMANDEX** if the additional information provided by that interface is needed in your implementation.

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 




