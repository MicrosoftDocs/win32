---
title: IpcGetKeyProperty function
description: Returns requested property information.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 1feff262-e92d-4209-98a7-ce0b82ece301
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- IpcGetKeyProperty function Active Directory Rights Management Services SDK 2.0
topic_type:
- apiref
api_name:
- IpcGetKeyProperty
api_location:
- Msipc.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# IpcGetKeyProperty function

Returns requested property information.

## Syntax


```C++
HRESULT WINAPI IpcGetKeyProperty(
  _In_       IPC_KEY_HANDLE hKey,
             DWORD          dwPropID,
  _Reserved_ LPVOID         pvReserved,
  _Out_      LPVOID         *ppvProperty
);
```



## Parameters

<dl> <dt>

*hKey* \[in\]
</dt> <dd>

A handle to the key object.

</dd> <dt>

*dwPropID* 
</dt> <dd>

The ID of the property to query.

<dt>

<span id="IPC_KI_BLOCK_SIZE"></span><span id="ipc_ki_block_size"></span>

<span id="IPC_KI_BLOCK_SIZE"></span><span id="ipc_ki_block_size"></span>**IPC\_KI\_BLOCK\_SIZE** (2)


</dt> <dd>

*ppvProperty* is of type **LPDWORD**\*.

The block size used when encrypting/decrypting.

</dd> <dt>

<span id="IPC_KI_LICENSE"></span><span id="ipc_ki_license"></span>

<span id="IPC_KI_LICENSE"></span><span id="ipc_ki_license"></span>**IPC\_KI\_LICENSE** (6)


</dt> <dd>

*ppvProperty* is of type **PIPC\_BUFFER**\*. For more information, see [**AD RMS data types**](microsoft-information-protection-and-control-client-data-types.md).

The license from which the key object was created.

See [**IpcGetKey**](ipcgetkey.md) for details.

</dd> <dt>

<span id="IPC_KI_USER_DISPLAYNAME"></span><span id="ipc_ki_user_displayname"></span>

<span id="IPC_KI_USER_DISPLAYNAME"></span><span id="ipc_ki_user_displayname"></span>**IPC\_KI\_USER\_DISPLAYNAME** (7)


</dt> <dd>

*ppvProperty* is of type **LPWSTR**\*.

The user for which the key is acquired.

</dd> </dl> </dd> <dt>

*pvReserved* 
</dt> <dd>

This parameter is reserved for future use. It must be **NULL**.

</dd> <dt>

*ppvProperty* \[out\]
</dt> <dd>

A pointer to a variable that receives a pointer to the buffer that contains the property information. The structure of the property information depends on the *dwPropID* parameter.

> [!Note]  
> The buffer is allocated by the RMS SDK 2.1 and must be freed by calling [**IpcFreeMemory**](ipcfreememory.md).

 

</dd> </dl>

## Return value

If the function succeeds, the return value is **S\_OK**. If the function fails, it returns an **HRESULT** value that indicates the error.

For more information, see [**Error codes**](error-codes.md) for a description of all RMS SDK 2.1 return values.

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Header<br/>                   | <dl> <dt>Ipcprot.h (include Msipc.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Msipc.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Msipc.dll</dt> </dl>                   |



## See also

<dl> <dt>

[**AD RMS data types**](microsoft-information-protection-and-control-client-data-types.md)
</dt> <dt>

[**IpcFreeMemory**](ipcfreememory.md)
</dt> <dt>

[**IpcGetKey**](ipcgetkey.md)
</dt> <dt>

[**Error codes**](error-codes.md)
</dt> </dl>

 

 





