---
description: OPM Certificate Revocation
ms.assetid: 21faf809-1335-4d93-be06-628c5a05a4c8
title: OPM Certificate Revocation
ms.topic: article
ms.date: 05/31/2018
---

# OPM Certificate Revocation

An output protection manager (OPM) certificate can be revoked by Microsoft. The list of revoked certificates is stored in a global revocation list (GRL). The GRL has the following format:



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Section</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Header</td>
<td>A <a href="grl-header.md"><strong>GRL_HEADER</strong></a> structure.</td>
</tr>
<tr class="even">
<td>Core</td>
<td>Contains the following revocation lists:
<ul>
<li>Kernel binary revocations</li>
<li>User-mode binary revocations</li>
<li>Certificate revocations</li>
<li>Trusted roots (reserved)</li>
</ul>
The list of trusted roots is currently not used, and is reserved for future use.</td>
</tr>
<tr class="odd">
<td>Extensible entries</td>
<td>Contains information used by other components. This section is not relevant to OPM.</td>
</tr>
<tr class="even">
<td>Renewals:</td>
<td>Contains GUIDs that define Windows Update identifiers. This section contains identifiers for the following lists:
<ul>
<li>Kernel binary revocations</li>
<li>User-mode binary revocations</li>
<li>Certificate revocations</li>
</ul>
An application can use these identifiers to request a renewed version of a revoked binary, if one is available.</td>
</tr>
<tr class="odd">
<td>Signature: Core section</td>
<td>Signs the header and core sections.</td>
</tr>
<tr class="even">
<td>Signature: Extensible section</td>
<td>Signs the header and extensible sections.</td>
</tr>
</tbody>
</table>



 

The GRL header is a [**GRL\_HEADER**](grl-header.md) structure. The **dwSequenceNumber** member of the structure contains the GRL version number. This number is incremented whenever the GRL is updated and a new version placed on the user's computer.

Revoked OPM certificates are listed in the certificate revocations list of the Core section. Each Core entry in the GRL is a 20-byte array that contains the SHA-1 hash of the public key of the revoked certificate.

The Signature sections contains signatures that can be used to verify that the GRL has not been tampered with. Each Signature sections contains am [**MF\_SIGNATURE**](mf-signature.md) structure. The first signature signs the header plus the Core section. The second signature signs the header plus the Extensible section; this signature is not relevant to OPM.

To ensure that the GRL itself has not been tampered with, verify the signature as follows:

1.  Find the start of the [**MF\_SIGNATURE**](mf-signature.md) structure. The location of the **MF\_SIGNATURE** structure is given in the **cbSignatureCoreOffset** member of the [**GRL\_HEADER**](grl-header.md) structure. The location is specified as an offset in bytes from the start of the GRL.
2.  Parse the [**MF\_SIGNATURE**](mf-signature.md) structure as a PKCS \#7 signature with a certificate chain.
3.  Verify the certificate chain up to a trusted root.
4.  Verify that the leaf certificate has the following object identifier in the EKU: "1.3.6.1.4.1.311.10.5.4".
5.  Compute a hash of the bytes that include the header and the core sections of the GRL.
6.  Verify that the hash matches the signature in the leaf certificate.

## Related topics

<dl> <dt>

[Output Protection Manager](output-protection-manager.md)
</dt> <dt>

[**GRL\_HEADER**](grl-header.md)
</dt> <dt>

[**MF\_SIGNATURE**](mf-signature.md)
</dt> </dl>

 

 



