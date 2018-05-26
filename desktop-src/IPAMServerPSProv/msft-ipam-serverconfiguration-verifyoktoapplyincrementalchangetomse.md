---
Description: Indicates whether a subset of the properties in the setting can be applied to the managed system element during the specified time or time interval.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0D2E9AC6-DCF7-4CC4-8DB3-908E5D241116
ms.prod: windows-server-dev
ms.technology:
- internet-protocol-address-management
- windows-management-instrumentation
ms.tgt_platform: multiple
title: VerifyOKToApplyIncrementalChangeToMSE method of the MSFT\_IPAM\_ServerConfiguration class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# VerifyOKToApplyIncrementalChangeToMSE method of the MSFT\_IPAM\_ServerConfiguration class

Indicates whether a subset of the properties in the setting can be applied to the managed system element during the specified time or time interval.

This method is inherited from the **CIM\_Setting** class.

## Syntax


```mof
uint32 VerifyOKToApplyIncrementalChangeToMSE(
  [in] CIM_ManagedSystemElement Ref MSE,
  [in] datetime                     TimeToApply,
  [in] datetime                     MustBeCompletedBy,
  [in] string                       PropertiesToApply[]
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

[**MSFT\_IPAM\_ServerConfiguration**](msft-ipam-serverconfiguration.md)
</dt> </dl>

 

 




