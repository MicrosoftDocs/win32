---
description: Sent by the default context menu implementation during creation, specifying the default menu command and allowing an alternate choice to be made. Used by LPFNDFMCALLBACK.
title: DFM_GETDEFSTATICID message (Shlobj.h)
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 9e4ad96e-7c90-456e-8668-21b347f2915c
api_name: 
 - DFM_GETDEFSTATICID
api_type: 
 - HeaderDef
api_location: 
 - Shlobj.h
topic_type: 
 - APIRef
 - kbSyntax

---

# DFM\_GETDEFSTATICID message

Sent by the default context menu implementation during creation, specifying the default menu command and allowing an alternate choice to be made. Used by [**LPFNDFMCALLBACK**](/windows/win32/api/shlobj_core/nc-shlobj_core-lpfndfmcallback).


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

This message is sent to either the callback function or the callback object depending on how the default context menu object is constructed. There are two APIs for its construction, [**CDefFolderMenu\_Create2**](/windows/desktop/api/shlobj_core/nf-shlobj_core-cdeffoldermenu_create2), [**SHCreateDefaultContextMenu**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shcreatedefaultcontextmenu).

[**DFM\_INVOKECOMMANDEX**](dfm-invokecommandex.md) is an extended version of this message and provides more information to the callback. Use **DFM\_INVOKECOMMANDEX** if the additional information provided by that interface is needed in your implementation.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 
