---
title: IpcFreeMemory function
description: Frees a buffer allocated by another Rights Management Services SDK 2.1 function.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'f72881ab-f456-4ddf-912e-ba316bca77bf'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["IpcFreeMemory function Active Directory Rights Management Services SDK 2.0"]
topic_type:
- apiref
api_name:
- IpcFreeMemory
api_location:
- Msipc.dll
api_type:
- DllExport
---

# IpcFreeMemory function

Frees a buffer allocated by another Rights Management Services SDK 2.1 function.

## Syntax


```C++
void WINAPI IpcFreeMemory(
  _In_ LPVOID pb
);
```



## Parameters

<dl> <dt>

*pb* \[in\]
</dt> <dd>

A pointer to the buffer to free.

</dd> </dl>

## Return value

This function does not return a value.

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Header<br/>                   | <dl> <dt>Ipcbase.h (include Msipc.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Msipc.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Msipc.dll</dt> </dl>                   |



 

 





