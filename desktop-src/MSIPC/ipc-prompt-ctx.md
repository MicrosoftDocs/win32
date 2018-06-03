---
title: IPC\_PROMPT\_CTX structure
description: Provides context for user prompts;.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: f330f876-6bd9-484c-bb5a-41c41631ecb0
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- IPC_PROMPT_CTX structure Active Directory Rights Management Services SDK 2.0
- PIPC_PROMPT_CTX structure pointer Active Directory Rights Management Services SDK 2.0
- PCIPC_PROMPT_CTX structure pointer Active Directory Rights Management Services SDK 2.0
topic_type:
- apiref
api_name:
- IPC_PROMPT_CTX
api_location:
- Ipcbase.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# IPC\_PROMPT\_CTX structure

Provides context for user prompts; in the event that a process must be prompted for credentials or to display information, this context is used to determine the behavior of the prompts.

## Syntax


```C++
typedef struct _IPC_PROMPT_CTX {
  DWORD            cbSize;
  HWND             hwndParent;
  DWORD            dwFlags;
  HANDLE           hCancelEvent;
  PCIPC_CREDENTIAL pcCredential;
} IPC_PROMPT_CTX, *PIPC_PROMPT_CTX;typedef const IPC_PROMPT_CTX *PCIPC_PROMPT_CTX;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

Used for version control. Must be set to `sizeof(IPC_PROMPT_CTX)`.

</dd> <dt>

**hwndParent**
</dt> <dd>

Optional handle to parent window for dialogs.

Setting this handle will cause the function to display all UI modal to the specified handle.

Set to **NULL** if not used.

</dd> <dt>

**dwFlags**
</dt> <dd>

Flags that specify prompt behavior.

<dt>

<span id="IPC_PROMPT_FLAG_SILENT"></span><span id="ipc_prompt_flag_silent"></span>

<span id="IPC_PROMPT_FLAG_SILENT"></span><span id="ipc_prompt_flag_silent"></span>**IPC\_PROMPT\_FLAG\_SILENT** (0x1)


</dt> <dd>

Do not prompt the user for input. Use of this flag will cause the **IPCERROR\_NEEDS\_UI** error to be returned if a prompt is required.

</dd> <dt>

<span id="IPC_PROMPT_FLAG_OFFLINE"></span><span id="ipc_prompt_flag_offline"></span>

<span id="IPC_PROMPT_FLAG_OFFLINE"></span><span id="ipc_prompt_flag_offline"></span>**IPC\_PROMPT\_FLAG\_OFFLINE** (0x2)


</dt> <dd>

Do not access the network. Use of this flag will cause the **IPCERROR\_NEEDS\_ONLINE** error to be returned if accessing the network is required.

This flag should not be used under normal conditions. When this flag is not set, the platform will attempt to service all requests offline and will go online only when necessary to service the request successfully. Setting this flag will not improve the platform's performance characteristics for requests that can be serviced offline, and will cause unwanted failures when the request could have been serviced online.

</dd> <dt>

<span id="IPC_PROMPT_FLAG_HAS_USER_CONSENT"></span><span id="ipc_prompt_flag_has_user_consent"></span>

<span id="IPC_PROMPT_FLAG_HAS_USER_CONSENT"></span><span id="ipc_prompt_flag_has_user_consent"></span>**IPC\_PROMPT\_FLAG\_HAS\_USER\_CONSENT** (0x4)


</dt> <dd>

This flag causes the privacy dialog display to be skipped when contacting an RMS server for the first time.

Using this flag will cause the URLs to be cached as if consent has already given.

</dd> </dl> </dd> <dt>

**hCancelEvent**
</dt> <dd>

Optional handle to an event created by [CreateEvent](https://msdn.microsoft.com/library/windows/desktop/ms682396.aspx) or [OpenEvent.](https://msdn.microsoft.com/library/windows/desktop/ms684305.aspx)

Setting this event cancels active calls to which this structure was passed. The initial state of the event should be non-signaled . If the event is in signaled state, the call will be aborted.

Set to **NULL** if not used.

</dd> <dt>

**pcCredential**
</dt> <dd>

Credential, represented by an [**IPC\_CREDENTIAL**](ipc-credential.md) structure, to authenticate to an RMS Server. This value can be NULL.

Credential will be ignored if **IPC\_PROMPT\_FLAG\_OFFLINE** flag is used. See the **dwFlags** member of this structure.

</dd> </dl>

## Remarks

If the application does not want the user to be prompted, the **IPC\_PROMPT\_FLAG\_SILENT** flag can be used.

If user prompting is allowed, the parent window for modal dialogs can be specified.

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Header<br/>                   | <dl> <dt>Ipcbase.h (include Msipc.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPC\_CREDENTIAL**](ipc-credential.md)
</dt> <dt>

[CreateEvent](https://msdn.microsoft.com/library/windows/desktop/ms682396.aspx)
</dt> <dt>

[OpenEvent](https://msdn.microsoft.com/library/windows/desktop/ms684305.aspx)
</dt> </dl>

 

 





