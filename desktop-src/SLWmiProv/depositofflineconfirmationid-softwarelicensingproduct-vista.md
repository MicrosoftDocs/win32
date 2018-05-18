---
Description: 'Not supported. Use the DepositOfflineConfirmationId method.'
ms.assetid: '79450a4b-2b01-4458-815c-426602482a6e'
title: DepositOfflineConfirmationId method of the SoftwareLicensingProduct class
---

# DepositOfflineConfirmationId method of the SoftwareLicensingProduct class

Not supported. Use the [**DepositOfflineConfirmationId**](https://msdn.microsoft.com/library/cc534587) method.

**Windows Vista and Windows Server 2008:** Activates this product by depositing an Offline Confirmation Identifier for this product when performing a telephone activation.

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



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                       |
| End of client support<br/>    | Windows Vista<br/>                                                             |
| End of server support<br/>    | Windows Server 2008<br/>                                                       |
| Namespace<br/>                | Root\\CIMV2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>SLWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SLWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**SoftwareLicensingProduct**](softwarelicensingproduct-vista.md)
</dt> <dt>

[**DepositOfflineConfirmationId**](https://msdn.microsoft.com/library/cc534587)
</dt> </dl>

 

 




