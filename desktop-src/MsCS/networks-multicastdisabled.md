---
title: MulticastDisabled
description: This property is not supported.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '60bf04e7-a6f4-4abe-8439-81ac67bbab8c'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["MulticastDisabled Failover Cluster ,for networks", "MulticastDisabled Failover Cluster"]
topic_type:
- apiref
api_name:
- MulticastDisabled
api_type:
- NA
---

# MulticastDisabled

\[The **MulticastDisabled** property is no longer available for use as of Windows Server 2012.\]

This property is not supported.

**Windows Server 2003:  **

Enables or disables [*heartbeat*](h-gly.md#-wolf-heartbeat-gly) multicasting for a [network](networks.md). The following table summarizes the attributes of the **MulticastDisabled** property.



| Attribute | Value                                          |
|-----------|------------------------------------------------|
| Data type | **DWORD**                                      |
| Access    | [Read/write](read-write-properties.md)        |
| Status    | Optional                                       |
| Structure | [**CLUSPROP\_DWORD**](clusprop-dword.md)      |
| Minimum   | 0 (multicast enabled)                          |
| Maximum   | any nonzero to 0xFFFFFFFF (multicast disabled) |
| Default   | 0 (multicast enabled)                          |



 

## Remarks

A network's **MulticastDisabled** property overrides the cluster's **MulticastDisabled** property for that particular network.

## Examples

The property value portion of a [property list](property-lists.md) entry for **MulticastDisabled** can be set with the following example code.


```C++
DWORD          MulticastDisabledData = 0;
CLUSPROP_DWORD MulticastDisabledValue;

MulticastDisabledValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
MulticastDisabledValue.cbLength  = sizeof(DWORD);
MulticastDisabledValue.dw        = MulticastDisabledData;
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2003 Datacenter, Windows Server 2003 Enterprise<br/> |
| End of server support<br/>    | Windows Server 2003 Datacenter, Windows Server 2003 Enterprise<br/> |



## See also

<dl> <dt>

[**MulticastAddress**](networks-multicastaddress.md)
</dt> <dt>

[**MulticastAddressRangeLower**](networks-multicastaddressrangelower.md)
</dt> <dt>

[**MulticastAddressRangeUpper**](networks-multicastaddressrangeupper.md)
</dt> <dt>

[**MulticastConfigType**](networks-multicastconfigtype.md)
</dt> </dl>

 

 





