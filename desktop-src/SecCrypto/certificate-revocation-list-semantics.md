---
description: Learn how Crypt32 uses CRLs for online revocation checking and how CRL pre-fetching and partitioning can be used to improve performance.
title: Crypt32 certificate revocation list (CRL) semantics
ms.topic: concept-article
ms.date: 10/10/2024
#customer intent: As a Windows developer, I want to learn how Crypt32 uses CRLs for online revocation checking and how CRL pre-fetching and partitioning can be used to improve performance.
---

# Crypt32 certificate revocation list (CRL) semantics

Crypt32 supports certificate revocation list (CRL) semantics for online revocation checking. This article provides information on how Crypt32 uses CRLs for online revocation checking and how CRL pre-fetching and partitioning can be used to improve performance.

## Introduction

When the Crypt32 [CertGetCertificateChain](/windows/win32/api/wincrypt/nf-wincrypt-certgetcertificatechain) API is called with online revocation enabled, it will attempt to retrieve a time valid OCSP response or CRL as follows:

- Check if a time valid stapled OCSP response was included in the handshake.
- Check if we have a time valid OCSP response or CRL in the user’s Cryptnet URL cache.
- Check if we have a time valid CRL in a system store, such as HKLM\CA.
- For OCSP URL in the subject certificate’s AIA extension, attempt to download the OCSP response from the OCSP server.
  - For success, add the OCSP response to the user’s Cryptnet URL cache.
- For CRL CDP extension in the subject certificate, attempt to download the CRL from the certificate authority (CA)’s CRL server.
  - For success, add the CRL to the user’s Cryptnet URL cache.

For a CRL added to the [Cryptnet URL cache](/windows/win32/api/wincrypt/ns-wincrypt-cryptnet_url_cache_pre_fetch_info), the next CRL will be retrieved before it expires if the CRL has the following extension: “1.3.6.1.4.1.311.21.4” (Next CRL Publish). By adding this extension, only the initial CRL download will take place during the certificate validation. See [CRL Pre-Fetching](#crl-pre-fetching) section for more information on how Crypt32 uses this extension to pre-fetch the next CRL.

If a CA issues a high volume of certificates, then, the number of revoked entries on a CRL could also become large, increasing the size of the CRL. To keep the size of the CRL in check, Microsoft recommends and supports CRL partitioning via the"2.5.29.28" (Issuing Distribution Point) extension added to the downloaded CRL. See [CRL Partitioning](#crl-partitioning) section for more information on how Crypt32 supports CRL partitioning via this extension.

CA’s considering dropping support for OCSP and only supporting CRLs need to consider the impact this will have on applications calling the **CertGetCertificateChain** API with online revocation enabled:

- On the first validation, the calling application will do an on demand CRL download and will block the API from completing until the CRL is downloaded.
  - For high volume TLS servers, there will be corresponding high volume downloads from the CA’s CRL server.
  - If the CRL becomes large, it will have a direct impact on the server being able to handle a high volume of downloads.
    - The size of the CRL can be limited by supporting partitioned CRLs.
- Subsequent validations will use the cached CRL until the CRL expires. When the CRL expires, the above will be repeated for the next validation.
  - This on demand CRL download can be avoided by adding the Next CRL Publish extension.

The following sections provide information on CRL pre-fetching and partitioning for improving online revocation performance where only CRLs are used.

## CRL pre-fetching

An encoded CRL has the following two fields indicating when the CRL was published and how long the client can cache before needing to retrieve the next published CRL.

```cpp
ThisUpdate    GeneralizedTime,
NextUpdate    GeneralizedTime OPTIONAL,
```

If *NextUpdate* is missing, this is the last CRL to be published and will never expire.

A CRL may contain the “1.3.6.1.4.1.311.21.4” (Next CRL Publish) extension which is also encoded as *GeneralizedTime*. When this extension is present, Crypt32 will attempt to pre-fetch the next published CRL after this *PublishTime* and before *NextUpdate* as follows:

Given, `PublishPeriod = NextUpdate – PublishTime`. The following three configuration parameters are used to determine the start and end of the *PreFetchPeriod*:

- *AfterPublishPreFetchDivisor*
  - The start of the *PreFetchPeriod* is delayed after the *PublishTime* by dividing the *PublishPeriod* by this divisor.
  - Default of 10
- *BeforeNextUpdatePreFetchDivisor*
  - The finish of the *PreFetchPeriod* occurs before *NextUpdate* by dividing the *PublishPeriod* by this divisor.
  - Default of 20
- *MinPreFetchPeriod*
  - Given, `PreFetchPeriod = PreFetchPeriodFinishTime – PreFetchPeriodStartTime`. Pre-Fetching is only enabled if the *PreFetchPeriod* exceeds this minimum.
  - Default of 1 hour

Given the above calculated *PreFetchPeriod*, a random time is picked within this *PreFetchPeriod* for each client to pre-fetch and download the published CRL from the server.

Some example times and the corresponding *PreFetchPeriod* using the default configuration values.

CRL is valid for two days and published every day:

```output
ThisUpdate:  Nov 05 08:00 
NextUpdate:  Nov 07 08:00 
PublishTime: Nov 06 08:00 

PublishPeriod = 24 hours 
PreFetchPeriodStartTime  = PublishTime + 24/10 (2.4 hours) 
PreFetchPeriodFinishTime = NextUpdate – 24/20 (1.2 hours) 

PreFetchPeriod = Nov 06 10:24 .. Nov 07 06:48 = 20:24  

Clients would randomly pre-fetch in the above PreFetchPeriod. 
```

CRL is valid for eight days and published every four days:

```output
ThisUpdate:  Nov 03 08:00 
NextUpdate:  Nov 11 08:00 
PublishTime: Nov 07 08:00 

PublishPeriod = 96 hours 
PreFetchPeriodStartTime  = PublishTime + 96/10 (9.6 hours) 
PreFetchPeriodFinishTime = NextUpdate – 96/20 (4.8 hours) 

PreFetchPeriod = Nov 07 17:36 .. Nov 11 03:12 = 81:36 

Clients would randomly pre-fetch in the above PreFetchPeriod 
```

>[!NOTE]
> If the pre-fetched CRL isn’t used by the client, then, the above pre-fetching will be stopped until the client initiates a new on demand download for this CRL.

## CRL partitioning

This section provides information on how Crypt32 supports CRL partitioning.

### Example

The following is an example of a commonly formatted CDP and identity provider (IDP) extension used for CRL partitioning.

For the first partition of certificates issued from the CA:

```output
Cert CDP:
[1]CRL Distribution Point
     Distribution Point Name:
          Full Name:
               URL=http://crl.godaddy.com/first.crl

CRL IDP:
Distribution Point Name:
     Full Name:
               URL=http://crl.godaddy.com/first.crl
Only Contains User Certs=No
Only Contains CA Certs=No
Indirect CRL=No
```

For the second partition of certificates issued from the CA, points to a different CRL in both the CDP and IDP:

```output
Cert CDP:
[1]CRL Distribution Point
     Distribution Point Name:
          Full Name:
               URL=http://crl.godaddy.com/second.crl

CRL IDP:
Distribution Point Name:
     Full Name:
               URL=http://crl.godaddy.com/second.crl
Only Contains User Certs=No
Only Contains CA Certs=No
Indirect CRL=No
```

As you can see, the same single http CRL URL is used in both the CDP and IDP. Also, the partitioned CRLs are directly signed by the CA and are applicable to both CAs and end user certs.

The next section provides details on the ASN.1 encoding of the IDP and CDP extensions and what is supported by Crypt32.

### Details

This is the ASN.1 for the Issuing Distribution Point (IDP) extension ("2.5.29.28"):

```cpp
--------------------------------------------
-- CRL Issuing Distribution Point Extension
--------------------------------------------
IssuingDistributionPoint ::= SEQUENCE {
    issuingDistributionPoint    [0] EXPLICIT DistributionPointName OPTIONAL,
    onlyContainsUserCerts       [1] IMPLICIT BOOLEAN DEFAULT FALSE,
    onlyContainsCACerts         [2] IMPLICIT BOOLEAN DEFAULT FALSE,
    onlySomeReasons             [3] IMPLICIT ReasonFlags OPTIONAL,
    indirectCRL                 [4] IMPLICIT BOOLEAN DEFAULT FALSE
} --#public—

DistributionPointName ::= CHOICE {
    fullName                [0] IMPLICIT GeneralNames,
    nameRelativeToCRLIssuer [1] IMPLICIT RelativeDistinguishedName
}

GeneralNames ::= SEQUENCE OF GeneralName

GeneralName ::= CHOICE {
    otherName               [0] IMPLICIT OtherName,
    rfc822Name              [1] IMPLICIT IA5STRING,
    dNSName                 [2] IMPLICIT IA5STRING,
    x400Address             [3] IMPLICIT SeqOfAny,
    directoryName           [4] EXPLICIT NOCOPYANY,    -- really Name
    ediPartyName            [5] IMPLICIT SeqOfAny,
    uniformResourceLocator  [6] IMPLICIT IA5STRING,
    iPAddress               [7] IMPLICIT OCTETSTRING,
    registeredID            [8] IMPLICIT EncodedObjectID
}
```

If a CRL has an IDP, the Windows Client will proceed as follows:

- Ignore IDPs having:
  - *onlySomeReasons*
  - *indirectCRL*
- Only support IDPs with the *fullName* choice.
  - The CRL CDP must also have the fullName choice.
- If *onlyContainsUserCerts* or *onlyContainsCACerts*:
  - Use certificate’s basic constraints extension to determine if the IDP is applicable to the certificate.

This is the ASN.1 for the CDP extension in a certificate:

```cpp
--------------------------------------------
-- CRL Distribution Points Extension
--------------------------------------------
CRLDistributionPoints ::= SEQUENCE OF DistributionPoint

DistributionPoint ::= SEQUENCE {
    distributionPoint       [0] EXPLICIT DistributionPointName OPTIONAL,
    reasons                 [1] IMPLICIT ReasonFlags OPTIONAL,
    cRLIssuer               [2] IMPLICIT GeneralNames OPTIONAL
}

DistributionPointName see above
```

A Windows client will:

- Iterate through the IDP’s sequence of *GeneralNames* until a match with a CDP name:
  - Iterate through the CDP’s sequence of *DistributionPoints*:
    - Skip CDP *DistributionPoint* having:
      - *reasons*
      - *cRLIssuer*
    - Skip CDP *DistributionPoint* if it doesn’t have a *fullName* choice for *DistributionPointName*.
    - Iterate through the CDP’s sequence of *GeneralNames*:
      - Check if IDP and CDP *GeneralName* matches
        - If **IsSameGeneralName()**, we have a match and the CRL can be used for the subject certificate.

**IsSameGeneralName**(IDP_GeneralName, CDP_GeneralName)

The IDP and CDP must have the same *GeneralName* choice. For same choice compare the IDP and CDP name according to the choice:

- rfc822Name
  - Case insensitive string comparison. No % character normalization.
- dNSName
  - Case insensitive string comparison. No % character normalization.
- uniformResourceLocator (URL)
  - Case insensitive string comparison. No % character normalization.
- otherName
  - The OID and OID specific binary value are compared.
- registeredID
  - The OIDs are compared.
- directoryName
  - The encoded name bytes are compared.
- iPAddress
  - The encoded OCTET bytes are compared.
- x400Address
  - Not supported.
- ediPartyName
  - Not supported.

The expectation is that the uniformResourceLocator *GeneralName* choice will be used.

## Related content

[CertGetCertificateChain](/windows/win32/api/wincrypt/nf-wincrypt-certgetcertificatechain)

[CertGetCRLContextProperty](/windows/win32/api/wincrypt/nf-wincrypt-certgetcrlcontextproperty)

[Cryptography Functions](cryptography-functions.md)
