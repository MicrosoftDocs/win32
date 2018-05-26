---
title: Environment properties
description: Environment property constants are used to query and set properties using IpcGetGlobalProperty and IpcSetGlobalProperty.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 1DBB272A-E36B-4DBF-802F-771AC875A709
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
topic_type:
- apiref
api_name:
- IPC_EI_API_MODE
- IPC_EI_RESERVED
- IPC_EI_APPLICATOIN_ID
- IPC_EI_STORE_NAME
api_location:
- Ipcprot.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Environment properties

Environment property constants are used to query and set properties using [**IpcGetGlobalProperty**](ipcgetglobalproperty.md) and [**IpcSetGlobalProperty**](ipcsetglobalproperty.md).

> [!Note]  
> Environment properties should be set after [**IpcInitialize**](ipcinitialize.md), but before calling any other Rights Management Services SDK 2.1 APIs.

 

<dl> <dt>

<span id="IPC_EI_API_MODE"></span><span id="ipc_ei_api_mode"></span>**IPC\_EI\_API\_MODE**
</dt> <dd> <dl> <dt>

3
</dt> <dt>



Use this constant to query or set the security mode. The default value is **IPC\_API\_MODE\_CLIENT**. See [**API Mode Values**](api-mode-values.md) for a list of security mode values.


</dt> </dl> </dd> <dt>

<span id="IPC_EI_RESERVED"></span><span id="ipc_ei_reserved"></span>**IPC\_EI\_RESERVED**
</dt> <dd> <dl> <dt>

4
</dt> <dt>



Reserved for future use.


</dt> </dl> </dd> <dt>

<span id="IPC_EI_APPLICATOIN_ID"></span><span id="ipc_ei_applicatoin_id"></span>**IPC\_EI\_APPLICATOIN\_ID**
</dt> <dd> <dl> <dt>

5
</dt> <dt>



Use this constant to define the application ID to use when authenticating with Azure RMS.

This property is only supported with [**IpcSetGlobalProperty**](ipcsetglobalproperty.md).

For more information, see [**IPC\_AAD\_APPLICATION\_ID**](ipc-aad-application-id.md) for more details.


</dt> </dl> </dd> <dt>

<span id="IPC_EI_STORE_NAME"></span><span id="ipc_ei_store_name"></span>**IPC\_EI\_STORE\_NAME**
</dt> <dd> <dl> <dt>

0x10000001
</dt> <dt>



The value set for **IPC\_EI\_STORE\_NAME** should be a valid folder name that is the location of a local store and must be no more than 8 characters. If this property is not set, the **IPC\_EI\_STORE\_NAME** will be shared with all other applications that also do not set the **IPC\_EI\_STORE\_NAME**.

> \[!Important\]  
> We strongly recommend that this property be set to a valid value.

 


</dt> </dl> </dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Header<br/>                   | <dl> <dt>Ipcprot.h (include Msipc.h)</dt> </dl> |



## See also

<dl> <dt>

[**IpcInitialize**](ipcinitialize.md)
</dt> <dt>

[**IpcGetGlobalProperty**](ipcgetglobalproperty.md)
</dt> <dt>

[**IpcSetGlobalProperty**](ipcsetglobalproperty.md)
</dt> <dt>

[**IPC\_AAD\_APPLICATION\_ID**](ipc-aad-application-id.md)
</dt> <dt>

[**API Mode Values**](api-mode-values.md)
</dt> </dl>

 

 





