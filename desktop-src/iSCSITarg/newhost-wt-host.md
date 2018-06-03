---
title: NewHost method of the WT\_Host class
description: Creates a new iSCSI target by using the specified target name.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ad5de576-de2f-4b54-a9cd-5e1854868387
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- NewHost method iSCSI Software Target API
- NewHost method iSCSI Software Target API , WT_Host class
- WT_Host class iSCSI Software Target API , NewHost method
topic_type:
- apiref
api_name:
- WT_Host.NewHost
api_location:
- WtWmiProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# NewHost method of the WT\_Host class

Creates a new iSCSI target by using the specified target name.

## Syntax


```mof
WT_Host NewHost(
  [in] string HostName,
  [in] string ResourceGroup
);
```



## Parameters

<dl> <dt>

*HostName* \[in\]
</dt> <dd>

A name that uniquely identifies the iSCSI target entry within the iSCSI target server. This is not the IQN (iSCSI Qualified Name), but a Microsoft iSCSI Target Server-specific identifier. It is recommended that the initiator’s NetBIOS name be used as the host name for easier identification.

</dd> <dt>

*ResourceGroup* \[in\]
</dt> <dd>

Optional name of the cluster group that the iSCSI target resource belongs to. If the Microsoft iSCSI Target Server Service is not running on a Microsoft Failover Cluster, this parameter is an empty string.

</dd> </dl>

## Remarks

If the Microsoft iSCSI Target Server service is running on a Microsoft Failover Cluster, a cluster resource is created to represent the new iSCSI target. If *ResourceGroup* is specified, the cluster resource will be created in the *ResourceGroup*. If no *ResourceGroup* is specified, the cluster resource will be created in the first resource group that is not considered a core resource group. It is highly recommended that the *ResourceGroup* parameter be specified when the iSCSI target service is running in a Microsoft cluster environment.

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\Wmi<br/>                                                                         |
| MOF<br/>                      | <dl> <dt>WmiWtProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WtWmiProv.dll</dt> </dl>     |



## See also

<dl> <dt>

[**WT\_Host**](wt-host.md)
</dt> </dl>

 

 





