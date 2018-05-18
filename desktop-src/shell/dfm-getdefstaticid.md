---
Description: 'Sent by the default context menu implementation during creation, specifying the default menu command and allowing an alternate choice to be made. Used by LPFNDFMCALLBACK.'
title: 'DFM\_GETDEFSTATICID message'
---

# DFM\_GETDEFSTATICID message

Sent by the default context menu implementation during creation, specifying the default menu command and allowing an alternate choice to be made. Used by [**LPFNDFMCALLBACK**](lpfndfmcallback.md).


```C++
DFM_GETDEFSTATICID
    lParam = (LPARAM)(int*) defaultID;          
            
```



## Parameters

<dl> <dt>

*defaultID* \[in, out\]
</dt> <dd>

A pointer to the ID of the selected menu command. The following flag is recognized.

<dt>

<span id="DFM_CMD_PROPERTIES"></span><span id="dfm_cmd_properties"></span>

<span id="DFM_CMD_PROPERTIES"></span><span id="dfm_cmd_properties"></span>**DFM\_CMD\_PROPERTIES**


</dt> <dd>

Show the **Properties** UI for the item the menu was invoked on.

</dd> </dl> </dd> </dl>

## Remarks

To override the default command choice, your handler should, upon receipt of this message, set the value pointed to by *defaultID* to the ID of the replacement command and return S\_OK. Return a failure code otherwise.

This message is sent to either the callback function or the callback object depending on how the default context menu object is constructed. There are two APIs for its construction, [**CDefFolderMenu\_Create2**](cdeffoldermenu-create2.md), [**SHCreateDefaultContextMenu**](shcreatedefaultcontextmenu.md).

[**DFM\_INVOKECOMMANDEX**](dfm-invokecommandex.md) is an extended version of this message and provides more information to the callback. Use **DFM\_INVOKECOMMANDEX** if the additional information provided by that interface is needed in your implementation.

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 




