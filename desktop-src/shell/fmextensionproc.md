---
description: Specifies an application-defined callback function called by File Manager to communicate with a File Manager extension.
title: FMExtensionProc callback function (Wfext.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FMExtensionProc
- FMExtensionProcW
api_type: 
- UserDefined
api_location: 
- Wfext.h
ms.assetid: 6e02d655-f7d8-460a-97d2-5b369493e941
api_name: 
 - FMExtensionProc
 - FMExtensionProcW
api_type: 
 - UserDefined
api_location: 
 - Wfext.h
topic_type: 
 - APIRef
 - kbSyntax

---

# FMExtensionProc callback function

Specifies an application-defined callback function called by File Manager to communicate with a File Manager extension.

## Syntax


```C++
LONG CALLBACK FMExtensionProc(
   HWND hwnd,
   WORD wMsg,
   LONG lParam
);
```



## Parameters

<dl> <dt>

*hwnd* 
</dt> <dd>

Type: **HWND**

A window handle to File Manager. An extension uses this handle to specify the parent window for any dialog box or message box it must display, and to send query messages to File Manager.

</dd> <dt>

*wMsg* 
</dt> <dd>

Type: **WORD**

One of the following File Manager messages.

<dt>

<span id="1_through_99"></span><span id="1_THROUGH_99"></span>

<span id="1_through_99"></span><span id="1_THROUGH_99"></span>**1 through 99**


</dt> <dd>

User selected an item from the extension-supplied menu. The value is the identifier of the selected menu item.

</dd> <dt>

<span id="FMEVENT_HELPMENUITEM"></span><span id="fmevent_helpmenuitem"></span>

<span id="FMEVENT_HELPMENUITEM"></span><span id="fmevent_helpmenuitem"></span>**FMEVENT\_HELPMENUITEM**


</dt> <dd>

User pressed F1 while selecting an extension menu or toolbar command item. Indicates that the extension should call **WinHelp** appropriately for the command item.

</dd> <dt>

<span id="FMEVENT_HELPSTRING"></span><span id="fmevent_helpstring"></span>

<span id="FMEVENT_HELPSTRING"></span><span id="fmevent_helpstring"></span>**FMEVENT\_HELPSTRING**


</dt> <dd>

User selected an extension menu or toolbar command item. Indicates that the extension should supply a Help string.

</dd> <dt>

<span id="FMEVENT_INITMENU"></span><span id="fmevent_initmenu"></span>

<span id="FMEVENT_INITMENU"></span><span id="fmevent_initmenu"></span>**FMEVENT\_INITMENU**


</dt> <dd>

User selected the extension's menu. The extension should initialize items in the menu.

</dd> <dt>

<span id="FMEVENT_LOAD"></span><span id="fmevent_load"></span>

<span id="FMEVENT_LOAD"></span><span id="fmevent_load"></span>**FMEVENT\_LOAD**


</dt> <dd>

File Manager is loading the extension DLL and prompts the DLL for information about the menu that the DLL supplies.

</dd> <dt>

<span id="FMEVENT_SELCHANGE"></span><span id="fmevent_selchange"></span>

<span id="FMEVENT_SELCHANGE"></span><span id="fmevent_selchange"></span>**FMEVENT\_SELCHANGE**


</dt> <dd>

Selection in the **File Manager** directory window or **Search Results** window has changed.

</dd> <dt>

<span id="FMEVENT_TOOLBARLOAD"></span><span id="fmevent_toolbarload"></span>

<span id="FMEVENT_TOOLBARLOAD"></span><span id="fmevent_toolbarload"></span>**FMEVENT\_TOOLBARLOAD**


</dt> <dd>

File Manager is creating the toolbar and prompts the extension DLL for information about any buttons the DLL adds to the toolbar.

</dd> <dt>

<span id="FMEVENT_UNLOAD"></span><span id="fmevent_unload"></span>

<span id="FMEVENT_UNLOAD"></span><span id="fmevent_unload"></span>**FMEVENT\_UNLOAD**


</dt> <dd>

File Manager is unloading the extension DLL.

</dd> <dt>

<span id="FMEVENT_USER_REFRESH"></span><span id="fmevent_user_refresh"></span>

<span id="FMEVENT_USER_REFRESH"></span><span id="fmevent_user_refresh"></span>**FMEVENT\_USER\_REFRESH**


</dt> <dd>

User selected the **Refresh** command from the **Window** menu. The extension should update items in the menu, if necessary.

</dd> </dl> </dd> <dt>

*lParam* 
</dt> <dd>

Type: **LONG**

Message-specific value.

</dd> </dl>

## Return value

Type: **LONG**

Returns a value dependent upon the *wMsg* parameter message.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wfext.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **FMExtensionProcW** (Unicode)<br/>                                          |



 

 




