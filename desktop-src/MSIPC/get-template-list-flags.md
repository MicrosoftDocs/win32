---
title: Get template list flags
description: These flags specify optional behavior for the IpcGetTemplateList and IpcGetTemplateIssuerList functions.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 8787D219-AAA2-40A2-BCDC-78211E39CAEA
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
topic_type:
- apiref
api_name:
- IPC_GTL_FLAG_DEFAULT
- IPC_GTL_FLAG_FORCE_DOWNLOAD
- IPC_GTIL_FLAG_DEFAULT_SERVER_ONLY
api_location:
- Ipcprot.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Get template list flags

These flags specify optional behavior for the [**IpcGetTemplateList**](ipcgettemplatelist.md) and [**IpcGetTemplateIssuerList**](ipcgettemplateissuerlist.md) functions.

<dl> <dt>

<span id="IPC_GTL_FLAG_DEFAULT"></span><span id="ipc_gtl_flag_default"></span>**IPC\_GTL\_FLAG\_DEFAULT**
</dt> <dd> <dl> <dt>

0
</dt> <dt>



0 is allowed.


</dt> </dl> </dd> <dt>

<span id="IPC_GTL_FLAG_FORCE_DOWNLOAD"></span><span id="ipc_gtl_flag_force_download"></span>**IPC\_GTL\_FLAG\_FORCE\_DOWNLOAD**
</dt> <dd> <dl> <dt>

1
</dt> <dt>



Use this flag to force the download of templates from the server. Templates are cached on the client and are not downloaded again unless the cache is expired or **IPC\_GTL\_FLAG\_FORCE\_DOWNLOAD** is set.

> [!Note]  
> This flag should not be used under normal conditions. Using locally cached templates has better performance characteristics and will less likely cause the display of any unwanted UI.

 


</dt> </dl> </dd> <dt>

<span id="IPC_GTIL_FLAG_DEFAULT_SERVER_ONLY"></span><span id="ipc_gtil_flag_default_server_only"></span>**IPC\_GTIL\_FLAG\_DEFAULT\_SERVER\_ONLY**
</dt> <dd> <dl> <dt>

1
</dt> <dt>



Use this flag to retrieve only the default server for the enterprise or user.

For usage information, see [**IpcGetTemplateIssuerList**](ipcgettemplateissuerlist.md).


</dt> </dl> </dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Header<br/>                   | <dl> <dt>Ipcprot.h (include Msipc.h)</dt> </dl> |



 

 





