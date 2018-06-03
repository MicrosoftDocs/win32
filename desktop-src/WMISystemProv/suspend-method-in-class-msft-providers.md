---
title: Suspend method of the MSFT\_Providers class
description: The Suspend method suspends a specific instance of a provider.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 79543231-6a07-4042-ae7c-28d451ce043a
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Suspend method
- Suspend method, MSFT_Providers class
- MSFT_Providers class, Suspend method
- Suspend method, MSFT_Providers class
- MSFT_Providers class, Suspend method
topic_type:
- apiref
api_name:
- MSFT_Providers.Suspend
- MSFT_Providers.Suspend
api_location:
- WmiPrvSD.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Suspend method of the MSFT\_Providers class

The **Suspend** method suspends a specific instance of a provider.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 Suspend();
```



## Parameters

This method has no parameters.

## Return value

Returns a value of 0 if the provider was successfully suspended, and any other number to indicate an error.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMv2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>System.mof</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>WmiPrvSD.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_Providers**](msft-providers.md)
</dt> </dl>

 

 





