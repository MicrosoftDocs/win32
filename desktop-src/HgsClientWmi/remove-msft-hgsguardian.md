---
title: Remove method of the MSFT\_HgsGuardian class
description: Removes a guardian from the guardian store.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 128cdf8d-91b6-4fa8-b5e5-d3a3958dfd19
ms.prod: windows-server-dev
ms.technology:
- host-guardian-service
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Remove method
- Remove method, MSFT_HgsGuardian class
- MSFT_HgsGuardian class, Remove method
topic_type:
- apiref
api_name:
- MSFT_HgsGuardian.Remove
api_location:
- HgsClientWmi.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Remove method of the MSFT\_HgsGuardian class

Removes a guardian from the guardian store.

## Syntax


```mof
uint32 Remove(
  [in] string Name
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the guardian to remove.

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                              |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Hgs<br/>                                                    |
| MOF<br/>                      | <dl> <dt>HgsClientWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>HgsClientWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_HgsGuardian**](msft-hgsguardian.md)
</dt> </dl>

 

 





