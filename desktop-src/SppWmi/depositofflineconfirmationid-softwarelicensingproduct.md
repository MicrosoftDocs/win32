---
title: DepositOfflineConfirmationId method of the SoftwareLicensingProduct class
description: Activates this product by depositing an Offline Confirmation Identifier for this product when performing a telephone activation.
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'a9145dcb-16d4-474e-b13c-b9e6551e58e1'
keywords: ["DepositOfflineConfirmationId method Windows Management Instrumentation", "DepositOfflineConfirmationId method Windows Management Instrumentation , SoftwareLicensingProduct class", "SoftwareLicensingProduct class Windows Management Instrumentation , DepositOfflineConfirmationId method"]
topic_type:
- apiref
api_name:
- SoftwareLicensingProduct.DepositOfflineConfirmationId
api_location:
- SppWmi.dll
api_type:
- COM
---

# DepositOfflineConfirmationId method of the SoftwareLicensingProduct class

Activates this product by depositing an Offline Confirmation Identifier for this product when performing a telephone activation.

## Syntax


```mof
uint32 DepositOfflineConfirmationId(
  [in] string InstallationId,
  [in] string ConfirmationId
);
```



## Parameters

<dl> <dt>

*InstallationId* \[in\]
</dt> <dd>

Specifies the installation ID.

</dd> <dt>

*ConfirmationId* \[in\]
</dt> <dd>

Specifies the confirmation ID.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                     |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                |
| MOF<br/>                      | <dl> <dt>SppWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SppWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**SoftwareLicensingProduct**](softwarelicensingproduct.md)
</dt> </dl>

 

 





