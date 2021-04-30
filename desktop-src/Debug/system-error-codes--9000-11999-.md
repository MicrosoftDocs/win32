---
description: Describes error codes 9000-11999 defined in the WinError.h header file and is intended for developers.
ms.assetid: 27fe3fee-4ae3-43f1-a1f2-91c935e9851b
title: System Error Codes (9000-11999) (WinError.h)
ms.topic: reference
ms.date: 07/18/2019
---

# System Error Codes (9000-11999)

> [!NOTE]
> This information is intended for developers debugging system errors. For other errors, such as issues with Windows Update, there is a list of resources on the [Error codes](system-error-codes.md) page.

The following list describes [system error codes](system-error-codes.md) (errors 9000 to 11999). They are returned by the [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) function when many functions fail. To retrieve the description text for the error in your application, use the [**FormatMessage**](/windows/desktop/api/WinBase/nf-winbase-formatmessage) function with the **FORMAT\_MESSAGE\_FROM\_SYSTEM** flag.

<dl> <dt>

<span id="DNS_ERROR_RCODE_FORMAT_ERROR"></span><span id="dns_error_rcode_format_error"></span>**DNS\_ERROR\_RCODE\_FORMAT\_ERROR**
</dt> <dd> <dl> <dt>

9001 (0x2329)
</dt> <dt>



DNS server unable to interpret format.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_RCODE_SERVER_FAILURE"></span><span id="dns_error_rcode_server_failure"></span>**DNS\_ERROR\_RCODE\_SERVER\_FAILURE**
</dt> <dd> <dl> <dt>

9002 (0x232A)
</dt> <dt>



DNS server failure.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_RCODE_NAME_ERROR"></span><span id="dns_error_rcode_name_error"></span>**DNS\_ERROR\_RCODE\_NAME\_ERROR**
</dt> <dd> <dl> <dt>

9003 (0x232B)
</dt> <dt>



DNS name does not exist.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_RCODE_NOT_IMPLEMENTED"></span><span id="dns_error_rcode_not_implemented"></span>**DNS\_ERROR\_RCODE\_NOT\_IMPLEMENTED**
</dt> <dd> <dl> <dt>

9004 (0x232C)
</dt> <dt>



DNS request not supported by name server.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_RCODE_REFUSED"></span><span id="dns_error_rcode_refused"></span>**DNS\_ERROR\_RCODE\_REFUSED**
</dt> <dd> <dl> <dt>

9005 (0x232D)
</dt> <dt>



DNS operation refused.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_RCODE_YXDOMAIN"></span><span id="dns_error_rcode_yxdomain"></span>**DNS\_ERROR\_RCODE\_YXDOMAIN**
</dt> <dd> <dl> <dt>

9006 (0x232E)
</dt> <dt>



DNS name that ought not exist, does exist.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_RCODE_YXRRSET"></span><span id="dns_error_rcode_yxrrset"></span>**DNS\_ERROR\_RCODE\_YXRRSET**
</dt> <dd> <dl> <dt>

9007 (0x232F)
</dt> <dt>



DNS RR set that ought not exist, does exist.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_RCODE_NXRRSET"></span><span id="dns_error_rcode_nxrrset"></span>**DNS\_ERROR\_RCODE\_NXRRSET**
</dt> <dd> <dl> <dt>

9008 (0x2330)
</dt> <dt>



DNS RR set that ought to exist, does not exist.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_RCODE_NOTAUTH"></span><span id="dns_error_rcode_notauth"></span>**DNS\_ERROR\_RCODE\_NOTAUTH**
</dt> <dd> <dl> <dt>

9009 (0x2331)
</dt> <dt>



DNS server not authoritative for zone.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_RCODE_NOTZONE"></span><span id="dns_error_rcode_notzone"></span>**DNS\_ERROR\_RCODE\_NOTZONE**
</dt> <dd> <dl> <dt>

9010 (0x2332)
</dt> <dt>



DNS name in update or prereq is not in zone.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_RCODE_BADSIG"></span><span id="dns_error_rcode_badsig"></span>**DNS\_ERROR\_RCODE\_BADSIG**
</dt> <dd> <dl> <dt>

9016 (0x2338)
</dt> <dt>



DNS signature failed to verify.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_RCODE_BADKEY"></span><span id="dns_error_rcode_badkey"></span>**DNS\_ERROR\_RCODE\_BADKEY**
</dt> <dd> <dl> <dt>

9017 (0x2339)
</dt> <dt>



DNS bad key.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_RCODE_BADTIME"></span><span id="dns_error_rcode_badtime"></span>**DNS\_ERROR\_RCODE\_BADTIME**
</dt> <dd> <dl> <dt>

9018 (0x233A)
</dt> <dt>



DNS signature validity expired.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_KEYMASTER_REQUIRED"></span><span id="dns_error_keymaster_required"></span>**DNS\_ERROR\_KEYMASTER\_REQUIRED**
</dt> <dd> <dl> <dt>

9101 (0x238D)
</dt> <dt>



Only the DNS server acting as the key master for the zone may perform this operation.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_NOT_ALLOWED_ON_SIGNED_ZONE"></span><span id="dns_error_not_allowed_on_signed_zone"></span>**DNS\_ERROR\_NOT\_ALLOWED\_ON\_SIGNED\_ZONE**
</dt> <dd> <dl> <dt>

9102 (0x238E)
</dt> <dt>



This operation is not allowed on a zone that is signed or has signing keys.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_NSEC3_INCOMPATIBLE_WITH_RSA_SHA1"></span><span id="dns_error_nsec3_incompatible_with_rsa_sha1"></span>**DNS\_ERROR\_NSEC3\_INCOMPATIBLE\_WITH\_RSA\_SHA1**
</dt> <dd> <dl> <dt>

9103 (0x238F)
</dt> <dt>



NSEC3 is not compatible with the RSA-SHA-1 algorithm. Choose a different algorithm or use NSEC.

This value was also named **DNS\_ERROR\_INVALID\_NSEC3\_PARAMETERS**


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_NOT_ENOUGH_SIGNING_KEY_DESCRIPTORS"></span><span id="dns_error_not_enough_signing_key_descriptors"></span>**DNS\_ERROR\_NOT\_ENOUGH\_SIGNING\_KEY\_DESCRIPTORS**
</dt> <dd> <dl> <dt>

9104 (0x2390)
</dt> <dt>



The zone does not have enough signing keys. There must be at least one key signing key (KSK) and at least one zone signing key (ZSK).


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_UNSUPPORTED_ALGORITHM"></span><span id="dns_error_unsupported_algorithm"></span>**DNS\_ERROR\_UNSUPPORTED\_ALGORITHM**
</dt> <dd> <dl> <dt>

9105 (0x2391)
</dt> <dt>



The specified algorithm is not supported.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_INVALID_KEY_SIZE"></span><span id="dns_error_invalid_key_size"></span>**DNS\_ERROR\_INVALID\_KEY\_SIZE**
</dt> <dd> <dl> <dt>

9106 (0x2392)
</dt> <dt>



The specified key size is not supported.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_SIGNING_KEY_NOT_ACCESSIBLE"></span><span id="dns_error_signing_key_not_accessible"></span>**DNS\_ERROR\_SIGNING\_KEY\_NOT\_ACCESSIBLE**
</dt> <dd> <dl> <dt>

9107 (0x2393)
</dt> <dt>



One or more of the signing keys for a zone are not accessible to the DNS server. Zone signing will not be operational until this error is resolved.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_KSP_DOES_NOT_SUPPORT_PROTECTION"></span><span id="dns_error_ksp_does_not_support_protection"></span>**DNS\_ERROR\_KSP\_DOES\_NOT\_SUPPORT\_PROTECTION**
</dt> <dd> <dl> <dt>

9108 (0x2394)
</dt> <dt>



The specified key storage provider does not support DPAPI++ data protection. Zone signing will not be operational until this error is resolved.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_UNEXPECTED_DATA_PROTECTION_ERROR"></span><span id="dns_error_unexpected_data_protection_error"></span>**DNS\_ERROR\_UNEXPECTED\_DATA\_PROTECTION\_ERROR**
</dt> <dd> <dl> <dt>

9109 (0x2395)
</dt> <dt>



An unexpected DPAPI++ error was encountered. Zone signing will not be operational until this error is resolved.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_UNEXPECTED_CNG_ERROR"></span><span id="dns_error_unexpected_cng_error"></span>**DNS\_ERROR\_UNEXPECTED\_CNG\_ERROR**
</dt> <dd> <dl> <dt>

9110 (0x2396)
</dt> <dt>



An unexpected crypto error was encountered. Zone signing may not be operational until this error is resolved.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_UNKNOWN_SIGNING_PARAMETER_VERSION"></span><span id="dns_error_unknown_signing_parameter_version"></span>**DNS\_ERROR\_UNKNOWN\_SIGNING\_PARAMETER\_VERSION**
</dt> <dd> <dl> <dt>

9111 (0x2397)
</dt> <dt>



The DNS server encountered a signing key with an unknown version. Zone signing will not be operational until this error is resolved.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_KSP_NOT_ACCESSIBLE"></span><span id="dns_error_ksp_not_accessible"></span>**DNS\_ERROR\_KSP\_NOT\_ACCESSIBLE**
</dt> <dd> <dl> <dt>

9112 (0x2398)
</dt> <dt>



The specified key service provider cannot be opened by the DNS server.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_TOO_MANY_SKDS"></span><span id="dns_error_too_many_skds"></span>**DNS\_ERROR\_TOO\_MANY\_SKDS**
</dt> <dd> <dl> <dt>

9113 (0x2399)
</dt> <dt>



The DNS server cannot accept any more signing keys with the specified algorithm and KSK flag value for this zone.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_INVALID_ROLLOVER_PERIOD"></span><span id="dns_error_invalid_rollover_period"></span>**DNS\_ERROR\_INVALID\_ROLLOVER\_PERIOD**
</dt> <dd> <dl> <dt>

9114 (0x239A)
</dt> <dt>



The specified rollover period is invalid.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_INVALID_INITIAL_ROLLOVER_OFFSET"></span><span id="dns_error_invalid_initial_rollover_offset"></span>**DNS\_ERROR\_INVALID\_INITIAL\_ROLLOVER\_OFFSET**
</dt> <dd> <dl> <dt>

9115 (0x239B)
</dt> <dt>



The specified initial rollover offset is invalid.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_ROLLOVER_IN_PROGRESS"></span><span id="dns_error_rollover_in_progress"></span>**DNS\_ERROR\_ROLLOVER\_IN\_PROGRESS**
</dt> <dd> <dl> <dt>

9116 (0x239C)
</dt> <dt>



The specified signing key is already in process of rolling over keys.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_STANDBY_KEY_NOT_PRESENT"></span><span id="dns_error_standby_key_not_present"></span>**DNS\_ERROR\_STANDBY\_KEY\_NOT\_PRESENT**
</dt> <dd> <dl> <dt>

9117 (0x239D)
</dt> <dt>



The specified signing key does not have a standby key to revoke.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_NOT_ALLOWED_ON_ZSK"></span><span id="dns_error_not_allowed_on_zsk"></span>**DNS\_ERROR\_NOT\_ALLOWED\_ON\_ZSK**
</dt> <dd> <dl> <dt>

9118 (0x239E)
</dt> <dt>



This operation is not allowed on a zone signing key (ZSK).


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_NOT_ALLOWED_ON_ACTIVE_SKD"></span><span id="dns_error_not_allowed_on_active_skd"></span>**DNS\_ERROR\_NOT\_ALLOWED\_ON\_ACTIVE\_SKD**
</dt> <dd> <dl> <dt>

9119 (0x239F)
</dt> <dt>



This operation is not allowed on an active signing key.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_ROLLOVER_ALREADY_QUEUED"></span><span id="dns_error_rollover_already_queued"></span>**DNS\_ERROR\_ROLLOVER\_ALREADY\_QUEUED**
</dt> <dd> <dl> <dt>

9120 (0x23A0)
</dt> <dt>



The specified signing key is already queued for rollover.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_NOT_ALLOWED_ON_UNSIGNED_ZONE"></span><span id="dns_error_not_allowed_on_unsigned_zone"></span>**DNS\_ERROR\_NOT\_ALLOWED\_ON\_UNSIGNED\_ZONE**
</dt> <dd> <dl> <dt>

9121 (0x23A1)
</dt> <dt>



This operation is not allowed on an unsigned zone.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_BAD_KEYMASTER"></span><span id="dns_error_bad_keymaster"></span>**DNS\_ERROR\_BAD\_KEYMASTER**
</dt> <dd> <dl> <dt>

9122 (0x23A2)
</dt> <dt>



This operation could not be completed because the DNS server listed as the current key master for this zone is down or misconfigured. Resolve the problem on the current key master for this zone or use another DNS server to seize the key master role.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_INVALID_SIGNATURE_VALIDITY_PERIOD"></span><span id="dns_error_invalid_signature_validity_period"></span>**DNS\_ERROR\_INVALID\_SIGNATURE\_VALIDITY\_PERIOD**
</dt> <dd> <dl> <dt>

9123 (0x23A3)
</dt> <dt>



The specified signature validity period is invalid.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_INVALID_NSEC3_ITERATION_COUNT"></span><span id="dns_error_invalid_nsec3_iteration_count"></span>**DNS\_ERROR\_INVALID\_NSEC3\_ITERATION\_COUNT**
</dt> <dd> <dl> <dt>

9124 (0x23A4)
</dt> <dt>



The specified NSEC3 iteration count is higher than allowed by the minimum key length used in the zone.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_DNSSEC_IS_DISABLED"></span><span id="dns_error_dnssec_is_disabled"></span>**DNS\_ERROR\_DNSSEC\_IS\_DISABLED**
</dt> <dd> <dl> <dt>

9125 (0x23A5)
</dt> <dt>



This operation could not be completed because the DNS server has been configured with DNSSEC features disabled. Enable DNSSEC on the DNS server.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_INVALID_XML"></span><span id="dns_error_invalid_xml"></span>**DNS\_ERROR\_INVALID\_XML**
</dt> <dd> <dl> <dt>

9126 (0x23A6)
</dt> <dt>



This operation could not be completed because the XML stream received is empty or syntactically invalid.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_NO_VALID_TRUST_ANCHORS"></span><span id="dns_error_no_valid_trust_anchors"></span>**DNS\_ERROR\_NO\_VALID\_TRUST\_ANCHORS**
</dt> <dd> <dl> <dt>

9127 (0x23A7)
</dt> <dt>



This operation completed, but no trust anchors were added because all of the trust anchors received were either invalid, unsupported, expired, or would not become valid in less than 30 days.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_ROLLOVER_NOT_POKEABLE"></span><span id="dns_error_rollover_not_pokeable"></span>**DNS\_ERROR\_ROLLOVER\_NOT\_POKEABLE**
</dt> <dd> <dl> <dt>

9128 (0x23A8)
</dt> <dt>



The specified signing key is not waiting for parental DS update.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_NSEC3_NAME_COLLISION"></span><span id="dns_error_nsec3_name_collision"></span>**DNS\_ERROR\_NSEC3\_NAME\_COLLISION**
</dt> <dd> <dl> <dt>

9129 (0x23A9)
</dt> <dt>



Hash collision detected during NSEC3 signing. Specify a different user-provided salt, or use a randomly generated salt, and attempt to sign the zone again.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_NSEC_INCOMPATIBLE_WITH_NSEC3_RSA_SHA1"></span><span id="dns_error_nsec_incompatible_with_nsec3_rsa_sha1"></span>**DNS\_ERROR\_NSEC\_INCOMPATIBLE\_WITH\_NSEC3\_RSA\_SHA1**
</dt> <dd> <dl> <dt>

9130 (0x23AA)
</dt> <dt>



NSEC is not compatible with the NSEC3-RSA-SHA-1 algorithm. Choose a different algorithm or use NSEC3.


</dt> </dl> </dd> <dt>

<span id="DNS_INFO_NO_RECORDS"></span><span id="dns_info_no_records"></span>**DNS\_INFO\_NO\_RECORDS**
</dt> <dd> <dl> <dt>

9501 (0x251D)
</dt> <dt>



No records found for given DNS query.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_BAD_PACKET"></span><span id="dns_error_bad_packet"></span>**DNS\_ERROR\_BAD\_PACKET**
</dt> <dd> <dl> <dt>

9502 (0x251E)
</dt> <dt>



Bad DNS packet.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_NO_PACKET"></span><span id="dns_error_no_packet"></span>**DNS\_ERROR\_NO\_PACKET**
</dt> <dd> <dl> <dt>

9503 (0x251F)
</dt> <dt>



No DNS packet.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_RCODE"></span><span id="dns_error_rcode"></span>**DNS\_ERROR\_RCODE**
</dt> <dd> <dl> <dt>

9504 (0x2520)
</dt> <dt>



DNS error, check rcode.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_UNSECURE_PACKET"></span><span id="dns_error_unsecure_packet"></span>**DNS\_ERROR\_UNSECURE\_PACKET**
</dt> <dd> <dl> <dt>

9505 (0x2521)
</dt> <dt>



Unsecured DNS packet.


</dt> </dl> </dd> <dt>

<span id="DNS_REQUEST_PENDING"></span><span id="dns_request_pending"></span>**DNS\_REQUEST\_PENDING**
</dt> <dd> <dl> <dt>

9506 (0x2522)
</dt> <dt>



DNS query request is pending.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_INVALID_TYPE"></span><span id="dns_error_invalid_type"></span>**DNS\_ERROR\_INVALID\_TYPE**
</dt> <dd> <dl> <dt>

9551 (0x254F)
</dt> <dt>



Invalid DNS type.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_INVALID_IP_ADDRESS"></span><span id="dns_error_invalid_ip_address"></span>**DNS\_ERROR\_INVALID\_IP\_ADDRESS**
</dt> <dd> <dl> <dt>

9552 (0x2550)
</dt> <dt>



Invalid IP address.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_INVALID_PROPERTY"></span><span id="dns_error_invalid_property"></span>**DNS\_ERROR\_INVALID\_PROPERTY**
</dt> <dd> <dl> <dt>

9553 (0x2551)
</dt> <dt>



Invalid property.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_TRY_AGAIN_LATER"></span><span id="dns_error_try_again_later"></span>**DNS\_ERROR\_TRY\_AGAIN\_LATER**
</dt> <dd> <dl> <dt>

9554 (0x2552)
</dt> <dt>



Try DNS operation again later.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_NOT_UNIQUE"></span><span id="dns_error_not_unique"></span>**DNS\_ERROR\_NOT\_UNIQUE**
</dt> <dd> <dl> <dt>

9555 (0x2553)
</dt> <dt>



Record for given name and type is not unique.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_NON_RFC_NAME"></span><span id="dns_error_non_rfc_name"></span>**DNS\_ERROR\_NON\_RFC\_NAME**
</dt> <dd> <dl> <dt>

9556 (0x2554)
</dt> <dt>



DNS name does not comply with RFC specifications.


</dt> </dl> </dd> <dt>

<span id="DNS_STATUS_FQDN"></span><span id="dns_status_fqdn"></span>**DNS\_STATUS\_FQDN**
</dt> <dd> <dl> <dt>

9557 (0x2555)
</dt> <dt>



DNS name is a fully-qualified DNS name.


</dt> </dl> </dd> <dt>

<span id="DNS_STATUS_DOTTED_NAME"></span><span id="dns_status_dotted_name"></span>**DNS\_STATUS\_DOTTED\_NAME**
</dt> <dd> <dl> <dt>

9558 (0x2556)
</dt> <dt>



DNS name is dotted (multi-label).


</dt> </dl> </dd> <dt>

<span id="DNS_STATUS_SINGLE_PART_NAME"></span><span id="dns_status_single_part_name"></span>**DNS\_STATUS\_SINGLE\_PART\_NAME**
</dt> <dd> <dl> <dt>

9559 (0x2557)
</dt> <dt>



DNS name is a single-part name.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_INVALID_NAME_CHAR"></span><span id="dns_error_invalid_name_char"></span>**DNS\_ERROR\_INVALID\_NAME\_CHAR**
</dt> <dd> <dl> <dt>

9560 (0x2558)
</dt> <dt>



DNS name contains an invalid character.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_NUMERIC_NAME"></span><span id="dns_error_numeric_name"></span>**DNS\_ERROR\_NUMERIC\_NAME**
</dt> <dd> <dl> <dt>

9561 (0x2559)
</dt> <dt>



DNS name is entirely numeric.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_NOT_ALLOWED_ON_ROOT_SERVER"></span><span id="dns_error_not_allowed_on_root_server"></span>**DNS\_ERROR\_NOT\_ALLOWED\_ON\_ROOT\_SERVER**
</dt> <dd> <dl> <dt>

9562 (0x255A)
</dt> <dt>



The operation requested is not permitted on a DNS root server.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_NOT_ALLOWED_UNDER_DELEGATION"></span><span id="dns_error_not_allowed_under_delegation"></span>**DNS\_ERROR\_NOT\_ALLOWED\_UNDER\_DELEGATION**
</dt> <dd> <dl> <dt>

9563 (0x255B)
</dt> <dt>



The record could not be created because this part of the DNS namespace has been delegated to another server.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_CANNOT_FIND_ROOT_HINTS"></span><span id="dns_error_cannot_find_root_hints"></span>**DNS\_ERROR\_CANNOT\_FIND\_ROOT\_HINTS**
</dt> <dd> <dl> <dt>

9564 (0x255C)
</dt> <dt>



The DNS server could not find a set of root hints.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_INCONSISTENT_ROOT_HINTS"></span><span id="dns_error_inconsistent_root_hints"></span>**DNS\_ERROR\_INCONSISTENT\_ROOT\_HINTS**
</dt> <dd> <dl> <dt>

9565 (0x255D)
</dt> <dt>



The DNS server found root hints but they were not consistent across all adapters.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_DWORD_VALUE_TOO_SMALL"></span><span id="dns_error_dword_value_too_small"></span>**DNS\_ERROR\_DWORD\_VALUE\_TOO\_SMALL**
</dt> <dd> <dl> <dt>

9566 (0x255E)
</dt> <dt>



The specified value is too small for this parameter.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_DWORD_VALUE_TOO_LARGE"></span><span id="dns_error_dword_value_too_large"></span>**DNS\_ERROR\_DWORD\_VALUE\_TOO\_LARGE**
</dt> <dd> <dl> <dt>

9567 (0x255F)
</dt> <dt>



The specified value is too large for this parameter.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_BACKGROUND_LOADING"></span><span id="dns_error_background_loading"></span>**DNS\_ERROR\_BACKGROUND\_LOADING**
</dt> <dd> <dl> <dt>

9568 (0x2560)
</dt> <dt>



This operation is not allowed while the DNS server is loading zones in the background. Please try again later.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_NOT_ALLOWED_ON_RODC"></span><span id="dns_error_not_allowed_on_rodc"></span>**DNS\_ERROR\_NOT\_ALLOWED\_ON\_RODC**
</dt> <dd> <dl> <dt>

9569 (0x2561)
</dt> <dt>



The operation requested is not permitted on against a DNS server running on a read-only DC.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_NOT_ALLOWED_UNDER_DNAME"></span><span id="dns_error_not_allowed_under_dname"></span>**DNS\_ERROR\_NOT\_ALLOWED\_UNDER\_DNAME**
</dt> <dd> <dl> <dt>

9570 (0x2562)
</dt> <dt>



No data is allowed to exist underneath a DNAME record.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_DELEGATION_REQUIRED"></span><span id="dns_error_delegation_required"></span>**DNS\_ERROR\_DELEGATION\_REQUIRED**
</dt> <dd> <dl> <dt>

9571 (0x2563)
</dt> <dt>



This operation requires credentials delegation.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_INVALID_POLICY_TABLE"></span><span id="dns_error_invalid_policy_table"></span>**DNS\_ERROR\_INVALID\_POLICY\_TABLE**
</dt> <dd> <dl> <dt>

9572 (0x2564)
</dt> <dt>



Name resolution policy table has been corrupted. DNS resolution will fail until it is fixed. Contact your network administrator.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_ZONE_DOES_NOT_EXIST"></span><span id="dns_error_zone_does_not_exist"></span>**DNS\_ERROR\_ZONE\_DOES\_NOT\_EXIST**
</dt> <dd> <dl> <dt>

9601 (0x2581)
</dt> <dt>



DNS zone does not exist.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_NO_ZONE_INFO"></span><span id="dns_error_no_zone_info"></span>**DNS\_ERROR\_NO\_ZONE\_INFO**
</dt> <dd> <dl> <dt>

9602 (0x2582)
</dt> <dt>



DNS zone information not available.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_INVALID_ZONE_OPERATION"></span><span id="dns_error_invalid_zone_operation"></span>**DNS\_ERROR\_INVALID\_ZONE\_OPERATION**
</dt> <dd> <dl> <dt>

9603 (0x2583)
</dt> <dt>



Invalid operation for DNS zone.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_ZONE_CONFIGURATION_ERROR"></span><span id="dns_error_zone_configuration_error"></span>**DNS\_ERROR\_ZONE\_CONFIGURATION\_ERROR**
</dt> <dd> <dl> <dt>

9604 (0x2584)
</dt> <dt>



Invalid DNS zone configuration.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_ZONE_HAS_NO_SOA_RECORD"></span><span id="dns_error_zone_has_no_soa_record"></span>**DNS\_ERROR\_ZONE\_HAS\_NO\_SOA\_RECORD**
</dt> <dd> <dl> <dt>

9605 (0x2585)
</dt> <dt>



DNS zone has no start of authority (SOA) record.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_ZONE_HAS_NO_NS_RECORDS"></span><span id="dns_error_zone_has_no_ns_records"></span>**DNS\_ERROR\_ZONE\_HAS\_NO\_NS\_RECORDS**
</dt> <dd> <dl> <dt>

9606 (0x2586)
</dt> <dt>



DNS zone has no Name Server (NS) record.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_ZONE_LOCKED"></span><span id="dns_error_zone_locked"></span>**DNS\_ERROR\_ZONE\_LOCKED**
</dt> <dd> <dl> <dt>

9607 (0x2587)
</dt> <dt>



DNS zone is locked.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_ZONE_CREATION_FAILED"></span><span id="dns_error_zone_creation_failed"></span>**DNS\_ERROR\_ZONE\_CREATION\_FAILED**
</dt> <dd> <dl> <dt>

9608 (0x2588)
</dt> <dt>



DNS zone creation failed.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_ZONE_ALREADY_EXISTS"></span><span id="dns_error_zone_already_exists"></span>**DNS\_ERROR\_ZONE\_ALREADY\_EXISTS**
</dt> <dd> <dl> <dt>

9609 (0x2589)
</dt> <dt>



DNS zone already exists.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_AUTOZONE_ALREADY_EXISTS"></span><span id="dns_error_autozone_already_exists"></span>**DNS\_ERROR\_AUTOZONE\_ALREADY\_EXISTS**
</dt> <dd> <dl> <dt>

9610 (0x258A)
</dt> <dt>



DNS automatic zone already exists.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_INVALID_ZONE_TYPE"></span><span id="dns_error_invalid_zone_type"></span>**DNS\_ERROR\_INVALID\_ZONE\_TYPE**
</dt> <dd> <dl> <dt>

9611 (0x258B)
</dt> <dt>



Invalid DNS zone type.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_SECONDARY_REQUIRES_MASTER_IP"></span><span id="dns_error_secondary_requires_master_ip"></span>**DNS\_ERROR\_SECONDARY\_REQUIRES\_MASTER\_IP**
</dt> <dd> <dl> <dt>

9612 (0x258C)
</dt> <dt>



Secondary DNS zone requires master IP address.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_ZONE_NOT_SECONDARY"></span><span id="dns_error_zone_not_secondary"></span>**DNS\_ERROR\_ZONE\_NOT\_SECONDARY**
</dt> <dd> <dl> <dt>

9613 (0x258D)
</dt> <dt>



DNS zone not secondary.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_NEED_SECONDARY_ADDRESSES"></span><span id="dns_error_need_secondary_addresses"></span>**DNS\_ERROR\_NEED\_SECONDARY\_ADDRESSES**
</dt> <dd> <dl> <dt>

9614 (0x258E)
</dt> <dt>



Need secondary IP address.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_WINS_INIT_FAILED"></span><span id="dns_error_wins_init_failed"></span>**DNS\_ERROR\_WINS\_INIT\_FAILED**
</dt> <dd> <dl> <dt>

9615 (0x258F)
</dt> <dt>



WINS initialization failed.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_NEED_WINS_SERVERS"></span><span id="dns_error_need_wins_servers"></span>**DNS\_ERROR\_NEED\_WINS\_SERVERS**
</dt> <dd> <dl> <dt>

9616 (0x2590)
</dt> <dt>



Need WINS servers.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_NBSTAT_INIT_FAILED"></span><span id="dns_error_nbstat_init_failed"></span>**DNS\_ERROR\_NBSTAT\_INIT\_FAILED**
</dt> <dd> <dl> <dt>

9617 (0x2591)
</dt> <dt>



NBTSTAT initialization call failed.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_SOA_DELETE_INVALID"></span><span id="dns_error_soa_delete_invalid"></span>**DNS\_ERROR\_SOA\_DELETE\_INVALID**
</dt> <dd> <dl> <dt>

9618 (0x2592)
</dt> <dt>



Invalid delete of start of authority (SOA).


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_FORWARDER_ALREADY_EXISTS"></span><span id="dns_error_forwarder_already_exists"></span>**DNS\_ERROR\_FORWARDER\_ALREADY\_EXISTS**
</dt> <dd> <dl> <dt>

9619 (0x2593)
</dt> <dt>



A conditional forwarding zone already exists for that name.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_ZONE_REQUIRES_MASTER_IP"></span><span id="dns_error_zone_requires_master_ip"></span>**DNS\_ERROR\_ZONE\_REQUIRES\_MASTER\_IP**
</dt> <dd> <dl> <dt>

9620 (0x2594)
</dt> <dt>



This zone must be configured with one or more master DNS server IP addresses.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_ZONE_IS_SHUTDOWN"></span><span id="dns_error_zone_is_shutdown"></span>**DNS\_ERROR\_ZONE\_IS\_SHUTDOWN**
</dt> <dd> <dl> <dt>

9621 (0x2595)
</dt> <dt>



The operation cannot be performed because this zone is shut down.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_ZONE_LOCKED_FOR_SIGNING"></span><span id="dns_error_zone_locked_for_signing"></span>**DNS\_ERROR\_ZONE\_LOCKED\_FOR\_SIGNING**
</dt> <dd> <dl> <dt>

9622 (0x2596)
</dt> <dt>



This operation cannot be performed because the zone is currently being signed. Please try again later.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_PRIMARY_REQUIRES_DATAFILE"></span><span id="dns_error_primary_requires_datafile"></span>**DNS\_ERROR\_PRIMARY\_REQUIRES\_DATAFILE**
</dt> <dd> <dl> <dt>

9651 (0x25B3)
</dt> <dt>



Primary DNS zone requires datafile.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_INVALID_DATAFILE_NAME"></span><span id="dns_error_invalid_datafile_name"></span>**DNS\_ERROR\_INVALID\_DATAFILE\_NAME**
</dt> <dd> <dl> <dt>

9652 (0x25B4)
</dt> <dt>



Invalid datafile name for DNS zone.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_DATAFILE_OPEN_FAILURE"></span><span id="dns_error_datafile_open_failure"></span>**DNS\_ERROR\_DATAFILE\_OPEN\_FAILURE**
</dt> <dd> <dl> <dt>

9653 (0x25B5)
</dt> <dt>



Failed to open datafile for DNS zone.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_FILE_WRITEBACK_FAILED"></span><span id="dns_error_file_writeback_failed"></span>**DNS\_ERROR\_FILE\_WRITEBACK\_FAILED**
</dt> <dd> <dl> <dt>

9654 (0x25B6)
</dt> <dt>



Failed to write datafile for DNS zone.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_DATAFILE_PARSING"></span><span id="dns_error_datafile_parsing"></span>**DNS\_ERROR\_DATAFILE\_PARSING**
</dt> <dd> <dl> <dt>

9655 (0x25B7)
</dt> <dt>



Failure while reading datafile for DNS zone.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_RECORD_DOES_NOT_EXIST"></span><span id="dns_error_record_does_not_exist"></span>**DNS\_ERROR\_RECORD\_DOES\_NOT\_EXIST**
</dt> <dd> <dl> <dt>

9701 (0x25E5)
</dt> <dt>



DNS record does not exist.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_RECORD_FORMAT"></span><span id="dns_error_record_format"></span>**DNS\_ERROR\_RECORD\_FORMAT**
</dt> <dd> <dl> <dt>

9702 (0x25E6)
</dt> <dt>



DNS record format error.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_NODE_CREATION_FAILED"></span><span id="dns_error_node_creation_failed"></span>**DNS\_ERROR\_NODE\_CREATION\_FAILED**
</dt> <dd> <dl> <dt>

9703 (0x25E7)
</dt> <dt>



Node creation failure in DNS.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_UNKNOWN_RECORD_TYPE"></span><span id="dns_error_unknown_record_type"></span>**DNS\_ERROR\_UNKNOWN\_RECORD\_TYPE**
</dt> <dd> <dl> <dt>

9704 (0x25E8)
</dt> <dt>



Unknown DNS record type.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_RECORD_TIMED_OUT"></span><span id="dns_error_record_timed_out"></span>**DNS\_ERROR\_RECORD\_TIMED\_OUT**
</dt> <dd> <dl> <dt>

9705 (0x25E9)
</dt> <dt>



DNS record timed out.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_NAME_NOT_IN_ZONE"></span><span id="dns_error_name_not_in_zone"></span>**DNS\_ERROR\_NAME\_NOT\_IN\_ZONE**
</dt> <dd> <dl> <dt>

9706 (0x25EA)
</dt> <dt>



Name not in DNS zone.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_CNAME_LOOP"></span><span id="dns_error_cname_loop"></span>**DNS\_ERROR\_CNAME\_LOOP**
</dt> <dd> <dl> <dt>

9707 (0x25EB)
</dt> <dt>



CNAME loop detected.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_NODE_IS_CNAME"></span><span id="dns_error_node_is_cname"></span>**DNS\_ERROR\_NODE\_IS\_CNAME**
</dt> <dd> <dl> <dt>

9708 (0x25EC)
</dt> <dt>



Node is a CNAME DNS record.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_CNAME_COLLISION"></span><span id="dns_error_cname_collision"></span>**DNS\_ERROR\_CNAME\_COLLISION**
</dt> <dd> <dl> <dt>

9709 (0x25ED)
</dt> <dt>



A CNAME record already exists for given name.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_RECORD_ONLY_AT_ZONE_ROOT"></span><span id="dns_error_record_only_at_zone_root"></span>**DNS\_ERROR\_RECORD\_ONLY\_AT\_ZONE\_ROOT**
</dt> <dd> <dl> <dt>

9710 (0x25EE)
</dt> <dt>



Record only at DNS zone root.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_RECORD_ALREADY_EXISTS"></span><span id="dns_error_record_already_exists"></span>**DNS\_ERROR\_RECORD\_ALREADY\_EXISTS**
</dt> <dd> <dl> <dt>

9711 (0x25EF)
</dt> <dt>



DNS record already exists.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_SECONDARY_DATA"></span><span id="dns_error_secondary_data"></span>**DNS\_ERROR\_SECONDARY\_DATA**
</dt> <dd> <dl> <dt>

9712 (0x25F0)
</dt> <dt>



Secondary DNS zone data error.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_NO_CREATE_CACHE_DATA"></span><span id="dns_error_no_create_cache_data"></span>**DNS\_ERROR\_NO\_CREATE\_CACHE\_DATA**
</dt> <dd> <dl> <dt>

9713 (0x25F1)
</dt> <dt>



Could not create DNS cache data.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_NAME_DOES_NOT_EXIST"></span><span id="dns_error_name_does_not_exist"></span>**DNS\_ERROR\_NAME\_DOES\_NOT\_EXIST**
</dt> <dd> <dl> <dt>

9714 (0x25F2)
</dt> <dt>



DNS name does not exist.


</dt> </dl> </dd> <dt>

<span id="DNS_WARNING_PTR_CREATE_FAILED"></span><span id="dns_warning_ptr_create_failed"></span>**DNS\_WARNING\_PTR\_CREATE\_FAILED**
</dt> <dd> <dl> <dt>

9715 (0x25F3)
</dt> <dt>



Could not create pointer (PTR) record.


</dt> </dl> </dd> <dt>

<span id="DNS_WARNING_DOMAIN_UNDELETED"></span><span id="dns_warning_domain_undeleted"></span>**DNS\_WARNING\_DOMAIN\_UNDELETED**
</dt> <dd> <dl> <dt>

9716 (0x25F4)
</dt> <dt>



DNS domain was undeleted.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_DS_UNAVAILABLE"></span><span id="dns_error_ds_unavailable"></span>**DNS\_ERROR\_DS\_UNAVAILABLE**
</dt> <dd> <dl> <dt>

9717 (0x25F5)
</dt> <dt>



The directory service is unavailable.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_DS_ZONE_ALREADY_EXISTS"></span><span id="dns_error_ds_zone_already_exists"></span>**DNS\_ERROR\_DS\_ZONE\_ALREADY\_EXISTS**
</dt> <dd> <dl> <dt>

9718 (0x25F6)
</dt> <dt>



DNS zone already exists in the directory service.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_NO_BOOTFILE_IF_DS_ZONE"></span><span id="dns_error_no_bootfile_if_ds_zone"></span>**DNS\_ERROR\_NO\_BOOTFILE\_IF\_DS\_ZONE**
</dt> <dd> <dl> <dt>

9719 (0x25F7)
</dt> <dt>



DNS server not creating or reading the boot file for the directory service integrated DNS zone.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_NODE_IS_DNAME"></span><span id="dns_error_node_is_dname"></span>**DNS\_ERROR\_NODE\_IS\_DNAME**
</dt> <dd> <dl> <dt>

9720 (0x25F8)
</dt> <dt>



Node is a DNAME DNS record.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_DNAME_COLLISION"></span><span id="dns_error_dname_collision"></span>**DNS\_ERROR\_DNAME\_COLLISION**
</dt> <dd> <dl> <dt>

9721 (0x25F9)
</dt> <dt>



A DNAME record already exists for given name.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_ALIAS_LOOP"></span><span id="dns_error_alias_loop"></span>**DNS\_ERROR\_ALIAS\_LOOP**
</dt> <dd> <dl> <dt>

9722 (0x25FA)
</dt> <dt>



An alias loop has been detected with either CNAME or DNAME records.


</dt> </dl> </dd> <dt>

<span id="DNS_INFO_AXFR_COMPLETE"></span><span id="dns_info_axfr_complete"></span>**DNS\_INFO\_AXFR\_COMPLETE**
</dt> <dd> <dl> <dt>

9751 (0x2617)
</dt> <dt>



DNS AXFR (zone transfer) complete.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_AXFR"></span><span id="dns_error_axfr"></span>**DNS\_ERROR\_AXFR**
</dt> <dd> <dl> <dt>

9752 (0x2618)
</dt> <dt>



DNS zone transfer failed.


</dt> </dl> </dd> <dt>

<span id="DNS_INFO_ADDED_LOCAL_WINS"></span><span id="dns_info_added_local_wins"></span>**DNS\_INFO\_ADDED\_LOCAL\_WINS**
</dt> <dd> <dl> <dt>

9753 (0x2619)
</dt> <dt>



Added local WINS server.


</dt> </dl> </dd> <dt>

<span id="DNS_STATUS_CONTINUE_NEEDED"></span><span id="dns_status_continue_needed"></span>**DNS\_STATUS\_CONTINUE\_NEEDED**
</dt> <dd> <dl> <dt>

9801 (0x2649)
</dt> <dt>



Secure update call needs to continue update request.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_NO_TCPIP"></span><span id="dns_error_no_tcpip"></span>**DNS\_ERROR\_NO\_TCPIP**
</dt> <dd> <dl> <dt>

9851 (0x267B)
</dt> <dt>



TCP/IP network protocol not installed.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_NO_DNS_SERVERS"></span><span id="dns_error_no_dns_servers"></span>**DNS\_ERROR\_NO\_DNS\_SERVERS**
</dt> <dd> <dl> <dt>

9852 (0x267C)
</dt> <dt>



No DNS servers configured for local system.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_DP_DOES_NOT_EXIST"></span><span id="dns_error_dp_does_not_exist"></span>**DNS\_ERROR\_DP\_DOES\_NOT\_EXIST**
</dt> <dd> <dl> <dt>

9901 (0x26AD)
</dt> <dt>



The specified directory partition does not exist.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_DP_ALREADY_EXISTS"></span><span id="dns_error_dp_already_exists"></span>**DNS\_ERROR\_DP\_ALREADY\_EXISTS**
</dt> <dd> <dl> <dt>

9902 (0x26AE)
</dt> <dt>



The specified directory partition already exists.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_DP_NOT_ENLISTED"></span><span id="dns_error_dp_not_enlisted"></span>**DNS\_ERROR\_DP\_NOT\_ENLISTED**
</dt> <dd> <dl> <dt>

9903 (0x26AF)
</dt> <dt>



This DNS server is not enlisted in the specified directory partition.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_DP_ALREADY_ENLISTED"></span><span id="dns_error_dp_already_enlisted"></span>**DNS\_ERROR\_DP\_ALREADY\_ENLISTED**
</dt> <dd> <dl> <dt>

9904 (0x26B0)
</dt> <dt>



This DNS server is already enlisted in the specified directory partition.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_DP_NOT_AVAILABLE"></span><span id="dns_error_dp_not_available"></span>**DNS\_ERROR\_DP\_NOT\_AVAILABLE**
</dt> <dd> <dl> <dt>

9905 (0x26B1)
</dt> <dt>



The directory partition is not available at this time. Please wait a few minutes and try again.


</dt> </dl> </dd> <dt>

<span id="DNS_ERROR_DP_FSMO_ERROR"></span><span id="dns_error_dp_fsmo_error"></span>**DNS\_ERROR\_DP\_FSMO\_ERROR**
</dt> <dd> <dl> <dt>

9906 (0x26B2)
</dt> <dt>



The operation failed because the domain naming master FSMO role could not be reached. The domain controller holding the domain naming master FSMO role is down or unable to service the request or is not running Windows Server 2003 or later.


</dt> </dl> </dd> <dt>

<span id="WSAEINTR"></span><span id="wsaeintr"></span>**WSAEINTR**
</dt> <dd> <dl> <dt>

10004 (0x2714)
</dt> <dt>



A blocking operation was interrupted by a call to WSACancelBlockingCall.


</dt> </dl> </dd> <dt>

<span id="WSAEBADF"></span><span id="wsaebadf"></span>**WSAEBADF**
</dt> <dd> <dl> <dt>

10009 (0x2719)
</dt> <dt>



The file handle supplied is not valid.


</dt> </dl> </dd> <dt>

<span id="WSAEACCES"></span><span id="wsaeacces"></span>**WSAEACCES**
</dt> <dd> <dl> <dt>

10013 (0x271D)
</dt> <dt>



An attempt was made to access a socket in a way forbidden by its access permissions.


</dt> </dl> </dd> <dt>

<span id="WSAEFAULT"></span><span id="wsaefault"></span>**WSAEFAULT**
</dt> <dd> <dl> <dt>

10014 (0x271E)
</dt> <dt>



The system detected an invalid pointer address in attempting to use a pointer argument in a call.


</dt> </dl> </dd> <dt>

<span id="WSAEINVAL"></span><span id="wsaeinval"></span>**WSAEINVAL**
</dt> <dd> <dl> <dt>

10022 (0x2726)
</dt> <dt>



An invalid argument was supplied.


</dt> </dl> </dd> <dt>

<span id="WSAEMFILE"></span><span id="wsaemfile"></span>**WSAEMFILE**
</dt> <dd> <dl> <dt>

10024 (0x2728)
</dt> <dt>



Too many open sockets.


</dt> </dl> </dd> <dt>

<span id="WSAEWOULDBLOCK"></span><span id="wsaewouldblock"></span>**WSAEWOULDBLOCK**
</dt> <dd> <dl> <dt>

10035 (0x2733)
</dt> <dt>



A non-blocking socket operation could not be completed immediately.


</dt> </dl> </dd> <dt>

<span id="WSAEINPROGRESS"></span><span id="wsaeinprogress"></span>**WSAEINPROGRESS**
</dt> <dd> <dl> <dt>

10036 (0x2734)
</dt> <dt>



A blocking operation is currently executing.


</dt> </dl> </dd> <dt>

<span id="WSAEALREADY"></span><span id="wsaealready"></span>**WSAEALREADY**
</dt> <dd> <dl> <dt>

10037 (0x2735)
</dt> <dt>



An operation was attempted on a non-blocking socket that already had an operation in progress.


</dt> </dl> </dd> <dt>

<span id="WSAENOTSOCK"></span><span id="wsaenotsock"></span>**WSAENOTSOCK**
</dt> <dd> <dl> <dt>

10038 (0x2736)
</dt> <dt>



An operation was attempted on something that is not a socket.


</dt> </dl> </dd> <dt>

<span id="WSAEDESTADDRREQ"></span><span id="wsaedestaddrreq"></span>**WSAEDESTADDRREQ**
</dt> <dd> <dl> <dt>

10039 (0x2737)
</dt> <dt>



A required address was omitted from an operation on a socket.


</dt> </dl> </dd> <dt>

<span id="WSAEMSGSIZE"></span><span id="wsaemsgsize"></span>**WSAEMSGSIZE**
</dt> <dd> <dl> <dt>

10040 (0x2738)
</dt> <dt>



A message sent on a datagram socket was larger than the internal message buffer or some other network limit, or the buffer used to receive a datagram into was smaller than the datagram itself.


</dt> </dl> </dd> <dt>

<span id="WSAEPROTOTYPE"></span><span id="wsaeprototype"></span>**WSAEPROTOTYPE**
</dt> <dd> <dl> <dt>

10041 (0x2739)
</dt> <dt>



A protocol was specified in the socket function call that does not support the semantics of the socket type requested.


</dt> </dl> </dd> <dt>

<span id="WSAENOPROTOOPT"></span><span id="wsaenoprotoopt"></span>**WSAENOPROTOOPT**
</dt> <dd> <dl> <dt>

10042 (0x273A)
</dt> <dt>



An unknown, invalid, or unsupported option or level was specified in a getsockopt or setsockopt call.


</dt> </dl> </dd> <dt>

<span id="WSAEPROTONOSUPPORT"></span><span id="wsaeprotonosupport"></span>**WSAEPROTONOSUPPORT**
</dt> <dd> <dl> <dt>

10043 (0x273B)
</dt> <dt>



The requested protocol has not been configured into the system, or no implementation for it exists.


</dt> </dl> </dd> <dt>

<span id="WSAESOCKTNOSUPPORT"></span><span id="wsaesocktnosupport"></span>**WSAESOCKTNOSUPPORT**
</dt> <dd> <dl> <dt>

10044 (0x273C)
</dt> <dt>



The support for the specified socket type does not exist in this address family.


</dt> </dl> </dd> <dt>

<span id="WSAEOPNOTSUPP"></span><span id="wsaeopnotsupp"></span>**WSAEOPNOTSUPP**
</dt> <dd> <dl> <dt>

10045 (0x273D)
</dt> <dt>



The attempted operation is not supported for the type of object referenced.


</dt> </dl> </dd> <dt>

<span id="WSAEPFNOSUPPORT"></span><span id="wsaepfnosupport"></span>**WSAEPFNOSUPPORT**
</dt> <dd> <dl> <dt>

10046 (0x273E)
</dt> <dt>



The protocol family has not been configured into the system or no implementation for it exists.


</dt> </dl> </dd> <dt>

<span id="WSAEAFNOSUPPORT"></span><span id="wsaeafnosupport"></span>**WSAEAFNOSUPPORT**
</dt> <dd> <dl> <dt>

10047 (0x273F)
</dt> <dt>



An address incompatible with the requested protocol was used.


</dt> </dl> </dd> <dt>

<span id="WSAEADDRINUSE"></span><span id="wsaeaddrinuse"></span>**WSAEADDRINUSE**
</dt> <dd> <dl> <dt>

10048 (0x2740)
</dt> <dt>



Only one usage of each socket address (protocol/network address/port) is normally permitted.


</dt> </dl> </dd> <dt>

<span id="WSAEADDRNOTAVAIL"></span><span id="wsaeaddrnotavail"></span>**WSAEADDRNOTAVAIL**
</dt> <dd> <dl> <dt>

10049 (0x2741)
</dt> <dt>



The requested address is not valid in its context.


</dt> </dl> </dd> <dt>

<span id="WSAENETDOWN"></span><span id="wsaenetdown"></span>**WSAENETDOWN**
</dt> <dd> <dl> <dt>

10050 (0x2742)
</dt> <dt>



A socket operation encountered a dead network.


</dt> </dl> </dd> <dt>

<span id="WSAENETUNREACH"></span><span id="wsaenetunreach"></span>**WSAENETUNREACH**
</dt> <dd> <dl> <dt>

10051 (0x2743)
</dt> <dt>



A socket operation was attempted to an unreachable network.


</dt> </dl> </dd> <dt>

<span id="WSAENETRESET"></span><span id="wsaenetreset"></span>**WSAENETRESET**
</dt> <dd> <dl> <dt>

10052 (0x2744)
</dt> <dt>



The connection has been broken due to keep-alive activity detecting a failure while the operation was in progress.


</dt> </dl> </dd> <dt>

<span id="WSAECONNABORTED"></span><span id="wsaeconnaborted"></span>**WSAECONNABORTED**
</dt> <dd> <dl> <dt>

10053 (0x2745)
</dt> <dt>



An established connection was aborted by the software in your host machine.


</dt> </dl> </dd> <dt>

<span id="WSAECONNRESET"></span><span id="wsaeconnreset"></span>**WSAECONNRESET**
</dt> <dd> <dl> <dt>

10054 (0x2746)
</dt> <dt>



An existing connection was forcibly closed by the remote host.


</dt> </dl> </dd> <dt>

<span id="WSAENOBUFS"></span><span id="wsaenobufs"></span>**WSAENOBUFS**
</dt> <dd> <dl> <dt>

10055 (0x2747)
</dt> <dt>



An operation on a socket could not be performed because the system lacked sufficient buffer space or because a queue was full.


</dt> </dl> </dd> <dt>

<span id="WSAEISCONN"></span><span id="wsaeisconn"></span>**WSAEISCONN**
</dt> <dd> <dl> <dt>

10056 (0x2748)
</dt> <dt>



A connect request was made on an already connected socket.


</dt> </dl> </dd> <dt>

<span id="WSAENOTCONN"></span><span id="wsaenotconn"></span>**WSAENOTCONN**
</dt> <dd> <dl> <dt>

10057 (0x2749)
</dt> <dt>



A request to send or receive data was disallowed because the socket is not connected and (when sending on a datagram socket using a sendto call) no address was supplied.


</dt> </dl> </dd> <dt>

<span id="WSAESHUTDOWN"></span><span id="wsaeshutdown"></span>**WSAESHUTDOWN**
</dt> <dd> <dl> <dt>

10058 (0x274A)
</dt> <dt>



A request to send or receive data was disallowed because the socket had already been shut down in that direction with a previous shutdown call.


</dt> </dl> </dd> <dt>

<span id="WSAETOOMANYREFS"></span><span id="wsaetoomanyrefs"></span>**WSAETOOMANYREFS**
</dt> <dd> <dl> <dt>

10059 (0x274B)
</dt> <dt>



Too many references to some kernel object.


</dt> </dl> </dd> <dt>

<span id="WSAETIMEDOUT"></span><span id="wsaetimedout"></span>**WSAETIMEDOUT**
</dt> <dd> <dl> <dt>

10060 (0x274C)
</dt> <dt>



A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond.


</dt> </dl> </dd> <dt>

<span id="WSAECONNREFUSED"></span><span id="wsaeconnrefused"></span>**WSAECONNREFUSED**
</dt> <dd> <dl> <dt>

10061 (0x274D)
</dt> <dt>



No connection could be made because the target machine actively refused it.


</dt> </dl> </dd> <dt>

<span id="WSAELOOP"></span><span id="wsaeloop"></span>**WSAELOOP**
</dt> <dd> <dl> <dt>

10062 (0x274E)
</dt> <dt>



Cannot translate name.


</dt> </dl> </dd> <dt>

<span id="WSAENAMETOOLONG"></span><span id="wsaenametoolong"></span>**WSAENAMETOOLONG**
</dt> <dd> <dl> <dt>

10063 (0x274F)
</dt> <dt>



Name component or name was too long.


</dt> </dl> </dd> <dt>

<span id="WSAEHOSTDOWN"></span><span id="wsaehostdown"></span>**WSAEHOSTDOWN**
</dt> <dd> <dl> <dt>

10064 (0x2750)
</dt> <dt>



A socket operation failed because the destination host was down.


</dt> </dl> </dd> <dt>

<span id="WSAEHOSTUNREACH"></span><span id="wsaehostunreach"></span>**WSAEHOSTUNREACH**
</dt> <dd> <dl> <dt>

10065 (0x2751)
</dt> <dt>



A socket operation was attempted to an unreachable host.


</dt> </dl> </dd> <dt>

<span id="WSAENOTEMPTY"></span><span id="wsaenotempty"></span>**WSAENOTEMPTY**
</dt> <dd> <dl> <dt>

10066 (0x2752)
</dt> <dt>



Cannot remove a directory that is not empty.


</dt> </dl> </dd> <dt>

<span id="WSAEPROCLIM"></span><span id="wsaeproclim"></span>**WSAEPROCLIM**
</dt> <dd> <dl> <dt>

10067 (0x2753)
</dt> <dt>



A Windows Sockets implementation may have a limit on the number of applications that may use it simultaneously.


</dt> </dl> </dd> <dt>

<span id="WSAEUSERS"></span><span id="wsaeusers"></span>**WSAEUSERS**
</dt> <dd> <dl> <dt>

10068 (0x2754)
</dt> <dt>



Ran out of quota.


</dt> </dl> </dd> <dt>

<span id="WSAEDQUOT"></span><span id="wsaedquot"></span>**WSAEDQUOT**
</dt> <dd> <dl> <dt>

10069 (0x2755)
</dt> <dt>



Ran out of disk quota.


</dt> </dl> </dd> <dt>

<span id="WSAESTALE"></span><span id="wsaestale"></span>**WSAESTALE**
</dt> <dd> <dl> <dt>

10070 (0x2756)
</dt> <dt>



File handle reference is no longer available.


</dt> </dl> </dd> <dt>

<span id="WSAEREMOTE"></span><span id="wsaeremote"></span>**WSAEREMOTE**
</dt> <dd> <dl> <dt>

10071 (0x2757)
</dt> <dt>



Item is not available locally.


</dt> </dl> </dd> <dt>

<span id="WSASYSNOTREADY"></span><span id="wsasysnotready"></span>**WSASYSNOTREADY**
</dt> <dd> <dl> <dt>

10091 (0x276B)
</dt> <dt>



WSAStartup cannot function at this time because the underlying system it uses to provide network services is currently unavailable.


</dt> </dl> </dd> <dt>

<span id="WSAVERNOTSUPPORTED"></span><span id="wsavernotsupported"></span>**WSAVERNOTSUPPORTED**
</dt> <dd> <dl> <dt>

10092 (0x276C)
</dt> <dt>



The Windows Sockets version requested is not supported.


</dt> </dl> </dd> <dt>

<span id="WSANOTINITIALISED"></span><span id="wsanotinitialised"></span>**WSANOTINITIALISED**
</dt> <dd> <dl> <dt>

10093 (0x276D)
</dt> <dt>



Either the application has not called WSAStartup, or WSAStartup failed.


</dt> </dl> </dd> <dt>

<span id="WSAEDISCON"></span><span id="wsaediscon"></span>**WSAEDISCON**
</dt> <dd> <dl> <dt>

10101 (0x2775)
</dt> <dt>



Returned by WSARecv or WSARecvFrom to indicate the remote party has initiated a graceful shutdown sequence.


</dt> </dl> </dd> <dt>

<span id="WSAENOMORE"></span><span id="wsaenomore"></span>**WSAENOMORE**
</dt> <dd> <dl> <dt>

10102 (0x2776)
</dt> <dt>



No more results can be returned by WSALookupServiceNext.


</dt> </dl> </dd> <dt>

<span id="WSAECANCELLED"></span><span id="wsaecancelled"></span>**WSAECANCELLED**
</dt> <dd> <dl> <dt>

10103 (0x2777)
</dt> <dt>



A call to WSALookupServiceEnd was made while this call was still processing. The call has been canceled.


</dt> </dl> </dd> <dt>

<span id="WSAEINVALIDPROCTABLE"></span><span id="wsaeinvalidproctable"></span>**WSAEINVALIDPROCTABLE**
</dt> <dd> <dl> <dt>

10104 (0x2778)
</dt> <dt>



The procedure call table is invalid.


</dt> </dl> </dd> <dt>

<span id="WSAEINVALIDPROVIDER"></span><span id="wsaeinvalidprovider"></span>**WSAEINVALIDPROVIDER**
</dt> <dd> <dl> <dt>

10105 (0x2779)
</dt> <dt>



The requested service provider is invalid.


</dt> </dl> </dd> <dt>

<span id="WSAEPROVIDERFAILEDINIT"></span><span id="wsaeproviderfailedinit"></span>**WSAEPROVIDERFAILEDINIT**
</dt> <dd> <dl> <dt>

10106 (0x277A)
</dt> <dt>



The requested service provider could not be loaded or initialized.


</dt> </dl> </dd> <dt>

<span id="WSASYSCALLFAILURE"></span><span id="wsasyscallfailure"></span>**WSASYSCALLFAILURE**
</dt> <dd> <dl> <dt>

10107 (0x277B)
</dt> <dt>



A system call has failed.


</dt> </dl> </dd> <dt>

<span id="WSASERVICE_NOT_FOUND"></span><span id="wsaservice_not_found"></span>**WSASERVICE\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

10108 (0x277C)
</dt> <dt>



No such service is known. The service cannot be found in the specified name space.


</dt> </dl> </dd> <dt>

<span id="WSATYPE_NOT_FOUND"></span><span id="wsatype_not_found"></span>**WSATYPE\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

10109 (0x277D)
</dt> <dt>



The specified class was not found.


</dt> </dl> </dd> <dt>

<span id="WSA_E_NO_MORE"></span><span id="wsa_e_no_more"></span>**WSA\_E\_NO\_MORE**
</dt> <dd> <dl> <dt>

10110 (0x277E)
</dt> <dt>



No more results can be returned by WSALookupServiceNext.


</dt> </dl> </dd> <dt>

<span id="WSA_E_CANCELLED"></span><span id="wsa_e_cancelled"></span>**WSA\_E\_CANCELLED**
</dt> <dd> <dl> <dt>

10111 (0x277F)
</dt> <dt>



A call to WSALookupServiceEnd was made while this call was still processing. The call has been canceled.


</dt> </dl> </dd> <dt>

<span id="WSAEREFUSED"></span><span id="wsaerefused"></span>**WSAEREFUSED**
</dt> <dd> <dl> <dt>

10112 (0x2780)
</dt> <dt>



A database query failed because it was actively refused.


</dt> </dl> </dd> <dt>

<span id="WSAHOST_NOT_FOUND"></span><span id="wsahost_not_found"></span>**WSAHOST\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

11001 (0x2AF9)
</dt> <dt>



No such host is known.


</dt> </dl> </dd> <dt>

<span id="WSATRY_AGAIN"></span><span id="wsatry_again"></span>**WSATRY\_AGAIN**
</dt> <dd> <dl> <dt>

11002 (0x2AFA)
</dt> <dt>



This is usually a temporary error during hostname resolution and means that the local server did not receive a response from an authoritative server.


</dt> </dl> </dd> <dt>

<span id="WSANO_RECOVERY"></span><span id="wsano_recovery"></span>**WSANO\_RECOVERY**
</dt> <dd> <dl> <dt>

11003 (0x2AFB)
</dt> <dt>



A non-recoverable error occurred during a database lookup.


</dt> </dl> </dd> <dt>

<span id="WSANO_DATA"></span><span id="wsano_data"></span>**WSANO\_DATA**
</dt> <dd> <dl> <dt>

11004 (0x2AFC)
</dt> <dt>



The requested name is valid, but no data of the requested type was found.


</dt> </dl> </dd> <dt>

<span id="WSA_QOS_RECEIVERS"></span><span id="wsa_qos_receivers"></span>**WSA\_QOS\_RECEIVERS**
</dt> <dd> <dl> <dt>

11005 (0x2AFD)
</dt> <dt>



At least one reserve has arrived.


</dt> </dl> </dd> <dt>

<span id="WSA_QOS_SENDERS"></span><span id="wsa_qos_senders"></span>**WSA\_QOS\_SENDERS**
</dt> <dd> <dl> <dt>

11006 (0x2AFE)
</dt> <dt>



At least one path has arrived.


</dt> </dl> </dd> <dt>

<span id="WSA_QOS_NO_SENDERS"></span><span id="wsa_qos_no_senders"></span>**WSA\_QOS\_NO\_SENDERS**
</dt> <dd> <dl> <dt>

11007 (0x2AFF)
</dt> <dt>



There are no senders.


</dt> </dl> </dd> <dt>

<span id="WSA_QOS_NO_RECEIVERS"></span><span id="wsa_qos_no_receivers"></span>**WSA\_QOS\_NO\_RECEIVERS**
</dt> <dd> <dl> <dt>

11008 (0x2B00)
</dt> <dt>



There are no receivers.


</dt> </dl> </dd> <dt>

<span id="WSA_QOS_REQUEST_CONFIRMED"></span><span id="wsa_qos_request_confirmed"></span>**WSA\_QOS\_REQUEST\_CONFIRMED**
</dt> <dd> <dl> <dt>

11009 (0x2B01)
</dt> <dt>



Reserve has been confirmed.


</dt> </dl> </dd> <dt>

<span id="WSA_QOS_ADMISSION_FAILURE"></span><span id="wsa_qos_admission_failure"></span>**WSA\_QOS\_ADMISSION\_FAILURE**
</dt> <dd> <dl> <dt>

11010 (0x2B02)
</dt> <dt>



Error due to lack of resources.


</dt> </dl> </dd> <dt>

<span id="WSA_QOS_POLICY_FAILURE"></span><span id="wsa_qos_policy_failure"></span>**WSA\_QOS\_POLICY\_FAILURE**
</dt> <dd> <dl> <dt>

11011 (0x2B03)
</dt> <dt>



Rejected for administrative reasons - bad credentials.


</dt> </dl> </dd> <dt>

<span id="WSA_QOS_BAD_STYLE"></span><span id="wsa_qos_bad_style"></span>**WSA\_QOS\_BAD\_STYLE**
</dt> <dd> <dl> <dt>

11012 (0x2B04)
</dt> <dt>



Unknown or conflicting style.


</dt> </dl> </dd> <dt>

<span id="WSA_QOS_BAD_OBJECT"></span><span id="wsa_qos_bad_object"></span>**WSA\_QOS\_BAD\_OBJECT**
</dt> <dd> <dl> <dt>

11013 (0x2B05)
</dt> <dt>



Problem with some part of the filterspec or providerspecific buffer in general.


</dt> </dl> </dd> <dt>

<span id="WSA_QOS_TRAFFIC_CTRL_ERROR"></span><span id="wsa_qos_traffic_ctrl_error"></span>**WSA\_QOS\_TRAFFIC\_CTRL\_ERROR**
</dt> <dd> <dl> <dt>

11014 (0x2B06)
</dt> <dt>



Problem with some part of the flowspec.


</dt> </dl> </dd> <dt>

<span id="WSA_QOS_GENERIC_ERROR"></span><span id="wsa_qos_generic_error"></span>**WSA\_QOS\_GENERIC\_ERROR**
</dt> <dd> <dl> <dt>

11015 (0x2B07)
</dt> <dt>



General QOS error.


</dt> </dl> </dd> <dt>

<span id="WSA_QOS_ESERVICETYPE"></span><span id="wsa_qos_eservicetype"></span>**WSA\_QOS\_ESERVICETYPE**
</dt> <dd> <dl> <dt>

11016 (0x2B08)
</dt> <dt>



An invalid or unrecognized service type was found in the flowspec.


</dt> </dl> </dd> <dt>

<span id="WSA_QOS_EFLOWSPEC"></span><span id="wsa_qos_eflowspec"></span>**WSA\_QOS\_EFLOWSPEC**
</dt> <dd> <dl> <dt>

11017 (0x2B09)
</dt> <dt>



An invalid or inconsistent flowspec was found in the QOS structure.


</dt> </dl> </dd> <dt>

<span id="WSA_QOS_EPROVSPECBUF"></span><span id="wsa_qos_eprovspecbuf"></span>**WSA\_QOS\_EPROVSPECBUF**
</dt> <dd> <dl> <dt>

11018 (0x2B0A)
</dt> <dt>



Invalid QOS provider-specific buffer.


</dt> </dl> </dd> <dt>

<span id="WSA_QOS_EFILTERSTYLE"></span><span id="wsa_qos_efilterstyle"></span>**WSA\_QOS\_EFILTERSTYLE**
</dt> <dd> <dl> <dt>

11019 (0x2B0B)
</dt> <dt>



An invalid QOS filter style was used.


</dt> </dl> </dd> <dt>

<span id="WSA_QOS_EFILTERTYPE"></span><span id="wsa_qos_efiltertype"></span>**WSA\_QOS\_EFILTERTYPE**
</dt> <dd> <dl> <dt>

11020 (0x2B0C)
</dt> <dt>



An invalid QOS filter type was used.


</dt> </dl> </dd> <dt>

<span id="WSA_QOS_EFILTERCOUNT"></span><span id="wsa_qos_efiltercount"></span>**WSA\_QOS\_EFILTERCOUNT**
</dt> <dd> <dl> <dt>

11021 (0x2B0D)
</dt> <dt>



An incorrect number of QOS FILTERSPECs were specified in the FLOWDESCRIPTOR.


</dt> </dl> </dd> <dt>

<span id="WSA_QOS_EOBJLENGTH"></span><span id="wsa_qos_eobjlength"></span>**WSA\_QOS\_EOBJLENGTH**
</dt> <dd> <dl> <dt>

11022 (0x2B0E)
</dt> <dt>



An object with an invalid ObjectLength field was specified in the QOS provider-specific buffer.


</dt> </dl> </dd> <dt>

<span id="WSA_QOS_EFLOWCOUNT"></span><span id="wsa_qos_eflowcount"></span>**WSA\_QOS\_EFLOWCOUNT**
</dt> <dd> <dl> <dt>

11023 (0x2B0F)
</dt> <dt>



An incorrect number of flow descriptors was specified in the QOS structure.


</dt> </dl> </dd> <dt>

<span id="WSA_QOS_EUNKOWNPSOBJ"></span><span id="wsa_qos_eunkownpsobj"></span>**WSA\_QOS\_EUNKOWNPSOBJ**
</dt> <dd> <dl> <dt>

11024 (0x2B10)
</dt> <dt>



An unrecognized object was found in the QOS provider-specific buffer.


</dt> </dl> </dd> <dt>

<span id="WSA_QOS_EPOLICYOBJ"></span><span id="wsa_qos_epolicyobj"></span>**WSA\_QOS\_EPOLICYOBJ**
</dt> <dd> <dl> <dt>

11025 (0x2B11)
</dt> <dt>



An invalid policy object was found in the QOS provider-specific buffer.


</dt> </dl> </dd> <dt>

<span id="WSA_QOS_EFLOWDESC"></span><span id="wsa_qos_eflowdesc"></span>**WSA\_QOS\_EFLOWDESC**
</dt> <dd> <dl> <dt>

11026 (0x2B12)
</dt> <dt>



An invalid QOS flow descriptor was found in the flow descriptor list.


</dt> </dl> </dd> <dt>

<span id="WSA_QOS_EPSFLOWSPEC"></span><span id="wsa_qos_epsflowspec"></span>**WSA\_QOS\_EPSFLOWSPEC**
</dt> <dd> <dl> <dt>

11027 (0x2B13)
</dt> <dt>



An invalid or inconsistent flowspec was found in the QOS provider specific buffer.


</dt> </dl> </dd> <dt>

<span id="WSA_QOS_EPSFILTERSPEC"></span><span id="wsa_qos_epsfilterspec"></span>**WSA\_QOS\_EPSFILTERSPEC**
</dt> <dd> <dl> <dt>

11028 (0x2B14)
</dt> <dt>



An invalid FILTERSPEC was found in the QOS provider-specific buffer.


</dt> </dl> </dd> <dt>

<span id="WSA_QOS_ESDMODEOBJ"></span><span id="wsa_qos_esdmodeobj"></span>**WSA\_QOS\_ESDMODEOBJ**
</dt> <dd> <dl> <dt>

11029 (0x2B15)
</dt> <dt>



An invalid shape discard mode object was found in the QOS provider specific buffer.


</dt> </dl> </dd> <dt>

<span id="WSA_QOS_ESHAPERATEOBJ"></span><span id="wsa_qos_eshaperateobj"></span>**WSA\_QOS\_ESHAPERATEOBJ**
</dt> <dd> <dl> <dt>

11030 (0x2B16)
</dt> <dt>



An invalid shaping rate object was found in the QOS provider-specific buffer.


</dt> </dl> </dd> <dt>

<span id="WSA_QOS_RESERVED_PETYPE"></span><span id="wsa_qos_reserved_petype"></span>**WSA\_QOS\_RESERVED\_PETYPE**
</dt> <dd> <dl> <dt>

11031 (0x2B17)
</dt> <dt>



A reserved policy element was found in the QOS provider-specific buffer.


</dt> </dl> </dd> <dt>

<span id="WSA_SECURE_HOST_NOT_FOUND"></span><span id="wsa_secure_host_not_found"></span>**WSA\_SECURE\_HOST\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

11032 (0x2B18)
</dt> <dt>



No such host is known securely.


</dt> </dl> </dd> <dt>

<span id="WSA_IPSEC_NAME_POLICY_ERROR"></span><span id="wsa_ipsec_name_policy_error"></span>**WSA\_IPSEC\_NAME\_POLICY\_ERROR**
</dt> <dd> <dl> <dt>

11033 (0x2B19)
</dt> <dt>



Name based IPSEC policy could not be added.


</dt> </dl> </dd> </dl>


## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>WinError.h</dt> </dl> |



## See also

<dl> <dt>

[System Error Codes](system-error-codes.md)
</dt> </dl>

 

 




