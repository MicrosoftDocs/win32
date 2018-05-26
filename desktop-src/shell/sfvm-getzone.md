---
Description: Allows the callback object to provide Internet zone information. Used by IShellFolderViewCBMessageSFVCB.
ms.assetid: 6fae7925-b1be-4270-9318-7fa517563dad
title: SFVM\_GETZONE message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SFVM\_GETZONE message

\[This notification is supported through Windows XP Service Pack 2 (SP2) and Windows Server 2003. It might be unsupported in subsequent versions of Windows.\]

Allows the callback object to provide Internet zone information. Used by [**IShellFolderViewCB::MessageSFVCB**](/windows/win32/Shlobj/?branch=master).


```C++
SFVM_GETZONE
    lParam = (LPARAM)(DWORD*) zone;
            
```



## Parameters

<dl> <dt>

*zone* \[out\]
</dt> <dd>

One of the following values indicating the Internet zone. These values constitute the [**URLZONE**](ie.URLZONE_Enumerated_Type) enumeration, defined in Urlmon.h.

<dt>

<span id="URLZONE_LOCAL_MACHINE"></span><span id="urlzone_local_machine"></span>

<span id="URLZONE_LOCAL_MACHINE"></span><span id="urlzone_local_machine"></span>**URLZONE\_LOCAL\_MACHINE**


</dt> <dd>

Zone used for content already on the user's local computer. This zone is not exposed by the user interface.

</dd> <dt>

<span id="URLZONE_INTRANET"></span><span id="urlzone_intranet"></span>

<span id="URLZONE_INTRANET"></span><span id="urlzone_intranet"></span>**URLZONE\_INTRANET**


</dt> <dd>

Zone used for content found on an intranet.

</dd> <dt>

<span id="URLZONE_TRUSTED"></span><span id="urlzone_trusted"></span>

<span id="URLZONE_TRUSTED"></span><span id="urlzone_trusted"></span>**URLZONE\_TRUSTED**


</dt> <dd>

Zone used for trusted websites on the Internet.

</dd> <dt>

<span id="URLZONE_INTERNET"></span><span id="urlzone_internet"></span>

<span id="URLZONE_INTERNET"></span><span id="urlzone_internet"></span>**URLZONE\_INTERNET**


</dt> <dd>

Zone used for most of the content on the Internet.

</dd> <dt>

<span id="URLZONE_UNTRUSTED"></span><span id="urlzone_untrusted"></span>

<span id="URLZONE_UNTRUSTED"></span><span id="urlzone_untrusted"></span>**URLZONE\_UNTRUSTED**


</dt> <dd>

Zone used for websites that are not trusted.

</dd> </dl> </dd> </dl>

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 




