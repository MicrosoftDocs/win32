---
Description: Applies the setting to a managed system element.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: CFF97CB8-97FF-4715-914D-4B08006D1497
ms.prod: windows-server-dev
ms.technology:
- internet-protocol-address-management
- windows-management-instrumentation
ms.tgt_platform: multiple
title: ApplyToMSE method of the MSFT\_IPAM\_ServerConfiguration class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ApplyToMSE method of the MSFT\_IPAM\_ServerConfiguration class

Applies the setting to a managed system element.

This method is inherited from the **CIM\_Setting** class.

## Syntax


```mof
uint32 ApplyToMSE(
  [in] CIM_ManagedSystemElement  REF MSE,
  [in] datetime                      TimeToApply,
  [in] datetime                      MustBeCompletedBy
);
```



## Parameters

<dl> <dt>

*MSE* \[in\]
</dt> <dd>

A reference to the [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) object that receives the setting.

</dd> <dt>

*TimeToApply* \[in\]
</dt> <dd>

The time or a time interval on which to apply the setting.

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

 

 




