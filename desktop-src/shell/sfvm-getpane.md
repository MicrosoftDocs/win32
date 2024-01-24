---
description: SFVM\_GETPANE may be altered or unavailable.
ms.assetid: 9621b921-e97f-4219-953a-7c961a81c379
title: SFVM_GETPANE message (Shlobj.h)
ms.topic: reference
ms.date: 05/31/2018
---

# SFVM\_GETPANE message

\[**SFVM\_GETPANE** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Allows the callback object to provide the status bar pane in which to display the Internet zone information. Used by [**IShellFolderViewCB::MessageSFVCB**](/windows/win32/api/shlobj_core/nf-shlobj_core-ishellfolderviewcb-messagesfvcb).


```C++
SFVM_GETPANE
    wParam = (WPARAM)(int) paneID;
    lParam = (LPARAM)(DWORD*) pane;
            
```



## Parameters

<dl> <dt>

*paneID* \[in\]
</dt> <dd>

ID of the requested pane. This is normally PANE\_ZONE, but can be any one of the following values.

<dt>

<span id="PANE_NONE"></span><span id="pane_none"></span>

<span id="PANE_NONE"></span><span id="pane_none"></span>**PANE\_NONE**


</dt> <dd>

No pane.

</dd> <dt>

<span id="PANE_ZONE"></span><span id="pane_zone"></span>

<span id="PANE_ZONE"></span><span id="pane_zone"></span>**PANE\_ZONE**


</dt> <dd>

The Internet zone pane.

</dd> <dt>

<span id="PANE_OFFLINE"></span><span id="pane_offline"></span>

<span id="PANE_OFFLINE"></span><span id="pane_offline"></span>**PANE\_OFFLINE**


</dt> <dd>

The offline pane.

</dd> <dt>

<span id="PANE_PRINTER"></span><span id="pane_printer"></span>

<span id="PANE_PRINTER"></span><span id="pane_printer"></span>**PANE\_PRINTER**


</dt> <dd>

The print indication pane.

</dd> <dt>

<span id="PANE_SSL"></span><span id="pane_ssl"></span>

<span id="PANE_SSL"></span><span id="pane_ssl"></span>**PANE\_SSL**


</dt> <dd>

The SSL pane.

</dd> <dt>

<span id="PANE_NAVIGATION"></span><span id="pane_navigation"></span>

<span id="PANE_NAVIGATION"></span><span id="pane_navigation"></span>**PANE\_NAVIGATION**


</dt> <dd>

The navigation pane.

</dd> <dt>

<span id="PANE_PROGRESS"></span><span id="pane_progress"></span>

<span id="PANE_PROGRESS"></span><span id="pane_progress"></span>**PANE\_PROGRESS**


</dt> <dd>

The progress bar pane.

</dd> <dt>

<span id="PANE_PRIVACY"></span><span id="pane_privacy"></span>

<span id="PANE_PRIVACY"></span><span id="pane_privacy"></span>**PANE\_PRIVACY**


</dt> <dd>

The privacy indicator pane.

</dd> </dl> </dd> <dt>

*pane* \[out\]
</dt> <dd>

Pointer to a **DWORD** containing the pane number.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                |
| End of client support<br/>    | Windows XP with SP2<br/>                                                      |
| End of server support<br/>    | Windows Server 2003<br/>                                                      |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 
