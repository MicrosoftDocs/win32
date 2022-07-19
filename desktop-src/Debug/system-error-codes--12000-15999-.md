---
description: Describes error codes 12000-1599 defined in the WinError.h header file and is intended for developers.
ms.assetid: bb3c658d-96db-495a-a0dc-e93949c3835d
title: System Error Codes (12000-15999) (WinError.h)
ms.topic: reference
ms.date: 07/18/2019
---

# System Error Codes (12000-15999)

> [!NOTE]
> This information is intended for developers debugging system errors. For other errors, such as issues with Windows Update, there is a list of resources on the [Error codes](system-error-codes.md) page.

The following list describes [system error codes](system-error-codes.md) (errors 12000 to 15999). They are returned by the [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) function when many functions fail. To retrieve the description text for the error in your application, use the [**FormatMessage**](/windows/desktop/api/WinBase/nf-winbase-formatmessage) function with the **FORMAT\_MESSAGE\_FROM\_SYSTEM** flag.

<dl> <dt>

<span id="ERROR_INTERNET__"></span><span id="error_internet__"></span>**ERROR\_INTERNET\_\***
</dt> <dd> <dl> <dt>

12000 - 12175 (0x2EE0)
</dt> <dt>



See [Internet Error Codes](../wininet/wininet-errors.md) and WinInet.h.


</dt> </dl> </dd> <dt>

<span id="ERROR_WINHTTP__"></span><span id="error_winhttp__"></span>**ERROR\_WINHTTP\_\***
</dt> <dd> <dl> <dt>

12001 - 12184 (0x2EE1)
</dt> <dt>



See [WinHTTP Error Codes](../winhttp/error-messages.md) and Winhttp.h.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_QM_POLICY_EXISTS"></span><span id="error_ipsec_qm_policy_exists"></span>**ERROR\_IPSEC\_QM\_POLICY\_EXISTS**
</dt> <dd> <dl> <dt>

13000 (0x32C8)
</dt> <dt>



The specified quick mode policy already exists.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_QM_POLICY_NOT_FOUND"></span><span id="error_ipsec_qm_policy_not_found"></span>**ERROR\_IPSEC\_QM\_POLICY\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

13001 (0x32C9)
</dt> <dt>



The specified quick mode policy was not found.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_QM_POLICY_IN_USE"></span><span id="error_ipsec_qm_policy_in_use"></span>**ERROR\_IPSEC\_QM\_POLICY\_IN\_USE**
</dt> <dd> <dl> <dt>

13002 (0x32CA)
</dt> <dt>



The specified quick mode policy is being used.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_MM_POLICY_EXISTS"></span><span id="error_ipsec_mm_policy_exists"></span>**ERROR\_IPSEC\_MM\_POLICY\_EXISTS**
</dt> <dd> <dl> <dt>

13003 (0x32CB)
</dt> <dt>



The specified main mode policy already exists.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_MM_POLICY_NOT_FOUND"></span><span id="error_ipsec_mm_policy_not_found"></span>**ERROR\_IPSEC\_MM\_POLICY\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

13004 (0x32CC)
</dt> <dt>



The specified main mode policy was not found.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_MM_POLICY_IN_USE"></span><span id="error_ipsec_mm_policy_in_use"></span>**ERROR\_IPSEC\_MM\_POLICY\_IN\_USE**
</dt> <dd> <dl> <dt>

13005 (0x32CD)
</dt> <dt>



The specified main mode policy is being used.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_MM_FILTER_EXISTS"></span><span id="error_ipsec_mm_filter_exists"></span>**ERROR\_IPSEC\_MM\_FILTER\_EXISTS**
</dt> <dd> <dl> <dt>

13006 (0x32CE)
</dt> <dt>



The specified main mode filter already exists.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_MM_FILTER_NOT_FOUND"></span><span id="error_ipsec_mm_filter_not_found"></span>**ERROR\_IPSEC\_MM\_FILTER\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

13007 (0x32CF)
</dt> <dt>



The specified main mode filter was not found.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_TRANSPORT_FILTER_EXISTS"></span><span id="error_ipsec_transport_filter_exists"></span>**ERROR\_IPSEC\_TRANSPORT\_FILTER\_EXISTS**
</dt> <dd> <dl> <dt>

13008 (0x32D0)
</dt> <dt>



The specified transport mode filter already exists.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_TRANSPORT_FILTER_NOT_FOUND"></span><span id="error_ipsec_transport_filter_not_found"></span>**ERROR\_IPSEC\_TRANSPORT\_FILTER\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

13009 (0x32D1)
</dt> <dt>



The specified transport mode filter does not exist.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_MM_AUTH_EXISTS"></span><span id="error_ipsec_mm_auth_exists"></span>**ERROR\_IPSEC\_MM\_AUTH\_EXISTS**
</dt> <dd> <dl> <dt>

13010 (0x32D2)
</dt> <dt>



The specified main mode authentication list exists.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_MM_AUTH_NOT_FOUND"></span><span id="error_ipsec_mm_auth_not_found"></span>**ERROR\_IPSEC\_MM\_AUTH\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

13011 (0x32D3)
</dt> <dt>



The specified main mode authentication list was not found.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_MM_AUTH_IN_USE"></span><span id="error_ipsec_mm_auth_in_use"></span>**ERROR\_IPSEC\_MM\_AUTH\_IN\_USE**
</dt> <dd> <dl> <dt>

13012 (0x32D4)
</dt> <dt>



The specified main mode authentication list is being used.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_DEFAULT_MM_POLICY_NOT_FOUND"></span><span id="error_ipsec_default_mm_policy_not_found"></span>**ERROR\_IPSEC\_DEFAULT\_MM\_POLICY\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

13013 (0x32D5)
</dt> <dt>



The specified default main mode policy was not found.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_DEFAULT_MM_AUTH_NOT_FOUND"></span><span id="error_ipsec_default_mm_auth_not_found"></span>**ERROR\_IPSEC\_DEFAULT\_MM\_AUTH\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

13014 (0x32D6)
</dt> <dt>



The specified default main mode authentication list was not found.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_DEFAULT_QM_POLICY_NOT_FOUND"></span><span id="error_ipsec_default_qm_policy_not_found"></span>**ERROR\_IPSEC\_DEFAULT\_QM\_POLICY\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

13015 (0x32D7)
</dt> <dt>



The specified default quick mode policy was not found.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_TUNNEL_FILTER_EXISTS"></span><span id="error_ipsec_tunnel_filter_exists"></span>**ERROR\_IPSEC\_TUNNEL\_FILTER\_EXISTS**
</dt> <dd> <dl> <dt>

13016 (0x32D8)
</dt> <dt>



The specified tunnel mode filter exists.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_TUNNEL_FILTER_NOT_FOUND"></span><span id="error_ipsec_tunnel_filter_not_found"></span>**ERROR\_IPSEC\_TUNNEL\_FILTER\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

13017 (0x32D9)
</dt> <dt>



The specified tunnel mode filter was not found.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_MM_FILTER_PENDING_DELETION"></span><span id="error_ipsec_mm_filter_pending_deletion"></span>**ERROR\_IPSEC\_MM\_FILTER\_PENDING\_DELETION**
</dt> <dd> <dl> <dt>

13018 (0x32DA)
</dt> <dt>



The Main Mode filter is pending deletion.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_TRANSPORT_FILTER_PENDING_DELETION"></span><span id="error_ipsec_transport_filter_pending_deletion"></span>**ERROR\_IPSEC\_TRANSPORT\_FILTER\_PENDING\_DELETION**
</dt> <dd> <dl> <dt>

13019 (0x32DB)
</dt> <dt>



The transport filter is pending deletion.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_TUNNEL_FILTER_PENDING_DELETION"></span><span id="error_ipsec_tunnel_filter_pending_deletion"></span>**ERROR\_IPSEC\_TUNNEL\_FILTER\_PENDING\_DELETION**
</dt> <dd> <dl> <dt>

13020 (0x32DC)
</dt> <dt>



The tunnel filter is pending deletion.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_MM_POLICY_PENDING_DELETION"></span><span id="error_ipsec_mm_policy_pending_deletion"></span>**ERROR\_IPSEC\_MM\_POLICY\_PENDING\_DELETION**
</dt> <dd> <dl> <dt>

13021 (0x32DD)
</dt> <dt>



The Main Mode policy is pending deletion.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_MM_AUTH_PENDING_DELETION"></span><span id="error_ipsec_mm_auth_pending_deletion"></span>**ERROR\_IPSEC\_MM\_AUTH\_PENDING\_DELETION**
</dt> <dd> <dl> <dt>

13022 (0x32DE)
</dt> <dt>



The Main Mode authentication bundle is pending deletion.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_QM_POLICY_PENDING_DELETION"></span><span id="error_ipsec_qm_policy_pending_deletion"></span>**ERROR\_IPSEC\_QM\_POLICY\_PENDING\_DELETION**
</dt> <dd> <dl> <dt>

13023 (0x32DF)
</dt> <dt>



The Quick Mode policy is pending deletion.


</dt> </dl> </dd> <dt>

<span id="WARNING_IPSEC_MM_POLICY_PRUNED"></span><span id="warning_ipsec_mm_policy_pruned"></span>**WARNING\_IPSEC\_MM\_POLICY\_PRUNED**
</dt> <dd> <dl> <dt>

13024 (0x32E0)
</dt> <dt>



The Main Mode policy was successfully added, but some of the requested offers are not supported.


</dt> </dl> </dd> <dt>

<span id="WARNING_IPSEC_QM_POLICY_PRUNED"></span><span id="warning_ipsec_qm_policy_pruned"></span>**WARNING\_IPSEC\_QM\_POLICY\_PRUNED**
</dt> <dd> <dl> <dt>

13025 (0x32E1)
</dt> <dt>



The Quick Mode policy was successfully added, but some of the requested offers are not supported.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_NEG_STATUS_BEGIN"></span><span id="error_ipsec_ike_neg_status_begin"></span>**ERROR\_IPSEC\_IKE\_NEG\_STATUS\_BEGIN**
</dt> <dd> <dl> <dt>

13800 (0x35E8)
</dt> <dt>



ERROR\_IPSEC\_IKE\_NEG\_STATUS\_BEGIN


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_AUTH_FAIL"></span><span id="error_ipsec_ike_auth_fail"></span>**ERROR\_IPSEC\_IKE\_AUTH\_FAIL**
</dt> <dd> <dl> <dt>

13801 (0x35E9)
</dt> <dt>



IKE authentication credentials are unacceptable.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_ATTRIB_FAIL"></span><span id="error_ipsec_ike_attrib_fail"></span>**ERROR\_IPSEC\_IKE\_ATTRIB\_FAIL**
</dt> <dd> <dl> <dt>

13802 (0x35EA)
</dt> <dt>



IKE security attributes are unacceptable.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_NEGOTIATION_PENDING"></span><span id="error_ipsec_ike_negotiation_pending"></span>**ERROR\_IPSEC\_IKE\_NEGOTIATION\_PENDING**
</dt> <dd> <dl> <dt>

13803 (0x35EB)
</dt> <dt>



IKE Negotiation in progress.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_GENERAL_PROCESSING_ERROR"></span><span id="error_ipsec_ike_general_processing_error"></span>**ERROR\_IPSEC\_IKE\_GENERAL\_PROCESSING\_ERROR**
</dt> <dd> <dl> <dt>

13804 (0x35EC)
</dt> <dt>



General processing error.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_TIMED_OUT"></span><span id="error_ipsec_ike_timed_out"></span>**ERROR\_IPSEC\_IKE\_TIMED\_OUT**
</dt> <dd> <dl> <dt>

13805 (0x35ED)
</dt> <dt>



Negotiation timed out.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_NO_CERT"></span><span id="error_ipsec_ike_no_cert"></span>**ERROR\_IPSEC\_IKE\_NO\_CERT**
</dt> <dd> <dl> <dt>

13806 (0x35EE)
</dt> <dt>



IKE failed to find valid machine certificate. Contact your Network Security Administrator about installing a valid certificate in the appropriate Certificate Store.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_SA_DELETED"></span><span id="error_ipsec_ike_sa_deleted"></span>**ERROR\_IPSEC\_IKE\_SA\_DELETED**
</dt> <dd> <dl> <dt>

13807 (0x35EF)
</dt> <dt>



IKE SA deleted by peer before establishment completed.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_SA_REAPED"></span><span id="error_ipsec_ike_sa_reaped"></span>**ERROR\_IPSEC\_IKE\_SA\_REAPED**
</dt> <dd> <dl> <dt>

13808 (0x35F0)
</dt> <dt>



IKE SA deleted before establishment completed.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_MM_ACQUIRE_DROP"></span><span id="error_ipsec_ike_mm_acquire_drop"></span>**ERROR\_IPSEC\_IKE\_MM\_ACQUIRE\_DROP**
</dt> <dd> <dl> <dt>

13809 (0x35F1)
</dt> <dt>



Negotiation request sat in Queue too long.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_QM_ACQUIRE_DROP"></span><span id="error_ipsec_ike_qm_acquire_drop"></span>**ERROR\_IPSEC\_IKE\_QM\_ACQUIRE\_DROP**
</dt> <dd> <dl> <dt>

13810 (0x35F2)
</dt> <dt>



Negotiation request sat in Queue too long.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_QUEUE_DROP_MM"></span><span id="error_ipsec_ike_queue_drop_mm"></span>**ERROR\_IPSEC\_IKE\_QUEUE\_DROP\_MM**
</dt> <dd> <dl> <dt>

13811 (0x35F3)
</dt> <dt>



Negotiation request sat in Queue too long.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_QUEUE_DROP_NO_MM"></span><span id="error_ipsec_ike_queue_drop_no_mm"></span>**ERROR\_IPSEC\_IKE\_QUEUE\_DROP\_NO\_MM**
</dt> <dd> <dl> <dt>

13812 (0x35F4)
</dt> <dt>



Negotiation request sat in Queue too long.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_DROP_NO_RESPONSE"></span><span id="error_ipsec_ike_drop_no_response"></span>**ERROR\_IPSEC\_IKE\_DROP\_NO\_RESPONSE**
</dt> <dd> <dl> <dt>

13813 (0x35F5)
</dt> <dt>



No response from peer.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_MM_DELAY_DROP"></span><span id="error_ipsec_ike_mm_delay_drop"></span>**ERROR\_IPSEC\_IKE\_MM\_DELAY\_DROP**
</dt> <dd> <dl> <dt>

13814 (0x35F6)
</dt> <dt>



Negotiation took too long.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_QM_DELAY_DROP"></span><span id="error_ipsec_ike_qm_delay_drop"></span>**ERROR\_IPSEC\_IKE\_QM\_DELAY\_DROP**
</dt> <dd> <dl> <dt>

13815 (0x35F7)
</dt> <dt>



Negotiation took too long.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_ERROR"></span><span id="error_ipsec_ike_error"></span>**ERROR\_IPSEC\_IKE\_ERROR**
</dt> <dd> <dl> <dt>

13816 (0x35F8)
</dt> <dt>



Unknown error occurred.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_CRL_FAILED"></span><span id="error_ipsec_ike_crl_failed"></span>**ERROR\_IPSEC\_IKE\_CRL\_FAILED**
</dt> <dd> <dl> <dt>

13817 (0x35F9)
</dt> <dt>



Certificate Revocation Check failed.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_INVALID_KEY_USAGE"></span><span id="error_ipsec_ike_invalid_key_usage"></span>**ERROR\_IPSEC\_IKE\_INVALID\_KEY\_USAGE**
</dt> <dd> <dl> <dt>

13818 (0x35FA)
</dt> <dt>



Invalid certificate key usage.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_INVALID_CERT_TYPE"></span><span id="error_ipsec_ike_invalid_cert_type"></span>**ERROR\_IPSEC\_IKE\_INVALID\_CERT\_TYPE**
</dt> <dd> <dl> <dt>

13819 (0x35FB)
</dt> <dt>



Invalid certificate type.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_NO_PRIVATE_KEY"></span><span id="error_ipsec_ike_no_private_key"></span>**ERROR\_IPSEC\_IKE\_NO\_PRIVATE\_KEY**
</dt> <dd> <dl> <dt>

13820 (0x35FC)
</dt> <dt>



IKE negotiation failed because the machine certificate used does not have a private key. IPsec certificates require a private key. Contact your Network Security administrator about replacing with a certificate that has a private key.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_SIMULTANEOUS_REKEY"></span><span id="error_ipsec_ike_simultaneous_rekey"></span>**ERROR\_IPSEC\_IKE\_SIMULTANEOUS\_REKEY**
</dt> <dd> <dl> <dt>

13821 (0x35FD)
</dt> <dt>



Simultaneous rekeys were detected.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_DH_FAIL"></span><span id="error_ipsec_ike_dh_fail"></span>**ERROR\_IPSEC\_IKE\_DH\_FAIL**
</dt> <dd> <dl> <dt>

13822 (0x35FE)
</dt> <dt>



Failure in Diffie-Hellman computation.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_CRITICAL_PAYLOAD_NOT_RECOGNIZED"></span><span id="error_ipsec_ike_critical_payload_not_recognized"></span>**ERROR\_IPSEC\_IKE\_CRITICAL\_PAYLOAD\_NOT\_RECOGNIZED**
</dt> <dd> <dl> <dt>

13823 (0x35FF)
</dt> <dt>



Don't know how to process critical payload.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_INVALID_HEADER"></span><span id="error_ipsec_ike_invalid_header"></span>**ERROR\_IPSEC\_IKE\_INVALID\_HEADER**
</dt> <dd> <dl> <dt>

13824 (0x3600)
</dt> <dt>



Invalid header.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_NO_POLICY"></span><span id="error_ipsec_ike_no_policy"></span>**ERROR\_IPSEC\_IKE\_NO\_POLICY**
</dt> <dd> <dl> <dt>

13825 (0x3601)
</dt> <dt>



No policy configured.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_INVALID_SIGNATURE"></span><span id="error_ipsec_ike_invalid_signature"></span>**ERROR\_IPSEC\_IKE\_INVALID\_SIGNATURE**
</dt> <dd> <dl> <dt>

13826 (0x3602)
</dt> <dt>



Failed to verify signature.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_KERBEROS_ERROR"></span><span id="error_ipsec_ike_kerberos_error"></span>**ERROR\_IPSEC\_IKE\_KERBEROS\_ERROR**
</dt> <dd> <dl> <dt>

13827 (0x3603)
</dt> <dt>



Failed to authenticate using Kerberos.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_NO_PUBLIC_KEY"></span><span id="error_ipsec_ike_no_public_key"></span>**ERROR\_IPSEC\_IKE\_NO\_PUBLIC\_KEY**
</dt> <dd> <dl> <dt>

13828 (0x3604)
</dt> <dt>



Peer's certificate did not have a public key.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_PROCESS_ERR"></span><span id="error_ipsec_ike_process_err"></span>**ERROR\_IPSEC\_IKE\_PROCESS\_ERR**
</dt> <dd> <dl> <dt>

13829 (0x3605)
</dt> <dt>



Error processing error payload.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_PROCESS_ERR_SA"></span><span id="error_ipsec_ike_process_err_sa"></span>**ERROR\_IPSEC\_IKE\_PROCESS\_ERR\_SA**
</dt> <dd> <dl> <dt>

13830 (0x3606)
</dt> <dt>



Error processing SA payload.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_PROCESS_ERR_PROP"></span><span id="error_ipsec_ike_process_err_prop"></span>**ERROR\_IPSEC\_IKE\_PROCESS\_ERR\_PROP**
</dt> <dd> <dl> <dt>

13831 (0x3607)
</dt> <dt>



Error processing Proposal payload.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_PROCESS_ERR_TRANS"></span><span id="error_ipsec_ike_process_err_trans"></span>**ERROR\_IPSEC\_IKE\_PROCESS\_ERR\_TRANS**
</dt> <dd> <dl> <dt>

13832 (0x3608)
</dt> <dt>



Error processing Transform payload.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_PROCESS_ERR_KE"></span><span id="error_ipsec_ike_process_err_ke"></span>**ERROR\_IPSEC\_IKE\_PROCESS\_ERR\_KE**
</dt> <dd> <dl> <dt>

13833 (0x3609)
</dt> <dt>



Error processing KE payload.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_PROCESS_ERR_ID"></span><span id="error_ipsec_ike_process_err_id"></span>**ERROR\_IPSEC\_IKE\_PROCESS\_ERR\_ID**
</dt> <dd> <dl> <dt>

13834 (0x360A)
</dt> <dt>



Error processing ID payload.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_PROCESS_ERR_CERT"></span><span id="error_ipsec_ike_process_err_cert"></span>**ERROR\_IPSEC\_IKE\_PROCESS\_ERR\_CERT**
</dt> <dd> <dl> <dt>

13835 (0x360B)
</dt> <dt>



Error processing Cert payload.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_PROCESS_ERR_CERT_REQ"></span><span id="error_ipsec_ike_process_err_cert_req"></span>**ERROR\_IPSEC\_IKE\_PROCESS\_ERR\_CERT\_REQ**
</dt> <dd> <dl> <dt>

13836 (0x360C)
</dt> <dt>



Error processing Certificate Request payload.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_PROCESS_ERR_HASH"></span><span id="error_ipsec_ike_process_err_hash"></span>**ERROR\_IPSEC\_IKE\_PROCESS\_ERR\_HASH**
</dt> <dd> <dl> <dt>

13837 (0x360D)
</dt> <dt>



Error processing Hash payload.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_PROCESS_ERR_SIG"></span><span id="error_ipsec_ike_process_err_sig"></span>**ERROR\_IPSEC\_IKE\_PROCESS\_ERR\_SIG**
</dt> <dd> <dl> <dt>

13838 (0x360E)
</dt> <dt>



Error processing Signature payload.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_PROCESS_ERR_NONCE"></span><span id="error_ipsec_ike_process_err_nonce"></span>**ERROR\_IPSEC\_IKE\_PROCESS\_ERR\_NONCE**
</dt> <dd> <dl> <dt>

13839 (0x360F)
</dt> <dt>



Error processing Nonce payload.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_PROCESS_ERR_NOTIFY"></span><span id="error_ipsec_ike_process_err_notify"></span>**ERROR\_IPSEC\_IKE\_PROCESS\_ERR\_NOTIFY**
</dt> <dd> <dl> <dt>

13840 (0x3610)
</dt> <dt>



Error processing Notify payload.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_PROCESS_ERR_DELETE"></span><span id="error_ipsec_ike_process_err_delete"></span>**ERROR\_IPSEC\_IKE\_PROCESS\_ERR\_DELETE**
</dt> <dd> <dl> <dt>

13841 (0x3611)
</dt> <dt>



Error processing Delete Payload.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_PROCESS_ERR_VENDOR"></span><span id="error_ipsec_ike_process_err_vendor"></span>**ERROR\_IPSEC\_IKE\_PROCESS\_ERR\_VENDOR**
</dt> <dd> <dl> <dt>

13842 (0x3612)
</dt> <dt>



Error processing VendorId payload.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_INVALID_PAYLOAD"></span><span id="error_ipsec_ike_invalid_payload"></span>**ERROR\_IPSEC\_IKE\_INVALID\_PAYLOAD**
</dt> <dd> <dl> <dt>

13843 (0x3613)
</dt> <dt>



Invalid payload received.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_LOAD_SOFT_SA"></span><span id="error_ipsec_ike_load_soft_sa"></span>**ERROR\_IPSEC\_IKE\_LOAD\_SOFT\_SA**
</dt> <dd> <dl> <dt>

13844 (0x3614)
</dt> <dt>



Soft SA loaded.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_SOFT_SA_TORN_DOWN"></span><span id="error_ipsec_ike_soft_sa_torn_down"></span>**ERROR\_IPSEC\_IKE\_SOFT\_SA\_TORN\_DOWN**
</dt> <dd> <dl> <dt>

13845 (0x3615)
</dt> <dt>



Soft SA torn down.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_INVALID_COOKIE"></span><span id="error_ipsec_ike_invalid_cookie"></span>**ERROR\_IPSEC\_IKE\_INVALID\_COOKIE**
</dt> <dd> <dl> <dt>

13846 (0x3616)
</dt> <dt>



Invalid cookie received.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_NO_PEER_CERT"></span><span id="error_ipsec_ike_no_peer_cert"></span>**ERROR\_IPSEC\_IKE\_NO\_PEER\_CERT**
</dt> <dd> <dl> <dt>

13847 (0x3617)
</dt> <dt>



Peer failed to send valid machine certificate.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_PEER_CRL_FAILED"></span><span id="error_ipsec_ike_peer_crl_failed"></span>**ERROR\_IPSEC\_IKE\_PEER\_CRL\_FAILED**
</dt> <dd> <dl> <dt>

13848 (0x3618)
</dt> <dt>



Certification Revocation check of peer's certificate failed.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_POLICY_CHANGE"></span><span id="error_ipsec_ike_policy_change"></span>**ERROR\_IPSEC\_IKE\_POLICY\_CHANGE**
</dt> <dd> <dl> <dt>

13849 (0x3619)
</dt> <dt>



New policy invalidated SAs formed with old policy.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_NO_MM_POLICY"></span><span id="error_ipsec_ike_no_mm_policy"></span>**ERROR\_IPSEC\_IKE\_NO\_MM\_POLICY**
</dt> <dd> <dl> <dt>

13850 (0x361A)
</dt> <dt>



There is no available Main Mode IKE policy.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_NOTCBPRIV"></span><span id="error_ipsec_ike_notcbpriv"></span>**ERROR\_IPSEC\_IKE\_NOTCBPRIV**
</dt> <dd> <dl> <dt>

13851 (0x361B)
</dt> <dt>



Failed to enabled TCB privilege.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_SECLOADFAIL"></span><span id="error_ipsec_ike_secloadfail"></span>**ERROR\_IPSEC\_IKE\_SECLOADFAIL**
</dt> <dd> <dl> <dt>

13852 (0x361C)
</dt> <dt>



Failed to load SECURITY.DLL.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_FAILSSPINIT"></span><span id="error_ipsec_ike_failsspinit"></span>**ERROR\_IPSEC\_IKE\_FAILSSPINIT**
</dt> <dd> <dl> <dt>

13853 (0x361D)
</dt> <dt>



Failed to obtain security function table dispatch address from SSPI.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_FAILQUERYSSP"></span><span id="error_ipsec_ike_failqueryssp"></span>**ERROR\_IPSEC\_IKE\_FAILQUERYSSP**
</dt> <dd> <dl> <dt>

13854 (0x361E)
</dt> <dt>



Failed to query Kerberos package to obtain max token size.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_SRVACQFAIL"></span><span id="error_ipsec_ike_srvacqfail"></span>**ERROR\_IPSEC\_IKE\_SRVACQFAIL**
</dt> <dd> <dl> <dt>

13855 (0x361F)
</dt> <dt>



Failed to obtain Kerberos server credentials for ISAKMP/ERROR\_IPSEC\_IKE service. Kerberos authentication will not function. The most likely reason for this is lack of domain membership. This is normal if your computer is a member of a workgroup.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_SRVQUERYCRED"></span><span id="error_ipsec_ike_srvquerycred"></span>**ERROR\_IPSEC\_IKE\_SRVQUERYCRED**
</dt> <dd> <dl> <dt>

13856 (0x3620)
</dt> <dt>



Failed to determine SSPI principal name for ISAKMP/ERROR\_IPSEC\_IKE service ([**QueryCredentialsAttributes**](/windows/win32/api/sspi/nf-sspi-querycredentialsattributesa)).


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_GETSPIFAIL"></span><span id="error_ipsec_ike_getspifail"></span>**ERROR\_IPSEC\_IKE\_GETSPIFAIL**
</dt> <dd> <dl> <dt>

13857 (0x3621)
</dt> <dt>



Failed to obtain new SPI for the inbound SA from IPsec driver. The most common cause for this is that the driver does not have the correct filter. Check your policy to verify the filters.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_INVALID_FILTER"></span><span id="error_ipsec_ike_invalid_filter"></span>**ERROR\_IPSEC\_IKE\_INVALID\_FILTER**
</dt> <dd> <dl> <dt>

13858 (0x3622)
</dt> <dt>



Given filter is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_OUT_OF_MEMORY"></span><span id="error_ipsec_ike_out_of_memory"></span>**ERROR\_IPSEC\_IKE\_OUT\_OF\_MEMORY**
</dt> <dd> <dl> <dt>

13859 (0x3623)
</dt> <dt>



Memory allocation failed.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_ADD_UPDATE_KEY_FAILED"></span><span id="error_ipsec_ike_add_update_key_failed"></span>**ERROR\_IPSEC\_IKE\_ADD\_UPDATE\_KEY\_FAILED**
</dt> <dd> <dl> <dt>

13860 (0x3624)
</dt> <dt>



Failed to add Security Association to IPsec Driver. The most common cause for this is if the IKE negotiation took too long to complete. If the problem persists, reduce the load on the faulting machine.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_INVALID_POLICY"></span><span id="error_ipsec_ike_invalid_policy"></span>**ERROR\_IPSEC\_IKE\_INVALID\_POLICY**
</dt> <dd> <dl> <dt>

13861 (0x3625)
</dt> <dt>



Invalid policy.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_UNKNOWN_DOI"></span><span id="error_ipsec_ike_unknown_doi"></span>**ERROR\_IPSEC\_IKE\_UNKNOWN\_DOI**
</dt> <dd> <dl> <dt>

13862 (0x3626)
</dt> <dt>



Invalid DOI.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_INVALID_SITUATION"></span><span id="error_ipsec_ike_invalid_situation"></span>**ERROR\_IPSEC\_IKE\_INVALID\_SITUATION**
</dt> <dd> <dl> <dt>

13863 (0x3627)
</dt> <dt>



Invalid situation.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_DH_FAILURE"></span><span id="error_ipsec_ike_dh_failure"></span>**ERROR\_IPSEC\_IKE\_DH\_FAILURE**
</dt> <dd> <dl> <dt>

13864 (0x3628)
</dt> <dt>



Diffie-Hellman failure.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_INVALID_GROUP"></span><span id="error_ipsec_ike_invalid_group"></span>**ERROR\_IPSEC\_IKE\_INVALID\_GROUP**
</dt> <dd> <dl> <dt>

13865 (0x3629)
</dt> <dt>



Invalid Diffie-Hellman group.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_ENCRYPT"></span><span id="error_ipsec_ike_encrypt"></span>**ERROR\_IPSEC\_IKE\_ENCRYPT**
</dt> <dd> <dl> <dt>

13866 (0x362A)
</dt> <dt>



Error encrypting payload.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_DECRYPT"></span><span id="error_ipsec_ike_decrypt"></span>**ERROR\_IPSEC\_IKE\_DECRYPT**
</dt> <dd> <dl> <dt>

13867 (0x362B)
</dt> <dt>



Error decrypting payload.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_POLICY_MATCH"></span><span id="error_ipsec_ike_policy_match"></span>**ERROR\_IPSEC\_IKE\_POLICY\_MATCH**
</dt> <dd> <dl> <dt>

13868 (0x362C)
</dt> <dt>



Policy match error.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_UNSUPPORTED_ID"></span><span id="error_ipsec_ike_unsupported_id"></span>**ERROR\_IPSEC\_IKE\_UNSUPPORTED\_ID**
</dt> <dd> <dl> <dt>

13869 (0x362D)
</dt> <dt>



Unsupported ID.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_INVALID_HASH"></span><span id="error_ipsec_ike_invalid_hash"></span>**ERROR\_IPSEC\_IKE\_INVALID\_HASH**
</dt> <dd> <dl> <dt>

13870 (0x362E)
</dt> <dt>



Hash verification failed.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_INVALID_HASH_ALG"></span><span id="error_ipsec_ike_invalid_hash_alg"></span>**ERROR\_IPSEC\_IKE\_INVALID\_HASH\_ALG**
</dt> <dd> <dl> <dt>

13871 (0x362F)
</dt> <dt>



Invalid hash algorithm.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_INVALID_HASH_SIZE"></span><span id="error_ipsec_ike_invalid_hash_size"></span>**ERROR\_IPSEC\_IKE\_INVALID\_HASH\_SIZE**
</dt> <dd> <dl> <dt>

13872 (0x3630)
</dt> <dt>



Invalid hash size.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_INVALID_ENCRYPT_ALG"></span><span id="error_ipsec_ike_invalid_encrypt_alg"></span>**ERROR\_IPSEC\_IKE\_INVALID\_ENCRYPT\_ALG**
</dt> <dd> <dl> <dt>

13873 (0x3631)
</dt> <dt>



Invalid encryption algorithm.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_INVALID_AUTH_ALG"></span><span id="error_ipsec_ike_invalid_auth_alg"></span>**ERROR\_IPSEC\_IKE\_INVALID\_AUTH\_ALG**
</dt> <dd> <dl> <dt>

13874 (0x3632)
</dt> <dt>



Invalid authentication algorithm.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_INVALID_SIG"></span><span id="error_ipsec_ike_invalid_sig"></span>**ERROR\_IPSEC\_IKE\_INVALID\_SIG**
</dt> <dd> <dl> <dt>

13875 (0x3633)
</dt> <dt>



Invalid certificate signature.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_LOAD_FAILED"></span><span id="error_ipsec_ike_load_failed"></span>**ERROR\_IPSEC\_IKE\_LOAD\_FAILED**
</dt> <dd> <dl> <dt>

13876 (0x3634)
</dt> <dt>



Load failed.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_RPC_DELETE"></span><span id="error_ipsec_ike_rpc_delete"></span>**ERROR\_IPSEC\_IKE\_RPC\_DELETE**
</dt> <dd> <dl> <dt>

13877 (0x3635)
</dt> <dt>



Deleted via RPC call.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_BENIGN_REINIT"></span><span id="error_ipsec_ike_benign_reinit"></span>**ERROR\_IPSEC\_IKE\_BENIGN\_REINIT**
</dt> <dd> <dl> <dt>

13878 (0x3636)
</dt> <dt>



Temporary state created to perform reinitialization. This is not a real failure.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_INVALID_RESPONDER_LIFETIME_NOTIFY"></span><span id="error_ipsec_ike_invalid_responder_lifetime_notify"></span>**ERROR\_IPSEC\_IKE\_INVALID\_RESPONDER\_LIFETIME\_NOTIFY**
</dt> <dd> <dl> <dt>

13879 (0x3637)
</dt> <dt>



The lifetime value received in the Responder Lifetime Notify is below the Windows 2000 configured minimum value. Please fix the policy on the peer machine.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_INVALID_MAJOR_VERSION"></span><span id="error_ipsec_ike_invalid_major_version"></span>**ERROR\_IPSEC\_IKE\_INVALID\_MAJOR\_VERSION**
</dt> <dd> <dl> <dt>

13880 (0x3638)
</dt> <dt>



The recipient cannot handle version of IKE specified in the header.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_INVALID_CERT_KEYLEN"></span><span id="error_ipsec_ike_invalid_cert_keylen"></span>**ERROR\_IPSEC\_IKE\_INVALID\_CERT\_KEYLEN**
</dt> <dd> <dl> <dt>

13881 (0x3639)
</dt> <dt>



Key length in certificate is too small for configured security requirements.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_MM_LIMIT"></span><span id="error_ipsec_ike_mm_limit"></span>**ERROR\_IPSEC\_IKE\_MM\_LIMIT**
</dt> <dd> <dl> <dt>

13882 (0x363A)
</dt> <dt>



Max number of established MM SAs to peer exceeded.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_NEGOTIATION_DISABLED"></span><span id="error_ipsec_ike_negotiation_disabled"></span>**ERROR\_IPSEC\_IKE\_NEGOTIATION\_DISABLED**
</dt> <dd> <dl> <dt>

13883 (0x363B)
</dt> <dt>



IKE received a policy that disables negotiation.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_QM_LIMIT"></span><span id="error_ipsec_ike_qm_limit"></span>**ERROR\_IPSEC\_IKE\_QM\_LIMIT**
</dt> <dd> <dl> <dt>

13884 (0x363C)
</dt> <dt>



Reached maximum quick mode limit for the main mode. New main mode will be started.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_MM_EXPIRED"></span><span id="error_ipsec_ike_mm_expired"></span>**ERROR\_IPSEC\_IKE\_MM\_EXPIRED**
</dt> <dd> <dl> <dt>

13885 (0x363D)
</dt> <dt>



Main mode SA lifetime expired or peer sent a main mode delete.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_PEER_MM_ASSUMED_INVALID"></span><span id="error_ipsec_ike_peer_mm_assumed_invalid"></span>**ERROR\_IPSEC\_IKE\_PEER\_MM\_ASSUMED\_INVALID**
</dt> <dd> <dl> <dt>

13886 (0x363E)
</dt> <dt>



Main mode SA assumed to be invalid because peer stopped responding.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_CERT_CHAIN_POLICY_MISMATCH"></span><span id="error_ipsec_ike_cert_chain_policy_mismatch"></span>**ERROR\_IPSEC\_IKE\_CERT\_CHAIN\_POLICY\_MISMATCH**
</dt> <dd> <dl> <dt>

13887 (0x363F)
</dt> <dt>



Certificate doesn't chain to a trusted root in IPsec policy.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_UNEXPECTED_MESSAGE_ID"></span><span id="error_ipsec_ike_unexpected_message_id"></span>**ERROR\_IPSEC\_IKE\_UNEXPECTED\_MESSAGE\_ID**
</dt> <dd> <dl> <dt>

13888 (0x3640)
</dt> <dt>



Received unexpected message ID.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_INVALID_AUTH_PAYLOAD"></span><span id="error_ipsec_ike_invalid_auth_payload"></span>**ERROR\_IPSEC\_IKE\_INVALID\_AUTH\_PAYLOAD**
</dt> <dd> <dl> <dt>

13889 (0x3641)
</dt> <dt>



Received invalid authentication offers.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_DOS_COOKIE_SENT"></span><span id="error_ipsec_ike_dos_cookie_sent"></span>**ERROR\_IPSEC\_IKE\_DOS\_COOKIE\_SENT**
</dt> <dd> <dl> <dt>

13890 (0x3642)
</dt> <dt>



Sent DoS cookie notify to initiator.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_SHUTTING_DOWN"></span><span id="error_ipsec_ike_shutting_down"></span>**ERROR\_IPSEC\_IKE\_SHUTTING\_DOWN**
</dt> <dd> <dl> <dt>

13891 (0x3643)
</dt> <dt>



IKE service is shutting down.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_CGA_AUTH_FAILED"></span><span id="error_ipsec_ike_cga_auth_failed"></span>**ERROR\_IPSEC\_IKE\_CGA\_AUTH\_FAILED**
</dt> <dd> <dl> <dt>

13892 (0x3644)
</dt> <dt>



Could not verify binding between CGA address and certificate.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_PROCESS_ERR_NATOA"></span><span id="error_ipsec_ike_process_err_natoa"></span>**ERROR\_IPSEC\_IKE\_PROCESS\_ERR\_NATOA**
</dt> <dd> <dl> <dt>

13893 (0x3645)
</dt> <dt>



Error processing NatOA payload.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_INVALID_MM_FOR_QM"></span><span id="error_ipsec_ike_invalid_mm_for_qm"></span>**ERROR\_IPSEC\_IKE\_INVALID\_MM\_FOR\_QM**
</dt> <dd> <dl> <dt>

13894 (0x3646)
</dt> <dt>



Parameters of the main mode are invalid for this quick mode.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_QM_EXPIRED"></span><span id="error_ipsec_ike_qm_expired"></span>**ERROR\_IPSEC\_IKE\_QM\_EXPIRED**
</dt> <dd> <dl> <dt>

13895 (0x3647)
</dt> <dt>



Quick mode SA was expired by IPsec driver.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_TOO_MANY_FILTERS"></span><span id="error_ipsec_ike_too_many_filters"></span>**ERROR\_IPSEC\_IKE\_TOO\_MANY\_FILTERS**
</dt> <dd> <dl> <dt>

13896 (0x3648)
</dt> <dt>



Too many dynamically added IKEEXT filters were detected.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_NEG_STATUS_END"></span><span id="error_ipsec_ike_neg_status_end"></span>**ERROR\_IPSEC\_IKE\_NEG\_STATUS\_END**
</dt> <dd> <dl> <dt>

13897 (0x3649)
</dt> <dt>



ERROR\_IPSEC\_IKE\_NEG\_STATUS\_END


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_KILL_DUMMY_NAP_TUNNEL"></span><span id="error_ipsec_ike_kill_dummy_nap_tunnel"></span>**ERROR\_IPSEC\_IKE\_KILL\_DUMMY\_NAP\_TUNNEL**
</dt> <dd> <dl> <dt>

13898 (0x364A)
</dt> <dt>



NAP reauth succeeded and must delete the dummy NAP IKEv2 tunnel.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_INNER_IP_ASSIGNMENT_FAILURE"></span><span id="error_ipsec_ike_inner_ip_assignment_failure"></span>**ERROR\_IPSEC\_IKE\_INNER\_IP\_ASSIGNMENT\_FAILURE**
</dt> <dd> <dl> <dt>

13899 (0x364B)
</dt> <dt>



Error in assigning inner IP address to initiator in tunnel mode.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_REQUIRE_CP_PAYLOAD_MISSING"></span><span id="error_ipsec_ike_require_cp_payload_missing"></span>**ERROR\_IPSEC\_IKE\_REQUIRE\_CP\_PAYLOAD\_MISSING**
</dt> <dd> <dl> <dt>

13900 (0x364C)
</dt> <dt>



Require configuration payload missing.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_KEY_MODULE_IMPERSONATION_NEGOTIATION_PENDING"></span><span id="error_ipsec_key_module_impersonation_negotiation_pending"></span>**ERROR\_IPSEC\_KEY\_MODULE\_IMPERSONATION\_NEGOTIATION\_PENDING**
</dt> <dd> <dl> <dt>

13901 (0x364D)
</dt> <dt>



A negotiation running as the security principle who issued the connection is in progress.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_COEXISTENCE_SUPPRESS"></span><span id="error_ipsec_ike_coexistence_suppress"></span>**ERROR\_IPSEC\_IKE\_COEXISTENCE\_SUPPRESS**
</dt> <dd> <dl> <dt>

13902 (0x364E)
</dt> <dt>



SA was deleted due to IKEv1/AuthIP co-existence suppress check.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_RATELIMIT_DROP"></span><span id="error_ipsec_ike_ratelimit_drop"></span>**ERROR\_IPSEC\_IKE\_RATELIMIT\_DROP**
</dt> <dd> <dl> <dt>

13903 (0x364F)
</dt> <dt>



Incoming SA request was dropped due to peer IP address rate limiting.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_PEER_DOESNT_SUPPORT_MOBIKE"></span><span id="error_ipsec_ike_peer_doesnt_support_mobike"></span>**ERROR\_IPSEC\_IKE\_PEER\_DOESNT\_SUPPORT\_MOBIKE**
</dt> <dd> <dl> <dt>

13904 (0x3650)
</dt> <dt>



Peer does not support MOBIKE.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_AUTHORIZATION_FAILURE"></span><span id="error_ipsec_ike_authorization_failure"></span>**ERROR\_IPSEC\_IKE\_AUTHORIZATION\_FAILURE**
</dt> <dd> <dl> <dt>

13905 (0x3651)
</dt> <dt>



SA establishment is not authorized.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_STRONG_CRED_AUTHORIZATION_FAILURE"></span><span id="error_ipsec_ike_strong_cred_authorization_failure"></span>**ERROR\_IPSEC\_IKE\_STRONG\_CRED\_AUTHORIZATION\_FAILURE**
</dt> <dd> <dl> <dt>

13906 (0x3652)
</dt> <dt>



SA establishment is not authorized because there is not a sufficiently strong PKINIT-based credential.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_AUTHORIZATION_FAILURE_WITH_OPTIONAL_RETRY"></span><span id="error_ipsec_ike_authorization_failure_with_optional_retry"></span>**ERROR\_IPSEC\_IKE\_AUTHORIZATION\_FAILURE\_WITH\_OPTIONAL\_RETRY**
</dt> <dd> <dl> <dt>

13907 (0x3653)
</dt> <dt>



SA establishment is not authorized. You may need to enter updated or different credentials such as a smartcard.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_STRONG_CRED_AUTHORIZATION_AND_CERTMAP_FAILURE"></span><span id="error_ipsec_ike_strong_cred_authorization_and_certmap_failure"></span>**ERROR\_IPSEC\_IKE\_STRONG\_CRED\_AUTHORIZATION\_AND\_CERTMAP\_FAILURE**
</dt> <dd> <dl> <dt>

13908 (0x3654)
</dt> <dt>



SA establishment is not authorized because there is not a sufficiently strong PKINIT-based credential. This might be related to certificate-to-account mapping failure for the SA.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_IKE_NEG_STATUS_EXTENDED_END"></span><span id="error_ipsec_ike_neg_status_extended_end"></span>**ERROR\_IPSEC\_IKE\_NEG\_STATUS\_EXTENDED\_END**
</dt> <dd> <dl> <dt>

13909 (0x3655)
</dt> <dt>



ERROR\_IPSEC\_IKE\_NEG\_STATUS\_EXTENDED\_END


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_BAD_SPI"></span><span id="error_ipsec_bad_spi"></span>**ERROR\_IPSEC\_BAD\_SPI**
</dt> <dd> <dl> <dt>

13910 (0x3656)
</dt> <dt>



The SPI in the packet does not match a valid IPsec SA.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_SA_LIFETIME_EXPIRED"></span><span id="error_ipsec_sa_lifetime_expired"></span>**ERROR\_IPSEC\_SA\_LIFETIME\_EXPIRED**
</dt> <dd> <dl> <dt>

13911 (0x3657)
</dt> <dt>



Packet was received on an IPsec SA whose lifetime has expired.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_WRONG_SA"></span><span id="error_ipsec_wrong_sa"></span>**ERROR\_IPSEC\_WRONG\_SA**
</dt> <dd> <dl> <dt>

13912 (0x3658)
</dt> <dt>



Packet was received on an IPsec SA that does not match the packet characteristics.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_REPLAY_CHECK_FAILED"></span><span id="error_ipsec_replay_check_failed"></span>**ERROR\_IPSEC\_REPLAY\_CHECK\_FAILED**
</dt> <dd> <dl> <dt>

13913 (0x3659)
</dt> <dt>



Packet sequence number replay check failed.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_INVALID_PACKET"></span><span id="error_ipsec_invalid_packet"></span>**ERROR\_IPSEC\_INVALID\_PACKET**
</dt> <dd> <dl> <dt>

13914 (0x365A)
</dt> <dt>



IPsec header and/or trailer in the packet is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_INTEGRITY_CHECK_FAILED"></span><span id="error_ipsec_integrity_check_failed"></span>**ERROR\_IPSEC\_INTEGRITY\_CHECK\_FAILED**
</dt> <dd> <dl> <dt>

13915 (0x365B)
</dt> <dt>



IPsec integrity check failed.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_CLEAR_TEXT_DROP"></span><span id="error_ipsec_clear_text_drop"></span>**ERROR\_IPSEC\_CLEAR\_TEXT\_DROP**
</dt> <dd> <dl> <dt>

13916 (0x365C)
</dt> <dt>



IPsec dropped a clear text packet.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_AUTH_FIREWALL_DROP"></span><span id="error_ipsec_auth_firewall_drop"></span>**ERROR\_IPSEC\_AUTH\_FIREWALL\_DROP**
</dt> <dd> <dl> <dt>

13917 (0x365D)
</dt> <dt>



IPsec dropped an incoming ESP packet in authenticated firewall mode. This drop is benign.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_THROTTLE_DROP"></span><span id="error_ipsec_throttle_drop"></span>**ERROR\_IPSEC\_THROTTLE\_DROP**
</dt> <dd> <dl> <dt>

13918 (0x365E)
</dt> <dt>



IPsec dropped a packet due to DoS throttling.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_DOSP_BLOCK"></span><span id="error_ipsec_dosp_block"></span>**ERROR\_IPSEC\_DOSP\_BLOCK**
</dt> <dd> <dl> <dt>

13925 (0x3665)
</dt> <dt>



IPsec DoS Protection matched an explicit block rule.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_DOSP_RECEIVED_MULTICAST"></span><span id="error_ipsec_dosp_received_multicast"></span>**ERROR\_IPSEC\_DOSP\_RECEIVED\_MULTICAST**
</dt> <dd> <dl> <dt>

13926 (0x3666)
</dt> <dt>



IPsec DoS Protection received an IPsec specific multicast packet which is not allowed.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_DOSP_INVALID_PACKET"></span><span id="error_ipsec_dosp_invalid_packet"></span>**ERROR\_IPSEC\_DOSP\_INVALID\_PACKET**
</dt> <dd> <dl> <dt>

13927 (0x3667)
</dt> <dt>



IPsec DoS Protection received an incorrectly formatted packet.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_DOSP_STATE_LOOKUP_FAILED"></span><span id="error_ipsec_dosp_state_lookup_failed"></span>**ERROR\_IPSEC\_DOSP\_STATE\_LOOKUP\_FAILED**
</dt> <dd> <dl> <dt>

13928 (0x3668)
</dt> <dt>



IPsec DoS Protection failed to look up state.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_DOSP_MAX_ENTRIES"></span><span id="error_ipsec_dosp_max_entries"></span>**ERROR\_IPSEC\_DOSP\_MAX\_ENTRIES**
</dt> <dd> <dl> <dt>

13929 (0x3669)
</dt> <dt>



IPsec DoS Protection failed to create state because the maximum number of entries allowed by policy has been reached.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_DOSP_KEYMOD_NOT_ALLOWED"></span><span id="error_ipsec_dosp_keymod_not_allowed"></span>**ERROR\_IPSEC\_DOSP\_KEYMOD\_NOT\_ALLOWED**
</dt> <dd> <dl> <dt>

13930 (0x366A)
</dt> <dt>



IPsec DoS Protection received an IPsec negotiation packet for a keying module which is not allowed by policy.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_DOSP_NOT_INSTALLED"></span><span id="error_ipsec_dosp_not_installed"></span>**ERROR\_IPSEC\_DOSP\_NOT\_INSTALLED**
</dt> <dd> <dl> <dt>

13931 (0x366B)
</dt> <dt>



IPsec DoS Protection has not been enabled.


</dt> </dl> </dd> <dt>

<span id="ERROR_IPSEC_DOSP_MAX_PER_IP_RATELIMIT_QUEUES"></span><span id="error_ipsec_dosp_max_per_ip_ratelimit_queues"></span>**ERROR\_IPSEC\_DOSP\_MAX\_PER\_IP\_RATELIMIT\_QUEUES**
</dt> <dd> <dl> <dt>

13932 (0x366C)
</dt> <dt>



IPsec DoS Protection failed to create a per internal IP rate limit queue because the maximum number of queues allowed by policy has been reached.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_SECTION_NOT_FOUND"></span><span id="error_sxs_section_not_found"></span>**ERROR\_SXS\_SECTION\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

14000 (0x36B0)
</dt> <dt>



The requested section was not present in the activation context.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_CANT_GEN_ACTCTX"></span><span id="error_sxs_cant_gen_actctx"></span>**ERROR\_SXS\_CANT\_GEN\_ACTCTX**
</dt> <dd> <dl> <dt>

14001 (0x36B1)
</dt> <dt>



The application has failed to start because its side-by-side configuration is incorrect. Please see the application event log or use the command-line sxstrace.exe tool for more detail.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_INVALID_ACTCTXDATA_FORMAT"></span><span id="error_sxs_invalid_actctxdata_format"></span>**ERROR\_SXS\_INVALID\_ACTCTXDATA\_FORMAT**
</dt> <dd> <dl> <dt>

14002 (0x36B2)
</dt> <dt>



The application binding data format is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_ASSEMBLY_NOT_FOUND"></span><span id="error_sxs_assembly_not_found"></span>**ERROR\_SXS\_ASSEMBLY\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

14003 (0x36B3)
</dt> <dt>



The referenced assembly is not installed on your system.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_MANIFEST_FORMAT_ERROR"></span><span id="error_sxs_manifest_format_error"></span>**ERROR\_SXS\_MANIFEST\_FORMAT\_ERROR**
</dt> <dd> <dl> <dt>

14004 (0x36B4)
</dt> <dt>



The manifest file does not begin with the required tag and format information.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_MANIFEST_PARSE_ERROR"></span><span id="error_sxs_manifest_parse_error"></span>**ERROR\_SXS\_MANIFEST\_PARSE\_ERROR**
</dt> <dd> <dl> <dt>

14005 (0x36B5)
</dt> <dt>



The manifest file contains one or more syntax errors.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_ACTIVATION_CONTEXT_DISABLED"></span><span id="error_sxs_activation_context_disabled"></span>**ERROR\_SXS\_ACTIVATION\_CONTEXT\_DISABLED**
</dt> <dd> <dl> <dt>

14006 (0x36B6)
</dt> <dt>



The application attempted to activate a disabled activation context.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_KEY_NOT_FOUND"></span><span id="error_sxs_key_not_found"></span>**ERROR\_SXS\_KEY\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

14007 (0x36B7)
</dt> <dt>



The requested lookup key was not found in any active activation context.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_VERSION_CONFLICT"></span><span id="error_sxs_version_conflict"></span>**ERROR\_SXS\_VERSION\_CONFLICT**
</dt> <dd> <dl> <dt>

14008 (0x36B8)
</dt> <dt>



A component version required by the application conflicts with another component version already active.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_WRONG_SECTION_TYPE"></span><span id="error_sxs_wrong_section_type"></span>**ERROR\_SXS\_WRONG\_SECTION\_TYPE**
</dt> <dd> <dl> <dt>

14009 (0x36B9)
</dt> <dt>



The type requested activation context section does not match the query API used.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_THREAD_QUERIES_DISABLED"></span><span id="error_sxs_thread_queries_disabled"></span>**ERROR\_SXS\_THREAD\_QUERIES\_DISABLED**
</dt> <dd> <dl> <dt>

14010 (0x36BA)
</dt> <dt>



Lack of system resources has required isolated activation to be disabled for the current thread of execution.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_PROCESS_DEFAULT_ALREADY_SET"></span><span id="error_sxs_process_default_already_set"></span>**ERROR\_SXS\_PROCESS\_DEFAULT\_ALREADY\_SET**
</dt> <dd> <dl> <dt>

14011 (0x36BB)
</dt> <dt>



An attempt to set the process default activation context failed because the process default activation context was already set.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_UNKNOWN_ENCODING_GROUP"></span><span id="error_sxs_unknown_encoding_group"></span>**ERROR\_SXS\_UNKNOWN\_ENCODING\_GROUP**
</dt> <dd> <dl> <dt>

14012 (0x36BC)
</dt> <dt>



The encoding group identifier specified is not recognized.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_UNKNOWN_ENCODING"></span><span id="error_sxs_unknown_encoding"></span>**ERROR\_SXS\_UNKNOWN\_ENCODING**
</dt> <dd> <dl> <dt>

14013 (0x36BD)
</dt> <dt>



The encoding requested is not recognized.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_INVALID_XML_NAMESPACE_URI"></span><span id="error_sxs_invalid_xml_namespace_uri"></span>**ERROR\_SXS\_INVALID\_XML\_NAMESPACE\_URI**
</dt> <dd> <dl> <dt>

14014 (0x36BE)
</dt> <dt>



The manifest contains a reference to an invalid URI.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_ROOT_MANIFEST_DEPENDENCY_NOT_INSTALLED"></span><span id="error_sxs_root_manifest_dependency_not_installed"></span>**ERROR\_SXS\_ROOT\_MANIFEST\_DEPENDENCY\_NOT\_INSTALLED**
</dt> <dd> <dl> <dt>

14015 (0x36BF)
</dt> <dt>



The application manifest contains a reference to a dependent assembly which is not installed.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_LEAF_MANIFEST_DEPENDENCY_NOT_INSTALLED"></span><span id="error_sxs_leaf_manifest_dependency_not_installed"></span>**ERROR\_SXS\_LEAF\_MANIFEST\_DEPENDENCY\_NOT\_INSTALLED**
</dt> <dd> <dl> <dt>

14016 (0x36C0)
</dt> <dt>



The manifest for an assembly used by the application has a reference to a dependent assembly which is not installed.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_INVALID_ASSEMBLY_IDENTITY_ATTRIBUTE"></span><span id="error_sxs_invalid_assembly_identity_attribute"></span>**ERROR\_SXS\_INVALID\_ASSEMBLY\_IDENTITY\_ATTRIBUTE**
</dt> <dd> <dl> <dt>

14017 (0x36C1)
</dt> <dt>



The manifest contains an attribute for the assembly identity which is not valid.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_MANIFEST_MISSING_REQUIRED_DEFAULT_NAMESPACE"></span><span id="error_sxs_manifest_missing_required_default_namespace"></span>**ERROR\_SXS\_MANIFEST\_MISSING\_REQUIRED\_DEFAULT\_NAMESPACE**
</dt> <dd> <dl> <dt>

14018 (0x36C2)
</dt> <dt>



The manifest is missing the required default namespace specification on the assembly element.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_MANIFEST_INVALID_REQUIRED_DEFAULT_NAMESPACE"></span><span id="error_sxs_manifest_invalid_required_default_namespace"></span>**ERROR\_SXS\_MANIFEST\_INVALID\_REQUIRED\_DEFAULT\_NAMESPACE**
</dt> <dd> <dl> <dt>

14019 (0x36C3)
</dt> <dt>



The manifest has a default namespace specified on the assembly element but its value is not "urn:schemas-microsoft-com:asm.v1".


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_PRIVATE_MANIFEST_CROSS_PATH_WITH_REPARSE_POINT"></span><span id="error_sxs_private_manifest_cross_path_with_reparse_point"></span>**ERROR\_SXS\_PRIVATE\_MANIFEST\_CROSS\_PATH\_WITH\_REPARSE\_POINT**
</dt> <dd> <dl> <dt>

14020 (0x36C4)
</dt> <dt>



The private manifest probed has crossed a path with an unsupported reparse point.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_DUPLICATE_DLL_NAME"></span><span id="error_sxs_duplicate_dll_name"></span>**ERROR\_SXS\_DUPLICATE\_DLL\_NAME**
</dt> <dd> <dl> <dt>

14021 (0x36C5)
</dt> <dt>



Two or more components referenced directly or indirectly by the application manifest have files by the same name.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_DUPLICATE_WINDOWCLASS_NAME"></span><span id="error_sxs_duplicate_windowclass_name"></span>**ERROR\_SXS\_DUPLICATE\_WINDOWCLASS\_NAME**
</dt> <dd> <dl> <dt>

14022 (0x36C6)
</dt> <dt>



Two or more components referenced directly or indirectly by the application manifest have window classes with the same name.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_DUPLICATE_CLSID"></span><span id="error_sxs_duplicate_clsid"></span>**ERROR\_SXS\_DUPLICATE\_CLSID**
</dt> <dd> <dl> <dt>

14023 (0x36C7)
</dt> <dt>



Two or more components referenced directly or indirectly by the application manifest have the same COM server CLSIDs.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_DUPLICATE_IID"></span><span id="error_sxs_duplicate_iid"></span>**ERROR\_SXS\_DUPLICATE\_IID**
</dt> <dd> <dl> <dt>

14024 (0x36C8)
</dt> <dt>



Two or more components referenced directly or indirectly by the application manifest have proxies for the same COM interface IIDs.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_DUPLICATE_TLBID"></span><span id="error_sxs_duplicate_tlbid"></span>**ERROR\_SXS\_DUPLICATE\_TLBID**
</dt> <dd> <dl> <dt>

14025 (0x36C9)
</dt> <dt>



Two or more components referenced directly or indirectly by the application manifest have the same COM type library TLBIDs.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_DUPLICATE_PROGID"></span><span id="error_sxs_duplicate_progid"></span>**ERROR\_SXS\_DUPLICATE\_PROGID**
</dt> <dd> <dl> <dt>

14026 (0x36CA)
</dt> <dt>



Two or more components referenced directly or indirectly by the application manifest have the same COM ProgIDs.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_DUPLICATE_ASSEMBLY_NAME"></span><span id="error_sxs_duplicate_assembly_name"></span>**ERROR\_SXS\_DUPLICATE\_ASSEMBLY\_NAME**
</dt> <dd> <dl> <dt>

14027 (0x36CB)
</dt> <dt>



Two or more components referenced directly or indirectly by the application manifest are different versions of the same component which is not permitted.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_FILE_HASH_MISMATCH"></span><span id="error_sxs_file_hash_mismatch"></span>**ERROR\_SXS\_FILE\_HASH\_MISMATCH**
</dt> <dd> <dl> <dt>

14028 (0x36CC)
</dt> <dt>



A component's file does not match the verification information present in the component manifest.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_POLICY_PARSE_ERROR"></span><span id="error_sxs_policy_parse_error"></span>**ERROR\_SXS\_POLICY\_PARSE\_ERROR**
</dt> <dd> <dl> <dt>

14029 (0x36CD)
</dt> <dt>



The policy manifest contains one or more syntax errors.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_XML_E_MISSINGQUOTE"></span><span id="error_sxs_xml_e_missingquote"></span>**ERROR\_SXS\_XML\_E\_MISSINGQUOTE**
</dt> <dd> <dl> <dt>

14030 (0x36CE)
</dt> <dt>



Manifest Parse Error : A string literal was expected, but no opening quote character was found.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_XML_E_COMMENTSYNTAX"></span><span id="error_sxs_xml_e_commentsyntax"></span>**ERROR\_SXS\_XML\_E\_COMMENTSYNTAX**
</dt> <dd> <dl> <dt>

14031 (0x36CF)
</dt> <dt>



Manifest Parse Error : Incorrect syntax was used in a comment.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_XML_E_BADSTARTNAMECHAR"></span><span id="error_sxs_xml_e_badstartnamechar"></span>**ERROR\_SXS\_XML\_E\_BADSTARTNAMECHAR**
</dt> <dd> <dl> <dt>

14032 (0x36D0)
</dt> <dt>



Manifest Parse Error : A name was started with an invalid character.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_XML_E_BADNAMECHAR"></span><span id="error_sxs_xml_e_badnamechar"></span>**ERROR\_SXS\_XML\_E\_BADNAMECHAR**
</dt> <dd> <dl> <dt>

14033 (0x36D1)
</dt> <dt>



Manifest Parse Error : A name contained an invalid character.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_XML_E_BADCHARINSTRING"></span><span id="error_sxs_xml_e_badcharinstring"></span>**ERROR\_SXS\_XML\_E\_BADCHARINSTRING**
</dt> <dd> <dl> <dt>

14034 (0x36D2)
</dt> <dt>



Manifest Parse Error : A string literal contained an invalid character.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_XML_E_XMLDECLSYNTAX"></span><span id="error_sxs_xml_e_xmldeclsyntax"></span>**ERROR\_SXS\_XML\_E\_XMLDECLSYNTAX**
</dt> <dd> <dl> <dt>

14035 (0x36D3)
</dt> <dt>



Manifest Parse Error : Invalid syntax for an xml declaration.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_XML_E_BADCHARDATA"></span><span id="error_sxs_xml_e_badchardata"></span>**ERROR\_SXS\_XML\_E\_BADCHARDATA**
</dt> <dd> <dl> <dt>

14036 (0x36D4)
</dt> <dt>



Manifest Parse Error : An Invalid character was found in text content.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_XML_E_MISSINGWHITESPACE"></span><span id="error_sxs_xml_e_missingwhitespace"></span>**ERROR\_SXS\_XML\_E\_MISSINGWHITESPACE**
</dt> <dd> <dl> <dt>

14037 (0x36D5)
</dt> <dt>



Manifest Parse Error : Required white space was missing.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_XML_E_EXPECTINGTAGEND"></span><span id="error_sxs_xml_e_expectingtagend"></span>**ERROR\_SXS\_XML\_E\_EXPECTINGTAGEND**
</dt> <dd> <dl> <dt>

14038 (0x36D6)
</dt> <dt>



Manifest Parse Error : The character '>' was expected.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_XML_E_MISSINGSEMICOLON"></span><span id="error_sxs_xml_e_missingsemicolon"></span>**ERROR\_SXS\_XML\_E\_MISSINGSEMICOLON**
</dt> <dd> <dl> <dt>

14039 (0x36D7)
</dt> <dt>



Manifest Parse Error : A semi colon character was expected.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_XML_E_UNBALANCEDPAREN"></span><span id="error_sxs_xml_e_unbalancedparen"></span>**ERROR\_SXS\_XML\_E\_UNBALANCEDPAREN**
</dt> <dd> <dl> <dt>

14040 (0x36D8)
</dt> <dt>



Manifest Parse Error : Unbalanced parentheses.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_XML_E_INTERNALERROR"></span><span id="error_sxs_xml_e_internalerror"></span>**ERROR\_SXS\_XML\_E\_INTERNALERROR**
</dt> <dd> <dl> <dt>

14041 (0x36D9)
</dt> <dt>



Manifest Parse Error : Internal error.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_XML_E_UNEXPECTED_WHITESPACE"></span><span id="error_sxs_xml_e_unexpected_whitespace"></span>**ERROR\_SXS\_XML\_E\_UNEXPECTED\_WHITESPACE**
</dt> <dd> <dl> <dt>

14042 (0x36DA)
</dt> <dt>



Manifest Parse Error : Whitespace is not allowed at this location.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_XML_E_INCOMPLETE_ENCODING"></span><span id="error_sxs_xml_e_incomplete_encoding"></span>**ERROR\_SXS\_XML\_E\_INCOMPLETE\_ENCODING**
</dt> <dd> <dl> <dt>

14043 (0x36DB)
</dt> <dt>



Manifest Parse Error : End of file reached in invalid state for current encoding.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_XML_E_MISSING_PAREN"></span><span id="error_sxs_xml_e_missing_paren"></span>**ERROR\_SXS\_XML\_E\_MISSING\_PAREN**
</dt> <dd> <dl> <dt>

14044 (0x36DC)
</dt> <dt>



Manifest Parse Error : Missing parenthesis.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_XML_E_EXPECTINGCLOSEQUOTE"></span><span id="error_sxs_xml_e_expectingclosequote"></span>**ERROR\_SXS\_XML\_E\_EXPECTINGCLOSEQUOTE**
</dt> <dd> <dl> <dt>

14045 (0x36DD)
</dt> <dt>



Manifest Parse Error : A single or double closing quote character (\\' or \\") is missing.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_XML_E_MULTIPLE_COLONS"></span><span id="error_sxs_xml_e_multiple_colons"></span>**ERROR\_SXS\_XML\_E\_MULTIPLE\_COLONS**
</dt> <dd> <dl> <dt>

14046 (0x36DE)
</dt> <dt>



Manifest Parse Error : Multiple colons are not allowed in a name.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_XML_E_INVALID_DECIMAL"></span><span id="error_sxs_xml_e_invalid_decimal"></span>**ERROR\_SXS\_XML\_E\_INVALID\_DECIMAL**
</dt> <dd> <dl> <dt>

14047 (0x36DF)
</dt> <dt>



Manifest Parse Error : Invalid character for decimal digit.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_XML_E_INVALID_HEXIDECIMAL"></span><span id="error_sxs_xml_e_invalid_hexidecimal"></span>**ERROR\_SXS\_XML\_E\_INVALID\_HEXIDECIMAL**
</dt> <dd> <dl> <dt>

14048 (0x36E0)
</dt> <dt>



Manifest Parse Error : Invalid character for hexadecimal digit.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_XML_E_INVALID_UNICODE"></span><span id="error_sxs_xml_e_invalid_unicode"></span>**ERROR\_SXS\_XML\_E\_INVALID\_UNICODE**
</dt> <dd> <dl> <dt>

14049 (0x36E1)
</dt> <dt>



Manifest Parse Error : Invalid unicode character value for this platform.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_XML_E_WHITESPACEORQUESTIONMARK"></span><span id="error_sxs_xml_e_whitespaceorquestionmark"></span>**ERROR\_SXS\_XML\_E\_WHITESPACEORQUESTIONMARK**
</dt> <dd> <dl> <dt>

14050 (0x36E2)
</dt> <dt>



Manifest Parse Error : Expecting whitespace or '?'.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_XML_E_UNEXPECTEDENDTAG"></span><span id="error_sxs_xml_e_unexpectedendtag"></span>**ERROR\_SXS\_XML\_E\_UNEXPECTEDENDTAG**
</dt> <dd> <dl> <dt>

14051 (0x36E3)
</dt> <dt>



Manifest Parse Error : End tag was not expected at this location.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_XML_E_UNCLOSEDTAG"></span><span id="error_sxs_xml_e_unclosedtag"></span>**ERROR\_SXS\_XML\_E\_UNCLOSEDTAG**
</dt> <dd> <dl> <dt>

14052 (0x36E4)
</dt> <dt>



Manifest Parse Error : The following tags were not closed: %1.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_XML_E_DUPLICATEATTRIBUTE"></span><span id="error_sxs_xml_e_duplicateattribute"></span>**ERROR\_SXS\_XML\_E\_DUPLICATEATTRIBUTE**
</dt> <dd> <dl> <dt>

14053 (0x36E5)
</dt> <dt>



Manifest Parse Error : Duplicate attribute.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_XML_E_MULTIPLEROOTS"></span><span id="error_sxs_xml_e_multipleroots"></span>**ERROR\_SXS\_XML\_E\_MULTIPLEROOTS**
</dt> <dd> <dl> <dt>

14054 (0x36E6)
</dt> <dt>



Manifest Parse Error : Only one top level element is allowed in an XML document.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_XML_E_INVALIDATROOTLEVEL"></span><span id="error_sxs_xml_e_invalidatrootlevel"></span>**ERROR\_SXS\_XML\_E\_INVALIDATROOTLEVEL**
</dt> <dd> <dl> <dt>

14055 (0x36E7)
</dt> <dt>



Manifest Parse Error : Invalid at the top level of the document.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_XML_E_BADXMLDECL"></span><span id="error_sxs_xml_e_badxmldecl"></span>**ERROR\_SXS\_XML\_E\_BADXMLDECL**
</dt> <dd> <dl> <dt>

14056 (0x36E8)
</dt> <dt>



Manifest Parse Error : Invalid xml declaration.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_XML_E_MISSINGROOT"></span><span id="error_sxs_xml_e_missingroot"></span>**ERROR\_SXS\_XML\_E\_MISSINGROOT**
</dt> <dd> <dl> <dt>

14057 (0x36E9)
</dt> <dt>



Manifest Parse Error : XML document must have a top level element.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_XML_E_UNEXPECTEDEOF"></span><span id="error_sxs_xml_e_unexpectedeof"></span>**ERROR\_SXS\_XML\_E\_UNEXPECTEDEOF**
</dt> <dd> <dl> <dt>

14058 (0x36EA)
</dt> <dt>



Manifest Parse Error : Unexpected end of file.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_XML_E_BADPEREFINSUBSET"></span><span id="error_sxs_xml_e_badperefinsubset"></span>**ERROR\_SXS\_XML\_E\_BADPEREFINSUBSET**
</dt> <dd> <dl> <dt>

14059 (0x36EB)
</dt> <dt>



Manifest Parse Error : Parameter entities cannot be used inside markup declarations in an internal subset.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_XML_E_UNCLOSEDSTARTTAG"></span><span id="error_sxs_xml_e_unclosedstarttag"></span>**ERROR\_SXS\_XML\_E\_UNCLOSEDSTARTTAG**
</dt> <dd> <dl> <dt>

14060 (0x36EC)
</dt> <dt>



Manifest Parse Error : Element was not closed.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_XML_E_UNCLOSEDENDTAG"></span><span id="error_sxs_xml_e_unclosedendtag"></span>**ERROR\_SXS\_XML\_E\_UNCLOSEDENDTAG**
</dt> <dd> <dl> <dt>

14061 (0x36ED)
</dt> <dt>



Manifest Parse Error : End element was missing the character '>'.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_XML_E_UNCLOSEDSTRING"></span><span id="error_sxs_xml_e_unclosedstring"></span>**ERROR\_SXS\_XML\_E\_UNCLOSEDSTRING**
</dt> <dd> <dl> <dt>

14062 (0x36EE)
</dt> <dt>



Manifest Parse Error : A string literal was not closed.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_XML_E_UNCLOSEDCOMMENT"></span><span id="error_sxs_xml_e_unclosedcomment"></span>**ERROR\_SXS\_XML\_E\_UNCLOSEDCOMMENT**
</dt> <dd> <dl> <dt>

14063 (0x36EF)
</dt> <dt>



Manifest Parse Error : A comment was not closed.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_XML_E_UNCLOSEDDECL"></span><span id="error_sxs_xml_e_uncloseddecl"></span>**ERROR\_SXS\_XML\_E\_UNCLOSEDDECL**
</dt> <dd> <dl> <dt>

14064 (0x36F0)
</dt> <dt>



Manifest Parse Error : A declaration was not closed.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_XML_E_UNCLOSEDCDATA"></span><span id="error_sxs_xml_e_unclosedcdata"></span>**ERROR\_SXS\_XML\_E\_UNCLOSEDCDATA**
</dt> <dd> <dl> <dt>

14065 (0x36F1)
</dt> <dt>



Manifest Parse Error : A CDATA section was not closed.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_XML_E_RESERVEDNAMESPACE"></span><span id="error_sxs_xml_e_reservednamespace"></span>**ERROR\_SXS\_XML\_E\_RESERVEDNAMESPACE**
</dt> <dd> <dl> <dt>

14066 (0x36F2)
</dt> <dt>



Manifest Parse Error : The namespace prefix is not allowed to start with the reserved string "xml".


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_XML_E_INVALIDENCODING"></span><span id="error_sxs_xml_e_invalidencoding"></span>**ERROR\_SXS\_XML\_E\_INVALIDENCODING**
</dt> <dd> <dl> <dt>

14067 (0x36F3)
</dt> <dt>



Manifest Parse Error : System does not support the specified encoding.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_XML_E_INVALIDSWITCH"></span><span id="error_sxs_xml_e_invalidswitch"></span>**ERROR\_SXS\_XML\_E\_INVALIDSWITCH**
</dt> <dd> <dl> <dt>

14068 (0x36F4)
</dt> <dt>



Manifest Parse Error : Switch from current encoding to specified encoding not supported.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_XML_E_BADXMLCASE"></span><span id="error_sxs_xml_e_badxmlcase"></span>**ERROR\_SXS\_XML\_E\_BADXMLCASE**
</dt> <dd> <dl> <dt>

14069 (0x36F5)
</dt> <dt>



Manifest Parse Error : The name 'xml' is reserved and must be lower case.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_XML_E_INVALID_STANDALONE"></span><span id="error_sxs_xml_e_invalid_standalone"></span>**ERROR\_SXS\_XML\_E\_INVALID\_STANDALONE**
</dt> <dd> <dl> <dt>

14070 (0x36F6)
</dt> <dt>



Manifest Parse Error : The standalone attribute must have the value 'yes' or 'no'.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_XML_E_UNEXPECTED_STANDALONE"></span><span id="error_sxs_xml_e_unexpected_standalone"></span>**ERROR\_SXS\_XML\_E\_UNEXPECTED\_STANDALONE**
</dt> <dd> <dl> <dt>

14071 (0x36F7)
</dt> <dt>



Manifest Parse Error : The standalone attribute cannot be used in external entities.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_XML_E_INVALID_VERSION"></span><span id="error_sxs_xml_e_invalid_version"></span>**ERROR\_SXS\_XML\_E\_INVALID\_VERSION**
</dt> <dd> <dl> <dt>

14072 (0x36F8)
</dt> <dt>



Manifest Parse Error : Invalid version number.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_XML_E_MISSINGEQUALS"></span><span id="error_sxs_xml_e_missingequals"></span>**ERROR\_SXS\_XML\_E\_MISSINGEQUALS**
</dt> <dd> <dl> <dt>

14073 (0x36F9)
</dt> <dt>



Manifest Parse Error : Missing equals sign between attribute and attribute value.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_PROTECTION_RECOVERY_FAILED"></span><span id="error_sxs_protection_recovery_failed"></span>**ERROR\_SXS\_PROTECTION\_RECOVERY\_FAILED**
</dt> <dd> <dl> <dt>

14074 (0x36FA)
</dt> <dt>



Assembly Protection Error : Unable to recover the specified assembly.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_PROTECTION_PUBLIC_KEY_TOO_SHORT"></span><span id="error_sxs_protection_public_key_too_short"></span>**ERROR\_SXS\_PROTECTION\_PUBLIC\_KEY\_TOO\_SHORT**
</dt> <dd> <dl> <dt>

14075 (0x36FB)
</dt> <dt>



Assembly Protection Error : The public key for an assembly was too short to be allowed.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_PROTECTION_CATALOG_NOT_VALID"></span><span id="error_sxs_protection_catalog_not_valid"></span>**ERROR\_SXS\_PROTECTION\_CATALOG\_NOT\_VALID**
</dt> <dd> <dl> <dt>

14076 (0x36FC)
</dt> <dt>



Assembly Protection Error : The catalog for an assembly is not valid, or does not match the assembly's manifest.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_UNTRANSLATABLE_HRESULT"></span><span id="error_sxs_untranslatable_hresult"></span>**ERROR\_SXS\_UNTRANSLATABLE\_HRESULT**
</dt> <dd> <dl> <dt>

14077 (0x36FD)
</dt> <dt>



An HRESULT could not be translated to a corresponding Win32 error code.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_PROTECTION_CATALOG_FILE_MISSING"></span><span id="error_sxs_protection_catalog_file_missing"></span>**ERROR\_SXS\_PROTECTION\_CATALOG\_FILE\_MISSING**
</dt> <dd> <dl> <dt>

14078 (0x36FE)
</dt> <dt>



Assembly Protection Error : The catalog for an assembly is missing.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_MISSING_ASSEMBLY_IDENTITY_ATTRIBUTE"></span><span id="error_sxs_missing_assembly_identity_attribute"></span>**ERROR\_SXS\_MISSING\_ASSEMBLY\_IDENTITY\_ATTRIBUTE**
</dt> <dd> <dl> <dt>

14079 (0x36FF)
</dt> <dt>



The supplied assembly identity is missing one or more attributes which must be present in this context.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_INVALID_ASSEMBLY_IDENTITY_ATTRIBUTE_NAME"></span><span id="error_sxs_invalid_assembly_identity_attribute_name"></span>**ERROR\_SXS\_INVALID\_ASSEMBLY\_IDENTITY\_ATTRIBUTE\_NAME**
</dt> <dd> <dl> <dt>

14080 (0x3700)
</dt> <dt>



The supplied assembly identity has one or more attribute names that contain characters not permitted in XML names.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_ASSEMBLY_MISSING"></span><span id="error_sxs_assembly_missing"></span>**ERROR\_SXS\_ASSEMBLY\_MISSING**
</dt> <dd> <dl> <dt>

14081 (0x3701)
</dt> <dt>



The referenced assembly could not be found.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_CORRUPT_ACTIVATION_STACK"></span><span id="error_sxs_corrupt_activation_stack"></span>**ERROR\_SXS\_CORRUPT\_ACTIVATION\_STACK**
</dt> <dd> <dl> <dt>

14082 (0x3702)
</dt> <dt>



The activation context activation stack for the running thread of execution is corrupt.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_CORRUPTION"></span><span id="error_sxs_corruption"></span>**ERROR\_SXS\_CORRUPTION**
</dt> <dd> <dl> <dt>

14083 (0x3703)
</dt> <dt>



The application isolation metadata for this process or thread has become corrupt.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_EARLY_DEACTIVATION"></span><span id="error_sxs_early_deactivation"></span>**ERROR\_SXS\_EARLY\_DEACTIVATION**
</dt> <dd> <dl> <dt>

14084 (0x3704)
</dt> <dt>



The activation context being deactivated is not the most recently activated one.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_INVALID_DEACTIVATION"></span><span id="error_sxs_invalid_deactivation"></span>**ERROR\_SXS\_INVALID\_DEACTIVATION**
</dt> <dd> <dl> <dt>

14085 (0x3705)
</dt> <dt>



The activation context being deactivated is not active for the current thread of execution.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_MULTIPLE_DEACTIVATION"></span><span id="error_sxs_multiple_deactivation"></span>**ERROR\_SXS\_MULTIPLE\_DEACTIVATION**
</dt> <dd> <dl> <dt>

14086 (0x3706)
</dt> <dt>



The activation context being deactivated has already been deactivated.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_PROCESS_TERMINATION_REQUESTED"></span><span id="error_sxs_process_termination_requested"></span>**ERROR\_SXS\_PROCESS\_TERMINATION\_REQUESTED**
</dt> <dd> <dl> <dt>

14087 (0x3707)
</dt> <dt>



A component used by the isolation facility has requested to terminate the process.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_RELEASE_ACTIVATION_CONTEXT"></span><span id="error_sxs_release_activation_context"></span>**ERROR\_SXS\_RELEASE\_ACTIVATION\_CONTEXT**
</dt> <dd> <dl> <dt>

14088 (0x3708)
</dt> <dt>



A kernel mode component is releasing a reference on an activation context.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_SYSTEM_DEFAULT_ACTIVATION_CONTEXT_EMPTY"></span><span id="error_sxs_system_default_activation_context_empty"></span>**ERROR\_SXS\_SYSTEM\_DEFAULT\_ACTIVATION\_CONTEXT\_EMPTY**
</dt> <dd> <dl> <dt>

14089 (0x3709)
</dt> <dt>



The activation context of system default assembly could not be generated.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_INVALID_IDENTITY_ATTRIBUTE_VALUE"></span><span id="error_sxs_invalid_identity_attribute_value"></span>**ERROR\_SXS\_INVALID\_IDENTITY\_ATTRIBUTE\_VALUE**
</dt> <dd> <dl> <dt>

14090 (0x370A)
</dt> <dt>



The value of an attribute in an identity is not within the legal range.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_INVALID_IDENTITY_ATTRIBUTE_NAME"></span><span id="error_sxs_invalid_identity_attribute_name"></span>**ERROR\_SXS\_INVALID\_IDENTITY\_ATTRIBUTE\_NAME**
</dt> <dd> <dl> <dt>

14091 (0x370B)
</dt> <dt>



The name of an attribute in an identity is not within the legal range.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_IDENTITY_DUPLICATE_ATTRIBUTE"></span><span id="error_sxs_identity_duplicate_attribute"></span>**ERROR\_SXS\_IDENTITY\_DUPLICATE\_ATTRIBUTE**
</dt> <dd> <dl> <dt>

14092 (0x370C)
</dt> <dt>



An identity contains two definitions for the same attribute.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_IDENTITY_PARSE_ERROR"></span><span id="error_sxs_identity_parse_error"></span>**ERROR\_SXS\_IDENTITY\_PARSE\_ERROR**
</dt> <dd> <dl> <dt>

14093 (0x370D)
</dt> <dt>



The identity string is malformed. This may be due to a trailing comma, more than two unnamed attributes, missing attribute name or missing attribute value.


</dt> </dl> </dd> <dt>

<span id="ERROR_MALFORMED_SUBSTITUTION_STRING"></span><span id="error_malformed_substitution_string"></span>**ERROR\_MALFORMED\_SUBSTITUTION\_STRING**
</dt> <dd> <dl> <dt>

14094 (0x370E)
</dt> <dt>



A string containing localized substitutable content was malformed. Either a dollar sign ($) was followed by something other than a left parenthesis or another dollar sign or an substitution's right parenthesis was not found.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_INCORRECT_PUBLIC_KEY_TOKEN"></span><span id="error_sxs_incorrect_public_key_token"></span>**ERROR\_SXS\_INCORRECT\_PUBLIC\_KEY\_TOKEN**
</dt> <dd> <dl> <dt>

14095 (0x370F)
</dt> <dt>



The public key token does not correspond to the public key specified.


</dt> </dl> </dd> <dt>

<span id="ERROR_UNMAPPED_SUBSTITUTION_STRING"></span><span id="error_unmapped_substitution_string"></span>**ERROR\_UNMAPPED\_SUBSTITUTION\_STRING**
</dt> <dd> <dl> <dt>

14096 (0x3710)
</dt> <dt>



A substitution string had no mapping.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_ASSEMBLY_NOT_LOCKED"></span><span id="error_sxs_assembly_not_locked"></span>**ERROR\_SXS\_ASSEMBLY\_NOT\_LOCKED**
</dt> <dd> <dl> <dt>

14097 (0x3711)
</dt> <dt>



The component must be locked before making the request.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_COMPONENT_STORE_CORRUPT"></span><span id="error_sxs_component_store_corrupt"></span>**ERROR\_SXS\_COMPONENT\_STORE\_CORRUPT**
</dt> <dd> <dl> <dt>

14098 (0x3712)
</dt> <dt>



The component store has been corrupted.


</dt> </dl> </dd> <dt>

<span id="ERROR_ADVANCED_INSTALLER_FAILED"></span><span id="error_advanced_installer_failed"></span>**ERROR\_ADVANCED\_INSTALLER\_FAILED**
</dt> <dd> <dl> <dt>

14099 (0x3713)
</dt> <dt>



An advanced installer failed during setup or servicing.


</dt> </dl> </dd> <dt>

<span id="ERROR_XML_ENCODING_MISMATCH"></span><span id="error_xml_encoding_mismatch"></span>**ERROR\_XML\_ENCODING\_MISMATCH**
</dt> <dd> <dl> <dt>

14100 (0x3714)
</dt> <dt>



The character encoding in the XML declaration did not match the encoding used in the document.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_MANIFEST_IDENTITY_SAME_BUT_CONTENTS_DIFFERENT"></span><span id="error_sxs_manifest_identity_same_but_contents_different"></span>**ERROR\_SXS\_MANIFEST\_IDENTITY\_SAME\_BUT\_CONTENTS\_DIFFERENT**
</dt> <dd> <dl> <dt>

14101 (0x3715)
</dt> <dt>



The identities of the manifests are identical but their contents are different.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_IDENTITIES_DIFFERENT"></span><span id="error_sxs_identities_different"></span>**ERROR\_SXS\_IDENTITIES\_DIFFERENT**
</dt> <dd> <dl> <dt>

14102 (0x3716)
</dt> <dt>



The component identities are different.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_ASSEMBLY_IS_NOT_A_DEPLOYMENT"></span><span id="error_sxs_assembly_is_not_a_deployment"></span>**ERROR\_SXS\_ASSEMBLY\_IS\_NOT\_A\_DEPLOYMENT**
</dt> <dd> <dl> <dt>

14103 (0x3717)
</dt> <dt>



The assembly is not a deployment.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_FILE_NOT_PART_OF_ASSEMBLY"></span><span id="error_sxs_file_not_part_of_assembly"></span>**ERROR\_SXS\_FILE\_NOT\_PART\_OF\_ASSEMBLY**
</dt> <dd> <dl> <dt>

14104 (0x3718)
</dt> <dt>



The file is not a part of the assembly.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_MANIFEST_TOO_BIG"></span><span id="error_sxs_manifest_too_big"></span>**ERROR\_SXS\_MANIFEST\_TOO\_BIG**
</dt> <dd> <dl> <dt>

14105 (0x3719)
</dt> <dt>



The size of the manifest exceeds the maximum allowed.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_SETTING_NOT_REGISTERED"></span><span id="error_sxs_setting_not_registered"></span>**ERROR\_SXS\_SETTING\_NOT\_REGISTERED**
</dt> <dd> <dl> <dt>

14106 (0x371A)
</dt> <dt>



The setting is not registered.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_TRANSACTION_CLOSURE_INCOMPLETE"></span><span id="error_sxs_transaction_closure_incomplete"></span>**ERROR\_SXS\_TRANSACTION\_CLOSURE\_INCOMPLETE**
</dt> <dd> <dl> <dt>

14107 (0x371B)
</dt> <dt>



One or more required members of the transaction are not present.


</dt> </dl> </dd> <dt>

<span id="ERROR_SMI_PRIMITIVE_INSTALLER_FAILED"></span><span id="error_smi_primitive_installer_failed"></span>**ERROR\_SMI\_PRIMITIVE\_INSTALLER\_FAILED**
</dt> <dd> <dl> <dt>

14108 (0x371C)
</dt> <dt>



The SMI primitive installer failed during setup or servicing.


</dt> </dl> </dd> <dt>

<span id="ERROR_GENERIC_COMMAND_FAILED"></span><span id="error_generic_command_failed"></span>**ERROR\_GENERIC\_COMMAND\_FAILED**
</dt> <dd> <dl> <dt>

14109 (0x371D)
</dt> <dt>



A generic command executable returned a result that indicates failure.


</dt> </dl> </dd> <dt>

<span id="ERROR_SXS_FILE_HASH_MISSING"></span><span id="error_sxs_file_hash_missing"></span>**ERROR\_SXS\_FILE\_HASH\_MISSING**
</dt> <dd> <dl> <dt>

14110 (0x371E)
</dt> <dt>



A component is missing file verification information in its manifest.


</dt> </dl> </dd> <dt>

<span id="ERROR_EVT_INVALID_CHANNEL_PATH"></span><span id="error_evt_invalid_channel_path"></span>**ERROR\_EVT\_INVALID\_CHANNEL\_PATH**
</dt> <dd> <dl> <dt>

15000 (0x3A98)
</dt> <dt>



The specified channel path is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_EVT_INVALID_QUERY"></span><span id="error_evt_invalid_query"></span>**ERROR\_EVT\_INVALID\_QUERY**
</dt> <dd> <dl> <dt>

15001 (0x3A99)
</dt> <dt>



The specified query is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_EVT_PUBLISHER_METADATA_NOT_FOUND"></span><span id="error_evt_publisher_metadata_not_found"></span>**ERROR\_EVT\_PUBLISHER\_METADATA\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

15002 (0x3A9A)
</dt> <dt>



The publisher metadata cannot be found in the resource.


</dt> </dl> </dd> <dt>

<span id="ERROR_EVT_EVENT_TEMPLATE_NOT_FOUND"></span><span id="error_evt_event_template_not_found"></span>**ERROR\_EVT\_EVENT\_TEMPLATE\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

15003 (0x3A9B)
</dt> <dt>



The template for an event definition cannot be found in the resource (error = %1).


</dt> </dl> </dd> <dt>

<span id="ERROR_EVT_INVALID_PUBLISHER_NAME"></span><span id="error_evt_invalid_publisher_name"></span>**ERROR\_EVT\_INVALID\_PUBLISHER\_NAME**
</dt> <dd> <dl> <dt>

15004 (0x3A9C)
</dt> <dt>



The specified publisher name is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_EVT_INVALID_EVENT_DATA"></span><span id="error_evt_invalid_event_data"></span>**ERROR\_EVT\_INVALID\_EVENT\_DATA**
</dt> <dd> <dl> <dt>

15005 (0x3A9D)
</dt> <dt>



The event data raised by the publisher is not compatible with the event template definition in the publisher's manifest.


</dt> </dl> </dd> <dt>

<span id="ERROR_EVT_CHANNEL_NOT_FOUND"></span><span id="error_evt_channel_not_found"></span>**ERROR\_EVT\_CHANNEL\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

15007 (0x3A9F)
</dt> <dt>



The specified channel could not be found. Check channel configuration.


</dt> </dl> </dd> <dt>

<span id="ERROR_EVT_MALFORMED_XML_TEXT"></span><span id="error_evt_malformed_xml_text"></span>**ERROR\_EVT\_MALFORMED\_XML\_TEXT**
</dt> <dd> <dl> <dt>

15008 (0x3AA0)
</dt> <dt>



The specified xml text was not well-formed. See Extended Error for more details.


</dt> </dl> </dd> <dt>

<span id="ERROR_EVT_SUBSCRIPTION_TO_DIRECT_CHANNEL"></span><span id="error_evt_subscription_to_direct_channel"></span>**ERROR\_EVT\_SUBSCRIPTION\_TO\_DIRECT\_CHANNEL**
</dt> <dd> <dl> <dt>

15009 (0x3AA1)
</dt> <dt>



The caller is trying to subscribe to a direct channel which is not allowed. The events for a direct channel go directly to a logfile and cannot be subscribed to.


</dt> </dl> </dd> <dt>

<span id="ERROR_EVT_CONFIGURATION_ERROR"></span><span id="error_evt_configuration_error"></span>**ERROR\_EVT\_CONFIGURATION\_ERROR**
</dt> <dd> <dl> <dt>

15010 (0x3AA2)
</dt> <dt>



Configuration error.


</dt> </dl> </dd> <dt>

<span id="ERROR_EVT_QUERY_RESULT_STALE"></span><span id="error_evt_query_result_stale"></span>**ERROR\_EVT\_QUERY\_RESULT\_STALE**
</dt> <dd> <dl> <dt>

15011 (0x3AA3)
</dt> <dt>



The query result is stale / invalid. This may be due to the log being cleared or rolling over after the query result was created. Users should handle this code by releasing the query result object and reissuing the query.


</dt> </dl> </dd> <dt>

<span id="ERROR_EVT_QUERY_RESULT_INVALID_POSITION"></span><span id="error_evt_query_result_invalid_position"></span>**ERROR\_EVT\_QUERY\_RESULT\_INVALID\_POSITION**
</dt> <dd> <dl> <dt>

15012 (0x3AA4)
</dt> <dt>



Query result is currently at an invalid position.


</dt> </dl> </dd> <dt>

<span id="ERROR_EVT_NON_VALIDATING_MSXML"></span><span id="error_evt_non_validating_msxml"></span>**ERROR\_EVT\_NON\_VALIDATING\_MSXML**
</dt> <dd> <dl> <dt>

15013 (0x3AA5)
</dt> <dt>



Registered MSXML doesn't support validation.


</dt> </dl> </dd> <dt>

<span id="ERROR_EVT_FILTER_ALREADYSCOPED"></span><span id="error_evt_filter_alreadyscoped"></span>**ERROR\_EVT\_FILTER\_ALREADYSCOPED**
</dt> <dd> <dl> <dt>

15014 (0x3AA6)
</dt> <dt>



An expression can only be followed by a change of scope operation if it itself evaluates to a node set and is not already part of some other change of scope operation.


</dt> </dl> </dd> <dt>

<span id="ERROR_EVT_FILTER_NOTELTSET"></span><span id="error_evt_filter_noteltset"></span>**ERROR\_EVT\_FILTER\_NOTELTSET**
</dt> <dd> <dl> <dt>

15015 (0x3AA7)
</dt> <dt>



Can't perform a step operation from a term that does not represent an element set.


</dt> </dl> </dd> <dt>

<span id="ERROR_EVT_FILTER_INVARG"></span><span id="error_evt_filter_invarg"></span>**ERROR\_EVT\_FILTER\_INVARG**
</dt> <dd> <dl> <dt>

15016 (0x3AA8)
</dt> <dt>



Left hand side arguments to binary operators must be either attributes, nodes or variables and right hand side arguments must be constants.


</dt> </dl> </dd> <dt>

<span id="ERROR_EVT_FILTER_INVTEST"></span><span id="error_evt_filter_invtest"></span>**ERROR\_EVT\_FILTER\_INVTEST**
</dt> <dd> <dl> <dt>

15017 (0x3AA9)
</dt> <dt>



A step operation must involve either a node test or, in the case of a predicate, an algebraic expression against which to test each node in the node set identified by the preceeding node set can be evaluated.


</dt> </dl> </dd> <dt>

<span id="ERROR_EVT_FILTER_INVTYPE"></span><span id="error_evt_filter_invtype"></span>**ERROR\_EVT\_FILTER\_INVTYPE**
</dt> <dd> <dl> <dt>

15018 (0x3AAA)
</dt> <dt>



This data type is currently unsupported.


</dt> </dl> </dd> <dt>

<span id="ERROR_EVT_FILTER_PARSEERR"></span><span id="error_evt_filter_parseerr"></span>**ERROR\_EVT\_FILTER\_PARSEERR**
</dt> <dd> <dl> <dt>

15019 (0x3AAB)
</dt> <dt>



A syntax error occurred at position %1!d!.


</dt> </dl> </dd> <dt>

<span id="ERROR_EVT_FILTER_UNSUPPORTEDOP"></span><span id="error_evt_filter_unsupportedop"></span>**ERROR\_EVT\_FILTER\_UNSUPPORTEDOP**
</dt> <dd> <dl> <dt>

15020 (0x3AAC)
</dt> <dt>



This operator is unsupported by this implementation of the filter.


</dt> </dl> </dd> <dt>

<span id="ERROR_EVT_FILTER_UNEXPECTEDTOKEN"></span><span id="error_evt_filter_unexpectedtoken"></span>**ERROR\_EVT\_FILTER\_UNEXPECTEDTOKEN**
</dt> <dd> <dl> <dt>

15021 (0x3AAD)
</dt> <dt>



The token encountered was unexpected.


</dt> </dl> </dd> <dt>

<span id="ERROR_EVT_INVALID_OPERATION_OVER_ENABLED_DIRECT_CHANNEL"></span><span id="error_evt_invalid_operation_over_enabled_direct_channel"></span>**ERROR\_EVT\_INVALID\_OPERATION\_OVER\_ENABLED\_DIRECT\_CHANNEL**
</dt> <dd> <dl> <dt>

15022 (0x3AAE)
</dt> <dt>



The requested operation cannot be performed over an enabled direct channel. The channel must first be disabled before performing the requested operation.


</dt> </dl> </dd> <dt>

<span id="ERROR_EVT_INVALID_CHANNEL_PROPERTY_VALUE"></span><span id="error_evt_invalid_channel_property_value"></span>**ERROR\_EVT\_INVALID\_CHANNEL\_PROPERTY\_VALUE**
</dt> <dd> <dl> <dt>

15023 (0x3AAF)
</dt> <dt>



Channel property %1!s! contains invalid value. The value has invalid type, is outside of valid range, can't be updated or is not supported by this type of channel.


</dt> </dl> </dd> <dt>

<span id="ERROR_EVT_INVALID_PUBLISHER_PROPERTY_VALUE"></span><span id="error_evt_invalid_publisher_property_value"></span>**ERROR\_EVT\_INVALID\_PUBLISHER\_PROPERTY\_VALUE**
</dt> <dd> <dl> <dt>

15024 (0x3AB0)
</dt> <dt>



Publisher property %1!s! contains invalid value. The value has invalid type, is outside of valid range, can't be updated or is not supported by this type of publisher.


</dt> </dl> </dd> <dt>

<span id="ERROR_EVT_CHANNEL_CANNOT_ACTIVATE"></span><span id="error_evt_channel_cannot_activate"></span>**ERROR\_EVT\_CHANNEL\_CANNOT\_ACTIVATE**
</dt> <dd> <dl> <dt>

15025 (0x3AB1)
</dt> <dt>



The channel fails to activate.


</dt> </dl> </dd> <dt>

<span id="ERROR_EVT_FILTER_TOO_COMPLEX"></span><span id="error_evt_filter_too_complex"></span>**ERROR\_EVT\_FILTER\_TOO\_COMPLEX**
</dt> <dd> <dl> <dt>

15026 (0x3AB2)
</dt> <dt>



The xpath expression exceeded supported complexity. Please symplify it or split it into two or more simple expressions.


</dt> </dl> </dd> <dt>

<span id="ERROR_EVT_MESSAGE_NOT_FOUND"></span><span id="error_evt_message_not_found"></span>**ERROR\_EVT\_MESSAGE\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

15027 (0x3AB3)
</dt> <dt>



the message resource is present but the message is not found in the string/message table.


</dt> </dl> </dd> <dt>

<span id="ERROR_EVT_MESSAGE_ID_NOT_FOUND"></span><span id="error_evt_message_id_not_found"></span>**ERROR\_EVT\_MESSAGE\_ID\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

15028 (0x3AB4)
</dt> <dt>



The message id for the desired message could not be found.


</dt> </dl> </dd> <dt>

<span id="ERROR_EVT_UNRESOLVED_VALUE_INSERT"></span><span id="error_evt_unresolved_value_insert"></span>**ERROR\_EVT\_UNRESOLVED\_VALUE\_INSERT**
</dt> <dd> <dl> <dt>

15029 (0x3AB5)
</dt> <dt>



The substitution string for insert index (%1) could not be found.


</dt> </dl> </dd> <dt>

<span id="ERROR_EVT_UNRESOLVED_PARAMETER_INSERT"></span><span id="error_evt_unresolved_parameter_insert"></span>**ERROR\_EVT\_UNRESOLVED\_PARAMETER\_INSERT**
</dt> <dd> <dl> <dt>

15030 (0x3AB6)
</dt> <dt>



The description string for parameter reference (%1) could not be found.


</dt> </dl> </dd> <dt>

<span id="ERROR_EVT_MAX_INSERTS_REACHED"></span><span id="error_evt_max_inserts_reached"></span>**ERROR\_EVT\_MAX\_INSERTS\_REACHED**
</dt> <dd> <dl> <dt>

15031 (0x3AB7)
</dt> <dt>



The maximum number of replacements has been reached.


</dt> </dl> </dd> <dt>

<span id="ERROR_EVT_EVENT_DEFINITION_NOT_FOUND"></span><span id="error_evt_event_definition_not_found"></span>**ERROR\_EVT\_EVENT\_DEFINITION\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

15032 (0x3AB8)
</dt> <dt>



The event definition could not be found for event id (%1).


</dt> </dl> </dd> <dt>

<span id="ERROR_EVT_MESSAGE_LOCALE_NOT_FOUND"></span><span id="error_evt_message_locale_not_found"></span>**ERROR\_EVT\_MESSAGE\_LOCALE\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

15033 (0x3AB9)
</dt> <dt>



The locale specific resource for the desired message is not present.


</dt> </dl> </dd> <dt>

<span id="ERROR_EVT_VERSION_TOO_OLD"></span><span id="error_evt_version_too_old"></span>**ERROR\_EVT\_VERSION\_TOO\_OLD**
</dt> <dd> <dl> <dt>

15034 (0x3ABA)
</dt> <dt>



The resource is too old to be compatible.


</dt> </dl> </dd> <dt>

<span id="ERROR_EVT_VERSION_TOO_NEW"></span><span id="error_evt_version_too_new"></span>**ERROR\_EVT\_VERSION\_TOO\_NEW**
</dt> <dd> <dl> <dt>

15035 (0x3ABB)
</dt> <dt>



The resource is too new to be compatible.


</dt> </dl> </dd> <dt>

<span id="ERROR_EVT_CANNOT_OPEN_CHANNEL_OF_QUERY"></span><span id="error_evt_cannot_open_channel_of_query"></span>**ERROR\_EVT\_CANNOT\_OPEN\_CHANNEL\_OF\_QUERY**
</dt> <dd> <dl> <dt>

15036 (0x3ABC)
</dt> <dt>



The channel at index %1!d! of the query can't be opened.


</dt> </dl> </dd> <dt>

<span id="ERROR_EVT_PUBLISHER_DISABLED"></span><span id="error_evt_publisher_disabled"></span>**ERROR\_EVT\_PUBLISHER\_DISABLED**
</dt> <dd> <dl> <dt>

15037 (0x3ABD)
</dt> <dt>



The publisher has been disabled and its resource is not available. This usually occurs when the publisher is in the process of being uninstalled or upgraded.


</dt> </dl> </dd> <dt>

<span id="ERROR_EVT_FILTER_OUT_OF_RANGE"></span><span id="error_evt_filter_out_of_range"></span>**ERROR\_EVT\_FILTER\_OUT\_OF\_RANGE**
</dt> <dd> <dl> <dt>

15038 (0x3ABE)
</dt> <dt>



Attempted to create a numeric type that is outside of its valid range.


</dt> </dl> </dd> <dt>

<span id="ERROR_EC_SUBSCRIPTION_CANNOT_ACTIVATE"></span><span id="error_ec_subscription_cannot_activate"></span>**ERROR\_EC\_SUBSCRIPTION\_CANNOT\_ACTIVATE**
</dt> <dd> <dl> <dt>

15080 (0x3AE8)
</dt> <dt>



The subscription fails to activate.


</dt> </dl> </dd> <dt>

<span id="ERROR_EC_LOG_DISABLED"></span><span id="error_ec_log_disabled"></span>**ERROR\_EC\_LOG\_DISABLED**
</dt> <dd> <dl> <dt>

15081 (0x3AE9)
</dt> <dt>



The log of the subscription is in disabled state, and can not be used to forward events to. The log must first be enabled before the subscription can be activated.


</dt> </dl> </dd> <dt>

<span id="ERROR_EC_CIRCULAR_FORWARDING"></span><span id="error_ec_circular_forwarding"></span>**ERROR\_EC\_CIRCULAR\_FORWARDING**
</dt> <dd> <dl> <dt>

15082 (0x3AEA)
</dt> <dt>



When forwarding events from local machine to itself, the query of the subscription can't contain target log of the subscription.


</dt> </dl> </dd> <dt>

<span id="ERROR_EC_CREDSTORE_FULL"></span><span id="error_ec_credstore_full"></span>**ERROR\_EC\_CREDSTORE\_FULL**
</dt> <dd> <dl> <dt>

15083 (0x3AEB)
</dt> <dt>



The credential store that is used to save credentials is full.


</dt> </dl> </dd> <dt>

<span id="ERROR_EC_CRED_NOT_FOUND"></span><span id="error_ec_cred_not_found"></span>**ERROR\_EC\_CRED\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

15084 (0x3AEC)
</dt> <dt>



The credential used by this subscription can't be found in credential store.


</dt> </dl> </dd> <dt>

<span id="ERROR_EC_NO_ACTIVE_CHANNEL"></span><span id="error_ec_no_active_channel"></span>**ERROR\_EC\_NO\_ACTIVE\_CHANNEL**
</dt> <dd> <dl> <dt>

15085 (0x3AED)
</dt> <dt>



No active channel is found for the query.


</dt> </dl> </dd> <dt>

<span id="ERROR_MUI_FILE_NOT_FOUND"></span><span id="error_mui_file_not_found"></span>**ERROR\_MUI\_FILE\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

15100 (0x3AFC)
</dt> <dt>



The resource loader failed to find MUI file.


</dt> </dl> </dd> <dt>

<span id="ERROR_MUI_INVALID_FILE"></span><span id="error_mui_invalid_file"></span>**ERROR\_MUI\_INVALID\_FILE**
</dt> <dd> <dl> <dt>

15101 (0x3AFD)
</dt> <dt>



The resource loader failed to load MUI file because the file fail to pass validation.


</dt> </dl> </dd> <dt>

<span id="ERROR_MUI_INVALID_RC_CONFIG"></span><span id="error_mui_invalid_rc_config"></span>**ERROR\_MUI\_INVALID\_RC\_CONFIG**
</dt> <dd> <dl> <dt>

15102 (0x3AFE)
</dt> <dt>



The RC Manifest is corrupted with garbage data or unsupported version or missing required item.


</dt> </dl> </dd> <dt>

<span id="ERROR_MUI_INVALID_LOCALE_NAME"></span><span id="error_mui_invalid_locale_name"></span>**ERROR\_MUI\_INVALID\_LOCALE\_NAME**
</dt> <dd> <dl> <dt>

15103 (0x3AFF)
</dt> <dt>



The RC Manifest has invalid culture name.


</dt> </dl> </dd> <dt>

<span id="ERROR_MUI_INVALID_ULTIMATEFALLBACK_NAME"></span><span id="error_mui_invalid_ultimatefallback_name"></span>**ERROR\_MUI\_INVALID\_ULTIMATEFALLBACK\_NAME**
</dt> <dd> <dl> <dt>

15104 (0x3B00)
</dt> <dt>



The RC Manifest has invalid ultimatefallback name.


</dt> </dl> </dd> <dt>

<span id="ERROR_MUI_FILE_NOT_LOADED"></span><span id="error_mui_file_not_loaded"></span>**ERROR\_MUI\_FILE\_NOT\_LOADED**
</dt> <dd> <dl> <dt>

15105 (0x3B01)
</dt> <dt>



The resource loader cache doesn't have loaded MUI entry.


</dt> </dl> </dd> <dt>

<span id="ERROR_RESOURCE_ENUM_USER_STOP"></span><span id="error_resource_enum_user_stop"></span>**ERROR\_RESOURCE\_ENUM\_USER\_STOP**
</dt> <dd> <dl> <dt>

15106 (0x3B02)
</dt> <dt>



User stopped resource enumeration.


</dt> </dl> </dd> <dt>

<span id="ERROR_MUI_INTLSETTINGS_UILANG_NOT_INSTALLED"></span><span id="error_mui_intlsettings_uilang_not_installed"></span>**ERROR\_MUI\_INTLSETTINGS\_UILANG\_NOT\_INSTALLED**
</dt> <dd> <dl> <dt>

15107 (0x3B03)
</dt> <dt>



UI language installation failed.


</dt> </dl> </dd> <dt>

<span id="ERROR_MUI_INTLSETTINGS_INVALID_LOCALE_NAME"></span><span id="error_mui_intlsettings_invalid_locale_name"></span>**ERROR\_MUI\_INTLSETTINGS\_INVALID\_LOCALE\_NAME**
</dt> <dd> <dl> <dt>

15108 (0x3B04)
</dt> <dt>



Locale installation failed.


</dt> </dl> </dd> <dt>

<span id="ERROR_MRM_RUNTIME_NO_DEFAULT_OR_NEUTRAL_RESOURCE"></span><span id="error_mrm_runtime_no_default_or_neutral_resource"></span>**ERROR\_MRM\_RUNTIME\_NO\_DEFAULT\_OR\_NEUTRAL\_RESOURCE**
</dt> <dd> <dl> <dt>

15110 (0x3B06)
</dt> <dt>



A resource does not have default or neutral value.


</dt> </dl> </dd> <dt>

<span id="ERROR_MRM_INVALID_PRICONFIG"></span><span id="error_mrm_invalid_priconfig"></span>**ERROR\_MRM\_INVALID\_PRICONFIG**
</dt> <dd> <dl> <dt>

15111 (0x3B07)
</dt> <dt>



Invalid PRI config file.


</dt> </dl> </dd> <dt>

<span id="ERROR_MRM_INVALID_FILE_TYPE"></span><span id="error_mrm_invalid_file_type"></span>**ERROR\_MRM\_INVALID\_FILE\_TYPE**
</dt> <dd> <dl> <dt>

15112 (0x3B08)
</dt> <dt>



Invalid file type.


</dt> </dl> </dd> <dt>

<span id="ERROR_MRM_UNKNOWN_QUALIFIER"></span><span id="error_mrm_unknown_qualifier"></span>**ERROR\_MRM\_UNKNOWN\_QUALIFIER**
</dt> <dd> <dl> <dt>

15113 (0x3B09)
</dt> <dt>



Unknown qualifier.


</dt> </dl> </dd> <dt>

<span id="ERROR_MRM_INVALID_QUALIFIER_VALUE"></span><span id="error_mrm_invalid_qualifier_value"></span>**ERROR\_MRM\_INVALID\_QUALIFIER\_VALUE**
</dt> <dd> <dl> <dt>

15114 (0x3B0A)
</dt> <dt>



Invalid qualifier value.


</dt> </dl> </dd> <dt>

<span id="ERROR_MRM_NO_CANDIDATE"></span><span id="error_mrm_no_candidate"></span>**ERROR\_MRM\_NO\_CANDIDATE**
</dt> <dd> <dl> <dt>

15115 (0x3B0B)
</dt> <dt>



No Candidate found.


</dt> </dl> </dd> <dt>

<span id="ERROR_MRM_NO_MATCH_OR_DEFAULT_CANDIDATE"></span><span id="error_mrm_no_match_or_default_candidate"></span>**ERROR\_MRM\_NO\_MATCH\_OR\_DEFAULT\_CANDIDATE**
</dt> <dd> <dl> <dt>

15116 (0x3B0C)
</dt> <dt>



The ResourceMap or NamedResource has an item that does not have default or neutral resource..


</dt> </dl> </dd> <dt>

<span id="ERROR_MRM_RESOURCE_TYPE_MISMATCH"></span><span id="error_mrm_resource_type_mismatch"></span>**ERROR\_MRM\_RESOURCE\_TYPE\_MISMATCH**
</dt> <dd> <dl> <dt>

15117 (0x3B0D)
</dt> <dt>



Invalid ResourceCandidate type.


</dt> </dl> </dd> <dt>

<span id="ERROR_MRM_DUPLICATE_MAP_NAME"></span><span id="error_mrm_duplicate_map_name"></span>**ERROR\_MRM\_DUPLICATE\_MAP\_NAME**
</dt> <dd> <dl> <dt>

15118 (0x3B0E)
</dt> <dt>



Duplicate Resource Map.


</dt> </dl> </dd> <dt>

<span id="ERROR_MRM_DUPLICATE_ENTRY"></span><span id="error_mrm_duplicate_entry"></span>**ERROR\_MRM\_DUPLICATE\_ENTRY**
</dt> <dd> <dl> <dt>

15119 (0x3B0F)
</dt> <dt>



Duplicate Entry.


</dt> </dl> </dd> <dt>

<span id="ERROR_MRM_INVALID_RESOURCE_IDENTIFIER"></span><span id="error_mrm_invalid_resource_identifier"></span>**ERROR\_MRM\_INVALID\_RESOURCE\_IDENTIFIER**
</dt> <dd> <dl> <dt>

15120 (0x3B10)
</dt> <dt>



Invalid Resource Identifier.


</dt> </dl> </dd> <dt>

<span id="ERROR_MRM_FILEPATH_TOO_LONG"></span><span id="error_mrm_filepath_too_long"></span>**ERROR\_MRM\_FILEPATH\_TOO\_LONG**
</dt> <dd> <dl> <dt>

15121 (0x3B11)
</dt> <dt>



Filepath too long.


</dt> </dl> </dd> <dt>

<span id="ERROR_MRM_UNSUPPORTED_DIRECTORY_TYPE"></span><span id="error_mrm_unsupported_directory_type"></span>**ERROR\_MRM\_UNSUPPORTED\_DIRECTORY\_TYPE**
</dt> <dd> <dl> <dt>

15122 (0x3B12)
</dt> <dt>



Unsupported directory type.


</dt> </dl> </dd> <dt>

<span id="ERROR_MRM_INVALID_PRI_FILE"></span><span id="error_mrm_invalid_pri_file"></span>**ERROR\_MRM\_INVALID\_PRI\_FILE**
</dt> <dd> <dl> <dt>

15126 (0x3B16)
</dt> <dt>



Invalid PRI File.


</dt> </dl> </dd> <dt>

<span id="ERROR_MRM_NAMED_RESOURCE_NOT_FOUND"></span><span id="error_mrm_named_resource_not_found"></span>**ERROR\_MRM\_NAMED\_RESOURCE\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

15127 (0x3B17)
</dt> <dt>



NamedResource Not Found.


</dt> </dl> </dd> <dt>

<span id="ERROR_MRM_MAP_NOT_FOUND"></span><span id="error_mrm_map_not_found"></span>**ERROR\_MRM\_MAP\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

15135 (0x3B1F)
</dt> <dt>



ResourceMap Not Found.


</dt> </dl> </dd> <dt>

<span id="ERROR_MRM_UNSUPPORTED_PROFILE_TYPE"></span><span id="error_mrm_unsupported_profile_type"></span>**ERROR\_MRM\_UNSUPPORTED\_PROFILE\_TYPE**
</dt> <dd> <dl> <dt>

15136 (0x3B20)
</dt> <dt>



Unsupported MRT profile type.


</dt> </dl> </dd> <dt>

<span id="ERROR_MRM_INVALID_QUALIFIER_OPERATOR"></span><span id="error_mrm_invalid_qualifier_operator"></span>**ERROR\_MRM\_INVALID\_QUALIFIER\_OPERATOR**
</dt> <dd> <dl> <dt>

15137 (0x3B21)
</dt> <dt>



Invalid qualifier operator.


</dt> </dl> </dd> <dt>

<span id="ERROR_MRM_INDETERMINATE_QUALIFIER_VALUE"></span><span id="error_mrm_indeterminate_qualifier_value"></span>**ERROR\_MRM\_INDETERMINATE\_QUALIFIER\_VALUE**
</dt> <dd> <dl> <dt>

15138 (0x3B22)
</dt> <dt>



Unable to determine qualifier value or qualifier value has not been set.


</dt> </dl> </dd> <dt>

<span id="ERROR_MRM_AUTOMERGE_ENABLED"></span><span id="error_mrm_automerge_enabled"></span>**ERROR\_MRM\_AUTOMERGE\_ENABLED**
</dt> <dd> <dl> <dt>

15139 (0x3B23)
</dt> <dt>



Automerge is enabled in the PRI file.


</dt> </dl> </dd> <dt>

<span id="ERROR_MRM_TOO_MANY_RESOURCES"></span><span id="error_mrm_too_many_resources"></span>**ERROR\_MRM\_TOO\_MANY\_RESOURCES**
</dt> <dd> <dl> <dt>

15140 (0x3B24)
</dt> <dt>



Too many resources defined for package.


</dt> </dl> </dd> <dt>

<span id="ERROR_MCA_INVALID_CAPABILITIES_STRING"></span><span id="error_mca_invalid_capabilities_string"></span>**ERROR\_MCA\_INVALID\_CAPABILITIES\_STRING**
</dt> <dd> <dl> <dt>

15200 (0x3B60)
</dt> <dt>



The monitor returned a DDC/CI capabilities string that did not comply with the ACCESS.bus 3.0, DDC/CI 1.1 or MCCS 2 Revision 1 specification.


</dt> </dl> </dd> <dt>

<span id="ERROR_MCA_INVALID_VCP_VERSION"></span><span id="error_mca_invalid_vcp_version"></span>**ERROR\_MCA\_INVALID\_VCP\_VERSION**
</dt> <dd> <dl> <dt>

15201 (0x3B61)
</dt> <dt>



The monitor's VCP Version (0xDF) VCP code returned an invalid version value.


</dt> </dl> </dd> <dt>

<span id="ERROR_MCA_MONITOR_VIOLATES_MCCS_SPECIFICATION"></span><span id="error_mca_monitor_violates_mccs_specification"></span>**ERROR\_MCA\_MONITOR\_VIOLATES\_MCCS\_SPECIFICATION**
</dt> <dd> <dl> <dt>

15202 (0x3B62)
</dt> <dt>



The monitor does not comply with the MCCS specification it claims to support.


</dt> </dl> </dd> <dt>

<span id="ERROR_MCA_MCCS_VERSION_MISMATCH"></span><span id="error_mca_mccs_version_mismatch"></span>**ERROR\_MCA\_MCCS\_VERSION\_MISMATCH**
</dt> <dd> <dl> <dt>

15203 (0x3B63)
</dt> <dt>



The MCCS version in a monitor's mccs\_ver capability does not match the MCCS version the monitor reports when the VCP Version (0xDF) VCP code is used.


</dt> </dl> </dd> <dt>

<span id="ERROR_MCA_UNSUPPORTED_MCCS_VERSION"></span><span id="error_mca_unsupported_mccs_version"></span>**ERROR\_MCA\_UNSUPPORTED\_MCCS\_VERSION**
</dt> <dd> <dl> <dt>

15204 (0x3B64)
</dt> <dt>



The Monitor Configuration API only works with monitors that support the MCCS 1.0 specification, MCCS 2.0 specification or the MCCS 2.0 Revision 1 specification.


</dt> </dl> </dd> <dt>

<span id="ERROR_MCA_INTERNAL_ERROR"></span><span id="error_mca_internal_error"></span>**ERROR\_MCA\_INTERNAL\_ERROR**
</dt> <dd> <dl> <dt>

15205 (0x3B65)
</dt> <dt>



An internal Monitor Configuration API error occurred.


</dt> </dl> </dd> <dt>

<span id="ERROR_MCA_INVALID_TECHNOLOGY_TYPE_RETURNED"></span><span id="error_mca_invalid_technology_type_returned"></span>**ERROR\_MCA\_INVALID\_TECHNOLOGY\_TYPE\_RETURNED**
</dt> <dd> <dl> <dt>

15206 (0x3B66)
</dt> <dt>



The monitor returned an invalid monitor technology type. CRT, Plasma and LCD (TFT) are examples of monitor technology types. This error implies that the monitor violated the MCCS 2.0 or MCCS 2.0 Revision 1 specification.


</dt> </dl> </dd> <dt>

<span id="ERROR_MCA_UNSUPPORTED_COLOR_TEMPERATURE"></span><span id="error_mca_unsupported_color_temperature"></span>**ERROR\_MCA\_UNSUPPORTED\_COLOR\_TEMPERATURE**
</dt> <dd> <dl> <dt>

15207 (0x3B67)
</dt> <dt>



The caller of [**SetMonitorColorTemperature**](/windows/win32/api/highlevelmonitorconfigurationapi/nf-highlevelmonitorconfigurationapi-setmonitorcolortemperature) specified a color temperature that the current monitor did not support. This error implies that the monitor violated the MCCS 2.0 or MCCS 2.0 Revision 1 specification.


</dt> </dl> </dd> <dt>

<span id="ERROR_AMBIGUOUS_SYSTEM_DEVICE"></span><span id="error_ambiguous_system_device"></span>**ERROR\_AMBIGUOUS\_SYSTEM\_DEVICE**
</dt> <dd> <dl> <dt>

15250 (0x3B92)
</dt> <dt>



The requested system device cannot be identified due to multiple indistinguishable devices potentially matching the identification criteria.


</dt> </dl> </dd> <dt>

<span id="ERROR_SYSTEM_DEVICE_NOT_FOUND"></span><span id="error_system_device_not_found"></span>**ERROR\_SYSTEM\_DEVICE\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

15299 (0x3BC3)
</dt> <dt>



The requested system device cannot be found.


</dt> </dl> </dd> <dt>

<span id="ERROR_HASH_NOT_SUPPORTED"></span><span id="error_hash_not_supported"></span>**ERROR\_HASH\_NOT\_SUPPORTED**
</dt> <dd> <dl> <dt>

15300 (0x3BC4)
</dt> <dt>



Hash generation for the specified hash version and hash type is not enabled on the server.


</dt> </dl> </dd> <dt>

<span id="ERROR_HASH_NOT_PRESENT"></span><span id="error_hash_not_present"></span>**ERROR\_HASH\_NOT\_PRESENT**
</dt> <dd> <dl> <dt>

15301 (0x3BC5)
</dt> <dt>



The hash requested from the server is not available or no longer valid.


</dt> </dl> </dd> <dt>

<span id="ERROR_SECONDARY_IC_PROVIDER_NOT_REGISTERED"></span><span id="error_secondary_ic_provider_not_registered"></span>**ERROR\_SECONDARY\_IC\_PROVIDER\_NOT\_REGISTERED**
</dt> <dd> <dl> <dt>

15321 (0x3BD9)
</dt> <dt>



The secondary interrupt controller instance that manages the specified interrupt is not registered.


</dt> </dl> </dd> <dt>

<span id="ERROR_GPIO_CLIENT_INFORMATION_INVALID"></span><span id="error_gpio_client_information_invalid"></span>**ERROR\_GPIO\_CLIENT\_INFORMATION\_INVALID**
</dt> <dd> <dl> <dt>

15322 (0x3BDA)
</dt> <dt>



The information supplied by the GPIO client driver is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_GPIO_VERSION_NOT_SUPPORTED"></span><span id="error_gpio_version_not_supported"></span>**ERROR\_GPIO\_VERSION\_NOT\_SUPPORTED**
</dt> <dd> <dl> <dt>

15323 (0x3BDB)
</dt> <dt>



The version specified by the GPIO client driver is not supported.


</dt> </dl> </dd> <dt>

<span id="ERROR_GPIO_INVALID_REGISTRATION_PACKET"></span><span id="error_gpio_invalid_registration_packet"></span>**ERROR\_GPIO\_INVALID\_REGISTRATION\_PACKET**
</dt> <dd> <dl> <dt>

15324 (0x3BDC)
</dt> <dt>



The registration packet supplied by the GPIO client driver is not valid.


</dt> </dl> </dd> <dt>

<span id="ERROR_GPIO_OPERATION_DENIED"></span><span id="error_gpio_operation_denied"></span>**ERROR\_GPIO\_OPERATION\_DENIED**
</dt> <dd> <dl> <dt>

15325 (0x3BDD)
</dt> <dt>



The requested operation is not supported for the specified handle.


</dt> </dl> </dd> <dt>

<span id="ERROR_GPIO_INCOMPATIBLE_CONNECT_MODE"></span><span id="error_gpio_incompatible_connect_mode"></span>**ERROR\_GPIO\_INCOMPATIBLE\_CONNECT\_MODE**
</dt> <dd> <dl> <dt>

15326 (0x3BDE)
</dt> <dt>



The requested connect mode conflicts with an existing mode on one or more of the specified pins.


</dt> </dl> </dd> <dt>

<span id="ERROR_GPIO_INTERRUPT_ALREADY_UNMASKED"></span><span id="error_gpio_interrupt_already_unmasked"></span>**ERROR\_GPIO\_INTERRUPT\_ALREADY\_UNMASKED**
</dt> <dd> <dl> <dt>

15327 (0x3BDF)
</dt> <dt>



The interrupt requested to be unmasked is not masked.


</dt> </dl> </dd> <dt>

<span id="ERROR_CANNOT_SWITCH_RUNLEVEL"></span><span id="error_cannot_switch_runlevel"></span>**ERROR\_CANNOT\_SWITCH\_RUNLEVEL**
</dt> <dd> <dl> <dt>

15400 (0x3C28)
</dt> <dt>



The requested run level switch cannot be completed successfully.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_RUNLEVEL_SETTING"></span><span id="error_invalid_runlevel_setting"></span>**ERROR\_INVALID\_RUNLEVEL\_SETTING**
</dt> <dd> <dl> <dt>

15401 (0x3C29)
</dt> <dt>



The service has an invalid run level setting. The run level for a service must not be higher than the run level of its dependent services.


</dt> </dl> </dd> <dt>

<span id="ERROR_RUNLEVEL_SWITCH_TIMEOUT"></span><span id="error_runlevel_switch_timeout"></span>**ERROR\_RUNLEVEL\_SWITCH\_TIMEOUT**
</dt> <dd> <dl> <dt>

15402 (0x3C2A)
</dt> <dt>



The requested run level switch cannot be completed successfully since one or more services will not stop or restart within the specified timeout.


</dt> </dl> </dd> <dt>

<span id="ERROR_RUNLEVEL_SWITCH_AGENT_TIMEOUT"></span><span id="error_runlevel_switch_agent_timeout"></span>**ERROR\_RUNLEVEL\_SWITCH\_AGENT\_TIMEOUT**
</dt> <dd> <dl> <dt>

15403 (0x3C2B)
</dt> <dt>



A run level switch agent did not respond within the specified timeout.


</dt> </dl> </dd> <dt>

<span id="ERROR_RUNLEVEL_SWITCH_IN_PROGRESS"></span><span id="error_runlevel_switch_in_progress"></span>**ERROR\_RUNLEVEL\_SWITCH\_IN\_PROGRESS**
</dt> <dd> <dl> <dt>

15404 (0x3C2C)
</dt> <dt>



A run level switch is currently in progress.


</dt> </dl> </dd> <dt>

<span id="ERROR_SERVICES_FAILED_AUTOSTART"></span><span id="error_services_failed_autostart"></span>**ERROR\_SERVICES\_FAILED\_AUTOSTART**
</dt> <dd> <dl> <dt>

15405 (0x3C2D)
</dt> <dt>



One or more services failed to start during the service startup phase of a run level switch.


</dt> </dl> </dd> <dt>

<span id="ERROR_COM_TASK_STOP_PENDING"></span><span id="error_com_task_stop_pending"></span>**ERROR\_COM\_TASK\_STOP\_PENDING**
</dt> <dd> <dl> <dt>

15501 (0x3C8D)
</dt> <dt>



The task stop request cannot be completed immediately since task needs more time to shutdown.


</dt> </dl> </dd> <dt>

<span id="ERROR_INSTALL_OPEN_PACKAGE_FAILED"></span><span id="error_install_open_package_failed"></span>**ERROR\_INSTALL\_OPEN\_PACKAGE\_FAILED**
</dt> <dd> <dl> <dt>

15600 (0x3CF0)
</dt> <dt>



Package could not be opened.


</dt> </dl> </dd> <dt>

<span id="ERROR_INSTALL_PACKAGE_NOT_FOUND"></span><span id="error_install_package_not_found"></span>**ERROR\_INSTALL\_PACKAGE\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

15601 (0x3CF1)
</dt> <dt>



Package was not found.


</dt> </dl> </dd> <dt>

<span id="ERROR_INSTALL_INVALID_PACKAGE"></span><span id="error_install_invalid_package"></span>**ERROR\_INSTALL\_INVALID\_PACKAGE**
</dt> <dd> <dl> <dt>

15602 (0x3CF2)
</dt> <dt>



Package data is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_INSTALL_RESOLVE_DEPENDENCY_FAILED"></span><span id="error_install_resolve_dependency_failed"></span>**ERROR\_INSTALL\_RESOLVE\_DEPENDENCY\_FAILED**
</dt> <dd> <dl> <dt>

15603 (0x3CF3)
</dt> <dt>



Package failed updates, dependency or conflict validation.


</dt> </dl> </dd> <dt>

<span id="ERROR_INSTALL_OUT_OF_DISK_SPACE"></span><span id="error_install_out_of_disk_space"></span>**ERROR\_INSTALL\_OUT\_OF\_DISK\_SPACE**
</dt> <dd> <dl> <dt>

15604 (0x3CF4)
</dt> <dt>



There is not enough disk space on your computer. Please free up some space and try again.


</dt> </dl> </dd> <dt>

<span id="ERROR_INSTALL_NETWORK_FAILURE"></span><span id="error_install_network_failure"></span>**ERROR\_INSTALL\_NETWORK\_FAILURE**
</dt> <dd> <dl> <dt>

15605 (0x3CF5)
</dt> <dt>



There was a problem downloading your product.


</dt> </dl> </dd> <dt>

<span id="ERROR_INSTALL_REGISTRATION_FAILURE"></span><span id="error_install_registration_failure"></span>**ERROR\_INSTALL\_REGISTRATION\_FAILURE**
</dt> <dd> <dl> <dt>

15606 (0x3CF6)
</dt> <dt>



Package could not be registered.


</dt> </dl> </dd> <dt>

<span id="ERROR_INSTALL_DEREGISTRATION_FAILURE"></span><span id="error_install_deregistration_failure"></span>**ERROR\_INSTALL\_DEREGISTRATION\_FAILURE**
</dt> <dd> <dl> <dt>

15607 (0x3CF7)
</dt> <dt>



Package could not be unregistered.


</dt> </dl> </dd> <dt>

<span id="ERROR_INSTALL_CANCEL"></span><span id="error_install_cancel"></span>**ERROR\_INSTALL\_CANCEL**
</dt> <dd> <dl> <dt>

15608 (0x3CF8)
</dt> <dt>



User cancelled the install request.


</dt> </dl> </dd> <dt>

<span id="ERROR_INSTALL_FAILED"></span><span id="error_install_failed"></span>**ERROR\_INSTALL\_FAILED**
</dt> <dd> <dl> <dt>

15609 (0x3CF9)
</dt> <dt>



Install failed. Please contact your software vendor.


</dt> </dl> </dd> <dt>

<span id="ERROR_REMOVE_FAILED"></span><span id="error_remove_failed"></span>**ERROR\_REMOVE\_FAILED**
</dt> <dd> <dl> <dt>

15610 (0x3CFA)
</dt> <dt>



Removal failed. Please contact your software vendor.


</dt> </dl> </dd> <dt>

<span id="ERROR_PACKAGE_ALREADY_EXISTS"></span><span id="error_package_already_exists"></span>**ERROR\_PACKAGE\_ALREADY\_EXISTS**
</dt> <dd> <dl> <dt>

15611 (0x3CFB)
</dt> <dt>



The provided package is already installed, and reinstallation of the package was blocked. Check the AppXDeployment-Server event log for details.


</dt> </dl> </dd> <dt>

<span id="ERROR_NEEDS_REMEDIATION"></span><span id="error_needs_remediation"></span>**ERROR\_NEEDS\_REMEDIATION**
</dt> <dd> <dl> <dt>

15612 (0x3CFC)
</dt> <dt>



The application cannot be started. Try reinstalling the application to fix the problem.


</dt> </dl> </dd> <dt>

<span id="ERROR_INSTALL_PREREQUISITE_FAILED"></span><span id="error_install_prerequisite_failed"></span>**ERROR\_INSTALL\_PREREQUISITE\_FAILED**
</dt> <dd> <dl> <dt>

15613 (0x3CFD)
</dt> <dt>



A Prerequisite for an install could not be satisfied.


</dt> </dl> </dd> <dt>

<span id="ERROR_PACKAGE_REPOSITORY_CORRUPTED"></span><span id="error_package_repository_corrupted"></span>**ERROR\_PACKAGE\_REPOSITORY\_CORRUPTED**
</dt> <dd> <dl> <dt>

15614 (0x3CFE)
</dt> <dt>



The package repository is corrupted.


</dt> </dl> </dd> <dt>

<span id="ERROR_INSTALL_POLICY_FAILURE"></span><span id="error_install_policy_failure"></span>**ERROR\_INSTALL\_POLICY\_FAILURE**
</dt> <dd> <dl> <dt>

15615 (0x3CFF)
</dt> <dt>



To install this application you need either a Windows developer license or a sideloading-enabled system.


</dt> </dl> </dd> <dt>

<span id="ERROR_PACKAGE_UPDATING"></span><span id="error_package_updating"></span>**ERROR\_PACKAGE\_UPDATING**
</dt> <dd> <dl> <dt>

15616 (0x3D00)
</dt> <dt>



The application cannot be started because it is currently updating.


</dt> </dl> </dd> <dt>

<span id="ERROR_DEPLOYMENT_BLOCKED_BY_POLICY"></span><span id="error_deployment_blocked_by_policy"></span>**ERROR\_DEPLOYMENT\_BLOCKED\_BY\_POLICY**
</dt> <dd> <dl> <dt>

15617 (0x3D01)
</dt> <dt>



The package deployment operation is blocked by policy. Please contact your system administrator.


</dt> </dl> </dd> <dt>

<span id="ERROR_PACKAGES_IN_USE"></span><span id="error_packages_in_use"></span>**ERROR\_PACKAGES\_IN\_USE**
</dt> <dd> <dl> <dt>

15618 (0x3D02)
</dt> <dt>



The package could not be installed because resources it modifies are currently in use.


</dt> </dl> </dd> <dt>

<span id="ERROR_RECOVERY_FILE_CORRUPT"></span><span id="error_recovery_file_corrupt"></span>**ERROR\_RECOVERY\_FILE\_CORRUPT**
</dt> <dd> <dl> <dt>

15619 (0x3D03)
</dt> <dt>



The package could not be recovered because necessary data for recovery have been corrupted.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_STAGED_SIGNATURE"></span><span id="error_invalid_staged_signature"></span>**ERROR\_INVALID\_STAGED\_SIGNATURE**
</dt> <dd> <dl> <dt>

15620 (0x3D04)
</dt> <dt>



The signature is invalid. To register in developer mode, AppxSignature.p7x and AppxBlockMap.xml must be valid or should not be present.


</dt> </dl> </dd> <dt>

<span id="ERROR_DELETING_EXISTING_APPLICATIONDATA_STORE_FAILED"></span><span id="error_deleting_existing_applicationdata_store_failed"></span>**ERROR\_DELETING\_EXISTING\_APPLICATIONDATA\_STORE\_FAILED**
</dt> <dd> <dl> <dt>

15621 (0x3D05)
</dt> <dt>



An error occurred while deleting the package's previously existing application data.


</dt> </dl> </dd> <dt>

<span id="ERROR_INSTALL_PACKAGE_DOWNGRADE"></span><span id="error_install_package_downgrade"></span>**ERROR\_INSTALL\_PACKAGE\_DOWNGRADE**
</dt> <dd> <dl> <dt>

15622 (0x3D06)
</dt> <dt>



The package could not be installed because a higher version of this package is already installed.


</dt> </dl> </dd> <dt>

<span id="ERROR_SYSTEM_NEEDS_REMEDIATION"></span><span id="error_system_needs_remediation"></span>**ERROR\_SYSTEM\_NEEDS\_REMEDIATION**
</dt> <dd> <dl> <dt>

15623 (0x3D07)
</dt> <dt>



An error in a system binary was detected. Try refreshing the PC to fix the problem.


</dt> </dl> </dd> <dt>

<span id="ERROR_APPX_INTEGRITY_FAILURE_CLR_NGEN"></span><span id="error_appx_integrity_failure_clr_ngen"></span>**ERROR\_APPX\_INTEGRITY\_FAILURE\_CLR\_NGEN**
</dt> <dd> <dl> <dt>

15624 (0x3D08)
</dt> <dt>



A corrupted CLR NGEN binary was detected on the system.


</dt> </dl> </dd> <dt>

<span id="ERROR_RESILIENCY_FILE_CORRUPT"></span><span id="error_resiliency_file_corrupt"></span>**ERROR\_RESILIENCY\_FILE\_CORRUPT**
</dt> <dd> <dl> <dt>

15625 (0x3D09)
</dt> <dt>



The operation could not be resumed because necessary data for recovery have been corrupted.


</dt> </dl> </dd> <dt>

<span id="ERROR_INSTALL_FIREWALL_SERVICE_NOT_RUNNING"></span><span id="error_install_firewall_service_not_running"></span>**ERROR\_INSTALL\_FIREWALL\_SERVICE\_NOT\_RUNNING**
</dt> <dd> <dl> <dt>

15626 (0x3D0A)
</dt> <dt>



The package could not be installed because the Windows Firewall service is not running. Enable the Windows Firewall service and try again.


</dt> </dl> </dd> <dt>

<span id="APPMODEL_ERROR_NO_PACKAGE"></span><span id="appmodel_error_no_package"></span>**APPMODEL\_ERROR\_NO\_PACKAGE**
</dt> <dd> <dl> <dt>

15700 (0x3D54)
</dt> <dt>



The process has no package identity.


</dt> </dl> </dd> <dt>

<span id="APPMODEL_ERROR_PACKAGE_RUNTIME_CORRUPT"></span><span id="appmodel_error_package_runtime_corrupt"></span>**APPMODEL\_ERROR\_PACKAGE\_RUNTIME\_CORRUPT**
</dt> <dd> <dl> <dt>

15701 (0x3D55)
</dt> <dt>



The package runtime information is corrupted.


</dt> </dl> </dd> <dt>

<span id="APPMODEL_ERROR_PACKAGE_IDENTITY_CORRUPT"></span><span id="appmodel_error_package_identity_corrupt"></span>**APPMODEL\_ERROR\_PACKAGE\_IDENTITY\_CORRUPT**
</dt> <dd> <dl> <dt>

15702 (0x3D56)
</dt> <dt>



The package identity is corrupted.


</dt> </dl> </dd> <dt>

<span id="APPMODEL_ERROR_NO_APPLICATION"></span><span id="appmodel_error_no_application"></span>**APPMODEL\_ERROR\_NO\_APPLICATION**
</dt> <dd> <dl> <dt>

15703 (0x3D57)
</dt> <dt>



The process has no application identity.


</dt> </dl> </dd> <dt>

<span id="ERROR_STATE_LOAD_STORE_FAILED"></span><span id="error_state_load_store_failed"></span>**ERROR\_STATE\_LOAD\_STORE\_FAILED**
</dt> <dd> <dl> <dt>

15800 (0x3DB8)
</dt> <dt>



Loading the state store failed.


</dt> </dl> </dd> <dt>

<span id="ERROR_STATE_GET_VERSION_FAILED"></span><span id="error_state_get_version_failed"></span>**ERROR\_STATE\_GET\_VERSION\_FAILED**
</dt> <dd> <dl> <dt>

15801 (0x3DB9)
</dt> <dt>



Retrieving the state version for the application failed.


</dt> </dl> </dd> <dt>

<span id="ERROR_STATE_SET_VERSION_FAILED"></span><span id="error_state_set_version_failed"></span>**ERROR\_STATE\_SET\_VERSION\_FAILED**
</dt> <dd> <dl> <dt>

15802 (0x3DBA)
</dt> <dt>



Setting the state version for the application failed.


</dt> </dl> </dd> <dt>

<span id="ERROR_STATE_STRUCTURED_RESET_FAILED"></span><span id="error_state_structured_reset_failed"></span>**ERROR\_STATE\_STRUCTURED\_RESET\_FAILED**
</dt> <dd> <dl> <dt>

15803 (0x3DBB)
</dt> <dt>



Resetting the structured state of the application failed.


</dt> </dl> </dd> <dt>

<span id="ERROR_STATE_OPEN_CONTAINER_FAILED"></span><span id="error_state_open_container_failed"></span>**ERROR\_STATE\_OPEN\_CONTAINER\_FAILED**
</dt> <dd> <dl> <dt>

15804 (0x3DBC)
</dt> <dt>



State Manager failed to open the container.


</dt> </dl> </dd> <dt>

<span id="ERROR_STATE_CREATE_CONTAINER_FAILED"></span><span id="error_state_create_container_failed"></span>**ERROR\_STATE\_CREATE\_CONTAINER\_FAILED**
</dt> <dd> <dl> <dt>

15805 (0x3DBD)
</dt> <dt>



State Manager failed to create the container.


</dt> </dl> </dd> <dt>

<span id="ERROR_STATE_DELETE_CONTAINER_FAILED"></span><span id="error_state_delete_container_failed"></span>**ERROR\_STATE\_DELETE\_CONTAINER\_FAILED**
</dt> <dd> <dl> <dt>

15806 (0x3DBE)
</dt> <dt>



State Manager failed to delete the container.


</dt> </dl> </dd> <dt>

<span id="ERROR_STATE_READ_SETTING_FAILED"></span><span id="error_state_read_setting_failed"></span>**ERROR\_STATE\_READ\_SETTING\_FAILED**
</dt> <dd> <dl> <dt>

15807 (0x3DBF)
</dt> <dt>



State Manager failed to read the setting.


</dt> </dl> </dd> <dt>

<span id="ERROR_STATE_WRITE_SETTING_FAILED"></span><span id="error_state_write_setting_failed"></span>**ERROR\_STATE\_WRITE\_SETTING\_FAILED**
</dt> <dd> <dl> <dt>

15808 (0x3DC0)
</dt> <dt>



State Manager failed to write the setting.


</dt> </dl> </dd> <dt>

<span id="ERROR_STATE_DELETE_SETTING_FAILED"></span><span id="error_state_delete_setting_failed"></span>**ERROR\_STATE\_DELETE\_SETTING\_FAILED**
</dt> <dd> <dl> <dt>

15809 (0x3DC1)
</dt> <dt>



State Manager failed to delete the setting.


</dt> </dl> </dd> <dt>

<span id="ERROR_STATE_QUERY_SETTING_FAILED"></span><span id="error_state_query_setting_failed"></span>**ERROR\_STATE\_QUERY\_SETTING\_FAILED**
</dt> <dd> <dl> <dt>

15810 (0x3DC2)
</dt> <dt>



State Manager failed to query the setting.


</dt> </dl> </dd> <dt>

<span id="ERROR_STATE_READ_COMPOSITE_SETTING_FAILED"></span><span id="error_state_read_composite_setting_failed"></span>**ERROR\_STATE\_READ\_COMPOSITE\_SETTING\_FAILED**
</dt> <dd> <dl> <dt>

15811 (0x3DC3)
</dt> <dt>



State Manager failed to read the composite setting.


</dt> </dl> </dd> <dt>

<span id="ERROR_STATE_WRITE_COMPOSITE_SETTING_FAILED"></span><span id="error_state_write_composite_setting_failed"></span>**ERROR\_STATE\_WRITE\_COMPOSITE\_SETTING\_FAILED**
</dt> <dd> <dl> <dt>

15812 (0x3DC4)
</dt> <dt>



State Manager failed to write the composite setting.


</dt> </dl> </dd> <dt>

<span id="ERROR_STATE_ENUMERATE_CONTAINER_FAILED"></span><span id="error_state_enumerate_container_failed"></span>**ERROR\_STATE\_ENUMERATE\_CONTAINER\_FAILED**
</dt> <dd> <dl> <dt>

15813 (0x3DC5)
</dt> <dt>



State Manager failed to enumerate the containers.


</dt> </dl> </dd> <dt>

<span id="ERROR_STATE_ENUMERATE_SETTINGS_FAILED"></span><span id="error_state_enumerate_settings_failed"></span>**ERROR\_STATE\_ENUMERATE\_SETTINGS\_FAILED**
</dt> <dd> <dl> <dt>

15814 (0x3DC6)
</dt> <dt>



State Manager failed to enumerate the settings.


</dt> </dl> </dd> <dt>

<span id="ERROR_STATE_COMPOSITE_SETTING_VALUE_SIZE_LIMIT_EXCEEDED"></span><span id="error_state_composite_setting_value_size_limit_exceeded"></span>**ERROR\_STATE\_COMPOSITE\_SETTING\_VALUE\_SIZE\_LIMIT\_EXCEEDED**
</dt> <dd> <dl> <dt>

15815 (0x3DC7)
</dt> <dt>



The size of the state manager composite setting value has exceeded the limit.


</dt> </dl> </dd> <dt>

<span id="ERROR_STATE_SETTING_VALUE_SIZE_LIMIT_EXCEEDED"></span><span id="error_state_setting_value_size_limit_exceeded"></span>**ERROR\_STATE\_SETTING\_VALUE\_SIZE\_LIMIT\_EXCEEDED**
</dt> <dd> <dl> <dt>

15816 (0x3DC8)
</dt> <dt>



The size of the state manager setting value has exceeded the limit.


</dt> </dl> </dd> <dt>

<span id="ERROR_STATE_SETTING_NAME_SIZE_LIMIT_EXCEEDED"></span><span id="error_state_setting_name_size_limit_exceeded"></span>**ERROR\_STATE\_SETTING\_NAME\_SIZE\_LIMIT\_EXCEEDED**
</dt> <dd> <dl> <dt>

15817 (0x3DC9)
</dt> <dt>



The length of the state manager setting name has exceeded the limit.


</dt> </dl> </dd> <dt>

<span id="ERROR_STATE_CONTAINER_NAME_SIZE_LIMIT_EXCEEDED"></span><span id="error_state_container_name_size_limit_exceeded"></span>**ERROR\_STATE\_CONTAINER\_NAME\_SIZE\_LIMIT\_EXCEEDED**
</dt> <dd> <dl> <dt>

15818 (0x3DCA)
</dt> <dt>



The length of the state manager container name has exceeded the limit.


</dt> </dl> </dd> <dt>

<span id="ERROR_API_UNAVAILABLE"></span><span id="error_api_unavailable"></span>**ERROR\_API\_UNAVAILABLE**
</dt> <dd> <dl> <dt>

15841 (0x3DE1)
</dt> <dt>



This API cannot be used in the context of the caller's application type.


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

 

 
