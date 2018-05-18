---
Description: 'Shuts down a job.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '7D66E421-54D0-4088-89B7-BC8E4A9D676C'
ms.prod: 'windows-server-dev'
ms.technology:
- 'internet-protocol-address-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'KillJob method of the CIM\_ConcreteJob class'
---

# KillJob method of the CIM\_ConcreteJob class

Shuts down a job.

> [!Note]  
> This method is deprecated. Instead we recommend that you use the **RequestStateChange** method.

 

This method is inherited from the **CIM\_Job** class.

## Syntax


```mof
uint32 KillJob(
  [in] boolean DeleteOnKill
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

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                   |
| Namespace<br/>                | Root\\Microsoft\\IPAM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>IPAMServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IPAMServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ConcreteJob**](cim-concretejob.md)
</dt> </dl>

 

 




