---
Description: Contains optional data that can be understood by the application that processes the Active Directory Rights Management Services (AD RMS) certificate or license. This element has the following definition.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 7d0daa59-1c57-4681-ad20-b3b175e47cd8
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: AUTHENTICATEDDATA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AUTHENTICATEDDATA

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

Contains optional data that can be understood by the application that processes the Active Directory Rights Management Services (AD RMS) certificate or license. This element has the following definition.

``` syntax
<!ELEMENT AUTHENTICATEDDATA (#PCDATA)>
<!ATTLIST AUTHENTICATEDDATA
  size CDATA #REQUIRED
  name CDATA #REQUIRED
  id CDATA #IMPLIED>
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

 

 




