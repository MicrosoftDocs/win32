---
Description: Identifies the Active Directory Rights Management Services (AD RMS) license or certificate by using the generic OBJECT element. This element has the following definition.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: fcb2a9b8-5c48-4e79-a177-bfb58f53a196
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: DESCRIPTOR
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DESCRIPTOR

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

Identifies the Active Directory Rights Management Services (AD RMS) license or certificate by using the generic [**OBJECT**](object.md) element. This element has the following definition.

``` syntax
<!ELEMENT DESCRIPTOR (OBJECT)>
<!ATTLIST DESCRIPTOR
  parent-id CDATA #IMPLIED >
```

## Remarks

The **parent-id** attribute contains a reference to another XrML document, if any, with which the current document is associated.

## Examples

The following example shows a machine certificate identified by using a GUID.


```XML
<DESCRIPTOR>
  <OBJECT type="Machine-Certificate">
    <ID type="MS-GUID">{958E4BE1-6B28-4C3D-9DEC-EA5B36169085}</ID>
    <NAME>Microsoft Machine-Certificate</NAME>
  </OBJECT>
</DESCRIPTOR>
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

 

 




