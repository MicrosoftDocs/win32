---
Description: 'Notifies the IShellView when one of its objects is placed on the Clipboard as a result of a menu command. Used by SHShellFolderView\_Message.'
title: 'SFVM\_SETCLIPBOARD message'
---

# SFVM\_SETCLIPBOARD message

Notifies the [**IShellView**](ishellview.md) when one of its objects is placed on the Clipboard as a result of a menu command. Used by [**SHShellFolderView\_Message**](shshellfolderview-message.md).


```C++
SFVM_SETCLIPBOARD 

    lParam = (DWORD) dwEffect;

            
```



## Parameters

<dl> <dt>

*dwEffect* \[in\]
</dt> <dd>

Use (WPARAM)-2 if the item is being cut to the Clipboard or (WPARAM)-3 if the item is being copied to the Clipboard.

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



 

 




