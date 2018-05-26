---
Description: Contains the date and time at which the XrML license or certificate was issued. It has the following definition.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 260991d8-b8dd-42e9-9843-c43c43f8cd41
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ISSUEDTIME
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ISSUEDTIME

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

Contains the date and time at which the XrML license or certificate was issued. It has the following definition.

``` syntax
<!ELEMENT ISSUEDTIME (%moment;)>

<!-- The format is yyyy-mm-ddThh:mm:ss; e.g. 2000-01-27T15:30 -->
<!ENTITY % moment "#PCDATA" >
```

## Remarks

The format of the **%moment** entity is y*yyy-mm-dd*T*hh:mm:ss* where *yyyy* specifies the year, *mm* the month, *dd* the day, *hh* the hour, *mm* the minute, and *ss* the second of issuance in Coordinated Universal Time (UTC). This is shown by the following example.


```XML
<BODY type="LICENSE" version="3.0">
  <ISSUEDTIME>20030122T21:59</ISSUEDTIME>
    .
    .
    .
</BODY>
```



## Requirements



|                    |                                                           |
|--------------------|-----------------------------------------------------------|
| Product<br/> | Rights Management Services client 1.0 or later<br/> |



## See also

<dl> <dt>

[**BODY**](body.md)
</dt> <dt>

[XrML Elements](xrml-elements.md)
</dt> </dl>

 

 




