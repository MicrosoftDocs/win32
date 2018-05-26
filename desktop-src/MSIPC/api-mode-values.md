---
title: API mode values
description: Constants for specifying security mode.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: DF3249F1-AB84-4DF2-BDF5-65C9DD42554E
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
topic_type:
- apiref
api_name:
- IPC_API_MODE_CLIENT
- IPC_API_MODE_SERVER
- IPC_API_MODE_CLIENT_IMPERSONATION
api_location:
- Ipcprot.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# API mode values

Constants for specifying security mode.

For more usage information see, [Setting the API security mode](setting-the-api-security-mode--api-mode-.md).

<dl> <dt>

<span id="IPC_API_MODE_CLIENT"></span><span id="ipc_api_mode_client"></span>**IPC\_API\_MODE\_CLIENT**
</dt> <dd> <dl> <dt>

1
</dt> <dt>



Used for less trusted systems, such as those running on a client operating system.


</dt> </dl> </dd> <dt>

<span id="IPC_API_MODE_SERVER"></span><span id="ipc_api_mode_server"></span>**IPC\_API\_MODE\_SERVER**
</dt> <dd> <dl> <dt>

2
</dt> <dt>



Used for more trusted systems, such as those running on a server operating system.


</dt> </dl> </dd> <dt>

<span id="IPC_API_MODE_CLIENT_IMPERSONATION"></span><span id="ipc_api_mode_client_impersonation"></span>**IPC\_API\_MODE\_CLIENT\_IMPERSONATION**
</dt> <dd> <dl> <dt>

3
</dt> <dt>



This value is not supported and should not be used.

> [!Note]  
> This value may be removed from future versions of the RMS SDK 2.1.

 

The behavior of [**IpcSetGlobalProperty**](ipcsetglobalproperty.md) is undefined when using this value with the **IPC\_EI\_API\_MODE** property.


</dt> </dl> </dd> </dl>

## Remarks

The security mode is queried or set by calling [**IpcGetGlobalProperty**](ipcgetglobalproperty.md) or [**IpcSetGlobalProperty**](ipcsetglobalproperty.md) with the **IPC\_EI\_API\_MODE** environment property specified. For more information, see [**Environment Properties**](environment-properties.md).

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Header<br/>                   | <dl> <dt>Ipcprot.h (include Msipc.h)</dt> </dl> |



## See also

<dl> <dt>

[Setting the API security mode](setting-the-api-security-mode--api-mode-.md)
</dt> <dt>

[**IpcGetGlobalProperty**](ipcgetglobalproperty.md)
</dt> <dt>

[**IpcSetGlobalProperty**](ipcsetglobalproperty.md)
</dt> <dt>

[**Environment Properties**](environment-properties.md)
</dt> </dl>

 

 





