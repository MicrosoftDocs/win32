---
title: Step method of the PS\_DnsServerSigningKeyRollover class
description: Forces KSK rollover that is waiting for a parent DS update.
audience: developer
ms.assetid: a6890628-bc02-498d-8363-a72a73e00086
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Step method
- Step method, PS_DnsServerSigningKeyRollover class
- PS_DnsServerSigningKeyRollover class, Step method
topic_type:
- apiref
api_name:
- PS_DnsServerSigningKeyRollover.Step
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Step method of the PS\_DnsServerSigningKeyRollover class

Forces KSK rollover that is waiting for a parent DS update.

## Syntax


```mof
uint32 Step(
  [in]  string              ZoneName,
  [in]  string              KeyId,
  [in]  boolean             Force,
  [in]  boolean             PassThru,
  [in]  string              ComputerName,
  [out] DnsServerSigningKey cmdletOutput
);
```



## Parameters

<dl> <dt>

*ZoneName* \[in\]
</dt> <dd>

Name of the zone in which the operation is performed.

</dd> <dt>

*KeyId* \[in\]
</dt> <dd>

Uniquely identifies the key.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

**true** to not require user confirmation before continuing with the operation; **false** to require user confirmation. The default is **false**.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**True** to return the object that was modified by the method. By default, this method does not generate any output.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DnsServerSigningKeyRollover**](ps-dnsserversigningkeyrollover.md) class.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerSigningKeyRollover**](ps-dnsserversigningkeyrollover.md)
</dt> </dl>

 

 





