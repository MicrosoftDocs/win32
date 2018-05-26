---
title: UseNetworkName
description: Affects the outcome of a call to the GetComputerName function.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 694fd56f-6e06-456f-8912-180f6ddf74a6
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- UseNetworkName Failover Cluster ,for generic scripts
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

\[This property is no longer available for use as of Windows Server 2012.\]

This property is not supported.

**Windows Server 2008 R2 and Windows Server 2008:  **

Affects the outcome of a call to the [**GetComputerName**](https://msdn.microsoft.com/library/windows/desktop/ms724295) function.**UseNetworkName** is a property of a [generic script](generic-script.md) resource. The following table summarizes the attributes of the **UseNetworkName** property.



| Attribute            | Value                                                |
|----------------------|------------------------------------------------------|
| Data type<br/> | **DWORD**<br/>                                 |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>   |
| Status<br/>    | Optional<br/>                                  |
| Structure<br/> | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master)<br/> |
| Minimum<br/>   | **FALSE** (0)<br/>                             |
| Maximum<br/>   | **TRUE** (1)<br/>                              |
| Default<br/>   | **FALSE** (0)<br/>                             |



 

## Remarks

When an application being managed as a [generic script](generic-script.md) resource calls [**GetComputerName**](https://msdn.microsoft.com/library/windows/desktop/ms724295), the **UseNetworkName** property determines what kind of data is returned as follows.



| **UseNetworkName** value | Name returned by [**GetComputerName**](https://msdn.microsoft.com/library/windows/desktop/ms724295)                                                                                                                                |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **TRUE** (1)<br/>  | The name of the network, as stored in the [**Name**](network-names-name.md) private property of the [Network Name](network-name.md) resource on which the application depends.<br/> |
| **FALSE** (0)<br/> | The name of the [node](nodes.md) currently running the application.<br/>                                                                                                             |



 

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



|                                     |                                                                                 |
|-------------------------------------|---------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                       |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/>       |
| End of client support<br/>    | None supported<br/>                                                       |
| End of server support<br/>    | Windows Server 2008 R2 Datacenter, Windows Server 2008 R2 Enterprise<br/> |



## See also

<dl> <dt>

[Generic Script Private Properties](generic-script-private-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> <dt>

[**GetComputerName**](https://msdn.microsoft.com/library/windows/desktop/ms724295)
</dt> <dt>

[**Name**](network-names-name.md)
</dt> </dl>

 

 





