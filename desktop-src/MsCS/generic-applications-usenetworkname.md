---
title: UseNetworkName
description: Affects the outcome of a call to the GetComputerName function.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '3ef0eb0b-1472-450d-aa08-6622a7475793'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["UseNetworkName Failover Cluster ,for generic applications", "UseNetworkName Failover Cluster"]
topic_type:
- apiref
api_name:
- UseNetworkName
api_type:
- NA
---

# UseNetworkName

\[The **UseNetworkName** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Affects the outcome of a call to the [**GetComputerName**](https://msdn.microsoft.com/library/windows/desktop/ms724295) function.**UseNetworkName** is a property of a [Generic Application](generic-application.md) resource. The following table summarizes the attributes of the **UseNetworkName** property.



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

When an application being managed as a [Generic Application](generic-application.md) resource calls [**GetComputerName**](https://msdn.microsoft.com/library/windows/desktop/ms724295), the **UseNetworkName** property determines what kind of data is returned as follows.



| UseNetworkName value | Name returned by GetComputerName                                                                                                                                                 |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **TRUE**             | The name of the network, as stored in the [**Name**](network-names-name.md) private property of the [Network Name](network-name.md) resource on which the application depends. |
| **FALSE**            | The name of the [node](nodes.md) currently running the application.                                                                                                             |



 

## Examples

The property value portion of a [property list](property-lists.md) entry for **UseNetworkName** can be set with the following example code.


```C++
DWORD          UseNetworkNameData = TRUE;
CLUSPROP_DWORD UseNetworkNameValue;

UseNetworkNameValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
UseNetworkNameValue.cbLength  = sizeof(DWORD);
UseNetworkNameValue.dw        = UseNetworkNameData;
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
</dt> <dt>

[**GetComputerName**](https://msdn.microsoft.com/library/windows/desktop/ms724295)
</dt> <dt>

[**Name**](network-names-name.md)
</dt> </dl>

 

 





