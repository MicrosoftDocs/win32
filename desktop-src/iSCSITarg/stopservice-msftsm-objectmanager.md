---
title: StopService method of the MSFTSM\_ObjectManager class
description: Places the service in the stopped state. Deprecated. Instead, use the RequestStateChange method.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e7be9780-2662-4b30-ae61-1ad6f594e7f4
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- StopService method iSCSI Software Target API
- StopService method iSCSI Software Target API , MSFTSM_ObjectManager class
- MSFTSM_ObjectManager class iSCSI Software Target API , StopService method
topic_type:
- apiref
api_name:
- MSFTSM_ObjectManager.StopService
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# StopService method of the MSFTSM\_ObjectManager class

Places the service in the stopped state. Deprecated. Instead, use the [**RequestStateChange**](requeststatechange-msftsm-objectmanager.md) method. Invoking this method should set the **RequestedState** property appropriately.

This method is inherited from the [**CIM\_Service**](https://msdn.microsoft.com/library/aa388442) class.

## Syntax


```mof
uint32 StopService();
```



## Parameters

This method has no parameters.

## Return value

<dl> <dt>


</dt> <dd>

0

The Service was successfully stopped.

</dd> <dt>


</dt> <dd>

1

The request is not supported.

</dd> <dt>


</dt> <dd>

2 = *value*

Undefined error.

</dd> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| Header<br/>                   | <dl> <dt>Sdoias.h</dt> </dl>              |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SmIScsiTargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFTSM\_ObjectManager**](msftsm-objectmanager.md)
</dt> <dt>

[**CIM\_EnabledLogicalElement**](https://msdn.microsoft.com/library/mt446063)
</dt> <dt>

[**CIM\_Service**](https://msdn.microsoft.com/library/aa388442)
</dt> </dl>

 

 





