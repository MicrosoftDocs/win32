---
Description: 'Allows the callback object to specify a default sorting parameter. Used by IShellFolderViewCB::MessageSFVCB.'
title: 'SFVM\_GETSORTDEFAULTS message'
---

# SFVM\_GETSORTDEFAULTS message

Allows the callback object to specify a default sorting parameter. Used by [**IShellFolderViewCB::MessageSFVCB**](ishellfolderviewcb-messagesfvcb.md).


```C++
SFVM_GETSORTDEFAULTS 

    wParam = (WPARAM)(int*) iDirection;

    lParam = (LPARAM)(int*) iColumn;

            
```



## Parameters

<dl> <dt>

*iDirection* \[out\]
</dt> <dd>

The default sorting direction. Set this parameter to a positive value to sort in ascending order. Set this parameter to zero or a negative value to sort in descending order.

</dd> <dt>

*iColumn* \[out\]
</dt> <dd>

The column used for the sort. This will be passed to the [**IShellFolder::CompareIDs**](ishellfolder-compareids.md) in the lower 16 bits of its *lParam* value.

</dd> </dl>

## Remarks

> [!Note]  
> : **SFVM\_GETSORTDEFAULTS** is not recognized by the system folder view object.

 

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 




