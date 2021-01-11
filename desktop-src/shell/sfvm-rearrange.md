---
description: Notifies the IShellView to rearrange its items. Used by SHShellFolderView\_Message.
title: SFVM_REARRANGE message (Shlobj.h)
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: d745bafc-f2f5-40a1-b7e8-e16e4cf0153d
api_name: 
 - SFVM_REARRANGE
api_type: 
 - HeaderDef
api_location: 
 - Shlobj.h
topic_type: 
 - APIRef
 - kbSyntax

---

# SFVM\_REARRANGE message

Notifies the [**IShellView**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellview) to rearrange its items. Used by [**SHShellFolderView\_Message**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shshellfolderview_message).


```C++
SFVM_REARRANGE 

    lParam = (LPARAM) lparam;

            
```



## Parameters

<dl> <dt>

*lParam* \[in\]
</dt> <dd>

Passed to [**IShellFolder::CompareIDs**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-compareids). See [**IShellFolder::CompareIDs**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-compareids) for more information on this parameter.

</dd> </dl>

## Return value

No return value.

## Remarks

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 




