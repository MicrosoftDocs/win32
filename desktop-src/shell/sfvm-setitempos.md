---
Description: 'Sets the position of an item in the Shell view. Used by SHShellFolderView\_Message.'
title: 'SFVM\_SETITEMPOS message'
---

# SFVM\_SETITEMPOS message

Sets the position of an item in the Shell view. Used by [**SHShellFolderView\_Message**](shshellfolderview-message.md).


```C++

                SFVM_SETITEMPOS 

    lParam = (LPSFV_SETITEMPOS)&amp;sip;

            
```



## Parameters

<dl> <dt>

*sip* \[in\]
</dt> <dd>

A pointer to an [**SFV\_SETITEMPOS**](sfv-setitempos.md) structure.

</dd> </dl>

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP1 \[desktop apps only\]<br/>                                |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 




