---
description: Retrieves the validity status of the chain or a specific certificate in the chain.
title: IChain2::Status property
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- IChain2.Status
- IChain.Status
- Chain.Status
api_type:
- COM
api_location:
- Capicom.dll
---

# IChain2::Status property

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**X509Chain Class**](/dotnet/api/system.security.cryptography.x509certificates.x509chain) in the [**System.Security.Cryptography.X509Certificates**](/dotnet/api/system.security.cryptography.x509certificates.publickey.-ctor) namespace.\]

The **Status** property retrieves the validity status of the chain or a specific certificate in the chain.

## Syntax


```VB
Chain.Status( _
  ByVal Index _
) As Long
```



## Property value

A **LONG** value that represents the validity status indicator of the chain or the specified certificate. The following table shows the possible values. This property will contain zero if the chain or specified certificate is valid. Otherwise, this property will contain a combination of one or more of the following values.

<dt>

<span id="CAPICOM_TRUST_IS_NOT_TIME_VALID"></span><span id="capicom_trust_is_not_time_valid"></span>

<span id="CAPICOM_TRUST_IS_NOT_TIME_VALID"></span><span id="capicom_trust_is_not_time_valid"></span>**CAPICOM\_TRUST\_IS\_NOT\_TIME\_VALID** (&H00000001)


</dt> <dd>

This certificate or one of the certificates in the certificate chain is not time valid.

</dd> <dt>

<span id="CAPICOM_TRUST_IS_NOT_TIME_NESTED"></span><span id="capicom_trust_is_not_time_nested"></span>

<span id="CAPICOM_TRUST_IS_NOT_TIME_NESTED"></span><span id="capicom_trust_is_not_time_nested"></span>**CAPICOM\_TRUST\_IS\_NOT\_TIME\_NESTED** (&H00000002)


</dt> <dd>

Certificates in the chain are not properly time nested.

</dd> <dt>

<span id="CAPICOM_TRUST_IS_REVOKED"></span><span id="capicom_trust_is_revoked"></span>

<span id="CAPICOM_TRUST_IS_REVOKED"></span><span id="capicom_trust_is_revoked"></span>**CAPICOM\_TRUST\_IS\_REVOKED** (&H00000004)


</dt> <dd>

Trust for this certificate or one of the certificates in the certificate chain has been revoked.

</dd> <dt>

<span id="CAPICOM_TRUST_IS_NOT_SIGNATURE_VALID"></span><span id="capicom_trust_is_not_signature_valid"></span>

<span id="CAPICOM_TRUST_IS_NOT_SIGNATURE_VALID"></span><span id="capicom_trust_is_not_signature_valid"></span>**CAPICOM\_TRUST\_IS\_NOT\_SIGNATURE\_VALID** (&H00000008)


</dt> <dd>

The certificate or one of the certificates in the certificate chain does not have a valid signature.

</dd> <dt>

<span id="CAPICOM_TRUST_IS_NOT_VALID_FOR_USAGE"></span><span id="capicom_trust_is_not_valid_for_usage"></span>

<span id="CAPICOM_TRUST_IS_NOT_VALID_FOR_USAGE"></span><span id="capicom_trust_is_not_valid_for_usage"></span>**CAPICOM\_TRUST\_IS\_NOT\_VALID\_FOR\_USAGE** (&H00000010)


</dt> <dd>

The certificate or certificate chain is not valid for its proposed usage.

</dd> <dt>

<span id="CAPICOM_TRUST_IS_UNTRUSTED_ROOT"></span><span id="capicom_trust_is_untrusted_root"></span>

<span id="CAPICOM_TRUST_IS_UNTRUSTED_ROOT"></span><span id="capicom_trust_is_untrusted_root"></span>**CAPICOM\_TRUST\_IS\_UNTRUSTED\_ROOT** (&H00000020)


</dt> <dd>

The certificate or certificate chain is based on an untrusted root.

</dd> <dt>

<span id="CAPICOM_TRUST_REVOCATION_STATUS_UNKNOWN"></span><span id="capicom_trust_revocation_status_unknown"></span>

<span id="CAPICOM_TRUST_REVOCATION_STATUS_UNKNOWN"></span><span id="capicom_trust_revocation_status_unknown"></span>**CAPICOM\_TRUST\_REVOCATION\_STATUS\_UNKNOWN** (&H00000040)


</dt> <dd>

The revocation status of the certificate or one of the certificates in the certificate chain is unknown.

</dd> <dt>

<span id="CAPICOM_TRUST_IS_CYCLIC"></span><span id="capicom_trust_is_cyclic"></span>

<span id="CAPICOM_TRUST_IS_CYCLIC"></span><span id="capicom_trust_is_cyclic"></span>**CAPICOM\_TRUST\_IS\_CYCLIC** (&H00000080)


</dt> <dd>

One of the certificates in the chain was issued by a [*certification authority*](../secgloss/c-gly.md) that the original certificate had certified.

</dd> <dt>

<span id="CAPICOM_TRUST_INVALID_EXTENSION"></span><span id="capicom_trust_invalid_extension"></span>

<span id="CAPICOM_TRUST_INVALID_EXTENSION"></span><span id="capicom_trust_invalid_extension"></span>**CAPICOM\_TRUST\_INVALID\_EXTENSION** (&H00000100)


</dt> <dd>

One of the certificates has an extension that is not valid.

</dd> <dt>

<span id="CAPICOM_TRUST_INVALID_POLICY_CONSTRAINTS"></span><span id="capicom_trust_invalid_policy_constraints"></span>

<span id="CAPICOM_TRUST_INVALID_POLICY_CONSTRAINTS"></span><span id="capicom_trust_invalid_policy_constraints"></span>**CAPICOM\_TRUST\_INVALID\_POLICY\_CONSTRAINTS** (&H00000200)


</dt> <dd>

The certificate or one of the certificates in the certificate chain has a policy constraints extension, and one of the issued certificates has a disallowed policy mapping extension or does not have a required issuance policies extension.

</dd> <dt>

<span id="CAPICOM_TRUST_INVALID_BASIC_CONSTRAINTS"></span><span id="capicom_trust_invalid_basic_constraints"></span>

<span id="CAPICOM_TRUST_INVALID_BASIC_CONSTRAINTS"></span><span id="capicom_trust_invalid_basic_constraints"></span>**CAPICOM\_TRUST\_INVALID\_BASIC\_CONSTRAINTS** (&H00000400)


</dt> <dd>

The certificate or one of the certificates in the certificate chain has a basic constraints extension, and either the certificate cannot be used to issue other certificates, or the chain path length has been exceeded.

</dd> <dt>

<span id="CAPICOM_TRUST_INVALID_NAME_CONSTRAINTS"></span><span id="capicom_trust_invalid_name_constraints"></span>

<span id="CAPICOM_TRUST_INVALID_NAME_CONSTRAINTS"></span><span id="capicom_trust_invalid_name_constraints"></span>**CAPICOM\_TRUST\_INVALID\_NAME\_CONSTRAINTS** (&H00000800)


</dt> <dd>

The certificate or one of the certificates in the certificate chain has a name constraints extension that is not valid.

</dd> <dt>

<span id="CAPICOM_TRUST_HAS_NOT_SUPPORTED_NAME_CONSTRAINT"></span><span id="capicom_trust_has_not_supported_name_constraint"></span>

<span id="CAPICOM_TRUST_HAS_NOT_SUPPORTED_NAME_CONSTRAINT"></span><span id="capicom_trust_has_not_supported_name_constraint"></span>**CAPICOM\_TRUST\_HAS\_NOT\_SUPPORTED\_NAME\_CONSTRAINT** (&H00001000)


</dt> <dd>

The certificate or one of the certificates in the certificate chain has a name constraints extension that contains unsupported fields. The minimum and maximum fields are not supported. Thus minimum must always be zero and maximum must always be absent. Only UPN is supported for an Other Name. The following alternative name choices are not supported:

-   X400 Address
-   EDI Party Name
-   Registered Id

</dd> <dt>

<span id="CAPICOM_TRUST_HAS_NOT_DEFINED_NAME_CONSTRAINT"></span><span id="capicom_trust_has_not_defined_name_constraint"></span>

<span id="CAPICOM_TRUST_HAS_NOT_DEFINED_NAME_CONSTRAINT"></span><span id="capicom_trust_has_not_defined_name_constraint"></span>**CAPICOM\_TRUST\_HAS\_NOT\_DEFINED\_NAME\_CONSTRAINT** (&H00002000)


</dt> <dd>

The certificate or one of the certificates in the certificate chain has a name constraints extension, and a name constraint is missing for one of the name choices in the end certificate.

</dd> <dt>

<span id="CAPICOM_TRUST_HAS_NOT_PERMITTED_NAME_CONSTRAINT"></span><span id="capicom_trust_has_not_permitted_name_constraint"></span>

<span id="CAPICOM_TRUST_HAS_NOT_PERMITTED_NAME_CONSTRAINT"></span><span id="capicom_trust_has_not_permitted_name_constraint"></span>**CAPICOM\_TRUST\_HAS\_NOT\_PERMITTED\_NAME\_CONSTRAINT** (&H00004000)


</dt> <dd>

The certificate or one of the certificates in the certificate chain has a name constraints extension, and there is not a permitted name constraint for one of the name choices in the end certificate.

</dd> <dt>

<span id="CAPICOM_TRUST_HAS_EXCLUDED_NAME_CONSTRAINT"></span><span id="capicom_trust_has_excluded_name_constraint"></span>

<span id="CAPICOM_TRUST_HAS_EXCLUDED_NAME_CONSTRAINT"></span><span id="capicom_trust_has_excluded_name_constraint"></span>**CAPICOM\_TRUST\_HAS\_EXCLUDED\_NAME\_CONSTRAINT** (&H00008000)


</dt> <dd>

The certificate or one of the certificates in the certificate chain has a name constraints extension, and one of the name choices in the end certificate is explicitly excluded.

</dd> <dt>

<span id="CAPICOM_TRUST_IS_OFFLINE_REVOCATION"></span><span id="capicom_trust_is_offline_revocation"></span>

<span id="CAPICOM_TRUST_IS_OFFLINE_REVOCATION"></span><span id="capicom_trust_is_offline_revocation"></span>**CAPICOM\_TRUST\_IS\_OFFLINE\_REVOCATION** (&H01000000)


</dt> <dd>

The revocation status of the certificate or one of the certificates in the certificate chain is either offline or stale.

</dd> <dt>

<span id="CAPICOM_TRUST_NO_ISSUANCE_CHAIN_POLICY"></span><span id="capicom_trust_no_issuance_chain_policy"></span>

<span id="CAPICOM_TRUST_NO_ISSUANCE_CHAIN_POLICY"></span><span id="capicom_trust_no_issuance_chain_policy"></span>**CAPICOM\_TRUST\_NO\_ISSUANCE\_CHAIN\_POLICY** (&H02000000)


</dt> <dd>

The end certificate does not have any resultant issuance policies, and one of the issuing CA certificates has a policy constraints extension requiring it.

</dd> <dt>

<span id="CAPICOM_TRUST_IS_PARTIAL_CHAIN"></span><span id="capicom_trust_is_partial_chain"></span>

<span id="CAPICOM_TRUST_IS_PARTIAL_CHAIN"></span><span id="capicom_trust_is_partial_chain"></span>**CAPICOM\_TRUST\_IS\_PARTIAL\_CHAIN** (&H00010000)


</dt> <dd>

The certificate chain is not compete.

</dd> <dt>

<span id="CAPICOM_TRUST_CTL_IS_NOT_TIME_VALID"></span><span id="capicom_trust_ctl_is_not_time_valid"></span>

<span id="CAPICOM_TRUST_CTL_IS_NOT_TIME_VALID"></span><span id="capicom_trust_ctl_is_not_time_valid"></span>**CAPICOM\_TRUST\_CTL\_IS\_NOT\_TIME\_VALID** (&H00020000)


</dt> <dd>

A CTL used to create this chain was not time valid.

</dd> <dt>

<span id="CAPICOM_TRUST_CTL_IS_NOT_SIGNATURE_VALID"></span><span id="capicom_trust_ctl_is_not_signature_valid"></span>

<span id="CAPICOM_TRUST_CTL_IS_NOT_SIGNATURE_VALID"></span><span id="capicom_trust_ctl_is_not_signature_valid"></span>**CAPICOM\_TRUST\_CTL\_IS\_NOT\_SIGNATURE\_VALID** (&H00040000)


</dt> <dd>

A CTL used to create this chain did not have a valid signature.

</dd> <dt>

<span id="CAPICOM_TRUST_CTL_IS_NOT_VALID_FOR_USAGE"></span><span id="capicom_trust_ctl_is_not_valid_for_usage"></span>

<span id="CAPICOM_TRUST_CTL_IS_NOT_VALID_FOR_USAGE"></span><span id="capicom_trust_ctl_is_not_valid_for_usage"></span>**CAPICOM\_TRUST\_CTL\_IS\_NOT\_VALID\_FOR\_USAGE** (&H00080000)


</dt> <dd>

A CTL used to create this chain is not valid for this usage.

</dd> </dl>

## Requirements



| Requirement | Value |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



 

 
