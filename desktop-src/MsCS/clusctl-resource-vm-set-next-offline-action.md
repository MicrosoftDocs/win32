---
title: CLUSCTL\_RESOURCE\_VM\_SET\_NEXT\_OFFLINE\_ACTION control code
description: Specifies the offline action for the next Offline operation on the virtual machine (VM) resource instance.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 525efa3e-6e3c-4dbf-bd06-ff80077b6921
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_VM_SET_NEXT_OFFLINE_ACTION control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_VM_SET_NEXT_OFFLINE_ACTION
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CLUSCTL\_RESOURCE\_VM\_SET\_NEXT\_OFFLINE\_ACTION control code

Specifies the offline action for the next [*Offline*](/windows/previous-versions/ResApi/nc-resapi-poffline_routine?branch=master) operation on the virtual machine (VM) resource instance. This can be used to temporarily change the value of the [**OfflineAction**](virtual-machines-offlineaction.md) property without the overhead of modifying and restoring the resource property. Applications use this control code as a parameter to the [**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master) function, and [resource DLLs](resource-dlls.md) receive the control code as a parameter to the [*ResourceControl*](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master) callback function.


```C++
ClusterResourceControl( hResource,            // resource handle
                        hHostNode,            // optional node handle
                        CLUSCTL_RESOURCE_VM_SET_NEXT_OFFLINE_ACTION,
                        lpInBuffer,           // input buffer: DWORD
                        cbInBufferSize,       // input buffer size (bytes)
                        NULL,                 // output buffer (not used)
                        0,                    // output buffer size (not used)
                        NULL );               // resulting data size (not used)
```



## Parameters

The following control code function parameters are specific to this control code. For complete parameter descriptions, see [**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master).

<dl> <dt>

*lpInBuffer* \[in, optional\]
</dt> <dd>

A pointer to an input buffer containing a **DWORD** with the [**OfflineAction**](virtual-machines-offlineaction.md).

<dt>

<span id="Turn_Off"></span><span id="turn_off"></span><span id="TURN_OFF"></span>

<span id="Turn_Off"></span><span id="turn_off"></span><span id="TURN_OFF"></span>**Turn Off** (0)


</dt> <dd>

The VM is turned off.

</dd> <dt>

<span id="Save"></span><span id="save"></span><span id="SAVE"></span>

<span id="Save"></span><span id="save"></span><span id="SAVE"></span>**Save** (1)


</dt> <dd>

The VM is saved.

</dd> <dt>

<span id="Shutdown"></span><span id="shutdown"></span><span id="SHUTDOWN"></span>

<span id="Shutdown"></span><span id="shutdown"></span><span id="SHUTDOWN"></span>**Shutdown** (2)


</dt> <dd>

The guest operating system running in the VM is shut down. This requires that the guest operating system has the shutdown integration component installed. For more information on the shutdown integration component, see the [**Msvm\_ShutdownComponent**](https://msdn.microsoft.com/library/cc136893) and [**Msvm\_ShutdownComponentSettingData**](https://msdn.microsoft.com/library/cc136894) classes.

</dd> <dt>

<span id="Shutdown__Forced_"></span><span id="shutdown__forced_"></span><span id="SHUTDOWN__FORCED_"></span>

<span id="Shutdown__Forced_"></span><span id="shutdown__forced_"></span><span id="SHUTDOWN__FORCED_"></span>**Shutdown (Forced)** (3)


</dt> <dd>

The Windows guest operating system running in the VM is shut down forcibly. For more information, see the **EWX\_FORCE** option flag on the [**ExitWindowsEx**](https://msdn.microsoft.com/library/windows/desktop/aa376868) function page. This requires that the guest operating system has the shutdown integration component installed.

</dd> </dl> </dd> <dt>

*cbInBufferSize* \[in\]
</dt> <dd>

The allocated size (in bytes) of the input buffer.

</dd> </dl>

## Return value

[**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master) returns one of the following values.

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The operation was successful.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

The operation failed.

</dd> </dl>

## Remarks

The 32 bits of CLUSCTL\_RESOURCE\_VM\_SET\_NEXT\_OFFLINE\_ACTION (0x01600014) are defined as follows.



| Component                 | Bit location     | Value                                       |
|---------------------------|------------------|---------------------------------------------|
| Object code<br/>    | 24 31<br/> | **CLUS\_OBJECT\_RESOURCE** (0x1)<br/> |
| Global bit<br/>     | 23<br/>    | **CLUS\_NOT\_GLOBAL** (0x0)<br/>      |
| Modify bit<br/>     | 22<br/>    | **CLUS\_MODIFY** (0x1)<br/>           |
| User bit<br/>       | 21<br/>    | **CLCTL\_USER\_BASE** (0x200000)<br/> |
| Type bit<br/>       | 20<br/>    | External (0x0)<br/>                   |
| Operation code<br/> | 0 23<br/>  | (0x14)<br/>                           |
| Access code<br/>    | 0 1<br/>   | **CLUS\_ACCESS\_ANY** (0x0)<br/>      |



 

For more information, see [Control Code Architecture](control-code-architecture.md).

## Requirements



|                                     |                                                                                 |
|-------------------------------------|---------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                       |
| Minimum supported server<br/> | Windows Server 2008 R2 Datacenter, Windows Server 2008 R2 Enterprise<br/> |



## See also

<dl> <dt>

[External Resource Control Codes](external-resource-control-codes.md)
</dt> <dt>

[**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master)
</dt> <dt>

[*ResourceControl*](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master)
</dt> <dt>

[**OfflineAction**](virtual-machines-offlineaction.md)
</dt> </dl>

 

 





