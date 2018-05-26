---
title: CLUSCTL\_NETINTERFACE\_GET\_COMMON\_PROPERTY\_FMTS control code
description: Reserved for future use.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: bfd17e43-0288-4f5d-835c-41a7e023c79e
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_NETINTERFACE_GET_COMMON_PROPERTY_FMTS control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_NETINTERFACE_GET_COMMON_PROPERTY_FMTS
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CLUSCTL\_NETINTERFACE\_GET\_COMMON\_PROPERTY\_FMTS control code

Reserved for future use. Applications use this control code as a parameter to the [**ClusterNetInterfaceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusternetinterfacecontrol?branch=master) function.


```C++
ClusterNetInterfaceControl( hCluster,                                       // cluster handle
                            hHostNode,                                      // optional node handle
                            CLUSCTL_NETINTERFACE_GET_COMMON_PROPERTY_FMTS,  // this control code
                            NULL,                                           // input buffer (not used)
                            0,                                              // input buffer size (not used)
                            lpOutBuffer,                                    // output buffer: property list
                            cbOutBufferSize,                                // output buffer size (bytes)
                            lpcbBytesReturned );                            // resulting data size (bytes)
```



## Parameters

The following control code function parameter is specific to this control code. For complete parameter descriptions, see [**ClusterNetInterfaceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusternetinterfacecontrol?branch=master).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, points to a [property list](property-lists.md) describing the format of each [common property](network-interface-common-properties.md).

</dd> </dl>

## Return value

[**ClusterNetInterfaceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusternetinterfacecontrol?branch=master) returns the following value.

<dl> <dt>

**ERROR\_INVALID\_FUNCTION**
</dt> <dd>

1

Incorrect function. Always returns **ERROR\_INVALID\_FUNCTION**.

</dd> </dl>

## Remarks

For information on working with property lists, see [Using Property Lists](using-property-lists.md).

ClusAPI.h defines the 32 bits of CLUSCTL\_NETINTERFACE\_GET\_COMMON\_PROPERTY\_FMTS as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component                 | Bit location     | Value                                                    |
|---------------------------|------------------|----------------------------------------------------------|
| Object code<br/>    | 24 31<br/> | **CLUS\_OBJECT\_NETINTERFACE** (0x6)<br/>          |
| Global bit<br/>     | 23<br/>    | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                   |
| Modify bit<br/>     | 22<br/>    | **CLUS\_NO\_MODIFY** (0x0)<br/>                    |
| User bit<br/>       | 21<br/>    | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>                |
| Type bit<br/>       | 20<br/>    | External (0x0)<br/>                                |
| Operation code<br/> | 0 23<br/>  | **CLCTL\_GET\_COMMON\_PROPERTY\_FMTS** (0x65)<br/> |
| Access code<br/>    | 0 1<br/>   | **CLUS\_ACCESS\_READ** (0x1)<br/>                  |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[Network Interface Control Codes](network-interface-control-codes.md)
</dt> <dt>

[**ClusterNetInterfaceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusternetinterfacecontrol?branch=master)
</dt> </dl>

 

 





