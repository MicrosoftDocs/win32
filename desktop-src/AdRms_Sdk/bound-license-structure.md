---
Description: Within an Active Directory Rights Management Services (AD RMS) infrastructure, a license is an eXtensible Rights Markup Language (XrML) document.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: d3f22338-046d-4eeb-961f-306a7dc1e502
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Bound License Structure
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Bound License Structure

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

Within an Active Directory Rights Management Services (AD RMS) infrastructure, a license is an eXtensible Rights Markup Language (XrML) document. A bound license contains a distilled version of an XrML end-user license. In a bound license, all information not pertaining to the bound user or environment is removed. Additionally, duplicated information, such as condition lists or rights, is combined into single entities.

To make it easier to retrieve information from a bound license, you can use the following AD RMS functions:

-   [**DRMGetBoundLicenseAttribute**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetboundlicenseattribute?branch=master)
-   [**DRMGetBoundLicenseAttributeCount**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetboundlicenseattributecount?branch=master)
-   [**DRMGetBoundLicenseObject**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetboundlicenseobject?branch=master)
-   [**DRMGetBoundLicenseObjectCount**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetboundlicenseobjectcount?branch=master)

The following elements, declared in Msdrmgetinfo.h, can be retrieved from a bound license:

<dl> g\_wszQUERY\_CONTENTIDTYPE  
g\_wszQUERY\_CONTENTIDVALUE  
g\_wszQUERY\_CONTENTSKUTYPE  
g\_wszQUERY\_CONTENTSKUVALUE  
g\_wszQUERY\_ENABLINGPRINCIPALIDTYPE  
g\_wszQUERY\_ENABLINGPRINCIPALIDVALUE  
**g\_wszQUERY\_RIGHT** (1...n)  
     **g\_wszQUERY\_INTERVALTIMECONDITION**  
         g\_wszQUERY\_INTERVALTIMEINTERVAL  
     **g\_wszQUERY\_OSEXCLUSIONCONDITION**  
         g\_wszQUERY\_MINVERSION  
         g\_wszQUERY\_MAXVERSION  
     g\_wszQUERY\_NAME  
     g\_wszQUERYRIGHTSPARAMETERNAME (1...n)  
     g\_wszQUERYRIGHTSPARAMETERVALUE (1...n)  
     **g\_wszQUERY\_ACCESSCONDITION** (1...n)  
         **g\_wszQUERY\_PRINCIPAL** (1...n)  
             Sub-Hierarchy A  
     **g\_wszQUERY\_REVOCATIONCONDITION** (1...n)  
         g\_wszQUERY\_REFRESHPERIOD  
         **g\_wszQUERY\_DISTRIBUTIONPOINT** (1...n)  
             Sub-Hierarchy A  
</dl>

The following elements make up Sub-Hierarchy A.

<dl> g\_wszQUERY\_IDTYPE  
g\_wszQUERY\_IDVALUE  
g\_wszQUERY\_NAME  
g\_wszQUERY\_ADDRESSTYPE (1...n)  
g\_wszQUERY\_ADDRESSVALUE (1...n)  
</dl>

## Related topics

<dl> <dt>

[Querying Licenses](querying-licenses.md)
</dt> <dt>

[Working with Licenses and Templates](working-with-licenses-and-templates.md)
</dt> </dl>

 

 



