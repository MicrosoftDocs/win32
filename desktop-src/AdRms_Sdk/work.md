---
Description: Represents an item of content in an Active Directory Rights Management Services (AD RMS) issuance license or end-user license. This element has the following definition.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 0f890c29-4433-488d-8008-a733c2af2ead
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: WORK
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# WORK

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

Represents an item of content in an Active Directory Rights Management Services (AD RMS) issuance license or end-user license. This element has the following definition.

``` syntax
<!-- WORK element -->
<!ELEMENT WORK (OBJECT, 
                DESCRIPTION?,
                METADATA?,
                SIGNATURE*,
                WORKLIST?,
                CONTENT?,
                COPIES?,
                DISTRIBUTIONPOINT*,
                SECURESTORE?,
                PRECONDITIONLIST?,
                CONDITIONLIST?,
                RIGHTSGROUP*,
                REFERENCEDRIGHTSGROUP*)>

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

<!-- RIGHTSGROUP element -->
<!ELEMENT RIGHTSGROUP (DESCRIPTION?, 
                       DISTRIBUTIONPOINT*, 
                       SECURESTORE?, 
                       PRECONDITIONLIST?,
                       CONDITIONLIST?, 
                       RIGHTSLIST?)>
!ATTLIST RIGHTSGROUP
  name CDATA #REQUIRED
  id CDATA #IMPLIED>
```

## Remarks

Of the available elements, AD RMS typically uses only [**OBJECT**](object.md), [**METADATA**](metadata.md), and **RIGHTSGROUP**. Within the **RIGHTSGROUP** element, the [**RIGHTSLIST**](rightslist.md) element is typically used. For more information, see the following topics:

-   [**METADATA**](metadata.md)
-   [**RIGHTSLIST**](rightslist.md)

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

 

 




