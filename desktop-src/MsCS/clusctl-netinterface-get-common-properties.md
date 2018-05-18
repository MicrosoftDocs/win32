---
title: CLUSCTL\_NETINTERFACE\_GET\_COMMON\_PROPERTIES control code
description: Retrieves the read/write common properties for a network interface.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'd83b0eb5-3043-4466-8ed5-2dde96073d49'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CLUSCTL_NETINTERFACE_GET_COMMON_PROPERTIES control code Failover Cluster"]
topic_type:
- apiref
api_name:
- CLUSCTL_NETINTERFACE_GET_COMMON_PROPERTIES
api_location:
- ClusAPI.h
api_type:
- HeaderDef
---

# CLUSCTL\_NETINTERFACE\_GET\_COMMON\_PROPERTIES control code

Retrieves the read/write [common properties](common-properties.md) for a [network interface](network-interfaces.md). Applications use this [control code](about-control-codes.md) as a [**ClusterNetInterfaceControl**](clusternetinterfacecontrol.md) parameter.


```C++
ClusterNetInterfaceControl( 
  hNetInterface,                               // network interface handle
  hHostNode,                                   // optional host node
  CLUSCTL_NETINTERFACE_GET_COMMON_PROPERTIES,  // this control code
  NULL,                                        // input buffer (not used)
  0,                                           // input buffer size (not used)
  lpOutBuffer,                                 // output buffer: property list
  cbOutBufferSize,                             // allocated buffer size (bytes)
  lpcbBytesReturned                            // actual size of resulting data (bytes)
);
```



## Parameters

The following control code function parameter is specific to this control code. For complete parameter descriptions, see [**ClusterNetInterfaceControl**](clusternetinterfacecontrol.md).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, points to a [property list](property-lists.md) containing the specified network interface's read/write [common network interface properties](network-interface-common-properties.md).

</dd> </dl>

## Return value

[**ClusterNetInterfaceControl**](clusternetinterfacecontrol.md) returns one of the following values.

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

The operation completed successfully. The *lpcbBytesReturned* parameter points to the actual size of the returned data.

</dd> <dt>

**ERROR\_MORE\_DATA**
</dt> <dd>

More data is available. The output buffer pointed to by *lpOutBuffer* was not large enough to hold the data resulting from the operation. The *lpcbBytesReturned* parameter points to the size required for the output buffer.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

If any other value is returned, the operation failed. The value of *lpcbBytesReturned* is unreliable.

</dd> </dl>

## Remarks

For information on working with property lists, see [Using Property Lists](using-property-lists.md).

ClusAPI.h defines the 32 bits of CLUSCTL\_NETINTERFACE\_GET\_COMMON\_PROPERTIES as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                                |
|----------------|--------------|------------------------------------------------------|
| Object code    | 24–31        | **CLUS\_OBJECT\_NETINTERFACE** (0x6)<br/>      |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>               |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)<br/>                |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>            |
| Type bit       | 20           | External (0x0)<br/>                            |
| Operation code | 0–23         | **CLCTL\_GET\_COMMON\_PROPERTIES** (0x59)<br/> |
| Access code    | 0–1          | **CLUS\_ACCESS\_READ** (0x1)<br/>              |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[Network Interface Control Codes](network-interface-control-codes.md)
</dt> <dt>

[**ClusterNetInterfaceControl**](clusternetinterfacecontrol.md)
</dt> <dt>

[**Description Property for Network Interfaces**](network-interfaces-description.md)
</dt> </dl>

 

 





