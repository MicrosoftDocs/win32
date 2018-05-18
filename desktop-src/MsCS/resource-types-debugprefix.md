---
title: DebugPrefix
description: This property is not supported.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '8d91757d-a65a-49f8-afdb-d6fe19d08923'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["DebugPrefix Failover Cluster ,for resource types", "DebugPrefix Failover Cluster"]
topic_type:
- apiref
api_name:
- DebugPrefix
api_type:
- NA
---

# DebugPrefix

\[This property is no longer available for use as of Windows Server 2012.\]

This property is not supported.

**Windows Server 2008 R2, Windows Server 2008 and Windows Server 2003:  **

Provides the path to a debugger that is used to debug all resources of the type that are running in the [Resource Monitor](resource-monitor.md) for the resource type. The following table summarizes the attributes of the **DebugPrefix** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read/write](read-write-properties.md)                          |
| Structure | [**CLUSPROP\_SZ**](clusprop-sz.md)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

## Remarks

A debugger can be used only if the resource type is running with a separate Resource Monitor. If the debugger is in a directory that is included in the path, the **DebugPrefix** property can be set to a relative path. Otherwise, a full path must be specified.

Setting the **DebugPrefix** property causes -p &lt;process id&gt; to be appended to the end of the debug command, where &lt;process id&gt; represents the process identifier for the Resource Monitor handling the resource type.

The [**CLUSPROP\_SZ\_DECLARE**](clusprop-sz-declare.md) macro creates a [**CLUSPROP\_SZ**](clusprop-sz.md) structure with an array of the correct size.

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
| Minimum supported server<br/> | Windows Server 2003 Enterprise, Windows Server 2003 Datacenter<br/>       |
| End of client support<br/>    | None supported<br/>                                                       |
| End of server support<br/>    | Windows Server 2008 R2 Enterprise, Windows Server 2008 R2 Datacenter<br/> |



## See also

<dl> <dt>

[**CLUSPROP\_SZ**](clusprop-sz.md)
</dt> <dt>

[**CLUSPROP\_SZ\_DECLARE**](clusprop-sz-declare.md)
</dt> </dl>

 

 





