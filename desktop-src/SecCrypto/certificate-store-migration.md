---
description: During a computer upgrade or a computer-to-computer migration, the certificates in certain certificate stores will be migrated.
ms.assetid: fe81d578-f2f6-41f0-9ebf-e7bd5532bed9
title: Certificate Store Migration
ms.topic: article
ms.date: 05/31/2018
---

# Certificate Store Migration

During a computer upgrade or a computer-to-computer migration, the certificates in certain certificate stores will be migrated. The following table lists the certificate stores that are migrated by default. For the system Automatic Certificate Request Settings (ACRS) store, only the [*certificate trust lists*](../secgloss/c-gly.md) (CTLs) are migrated. For all other stores listed below, only the certificates are migrated.

<table>
<thead>
<tr class="header">
<th>System/user</th>
<th>Store</th>
<th>Storage location</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>${ROWSPAN8}$System${REMOVE}$<br />
</td>
<td>ROOT</td>
<td><strong>HKEY_LOCAL_MACHINE</strong>\<strong>SOFTWARE</strong>\<strong>Microsoft</strong>\<strong>SystemCertificates</strong>\<strong>Root</strong>\<strong>Certificates</strong><br/></td>
</tr>
<tr class="even">
<td>MY</td>
<td><strong>HKEY_LOCAL_MACHINE</strong>\<strong>SOFTWARE</strong>\<strong>Microsoft</strong>\<strong>SystemCertificates</strong>\<strong>My</strong>\<strong>Certificates</strong><br/></td>

</tr>
<tr class="odd">
<td>REQUEST</td>
<td><strong>HKEY_LOCAL_MACHINE</strong>\<strong>SOFTWARE</strong>\<strong>Microsoft</strong>\<strong>SystemCertificates</strong>\<strong>Request</strong>\<strong>Certificates</strong><br/></td>

</tr>
<tr class="even">
<td>TrustedPublisher</td>
<td><strong>HKEY_LOCAL_MACHINE</strong>\<strong>SOFTWARE</strong>\<strong>Microsoft</strong>\<strong>SystemCertificates</strong>\<strong>TrustedPublisher</strong>\<strong>Certificates</strong><br/></td>

</tr>
<tr class="odd">
<td>TrustedPeople</td>
<td><strong>HKEY_LOCAL_MACHINE</strong>\<strong>SOFTWARE</strong>\<strong>Microsoft</strong>\<strong>SystemCertificates</strong>\<strong>TrustedPeople</strong>\<strong>Certificates</strong><br/></td>

</tr>
<tr class="even">
<td>Disallowed</td>
<td><strong>HKEY_LOCAL_MACHINE</strong>\<strong>SOFTWARE</strong>\<strong>Microsoft</strong>\<strong>SystemCertificates</strong>\<strong>Disallowed</strong>\<strong>Certificates</strong><br/></td>

</tr>
<tr class="odd">
<td>CA</td>
<td><strong>HKEY_LOCAL_MACHINE</strong>\<strong>SOFTWARE</strong>\<strong>Microsoft</strong>\<strong>SystemCertificates</strong>\<strong>CA</strong>\<strong>Certificates</strong><br/></td>

</tr>
<tr class="even">
<td>ACRS</td>
<td><strong>HKEY_LOCAL_MACHINE</strong>\<strong>SOFTWARE</strong>\<strong>Microsoft</strong>\<strong>SystemCertificates</strong>\<strong>ACRS</strong>\<strong>CTLs</strong><br/></td>

</tr>
<tr class="odd">
<td rowspan="7">User${REMOVE}$<br />
</td>
<td>ROOT</td>
<td><strong>HKEY_CURRENT_USER</strong>\<strong>SOFTWARE</strong>\<strong>Microsoft</strong>\<strong>SystemCertificates</strong>\<strong>Root</strong>\<strong>Certificates</strong><br/></td>
</tr>
<tr class="even">
<td>MY</td>
<td>file:\\%APPDATA%\Microsoft\SystemCertificates\My\Certificates</td>

</tr>
<tr class="odd">
<td>REQUEST</td>
<td>file:\\%APPDATA%\Microsoft\SystemCertificates\Request\Certificates</td>

</tr>
<tr class="even">
<td>TrustedPublisher</td>
<td><strong>HKEY_CURRENT_USER</strong>\<strong>SOFTWARE</strong>\<strong>Microsoft</strong>\<strong>SystemCertificates</strong>\<strong>TrustedPublisher</strong>\<strong>Certificates</strong><br/></td>

</tr>
<tr class="odd">
<td>TrustedPeople</td>
<td><strong>HKEY_CURRENT_USER</strong>\<strong>SOFTWARE</strong>\<strong>Microsoft</strong>\<strong>SystemCertificates</strong>\<strong>TrustedPeople</strong>\<strong>Certificates</strong><br/></td>

</tr>
<tr class="even">
<td>Disallowed</td>
<td><strong>HKEY_CURRENT_USER</strong>\<strong>SOFTWARE</strong>\<strong>Microsoft</strong>\<strong>SystemCertificates</strong>\<strong>Disallowed</strong>\<strong>Certificates</strong><br/></td>

</tr>
<tr class="odd">
<td>CA</td>
<td><strong>HKEY_CURRENT_USER</strong>\<strong>SOFTWARE</strong>\<strong>Microsoft</strong>\<strong>SystemCertificates</strong>\<strong>CA</strong>\<strong>Certificates</strong><br/></td>

</tr>
</tbody>
</table>



 

Other certificate stores created by applications are not migrated by default. Applications that create their own stores are responsible for migration of the stores that they create. To create stores, we recommend that you define a registry key in the application settings and create a store within the registry settings by using the **CERT\_STORE\_PROV\_REG** store provider. For more information about migrating application settings, see the *How To Create a Custom .xml File* topic in the *Using USMT 3.0* guide at [User State Migration Tool 3.0](https://www.microsoft.com/technet/windowsvista/library/91f62fc4-621f-4537-b311-1307df010561.mspx). (This resource may not be available in some languages and countries or regions.)

 

 
