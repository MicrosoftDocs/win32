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




| Basic option | Description | 
|--------------|-------------|
| <strong>-a</strong><strong></strong><em>Algorithm</em> | <a href="/windows/desktop/SecGloss/h-gly"><em>Hash</em></a> algorithm. Must be set to either <strong>SHA-1</strong> or <strong>MD5</strong> (default). For information about MD5, see <a href="/windows/desktop/SecGloss/m-gly"><em>MD5</em></a>. | 
| <strong>-b</strong><strong></strong><em>DateStart</em> | Date the certificate first becomes valid. The default is when the certificate is created. The format of <em>DateStart</em> is mm/dd/yyyy. | 
| <strong>-cy</strong><strong></strong><em>CertificateTypes</em> | Certificate type. <em>CertificateTypes</em> can be <strong>end</strong> for end-entity, or <strong>authority</strong> for <a href="/windows/desktop/SecGloss/c-gly"><em>certification authority</em></a>. | 
| <strong>-e</strong><strong></strong><em>DateEnd</em> | Date when the validity period ends. The default is the year 2039. | 
| <strong>-eku</strong><strong></strong><em>OID1</em><strong>,</strong><em>OID2</em> … | Inserts a list of one or more comma-separated, <a href="/windows/desktop/SecGloss/e-gly"><em>enhanced key usage</em></a><a href="/windows/desktop/SecGloss/o-gly"><em>object identifiers</em></a> (OIDs) into the certificate. For example, <strong>-eku 1.3.6.1.5.5.7.3.2</strong> inserts the client authentication OID. For definitions of allowable OIDs, see the Wincrypt.h file in CryptoAPI 2.0. | 
| <strong>-h</strong><strong></strong><em>NumChildren</em> | Maximum height of the tree below this certificate. | 
| <strong>-l</strong><strong></strong><em>PolicyLink</em> | Link to SPC agency policy information (for example, a URL). | 
| <strong>-m</strong><strong></strong><em>nMonths</em> | Duration of the validity period. | 
| <strong>-n</strong><strong>"</strong><em>Name</em><strong>"</strong> | Name for the publisher's certificate. This name must conform to the <a href="/windows/desktop/SecGloss/x-gly"><em>X.500</em></a> standard. The simplest method is to use the "CN=<em>MyName</em>" format. For example: <strong>-n "CN=Test"</strong>. | 
| <strong>-nscp</strong> | The Netscape client authentication extension should be included. | 
| <strong>-pe</strong> | Marks the private key as exportable. | 
| <strong>-r</strong> | Creates a self-signed certificate. | 
| <strong>-sc</strong><strong></strong><em>SubjectCertFile</em> | Certificate file name with the existing subject public key to be used. | 
| <strong>-sk</strong><strong></strong><em>SubjectKey</em> | Location of the subject's key container which holds the <a href="/windows/desktop/SecGloss/p-gly"><em>private key</em></a>. If a key container does not exist, one is created. If neither the <strong>-sk</strong> or <strong>-sv</strong> option is used, a default key container is created and used by default. | 
| <strong>-sky</strong><strong></strong><em>SubjectKeySpec</em> | Subject's key specification. <em>SubjectKeySpec</em> must be one of three possible values:<br /><ul><li><strong>Signature</strong> (AT_SIGNATURE key specification)</li><li><strong>Exchange</strong> (AT_KEYEXCHANGE key specification)</li><li>An integer, such as <strong>3</strong></li></ul>For more information, see the Note that follows this table.<br /> | 
| <strong>-sp</strong><strong></strong><em>SubjectProviderName</em> | CryptoAPI provider for subject. The default is the user's provider. For information about CryptoAPI providers, see the CryptoAPI 2.0 documentation. | 
| <strong>-sr</strong><strong></strong><em>SubjectCertStoreLocation</em> | Registry location of the subject's certificate store. <em>SubjectCertStoreLocation</em> must be either <strong>LocalMachine</strong> (registry key HKEY_LOCAL_MACHINE) or <strong>CurrentUser</strong> (registry key HKEY_CURRENT_USER). <strong>CurrentUser</strong> is the default. | 
| <strong>-ss</strong><strong></strong><em>SubjectCertStoreName</em> | Name of the subject's certificate store where the generated certificate will be stored. | 
| <strong>-sv</strong><strong></strong><em>SubjectKeyFile</em> | Name of the subject's .pvk file. If neither the <strong>-sk</strong> or <strong>-sv</strong> option is used, a default key container is created and used by default. | 
| <strong>-sy</strong><strong></strong><em>nSubjectProviderType</em> | CryptoAPI provider type for subject. The default is <a href="/windows/desktop/SecGloss/p-gly"><em>PROV_RSA_FULL</em></a>. For information about CryptoAPI provider types, see the CryptoAPI 2.0 documentation. | 
| <strong>-#</strong><strong></strong><em>SerialNumber</em> | Serial number of the certificate. The maximum value is 2^31. The default is a value generated by the tool that is guaranteed to be unique. | 
| <strong>-$</strong><strong></strong><em>CertificateAuthority</em> | Type of <a href="/windows/desktop/SecGloss/c-gly"><em>certification authority</em></a>. <em>CertificateAuthority</em> must be set to either <strong>commercial</strong> (for certificates to be used by commercial software publishers) or <strong>individual</strong> (for certificates to be used by individual software publishers). | 
| <strong>-?</strong> | Displays the basic options. | 
| <strong>-!</strong> | Displays the extended options. | 




 

> [!Note]  
> If the **-sky** key specification option is used in Internet Explorer version 4.0 or later, the specification must match the key specification indicated by the [*private key*](../secgloss/p-gly.md) file or private [*key container*](../secgloss/k-gly.md). If the key specification option is not used, the key specification indicated by the private key file or private key container will be used. If there is more than one key specification in the key container, MakeCert will first attempt to use the AT\_SIGNATURE key specification. If that fails, MakeCert will try to use AT\_KEYEXCHANGE. Because most users have either an AT\_SIGNATURE key or an AT\_KEYEXCHANGE key, this option does not need to be used in most cases.

 

The following options are only for [*Software Publisher Certificate*](../secgloss/s-gly.md) (SPC) files and private key technology.




| SPC and private key option | Description | 
|----------------------------|-------------|
| <strong>-ic</strong><strong></strong><em>IssuerCertFile</em> | Location of the issuer's certificate. | 
| <strong>-ik</strong><strong></strong><em>IssuerKey</em> | Location of the issuer's key container. The default is the test root key. | 
| <strong>-iky</strong><strong></strong><em>IssuerKeySpec</em> | Issuer's key specification, which must be one of three possible values:<br /><ul><li><strong>Signature</strong> (AT_SIGNATURE key specification)</li><li><strong>Exchange</strong> (AT_KEYEXCHANGE key specification)</li><li>An integer, such as <strong>3</strong></li></ul>For more information, see the Note that follows this table.<br /> | 
| <strong>-ip</strong><strong></strong><em>IssuerProviderName</em> | CryptoAPI provider for issuer. The default is the user's provider. For information about CryptoAPI providers, see the CryptoAPI 2.0 documentation. | 
| <strong>-iv</strong><strong></strong><em>IssuerKeyFile</em> | Issuer's private key file. The default is the test root. | 
| <strong>-iy</strong><strong></strong><em>nIssuerProviderType</em> | CryptoAPI provider type for issuer. The default is <a href="/windows/desktop/SecGloss/p-gly"><em>PROV_RSA_FULL</em></a>. For information about CryptoAPI provider types, see the CryptoAPI 2.0 documentation. | 




 

> [!Note]  
> If the **-iky** key specification option is used in Internet Explorer 4.0 or later, the specification must match the key specification indicated by the [*private key*](../secgloss/p-gly.md) file or private [*key container*](../secgloss/k-gly.md). If the key specification option is not used, the key specification indicated by the private key file or private key container will be used. If there is more than one key specification in the key container, MakeCert will first attempt to use the AT\_SIGNATURE key specification. If that fails, MakeCert will try to use AT\_KEYEXCHANGE. Because most users have either an AT\_SIGNATURE key or an AT\_KEYEXCHANGE key, this option does not need to be used in most cases.

 

The following options are for [*certificate store*](../secgloss/c-gly.md) technology only.



| Certificate store option          | Description                                                                                                                                                                                                                                                                                                                              |
|-----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **-ic** *IssuerCertFile*          | File that contains the issuer's certificate. MakeCert will search in the certificate store for a certificate with an exact match.                                                                                                                                                                                                        |
| **-in** *IssuerNameString*        | Common name of the issuer's certificate. MakeCert will search in the certificate store for a certificate whose common name includes *IssuerNameString*.                                                                                                                                                                                  |
| **-ir** *IssuerCertStoreLocation* | Registry location of the issuer's certificate store. *IssuerCertStoreLocation* must be either **LocalMachine** (registry key HKEY\_LOCAL\_MACHINE) or **CurrentUser** (registry key HKEY\_CURRENT\_USER). **CurrentUser** is the default.                                                                                                |
| **-is** *IssuerCertStoreName*     | Issuer's certificate store that includes the issuer's certificate and its associated private key information. If there is more than one certificate in the store, the user must uniquely identify it by using the **-ic** or **-in** option. If the certificate in the certificate store is not uniquely identified, MakeCert will fail. |



 

 

 
