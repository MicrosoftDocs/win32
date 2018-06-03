---
title: CommandLine
description: Describes the command-line used to invoke the application when it is started.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3091ff6f-1430-4b06-9d83-b2a98c3a8e22
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CommandLine Failover Cluster ,for generic applications
- CommandLine Failover Cluster
topic_type:
- apiref
api_name:
- CommandLine
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CommandLine

\[The [**CurrentDirectory**](generic-applications-currentdirectory.md) property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Describes the command-line used to invoke the application when it is started. The following table summarizes the attributes of the **CommandLine** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read/write](read-write-properties.md)                          |
| Status    | Required                                                         |
| Structure | [**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

## Remarks

The [**CLUSPROP\_SZ\_DECLARE**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusprop_sz_declare) macro creates a [**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/) structure with an array of the correct size.

## Examples

The property value portion of a [property list](property-lists.md) entry for **CommandLine** can be set with the following example code.


```C++
WCHAR                szCommandLineData[] = L"C:\\Bin\\MyApp.exe";
CLUSPROP_SZ_DECLARE( CommandLineValue, 
                     sizeof( szCommandLineData ) / sizeof( WCHAR ) );

CommandLineValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_SZ;
CommandLineValue.cbLength  = sizeof( szCommandLineData );
StringCbCopy( CommandLineValue.sz, 
              CommandLineValue.cbLength, 
              szCommandLineData );
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2003 Enterprise, Windows Server 2003 Datacenter<br/> |
| End of server support<br/>    | Windows Server 2003 Datacenter, Windows Server 2003 Enterprise<br/> |



## See also

<dl> <dt>

[Generic Application Private Properties](generic-application-private-properties.md)
</dt> <dt>

[**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/)
</dt> <dt>

[**CLUSPROP\_SZ\_DECLARE**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusprop_sz_declare)
</dt> </dl>

 

 





