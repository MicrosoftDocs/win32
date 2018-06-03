---
title: SMS\_Attention method of the Microsoft\_IPMI class
description: Obtains the value of the IPMI status register.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 64f1a4e3-c5a5-43f3-b723-e1f92f6969fa
ms.prod: windows-server-dev
ms.technology:
- intelligent-platform-management-interface
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- IPMI driver WS-Management
- SMS_Attention method
- SMS_Attention method, Microsoft_IPMI class
- Microsoft_IPMI class, SMS_Attention method
topic_type:
- apiref
api_name:
- Microsoft_IPMI.SMS_Attention
api_location:
- IpmiDrv.sys
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SMS\_Attention method of the Microsoft\_IPMI class

Obtains the value of the IPMI status register.

## Syntax


```mof
void SMS_Attention(
  [out] boolean AttentionSet,
  [out] uint8   StatusRegisterValue
);
```



## Parameters

<dl> <dt>

*AttentionSet* \[out\]
</dt> <dd>

Indicates the status of the **SMS\_ATTN** register flag.

</dd> <dt>

*StatusRegisterValue* \[out\]
</dt> <dd>

Value of the IPMI status register.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\wmi<br/>                                                                   |
| DLL<br/>                      | <dl> <dt>IpmiDrv.sys</dt> </dl> |



## See also

<dl> <dt>

[**Microsoft\_IPMI**](microsoft-ipmi.md)
</dt> <dt>

[IPMI Provider](ipmi-provider.md)
</dt> </dl>

 

 





