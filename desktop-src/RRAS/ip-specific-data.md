---
title: IP_SPECIFIC_DATA structure (Rtm.h)
description: The IP\_SPECIFIC DATA structure contains IP-specific data.
ms.assetid: 68f2f4cc-141b-4f22-94ac-cc72e8dcca0a
keywords:
- IP_SPECIFIC_DATA structure RAS
- PIP_SPECIFIC_DATA structure pointer RAS
topic_type:
- apiref
api_name:
- IP_SPECIFIC_DATA
api_location:
- Rtm.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# IP\_SPECIFIC\_DATA structure

\[This API has been superseded by the [Routing Table Manager Version 2](about-routing-table-manager-version-2.md) API and will not be available beyond Windows Server 2003. Applications should use the Routing Table Manager Version 2 API.\]

The **IP\_SPECIFIC DATA** structure contains IP-specific data.

## Syntax


```C++
typedef struct _IP_SPECIFIC_DATA {
  DWORD FSD_Type;
  DWORD FSD_Policy;
  DWORD FSD_NextHopAS;
  DWORD FSD_Priority;
  DWORD FSD_Metric;
  DWORD FSD_Metric1;
  DWORD FSD_Metric2;
  DWORD FSD_Metric3;
  DWORD FSD_Metric4;
  DWORD FSD_Metric5;
  DWORD FSD_Flags;
} IP_SPECIFIC_DATA, *PIP_SPECIFIC_DATA;
```



## Members

<dl> <dt>

**FSD\_Type**
</dt> <dd>

Specifies the route type as defined in [RFC 1354](routing-protocols-request-for-comments.md). The following table shows the possible values for this member.



| Member                                                                                               | Meaning                                                                                                                                                                                                                                                                           |
|------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="1"></span><dl> <dt>**1**</dt> </dl> | The route type is not specified. The type is different from those listed here.<br/>                                                                                                                                                                                         |
| <span id="2"></span><dl> <dt>**2**</dt> </dl> | The route is invalid. Normally, this value is used to invalidate a route. However, since invalidation is not supported by the routing table manager, the route is still considered in best-route computations. Therefore, routing protocols should not use this value.<br/> |
| <span id="3"></span><dl> <dt>**3**</dt> </dl> | The route is a local route, that is, the next hop is the final destination.<br/>                                                                                                                                                                                            |
| <span id="4"></span><dl> <dt>**4**</dt> </dl> | The route is a remote route, that is, the next hop is not the final destination.<br/>                                                                                                                                                                                       |



 

</dd> <dt>

**FSD\_Policy**
</dt> <dd>

Specifies the set of conditions that would cause the selection of a multi-path route. This member is typically in IP TOS format. For more information, see [RFC 1354](routing-protocols-request-for-comments.md).

</dd> <dt>

**FSD\_NextHopAS**
</dt> <dd>

Specifies the autonomous system number of the next hop.

</dd> <dt>

**FSD\_Priority**
</dt> <dd>

Specifies a metric value. The routing table manager uses this value to compare this route entry to route entries obtained from other routing protocols. The value of this member is set by the routing table manager.

</dd> <dt>

**FSD\_Metric**
</dt> <dd>

Specifies a metric value. The routing table manager uses this value to compare this route entry to other route entries obtained from the same routing protocol. The value of this member is set by the routing protocol.

</dd> <dt>

**FSD\_Metric1**
</dt> <dd>

Specifies a routing-protocol-specific metric value. This metric value is documented in [RFC 1354](routing-protocols-request-for-comments.md).

</dd> <dt>

**FSD\_Metric2**
</dt> <dd>

Specifies a routing-protocol-specific metric value. This metric value is documented in [RFC 1354](routing-protocols-request-for-comments.md).

</dd> <dt>

**FSD\_Metric3**
</dt> <dd>

Specifies a routing-protocol-specific metric value. This metric value is documented in [RFC 1354](routing-protocols-request-for-comments.md).

</dd> <dt>

**FSD\_Metric4**
</dt> <dd>

Specifies a routing-protocol-specific metric value. This metric value is documented in [RFC 1354](routing-protocols-request-for-comments.md).

</dd> <dt>

**FSD\_Metric5**
</dt> <dd>

Specifies a routing-protocol-specific metric value. This metric value is documented in [RFC 1354](routing-protocols-request-for-comments.md).

</dd> <dt>

**FSD\_Flags**
</dt> <dd>

Specifies whether the route is valid. The routing protocol should first clear these flags, then set the route as either valid or invalid. The routing protocol should use the macros **ClearRouteFlags()**, **SetRouteValid()**, and **ClearRouteValid()** to perform these operations. These macros are defined in Rtm.h.

</dd> </dl>

## Remarks

The routing table manager uses the **FSD\_Priority** and **FSD\_Metric** members to compute the best route to a particular destination network.

The **FSD\_Metric\[1-5\]** members are for MIB II conformance. MIB II agents display only these metric values. They do not display the **FSD\_Metric** metric value. To have the **FSD\_Metric** displayed, the routing protocol should also store the value in one of the **FSD\_Metric\[1-5\]** members.

The routing table manager does not use the metric values in the **FSD\_Metric\[1-5\]** members when computing the best route to a destination network. Therefore, the routing protocol should ensure that the **FSD\_Metric** member has an appropriate metric value.

A routing protocol could use the **FSD\_Flags** to mark a route as invalid, if the route should not be used by other routing protocols.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                        |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| End of server support<br/>    | Windows Server 2003<br/>                                                   |
| Header<br/>                   | <dl> <dt>Rtm.h</dt> </dl> |



## See also

<dl> <dt>

[Routing Table Manager Version 1 Reference](routing-table-manager-version-1-reference.md)
</dt> <dt>

[Routing Table Manager Version 1 Structures](routing-table-manager-version-1-structures.md)
</dt> <dt>

[**RTM\_IP\_ROUTE**](rtm-ip-route.md)
</dt> </dl>

 

 





