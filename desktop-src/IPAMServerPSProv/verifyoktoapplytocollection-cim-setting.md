---
Description: 'Indicates whether the setting can be applied to the specified collection of managed system elements during the specified time or time interval.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '3b1f768a-d2e4-4631-a5ba-aa979a5930e1'
ms.prod: 'windows-server-dev'
ms.technology:
- 'internet-protocol-address-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'VerifyOKToApplyToCollection method of the CIM\_Setting class'
---

# VerifyOKToApplyToCollection method of the CIM\_Setting class

Indicates whether the setting can be applied to the specified collection of managed system elements during the specified time or time interval.

## Syntax


```mof
uint32 VerifyOKToApplyToCollection(
  [in]  CIM_CollectionOfMSEs REF Collection,
  [in]  datetime                 TimeToApply,
  [in]  datetime                 MustBeCompletedBy,
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

*CanNotApply* \[out\]
</dt> <dd>

When this method returns, this parameter contains an array of keys to the managed system elements that can not receive the setting.

</dd> </dl>

## Return value

The possible return values are:

<dl> <dt>


</dt> <dd>

0

The setting can be applied to the collection.

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

[**CIM\_Setting**](cim-setting.md)
</dt> </dl>

 

 




