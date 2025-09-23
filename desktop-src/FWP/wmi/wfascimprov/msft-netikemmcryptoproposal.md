---
description: Represents a crypto suite to propose in main mode.
ms.assetid: dcb539e6-1ec3-4224-a479-0dd636e28fb1
title: MSFT\_NetIKEMMCryptoProposal class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetIKEMMCryptoProposal
- MSFT_NetIKEMMCryptoProposal.AuthenticationMethod
- MSFT_NetIKEMMCryptoProposal.CipherAlgorithm
- MSFT_NetIKEMMCryptoProposal.HashAlgorithm
- MSFT_NetIKEMMCryptoProposal.GroupID
- MSFT_NetIKEMMCryptoProposal.MaxLifetimeSeconds
- MSFT_NetIKEMMCryptoProposal.MaxLifetimeKilobytes
- MSFT_NetIKEMMCryptoProposal.OtherCipherAlgorithm
- MSFT_NetIKEMMCryptoProposal.OtherHashAlgorithm
- MSFT_NetIKEMMCryptoProposal.OtherAuthenticationMethod
- MSFT_NetIKEMMCryptoProposal.VendorID
- MSFT_NetIKEMMCryptoProposal.InstanceID
- MSFT_NetIKEMMCryptoProposal.Caption
- MSFT_NetIKEMMCryptoProposal.Description
- MSFT_NetIKEMMCryptoProposal.ElementName
api_type: 
- DllExport
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetIKEMMCryptoProposal class

Represents a crypto suite to propose in main mode.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetIKEMMCryptoProposal : MSFT_NetIKECryptoProposal
{
  uint16 AuthenticationMethod;
  uint16 CipherAlgorithm;
  uint16 HashAlgorithm;
  uint16 GroupID;
  uint64 MaxLifetimeSeconds;
  uint64 MaxLifetimeKilobytes;
  string OtherCipherAlgorithm;
  string OtherHashAlgorithm;
  string OtherAuthenticationMethod;
  string VendorID;
  string InstanceID;
  string Caption;
  string Description;
  string ElementName;
};
```

## Members

The **MSFT\_NetIKEMMCryptoProposal** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetIKEMMCryptoProposal** class has these properties.

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

**CipherAlgorithm**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the proposed encryption algorithm.

<dl> <dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>**None** (0)
</dt> <dt>

<span id="DES"></span><span id="des"></span>**DES** (2)
</dt> <dt>

<span id="3DES"></span><span id="3des"></span>**3DES** (6)
</dt> <dt>

<span id="AES-128"></span><span id="aes-128"></span>**AES-128** (65001)
</dt> <dt>

<span id="AES-192"></span><span id="aes-192"></span>**AES-192** (65002)
</dt> <dt>

<span id="AES-256"></span><span id="aes-256"></span>**AES-256** (65003)
</dt> <dt>

<span id="AES-GCM-128"></span><span id="aes-gcm-128"></span>**AES-GCM-128** (65004)
</dt> <dt>

<span id="AES-GCM-192"></span><span id="aes-gcm-192"></span>**AES-GCM-192** (65005)
</dt> <dt>

<span id="AES-GCM-256_"></span><span id="aes-gcm-256_"></span>**AES-GCM-256** (65006 )
</dt> </dl>

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**GroupID**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The property GroupId specifies the proposed phase 1 security association key exchange group. Well-known group identifiers from RFC2412, Appendix E, are: Group 1='768 bit prime', Group 2='1024 bit prime', Group 3 ='Elliptic Curve Group with 155 bit field element', Group 4= 'Large Elliptic Curve Group with 185 bit field element', and Group 5='1536 bit prime'. Note that only groups 1, 2, 14, 19, 20, and 24 are acceptable in Windows 8.

<dl> <dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>**None** (0)
</dt> <dt>

<span id="DH_Group_1"></span><span id="dh_group_1"></span><span id="DH_GROUP_1"></span>**DH Group 1** (1)
</dt> <dt>

<span id="DH_Group_2"></span><span id="dh_group_2"></span><span id="DH_GROUP_2"></span>**DH Group 2** (2)
</dt> <dt>

<span id="DH_Group_14"></span><span id="dh_group_14"></span><span id="DH_GROUP_14"></span>**DH Group 14** (14)
</dt> <dt>

<span id="DH_Group_19"></span><span id="dh_group_19"></span><span id="DH_GROUP_19"></span>**DH Group 19** (19)
</dt> <dt>

<span id="DH_Group_20"></span><span id="dh_group_20"></span><span id="DH_GROUP_20"></span>**DH Group 20** (20)
</dt> <dt>

<span id="DH_Group_24_"></span><span id="dh_group_24_"></span><span id="DH_GROUP_24_"></span>**DH Group 24** (24 )
</dt> </dl>

</dd> <dt>

**HashAlgorithm**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the proposed hash algorithm.

<dl> <dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>**None** (0)
</dt> <dt>

<span id="MD5"></span><span id="md5"></span>**MD5** (2)
</dt> <dt>

<span id="SHA-1"></span><span id="sha-1"></span>**SHA-1** (3)
</dt> <dt>

<span id="SHA-256"></span><span id="sha-256"></span>**SHA-256** (65001)
</dt> <dt>

<span id="SHA-384"></span><span id="sha-384"></span>**SHA-384** (65002)
</dt> <dt>

<span id="AES-GMAC-128"></span><span id="aes-gmac-128"></span>**AES-GMAC-128** (65003)
</dt> <dt>

<span id="AES-GMAC-192"></span><span id="aes-gmac-192"></span>**AES-GMAC-192** (65004)
</dt> <dt>

<span id="AES-GMAC-256_"></span><span id="aes-gmac-256_"></span>**AES-GMAC-256** (65005 )
</dt> </dl>

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

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



 

 




