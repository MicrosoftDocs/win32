---
title: InteractWithDesktop
description: Specifies whether the generic application can provide a user interface, on the desktop, that can be used by any person logged on to the node on which the resource is online.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'd29ebbd4-9c15-46fa-ad86-8b49034f8787'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["InteractWithDesktop Failover Cluster ,for generic applications", "InteractWithDesktop Failover Cluster"]
topic_type:
- apiref
api_name:
- InteractWithDesktop
api_type:
- NA
---

# InteractWithDesktop

\[The **InteractWithDesktop** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Specifies whether the [generic application](generic-application.md) can provide a user interface, on the desktop, that can be used by any person logged on to the [node](nodes.md) on which the [resource](resources.md) is online. The following table summarizes the attributes of the **InteractWithDesktop** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Status    | Optional                                  |
| Structure | [**CLUSPROP\_DWORD**](clusprop-dword.md) |
| Minimum   | **FALSE**                                 |
| Maximum   | **TRUE**                                  |
| Default   | **FALSE**                                 |



 

## Remarks

The data for the **InteractWithDesktop** property can be set to **TRUE** or **FALSE**. Setting it to **TRUE** allows the application to display windows on the desktop. The application has read and write access to its own windows but no access to the rest of the desktop.

Setting **InteractWithDesktop** to **FALSE** causes the application to be inaccessible from either the desktop or the toolbar.

## Examples

The property value portion of a [property list](property-lists.md) entry for **InteractWithDesktop** can be set with the following example code.


```C++
DWORD          InteractWithDesktopData = TRUE;
CLUSPROP_DWORD InteractWithDesktopValue;

InteractWithDesktopValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
InteractWithDesktopValue.cbLength  = sizeof(DWORD);
InteractWithDesktopValue.dw        = InteractWithDesktopData;
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2003 Enterprise, Windows Server 2003 Datacenter<br/> |
| End of server support<br/>    | Windows Server 2003 Datacenter, Windows Server 2003 Enterprise<br/> |



## See also

<dl> <dt>

[Generic Application Private Properties](generic-application-private-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](clusprop-dword.md)
</dt> </dl>

 

 





