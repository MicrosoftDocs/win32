---
title: Adapter\_UnRegisterDLL function
description: Removes the registration of the provider DLL when Mofcomp.exe or Register-CimProvider.exe are used to register the provider with the WMI infrastructure.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c8abdeb8-c695-4149-a624-58204d3db74d
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Adapter_UnRegisterDLL function Windows Management Infrastructure (MI)
topic_type:
- apiref
api_name:
- Adapter_UnRegisterDLL
api_location:
- WmiToMi.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Adapter\_UnRegisterDLL function

Removes the registration of the provider DLL when Mofcomp.exe or Register-CimProvider.exe are used to register the provider with the WMI infrastructure. This function is required by a COM server, but is not used by it.

> \[!Important\]  
> This function is only used by generated code and should not be used by developers.

 

## Syntax


```C++
STDAPI Adapter_UnRegisterDLL(
   GUID classId
);
```



## Parameters

<dl> <dt>

*classId* 
</dt> <dd>

The COM class ID of the current provider.

</dd> </dl>

## Return value

This function always returns **S\_OK**.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| DLL<br/>                      | <dl> <dt>WmiToMi.dll</dt> </dl> |



## See also

<dl> <dt>

[Adapter Functions](adapter-functions.md)
</dt> </dl>

 

 





