---
title: IpcSetGlobalProperty function
description: Sets environment properties for the system.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: d3e39fbb-ccb8-442e-9776-2ca81226552b
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- IpcSetGlobalProperty function Active Directory Rights Management Services SDK 2.0
topic_type:
- apiref
api_name:
- IpcSetGlobalProperty
api_location:
- Msipc.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# IpcSetGlobalProperty function

Sets environment properties for the system. Every environment configuration setting has a default value that can be overridden by using this function.

These properties can only be set once per process. Once the RMS system has been initialized with the call to [**IpcInitialize**](ipcinitialize.md), you may then set these properties, doing so before calling other Rights Management Services SDK 2.1 APIs.

## Syntax


```C++
HRESULT WINAPI IpcSetGlobalProperty(
       DWORD   dwPropID,
  _In_ LPCVOID pvProperty
);
```



## Parameters

<dl> <dt>

*dwPropID* 
</dt> <dd>

The ID of the property that is being set. For a list of valid property IDs, see [**Environment properties**](environment-properties.md).

</dd> <dt>

*pvProperty* \[in\]
</dt> <dd>

A pointer to a buffer that contains the value for the property. The structure of the property information depends on the property ID specified in the *dwPropID* parameter. For more information, see [**Environment properties**](environment-properties.md).

</dd> </dl>

## Return value

If the function succeeds, the return value is **S\_OK**. If the function fails, it returns an **HRESULT** value that indicates the error.

For more information, see [**Error codes**](error-codes.md) for a description of all RMS SDK 2.1 return values.

Possible values include, but are not limited to, those in the following list.

<dl> <dt>

**IPCERROR\_PROPERTY\_ALREADY\_SET**
</dt> <dd>

Meaning: When the *dwPropID* parameter is set to **IPC\_EI\_API\_MODE**, this property has been set before.

Action: This function should be called before any other RMS SDK 2.1 function if the application needs to change the API mode. The RMS SDK 2.1 will set the API mode automatically, and the API mode cannot be changed after it is set.

</dd> </dl>

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

[**Environment properties**](environment-properties.md)
</dt> <dt>

[**IpcGetGlobalProperty**](ipcgetglobalproperty.md)
</dt> <dt>

[**Error codes**](error-codes.md)
</dt> </dl>

 

 





