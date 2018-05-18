---
Description: 'Indicates whether a subset of the properties in the setting can be applied to the collection of managed systems element during the specified time or time interval.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: 'C0E64462-BA02-4D53-8BAB-06AADAD35682'
ms.prod: 'windows-server-dev'
ms.technology:
- 'internet-protocol-address-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'VerifyOKToApplyIncrementalChangeToCollection method of the MSFT\_IPAM\_ServerConfiguration class'
---

# VerifyOKToApplyIncrementalChangeToCollection method of the MSFT\_IPAM\_ServerConfiguration class

Indicates whether a subset of the properties in the setting can be applied to the collection of managed systems element during the specified time or time interval.

This method is inherited from the **CIM\_Setting** class.

## Syntax


```mof
uint32 VerifyOKToApplyIncrementalChangeToCollection(
  [in]  CIM_CollectionOfMSEs Ref Collection,
  [in]  datetime                 TimeToApply,
  [in]  datetime                 MustBeCompletedBy,
  [in]  string                   PropertiesToApply[],
  [out] string                   CanNotApply[]
);
```



## Parameters

<dl> <dt>

*Collection* \[in\]
</dt> <dd>

A reference to the collection of managed system elements to verify.

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

</dd> <dt>

*CanNotApply* \[out\]
</dt> <dd>

When this method returns, this parameter contains an array of keys to the managed system elements that can not receive the setting.

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

 

 




