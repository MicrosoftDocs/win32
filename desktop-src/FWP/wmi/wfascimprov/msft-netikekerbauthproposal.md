---
description: Represents an auth proposal for Kerberos.
ms.assetid: a1a8b0a7-5180-4cf3-aff9-fab556b9730a
title: MSFT\_NetIKEKerbAuthProposal class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetIKEKerbAuthProposal
- MSFT_NetIKEKerbAuthProposal.KerbProxy
- MSFT_NetIKEKerbAuthProposal.AuthenticationMethod
- MSFT_NetIKEKerbAuthProposal.MaxLifetimeSeconds
- MSFT_NetIKEKerbAuthProposal.MaxLifetimeKilobytes
- MSFT_NetIKEKerbAuthProposal.CipherAlgorithm
- MSFT_NetIKEKerbAuthProposal.OtherCipherAlgorithm
- MSFT_NetIKEKerbAuthProposal.HashAlgorithm
- MSFT_NetIKEKerbAuthProposal.OtherHashAlgorithm
- MSFT_NetIKEKerbAuthProposal.OtherAuthenticationMethod
- MSFT_NetIKEKerbAuthProposal.GroupId
- MSFT_NetIKEKerbAuthProposal.VendorID
- MSFT_NetIKEKerbAuthProposal.InstanceID
- MSFT_NetIKEKerbAuthProposal.Caption
- MSFT_NetIKEKerbAuthProposal.Description
- MSFT_NetIKEKerbAuthProposal.ElementName
api_type: 
- DllExport
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetIKEKerbAuthProposal class

Represents an auth proposal for Kerberos.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetIKEKerbAuthProposal : MSFT_NetIKEAuthProposal
{
  string KerbProxy;
  uint16 AuthenticationMethod;
  uint64 MaxLifetimeSeconds;
  uint64 MaxLifetimeKilobytes;
  uint16 CipherAlgorithm;
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

The **MSFT\_NetIKEKerbAuthProposal** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetIKEKerbAuthProposal** class has these properties.

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

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

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

**KerbProxy**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Kerberos proxy server to use when authenticating remotely.

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



 

 




