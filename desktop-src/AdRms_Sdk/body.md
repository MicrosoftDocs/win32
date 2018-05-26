---
Description: Contains information about the Active Directory Rights Management Services (AD RMS) license or certificate. It has the following definition. Of the elements listed, SECURESTORE and MODULELIST are not used by AD RMS.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 4feefc19-46c7-4216-8ba8-543b88ecf812
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: BODY
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# BODY

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

Contains information about the Active Directory Rights Management Services (AD RMS) license or certificate. It has the following definition. Of the elements listed, **SECURESTORE** and **MODULELIST** are not used by AD RMS.

``` syntax
<!ELEMENT BODY (ISSUEDTIME?,
                VALIDITYTIME?,
                DESCRIPTOR?,
                ISSUER?,
                DISTRIBUTIONPOINT*?,
                ISSUEDPRINCIPALS?,
                WORK?,
                AUTHENTICATEDDATA?,
                SECURESTORE?,
                CONDITIONLIST?
                FEDERATIONPRINCIPALS?,
                DIGESTLIST?,
                POLICYLIST?,
                MODULELIST?,
                REVOCATIONLIST?)>
<!ATTLIST BODY
  type    CDATA #IMPLIED
  version CDATA #IMPLIED
  xmlns   %URI; #IMPLIED>
```

## Remarks

The attributes **type**, **version**, and **xmlns** identify the type, version, and schema associated with the **BODY** element.

The following example shows the high level structure of an end-user license.


```XML
- <XrML xmlns="" version="1.2" purpose="ContentLicense">
  - <BODY type="LICENSE" version="3.0">
    + <ISSUEDTIME>
    + <DESCRIPTOR>
    + <ISSUER>
    + <ISSUEDPRINCIPALS>
    + <WORK>
    + <POLICYLIST>
    </BODY>
  + <SIGNATURE>
  </XrML>
```



The following topics discuss the individual body elements typically found in an AD RMS license or certificate. For a complete discussion of all elements, including those not listed below, go to the www.xrml.org and download the specification and DTD.

-   [**ISSUEDTIME**](issuedtime.md)
-   [**VALIDITYTIME**](validitytime.md)
-   [**DESCRIPTOR**](descriptor.md)
-   [**ISSUER**](issuer.md)
-   [**DISTRIBUTIONPOINT**](distributionpoint.md)
-   [**ISSUEDPRINCIPALS**](issuedprincipals.md)
-   [**WORK**](work.md)
-   [**AUTHENTICATEDDATA**](authenticateddata.md)
-   [**CONDITIONLIST**](conditionlist.md)
-   [**FEDERATIONPRINCIPALS**](federationprincipals.md)
-   [**REVOCATIONLIST**](revocationlist.md)
-   [**OBJECT**](object.md)

## Requirements



|                    |                                                           |
|--------------------|-----------------------------------------------------------|
| Product<br/> | Rights Management Services client 1.0 or later<br/> |



## See also

<dl> <dt>

[**SIGNATURE**](signature.md)
</dt> <dt>

[XrML Elements](xrml-elements.md)
</dt> </dl>

 

 




