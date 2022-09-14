---
description: Changes the owner authorization credential of the TPM device. The old and new owner authorization passwords are required.
ms.assetid: 5b7f1aec-5181-4330-982c-d80a1d5ae9e8
title: ChangeOwnerAuth method of the CIM_TPM class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_TPM.ChangeOwnerAuth
api_type: 
- COM
api_location: 
- vmms.exe
---

# ChangeOwnerAuth method of the CIM\_TPM class

Changes the owner authorization credential of the TPM device. The old and new owner authorization passwords are required.

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

Represents the old owner authorization credential required to take ownership of the TPM device.The **CIM\_SharedCredential** subclass may be required with non-null value of the **CIM\_SharedCredential**.**Secret** property for the parameter.

</dd> <dt>

*NewOwnerAuth* \[in\]
</dt> <dd>

Represents the new owner authorization credential required to take ownership of the TPM device.The **CIM\_SharedCredential** subclass may be required with non-null value of the **CIM\_SharedCredential**.**Secret** property for the parameter.

</dd> </dl>

## Return value

Returns a 0 on success; otherwise, returns an error.

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Unknown/Unspecified Error** (2)
</dt> <dt>

**DMTF Reserved** (3..4095)
</dt> <dt>

**Method Reserved** (4096..32767)
</dt> <dt>

**Vendor Specified** (32768..65535)
</dt> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                          |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_TPM**](cim-tpm.md)
</dt> </dl>

 

 




