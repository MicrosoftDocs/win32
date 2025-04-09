---
description: Represents an auth proposal that uses certificates to authenticate the remote peer. Instances of this class only exist as embedded instances within a MSFT\_NetIKEP1AuthSet and MSFT\_NetIKEP2AuthSet.
ms.assetid: f1cde1bf-3e6d-403a-bdb8-49e1ad70e36d
title: MSFT\_NetIKECertAuthProposal class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetIKECertAuthProposal
- MSFT_NetIKECertAuthProposal.TrustedCA
- MSFT_NetIKECertAuthProposal.TrustedCAType
- MSFT_NetIKECertAuthProposal.ExcludeCAName
- MSFT_NetIKECertAuthProposal.MapToAccount
- MSFT_NetIKECertAuthProposal.SigningAlgorithm
- MSFT_NetIKECertAuthProposal.CertName
- MSFT_NetIKECertAuthProposal.CertNameType
- MSFT_NetIKECertAuthProposal.EKUs
- MSFT_NetIKECertAuthProposal.Thumbprint
- MSFT_NetIKECertAuthProposal.FollowRenewal
- MSFT_NetIKECertAuthProposal.SelectionCriteria
- MSFT_NetIKECertAuthProposal.ValidationCriteria
- MSFT_NetIKECertAuthProposal.AuthenticationMethod
- MSFT_NetIKECertAuthProposal.MaxLifetimeSeconds
- MSFT_NetIKECertAuthProposal.MaxLifetimeKilobytes
- MSFT_NetIKECertAuthProposal.CipherAlgorithm
- MSFT_NetIKECertAuthProposal.OtherCipherAlgorithm
- MSFT_NetIKECertAuthProposal.HashAlgorithm
- MSFT_NetIKECertAuthProposal.OtherHashAlgorithm
- MSFT_NetIKECertAuthProposal.OtherAuthenticationMethod
- MSFT_NetIKECertAuthProposal.GroupId
- MSFT_NetIKECertAuthProposal.VendorID
- MSFT_NetIKECertAuthProposal.InstanceID
- MSFT_NetIKECertAuthProposal.Caption
- MSFT_NetIKECertAuthProposal.Description
- MSFT_NetIKECertAuthProposal.ElementName
api_type: 
- DllExport
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetIKECertAuthProposal class

Represents an auth proposal that uses certificates to authenticate the remote peer. Instances of this class only exist as embedded instances within a MSFT\_NetIKEP1AuthSet and MSFT\_NetIKEP2AuthSet.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetIKECertAuthProposal : MSFT_NetIKEAuthProposal
{
  string  TrustedCA;
  uint16  TrustedCAType;
  boolean ExcludeCAName;
  boolean MapToAccount;
  uint16  SigningAlgorithm;
  string  CertName;
  uint16  CertNameType;
  string  EKUs[];
  string  Thumbprint;
  boolean FollowRenewal;
  boolean SelectionCriteria;
  boolean ValidationCriteria;
  uint16  AuthenticationMethod;
  uint64  MaxLifetimeSeconds;
  uint64  MaxLifetimeKilobytes;
  uint16  CipherAlgorithm;
  string  OtherCipherAlgorithm;
  uint16  HashAlgorithm;
  string  OtherHashAlgorithm;
  string  OtherAuthenticationMethod;
  uint16  GroupId;
  string  VendorID;
  string  InstanceID;
  string  Caption;
  string  Description;
  string  ElementName;
};
```

## Members

The **MSFT\_NetIKECertAuthProposal** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetIKECertAuthProposal** class has these properties.

<dl> <dt>

**AuthenticationMethod**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the proposed authentication. The list of methods was generated from Appendix A of RFC2409. Note that the enumeration is different than the RFC list and aligns with the values in IKESAEndpoint.AuthenticationMethod.

<dl> <dt>

<span id="Pre-shared_Key"></span><span id="pre-shared_key"></span><span id="PRE-SHARED_KEY"></span>**Pre-shared Key** (2)
</dt> <dt>

<span id="Anonymous"></span><span id="anonymous"></span><span id="ANONYMOUS"></span>**Anonymous** (65001)
</dt> <dt>

<span id="Kerberos__machine_as_principal_"></span><span id="kerberos__machine_as_principal_"></span><span id="KERBEROS__MACHINE_AS_PRINCIPAL_"></span>**Kerberos (machine as principal)** (65002)
</dt> <dt>

<span id="NTLM__machine_as_principal_"></span><span id="ntlm__machine_as_principal_"></span><span id="NTLM__MACHINE_AS_PRINCIPAL_"></span>**NTLM (machine as principal)** (65003)
</dt> <dt>

<span id="Kerberos__user_as_principal_"></span><span id="kerberos__user_as_principal_"></span><span id="KERBEROS__USER_AS_PRINCIPAL_"></span>**Kerberos (user as principal)** (65004)
</dt> <dt>

<span id="NTLM__user_as_principal_"></span><span id="ntlm__user_as_principal_"></span><span id="NTLM__USER_AS_PRINCIPAL_"></span>**NTLM (user as principal)** (65005)
</dt> <dt>

<span id="X.509_Certificates__machine_as_principal_"></span><span id="x.509_certificates__machine_as_principal_"></span><span id="X.509_CERTIFICATES__MACHINE_AS_PRINCIPAL_"></span>**X.509 Certificates (machine as principal)** (65005)
</dt> <dt>

<span id="X.509_Certificates__user_as_principal_"></span><span id="x.509_certificates__user_as_principal_"></span><span id="X.509_CERTIFICATES__USER_AS_PRINCIPAL_"></span>**X.509 Certificates (user as principal)** (65007)
</dt> <dt>

<span id="X.509_Certificates__machine_health__"></span><span id="x.509_certificates__machine_health__"></span><span id="X.509_CERTIFICATES__MACHINE_HEALTH__"></span>**X.509 Certificates (machine health)** (65008 )
</dt> </dl>

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**CertName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name that should be on the certificate.

</dd> <dt>

**CertNameType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The type of name used in CertName.

<dl> <dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>**None** (0)
</dt> <dt>

<span id="DNS"></span><span id="dns"></span>**DNS** (1)
</dt> <dt>

<span id="UPN"></span><span id="upn"></span>**UPN** (2)
</dt> <dt>

<span id="RFC822"></span><span id="rfc822"></span>**RFC822** (3)
</dt> <dt>

<span id="CN"></span><span id="cn"></span>**CN** (4)
</dt> <dt>

<span id="OU"></span><span id="ou"></span>**OU** (5)
</dt> <dt>

<span id="O"></span><span id="o"></span>**O** (6)
</dt> <dt>

<span id="DC_"></span><span id="dc_"></span>**DC** (7 )
</dt> </dl>

</dd> <dt>

**CipherAlgorithm**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**EKUs**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The EKU's to accept.

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**ExcludeCAName**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If this flag is set, certificate authority names are excluded. This flag MUST be set only on first authentications.

</dd> <dt>

**FollowRenewal**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether to follow certificate renewal.

</dd> <dt>

**GroupId**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**HashAlgorithm**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**MapToAccount**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If this flag is set, Windows will attempt to map certificates to domain accounts.

</dd> <dt>

**MaxLifetimeKilobytes**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**MaxLifetimeSeconds**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**OtherAuthenticationMethod**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**OtherCipherAlgorithm**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**OtherHashAlgorithm**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**SelectionCriteria**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether the cert criteria (CertName, EKUs, Thumbprint) should be used when choosing which certificates to offer.

</dd> <dt>

**SigningAlgorithm**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the certificate signing algorithm to use.

<dl> <dt>

<span id="RSA"></span><span id="rsa"></span>**RSA** (1)
</dt> <dt>

<span id="256-bit_Elliptic-Curve_DSA"></span><span id="256-bit_elliptic-curve_dsa"></span><span id="256-BIT_ELLIPTIC-CURVE_DSA"></span>**256-bit Elliptic-Curve DSA** (2)
</dt> <dt>

<span id="384-bit_Elliptic-Curve_DSA_"></span><span id="384-bit_elliptic-curve_dsa_"></span><span id="384-BIT_ELLIPTIC-CURVE_DSA_"></span>**384-bit Elliptic-Curve DSA** (3 )
</dt> </dl>

</dd> <dt>

**Thumbprint**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The thumbprint to accept.

</dd> <dt>

**TrustedCA**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Only certs issued by this CA should be allowed.

</dd> <dt>

**TrustedCAType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether to accept certificates only from the root TrustedCA, or to also accept certificates from Intermediate CA's which are children of the TrustedCA.

<dl> <dt>

<span id="Root_CA"></span><span id="root_ca"></span><span id="ROOT_CA"></span>**Root CA** (1)
</dt> <dt>

<span id="Intermediate_CA_"></span><span id="intermediate_ca_"></span><span id="INTERMEDIATE_CA_"></span>**Intermediate CA** (2 )
</dt> </dl>

</dd> <dt>

**ValidationCriteria**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether the cert criteria (CertName, EKUs, Thumbprint) should be used for validating the certificates presented.

</dd> <dt>

**VendorID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                         |
| MOF<br/>                      | <dl> <dt>WFasCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WFasCim.dll</dt> </dl> |



 

 




