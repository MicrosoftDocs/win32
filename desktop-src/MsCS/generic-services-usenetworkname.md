---
title: UseNetworkName
description: Affects the outcome of a call to the GetComputerName function.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a1c78cde-2e32-4cb2-8d29-c0fd23d64b28
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- UseNetworkName Failover Cluster ,for generic services
- UseNetworkName Failover Cluster
topic_type:
- apiref
api_name:
- UseNetworkName
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# UseNetworkName

Affects the outcome of a call to the [**GetComputerName**](https://msdn.microsoft.com/library/windows/desktop/ms724295) function.**UseNetworkName** is a property of a [Generic Service](generic-service.md) resource. The following table summarizes the attributes of the **UseNetworkName** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Status    | Optional                                  |
| Structure | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master) |
| Minimum   | **FALSE**                                 |
| Maximum   | **TRUE**                                  |
| Default   | **FALSE**                                 |



 

## Remarks

When an application being managed as a [Generic Service](generic-service.md) resource calls [**GetComputerName**](https://msdn.microsoft.com/library/windows/desktop/ms724295), the **UseNetworkName** property determines what kind of data is returned as follows.



| UseNetworkName value | Name returned by GetComputerName                                                                                                                                                 |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **TRUE**             | The name of the network, as stored in the [**Name**](network-names-name.md) private property of the [Network Name](network-name.md) resource on which the application depends. |
| **FALSE**            | The name of the [node](nodes.md) currently running the service.                                                                                                                 |



 

## Examples

The property value portion of a [property list](property-lists.md) entry for **UseNetworkName** can be set with the following example code.


```C++
DWORD UseNetworkNameData = TRUE;
CLUSPROP_DWORD UseNetworkNameValue;

UseNetworkNameValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
UseNetworkNameValue.cbLength = sizeof(DWORD);
UseNetworkNameValue.dw = UseNetworkNameData;
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



## See also

<dl> <dt>

[Generic Service Private Properties](generic-service-private-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> <dt>

[**GetComputerName**](https://msdn.microsoft.com/library/windows/desktop/ms724295)
</dt> <dt>

[**Name**](network-names-name.md)
</dt> </dl>

 

 





