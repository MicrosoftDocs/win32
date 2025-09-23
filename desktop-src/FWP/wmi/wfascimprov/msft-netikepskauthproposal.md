---
description: A Pre-shared Key authentication proposal.
ms.assetid: 1c0ba1ea-4020-44cf-a4f1-496159e21e2c
title: MSFT\_NetIKEPSKAuthProposal class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetIKEPSKAuthProposal
- MSFT_NetIKEPSKAuthProposal.PreSharedKey
- MSFT_NetIKEPSKAuthProposal.AuthenticationMethod
- MSFT_NetIKEPSKAuthProposal.MaxLifetimeSeconds
- MSFT_NetIKEPSKAuthProposal.MaxLifetimeKilobytes
- MSFT_NetIKEPSKAuthProposal.CipherAlgorithm
- MSFT_NetIKEPSKAuthProposal.OtherCipherAlgorithm
- MSFT_NetIKEPSKAuthProposal.HashAlgorithm
- MSFT_NetIKEPSKAuthProposal.OtherHashAlgorithm
- MSFT_NetIKEPSKAuthProposal.OtherAuthenticationMethod
- MSFT_NetIKEPSKAuthProposal.GroupId
- MSFT_NetIKEPSKAuthProposal.VendorID
- MSFT_NetIKEPSKAuthProposal.InstanceID
- MSFT_NetIKEPSKAuthProposal.Caption
- MSFT_NetIKEPSKAuthProposal.Description
- MSFT_NetIKEPSKAuthProposal.ElementName
api_type: 
- DllExport
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetIKEPSKAuthProposal class

A Pre-shared Key authentication proposal.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetIKEPSKAuthProposal : MSFT_NetIKEAuthProposal
{
  string PreSharedKey;
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

The **MSFT\_NetIKEPSKAuthProposal** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetIKEPSKAuthProposal** class has these properties.

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

**PreSharedKey**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The key to use in the authentication.

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



 

 




