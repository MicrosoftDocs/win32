---
description: Describes error codes 9000-11999 defined in the WinError.h header file and is intended for developers.
ms.assetid: 27fe3fee-4ae3-43f1-a1f2-91c935e9851b
title: System Error Codes (9000-11999) (WinError.h)
ms.topic: reference
ms.date: 07/15/2024
---

# System Error Codes (9000-11999)

The following list describes [system error codes](system-error-codes.md) (errors 9000 to 11999). They are returned by the [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) function when many functions fail. To retrieve the description text for the error in your application, use the [**FormatMessage**](/windows/desktop/api/WinBase/nf-winbase-formatmessage) function with the **FORMAT\_MESSAGE\_FROM\_SYSTEM** flag.

> [!NOTE]
> This information is intended for developers debugging system errors. For other errors, such as issues with Windows Update, see the list of resources on the [Error codes](system-error-codes.md) page.

 

<span id="DNS_ERROR_RCODE_FORMAT_ERROR"></span><span id="dns_error_rcode_format_error"></span>**DNS\_ERROR\_RCODE\_FORMAT\_ERROR**
   

9001 (0x2329)
 



DNS server unable to interpret format.


   

<span id="DNS_ERROR_RCODE_SERVER_FAILURE"></span><span id="dns_error_rcode_server_failure"></span>**DNS\_ERROR\_RCODE\_SERVER\_FAILURE**
   

9002 (0x232A)
 



DNS server failure.


   

<span id="DNS_ERROR_RCODE_NAME_ERROR"></span><span id="dns_error_rcode_name_error"></span>**DNS\_ERROR\_RCODE\_NAME\_ERROR**
   

9003 (0x232B)
 



DNS name does not exist.


   

<span id="DNS_ERROR_RCODE_NOT_IMPLEMENTED"></span><span id="dns_error_rcode_not_implemented"></span>**DNS\_ERROR\_RCODE\_NOT\_IMPLEMENTED**
   

9004 (0x232C)
 



DNS request not supported by name server.


   

<span id="DNS_ERROR_RCODE_REFUSED"></span><span id="dns_error_rcode_refused"></span>**DNS\_ERROR\_RCODE\_REFUSED**
   

9005 (0x232D)
 



DNS operation refused.


   

<span id="DNS_ERROR_RCODE_YXDOMAIN"></span><span id="dns_error_rcode_yxdomain"></span>**DNS\_ERROR\_RCODE\_YXDOMAIN**
   

9006 (0x232E)
 



DNS name that ought not exist, does exist.


   

<span id="DNS_ERROR_RCODE_YXRRSET"></span><span id="dns_error_rcode_yxrrset"></span>**DNS\_ERROR\_RCODE\_YXRRSET**
   

9007 (0x232F)
 



DNS RR set that ought not exist, does exist.


   

<span id="DNS_ERROR_RCODE_NXRRSET"></span><span id="dns_error_rcode_nxrrset"></span>**DNS\_ERROR\_RCODE\_NXRRSET**
   

9008 (0x2330)
 



DNS RR set that ought to exist, does not exist.


   

<span id="DNS_ERROR_RCODE_NOTAUTH"></span><span id="dns_error_rcode_notauth"></span>**DNS\_ERROR\_RCODE\_NOTAUTH**
   

9009 (0x2331)
 



DNS server not authoritative for zone.


   

<span id="DNS_ERROR_RCODE_NOTZONE"></span><span id="dns_error_rcode_notzone"></span>**DNS\_ERROR\_RCODE\_NOTZONE**
   

9010 (0x2332)
 



DNS name in update or prereq is not in zone.


   

<span id="DNS_ERROR_RCODE_BADSIG"></span><span id="dns_error_rcode_badsig"></span>**DNS\_ERROR\_RCODE\_BADSIG**
   

9016 (0x2338)
 



DNS signature failed to verify.


   

<span id="DNS_ERROR_RCODE_BADKEY"></span><span id="dns_error_rcode_badkey"></span>**DNS\_ERROR\_RCODE\_BADKEY**
   

9017 (0x2339)
 



DNS bad key.


   

<span id="DNS_ERROR_RCODE_BADTIME"></span><span id="dns_error_rcode_badtime"></span>**DNS\_ERROR\_RCODE\_BADTIME**
   

9018 (0x233A)
 



DNS signature validity expired.


   

<span id="DNS_ERROR_KEYMASTER_REQUIRED"></span><span id="dns_error_keymaster_required"></span>**DNS\_ERROR\_KEYMASTER\_REQUIRED**
   

9101 (0x238D)
 



Only the DNS server acting as the key master for the zone may perform this operation.


   

<span id="DNS_ERROR_NOT_ALLOWED_ON_SIGNED_ZONE"></span><span id="dns_error_not_allowed_on_signed_zone"></span>**DNS\_ERROR\_NOT\_ALLOWED\_ON\_SIGNED\_ZONE**
   

9102 (0x238E)
 



This operation is not allowed on a zone that is signed or has signing keys.


   

<span id="DNS_ERROR_NSEC3_INCOMPATIBLE_WITH_RSA_SHA1"></span><span id="dns_error_nsec3_incompatible_with_rsa_sha1"></span>**DNS\_ERROR\_NSEC3\_INCOMPATIBLE\_WITH\_RSA\_SHA1**
   

9103 (0x238F)
 



NSEC3 is not compatible with the RSA-SHA-1 algorithm. Choose a different algorithm or use NSEC.

This value was also named **DNS\_ERROR\_INVALID\_NSEC3\_PARAMETERS**


   

<span id="DNS_ERROR_NOT_ENOUGH_SIGNING_KEY_DESCRIPTORS"></span><span id="dns_error_not_enough_signing_key_descriptors"></span>**DNS\_ERROR\_NOT\_ENOUGH\_SIGNING\_KEY\_DESCRIPTORS**
   

9104 (0x2390)
 



The zone does not have enough signing keys. There must be at least one key signing key (KSK) and at least one zone signing key (ZSK).


   

<span id="DNS_ERROR_UNSUPPORTED_ALGORITHM"></span><span id="dns_error_unsupported_algorithm"></span>**DNS\_ERROR\_UNSUPPORTED\_ALGORITHM**
   

9105 (0x2391)
 



The specified algorithm is not supported.


   

<span id="DNS_ERROR_INVALID_KEY_SIZE"></span><span id="dns_error_invalid_key_size"></span>**DNS\_ERROR\_INVALID\_KEY\_SIZE**
   

9106 (0x2392)
 



The specified key size is not supported.


   

<span id="DNS_ERROR_SIGNING_KEY_NOT_ACCESSIBLE"></span><span id="dns_error_signing_key_not_accessible"></span>**DNS\_ERROR\_SIGNING\_KEY\_NOT\_ACCESSIBLE**
   

9107 (0x2393)
 



One or more of the signing keys for a zone are not accessible to the DNS server. Zone signing will not be operational until this error is resolved.


   

<span id="DNS_ERROR_KSP_DOES_NOT_SUPPORT_PROTECTION"></span><span id="dns_error_ksp_does_not_support_protection"></span>**DNS\_ERROR\_KSP\_DOES\_NOT\_SUPPORT\_PROTECTION**
   

9108 (0x2394)
 



The specified key storage provider does not support DPAPI++ data protection. Zone signing will not be operational until this error is resolved.


   

<span id="DNS_ERROR_UNEXPECTED_DATA_PROTECTION_ERROR"></span><span id="dns_error_unexpected_data_protection_error"></span>**DNS\_ERROR\_UNEXPECTED\_DATA\_PROTECTION\_ERROR**
   

9109 (0x2395)
 



An unexpected DPAPI++ error was encountered. Zone signing will not be operational until this error is resolved.


   

<span id="DNS_ERROR_UNEXPECTED_CNG_ERROR"></span><span id="dns_error_unexpected_cng_error"></span>**DNS\_ERROR\_UNEXPECTED\_CNG\_ERROR**
   

9110 (0x2396)
 



An unexpected crypto error was encountered. Zone signing may not be operational until this error is resolved.


   

<span id="DNS_ERROR_UNKNOWN_SIGNING_PARAMETER_VERSION"></span><span id="dns_error_unknown_signing_parameter_version"></span>**DNS\_ERROR\_UNKNOWN\_SIGNING\_PARAMETER\_VERSION**
   

9111 (0x2397)
 



The DNS server encountered a signing key with an unknown version. Zone signing will not be operational until this error is resolved.


   

<span id="DNS_ERROR_KSP_NOT_ACCESSIBLE"></span><span id="dns_error_ksp_not_accessible"></span>**DNS\_ERROR\_KSP\_NOT\_ACCESSIBLE**
   

9112 (0x2398)
 



The specified key service provider cannot be opened by the DNS server.


   

<span id="DNS_ERROR_TOO_MANY_SKDS"></span><span id="dns_error_too_many_skds"></span>**DNS\_ERROR\_TOO\_MANY\_SKDS**
   

9113 (0x2399)
 



The DNS server cannot accept any more signing keys with the specified algorithm and KSK flag value for this zone.


   

<span id="DNS_ERROR_INVALID_ROLLOVER_PERIOD"></span><span id="dns_error_invalid_rollover_period"></span>**DNS\_ERROR\_INVALID\_ROLLOVER\_PERIOD**
   

9114 (0x239A)
 



The specified rollover period is invalid.


   

<span id="DNS_ERROR_INVALID_INITIAL_ROLLOVER_OFFSET"></span><span id="dns_error_invalid_initial_rollover_offset"></span>**DNS\_ERROR\_INVALID\_INITIAL\_ROLLOVER\_OFFSET**
   

9115 (0x239B)
 



The specified initial rollover offset is invalid.


   

<span id="DNS_ERROR_ROLLOVER_IN_PROGRESS"></span><span id="dns_error_rollover_in_progress"></span>**DNS\_ERROR\_ROLLOVER\_IN\_PROGRESS**
   

9116 (0x239C)
 



The specified signing key is already in process of rolling over keys.


   

<span id="DNS_ERROR_STANDBY_KEY_NOT_PRESENT"></span><span id="dns_error_standby_key_not_present"></span>**DNS\_ERROR\_STANDBY\_KEY\_NOT\_PRESENT**
   

9117 (0x239D)
 



The specified signing key does not have a standby key to revoke.


   

<span id="DNS_ERROR_NOT_ALLOWED_ON_ZSK"></span><span id="dns_error_not_allowed_on_zsk"></span>**DNS\_ERROR\_NOT\_ALLOWED\_ON\_ZSK**
   

9118 (0x239E)
 



This operation is not allowed on a zone signing key (ZSK).


   

<span id="DNS_ERROR_NOT_ALLOWED_ON_ACTIVE_SKD"></span><span id="dns_error_not_allowed_on_active_skd"></span>**DNS\_ERROR\_NOT\_ALLOWED\_ON\_ACTIVE\_SKD**
   

9119 (0x239F)
 



This operation is not allowed on an active signing key.


   

<span id="DNS_ERROR_ROLLOVER_ALREADY_QUEUED"></span><span id="dns_error_rollover_already_queued"></span>**DNS\_ERROR\_ROLLOVER\_ALREADY\_QUEUED**
   

9120 (0x23A0)
 



The specified signing key is already queued for rollover.


   

<span id="DNS_ERROR_NOT_ALLOWED_ON_UNSIGNED_ZONE"></span><span id="dns_error_not_allowed_on_unsigned_zone"></span>**DNS\_ERROR\_NOT\_ALLOWED\_ON\_UNSIGNED\_ZONE**
   

9121 (0x23A1)
 



This operation is not allowed on an unsigned zone.


   

<span id="DNS_ERROR_BAD_KEYMASTER"></span><span id="dns_error_bad_keymaster"></span>**DNS\_ERROR\_BAD\_KEYMASTER**
   

9122 (0x23A2)
 



This operation could not be completed because the DNS server listed as the current key master for this zone is down or misconfigured. Resolve the problem on the current key master for this zone or use another DNS server to seize the key master role.


   

<span id="DNS_ERROR_INVALID_SIGNATURE_VALIDITY_PERIOD"></span><span id="dns_error_invalid_signature_validity_period"></span>**DNS\_ERROR\_INVALID\_SIGNATURE\_VALIDITY\_PERIOD**
   

9123 (0x23A3)
 



The specified signature validity period is invalid.


   

<span id="DNS_ERROR_INVALID_NSEC3_ITERATION_COUNT"></span><span id="dns_error_invalid_nsec3_iteration_count"></span>**DNS\_ERROR\_INVALID\_NSEC3\_ITERATION\_COUNT**
   

9124 (0x23A4)
 



The specified NSEC3 iteration count is higher than allowed by the minimum key length used in the zone.


   

<span id="DNS_ERROR_DNSSEC_IS_DISABLED"></span><span id="dns_error_dnssec_is_disabled"></span>**DNS\_ERROR\_DNSSEC\_IS\_DISABLED**
   

9125 (0x23A5)
 



This operation could not be completed because the DNS server has been configured with DNSSEC features disabled. Enable DNSSEC on the DNS server.


   

<span id="DNS_ERROR_INVALID_XML"></span><span id="dns_error_invalid_xml"></span>**DNS\_ERROR\_INVALID\_XML**
   

9126 (0x23A6)
 



This operation could not be completed because the XML stream received is empty or syntactically invalid.


   

<span id="DNS_ERROR_NO_VALID_TRUST_ANCHORS"></span><span id="dns_error_no_valid_trust_anchors"></span>**DNS\_ERROR\_NO\_VALID\_TRUST\_ANCHORS**
   

9127 (0x23A7)
 



This operation completed, but no trust anchors were added because all of the trust anchors received were either invalid, unsupported, expired, or would not become valid in less than 30 days.


   

<span id="DNS_ERROR_ROLLOVER_NOT_POKEABLE"></span><span id="dns_error_rollover_not_pokeable"></span>**DNS\_ERROR\_ROLLOVER\_NOT\_POKEABLE**
   

9128 (0x23A8)
 



The specified signing key is not waiting for parental DS update.


   

<span id="DNS_ERROR_NSEC3_NAME_COLLISION"></span><span id="dns_error_nsec3_name_collision"></span>**DNS\_ERROR\_NSEC3\_NAME\_COLLISION**
   

9129 (0x23A9)
 



Hash collision detected during NSEC3 signing. Specify a different user-provided salt, or use a randomly generated salt, and attempt to sign the zone again.


   

<span id="DNS_ERROR_NSEC_INCOMPATIBLE_WITH_NSEC3_RSA_SHA1"></span><span id="dns_error_nsec_incompatible_with_nsec3_rsa_sha1"></span>**DNS\_ERROR\_NSEC\_INCOMPATIBLE\_WITH\_NSEC3\_RSA\_SHA1**
   

9130 (0x23AA)
 



NSEC is not compatible with the NSEC3-RSA-SHA-1 algorithm. Choose a different algorithm or use NSEC3.


   

<span id="DNS_INFO_NO_RECORDS"></span><span id="dns_info_no_records"></span>**DNS\_INFO\_NO\_RECORDS**
   

9501 (0x251D)
 



No records found for given DNS query.


   

<span id="DNS_ERROR_BAD_PACKET"></span><span id="dns_error_bad_packet"></span>**DNS\_ERROR\_BAD\_PACKET**
   

9502 (0x251E)
 



Bad DNS packet.


   

<span id="DNS_ERROR_NO_PACKET"></span><span id="dns_error_no_packet"></span>**DNS\_ERROR\_NO\_PACKET**
   

9503 (0x251F)
 



No DNS packet.


   

<span id="DNS_ERROR_RCODE"></span><span id="dns_error_rcode"></span>**DNS\_ERROR\_RCODE**
   

9504 (0x2520)
 



DNS error, check rcode.


   

<span id="DNS_ERROR_UNSECURE_PACKET"></span><span id="dns_error_unsecure_packet"></span>**DNS\_ERROR\_UNSECURE\_PACKET**
   

9505 (0x2521)
 



Unsecured DNS packet.


   

<span id="DNS_REQUEST_PENDING"></span><span id="dns_request_pending"></span>**DNS\_REQUEST\_PENDING**
   

9506 (0x2522)
 



DNS query request is pending.


   

<span id="DNS_ERROR_INVALID_TYPE"></span><span id="dns_error_invalid_type"></span>**DNS\_ERROR\_INVALID\_TYPE**
   

9551 (0x254F)
 



Invalid DNS type.


   

<span id="DNS_ERROR_INVALID_IP_ADDRESS"></span><span id="dns_error_invalid_ip_address"></span>**DNS\_ERROR\_INVALID\_IP\_ADDRESS**
   

9552 (0x2550)
 



Invalid IP address.


   

<span id="DNS_ERROR_INVALID_PROPERTY"></span><span id="dns_error_invalid_property"></span>**DNS\_ERROR\_INVALID\_PROPERTY**
   

9553 (0x2551)
 



Invalid property.


   

<span id="DNS_ERROR_TRY_AGAIN_LATER"></span><span id="dns_error_try_again_later"></span>**DNS\_ERROR\_TRY\_AGAIN\_LATER**
   

9554 (0x2552)
 



Try DNS operation again later.


   

<span id="DNS_ERROR_NOT_UNIQUE"></span><span id="dns_error_not_unique"></span>**DNS\_ERROR\_NOT\_UNIQUE**
   

9555 (0x2553)
 



Record for given name and type is not unique.


   

<span id="DNS_ERROR_NON_RFC_NAME"></span><span id="dns_error_non_rfc_name"></span>**DNS\_ERROR\_NON\_RFC\_NAME**
   

9556 (0x2554)
 



DNS name does not comply with RFC specifications.


   

<span id="DNS_STATUS_FQDN"></span><span id="dns_status_fqdn"></span>**DNS\_STATUS\_FQDN**
   

9557 (0x2555)
 



DNS name is a fully-qualified DNS name.


   

<span id="DNS_STATUS_DOTTED_NAME"></span><span id="dns_status_dotted_name"></span>**DNS\_STATUS\_DOTTED\_NAME**
   

9558 (0x2556)
 



DNS name is dotted (multi-label).


   

<span id="DNS_STATUS_SINGLE_PART_NAME"></span><span id="dns_status_single_part_name"></span>**DNS\_STATUS\_SINGLE\_PART\_NAME**
   

9559 (0x2557)
 



DNS name is a single-part name.


   

<span id="DNS_ERROR_INVALID_NAME_CHAR"></span><span id="dns_error_invalid_name_char"></span>**DNS\_ERROR\_INVALID\_NAME\_CHAR**
   

9560 (0x2558)
 



DNS name contains an invalid character.


   

<span id="DNS_ERROR_NUMERIC_NAME"></span><span id="dns_error_numeric_name"></span>**DNS\_ERROR\_NUMERIC\_NAME**
   

9561 (0x2559)
 



DNS name is entirely numeric.


   

<span id="DNS_ERROR_NOT_ALLOWED_ON_ROOT_SERVER"></span><span id="dns_error_not_allowed_on_root_server"></span>**DNS\_ERROR\_NOT\_ALLOWED\_ON\_ROOT\_SERVER**
   

9562 (0x255A)
 



The operation requested is not permitted on a DNS root server.


   

<span id="DNS_ERROR_NOT_ALLOWED_UNDER_DELEGATION"></span><span id="dns_error_not_allowed_under_delegation"></span>**DNS\_ERROR\_NOT\_ALLOWED\_UNDER\_DELEGATION**
   

9563 (0x255B)
 



The record could not be created because this part of the DNS namespace has been delegated to another server.


   

<span id="DNS_ERROR_CANNOT_FIND_ROOT_HINTS"></span><span id="dns_error_cannot_find_root_hints"></span>**DNS\_ERROR\_CANNOT\_FIND\_ROOT\_HINTS**
   

9564 (0x255C)
 



The DNS server could not find a set of root hints.


   

<span id="DNS_ERROR_INCONSISTENT_ROOT_HINTS"></span><span id="dns_error_inconsistent_root_hints"></span>**DNS\_ERROR\_INCONSISTENT\_ROOT\_HINTS**
   

9565 (0x255D)
 



The DNS server found root hints but they were not consistent across all adapters.


   

<span id="DNS_ERROR_DWORD_VALUE_TOO_SMALL"></span><span id="dns_error_dword_value_too_small"></span>**DNS\_ERROR\_DWORD\_VALUE\_TOO\_SMALL**
   

9566 (0x255E)
 



The specified value is too small for this parameter.


   

<span id="DNS_ERROR_DWORD_VALUE_TOO_LARGE"></span><span id="dns_error_dword_value_too_large"></span>**DNS\_ERROR\_DWORD\_VALUE\_TOO\_LARGE**
   

9567 (0x255F)
 



The specified value is too large for this parameter.


   

<span id="DNS_ERROR_BACKGROUND_LOADING"></span><span id="dns_error_background_loading"></span>**DNS\_ERROR\_BACKGROUND\_LOADING**
   

9568 (0x2560)
 



This operation is not allowed while the DNS server is loading zones in the background. Please try again later.


   

<span id="DNS_ERROR_NOT_ALLOWED_ON_RODC"></span><span id="dns_error_not_allowed_on_rodc"></span>**DNS\_ERROR\_NOT\_ALLOWED\_ON\_RODC**
   

9569 (0x2561)
 



The operation requested is not permitted on against a DNS server running on a read-only DC.


   

<span id="DNS_ERROR_NOT_ALLOWED_UNDER_DNAME"></span><span id="dns_error_not_allowed_under_dname"></span>**DNS\_ERROR\_NOT\_ALLOWED\_UNDER\_DNAME**
   

9570 (0x2562)
 



No data is allowed to exist underneath a DNAME record.


   

<span id="DNS_ERROR_DELEGATION_REQUIRED"></span><span id="dns_error_delegation_required"></span>**DNS\_ERROR\_DELEGATION\_REQUIRED**
   

9571 (0x2563)
 



This operation requires credentials delegation.


   

<span id="DNS_ERROR_INVALID_POLICY_TABLE"></span><span id="dns_error_invalid_policy_table"></span>**DNS\_ERROR\_INVALID\_POLICY\_TABLE**
   

9572 (0x2564)
 



Name resolution policy table has been corrupted. DNS resolution will fail until it is fixed. Contact your network administrator.


   

<span id="DNS_ERROR_ZONE_DOES_NOT_EXIST"></span><span id="dns_error_zone_does_not_exist"></span>**DNS\_ERROR\_ZONE\_DOES\_NOT\_EXIST**
   

9601 (0x2581)
 



DNS zone does not exist.


   

<span id="DNS_ERROR_NO_ZONE_INFO"></span><span id="dns_error_no_zone_info"></span>**DNS\_ERROR\_NO\_ZONE\_INFO**
   

9602 (0x2582)
 



DNS zone information not available.


   

<span id="DNS_ERROR_INVALID_ZONE_OPERATION"></span><span id="dns_error_invalid_zone_operation"></span>**DNS\_ERROR\_INVALID\_ZONE\_OPERATION**
   

9603 (0x2583)
 



Invalid operation for DNS zone.


   

<span id="DNS_ERROR_ZONE_CONFIGURATION_ERROR"></span><span id="dns_error_zone_configuration_error"></span>**DNS\_ERROR\_ZONE\_CONFIGURATION\_ERROR**
   

9604 (0x2584)
 



Invalid DNS zone configuration.


   

<span id="DNS_ERROR_ZONE_HAS_NO_SOA_RECORD"></span><span id="dns_error_zone_has_no_soa_record"></span>**DNS\_ERROR\_ZONE\_HAS\_NO\_SOA\_RECORD**
   

9605 (0x2585)
 



DNS zone has no start of authority (SOA) record.


   

<span id="DNS_ERROR_ZONE_HAS_NO_NS_RECORDS"></span><span id="dns_error_zone_has_no_ns_records"></span>**DNS\_ERROR\_ZONE\_HAS\_NO\_NS\_RECORDS**
   

9606 (0x2586)
 



DNS zone has no Name Server (NS) record.


   

<span id="DNS_ERROR_ZONE_LOCKED"></span><span id="dns_error_zone_locked"></span>**DNS\_ERROR\_ZONE\_LOCKED**
   

9607 (0x2587)
 



DNS zone is locked.


   

<span id="DNS_ERROR_ZONE_CREATION_FAILED"></span><span id="dns_error_zone_creation_failed"></span>**DNS\_ERROR\_ZONE\_CREATION\_FAILED**
   

9608 (0x2588)
 



DNS zone creation failed.


   

<span id="DNS_ERROR_ZONE_ALREADY_EXISTS"></span><span id="dns_error_zone_already_exists"></span>**DNS\_ERROR\_ZONE\_ALREADY\_EXISTS**
   

9609 (0x2589)
 



DNS zone already exists.


   

<span id="DNS_ERROR_AUTOZONE_ALREADY_EXISTS"></span><span id="dns_error_autozone_already_exists"></span>**DNS\_ERROR\_AUTOZONE\_ALREADY\_EXISTS**
   

9610 (0x258A)
 



DNS automatic zone already exists.


   

<span id="DNS_ERROR_INVALID_ZONE_TYPE"></span><span id="dns_error_invalid_zone_type"></span>**DNS\_ERROR\_INVALID\_ZONE\_TYPE**
   

9611 (0x258B)
 



Invalid DNS zone type.


   

<span id="DNS_ERROR_SECONDARY_REQUIRES_MASTER_IP"></span><span id="dns_error_secondary_requires_master_ip"></span>**DNS\_ERROR\_SECONDARY\_REQUIRES\_MASTER\_IP**
   

9612 (0x258C)
 



Secondary DNS zone requires master IP address.


   

<span id="DNS_ERROR_ZONE_NOT_SECONDARY"></span><span id="dns_error_zone_not_secondary"></span>**DNS\_ERROR\_ZONE\_NOT\_SECONDARY**
   

9613 (0x258D)
 



DNS zone not secondary.


   

<span id="DNS_ERROR_NEED_SECONDARY_ADDRESSES"></span><span id="dns_error_need_secondary_addresses"></span>**DNS\_ERROR\_NEED\_SECONDARY\_ADDRESSES**
   

9614 (0x258E)
 



Need secondary IP address.


   

<span id="DNS_ERROR_WINS_INIT_FAILED"></span><span id="dns_error_wins_init_failed"></span>**DNS\_ERROR\_WINS\_INIT\_FAILED**
   

9615 (0x258F)
 



WINS initialization failed.


   

<span id="DNS_ERROR_NEED_WINS_SERVERS"></span><span id="dns_error_need_wins_servers"></span>**DNS\_ERROR\_NEED\_WINS\_SERVERS**
   

9616 (0x2590)
 



Need WINS servers.


   

<span id="DNS_ERROR_NBSTAT_INIT_FAILED"></span><span id="dns_error_nbstat_init_failed"></span>**DNS\_ERROR\_NBSTAT\_INIT\_FAILED**
   

9617 (0x2591)
 



NBTSTAT initialization call failed.


   

<span id="DNS_ERROR_SOA_DELETE_INVALID"></span><span id="dns_error_soa_delete_invalid"></span>**DNS\_ERROR\_SOA\_DELETE\_INVALID**
   

9618 (0x2592)
 



Invalid delete of start of authority (SOA).


   

<span id="DNS_ERROR_FORWARDER_ALREADY_EXISTS"></span><span id="dns_error_forwarder_already_exists"></span>**DNS\_ERROR\_FORWARDER\_ALREADY\_EXISTS**
   

9619 (0x2593)
 



A conditional forwarding zone already exists for that name.


   

<span id="DNS_ERROR_ZONE_REQUIRES_MASTER_IP"></span><span id="dns_error_zone_requires_master_ip"></span>**DNS\_ERROR\_ZONE\_REQUIRES\_MASTER\_IP**
   

9620 (0x2594)
 



This zone must be configured with one or more master DNS server IP addresses.


   

<span id="DNS_ERROR_ZONE_IS_SHUTDOWN"></span><span id="dns_error_zone_is_shutdown"></span>**DNS\_ERROR\_ZONE\_IS\_SHUTDOWN**
   

9621 (0x2595)
 



The operation cannot be performed because this zone is shut down.


   

<span id="DNS_ERROR_ZONE_LOCKED_FOR_SIGNING"></span><span id="dns_error_zone_locked_for_signing"></span>**DNS\_ERROR\_ZONE\_LOCKED\_FOR\_SIGNING**
   

9622 (0x2596)
 



This operation cannot be performed because the zone is currently being signed. Please try again later.


   

<span id="DNS_ERROR_PRIMARY_REQUIRES_DATAFILE"></span><span id="dns_error_primary_requires_datafile"></span>**DNS\_ERROR\_PRIMARY\_REQUIRES\_DATAFILE**
   

9651 (0x25B3)
 



Primary DNS zone requires datafile.


   

<span id="DNS_ERROR_INVALID_DATAFILE_NAME"></span><span id="dns_error_invalid_datafile_name"></span>**DNS\_ERROR\_INVALID\_DATAFILE\_NAME**
   

9652 (0x25B4)
 



Invalid datafile name for DNS zone.


   

<span id="DNS_ERROR_DATAFILE_OPEN_FAILURE"></span><span id="dns_error_datafile_open_failure"></span>**DNS\_ERROR\_DATAFILE\_OPEN\_FAILURE**
   

9653 (0x25B5)
 



Failed to open datafile for DNS zone.


   

<span id="DNS_ERROR_FILE_WRITEBACK_FAILED"></span><span id="dns_error_file_writeback_failed"></span>**DNS\_ERROR\_FILE\_WRITEBACK\_FAILED**
   

9654 (0x25B6)
 



Failed to write datafile for DNS zone.


   

<span id="DNS_ERROR_DATAFILE_PARSING"></span><span id="dns_error_datafile_parsing"></span>**DNS\_ERROR\_DATAFILE\_PARSING**
   

9655 (0x25B7)
 



Failure while reading datafile for DNS zone.


   

<span id="DNS_ERROR_RECORD_DOES_NOT_EXIST"></span><span id="dns_error_record_does_not_exist"></span>**DNS\_ERROR\_RECORD\_DOES\_NOT\_EXIST**
   

9701 (0x25E5)
 



DNS record does not exist.


   

<span id="DNS_ERROR_RECORD_FORMAT"></span><span id="dns_error_record_format"></span>**DNS\_ERROR\_RECORD\_FORMAT**
   

9702 (0x25E6)
 



DNS record format error.


   

<span id="DNS_ERROR_NODE_CREATION_FAILED"></span><span id="dns_error_node_creation_failed"></span>**DNS\_ERROR\_NODE\_CREATION\_FAILED**
   

9703 (0x25E7)
 



Node creation failure in DNS.


   

<span id="DNS_ERROR_UNKNOWN_RECORD_TYPE"></span><span id="dns_error_unknown_record_type"></span>**DNS\_ERROR\_UNKNOWN\_RECORD\_TYPE**
   

9704 (0x25E8)
 



Unknown DNS record type.


   

<span id="DNS_ERROR_RECORD_TIMED_OUT"></span><span id="dns_error_record_timed_out"></span>**DNS\_ERROR\_RECORD\_TIMED\_OUT**
   

9705 (0x25E9)
 



DNS record timed out.


   

<span id="DNS_ERROR_NAME_NOT_IN_ZONE"></span><span id="dns_error_name_not_in_zone"></span>**DNS\_ERROR\_NAME\_NOT\_IN\_ZONE**
   

9706 (0x25EA)
 



Name not in DNS zone.


   

<span id="DNS_ERROR_CNAME_LOOP"></span><span id="dns_error_cname_loop"></span>**DNS\_ERROR\_CNAME\_LOOP**
   

9707 (0x25EB)
 



CNAME loop detected.


   

<span id="DNS_ERROR_NODE_IS_CNAME"></span><span id="dns_error_node_is_cname"></span>**DNS\_ERROR\_NODE\_IS\_CNAME**
   

9708 (0x25EC)
 



Node is a CNAME DNS record.


   

<span id="DNS_ERROR_CNAME_COLLISION"></span><span id="dns_error_cname_collision"></span>**DNS\_ERROR\_CNAME\_COLLISION**
   

9709 (0x25ED)
 



A CNAME record already exists for given name.


   

<span id="DNS_ERROR_RECORD_ONLY_AT_ZONE_ROOT"></span><span id="dns_error_record_only_at_zone_root"></span>**DNS\_ERROR\_RECORD\_ONLY\_AT\_ZONE\_ROOT**
   

9710 (0x25EE)
 



Record only at DNS zone root.


   

<span id="DNS_ERROR_RECORD_ALREADY_EXISTS"></span><span id="dns_error_record_already_exists"></span>**DNS\_ERROR\_RECORD\_ALREADY\_EXISTS**
   

9711 (0x25EF)
 



DNS record already exists.


   

<span id="DNS_ERROR_SECONDARY_DATA"></span><span id="dns_error_secondary_data"></span>**DNS\_ERROR\_SECONDARY\_DATA**
   

9712 (0x25F0)
 



Secondary DNS zone data error.


   

<span id="DNS_ERROR_NO_CREATE_CACHE_DATA"></span><span id="dns_error_no_create_cache_data"></span>**DNS\_ERROR\_NO\_CREATE\_CACHE\_DATA**
   

9713 (0x25F1)
 



Could not create DNS cache data.


   

<span id="DNS_ERROR_NAME_DOES_NOT_EXIST"></span><span id="dns_error_name_does_not_exist"></span>**DNS\_ERROR\_NAME\_DOES\_NOT\_EXIST**
   

9714 (0x25F2)
 



DNS name does not exist.


   

<span id="DNS_WARNING_PTR_CREATE_FAILED"></span><span id="dns_warning_ptr_create_failed"></span>**DNS\_WARNING\_PTR\_CREATE\_FAILED**
   

9715 (0x25F3)
 



Could not create pointer (PTR) record.


   

<span id="DNS_WARNING_DOMAIN_UNDELETED"></span><span id="dns_warning_domain_undeleted"></span>**DNS\_WARNING\_DOMAIN\_UNDELETED**
   

9716 (0x25F4)
 



DNS domain was undeleted.


   

<span id="DNS_ERROR_DS_UNAVAILABLE"></span><span id="dns_error_ds_unavailable"></span>**DNS\_ERROR\_DS\_UNAVAILABLE**
   

9717 (0x25F5)
 



The directory service is unavailable.


   

<span id="DNS_ERROR_DS_ZONE_ALREADY_EXISTS"></span><span id="dns_error_ds_zone_already_exists"></span>**DNS\_ERROR\_DS\_ZONE\_ALREADY\_EXISTS**
   

9718 (0x25F6)
 



DNS zone already exists in the directory service.


   

<span id="DNS_ERROR_NO_BOOTFILE_IF_DS_ZONE"></span><span id="dns_error_no_bootfile_if_ds_zone"></span>**DNS\_ERROR\_NO\_BOOTFILE\_IF\_DS\_ZONE**
   

9719 (0x25F7)
 



DNS server not creating or reading the boot file for the directory service integrated DNS zone.


   

<span id="DNS_ERROR_NODE_IS_DNAME"></span><span id="dns_error_node_is_dname"></span>**DNS\_ERROR\_NODE\_IS\_DNAME**
   

9720 (0x25F8)
 



Node is a DNAME DNS record.


   

<span id="DNS_ERROR_DNAME_COLLISION"></span><span id="dns_error_dname_collision"></span>**DNS\_ERROR\_DNAME\_COLLISION**
   

9721 (0x25F9)
 



A DNAME record already exists for given name.


   

<span id="DNS_ERROR_ALIAS_LOOP"></span><span id="dns_error_alias_loop"></span>**DNS\_ERROR\_ALIAS\_LOOP**
   

9722 (0x25FA)
 



An alias loop has been detected with either CNAME or DNAME records.


   

<span id="DNS_INFO_AXFR_COMPLETE"></span><span id="dns_info_axfr_complete"></span>**DNS\_INFO\_AXFR\_COMPLETE**
   

9751 (0x2617)
 



DNS AXFR (zone transfer) complete.


   

<span id="DNS_ERROR_AXFR"></span><span id="dns_error_axfr"></span>**DNS\_ERROR\_AXFR**
   

9752 (0x2618)
 



DNS zone transfer failed.


   

<span id="DNS_INFO_ADDED_LOCAL_WINS"></span><span id="dns_info_added_local_wins"></span>**DNS\_INFO\_ADDED\_LOCAL\_WINS**
   

9753 (0x2619)
 



Added local WINS server.


   

<span id="DNS_STATUS_CONTINUE_NEEDED"></span><span id="dns_status_continue_needed"></span>**DNS\_STATUS\_CONTINUE\_NEEDED**
   

9801 (0x2649)
 



Secure update call needs to continue update request.


   

<span id="DNS_ERROR_NO_TCPIP"></span><span id="dns_error_no_tcpip"></span>**DNS\_ERROR\_NO\_TCPIP**
   

9851 (0x267B)
 



TCP/IP network protocol not installed.


   

<span id="DNS_ERROR_NO_DNS_SERVERS"></span><span id="dns_error_no_dns_servers"></span>**DNS\_ERROR\_NO\_DNS\_SERVERS**
   

9852 (0x267C)
 



No DNS servers configured for local system.


   

<span id="DNS_ERROR_DP_DOES_NOT_EXIST"></span><span id="dns_error_dp_does_not_exist"></span>**DNS\_ERROR\_DP\_DOES\_NOT\_EXIST**
   

9901 (0x26AD)
 



The specified directory partition does not exist.


   

<span id="DNS_ERROR_DP_ALREADY_EXISTS"></span><span id="dns_error_dp_already_exists"></span>**DNS\_ERROR\_DP\_ALREADY\_EXISTS**
   

9902 (0x26AE)
 



The specified directory partition already exists.


   

<span id="DNS_ERROR_DP_NOT_ENLISTED"></span><span id="dns_error_dp_not_enlisted"></span>**DNS\_ERROR\_DP\_NOT\_ENLISTED**
   

9903 (0x26AF)
 



This DNS server is not enlisted in the specified directory partition.


   

<span id="DNS_ERROR_DP_ALREADY_ENLISTED"></span><span id="dns_error_dp_already_enlisted"></span>**DNS\_ERROR\_DP\_ALREADY\_ENLISTED**
   

9904 (0x26B0)
 



This DNS server is already enlisted in the specified directory partition.


   

<span id="DNS_ERROR_DP_NOT_AVAILABLE"></span><span id="dns_error_dp_not_available"></span>**DNS\_ERROR\_DP\_NOT\_AVAILABLE**
   

9905 (0x26B1)
 



The directory partition is not available at this time. Please wait a few minutes and try again.


   

<span id="DNS_ERROR_DP_FSMO_ERROR"></span><span id="dns_error_dp_fsmo_error"></span>**DNS\_ERROR\_DP\_FSMO\_ERROR**
   

9906 (0x26B2)
 



The operation failed because the domain naming master FSMO role could not be reached. The domain controller holding the domain naming master FSMO role is down or unable to service the request or is not running Windows Server 2003 or later.


   

<span id="WSAEINTR"></span><span id="wsaeintr"></span>**WSAEINTR**
   

10004 (0x2714)
 



A blocking operation was interrupted by a call to WSACancelBlockingCall.


   

<span id="WSAEBADF"></span><span id="wsaebadf"></span>**WSAEBADF**
   

10009 (0x2719)
 



The file handle supplied is not valid.


   

<span id="WSAEACCES"></span><span id="wsaeacces"></span>**WSAEACCES**
   

10013 (0x271D)
 



An attempt was made to access a socket in a way forbidden by its access permissions.


   

<span id="WSAEFAULT"></span><span id="wsaefault"></span>**WSAEFAULT**
   

10014 (0x271E)
 



The system detected an invalid pointer address in attempting to use a pointer argument in a call.


   

<span id="WSAEINVAL"></span><span id="wsaeinval"></span>**WSAEINVAL**
   

10022 (0x2726)
 



An invalid argument was supplied.


   

<span id="WSAEMFILE"></span><span id="wsaemfile"></span>**WSAEMFILE**
   

10024 (0x2728)
 



Too many open sockets.


   

<span id="WSAEWOULDBLOCK"></span><span id="wsaewouldblock"></span>**WSAEWOULDBLOCK**
   

10035 (0x2733)
 



A non-blocking socket operation could not be completed immediately.


   

<span id="WSAEINPROGRESS"></span><span id="wsaeinprogress"></span>**WSAEINPROGRESS**
   

10036 (0x2734)
 



A blocking operation is currently executing.


   

<span id="WSAEALREADY"></span><span id="wsaealready"></span>**WSAEALREADY**
   

10037 (0x2735)
 



An operation was attempted on a non-blocking socket that already had an operation in progress.


   

<span id="WSAENOTSOCK"></span><span id="wsaenotsock"></span>**WSAENOTSOCK**
   

10038 (0x2736)
 



An operation was attempted on something that is not a socket.


   

<span id="WSAEDESTADDRREQ"></span><span id="wsaedestaddrreq"></span>**WSAEDESTADDRREQ**
   

10039 (0x2737)
 



A required address was omitted from an operation on a socket.


   

<span id="WSAEMSGSIZE"></span><span id="wsaemsgsize"></span>**WSAEMSGSIZE**
   

10040 (0x2738)
 



A message sent on a datagram socket was larger than the internal message buffer or some other network limit, or the buffer used to receive a datagram into was smaller than the datagram itself.


   

<span id="WSAEPROTOTYPE"></span><span id="wsaeprototype"></span>**WSAEPROTOTYPE**
   

10041 (0x2739)
 



A protocol was specified in the socket function call that does not support the semantics of the socket type requested.


   

<span id="WSAENOPROTOOPT"></span><span id="wsaenoprotoopt"></span>**WSAENOPROTOOPT**
   

10042 (0x273A)
 



An unknown, invalid, or unsupported option or level was specified in a getsockopt or setsockopt call.


   

<span id="WSAEPROTONOSUPPORT"></span><span id="wsaeprotonosupport"></span>**WSAEPROTONOSUPPORT**
   

10043 (0x273B)
 



The requested protocol has not been configured into the system, or no implementation for it exists.


   

<span id="WSAESOCKTNOSUPPORT"></span><span id="wsaesocktnosupport"></span>**WSAESOCKTNOSUPPORT**
   

10044 (0x273C)
 



The support for the specified socket type does not exist in this address family.


   

<span id="WSAEOPNOTSUPP"></span><span id="wsaeopnotsupp"></span>**WSAEOPNOTSUPP**
   

10045 (0x273D)
 



The attempted operation is not supported for the type of object referenced.


   

<span id="WSAEPFNOSUPPORT"></span><span id="wsaepfnosupport"></span>**WSAEPFNOSUPPORT**
   

10046 (0x273E)
 



The protocol family has not been configured into the system or no implementation for it exists.


   

<span id="WSAEAFNOSUPPORT"></span><span id="wsaeafnosupport"></span>**WSAEAFNOSUPPORT**
   

10047 (0x273F)
 



An address incompatible with the requested protocol was used.


   

<span id="WSAEADDRINUSE"></span><span id="wsaeaddrinuse"></span>**WSAEADDRINUSE**
   

10048 (0x2740)
 



Only one usage of each socket address (protocol/network address/port) is normally permitted.


   

<span id="WSAEADDRNOTAVAIL"></span><span id="wsaeaddrnotavail"></span>**WSAEADDRNOTAVAIL**
   

10049 (0x2741)
 



The requested address is not valid in its context.


   

<span id="WSAENETDOWN"></span><span id="wsaenetdown"></span>**WSAENETDOWN**
   

10050 (0x2742)
 



A socket operation encountered a dead network.


   

<span id="WSAENETUNREACH"></span><span id="wsaenetunreach"></span>**WSAENETUNREACH**
   

10051 (0x2743)
 



A socket operation was attempted to an unreachable network.


   

<span id="WSAENETRESET"></span><span id="wsaenetreset"></span>**WSAENETRESET**
   

10052 (0x2744)
 



The connection has been broken due to keep-alive activity detecting a failure while the operation was in progress.


   

<span id="WSAECONNABORTED"></span><span id="wsaeconnaborted"></span>**WSAECONNABORTED**
   

10053 (0x2745)
 



An established connection was aborted by the software in your host machine.


   

<span id="WSAECONNRESET"></span><span id="wsaeconnreset"></span>**WSAECONNRESET**
   

10054 (0x2746)
 



An existing connection was forcibly closed by the remote host.


   

<span id="WSAENOBUFS"></span><span id="wsaenobufs"></span>**WSAENOBUFS**
   

10055 (0x2747)
 



An operation on a socket could not be performed because the system lacked sufficient buffer space or because a queue was full.


   

<span id="WSAEISCONN"></span><span id="wsaeisconn"></span>**WSAEISCONN**
   

10056 (0x2748)
 



A connect request was made on an already connected socket.


   

<span id="WSAENOTCONN"></span><span id="wsaenotconn"></span>**WSAENOTCONN**
   

10057 (0x2749)
 



A request to send or receive data was disallowed because the socket is not connected and (when sending on a datagram socket using a sendto call) no address was supplied.


   

<span id="WSAESHUTDOWN"></span><span id="wsaeshutdown"></span>**WSAESHUTDOWN**
   

10058 (0x274A)
 



A request to send or receive data was disallowed because the socket had already been shut down in that direction with a previous shutdown call.


   

<span id="WSAETOOMANYREFS"></span><span id="wsaetoomanyrefs"></span>**WSAETOOMANYREFS**
   

10059 (0x274B)
 



Too many references to some kernel object.


   

<span id="WSAETIMEDOUT"></span><span id="wsaetimedout"></span>**WSAETIMEDOUT**
   

10060 (0x274C)
 



A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond.


   

<span id="WSAECONNREFUSED"></span><span id="wsaeconnrefused"></span>**WSAECONNREFUSED**
   

10061 (0x274D)
 



No connection could be made because the target machine actively refused it.


   

<span id="WSAELOOP"></span><span id="wsaeloop"></span>**WSAELOOP**
   

10062 (0x274E)
 



Cannot translate name.


   

<span id="WSAENAMETOOLONG"></span><span id="wsaenametoolong"></span>**WSAENAMETOOLONG**
   

10063 (0x274F)
 



Name component or name was too long.


   

<span id="WSAEHOSTDOWN"></span><span id="wsaehostdown"></span>**WSAEHOSTDOWN**
   

10064 (0x2750)
 



A socket operation failed because the destination host was down.


   

<span id="WSAEHOSTUNREACH"></span><span id="wsaehostunreach"></span>**WSAEHOSTUNREACH**
   

10065 (0x2751)
 



A socket operation was attempted to an unreachable host.


   

<span id="WSAENOTEMPTY"></span><span id="wsaenotempty"></span>**WSAENOTEMPTY**
   

10066 (0x2752)
 



Cannot remove a directory that is not empty.


   

<span id="WSAEPROCLIM"></span><span id="wsaeproclim"></span>**WSAEPROCLIM**
   

10067 (0x2753)
 



A Windows Sockets implementation may have a limit on the number of applications that may use it simultaneously.


   

<span id="WSAEUSERS"></span><span id="wsaeusers"></span>**WSAEUSERS**
   

10068 (0x2754)
 



Ran out of quota.


   

<span id="WSAEDQUOT"></span><span id="wsaedquot"></span>**WSAEDQUOT**
   

10069 (0x2755)
 



Ran out of disk quota.


   

<span id="WSAESTALE"></span><span id="wsaestale"></span>**WSAESTALE**
   

10070 (0x2756)
 



File handle reference is no longer available.


   

<span id="WSAEREMOTE"></span><span id="wsaeremote"></span>**WSAEREMOTE**
   

10071 (0x2757)
 



Item is not available locally.


   

<span id="WSASYSNOTREADY"></span><span id="wsasysnotready"></span>**WSASYSNOTREADY**
   

10091 (0x276B)
 



WSAStartup cannot function at this time because the underlying system it uses to provide network services is currently unavailable.


   

<span id="WSAVERNOTSUPPORTED"></span><span id="wsavernotsupported"></span>**WSAVERNOTSUPPORTED**
   

10092 (0x276C)
 



The Windows Sockets version requested is not supported.


   

<span id="WSANOTINITIALISED"></span><span id="wsanotinitialised"></span>**WSANOTINITIALISED**
   

10093 (0x276D)
 



Either the application has not called WSAStartup, or WSAStartup failed.


   

<span id="WSAEDISCON"></span><span id="wsaediscon"></span>**WSAEDISCON**
   

10101 (0x2775)
 



Returned by WSARecv or WSARecvFrom to indicate the remote party has initiated a graceful shutdown sequence.


   

<span id="WSAENOMORE"></span><span id="wsaenomore"></span>**WSAENOMORE**
   

10102 (0x2776)
 



No more results can be returned by WSALookupServiceNext.


   

<span id="WSAECANCELLED"></span><span id="wsaecancelled"></span>**WSAECANCELLED**
   

10103 (0x2777)
 



A call to WSALookupServiceEnd was made while this call was still processing. The call has been canceled.


   

<span id="WSAEINVALIDPROCTABLE"></span><span id="wsaeinvalidproctable"></span>**WSAEINVALIDPROCTABLE**
   

10104 (0x2778)
 



The procedure call table is invalid.


   

<span id="WSAEINVALIDPROVIDER"></span><span id="wsaeinvalidprovider"></span>**WSAEINVALIDPROVIDER**
   

10105 (0x2779)
 



The requested service provider is invalid.


   

<span id="WSAEPROVIDERFAILEDINIT"></span><span id="wsaeproviderfailedinit"></span>**WSAEPROVIDERFAILEDINIT**
   

10106 (0x277A)
 



The requested service provider could not be loaded or initialized.


   

<span id="WSASYSCALLFAILURE"></span><span id="wsasyscallfailure"></span>**WSASYSCALLFAILURE**
   

10107 (0x277B)
 



A system call has failed.


   

<span id="WSASERVICE_NOT_FOUND"></span><span id="wsaservice_not_found"></span>**WSASERVICE\_NOT\_FOUND**
   

10108 (0x277C)
 



No such service is known. The service cannot be found in the specified name space.


   

<span id="WSATYPE_NOT_FOUND"></span><span id="wsatype_not_found"></span>**WSATYPE\_NOT\_FOUND**
   

10109 (0x277D)
 



The specified class was not found.


   

<span id="WSA_E_NO_MORE"></span><span id="wsa_e_no_more"></span>**WSA\_E\_NO\_MORE**
   

10110 (0x277E)
 



No more results can be returned by WSALookupServiceNext.


   

<span id="WSA_E_CANCELLED"></span><span id="wsa_e_cancelled"></span>**WSA\_E\_CANCELLED**
   

10111 (0x277F)
 



A call to WSALookupServiceEnd was made while this call was still processing. The call has been canceled.


   

<span id="WSAEREFUSED"></span><span id="wsaerefused"></span>**WSAEREFUSED**
   

10112 (0x2780)
 



A database query failed because it was actively refused.


   

<span id="WSAHOST_NOT_FOUND"></span><span id="wsahost_not_found"></span>**WSAHOST\_NOT\_FOUND**
   

11001 (0x2AF9)
 



No such host is known.


   

<span id="WSATRY_AGAIN"></span><span id="wsatry_again"></span>**WSATRY\_AGAIN**
   

11002 (0x2AFA)
 



This is usually a temporary error during hostname resolution and means that the local server did not receive a response from an authoritative server.


   

<span id="WSANO_RECOVERY"></span><span id="wsano_recovery"></span>**WSANO\_RECOVERY**
   

11003 (0x2AFB)
 



A non-recoverable error occurred during a database lookup.


   

<span id="WSANO_DATA"></span><span id="wsano_data"></span>**WSANO\_DATA**
   

11004 (0x2AFC)
 



The requested name is valid, but no data of the requested type was found.


   

<span id="WSA_QOS_RECEIVERS"></span><span id="wsa_qos_receivers"></span>**WSA\_QOS\_RECEIVERS**
   

11005 (0x2AFD)
 



At least one reserve has arrived.


   

<span id="WSA_QOS_SENDERS"></span><span id="wsa_qos_senders"></span>**WSA\_QOS\_SENDERS**
   

11006 (0x2AFE)
 



At least one path has arrived.


   

<span id="WSA_QOS_NO_SENDERS"></span><span id="wsa_qos_no_senders"></span>**WSA\_QOS\_NO\_SENDERS**
   

11007 (0x2AFF)
 



There are no senders.


   

<span id="WSA_QOS_NO_RECEIVERS"></span><span id="wsa_qos_no_receivers"></span>**WSA\_QOS\_NO\_RECEIVERS**
   

11008 (0x2B00)
 



There are no receivers.


   

<span id="WSA_QOS_REQUEST_CONFIRMED"></span><span id="wsa_qos_request_confirmed"></span>**WSA\_QOS\_REQUEST\_CONFIRMED**
   

11009 (0x2B01)
 



Reserve has been confirmed.


   

<span id="WSA_QOS_ADMISSION_FAILURE"></span><span id="wsa_qos_admission_failure"></span>**WSA\_QOS\_ADMISSION\_FAILURE**
   

11010 (0x2B02)
 



Error due to lack of resources.


   

<span id="WSA_QOS_POLICY_FAILURE"></span><span id="wsa_qos_policy_failure"></span>**WSA\_QOS\_POLICY\_FAILURE**
   

11011 (0x2B03)
 



Rejected for administrative reasons - bad credentials.


   

<span id="WSA_QOS_BAD_STYLE"></span><span id="wsa_qos_bad_style"></span>**WSA\_QOS\_BAD\_STYLE**
   

11012 (0x2B04)
 



Unknown or conflicting style.


   

<span id="WSA_QOS_BAD_OBJECT"></span><span id="wsa_qos_bad_object"></span>**WSA\_QOS\_BAD\_OBJECT**
   

11013 (0x2B05)
 



Problem with some part of the filterspec or providerspecific buffer in general.


   

<span id="WSA_QOS_TRAFFIC_CTRL_ERROR"></span><span id="wsa_qos_traffic_ctrl_error"></span>**WSA\_QOS\_TRAFFIC\_CTRL\_ERROR**
   

11014 (0x2B06)
 



Problem with some part of the flowspec.


   

<span id="WSA_QOS_GENERIC_ERROR"></span><span id="wsa_qos_generic_error"></span>**WSA\_QOS\_GENERIC\_ERROR**
   

11015 (0x2B07)
 



General QOS error.


   

<span id="WSA_QOS_ESERVICETYPE"></span><span id="wsa_qos_eservicetype"></span>**WSA\_QOS\_ESERVICETYPE**
   

11016 (0x2B08)
 



An invalid or unrecognized service type was found in the flowspec.


   

<span id="WSA_QOS_EFLOWSPEC"></span><span id="wsa_qos_eflowspec"></span>**WSA\_QOS\_EFLOWSPEC**
   

11017 (0x2B09)
 



An invalid or inconsistent flowspec was found in the QOS structure.


   

<span id="WSA_QOS_EPROVSPECBUF"></span><span id="wsa_qos_eprovspecbuf"></span>**WSA\_QOS\_EPROVSPECBUF**
   

11018 (0x2B0A)
 



Invalid QOS provider-specific buffer.


   

<span id="WSA_QOS_EFILTERSTYLE"></span><span id="wsa_qos_efilterstyle"></span>**WSA\_QOS\_EFILTERSTYLE**
   

11019 (0x2B0B)
 



An invalid QOS filter style was used.


   

<span id="WSA_QOS_EFILTERTYPE"></span><span id="wsa_qos_efiltertype"></span>**WSA\_QOS\_EFILTERTYPE**
   

11020 (0x2B0C)
 



An invalid QOS filter type was used.


   

<span id="WSA_QOS_EFILTERCOUNT"></span><span id="wsa_qos_efiltercount"></span>**WSA\_QOS\_EFILTERCOUNT**
   

11021 (0x2B0D)
 



An incorrect number of QOS FILTERSPECs were specified in the FLOWDESCRIPTOR.


   

<span id="WSA_QOS_EOBJLENGTH"></span><span id="wsa_qos_eobjlength"></span>**WSA\_QOS\_EOBJLENGTH**
   

11022 (0x2B0E)
 



An object with an invalid ObjectLength field was specified in the QOS provider-specific buffer.


   

<span id="WSA_QOS_EFLOWCOUNT"></span><span id="wsa_qos_eflowcount"></span>**WSA\_QOS\_EFLOWCOUNT**
   

11023 (0x2B0F)
 



An incorrect number of flow descriptors was specified in the QOS structure.


   

<span id="WSA_QOS_EUNKOWNPSOBJ"></span><span id="wsa_qos_eunkownpsobj"></span>**WSA\_QOS\_EUNKOWNPSOBJ**
   

11024 (0x2B10)
 



An unrecognized object was found in the QOS provider-specific buffer.


   

<span id="WSA_QOS_EPOLICYOBJ"></span><span id="wsa_qos_epolicyobj"></span>**WSA\_QOS\_EPOLICYOBJ**
   

11025 (0x2B11)
 



An invalid policy object was found in the QOS provider-specific buffer.


   

<span id="WSA_QOS_EFLOWDESC"></span><span id="wsa_qos_eflowdesc"></span>**WSA\_QOS\_EFLOWDESC**
   

11026 (0x2B12)
 



An invalid QOS flow descriptor was found in the flow descriptor list.


   

<span id="WSA_QOS_EPSFLOWSPEC"></span><span id="wsa_qos_epsflowspec"></span>**WSA\_QOS\_EPSFLOWSPEC**
   

11027 (0x2B13)
 



An invalid or inconsistent flowspec was found in the QOS provider specific buffer.


   

<span id="WSA_QOS_EPSFILTERSPEC"></span><span id="wsa_qos_epsfilterspec"></span>**WSA\_QOS\_EPSFILTERSPEC**
   

11028 (0x2B14)
 



An invalid FILTERSPEC was found in the QOS provider-specific buffer.


   

<span id="WSA_QOS_ESDMODEOBJ"></span><span id="wsa_qos_esdmodeobj"></span>**WSA\_QOS\_ESDMODEOBJ**
   

11029 (0x2B15)
 



An invalid shape discard mode object was found in the QOS provider specific buffer.


   

<span id="WSA_QOS_ESHAPERATEOBJ"></span><span id="wsa_qos_eshaperateobj"></span>**WSA\_QOS\_ESHAPERATEOBJ**
   

11030 (0x2B16)
 



An invalid shaping rate object was found in the QOS provider-specific buffer.


   

<span id="WSA_QOS_RESERVED_PETYPE"></span><span id="wsa_qos_reserved_petype"></span>**WSA\_QOS\_RESERVED\_PETYPE**
   

11031 (0x2B17)
 



A reserved policy element was found in the QOS provider-specific buffer.


   

<span id="WSA_SECURE_HOST_NOT_FOUND"></span><span id="wsa_secure_host_not_found"></span>**WSA\_SECURE\_HOST\_NOT\_FOUND**
   

11032 (0x2B18)
 



No such host is known securely.


   

<span id="WSA_IPSEC_NAME_POLICY_ERROR"></span><span id="wsa_ipsec_name_policy_error"></span>**WSA\_IPSEC\_NAME\_POLICY\_ERROR**
   

11033 (0x2B19)
 



Name based IPSEC policy could not be added.


   


## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   |  WinError.h  |



## See also

 

[System Error Codes](system-error-codes.md)
 

 

 




