---
Description: Allows the callback to add items to the top of the extended menu.
title: DFM\_MERGECONTEXTMENU\_TOP message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DFM\_MERGECONTEXTMENU\_TOP message

Allows the callback to add items to the top of the extended menu.


```C++
DFM_MERGECONTEXTMENU_TOP

    lParam = (LPARAM)(LPQCMINFO) pqcminfo;

    wParam = (WPARAM)(UINT) uFlags;         

            
```



## Parameters

<dl> <dt>

*pqcminfo* \[in\]
</dt> <dd>

A pointer to a [**QCMINFO**](/windows/win32/shlobj_core/ns-shlobj_core-_qcminfo?branch=master) structure containing the information used in the merge.

</dd> <dt>

*uFlags* \[in\]
</dt> <dd>

Flags specifying how the context menu can be changed. This parameter uses the CMF\_\* values described in [**IContextMenu::QueryContextMenu**](/windows/win32/shobjidl_core/nf-shobjidl_core-icontextmenu-querycontextmenu?branch=master).

</dd> </dl>

## Remarks

If items are added to the extended context menu, they must be supported with routines that respond appropriately when one of those items is invoked using [**DFM\_INVOKECOMMAND**](dfm-invokecommand.md).

This message is sent to either the callback function or the callback object depending on how the default context menu object is implemented. There are two APIs for its implementation, [**CDefFolderMenu\_Create2**](/windows/win32/shlobj_core/nf-shlobj_core-cdeffoldermenu_create2?branch=master), [**SHCreateDefaultContextMenu**](/windows/win32/shlobj_core/nf-shlobj_core-shcreatedefaultcontextmenu?branch=master).

[**DFM\_INVOKECOMMANDEX**](dfm-invokecommandex.md) is an extended version of this message and provides more information to the callback. Use **DFM\_INVOKECOMMANDEX** if the additional information provided by that interface is needed in your implementation.

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 




