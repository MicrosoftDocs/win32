---
title: CommandLine
description: Describes the command-line used to invoke the script when it is started.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1f7dcfc0-3d74-4adb-9faa-275ccf6d26d6
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CommandLine Failover Cluster ,for generic scripts
- CommandLine Failover Cluster
topic_type:
- apiref
api_name:
- CommandLine
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CommandLine

\[This property is no longer available for use as of Windows Server 2012.\]

This property is not supported.

**Windows Server 2008 R2 and Windows Server 2008:  **

Describes the command-line used to invoke the script when it is started. The following table summarizes the attributes of the **CommandLine** property.



| Attribute            | Value                                                                     |
|----------------------|---------------------------------------------------------------------------|
| Data type<br/> | Null-terminated Unicode string<br/>                                 |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>                        |
| Status<br/>    | Required<br/>                                                       |
| Structure<br/> | [**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)<br/>                            |
| Minimum<br/>   | **NULL**<br/>                                                       |
| Maximum<br/>   | None (but see [Maximum String Size](maximum-string-size.md)).<br/> |
| Default<br/>   | **NULL**<br/>                                                       |



 

## Remarks

The [**CLUSPROP\_SZ\_DECLARE**](/windows/previous-versions/ClusAPI/nf-clusapi-clusprop_sz_declare?branch=master) macro creates a [**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master) structure with an array of the correct size.

## Examples

The property value portion of a [property list](property-lists.md) entry for **CommandLine** can be set with the following example code.


```C++
WCHAR                szCommandLineData[] = L"C:\\Bin\\MyApp.exe";
CLUSPROP_SZ_DECLARE( CommandLineValue, sizeof( szCommandLineData ) / sizeof( WCHAR ) );

CommandLineValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_SZ;
CommandLineValue.cbLength  = sizeof( szCommandLineData );
StringCbCopy( CommandLineValue.sz, CommandLineValue.cbLength, szCommandLineData );
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

[**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> <dt>

[**CLUSPROP\_SZ\_DECLARE**](/windows/previous-versions/ClusAPI/nf-clusapi-clusprop_sz_declare?branch=master)
</dt> </dl>

 

 





