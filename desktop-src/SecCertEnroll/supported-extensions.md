---
description: You can use the IX509Extension interface to define an arbitrary extension.
ms.assetid: 025447f4-98d0-4cb8-b546-4797b7e60722
title: Supported Extensions
ms.topic: article
ms.date: 04/21/2023
---

# Supported Extensions

You can use the [**IX509Extension**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extension) interface to define an arbitrary extension. The Certificate Enrollment API also provides interfaces derived from **IX509Extension** to enable you to easily create any of the most common extensions. The following list identifies the common extensions supported by Microsoft certification authorities, and the object identifiers and interfaces that you can use to create them.

## AlternativeNames

The alternative names extension can be used to define one or more alternative name forms for the subject of the certificate request. Example alternative forms include email addresses, DNS names, IP addresses, and URIs.

**Interface:** [**IX509ExtensionAlternativeNames**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensionalternativenames)

**OID:** XCN\_OID\_SUBJECT\_ALT\_NAME2 (2.5.29.17)

## AuthorityInformationAccess

The authority information access extension identifies how to access CA information and services. The extension value contains a sequence of URIs.

**Interface:** [**IX509Extension**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extension)

**OID:** XCN\_OID\_AUTHORITY\_INFO\_ACCESS (1.3.6.1.5.5.7.1.1)

## AuthorityKeyIdentifier

The authority key identifier extension enables identification of the CA public key that corresponds to the CA private key that signed an issued certificate. It is used by certificate path building software on a Windows server to find the CA certificate. When a CA issues a certificate, the extension value is set equal to the **SubjectKeyIdentifier** extension in the CA signing certificate. The value is typically a SHA-1 hash of the public key.

**Interface:** [**IX509ExtensionAuthorityKeyIdentifier**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensionauthoritykeyidentifier)

**OID:** XCN\_OID\_AUTHORITY\_KEY\_IDENTIFIER2 (2.5.29.35)

## BasicConstraints

The basic constraints extension can be used to identify whether the entity can be used as a certification authority (CA) and, if so, the number of subordinate CAs that can exist beneath it in the certificate chain.

**Interface:** [**IX509ExtensionBasicConstraints**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensionbasicconstraints)

**OID:** XCN\_OID\_BASIC\_CONSTRAINTS2 (2.5.29.19)

## CertificatePolicies

The certificate policies extension can be used to identify the policies under which the certificate has been issued and the purposes for it can be used. These are identified by a collection of object identifiers (OIDs). Policies are customized for the requirements of an organization.

**Interface:** [**IX509ExtensionCertificatePolicies**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensioncertificatepolicies)

**OID:** XCN\_OID\_CERT\_POLICIES (2.5.29.32)

## CrlDistributionPoints

The certificate revocation list (CRL) distribution points extension contains the URI of the base certificate revocation list (CRL).

**Interface:** [**IX509Extension**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extension)

**OID:** XCN\_OID\_CRL\_DIST\_POINTS (2.5.29.31)

## EnhancedKeyUsage

The enhanced key usage extension can be used to define one or more uses of the public key contained in the certificate.

**Interface:** [**IX509ExtensionEnhancedKeyUsage**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensionenhancedkeyusage)

**OID:** XCN\_OID\_ENHANCED\_KEY\_USAGE (2.5.29.37)

## FreshestCRL

The freshest CRL extension contains the URI of the delta CRL. The same ASN.1 syntax is used for this extension and the **CrlDistributionPoints** extension.

**Interface:** [**IX509Extension**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extension)

**OID:** XCN\_OID\_FRESHEST\_CRL (2.5.29.46)

## KeyUsage

The key usage extension can be used to define restrictions on the operations that can be performed by the public key contained in the certificate. For example, you can specify that the public key be used only to create a digital signature, sign a certificate revocation list (CRL), or encrypt another key.

**Interface:** [**IX509ExtensionKeyUsage**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensionkeyusage)

**OID:** XCN\_OID\_KEY\_USAGE (2.5.29.15)

## MSApplicationPolicies

The Microsoft application policies extension can be used by an application to filter certificates on the basis of permitted use. Permitted uses are identified by OIDs. This extension is similar to the **EnhancedKeyUsage** extension but with stricter semantics applied to the parent CA. The extension is Microsoft specific. For non-Windows-based verifiers that do not support this extension, this extension can be ignored—even when marked critical—if the ExtendedKeyUsage extension is also present.

**Interface:** [**IX509ExtensionMSApplicationPolicies**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensionmsapplicationpolicies)

**OID:** XCN\_OID\_APPLICATION\_CERT\_POLICIES (1.3.6.1.4.1.311.21.10)

## NameConstraints

The name constraints extension is used to identify the namespace within which all subject names of certificates in a certificate hierarchy must be located. The extension is used only in a CA certificate.

**Interface:** [**IX509Extension**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extension)

**OID:** XCN\_OID\_NAME\_CONSTRAINTS (2.5.29.30)

## PolicyConstraints

The policy constraints extension is added to CA certificates to constrain path validation by prohibiting policy mapping or by requiring that each certificate in the hierarchy contain an acceptable policy identifier.

**Interface:** [**IX509Extension**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extension)

**OID:** XCN\_OID\_POLICY\_CONSTRAINTS (2.5.29.36)

## PolicyMappings

The policy mappings extension is used to identify the policies in a subordinate CA that correspond to policies in the issuing CA. The extension value contains a sequence of issuing CA and subordinate CA policy mappings represented by object identifiers.

**Interface:** [**IX509Extension**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extension)

**OID:** XCN\_OID\_POLICY\_MAPPINGS (2.5.29.33)

## PrivateKeyUsagePeriod

The private key usage period extension is used to specify a different validity period for the private key than for the certificate with which the key is associated.

**Interface:** [**IX509Extension**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extension)

**OID:** XCN\_OID\_PRIVATEKEY\_USAGE\_PERIOD (2.5.29.16)

## SmimeCapabilities

The Secure/Multipurpose Internet Mail Extensions (S/MIME) capabilities extension can be used to report an email recipient's decryption capabilities to the sender of the email message so that the sender can choose the most secure encryption algorithm supported by both parties. The extension value contains a collection of symmetric encryption algorithm OIDs and an optional encryption strength for each.

**Interface:** [**IX509ExtensionSmimeCapabilities**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensionsmimecapabilities)

**OID:** XCN\_OID\_RSA\_SMIMECapabilities (1.2.840.113549.1.9.15)

## SubjectDirectoryAttributes

The subject directory attributes extension can be used to convey identification attributes such as the nationality of the certificate subject. The extension value is a sequence of OID-value pairs.

**Interface:** [**IX509Extension**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extension)

**OID:** XCN\_OID\_SUBJECT\_DIR\_ATTRS (2.5.29.9)

## SubjectKeyIdentifier

The subject key identifier extension can be used to differentiate between multiple public keys held by the certificate subject. The extension value is typically a SHA-1 hash of the key.

**Interface:** [**IX509ExtensionSubjectKeyIdentifier**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensionsubjectkeyidentifier)

**OID:** XCN\_OID\_SUBJECT\_KEY\_IDENTIFIER (2.5.29.14)

## Template

The template extension can be used to identify the version 2 template to use when issuing or renewing a certificate. The extension value contains the template OID and optional version information. The extension is Microsoft specific.

**Interface:** [**IX509ExtensionTemplate**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensiontemplate)

**OID:** XCN\_OID\_CERTIFICATE\_TEMPLATE (1.3.6.1.4.1.311.21.7)

## TemplateName

The template name extension can be used to identify the version 1 template to use when issuing or renewing a certificate. The extension value contains the name of the template. The extension is Microsoft specific.

**Interface:** [**IX509ExtensionTemplateName**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509extensiontemplatename)

**OID:** XCN\_OID\_ENROLL\_CERTTYPE\_EXTENSION (1.3.6.1.4.1.311.20.2)

## Related topics

<dl> <dt>

[Extensions](extensions.md)
</dt> </dl>

 

 



