---
Description: Concepts that you should understand before using the Active Directory Rights Management Services (AD RMS) SDK.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 4e184718-73f6-4096-b28c-05821518860b
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: AD RMS Concepts
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AD RMS Concepts

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The following topics contain overviews of the major concepts that you should understand before using the Active Directory Rights Management Services (AD RMS) SDK.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[Licenses](licenses.md)</td>
<td>Introduces issuance licenses and end-user licenses.</td>
</tr>
<tr class="even">
<td>[Certificates](certificates.md)</td>
<td>Introduces the following certificates:
<ul>
<li>machine certificates</li>
<li>rights account certificates</li>
<li>client licensor certificates</li>
<li>server licensor certificates</li>
<li>application manifests</li>
<li>Pre-production certificates</li>
<li>Production certificates</li>
</ul></td>
</tr>
<tr class="odd">
<td>[Certificate Hierarchy](certificate-hierarchy.md)</td>
<td>Introduces the AD RMS Pre-production and Production certificate hierarchy.</td>
</tr>
<tr class="even">
<td>[Templates](templates.md)</td>
<td>Introduces predefined templates that can be used to apply usage policies when creating a license.</td>
</tr>
<tr class="odd">
<td>[Extended Policy Template Information](extended-policy-template-information.md)</td>
<td>Discusses the rights policy of a template that controls how content licenses are to be implemented.</td>
</tr>
<tr class="even">
<td>[Application Manifests](application-manifests.md)</td>
<td>Introduces application manifests, a type of certificate that signs your application into the appropriate AD RMS certificate hierarchy.</td>
</tr>
<tr class="odd">
<td>[Lockboxes](lockboxes.md)</td>
<td>These can be used to create secure environments on AD RMS clients and servers.</td>
</tr>
<tr class="even">
<td>[Encryption](encryption.md)</td>
<td>Discusses encrypting and decrypting content.</td>
</tr>
<tr class="odd">
<td>[Computer Activation](computer-activation.md)</td>
<td>Introduces computer activation, a process that identifies the computer by signing it into the appropriate AD RMS hierarchy.</td>
</tr>
<tr class="even">
<td>[User Activation](user-activation.md)</td>
<td>Introduces user activation, a process that identifies an Active Directory user account in the appropriate AD RMS hierarchy and associates it with a specific computer.</td>
</tr>
<tr class="odd">
<td>[Server Enrollment](server-enrollment.md)</td>
<td>Discusses how an AD RMS server is enrolled into the certificate hierarchy.</td>
</tr>
<tr class="even">
<td>[Service Discovery](service-discovery.md)</td>
<td>Discusses how an application finds an AD RMS certification, licensing, or publishing web service.</td>
</tr>
<tr class="odd">
<td>[Rights](rights.md)</td>
<td>Introduces the common rights used in AD RMS licenses.</td>
</tr>
<tr class="even">
<td>[Exclusion](exclusion.md)</td>
<td>Discusses how users can be prohibited from acquiring new licenses or certificates.</td>
</tr>
<tr class="odd">
<td>[Revocation](revocation.md)</td>
<td>Discusses how AD RMS licenses and certificates can be invalidated after issuance.</td>
</tr>
<tr class="even">
<td>[Server Transport Protocol](server-transport-protocol.md)</td>
<td>Discusses the protocols that can be used to communicate with an AD server.</td>
</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[About the AD RMS SDK](about-the-ad-rms-sdk.md)
</dt> <dt>

[AD RMS Overview](ad-rms-overview.md)
</dt> </dl>

 

 



