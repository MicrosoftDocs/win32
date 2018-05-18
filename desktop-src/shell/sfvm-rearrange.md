---
Description: 'Notifies the IShellView to rearrange its items. Used by SHShellFolderView\_Message.'
title: 'SFVM\_REARRANGE message'
---

# SFVM\_REARRANGE message

Notifies the [**IShellView**](ishellview.md) to rearrange its items. Used by [**SHShellFolderView\_Message**](shshellfolderview-message.md).


```C++
SFVM_REARRANGE 

    lParam = (LPARAM) lparam;

            
```



## Parameters

<dl> <dt>

*lParam* \[in\]
</dt> <dd>

Passed to [**IShellFolder::CompareIDs**](ishellfolder-compareids.md). See [**IShellFolder::CompareIDs**](ishellfolder-compareids.md) for more information on this parameter.

</dd> </dl>

## Return value

No return value.

## Remarks

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 




