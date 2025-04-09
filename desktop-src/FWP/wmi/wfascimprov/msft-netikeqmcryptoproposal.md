---
description: Represents a crypto suite to propose in quick mode.
ms.assetid: 4ee6e39c-2358-4e27-a480-e9922770e891
title: MSFT\_NetIKEQMCryptoProposal class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetIKEQMCryptoProposal
- MSFT_NetIKEQMCryptoProposal.HashAlgorithmAH
- MSFT_NetIKEQMCryptoProposal.HashAlgorithmESP
- MSFT_NetIKEQMCryptoProposal.Encapsulation
- MSFT_NetIKEQMCryptoProposal.MaxLifetimeMinutes
- MSFT_NetIKEQMCryptoProposal.AuthenticationMethod
- MSFT_NetIKEQMCryptoProposal.CipherAlgorithm
- MSFT_NetIKEQMCryptoProposal.MaxLifetimeSeconds
- MSFT_NetIKEQMCryptoProposal.MaxLifetimeKilobytes
- MSFT_NetIKEQMCryptoProposal.OtherCipherAlgorithm
- MSFT_NetIKEQMCryptoProposal.HashAlgorithm
- MSFT_NetIKEQMCryptoProposal.OtherHashAlgorithm
- MSFT_NetIKEQMCryptoProposal.OtherAuthenticationMethod
- MSFT_NetIKEQMCryptoProposal.GroupId
- MSFT_NetIKEQMCryptoProposal.VendorID
- MSFT_NetIKEQMCryptoProposal.InstanceID
- MSFT_NetIKEQMCryptoProposal.Caption
- MSFT_NetIKEQMCryptoProposal.Description
- MSFT_NetIKEQMCryptoProposal.ElementName
api_type: 
- DllExport
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetIKEQMCryptoProposal class

Represents a crypto suite to propose in quick mode.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetIKEQMCryptoProposal : MSFT_NetIKECryptoProposal
{
  uint16 HashAlgorithmAH;
  uint16 HashAlgorithmESP;
  uint16 Encapsulation;
  uint32 MaxLifetimeMinutes;
  uint16 AuthenticationMethod;
  uint16 CipherAlgorithm;
  uint64 MaxLifetimeSeconds;
  uint64 MaxLifetimeKilobytes;
  string OtherCipherAlgorithm;
  uint16 HashAlgorithm;
  string OtherHashAlgorithm;
  string OtherAuthenticationMethod;
  uint16 GroupId;
  string VendorID;
  string InstanceID;
  string Caption;
  string Description;
  string ElementName;
};
```

## Members

The **MSFT\_NetIKEQMCryptoProposal** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetIKEQMCryptoProposal** class has these properties.

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

**Encapsulation**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

What type of encapsulation to use.

<dl> <dt>

<span id="AH"></span><span id="ah"></span>**AH** (1)
</dt> <dt>

<span id="ESP"></span><span id="esp"></span>**ESP** (2)
</dt> <dt>

<span id="AH_ESP"></span><span id="ah_esp"></span>**AH/ESP** (3)
</dt> <dt>

<span id="None_"></span><span id="none_"></span><span id="NONE_"></span>**None** (0 )
</dt> </dl>

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

**HashAlgorithmAH**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Hash algorithm to use in AH.

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

**HashAlgorithmESP**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Hash algorithm to use in ESP.

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

The maximum lifetime for a Quick-Mode SA before it must be rekeyed, in kilobytes.

</dd> <dt>

**MaxLifetimeMinutes**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum lifetime for a Quick-Mode SA before it must be rekeyed, in minutes.

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



 

 




