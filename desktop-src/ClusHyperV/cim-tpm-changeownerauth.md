---
title: ChangeOwnerAuth method of the CIM\_TPM class
description: Changes the owner authorization credential of the TPM device.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9fa1c6de-97af-4cf2-868f-e1a79c035da2
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ChangeOwnerAuth method
- ChangeOwnerAuth method, CIM_TPM class
- CIM_TPM class, ChangeOwnerAuth method
topic_type:
- apiref
api_name:
- CIM_TPM.ChangeOwnerAuth
api_location:
- VMMS.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ChangeOwnerAuth method of the CIM\_TPM class

Changes the owner authorization credential of the TPM device.

> [!Note]  
> This method requires the old and new owner authorization passwords. For more information, see Section 17 Changing AuthData of *Spec \#3*.

 

## Syntax


```mof
uint32 ChangeOwnerAuth(
  [in] string OldOwnerAuth,
  [in] string NewOwnerAuth
);
```



## Parameters

<dl> <dt>

*OldOwnerAuth* \[in\]
</dt> <dd>

The old owner authorization credential that is required to take ownership of the TPM device.

> [!Note]  
> This parameter might require that the **CIM\_SharedCredential.Secret** of the **CIM\_SharedCredential** class contains a non-NULL value.

 

</dd> <dt>

*NewOwnerAuth* \[in\]
</dt> <dd>

The new owner authorization credentials required to take ownership of the TPM device.

> [!Note]  
> This parameter might require that the **CIM\_SharedCredential.Secret** of the **CIM\_SharedCredential** class contains a non-NULL value.

 

</dd> </dl>

## Return value

The possible return values are:

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Unknown/Unspecified Error** (2)
</dt> <dt>

**DMTF Reserved** (3 4095)
</dt> <dt>

**Method Reserved** (4096 32767)
</dt> <dt>

**Vendor Specified** (32768 65535)
</dt> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**CIM\_TPM**](cim-tpm.md)
</dt> </dl>

 

 





