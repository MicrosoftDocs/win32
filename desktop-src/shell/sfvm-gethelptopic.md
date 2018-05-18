---
Description: 'Allows the callback object to specify an HTML Help file and a topic within it. Used by IShellFolderViewCB::MessageSFVCB.'
title: 'SFVM\_GETHELPTOPIC message'
---

# SFVM\_GETHELPTOPIC message

Allows the callback object to specify an HTML Help file and a topic within it. Used by [**IShellFolderViewCB::MessageSFVCB**](ishellfolderviewcb-messagesfvcb.md).


```C++
SFVM_GETHELPTOPIC 

    lParam = (LPARAM)(SFVM_HELPTOPIC_DATA*) phtd;

            
```



## Parameters

<dl> <dt>

*phtd* \[out\]
</dt> <dd>

The address of a [**SFVM\_HELPTOPIC\_DATA**](sfvm-helptopic-data-str.md) structure that specifies the HTML Help file and topic.

</dd> </dl>

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 




