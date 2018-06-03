---
Description: Note  This method is deprecated. Instead we recommend that you use the RequestStateChange method. Shuts down a job.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1c218da9-49c2-4f6e-9484-ad5a3efdb89c
ms.prod: windows-server-dev
ms.technology:
- internet-protocol-address-management
- windows-management-instrumentation
ms.tgt_platform: multiple
title: KillJob method of the CIM\_Job class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# KillJob method of the CIM\_Job class

> [!Note]  
> This method is deprecated. Instead we recommend that you use the **RequestStateChange** method.

 

Shuts down a job.

## Syntax


```mof
uint32 KillJob(
  [in] boolean DeleteOnKill
);
```



## Parameters

<dl> <dt>

*DeleteOnKill* \[in\]
</dt> <dd>

**True** if the job should be automatically deleted upon termination; otherwise, **false**.

> [!Note]  
> This parameter takes precedence of the **DeleteOnCompletion** property of the **CIM\_Job** class.

 

</dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code.

<dl> <dt>

**Success** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Unknown** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Failed** (4)
</dt> <dt>

**Access Denied** (6)
</dt> <dt>

**Not Found** (7)
</dt> <dt>

**DMTF Reserved** (8 32767)
</dt> <dt>

**Vendor Specific** (32768 65535)
</dt> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                   |
| Namespace<br/>                | Root\\Microsoft\\IPAM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>IPAMServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IPAMServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Job**](cim-job.md)
</dt> </dl>

 

 




