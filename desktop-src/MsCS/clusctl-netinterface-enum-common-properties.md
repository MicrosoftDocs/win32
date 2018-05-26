---
title: CLUSCTL\_NETINTERFACE\_ENUM\_COMMON\_PROPERTIES control code
description: Retrieves a list of the read/write network interface common property names.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: cedac89a-121d-4d74-ac06-4723d292f3e7
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_NETINTERFACE_ENUM_COMMON_PROPERTIES control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_NETINTERFACE_ENUM_COMMON_PROPERTIES
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CLUSCTL\_NETINTERFACE\_ENUM\_COMMON\_PROPERTIES control code

Retrieves a list of the read/write [network interface](network-interfaces.md) [common property](common-properties.md) names. Applications use this [control code](about-control-codes.md) as a [**ClusterNetInterfaceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusternetinterfacecontrol?branch=master) parameter.


```C++
ClusterNetInterfaceControl( 
  hNetInterface,                                // network interface handle
  hHostNode,                                    // optional host node
  CLUSCTL_NETINTERFACE_ENUM_COMMON_PROPERTIES,  // this control code
  NULL,                                         // input buffer (not used)
  0,                                            // input buffer size (not used)
  lpOutBuffer,                                  // output buffer: array of strings
  cbOutBufferSize,                              // allocated buffer size (bytes)
  lpcbBytesReturned                             // actual size of resulting data (bytes)
);
```



## Parameters

The following control code function parameter is specific to this control code. For complete parameter descriptions, see [**ClusterNetInterfaceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusternetinterfacecontrol?branch=master).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, contains an array of null-terminated Unicode strings with an additional **NULL** terminator appended to the last string. Each string in the array contains the name of a read/write [network interface common property](network-interface-common-properties.md).

</dd> </dl>

## Return value

[**ClusterNetInterfaceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusternetinterfacecontrol?branch=master) returns one of the following values.

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The operation completed successfully. The *lpcbBytesReturned* parameter points to the actual size of the returned data.

</dd> <dt>

**ERROR\_MORE\_DATA**
</dt> <dd>

234 (0xEA)

More data is available. The output buffer pointed to by *lpOutBuffer* was not large enough to hold the data resulting from the operation. The *lpcbBytesReturned* parameter points to the size required for the output buffer.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

If any other value is returned, then the operation failed. The value of *lpcbBytesReturned* is unreliable.

</dd> </dl>

## Remarks

The CLUSCTL\_NETINTERFACE\_ENUM\_COMMON\_PROPERTIES control code returns only property names, not property values. To retrieve values for common network interface properties, use [CLUSCTL\_NETINTERFACE\_GET\_COMMON\_PROPERTIES](clusctl-netinterface-get-common-properties.md) and [CLUSCTL\_NETINTERFACE\_GET\_RO\_COMMON\_PROPERTIES](clusctl-netinterface-get-ro-common-properties.md).

ClusAPI.h defines the 32 bits of CLUSCTL\_NETINTERFACE\_ENUM\_COMMON\_PROPERTIES as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                                 |
|----------------|--------------|-------------------------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_NETINTERFACE** (0x6)<br/>       |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)<br/>                 |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>             |
| Type bit       | 20           | External (0x0)<br/>                             |
| Operation code | 0 23         | **CLCTL\_ENUM\_COMMON\_PROPERTIES** (0x51)<br/> |
| Access code    | 0 1          | **CLUS\_ACCESS\_READ** (0x1)<br/>               |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[Network Interface Control Codes](network-interface-control-codes.md)
</dt> <dt>

[CLUSCTL\_NETINTERFACE\_GET\_COMMON\_PROPERTIES](clusctl-netinterface-get-common-properties.md)
</dt> <dt>

[CLUSCTL\_NETINTERFACE\_GET\_RO\_COMMON\_PROPERTIES](clusctl-netinterface-get-ro-common-properties.md)
</dt> <dt>

[**ClusterNetInterfaceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusternetinterfacecontrol?branch=master)
</dt> </dl>

 

 





