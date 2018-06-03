---
title: IpcGetGlobalProperty function
description: Returns information about environment properties.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: acb97e42-9883-463f-af53-929810e11e89
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- IpcGetGlobalProperty function Active Directory Rights Management Services SDK 2.0
topic_type:
- apiref
api_name:
- IpcGetGlobalProperty
api_location:
- Msipc.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IpcGetGlobalProperty function

Returns information about environment properties of the Rights Management Services SDK 2.1 system.

## Syntax


```C++
HRESULT WINAPI IpcGetGlobalProperty(
        DWORD  dwPropID,
  _Out_ LPVOID *ppvProperty
);
```



## Parameters

<dl> <dt>

*dwPropID* 
</dt> <dd>

The ID of the property that is being queried.

For a list of valid property IDs, see [**Environment Properties**](environment-properties.md).

</dd> <dt>

*ppvProperty* \[out\]
</dt> <dd>

A pointer to a variable that receives a pointer to the buffer that contains the queried information. The buffer is allocated by the system and must be freed by calling [**IpcFreeMemory**](ipcfreememory.md). The structure of the information depends on the *dwPropID* parameter. For more information, see [**Environment Properties**](environment-properties.md).

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

[**Environment Properties**](environment-properties.md)
</dt> <dt>

[**IpcFreeMemory**](ipcfreememory.md)
</dt> <dt>

[**IpcSetGlobalProperty**](ipcsetglobalproperty.md)
</dt> <dt>

[**Error codes**](error-codes.md)
</dt> </dl>

 

 





