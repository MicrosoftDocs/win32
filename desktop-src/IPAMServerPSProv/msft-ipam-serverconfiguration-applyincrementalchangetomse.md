---
Description: 'Applies the subset of the properties in the setting to a managed system element.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: 'DFEE0A77-1C7B-441C-A5AD-3F2C39DF8F3C'
ms.prod: 'windows-server-dev'
ms.technology:
- 'internet-protocol-address-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'ApplyIncrementalChangeToMSE method of the MSFT\_IPAM\_ServerConfiguration class'
---

# ApplyIncrementalChangeToMSE method of the MSFT\_IPAM\_ServerConfiguration class

Applies the subset of the properties in the setting to a managed system element.

This method is inherited from the **CIM\_Setting** class.

## Syntax


```mof
uint32 ApplyIncrementalChangeToMSE(
  [in] CIM_ManagedSystemElement Ref MSE,
  [in] datetime                     TimeToApply,
  [in] datetime                     MustBeCompletedBy,
  [in] string                       PropertiesToApply[]
);
```



## Parameters

<dl> <dt>

*MSE* \[in\]
</dt> <dd>

A reference to the managed system element that receives the setting.

</dd> <dt>

*TimeToApply* \[in\]
</dt> <dd>

The time or time interval to verify with the setting.

</dd> <dt>

*MustBeCompletedBy* \[in\]
</dt> <dd>

The required completion time for the method.

</dd> <dt>

*PropertiesToApply* \[in\]
</dt> <dd>

An array that contains the property names of the setting.

</dd> </dl>

## Return value

The possible return values are:

<dl> <dt>


</dt> <dd>

0

The method completed successfully.

</dd> <dt>


</dt> <dd>

1

The method is not supported.

</dd> <dt>


</dt> <dd>

2

The setting could not be applied by the specified time.

</dd> <dt>


</dt> <dd>

3–...

Any other error.

</dd> </dl>

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

[**MSFT\_IPAM\_ServerConfiguration**](msft-ipam-serverconfiguration.md)
</dt> </dl>

 

 




