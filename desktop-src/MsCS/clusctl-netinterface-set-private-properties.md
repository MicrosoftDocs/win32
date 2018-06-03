---
title: CLUSCTL\_NETINTERFACE\_SET\_PRIVATE\_PROPERTIES control code
description: Updates the read/write private properties for a network interface.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0698ee19-d560-4e4c-a7ce-6fcf4ff061ae
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_NETINTERFACE_SET_PRIVATE_PROPERTIES control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_NETINTERFACE_SET_PRIVATE_PROPERTIES
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CLUSCTL\_NETINTERFACE\_SET\_PRIVATE\_PROPERTIES control code

Updates the read/write [private properties](private-properties.md) for a [network interface](network-interfaces.md). Applications use this [control code](about-control-codes.md) as a [**ClusterNetInterfaceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusternetinterfacecontrol) parameter.


```C++
ClusterNetInterfaceControl( hNetInterface,                                // network interface handle
                            hHostNode,                                    // optional host node
                            CLUSCTL_NETINTERFACE_SET_PRIVATE_PROPERTIES,  // this control code
                            lpInBuffer,                                   // input buffer: property list
                            cbInBufferSize,                               // allocated buffer size (bytes)
                            NULL,                                         // output buffer (not used)
                            0,                                            // output buffer size (not used)
                            NULL );                                       // actual size of resulting data (not used)
```



## Parameters

The following control code function parameters are specific to this control code. For complete parameter descriptions, see [**ClusterNetInterfaceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusternetinterfacecontrol).

<dl> <dt>

*lpInBuffer* 
</dt> <dd>

Pass a pointer to a [property list](property-lists.md) containing one or more read/write network interface private properties. Any properties that do not already exist will be created.

</dd> </dl>

## Return value

[**ClusterNetInterfaceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusternetinterfacecontrol) returns one of the following values.

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The operation completed successfully. The property list is correctly formatted and contains valid data values.

</dd> <dt>

**ERROR\_INSUFFICIENT\_BUFFER**
</dt> <dd>

122 (0x7A)

The data area passed to a system call is too small. The actual size of the property list buffer as determined by the [Cluster service](cluster-service.md) is larger than the size specified in the *cbInBufferSize* parameter.

</dd> <dt>

**ERROR\_INVALID\_DATA**
</dt> <dd>

13 (0xD)

The data is invalid. The property list is either formatted incorrectly or contains invalid data, such as an out-of-range value.

</dd> <dt>

**ERROR\_INVALID\_PARAMETER**
</dt> <dd>

87 (0x57)

The parameter is incorrect. The property list is not formatted correctly.

</dd> <dt>

**RPC\_X\_BAD\_STUB\_DATA**
</dt> <dd>

1783 (0x6F7)

The stub received bad data. The *lpInBuffer* parameter is **NULL**.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

If any other value is returned, then the operation failed.

</dd> </dl>

## Remarks

By default, failover clusters do not define any private properties for network interfaces. You can use the CLUSCTL\_NETINTERFACE\_SET\_PRIVATE\_PROPERTIES control code to define private properties for a network interface.

ClusAPI.h defines the 32 bits of CLUSCTL\_NETINTERFACE\_SET\_PRIVATE\_PROPERTIES as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component                 | Bit location     | Value                                                     |
|---------------------------|------------------|-----------------------------------------------------------|
| Object code<br/>    | 24 31<br/> | **CLUS\_OBJECT\_NETINTERFACE** (0x6)<br/>           |
| Global bit<br/>     | 23<br/>    | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                    |
| Modify bit<br/>     | 22<br/>    | **CLUS\_MODIFY** (0x1)<br/>                         |
| User bit<br/>       | 21<br/>    | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>                 |
| Type bit<br/>       | 20<br/>    | External (0x0)<br/>                                 |
| Operation code<br/> | 0 23<br/>  | **CLCTL\_SET\_PRIVATE\_PROPERTIES** (0x400086)<br/> |
| Access code<br/>    | 0 1<br/>   | **CLUS\_ACCESS\_WRITE** (0x2)<br/>                  |



 

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

[**ClusterNetInterfaceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusternetinterfacecontrol)
</dt> </dl>

 

 





