---
Description: Indicates whether the setting can be applied to the specified managed system element during the specified time or time interval.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: af86b5de-6630-408c-9c3f-18f8e2e860f1
ms.prod: windows-server-dev
ms.technology:
- internet-protocol-address-management
- windows-management-instrumentation
ms.tgt_platform: multiple
title: VerifyOKToApplyToMSE method of the CIM\_Setting class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# VerifyOKToApplyToMSE method of the CIM\_Setting class

Indicates whether the setting can be applied to the specified managed system element during the specified time or time interval.

## Syntax


```mof
uint32 VerifyOKToApplyToMSE(
  [in] CIM_ManagedSystemElement REF MSE,
  [in] datetime                     TimeToApply,
  [in] datetime                     MustBeCompletedBy
);
```



## Parameters

<dl> <dt>

*MSE* \[in\]
</dt> <dd>

A reference to the managed system element to verify.

</dd> <dt>

*TimeToApply* \[in\]
</dt> <dd>

The time or time interval to verify with the setting.

</dd> <dt>

*MustBeCompletedBy* \[in\]
</dt> <dd>

The required completion time for the method.

</dd> </dl>

## Return value

The possible return values are:

<dl> <dt>


</dt> <dd>

0

The setting can be applied.

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

3 ...

Any other error.

</dd> </dl>

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

[**CIM\_Setting**](cim-setting.md)
</dt> </dl>

 

 




