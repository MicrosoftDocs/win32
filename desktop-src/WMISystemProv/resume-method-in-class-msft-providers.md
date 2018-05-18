---
title: Resume method of the MSFT\_Providers class
description: The Resume method resumes a specific instance of a provider.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '8406a1ec-4c9e-4d92-8f4a-3b3fa3c71380'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Resume method", "Resume method, MSFT_Providers class", "MSFT_Providers class, Resume method", "Resume method, MSFT_Providers class", "MSFT_Providers class, Resume method"]
topic_type:
- apiref
api_name:
- MSFT_Providers.Resume
- MSFT_Providers.Resume
api_location:
- WmiPrvSD.dll
api_type:
- COM
---

# Resume method of the MSFT\_Providers class

The **Resume** method resumes a specific instance of a provider.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
Uint32 Resume();
```



## Parameters

This method has no parameters.

## Return value

Returns a value of 0 (zero) if the provider was successfully resumed, and any other number to indicate an error.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMv2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>System.mof</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>WmiPrvSD.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_Providers**](msft-providers.md)
</dt> </dl>

 

 





