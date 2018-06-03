---
Description: No certificates or licenses are valid forever.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: fd69c9a3-eb8d-482b-ac1c-f4e042dbd759
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: License Validity Time
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# License Validity Time

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

No certificates or licenses are valid forever. Because each license is actually part of a chain of certificates leading back to a single certificate (see [Certificate Hierarchy](certificate-hierarchy.md)), and no licensor certificates are issued for an indefinite period, eventually at least one certificate in the chain will expire.

Currently, server licensor certificates that are valid for seven years are reissued to a service each year. This means that if a service regularly updates their server licensor certificate, any license this service creates can be valid for a maximum of seven years (with a newly granted certificate) or a minimum of six years and a day (with a certificate granted the day before a service obtains a new certificate). However, if a service is not regularly updating its server licensor certificate, the existing certificate can be valid for any length of time from seven years (newly issued license) down to one second (a license issued seven years ago). Because there is no guarantee that a service is regularly updating their certificates, your application should be able to handle expired licenses by acquiring new end-user licenses.

Even if a service updates its server licensor certificate regularly, any licenses referencing these previously issued licenses can only be valid for a maximum of seven years (the validity period of the issuing service's certificate). Therefore, you should not protect content that you expect to archive indefinitely, unless you plan to refresh the licenses before they expire (or copy the content into new documents).

The default validity times for the licenses and certificates that a service issues ([*rights account certificate*](https://www.bing.com/search?q=*rights account certificate*) (RAC), temporary RAC, [*end-user license*](https://www.bing.com/search?q=*end-user license*), and so on) are set by the issuing service. These values can be changed, up to the maximum allowable time of seven years.

Revocation of a higher certificate can also make a license not valid, but this cannot be predicted or prevented by examining the certificate chain.

## Related topics

<dl> <dt>

[Working with Licenses and Templates](working-with-licenses-and-templates.md)
</dt> </dl>

 

 



