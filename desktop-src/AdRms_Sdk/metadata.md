---
Description: Contains additional information about an item of content in an Active Directory Rights Management Services (AD RMS) issuance or end-user license. This element has the following definition.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: e0252db2-9f41-4582-9d07-dcfb5c8c51f5
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: METADATA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# METADATA

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

Contains additional information about an item of content in an Active Directory Rights Management Services (AD RMS) issuance or end-user license. This element has the following definition.

``` syntax
<!-- METADATA element -->
<!ELEMENT METADATA (TITLE?,
                    ID?,
                    CREATOR*,
                    PUBLISHER*,
                    OWNER?,
                    COPYRIGHT*,
                    DATE*,
                    FORMAT?,
                    SKU?,
                    CATEGORY*,
                    REFERENCE*,
                    PARAMETER*)>

<!-- OWNER element and aPrincipal entity -->
<!ELEMENT OWNER (%aPrincipal;)>
<!ATTLIST OWNER
  type CDATA #IMPLIED
  internal-id CDATA #IMPLIED>

<!ENTITY % aPrincipal "OBJECT?, 
   AUTHENTICATOR*, 
   PASSWORD*,
   PUBLICKEY*,
   PRIVATEKEY*, 
   CERTIFICATE*,
   DIGEST*,
   VERIFICATIONDATA*, 
   ENABLINGBITS*, 
   PRINCIPAL*,
   SECURITYLEVEL*>

<!-- SKU element -->
<!ELEMENT SKU (#PCDATA)>
<!ATTLIST SKU
  type CDATA #IMPLIED>
```

## Remarks

Of the elements available in the XrML 1.2 DTD, AD RMS typically uses the **SKU** (stock keeping unit) and **OWNER** metadata elements as shown in the following example from an end-user license.

## Examples


```XML
<METADATA>
  <OWNER>
    <OBJECT>
      <ID type="Windows"/>
      <NAME>someone@example.com</NAME>
    </OBJECT>
  </OWNER>
  <SKU type="SKUIdType">Some_SKU_Identifier</SKU>
</METADATA>
```



## Requirements



|                    |                                                           |
|--------------------|-----------------------------------------------------------|
| Product<br/> | Rights Management Services client 1.0 or later<br/> |



## See also

<dl> <dt>

[**BODY**](body.md)
</dt> <dt>

[**WORK**](work.md)
</dt> </dl>

 

 




