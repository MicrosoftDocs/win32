---
description: Creates an X.509 certificate, signed by the test root key or other specified key, that binds your name to the public part of the key pair. The certificate is saved to a file, a system certificate store, or both.
ms.assetid: a28e77dd-72c9-42a3-a72d-1b3eaf59d9cf
title: MakeCert
ms.topic: article
ms.date: 05/31/2018
---

# MakeCert

> [!Note]  
> MakeCert is deprecated. To create self-signed certificates, use the Powershell Cmdlet [New-SelfSignedCertificate](/powershell/module/pki/new-selfsignedcertificate).

 

The MakeCert tool creates an [*X.509*](../secgloss/x-gly.md) certificate, signed by the test root key or other specified key, that binds your name to the public part of the key pair. The certificate is saved to a file, a system certificate store, or both. The tool is installed in the \\Bin folder of the Microsoft Windows Software Development Kit (SDK) installation path.

The MakeCert tool uses the following command syntax:

**MakeCert** \[*BasicOptions*\|*ExtendedOptions*\] *OutputFile*

*OutputFile* is the name of the file where the certificate will be written. You can omit *OutputFile* if the certificate is not to be written to a file.

## Options

MakeCert includes basic and extended options. Basic options are those most commonly used to create a certificate. Extended options provide more flexibility.

The options for MakeCert are also divided into three functional groups:

-   Basic options specific to certificate store technology only.
-   Extended options specific to SPC-file and private key technology only.
-   Extended options applicable to SPC-file, private key, and certificate store technology.

Options given in the following tables can be used only with Internet Explorer 4.0 or later.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Basic option</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>-a</strong> <strong></strong> <em>Algorithm</em></td>
<td><a href="/windows/desktop/SecGloss/h-gly"><em>Hash</em></a> algorithm. Must be set to either <strong>SHA-1</strong> or <strong>MD5</strong> (default). For information about MD5, see <a href="/windows/desktop/SecGloss/m-gly"><em>MD5</em></a>.</td>
</tr>
<tr class="even">
<td><strong>-b</strong> <strong></strong> <em>DateStart</em></td>
<td>Date the certificate first becomes valid. The default is when the certificate is created. The format of <em>DateStart</em> is mm/dd/yyyy.</td>
</tr>
<tr class="odd">
<td><strong>-cy</strong> <strong></strong> <em>CertificateTypes</em></td>
<td>Certificate type. <em>CertificateTypes</em> can be <strong>end</strong> for end-entity, or <strong>authority</strong> for <a href="/windows/desktop/SecGloss/c-gly"><em>certification authority</em></a>.</td>
</tr>
<tr class="even">
<td><strong>-e</strong> <strong></strong> <em>DateEnd</em></td>
<td>Date when the validity period ends. The default is the year 2039.</td>
</tr>
<tr class="odd">
<td><strong>-eku</strong> <strong></strong> <em>OID1</em><strong>,</strong> <em>OID2</em> …</td>
<td>Inserts a list of one or more comma-separated, <a href="/windows/desktop/SecGloss/e-gly"><em>enhanced key usage</em></a> <a href="/windows/desktop/SecGloss/o-gly"><em>object identifiers</em></a> (OIDs) into the certificate. For example, <strong>-eku 1.3.6.1.5.5.7.3.2</strong> inserts the client authentication OID. For definitions of allowable OIDs, see the Wincrypt.h file in CryptoAPI 2.0.</td>
</tr>
<tr class="even">
<td><strong>-h</strong> <strong></strong> <em>NumChildren</em></td>
<td>Maximum height of the tree below this certificate.</td>
</tr>
<tr class="odd">
<td><strong>-l</strong> <strong></strong> <em>PolicyLink</em></td>
<td>Link to SPC agency policy information (for example, a URL).</td>
</tr>
<tr class="even">
<td><strong>-m</strong> <strong></strong> <em>nMonths</em></td>
<td>Duration of the validity period.</td>
</tr>
<tr class="odd">
<td><strong>-n</strong> <strong>&quot;</strong><em>Name</em><strong>&quot;</strong></td>
<td>Name for the publisher's certificate. This name must conform to the <a href="/windows/desktop/SecGloss/x-gly"><em>X.500</em></a> standard. The simplest method is to use the &quot;CN=<em>MyName</em>&quot; format. For example: <strong>-n &quot;CN=Test&quot;</strong>.</td>
</tr>
<tr class="even">
<td><strong>-nscp</strong></td>
<td>The Netscape client authentication extension should be included.</td>
</tr>
<tr class="odd">
<td><strong>-pe</strong></td>
<td>Marks the private key as exportable.</td>
</tr>
<tr class="even">
<td><strong>-r</strong></td>
<td>Creates a self-signed certificate.</td>
</tr>
<tr class="odd">
<td><strong>-sc</strong> <strong></strong> <em>SubjectCertFile</em></td>
<td>Certificate file name with the existing subject public key to be used.</td>
</tr>
<tr class="even">
<td><strong>-sk</strong> <strong></strong> <em>SubjectKey</em></td>
<td>Location of the subject's key container which holds the <a href="/windows/desktop/SecGloss/p-gly"><em>private key</em></a>. If a key container does not exist, one is created. If neither the <strong>-sk</strong> or <strong>-sv</strong> option is used, a default key container is created and used by default.</td>
</tr>
<tr class="odd">
<td><strong>-sky</strong> <strong></strong> <em>SubjectKeySpec</em></td>
<td>Subject's key specification. <em>SubjectKeySpec</em> must be one of three possible values:<br/>
<ul>
<li><strong>Signature</strong> (AT_SIGNATURE key specification)</li>
<li><strong>Exchange</strong> (AT_KEYEXCHANGE key specification)</li>
<li>An integer, such as <strong>3</strong></li>
</ul>
For more information, see the Note that follows this table.<br/></td>
</tr>
<tr class="even">
<td><strong>-sp</strong> <strong></strong> <em>SubjectProviderName</em></td>
<td>CryptoAPI provider for subject. The default is the user's provider. For information about CryptoAPI providers, see the CryptoAPI 2.0 documentation.</td>
</tr>
<tr class="odd">
<td><strong>-sr</strong> <strong></strong> <em>SubjectCertStoreLocation</em></td>
<td>Registry location of the subject's certificate store. <em>SubjectCertStoreLocation</em> must be either <strong>LocalMachine</strong> (registry key HKEY_LOCAL_MACHINE) or <strong>CurrentUser</strong> (registry key HKEY_CURRENT_USER). <strong>CurrentUser</strong> is the default.</td>
</tr>
<tr class="even">
<td><strong>-ss</strong> <strong></strong> <em>SubjectCertStoreName</em></td>
<td>Name of the subject's certificate store where the generated certificate will be stored.</td>
</tr>
<tr class="odd">
<td><strong>-sv</strong> <strong></strong> <em>SubjectKeyFile</em></td>
<td>Name of the subject's .pvk file. If neither the <strong>-sk</strong> or <strong>-sv</strong> option is used, a default key container is created and used by default.</td>
</tr>
<tr class="even">
<td><strong>-sy</strong> <strong></strong> <em>nSubjectProviderType</em></td>
<td>CryptoAPI provider type for subject. The default is <a href="/windows/desktop/SecGloss/p-gly"><em>PROV_RSA_FULL</em></a>. For information about CryptoAPI provider types, see the CryptoAPI 2.0 documentation.</td>
</tr>
<tr class="odd">
<td><strong>-#</strong> <strong></strong> <em>SerialNumber</em></td>
<td>Serial number of the certificate. The maximum value is 2^31. The default is a value generated by the tool that is guaranteed to be unique.</td>
</tr>
<tr class="even">
<td><strong>-$</strong> <strong></strong> <em>CertificateAuthority</em></td>
<td>Type of <a href="/windows/desktop/SecGloss/c-gly"><em>certification authority</em></a>. <em>CertificateAuthority</em> must be set to either <strong>commercial</strong> (for certificates to be used by commercial software publishers) or <strong>individual</strong> (for certificates to be used by individual software publishers).</td>
</tr>
<tr class="odd">
<td><strong>-?</strong></td>
<td>Displays the basic options.</td>
</tr>
<tr class="even">
<td><strong>-!</strong></td>
<td>Displays the extended options.</td>
</tr>
</tbody>
</table>



 

> [!Note]  
> If the **-sky** key specification option is used in Internet Explorer version 4.0 or later, the specification must match the key specification indicated by the [*private key*](../secgloss/p-gly.md) file or private [*key container*](../secgloss/k-gly.md). If the key specification option is not used, the key specification indicated by the private key file or private key container will be used. If there is more than one key specification in the key container, MakeCert will first attempt to use the AT\_SIGNATURE key specification. If that fails, MakeCert will try to use AT\_KEYEXCHANGE. Because most users have either an AT\_SIGNATURE key or an AT\_KEYEXCHANGE key, this option does not need to be used in most cases.

 

The following options are only for [*Software Publisher Certificate*](../secgloss/s-gly.md) (SPC) files and private key technology.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>SPC and private key option</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>-ic</strong> <strong></strong> <em>IssuerCertFile</em></td>
<td>Location of the issuer's certificate.</td>
</tr>
<tr class="even">
<td><strong>-ik</strong> <strong></strong> <em>IssuerKey</em></td>
<td>Location of the issuer's key container. The default is the test root key.</td>
</tr>
<tr class="odd">
<td><strong>-iky</strong> <strong></strong> <em>IssuerKeySpec</em></td>
<td>Issuer's key specification, which must be one of three possible values:<br/>
<ul>
<li><strong>Signature</strong> (AT_SIGNATURE key specification)</li>
<li><strong>Exchange</strong> (AT_KEYEXCHANGE key specification)</li>
<li>An integer, such as <strong>3</strong></li>
</ul>
For more information, see the Note that follows this table.<br/></td>
</tr>
<tr class="even">
<td><strong>-ip</strong> <strong></strong> <em>IssuerProviderName</em></td>
<td>CryptoAPI provider for issuer. The default is the user's provider. For information about CryptoAPI providers, see the CryptoAPI 2.0 documentation.</td>
</tr>
<tr class="odd">
<td><strong>-iv</strong> <strong></strong> <em>IssuerKeyFile</em></td>
<td>Issuer's private key file. The default is the test root.</td>
</tr>
<tr class="even">
<td><strong>-iy</strong> <strong></strong> <em>nIssuerProviderType</em></td>
<td>CryptoAPI provider type for issuer. The default is <a href="/windows/desktop/SecGloss/p-gly"><em>PROV_RSA_FULL</em></a>. For information about CryptoAPI provider types, see the CryptoAPI 2.0 documentation.</td>
</tr>
</tbody>
</table>



 

> [!Note]  
> If the **-iky** key specification option is used in Internet Explorer 4.0 or later, the specification must match the key specification indicated by the [*private key*](../secgloss/p-gly.md) file or private [*key container*](../secgloss/k-gly.md). If the key specification option is not used, the key specification indicated by the private key file or private key container will be used. If there is more than one key specification in the key container, MakeCert will first attempt to use the AT\_SIGNATURE key specification. If that fails, MakeCert will try to use AT\_KEYEXCHANGE. Because most users have either an AT\_SIGNATURE key or an AT\_KEYEXCHANGE key, this option does not need to be used in most cases.

 

The following options are for [*certificate store*](../secgloss/c-gly.md) technology only.



| Certificate store option          | Description                                                                                                                                                                                                                                                                                                                              |
|-----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **-ic** *IssuerCertFile*          | File that contains the issuer's certificate. MakeCert will search in the certificate store for a certificate with an exact match.                                                                                                                                                                                                        |
| **-in** *IssuerNameString*        | Common name of the issuer's certificate. MakeCert will search in the certificate store for a certificate whose common name includes *IssuerNameString*.                                                                                                                                                                                  |
| **-ir** *IssuerCertStoreLocation* | Registry location of the issuer's certificate store. *IssuerCertStoreLocation* must be either **LocalMachine** (registry key HKEY\_LOCAL\_MACHINE) or **CurrentUser** (registry key HKEY\_CURRENT\_USER). **CurrentUser** is the default.                                                                                                |
| **-is** *IssuerCertStoreName*     | Issuer's certificate store that includes the issuer's certificate and its associated private key information. If there is more than one certificate in the store, the user must uniquely identify it by using the **-ic** or **-in** option. If the certificate in the certificate store is not uniquely identified, MakeCert will fail. |



 

 

 
