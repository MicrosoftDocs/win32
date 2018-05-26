---
Description: Within an Active Directory Rights Management Services (AD RMS) infrastructure, a license is an eXtensible Rights Markup Language (XrML) document.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: ec6820c9-623c-4572-8a41-27d78ca53809
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Unbound License Structure
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Unbound License Structure

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

Within an Active Directory Rights Management Services (AD RMS) infrastructure, a license is an eXtensible Rights Markup Language (XrML) document. To make it easier to retrieve information from an unbound license, you can use the following AD RMS functions:

-   [**DRMGetUnboundLicenseAttribute**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetunboundlicenseattribute?branch=master)
-   [**DRMGetUnboundLicenseAttributeCount**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetunboundlicenseattributecount?branch=master)
-   [**DRMGetUnboundLicenseObject**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetunboundlicenseobject?branch=master)
-   [**DRMGetUnboundLicenseObjectCount**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetunboundlicenseobjectcount?branch=master)
-   [**DRMParseUnboundLicense**](/windows/previous-versions/Msdrm/nf-msdrm-drmparseunboundlicense?branch=master)

An unbound end-user license contains the complete rights information for all of the users specified in the license. Certain information may be duplicated in different places in the license, and several copies of the same object with different values (for example, principals or condition lists) can exist in a license, and therefore an unbound license can be quite complex.

The unbound license retrieved by [**DRMEnumerateLicense**](/windows/previous-versions/Msdrm/nf-msdrm-drmenumeratelicense?branch=master) is a certificate chain. To properly query the unbound license itself, call [**DRMDeconstructCertificateChain**](/windows/previous-versions/Msdrm/nf-msdrm-drmdeconstructcertificatechain?branch=master) to obtain the first element of the chain (item zero), which is the actual license. The following elements, declared in Msdrmgetinfo.h, can be retrieved from an unbound license:

<dl> g\_wszQUERY\_IDTYPE  
g\_wszQUERY\_IDVALUE  
g\_wszQUERY\_ISSUEDTIME  
g\_wszQUERY\_VALIDITYFROMTIME  
g\_wszQUERY\_VALIDITYUNTILTIME  
**g\_wszQUERY\_ISSUEDPRINCIPAL**(1...n)  
     Sub-Hierarchy A  
**g\_wszQUERY\_GROUPIDENTITYPRINCIPAL**(1...n)  
     Sub-Hierarchy A  
**g\_wszQUERY\_ISSUER**  
     Sub-Hierarchy A  
**g\_wszQUERY\_DISTRIBUTIONPOINT** (1...n)  
     Sub-Hierarchy A  
**g\_wszQUERY\_WORK** (1...n)  
     g\_wszQUERY\_IDTYPE  
     g\_wszQUERY\_IDVALUE  
     g\_wszQUERY\_SKUTYPE  
     g\_wszQUERY\_SKUVALUE  
     g\_wszQUERY\_NAME  
     **g\_wszQUERY\_OWNER**  
         Sub-Hierarchy A  
     **g\_wszQUERY\_CONDITIONLIST**  
         Same sub-hierarchy as g\_wszQUERY\_CONDITIONLIST below  
     **g\_wszQUERY\_RIGHTSGROUP** (1...n)  
         g\_wszQUERY\_NAME  
         **g\_wszQUERY\_CONDITIONLIST**  
             Same sub-hierarchy as g\_wszQUERY\_CONDITIONLIST below  
         **g\_wszQUERY\_RIGHT** (1...n)  
             g\_wszQUERY\_NAME  
             g\_wszQUERY\_RIGHTSPARAMETERNAME (1...n)  
             g\_wszQUERY\_RIGHTSPARAMETERVALUE (1...n)  
             **g\_wszQUERY\_CONDITIONLIST**  
                 Same sub-hierarchy as g\_wszQUERY\_CONDITIONLIST below  
**g\_wszQUERY\_CONDITIONLIST**  
    **g\_wszQUERY\_INTERVALTIMECONDITION**  
        g\_wszQUERY\_INTERVALTIMEINTERVAL  
    **g\_wszQUERY\_OSEXCLUSIONCONDITION**  
        g\_wszQUERY\_MINVERSION  
        g\_wszQUERY\_MAXVERSION  
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

 

 



