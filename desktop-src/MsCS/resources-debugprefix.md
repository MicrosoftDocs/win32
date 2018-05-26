---
title: DebugPrefix
description: This property is not supported.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4ac7a2ab-3296-4a5d-825e-fa4cf82089e9
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- DebugPrefix Failover Cluster ,for resources
- DebugPrefix Failover Cluster
topic_type:
- apiref
api_name:
- DebugPrefix
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DebugPrefix

\[This property is no longer available for use as of Windows Server 2012.\]

This property is not supported.

**Windows Server 2008 R2, Windows Server 2008 and Windows Server 2003:  **

Specifies the path to the debugger used to debug the [resource](resources.md). The following table summarizes the attributes of the **DebugPrefix** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read/write](read-write-properties.md)                          |
| Structure | [**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

## Remarks

To use the **DebugPrefix** property, a resource must run in a separate [Resource Monitor](resource-monitor.md). The debugger specified by the **DebugPrefix** property is attached to the Resource Monitor. If the debugger is in a directory that is included in the path, **DebugPrefix** can be set to a relative path. Otherwise, a full path must be specified.

Setting the **DebugPrefix** property causes "-p &lt;process id&gt;" to be appended to the end of the debug command, where &lt;process id&gt; represents the process identifier for the Resource Monitor handling the resource.

For more information about debugging a resource, see [Debugging a Resource DLL](debugging-resource-dlls.md).

The [**CLUSPROP\_SZ\_DECLARE**](/windows/previous-versions/ClusAPI/nf-clusapi-clusprop_sz_declare?branch=master) macro creates a [**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master) structure with an array of the correct size.

## Examples

The property value portion of a [property list](property-lists.md) entry for **DebugPrefix** can be set with the following example code:


```C++
WCHAR szDebugPrefixData[] = L"C:\\Bin\\Debug.exe";
CLUSPROP_SZ_DECLARE( DebugPrefixValue, 
                     sizeof( szDebugPrefixData ) / sizeof( WCHAR ) );
DebugPrefixValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_SZ;
DebugPrefixValue.cbLength = sizeof( szDebugPrefixData );
StringCbCopy( DebugPrefixValue.sz, 
              DebugPrefixValue.cbLength, 
              szDebugPrefixData );
```



## Requirements



|                                     |                                                                                 |
|-------------------------------------|---------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                       |
| Minimum supported server<br/> | Windows Server 2003 Enterprise, Windows Server 2003 Datacenter<br/>       |
| End of client support<br/>    | None supported<br/>                                                       |
| End of server support<br/>    | Windows Server 2008 R2 Enterprise, Windows Server 2008 R2 Datacenter<br/> |



## See also

<dl> <dt>

[**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> <dt>

[**CLUSPROP\_SZ\_DECLARE**](/windows/previous-versions/ClusAPI/nf-clusapi-clusprop_sz_declare?branch=master)
</dt> <dt>

[**DebugPrefix**](resource-types-debugprefix.md)
</dt> </dl>

 

 





