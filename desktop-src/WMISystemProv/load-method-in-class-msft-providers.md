---
title: Load method of the MSFT\_Providers class
description: The Load method loads a specific instance of a provider.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 940efde0-8363-4c03-ab7c-b12e1ec13fe9
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Load method
- Load method, MSFT_Providers class
- MSFT_Providers class, Load method
- Load method, MSFT_Providers class
- MSFT_Providers class, Load method
topic_type:
- apiref
api_name:
- MSFT_Providers.Load
- MSFT_Providers.Load
api_location:
- WmiPrvSD.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Load method of the MSFT\_Providers class

The **Load** method loads a specific instance of a provider.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
Uint32 Load(
  [in] string Namespace,
  [in] string User,
  [in] string Locale,
  [in] string Provider,
  [in] string TransactionIdentifier
);
```



## Parameters

<dl> <dt>

*Namespace* \[in\]
</dt> <dd>

Provider namespace.

</dd> <dt>

*User* \[in\]
</dt> <dd>

Reserved for future use.

</dd> <dt>

*Locale* \[in\]
</dt> <dd>

Reserved for future use.

</dd> <dt>

*Provider* \[in\]
</dt> <dd>

Provider name.

</dd> <dt>

*TransactionIdentifier* \[in\]
</dt> <dd>

Reserved for future use.

</dd> </dl>

## Return value

Returns an integer value of 0 if the provider was successfully loaded, 1 if the request is not supported, and any other number to indicate an error.

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

 

 





