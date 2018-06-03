---
Description: Identifies the time interval for which the license or certificate is valid. It has the following definition.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: e04cd4e5-9be1-4871-993c-3cdfc09d9f83
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: VALIDITYTIME
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# VALIDITYTIME

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

Identifies the time interval for which the license or certificate is valid. It has the following definition.

``` syntax
<!ELEMENT VALIDITYTIME (FROM?, UNTIL?)>

<!ELEMENT FROM (%moment;)>
<!ELEMENT UNTIL (%moment;)>
```

## Remarks

The format of the **%moment** entity is y*yyy-mm-dd*T*hh:mm:ss* where *yyyy* specifies the year, *mm* the month, *dd* the day, *hh* the hour, *mm* the minute, and *ss* the second of issuance in Coordinated Universal Time (UTC).

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

 

 




