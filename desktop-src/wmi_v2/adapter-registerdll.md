---
title: Adapter\_RegisterDLL function
description: Registers a provider DLL when Mofcomp.exe or Register-CimProvider.exe are used to register the provider with the WMI infrastructure.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '04ea5273-6c0e-490e-8b05-2c559feed70c'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Adapter_RegisterDLL function Windows Management Infrastructure (MI)"]
topic_type:
- apiref
api_name:
- Adapter_RegisterDLL
api_location:
- WmiToMi.dll
api_type:
- DllExport
---

# Adapter\_RegisterDLL function

Registers a provider DLL when Mofcomp.exe or Register-CimProvider.exe are used to register the provider with the WMI infrastructure. This function is required by a COM server, but is not used by it.

> \[!Important\]  
> This function is only used by generated code and should not be used by developers.

 

## Syntax


```C++
STDAPI Adapter_RegisterDLL(
   HINSTANCE module,
   GUID      classId
);
```



## Parameters

<dl> <dt>

*module* 
</dt> <dd>

The handle of the provider module.

</dd> <dt>

*classId* 
</dt> <dd>

The COM class ID of the current provider.

</dd> </dl>

## Return value

This function always returns **S\_OK**.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| DLL<br/>                      | <dl> <dt>WmiToMi.dll</dt> </dl> |



## See also

<dl> <dt>

[Adapter Functions](adapter-functions.md)
</dt> </dl>

 

 





