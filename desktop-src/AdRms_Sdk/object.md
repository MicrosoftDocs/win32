---
Description: Describes a generic object. This element has the following definition.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: f813609d-8a09-4c67-bff4-4fee48fb3dbd
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: OBJECT
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# OBJECT

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

Describes a generic object. This element has the following definition.

``` syntax
<!ELEMENT OBJECT (ID, 
                  NAME?, 
                  ADDRESS*, 
                  DESCRIPTION?, 
                  VERSIONSPAN?)>
<!ATTLIST OBJECT
  type CDATA #IMPLIED
  version CDATA #IMPLIED>

<!-- Object ID -->
<!ELEMENT ID (#PCDATA)>
<!ATTLIST ID
  type CDATA #REQUIRED
  version CDATA #IMPLIED
  anonymity-level CDATA #IMPLIED>

<!-- Object Name -->
<!ELEMENT NAME (#PCDATA)>

<!-- Object Address -->
<!ELEMENT ADDRESS (#PCDATA)>
<!ATTLIST ADDRESS
  type CDATA #REQUIRED>
```

## Remarks

The **OBJECT** element consists of one required **ID** element and four optional elements - **NAME**, **ADDRESS**, **DESCRIPTION**, and **VERSIONSPAN**. The two attributes, **type** and **version**, can be used to identify the object type and version number.

**OBJECT** elements are used frequently in Active Directory Rights Management Services (AD RMS) licenses and certificates.

## Examples

The following example shows an **OBJECT** element that identifies a machine certificate by using a GUID.


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

 

 




