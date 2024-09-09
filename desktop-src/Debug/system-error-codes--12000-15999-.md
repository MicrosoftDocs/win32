---
description: Describes error codes 12000-1599 defined in the WinError.h header file and is intended for developers.
ms.assetid: bb3c658d-96db-495a-a0dc-e93949c3835d
title: System Error Codes (12000-15999) (WinError.h)
ms.topic: reference
ms.date: 07/15/2024
---

# System Error Codes (12000-15999)

The following list describes [system error codes](system-error-codes.md) (errors 12000 to 15999). They are returned by the [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) function when many functions fail. To retrieve the description text for the error in your application, use the [**FormatMessage**](/windows/desktop/api/WinBase/nf-winbase-formatmessage) function with the **FORMAT\_MESSAGE\_FROM\_SYSTEM** flag.

> [!NOTE]
> This information is intended for developers debugging system errors. For other errors, such as issues with Windows Update, see the list of resources on the [Error codes](system-error-codes.md) page.

 

<span id="ERROR_INTERNET__"></span><span id="error_internet__"></span>**ERROR\_INTERNET\_\***
   

12000 - 12175 (0x2EE0)
 



See [Internet Error Codes](../wininet/wininet-errors.md) and WinInet.h.


   

<span id="ERROR_WINHTTP__"></span><span id="error_winhttp__"></span>**ERROR\_WINHTTP\_\***
   

12001 - 12184 (0x2EE1)
 



See [WinHTTP Error Codes](../winhttp/error-messages.md) and Winhttp.h.


   

<span id="ERROR_IPSEC_QM_POLICY_EXISTS"></span><span id="error_ipsec_qm_policy_exists"></span>**ERROR\_IPSEC\_QM\_POLICY\_EXISTS**
   

13000 (0x32C8)
 



The specified quick mode policy already exists.


   

<span id="ERROR_IPSEC_QM_POLICY_NOT_FOUND"></span><span id="error_ipsec_qm_policy_not_found"></span>**ERROR\_IPSEC\_QM\_POLICY\_NOT\_FOUND**
   

13001 (0x32C9)
 



The specified quick mode policy was not found.


   

<span id="ERROR_IPSEC_QM_POLICY_IN_USE"></span><span id="error_ipsec_qm_policy_in_use"></span>**ERROR\_IPSEC\_QM\_POLICY\_IN\_USE**
   

13002 (0x32CA)
 



The specified quick mode policy is being used.


   

<span id="ERROR_IPSEC_MM_POLICY_EXISTS"></span><span id="error_ipsec_mm_policy_exists"></span>**ERROR\_IPSEC\_MM\_POLICY\_EXISTS**
   

13003 (0x32CB)
 



The specified main mode policy already exists.


   

<span id="ERROR_IPSEC_MM_POLICY_NOT_FOUND"></span><span id="error_ipsec_mm_policy_not_found"></span>**ERROR\_IPSEC\_MM\_POLICY\_NOT\_FOUND**
   

13004 (0x32CC)
 



The specified main mode policy was not found.


   

<span id="ERROR_IPSEC_MM_POLICY_IN_USE"></span><span id="error_ipsec_mm_policy_in_use"></span>**ERROR\_IPSEC\_MM\_POLICY\_IN\_USE**
   

13005 (0x32CD)
 



The specified main mode policy is being used.


   

<span id="ERROR_IPSEC_MM_FILTER_EXISTS"></span><span id="error_ipsec_mm_filter_exists"></span>**ERROR\_IPSEC\_MM\_FILTER\_EXISTS**
   

13006 (0x32CE)
 



The specified main mode filter already exists.


   

<span id="ERROR_IPSEC_MM_FILTER_NOT_FOUND"></span><span id="error_ipsec_mm_filter_not_found"></span>**ERROR\_IPSEC\_MM\_FILTER\_NOT\_FOUND**
   

13007 (0x32CF)
 



The specified main mode filter was not found.


   

<span id="ERROR_IPSEC_TRANSPORT_FILTER_EXISTS"></span><span id="error_ipsec_transport_filter_exists"></span>**ERROR\_IPSEC\_TRANSPORT\_FILTER\_EXISTS**
   

13008 (0x32D0)
 



The specified transport mode filter already exists.


   

<span id="ERROR_IPSEC_TRANSPORT_FILTER_NOT_FOUND"></span><span id="error_ipsec_transport_filter_not_found"></span>**ERROR\_IPSEC\_TRANSPORT\_FILTER\_NOT\_FOUND**
   

13009 (0x32D1)
 



The specified transport mode filter does not exist.


   

<span id="ERROR_IPSEC_MM_AUTH_EXISTS"></span><span id="error_ipsec_mm_auth_exists"></span>**ERROR\_IPSEC\_MM\_AUTH\_EXISTS**
   

13010 (0x32D2)
 



The specified main mode authentication list exists.


   

<span id="ERROR_IPSEC_MM_AUTH_NOT_FOUND"></span><span id="error_ipsec_mm_auth_not_found"></span>**ERROR\_IPSEC\_MM\_AUTH\_NOT\_FOUND**
   

13011 (0x32D3)
 



The specified main mode authentication list was not found.


   

<span id="ERROR_IPSEC_MM_AUTH_IN_USE"></span><span id="error_ipsec_mm_auth_in_use"></span>**ERROR\_IPSEC\_MM\_AUTH\_IN\_USE**
   

13012 (0x32D4)
 



The specified main mode authentication list is being used.


   

<span id="ERROR_IPSEC_DEFAULT_MM_POLICY_NOT_FOUND"></span><span id="error_ipsec_default_mm_policy_not_found"></span>**ERROR\_IPSEC\_DEFAULT\_MM\_POLICY\_NOT\_FOUND**
   

13013 (0x32D5)
 



The specified default main mode policy was not found.


   

<span id="ERROR_IPSEC_DEFAULT_MM_AUTH_NOT_FOUND"></span><span id="error_ipsec_default_mm_auth_not_found"></span>**ERROR\_IPSEC\_DEFAULT\_MM\_AUTH\_NOT\_FOUND**
   

13014 (0x32D6)
 



The specified default main mode authentication list was not found.


   

<span id="ERROR_IPSEC_DEFAULT_QM_POLICY_NOT_FOUND"></span><span id="error_ipsec_default_qm_policy_not_found"></span>**ERROR\_IPSEC\_DEFAULT\_QM\_POLICY\_NOT\_FOUND**
   

13015 (0x32D7)
 



The specified default quick mode policy was not found.


   

<span id="ERROR_IPSEC_TUNNEL_FILTER_EXISTS"></span><span id="error_ipsec_tunnel_filter_exists"></span>**ERROR\_IPSEC\_TUNNEL\_FILTER\_EXISTS**
   

13016 (0x32D8)
 



The specified tunnel mode filter exists.


   

<span id="ERROR_IPSEC_TUNNEL_FILTER_NOT_FOUND"></span><span id="error_ipsec_tunnel_filter_not_found"></span>**ERROR\_IPSEC\_TUNNEL\_FILTER\_NOT\_FOUND**
   

13017 (0x32D9)
 



The specified tunnel mode filter was not found.


   

<span id="ERROR_IPSEC_MM_FILTER_PENDING_DELETION"></span><span id="error_ipsec_mm_filter_pending_deletion"></span>**ERROR\_IPSEC\_MM\_FILTER\_PENDING\_DELETION**
   

13018 (0x32DA)
 



The Main Mode filter is pending deletion.


   

<span id="ERROR_IPSEC_TRANSPORT_FILTER_PENDING_DELETION"></span><span id="error_ipsec_transport_filter_pending_deletion"></span>**ERROR\_IPSEC\_TRANSPORT\_FILTER\_PENDING\_DELETION**
   

13019 (0x32DB)
 



The transport filter is pending deletion.


   

<span id="ERROR_IPSEC_TUNNEL_FILTER_PENDING_DELETION"></span><span id="error_ipsec_tunnel_filter_pending_deletion"></span>**ERROR\_IPSEC\_TUNNEL\_FILTER\_PENDING\_DELETION**
   

13020 (0x32DC)
 



The tunnel filter is pending deletion.


   

<span id="ERROR_IPSEC_MM_POLICY_PENDING_DELETION"></span><span id="error_ipsec_mm_policy_pending_deletion"></span>**ERROR\_IPSEC\_MM\_POLICY\_PENDING\_DELETION**
   

13021 (0x32DD)
 



The Main Mode policy is pending deletion.


   

<span id="ERROR_IPSEC_MM_AUTH_PENDING_DELETION"></span><span id="error_ipsec_mm_auth_pending_deletion"></span>**ERROR\_IPSEC\_MM\_AUTH\_PENDING\_DELETION**
   

13022 (0x32DE)
 



The Main Mode authentication bundle is pending deletion.


   

<span id="ERROR_IPSEC_QM_POLICY_PENDING_DELETION"></span><span id="error_ipsec_qm_policy_pending_deletion"></span>**ERROR\_IPSEC\_QM\_POLICY\_PENDING\_DELETION**
   

13023 (0x32DF)
 



The Quick Mode policy is pending deletion.


   

<span id="WARNING_IPSEC_MM_POLICY_PRUNED"></span><span id="warning_ipsec_mm_policy_pruned"></span>**WARNING\_IPSEC\_MM\_POLICY\_PRUNED**
   

13024 (0x32E0)
 



The Main Mode policy was successfully added, but some of the requested offers are not supported.


   

<span id="WARNING_IPSEC_QM_POLICY_PRUNED"></span><span id="warning_ipsec_qm_policy_pruned"></span>**WARNING\_IPSEC\_QM\_POLICY\_PRUNED**
   

13025 (0x32E1)
 



The Quick Mode policy was successfully added, but some of the requested offers are not supported.


   

<span id="ERROR_IPSEC_IKE_NEG_STATUS_BEGIN"></span><span id="error_ipsec_ike_neg_status_begin"></span>**ERROR\_IPSEC\_IKE\_NEG\_STATUS\_BEGIN**
   

13800 (0x35E8)
 



ERROR\_IPSEC\_IKE\_NEG\_STATUS\_BEGIN


   

<span id="ERROR_IPSEC_IKE_AUTH_FAIL"></span><span id="error_ipsec_ike_auth_fail"></span>**ERROR\_IPSEC\_IKE\_AUTH\_FAIL**
   

13801 (0x35E9)
 



IKE authentication credentials are unacceptable.


   

<span id="ERROR_IPSEC_IKE_ATTRIB_FAIL"></span><span id="error_ipsec_ike_attrib_fail"></span>**ERROR\_IPSEC\_IKE\_ATTRIB\_FAIL**
   

13802 (0x35EA)
 



IKE security attributes are unacceptable.


   

<span id="ERROR_IPSEC_IKE_NEGOTIATION_PENDING"></span><span id="error_ipsec_ike_negotiation_pending"></span>**ERROR\_IPSEC\_IKE\_NEGOTIATION\_PENDING**
   

13803 (0x35EB)
 



IKE Negotiation in progress.


   

<span id="ERROR_IPSEC_IKE_GENERAL_PROCESSING_ERROR"></span><span id="error_ipsec_ike_general_processing_error"></span>**ERROR\_IPSEC\_IKE\_GENERAL\_PROCESSING\_ERROR**
   

13804 (0x35EC)
 



General processing error.


   

<span id="ERROR_IPSEC_IKE_TIMED_OUT"></span><span id="error_ipsec_ike_timed_out"></span>**ERROR\_IPSEC\_IKE\_TIMED\_OUT**
   

13805 (0x35ED)
 



Negotiation timed out.


   

<span id="ERROR_IPSEC_IKE_NO_CERT"></span><span id="error_ipsec_ike_no_cert"></span>**ERROR\_IPSEC\_IKE\_NO\_CERT**
   

13806 (0x35EE)
 



IKE failed to find valid machine certificate. Contact your Network Security Administrator about installing a valid certificate in the appropriate Certificate Store.


   

<span id="ERROR_IPSEC_IKE_SA_DELETED"></span><span id="error_ipsec_ike_sa_deleted"></span>**ERROR\_IPSEC\_IKE\_SA\_DELETED**
   

13807 (0x35EF)
 



IKE SA deleted by peer before establishment completed.


   

<span id="ERROR_IPSEC_IKE_SA_REAPED"></span><span id="error_ipsec_ike_sa_reaped"></span>**ERROR\_IPSEC\_IKE\_SA\_REAPED**
   

13808 (0x35F0)
 



IKE SA deleted before establishment completed.


   

<span id="ERROR_IPSEC_IKE_MM_ACQUIRE_DROP"></span><span id="error_ipsec_ike_mm_acquire_drop"></span>**ERROR\_IPSEC\_IKE\_MM\_ACQUIRE\_DROP**
   

13809 (0x35F1)
 



Negotiation request sat in Queue too long.


   

<span id="ERROR_IPSEC_IKE_QM_ACQUIRE_DROP"></span><span id="error_ipsec_ike_qm_acquire_drop"></span>**ERROR\_IPSEC\_IKE\_QM\_ACQUIRE\_DROP**
   

13810 (0x35F2)
 



Negotiation request sat in Queue too long.


   

<span id="ERROR_IPSEC_IKE_QUEUE_DROP_MM"></span><span id="error_ipsec_ike_queue_drop_mm"></span>**ERROR\_IPSEC\_IKE\_QUEUE\_DROP\_MM**
   

13811 (0x35F3)
 



Negotiation request sat in Queue too long.


   

<span id="ERROR_IPSEC_IKE_QUEUE_DROP_NO_MM"></span><span id="error_ipsec_ike_queue_drop_no_mm"></span>**ERROR\_IPSEC\_IKE\_QUEUE\_DROP\_NO\_MM**
   

13812 (0x35F4)
 



Negotiation request sat in Queue too long.


   

<span id="ERROR_IPSEC_IKE_DROP_NO_RESPONSE"></span><span id="error_ipsec_ike_drop_no_response"></span>**ERROR\_IPSEC\_IKE\_DROP\_NO\_RESPONSE**
   

13813 (0x35F5)
 



No response from peer.


   

<span id="ERROR_IPSEC_IKE_MM_DELAY_DROP"></span><span id="error_ipsec_ike_mm_delay_drop"></span>**ERROR\_IPSEC\_IKE\_MM\_DELAY\_DROP**
   

13814 (0x35F6)
 



Negotiation took too long.


   

<span id="ERROR_IPSEC_IKE_QM_DELAY_DROP"></span><span id="error_ipsec_ike_qm_delay_drop"></span>**ERROR\_IPSEC\_IKE\_QM\_DELAY\_DROP**
   

13815 (0x35F7)
 



Negotiation took too long.


   

<span id="ERROR_IPSEC_IKE_ERROR"></span><span id="error_ipsec_ike_error"></span>**ERROR\_IPSEC\_IKE\_ERROR**
   

13816 (0x35F8)
 



Unknown error occurred.


   

<span id="ERROR_IPSEC_IKE_CRL_FAILED"></span><span id="error_ipsec_ike_crl_failed"></span>**ERROR\_IPSEC\_IKE\_CRL\_FAILED**
   

13817 (0x35F9)
 



Certificate Revocation Check failed.


   

<span id="ERROR_IPSEC_IKE_INVALID_KEY_USAGE"></span><span id="error_ipsec_ike_invalid_key_usage"></span>**ERROR\_IPSEC\_IKE\_INVALID\_KEY\_USAGE**
   

13818 (0x35FA)
 



Invalid certificate key usage.


   

<span id="ERROR_IPSEC_IKE_INVALID_CERT_TYPE"></span><span id="error_ipsec_ike_invalid_cert_type"></span>**ERROR\_IPSEC\_IKE\_INVALID\_CERT\_TYPE**
   

13819 (0x35FB)
 



Invalid certificate type.


   

<span id="ERROR_IPSEC_IKE_NO_PRIVATE_KEY"></span><span id="error_ipsec_ike_no_private_key"></span>**ERROR\_IPSEC\_IKE\_NO\_PRIVATE\_KEY**
   

13820 (0x35FC)
 



IKE negotiation failed because the machine certificate used does not have a private key. IPsec certificates require a private key. Contact your Network Security administrator about replacing with a certificate that has a private key.


   

<span id="ERROR_IPSEC_IKE_SIMULTANEOUS_REKEY"></span><span id="error_ipsec_ike_simultaneous_rekey"></span>**ERROR\_IPSEC\_IKE\_SIMULTANEOUS\_REKEY**
   

13821 (0x35FD)
 



Simultaneous rekeys were detected.


   

<span id="ERROR_IPSEC_IKE_DH_FAIL"></span><span id="error_ipsec_ike_dh_fail"></span>**ERROR\_IPSEC\_IKE\_DH\_FAIL**
   

13822 (0x35FE)
 



Failure in Diffie-Hellman computation.


   

<span id="ERROR_IPSEC_IKE_CRITICAL_PAYLOAD_NOT_RECOGNIZED"></span><span id="error_ipsec_ike_critical_payload_not_recognized"></span>**ERROR\_IPSEC\_IKE\_CRITICAL\_PAYLOAD\_NOT\_RECOGNIZED**
   

13823 (0x35FF)
 



Don't know how to process critical payload.


   

<span id="ERROR_IPSEC_IKE_INVALID_HEADER"></span><span id="error_ipsec_ike_invalid_header"></span>**ERROR\_IPSEC\_IKE\_INVALID\_HEADER**
   

13824 (0x3600)
 



Invalid header.


   

<span id="ERROR_IPSEC_IKE_NO_POLICY"></span><span id="error_ipsec_ike_no_policy"></span>**ERROR\_IPSEC\_IKE\_NO\_POLICY**
   

13825 (0x3601)
 



No policy configured.


   

<span id="ERROR_IPSEC_IKE_INVALID_SIGNATURE"></span><span id="error_ipsec_ike_invalid_signature"></span>**ERROR\_IPSEC\_IKE\_INVALID\_SIGNATURE**
   

13826 (0x3602)
 



Failed to verify signature.


   

<span id="ERROR_IPSEC_IKE_KERBEROS_ERROR"></span><span id="error_ipsec_ike_kerberos_error"></span>**ERROR\_IPSEC\_IKE\_KERBEROS\_ERROR**
   

13827 (0x3603)
 



Failed to authenticate using Kerberos.


   

<span id="ERROR_IPSEC_IKE_NO_PUBLIC_KEY"></span><span id="error_ipsec_ike_no_public_key"></span>**ERROR\_IPSEC\_IKE\_NO\_PUBLIC\_KEY**
   

13828 (0x3604)
 



Peer's certificate did not have a public key.


   

<span id="ERROR_IPSEC_IKE_PROCESS_ERR"></span><span id="error_ipsec_ike_process_err"></span>**ERROR\_IPSEC\_IKE\_PROCESS\_ERR**
   

13829 (0x3605)
 



Error processing error payload.


   

<span id="ERROR_IPSEC_IKE_PROCESS_ERR_SA"></span><span id="error_ipsec_ike_process_err_sa"></span>**ERROR\_IPSEC\_IKE\_PROCESS\_ERR\_SA**
   

13830 (0x3606)
 



Error processing SA payload.


   

<span id="ERROR_IPSEC_IKE_PROCESS_ERR_PROP"></span><span id="error_ipsec_ike_process_err_prop"></span>**ERROR\_IPSEC\_IKE\_PROCESS\_ERR\_PROP**
   

13831 (0x3607)
 



Error processing Proposal payload.


   

<span id="ERROR_IPSEC_IKE_PROCESS_ERR_TRANS"></span><span id="error_ipsec_ike_process_err_trans"></span>**ERROR\_IPSEC\_IKE\_PROCESS\_ERR\_TRANS**
   

13832 (0x3608)
 



Error processing Transform payload.


   

<span id="ERROR_IPSEC_IKE_PROCESS_ERR_KE"></span><span id="error_ipsec_ike_process_err_ke"></span>**ERROR\_IPSEC\_IKE\_PROCESS\_ERR\_KE**
   

13833 (0x3609)
 



Error processing KE payload.


   

<span id="ERROR_IPSEC_IKE_PROCESS_ERR_ID"></span><span id="error_ipsec_ike_process_err_id"></span>**ERROR\_IPSEC\_IKE\_PROCESS\_ERR\_ID**
   

13834 (0x360A)
 



Error processing ID payload.


   

<span id="ERROR_IPSEC_IKE_PROCESS_ERR_CERT"></span><span id="error_ipsec_ike_process_err_cert"></span>**ERROR\_IPSEC\_IKE\_PROCESS\_ERR\_CERT**
   

13835 (0x360B)
 



Error processing Cert payload.


   

<span id="ERROR_IPSEC_IKE_PROCESS_ERR_CERT_REQ"></span><span id="error_ipsec_ike_process_err_cert_req"></span>**ERROR\_IPSEC\_IKE\_PROCESS\_ERR\_CERT\_REQ**
   

13836 (0x360C)
 



Error processing Certificate Request payload.


   

<span id="ERROR_IPSEC_IKE_PROCESS_ERR_HASH"></span><span id="error_ipsec_ike_process_err_hash"></span>**ERROR\_IPSEC\_IKE\_PROCESS\_ERR\_HASH**
   

13837 (0x360D)
 



Error processing Hash payload.


   

<span id="ERROR_IPSEC_IKE_PROCESS_ERR_SIG"></span><span id="error_ipsec_ike_process_err_sig"></span>**ERROR\_IPSEC\_IKE\_PROCESS\_ERR\_SIG**
   

13838 (0x360E)
 



Error processing Signature payload.


   

<span id="ERROR_IPSEC_IKE_PROCESS_ERR_NONCE"></span><span id="error_ipsec_ike_process_err_nonce"></span>**ERROR\_IPSEC\_IKE\_PROCESS\_ERR\_NONCE**
   

13839 (0x360F)
 



Error processing Nonce payload.


   

<span id="ERROR_IPSEC_IKE_PROCESS_ERR_NOTIFY"></span><span id="error_ipsec_ike_process_err_notify"></span>**ERROR\_IPSEC\_IKE\_PROCESS\_ERR\_NOTIFY**
   

13840 (0x3610)
 



Error processing Notify payload.


   

<span id="ERROR_IPSEC_IKE_PROCESS_ERR_DELETE"></span><span id="error_ipsec_ike_process_err_delete"></span>**ERROR\_IPSEC\_IKE\_PROCESS\_ERR\_DELETE**
   

13841 (0x3611)
 



Error processing Delete Payload.


   

<span id="ERROR_IPSEC_IKE_PROCESS_ERR_VENDOR"></span><span id="error_ipsec_ike_process_err_vendor"></span>**ERROR\_IPSEC\_IKE\_PROCESS\_ERR\_VENDOR**
   

13842 (0x3612)
 



Error processing VendorId payload.


   

<span id="ERROR_IPSEC_IKE_INVALID_PAYLOAD"></span><span id="error_ipsec_ike_invalid_payload"></span>**ERROR\_IPSEC\_IKE\_INVALID\_PAYLOAD**
   

13843 (0x3613)
 



Invalid payload received.


   

<span id="ERROR_IPSEC_IKE_LOAD_SOFT_SA"></span><span id="error_ipsec_ike_load_soft_sa"></span>**ERROR\_IPSEC\_IKE\_LOAD\_SOFT\_SA**
   

13844 (0x3614)
 



Soft SA loaded.


   

<span id="ERROR_IPSEC_IKE_SOFT_SA_TORN_DOWN"></span><span id="error_ipsec_ike_soft_sa_torn_down"></span>**ERROR\_IPSEC\_IKE\_SOFT\_SA\_TORN\_DOWN**
   

13845 (0x3615)
 



Soft SA torn down.


   

<span id="ERROR_IPSEC_IKE_INVALID_COOKIE"></span><span id="error_ipsec_ike_invalid_cookie"></span>**ERROR\_IPSEC\_IKE\_INVALID\_COOKIE**
   

13846 (0x3616)
 



Invalid cookie received.


   

<span id="ERROR_IPSEC_IKE_NO_PEER_CERT"></span><span id="error_ipsec_ike_no_peer_cert"></span>**ERROR\_IPSEC\_IKE\_NO\_PEER\_CERT**
   

13847 (0x3617)
 



Peer failed to send valid machine certificate.


   

<span id="ERROR_IPSEC_IKE_PEER_CRL_FAILED"></span><span id="error_ipsec_ike_peer_crl_failed"></span>**ERROR\_IPSEC\_IKE\_PEER\_CRL\_FAILED**
   

13848 (0x3618)
 



Certification Revocation check of peer's certificate failed.


   

<span id="ERROR_IPSEC_IKE_POLICY_CHANGE"></span><span id="error_ipsec_ike_policy_change"></span>**ERROR\_IPSEC\_IKE\_POLICY\_CHANGE**
   

13849 (0x3619)
 



New policy invalidated SAs formed with old policy.


   

<span id="ERROR_IPSEC_IKE_NO_MM_POLICY"></span><span id="error_ipsec_ike_no_mm_policy"></span>**ERROR\_IPSEC\_IKE\_NO\_MM\_POLICY**
   

13850 (0x361A)
 



There is no available Main Mode IKE policy.


   

<span id="ERROR_IPSEC_IKE_NOTCBPRIV"></span><span id="error_ipsec_ike_notcbpriv"></span>**ERROR\_IPSEC\_IKE\_NOTCBPRIV**
   

13851 (0x361B)
 



Failed to enabled TCB privilege.


   

<span id="ERROR_IPSEC_IKE_SECLOADFAIL"></span><span id="error_ipsec_ike_secloadfail"></span>**ERROR\_IPSEC\_IKE\_SECLOADFAIL**
   

13852 (0x361C)
 



Failed to load SECURITY.DLL.


   

<span id="ERROR_IPSEC_IKE_FAILSSPINIT"></span><span id="error_ipsec_ike_failsspinit"></span>**ERROR\_IPSEC\_IKE\_FAILSSPINIT**
   

13853 (0x361D)
 



Failed to obtain security function table dispatch address from SSPI.


   

<span id="ERROR_IPSEC_IKE_FAILQUERYSSP"></span><span id="error_ipsec_ike_failqueryssp"></span>**ERROR\_IPSEC\_IKE\_FAILQUERYSSP**
   

13854 (0x361E)
 



Failed to query Kerberos package to obtain max token size.


   

<span id="ERROR_IPSEC_IKE_SRVACQFAIL"></span><span id="error_ipsec_ike_srvacqfail"></span>**ERROR\_IPSEC\_IKE\_SRVACQFAIL**
   

13855 (0x361F)
 



Failed to obtain Kerberos server credentials for ISAKMP/ERROR\_IPSEC\_IKE service. Kerberos authentication will not function. The most likely reason for this is lack of domain membership. This is normal if your computer is a member of a workgroup.


   

<span id="ERROR_IPSEC_IKE_SRVQUERYCRED"></span><span id="error_ipsec_ike_srvquerycred"></span>**ERROR\_IPSEC\_IKE\_SRVQUERYCRED**
   

13856 (0x3620)
 



Failed to determine SSPI principal name for ISAKMP/ERROR\_IPSEC\_IKE service ([**QueryCredentialsAttributes**](/windows/win32/api/sspi/nf-sspi-querycredentialsattributesa)).


   

<span id="ERROR_IPSEC_IKE_GETSPIFAIL"></span><span id="error_ipsec_ike_getspifail"></span>**ERROR\_IPSEC\_IKE\_GETSPIFAIL**
   

13857 (0x3621)
 



Failed to obtain new SPI for the inbound SA from IPsec driver. The most common cause for this is that the driver does not have the correct filter. Check your policy to verify the filters.


   

<span id="ERROR_IPSEC_IKE_INVALID_FILTER"></span><span id="error_ipsec_ike_invalid_filter"></span>**ERROR\_IPSEC\_IKE\_INVALID\_FILTER**
   

13858 (0x3622)
 



Given filter is invalid.


   

<span id="ERROR_IPSEC_IKE_OUT_OF_MEMORY"></span><span id="error_ipsec_ike_out_of_memory"></span>**ERROR\_IPSEC\_IKE\_OUT\_OF\_MEMORY**
   

13859 (0x3623)
 



Memory allocation failed.


   

<span id="ERROR_IPSEC_IKE_ADD_UPDATE_KEY_FAILED"></span><span id="error_ipsec_ike_add_update_key_failed"></span>**ERROR\_IPSEC\_IKE\_ADD\_UPDATE\_KEY\_FAILED**
   

13860 (0x3624)
 



Failed to add Security Association to IPsec Driver. The most common cause for this is if the IKE negotiation took too long to complete. If the problem persists, reduce the load on the faulting machine.


   

<span id="ERROR_IPSEC_IKE_INVALID_POLICY"></span><span id="error_ipsec_ike_invalid_policy"></span>**ERROR\_IPSEC\_IKE\_INVALID\_POLICY**
   

13861 (0x3625)
 



Invalid policy.


   

<span id="ERROR_IPSEC_IKE_UNKNOWN_DOI"></span><span id="error_ipsec_ike_unknown_doi"></span>**ERROR\_IPSEC\_IKE\_UNKNOWN\_DOI**
   

13862 (0x3626)
 



Invalid DOI.


   

<span id="ERROR_IPSEC_IKE_INVALID_SITUATION"></span><span id="error_ipsec_ike_invalid_situation"></span>**ERROR\_IPSEC\_IKE\_INVALID\_SITUATION**
   

13863 (0x3627)
 



Invalid situation.


   

<span id="ERROR_IPSEC_IKE_DH_FAILURE"></span><span id="error_ipsec_ike_dh_failure"></span>**ERROR\_IPSEC\_IKE\_DH\_FAILURE**
   

13864 (0x3628)
 



Diffie-Hellman failure.


   

<span id="ERROR_IPSEC_IKE_INVALID_GROUP"></span><span id="error_ipsec_ike_invalid_group"></span>**ERROR\_IPSEC\_IKE\_INVALID\_GROUP**
   

13865 (0x3629)
 



Invalid Diffie-Hellman group.


   

<span id="ERROR_IPSEC_IKE_ENCRYPT"></span><span id="error_ipsec_ike_encrypt"></span>**ERROR\_IPSEC\_IKE\_ENCRYPT**
   

13866 (0x362A)
 



Error encrypting payload.


   

<span id="ERROR_IPSEC_IKE_DECRYPT"></span><span id="error_ipsec_ike_decrypt"></span>**ERROR\_IPSEC\_IKE\_DECRYPT**
   

13867 (0x362B)
 



Error decrypting payload.


   

<span id="ERROR_IPSEC_IKE_POLICY_MATCH"></span><span id="error_ipsec_ike_policy_match"></span>**ERROR\_IPSEC\_IKE\_POLICY\_MATCH**
   

13868 (0x362C)
 



Policy match error.


   

<span id="ERROR_IPSEC_IKE_UNSUPPORTED_ID"></span><span id="error_ipsec_ike_unsupported_id"></span>**ERROR\_IPSEC\_IKE\_UNSUPPORTED\_ID**
   

13869 (0x362D)
 



Unsupported ID.


   

<span id="ERROR_IPSEC_IKE_INVALID_HASH"></span><span id="error_ipsec_ike_invalid_hash"></span>**ERROR\_IPSEC\_IKE\_INVALID\_HASH**
   

13870 (0x362E)
 



Hash verification failed.


   

<span id="ERROR_IPSEC_IKE_INVALID_HASH_ALG"></span><span id="error_ipsec_ike_invalid_hash_alg"></span>**ERROR\_IPSEC\_IKE\_INVALID\_HASH\_ALG**
   

13871 (0x362F)
 



Invalid hash algorithm.


   

<span id="ERROR_IPSEC_IKE_INVALID_HASH_SIZE"></span><span id="error_ipsec_ike_invalid_hash_size"></span>**ERROR\_IPSEC\_IKE\_INVALID\_HASH\_SIZE**
   

13872 (0x3630)
 



Invalid hash size.


   

<span id="ERROR_IPSEC_IKE_INVALID_ENCRYPT_ALG"></span><span id="error_ipsec_ike_invalid_encrypt_alg"></span>**ERROR\_IPSEC\_IKE\_INVALID\_ENCRYPT\_ALG**
   

13873 (0x3631)
 



Invalid encryption algorithm.


   

<span id="ERROR_IPSEC_IKE_INVALID_AUTH_ALG"></span><span id="error_ipsec_ike_invalid_auth_alg"></span>**ERROR\_IPSEC\_IKE\_INVALID\_AUTH\_ALG**
   

13874 (0x3632)
 



Invalid authentication algorithm.


   

<span id="ERROR_IPSEC_IKE_INVALID_SIG"></span><span id="error_ipsec_ike_invalid_sig"></span>**ERROR\_IPSEC\_IKE\_INVALID\_SIG**
   

13875 (0x3633)
 



Invalid certificate signature.


   

<span id="ERROR_IPSEC_IKE_LOAD_FAILED"></span><span id="error_ipsec_ike_load_failed"></span>**ERROR\_IPSEC\_IKE\_LOAD\_FAILED**
   

13876 (0x3634)
 



Load failed.


   

<span id="ERROR_IPSEC_IKE_RPC_DELETE"></span><span id="error_ipsec_ike_rpc_delete"></span>**ERROR\_IPSEC\_IKE\_RPC\_DELETE**
   

13877 (0x3635)
 



Deleted via RPC call.


   

<span id="ERROR_IPSEC_IKE_BENIGN_REINIT"></span><span id="error_ipsec_ike_benign_reinit"></span>**ERROR\_IPSEC\_IKE\_BENIGN\_REINIT**
   

13878 (0x3636)
 



Temporary state created to perform reinitialization. This is not a real failure.


   

<span id="ERROR_IPSEC_IKE_INVALID_RESPONDER_LIFETIME_NOTIFY"></span><span id="error_ipsec_ike_invalid_responder_lifetime_notify"></span>**ERROR\_IPSEC\_IKE\_INVALID\_RESPONDER\_LIFETIME\_NOTIFY**
   

13879 (0x3637)
 



The lifetime value received in the Responder Lifetime Notify is below the Windows 2000 configured minimum value. Please fix the policy on the peer machine.


   

<span id="ERROR_IPSEC_IKE_INVALID_MAJOR_VERSION"></span><span id="error_ipsec_ike_invalid_major_version"></span>**ERROR\_IPSEC\_IKE\_INVALID\_MAJOR\_VERSION**
   

13880 (0x3638)
 



The recipient cannot handle version of IKE specified in the header.


   

<span id="ERROR_IPSEC_IKE_INVALID_CERT_KEYLEN"></span><span id="error_ipsec_ike_invalid_cert_keylen"></span>**ERROR\_IPSEC\_IKE\_INVALID\_CERT\_KEYLEN**
   

13881 (0x3639)
 



Key length in certificate is too small for configured security requirements.


   

<span id="ERROR_IPSEC_IKE_MM_LIMIT"></span><span id="error_ipsec_ike_mm_limit"></span>**ERROR\_IPSEC\_IKE\_MM\_LIMIT**
   

13882 (0x363A)
 



Max number of established MM SAs to peer exceeded.


   

<span id="ERROR_IPSEC_IKE_NEGOTIATION_DISABLED"></span><span id="error_ipsec_ike_negotiation_disabled"></span>**ERROR\_IPSEC\_IKE\_NEGOTIATION\_DISABLED**
   

13883 (0x363B)
 



IKE received a policy that disables negotiation.


   

<span id="ERROR_IPSEC_IKE_QM_LIMIT"></span><span id="error_ipsec_ike_qm_limit"></span>**ERROR\_IPSEC\_IKE\_QM\_LIMIT**
   

13884 (0x363C)
 



Reached maximum quick mode limit for the main mode. New main mode will be started.


   

<span id="ERROR_IPSEC_IKE_MM_EXPIRED"></span><span id="error_ipsec_ike_mm_expired"></span>**ERROR\_IPSEC\_IKE\_MM\_EXPIRED**
   

13885 (0x363D)
 



Main mode SA lifetime expired or peer sent a main mode delete.


   

<span id="ERROR_IPSEC_IKE_PEER_MM_ASSUMED_INVALID"></span><span id="error_ipsec_ike_peer_mm_assumed_invalid"></span>**ERROR\_IPSEC\_IKE\_PEER\_MM\_ASSUMED\_INVALID**
   

13886 (0x363E)
 



Main mode SA assumed to be invalid because peer stopped responding.


   

<span id="ERROR_IPSEC_IKE_CERT_CHAIN_POLICY_MISMATCH"></span><span id="error_ipsec_ike_cert_chain_policy_mismatch"></span>**ERROR\_IPSEC\_IKE\_CERT\_CHAIN\_POLICY\_MISMATCH**
   

13887 (0x363F)
 



Certificate doesn't chain to a trusted root in IPsec policy.


   

<span id="ERROR_IPSEC_IKE_UNEXPECTED_MESSAGE_ID"></span><span id="error_ipsec_ike_unexpected_message_id"></span>**ERROR\_IPSEC\_IKE\_UNEXPECTED\_MESSAGE\_ID**
   

13888 (0x3640)
 



Received unexpected message ID.


   

<span id="ERROR_IPSEC_IKE_INVALID_AUTH_PAYLOAD"></span><span id="error_ipsec_ike_invalid_auth_payload"></span>**ERROR\_IPSEC\_IKE\_INVALID\_AUTH\_PAYLOAD**
   

13889 (0x3641)
 



Received invalid authentication offers.


   

<span id="ERROR_IPSEC_IKE_DOS_COOKIE_SENT"></span><span id="error_ipsec_ike_dos_cookie_sent"></span>**ERROR\_IPSEC\_IKE\_DOS\_COOKIE\_SENT**
   

13890 (0x3642)
 



Sent DoS cookie notify to initiator.


   

<span id="ERROR_IPSEC_IKE_SHUTTING_DOWN"></span><span id="error_ipsec_ike_shutting_down"></span>**ERROR\_IPSEC\_IKE\_SHUTTING\_DOWN**
   

13891 (0x3643)
 



IKE service is shutting down.


   

<span id="ERROR_IPSEC_IKE_CGA_AUTH_FAILED"></span><span id="error_ipsec_ike_cga_auth_failed"></span>**ERROR\_IPSEC\_IKE\_CGA\_AUTH\_FAILED**
   

13892 (0x3644)
 



Could not verify binding between CGA address and certificate.


   

<span id="ERROR_IPSEC_IKE_PROCESS_ERR_NATOA"></span><span id="error_ipsec_ike_process_err_natoa"></span>**ERROR\_IPSEC\_IKE\_PROCESS\_ERR\_NATOA**
   

13893 (0x3645)
 



Error processing NatOA payload.


   

<span id="ERROR_IPSEC_IKE_INVALID_MM_FOR_QM"></span><span id="error_ipsec_ike_invalid_mm_for_qm"></span>**ERROR\_IPSEC\_IKE\_INVALID\_MM\_FOR\_QM**
   

13894 (0x3646)
 



Parameters of the main mode are invalid for this quick mode.


   

<span id="ERROR_IPSEC_IKE_QM_EXPIRED"></span><span id="error_ipsec_ike_qm_expired"></span>**ERROR\_IPSEC\_IKE\_QM\_EXPIRED**
   

13895 (0x3647)
 



Quick mode SA was expired by IPsec driver.


   

<span id="ERROR_IPSEC_IKE_TOO_MANY_FILTERS"></span><span id="error_ipsec_ike_too_many_filters"></span>**ERROR\_IPSEC\_IKE\_TOO\_MANY\_FILTERS**
   

13896 (0x3648)
 



Too many dynamically added IKEEXT filters were detected.


   

<span id="ERROR_IPSEC_IKE_NEG_STATUS_END"></span><span id="error_ipsec_ike_neg_status_end"></span>**ERROR\_IPSEC\_IKE\_NEG\_STATUS\_END**
   

13897 (0x3649)
 



ERROR\_IPSEC\_IKE\_NEG\_STATUS\_END


   

<span id="ERROR_IPSEC_IKE_KILL_DUMMY_NAP_TUNNEL"></span><span id="error_ipsec_ike_kill_dummy_nap_tunnel"></span>**ERROR\_IPSEC\_IKE\_KILL\_DUMMY\_NAP\_TUNNEL**
   

13898 (0x364A)
 



NAP reauth succeeded and must delete the dummy NAP IKEv2 tunnel.


   

<span id="ERROR_IPSEC_IKE_INNER_IP_ASSIGNMENT_FAILURE"></span><span id="error_ipsec_ike_inner_ip_assignment_failure"></span>**ERROR\_IPSEC\_IKE\_INNER\_IP\_ASSIGNMENT\_FAILURE**
   

13899 (0x364B)
 



Error in assigning inner IP address to initiator in tunnel mode.


   

<span id="ERROR_IPSEC_IKE_REQUIRE_CP_PAYLOAD_MISSING"></span><span id="error_ipsec_ike_require_cp_payload_missing"></span>**ERROR\_IPSEC\_IKE\_REQUIRE\_CP\_PAYLOAD\_MISSING**
   

13900 (0x364C)
 



Require configuration payload missing.


   

<span id="ERROR_IPSEC_KEY_MODULE_IMPERSONATION_NEGOTIATION_PENDING"></span><span id="error_ipsec_key_module_impersonation_negotiation_pending"></span>**ERROR\_IPSEC\_KEY\_MODULE\_IMPERSONATION\_NEGOTIATION\_PENDING**
   

13901 (0x364D)
 



A negotiation running as the security principle who issued the connection is in progress.


   

<span id="ERROR_IPSEC_IKE_COEXISTENCE_SUPPRESS"></span><span id="error_ipsec_ike_coexistence_suppress"></span>**ERROR\_IPSEC\_IKE\_COEXISTENCE\_SUPPRESS**
   

13902 (0x364E)
 



SA was deleted due to IKEv1/AuthIP co-existence suppress check.


   

<span id="ERROR_IPSEC_IKE_RATELIMIT_DROP"></span><span id="error_ipsec_ike_ratelimit_drop"></span>**ERROR\_IPSEC\_IKE\_RATELIMIT\_DROP**
   

13903 (0x364F)
 



Incoming SA request was dropped due to peer IP address rate limiting.


   

<span id="ERROR_IPSEC_IKE_PEER_DOESNT_SUPPORT_MOBIKE"></span><span id="error_ipsec_ike_peer_doesnt_support_mobike"></span>**ERROR\_IPSEC\_IKE\_PEER\_DOESNT\_SUPPORT\_MOBIKE**
   

13904 (0x3650)
 



Peer does not support MOBIKE.


   

<span id="ERROR_IPSEC_IKE_AUTHORIZATION_FAILURE"></span><span id="error_ipsec_ike_authorization_failure"></span>**ERROR\_IPSEC\_IKE\_AUTHORIZATION\_FAILURE**
   

13905 (0x3651)
 



SA establishment is not authorized.


   

<span id="ERROR_IPSEC_IKE_STRONG_CRED_AUTHORIZATION_FAILURE"></span><span id="error_ipsec_ike_strong_cred_authorization_failure"></span>**ERROR\_IPSEC\_IKE\_STRONG\_CRED\_AUTHORIZATION\_FAILURE**
   

13906 (0x3652)
 



SA establishment is not authorized because there is not a sufficiently strong PKINIT-based credential.


   

<span id="ERROR_IPSEC_IKE_AUTHORIZATION_FAILURE_WITH_OPTIONAL_RETRY"></span><span id="error_ipsec_ike_authorization_failure_with_optional_retry"></span>**ERROR\_IPSEC\_IKE\_AUTHORIZATION\_FAILURE\_WITH\_OPTIONAL\_RETRY**
   

13907 (0x3653)
 



SA establishment is not authorized. You may need to enter updated or different credentials such as a smartcard.


   

<span id="ERROR_IPSEC_IKE_STRONG_CRED_AUTHORIZATION_AND_CERTMAP_FAILURE"></span><span id="error_ipsec_ike_strong_cred_authorization_and_certmap_failure"></span>**ERROR\_IPSEC\_IKE\_STRONG\_CRED\_AUTHORIZATION\_AND\_CERTMAP\_FAILURE**
   

13908 (0x3654)
 



SA establishment is not authorized because there is not a sufficiently strong PKINIT-based credential. This might be related to certificate-to-account mapping failure for the SA.


   

<span id="ERROR_IPSEC_IKE_NEG_STATUS_EXTENDED_END"></span><span id="error_ipsec_ike_neg_status_extended_end"></span>**ERROR\_IPSEC\_IKE\_NEG\_STATUS\_EXTENDED\_END**
   

13909 (0x3655)
 



ERROR\_IPSEC\_IKE\_NEG\_STATUS\_EXTENDED\_END


   

<span id="ERROR_IPSEC_BAD_SPI"></span><span id="error_ipsec_bad_spi"></span>**ERROR\_IPSEC\_BAD\_SPI**
   

13910 (0x3656)
 



The SPI in the packet does not match a valid IPsec SA.


   

<span id="ERROR_IPSEC_SA_LIFETIME_EXPIRED"></span><span id="error_ipsec_sa_lifetime_expired"></span>**ERROR\_IPSEC\_SA\_LIFETIME\_EXPIRED**
   

13911 (0x3657)
 



Packet was received on an IPsec SA whose lifetime has expired.


   

<span id="ERROR_IPSEC_WRONG_SA"></span><span id="error_ipsec_wrong_sa"></span>**ERROR\_IPSEC\_WRONG\_SA**
   

13912 (0x3658)
 



Packet was received on an IPsec SA that does not match the packet characteristics.


   

<span id="ERROR_IPSEC_REPLAY_CHECK_FAILED"></span><span id="error_ipsec_replay_check_failed"></span>**ERROR\_IPSEC\_REPLAY\_CHECK\_FAILED**
   

13913 (0x3659)
 



Packet sequence number replay check failed.


   

<span id="ERROR_IPSEC_INVALID_PACKET"></span><span id="error_ipsec_invalid_packet"></span>**ERROR\_IPSEC\_INVALID\_PACKET**
   

13914 (0x365A)
 



IPsec header and/or trailer in the packet is invalid.


   

<span id="ERROR_IPSEC_INTEGRITY_CHECK_FAILED"></span><span id="error_ipsec_integrity_check_failed"></span>**ERROR\_IPSEC\_INTEGRITY\_CHECK\_FAILED**
   

13915 (0x365B)
 



IPsec integrity check failed.


   

<span id="ERROR_IPSEC_CLEAR_TEXT_DROP"></span><span id="error_ipsec_clear_text_drop"></span>**ERROR\_IPSEC\_CLEAR\_TEXT\_DROP**
   

13916 (0x365C)
 



IPsec dropped a clear text packet.


   

<span id="ERROR_IPSEC_AUTH_FIREWALL_DROP"></span><span id="error_ipsec_auth_firewall_drop"></span>**ERROR\_IPSEC\_AUTH\_FIREWALL\_DROP**
   

13917 (0x365D)
 



IPsec dropped an incoming ESP packet in authenticated firewall mode. This drop is benign.


   

<span id="ERROR_IPSEC_THROTTLE_DROP"></span><span id="error_ipsec_throttle_drop"></span>**ERROR\_IPSEC\_THROTTLE\_DROP**
   

13918 (0x365E)
 



IPsec dropped a packet due to DoS throttling.


   

<span id="ERROR_IPSEC_DOSP_BLOCK"></span><span id="error_ipsec_dosp_block"></span>**ERROR\_IPSEC\_DOSP\_BLOCK**
   

13925 (0x3665)
 



IPsec DoS Protection matched an explicit block rule.


   

<span id="ERROR_IPSEC_DOSP_RECEIVED_MULTICAST"></span><span id="error_ipsec_dosp_received_multicast"></span>**ERROR\_IPSEC\_DOSP\_RECEIVED\_MULTICAST**
   

13926 (0x3666)
 



IPsec DoS Protection received an IPsec specific multicast packet which is not allowed.


   

<span id="ERROR_IPSEC_DOSP_INVALID_PACKET"></span><span id="error_ipsec_dosp_invalid_packet"></span>**ERROR\_IPSEC\_DOSP\_INVALID\_PACKET**
   

13927 (0x3667)
 



IPsec DoS Protection received an incorrectly formatted packet.


   

<span id="ERROR_IPSEC_DOSP_STATE_LOOKUP_FAILED"></span><span id="error_ipsec_dosp_state_lookup_failed"></span>**ERROR\_IPSEC\_DOSP\_STATE\_LOOKUP\_FAILED**
   

13928 (0x3668)
 



IPsec DoS Protection failed to look up state.


   

<span id="ERROR_IPSEC_DOSP_MAX_ENTRIES"></span><span id="error_ipsec_dosp_max_entries"></span>**ERROR\_IPSEC\_DOSP\_MAX\_ENTRIES**
   

13929 (0x3669)
 



IPsec DoS Protection failed to create state because the maximum number of entries allowed by policy has been reached.


   

<span id="ERROR_IPSEC_DOSP_KEYMOD_NOT_ALLOWED"></span><span id="error_ipsec_dosp_keymod_not_allowed"></span>**ERROR\_IPSEC\_DOSP\_KEYMOD\_NOT\_ALLOWED**
   

13930 (0x366A)
 



IPsec DoS Protection received an IPsec negotiation packet for a keying module which is not allowed by policy.


   

<span id="ERROR_IPSEC_DOSP_NOT_INSTALLED"></span><span id="error_ipsec_dosp_not_installed"></span>**ERROR\_IPSEC\_DOSP\_NOT\_INSTALLED**
   

13931 (0x366B)
 



IPsec DoS Protection has not been enabled.


   

<span id="ERROR_IPSEC_DOSP_MAX_PER_IP_RATELIMIT_QUEUES"></span><span id="error_ipsec_dosp_max_per_ip_ratelimit_queues"></span>**ERROR\_IPSEC\_DOSP\_MAX\_PER\_IP\_RATELIMIT\_QUEUES**
   

13932 (0x366C)
 



IPsec DoS Protection failed to create a per internal IP rate limit queue because the maximum number of queues allowed by policy has been reached.


   

<span id="ERROR_SXS_SECTION_NOT_FOUND"></span><span id="error_sxs_section_not_found"></span>**ERROR\_SXS\_SECTION\_NOT\_FOUND**
   

14000 (0x36B0)
 



The requested section was not present in the activation context.


   

<span id="ERROR_SXS_CANT_GEN_ACTCTX"></span><span id="error_sxs_cant_gen_actctx"></span>**ERROR\_SXS\_CANT\_GEN\_ACTCTX**
   

14001 (0x36B1)
 



The application has failed to start because its side-by-side configuration is incorrect. Please see the application event log or use the command-line sxstrace.exe tool for more detail.


   

<span id="ERROR_SXS_INVALID_ACTCTXDATA_FORMAT"></span><span id="error_sxs_invalid_actctxdata_format"></span>**ERROR\_SXS\_INVALID\_ACTCTXDATA\_FORMAT**
   

14002 (0x36B2)
 



The application binding data format is invalid.


   

<span id="ERROR_SXS_ASSEMBLY_NOT_FOUND"></span><span id="error_sxs_assembly_not_found"></span>**ERROR\_SXS\_ASSEMBLY\_NOT\_FOUND**
   

14003 (0x36B3)
 



The referenced assembly is not installed on your system.


   

<span id="ERROR_SXS_MANIFEST_FORMAT_ERROR"></span><span id="error_sxs_manifest_format_error"></span>**ERROR\_SXS\_MANIFEST\_FORMAT\_ERROR**
   

14004 (0x36B4)
 



The manifest file does not begin with the required tag and format information.


   

<span id="ERROR_SXS_MANIFEST_PARSE_ERROR"></span><span id="error_sxs_manifest_parse_error"></span>**ERROR\_SXS\_MANIFEST\_PARSE\_ERROR**
   

14005 (0x36B5)
 



The manifest file contains one or more syntax errors.


   

<span id="ERROR_SXS_ACTIVATION_CONTEXT_DISABLED"></span><span id="error_sxs_activation_context_disabled"></span>**ERROR\_SXS\_ACTIVATION\_CONTEXT\_DISABLED**
   

14006 (0x36B6)
 



The application attempted to activate a disabled activation context.


   

<span id="ERROR_SXS_KEY_NOT_FOUND"></span><span id="error_sxs_key_not_found"></span>**ERROR\_SXS\_KEY\_NOT\_FOUND**
   

14007 (0x36B7)
 



The requested lookup key was not found in any active activation context.


   

<span id="ERROR_SXS_VERSION_CONFLICT"></span><span id="error_sxs_version_conflict"></span>**ERROR\_SXS\_VERSION\_CONFLICT**
   

14008 (0x36B8)
 



A component version required by the application conflicts with another component version already active.


   

<span id="ERROR_SXS_WRONG_SECTION_TYPE"></span><span id="error_sxs_wrong_section_type"></span>**ERROR\_SXS\_WRONG\_SECTION\_TYPE**
   

14009 (0x36B9)
 



The type requested activation context section does not match the query API used.


   

<span id="ERROR_SXS_THREAD_QUERIES_DISABLED"></span><span id="error_sxs_thread_queries_disabled"></span>**ERROR\_SXS\_THREAD\_QUERIES\_DISABLED**
   

14010 (0x36BA)
 



Lack of system resources has required isolated activation to be disabled for the current thread of execution.


   

<span id="ERROR_SXS_PROCESS_DEFAULT_ALREADY_SET"></span><span id="error_sxs_process_default_already_set"></span>**ERROR\_SXS\_PROCESS\_DEFAULT\_ALREADY\_SET**
   

14011 (0x36BB)
 



An attempt to set the process default activation context failed because the process default activation context was already set.


   

<span id="ERROR_SXS_UNKNOWN_ENCODING_GROUP"></span><span id="error_sxs_unknown_encoding_group"></span>**ERROR\_SXS\_UNKNOWN\_ENCODING\_GROUP**
   

14012 (0x36BC)
 



The encoding group identifier specified is not recognized.


   

<span id="ERROR_SXS_UNKNOWN_ENCODING"></span><span id="error_sxs_unknown_encoding"></span>**ERROR\_SXS\_UNKNOWN\_ENCODING**
   

14013 (0x36BD)
 



The encoding requested is not recognized.


   

<span id="ERROR_SXS_INVALID_XML_NAMESPACE_URI"></span><span id="error_sxs_invalid_xml_namespace_uri"></span>**ERROR\_SXS\_INVALID\_XML\_NAMESPACE\_URI**
   

14014 (0x36BE)
 



The manifest contains a reference to an invalid URI.


   

<span id="ERROR_SXS_ROOT_MANIFEST_DEPENDENCY_NOT_INSTALLED"></span><span id="error_sxs_root_manifest_dependency_not_installed"></span>**ERROR\_SXS\_ROOT\_MANIFEST\_DEPENDENCY\_NOT\_INSTALLED**
   

14015 (0x36BF)
 



The application manifest contains a reference to a dependent assembly which is not installed.


   

<span id="ERROR_SXS_LEAF_MANIFEST_DEPENDENCY_NOT_INSTALLED"></span><span id="error_sxs_leaf_manifest_dependency_not_installed"></span>**ERROR\_SXS\_LEAF\_MANIFEST\_DEPENDENCY\_NOT\_INSTALLED**
   

14016 (0x36C0)
 



The manifest for an assembly used by the application has a reference to a dependent assembly which is not installed.


   

<span id="ERROR_SXS_INVALID_ASSEMBLY_IDENTITY_ATTRIBUTE"></span><span id="error_sxs_invalid_assembly_identity_attribute"></span>**ERROR\_SXS\_INVALID\_ASSEMBLY\_IDENTITY\_ATTRIBUTE**
   

14017 (0x36C1)
 



The manifest contains an attribute for the assembly identity which is not valid.


   

<span id="ERROR_SXS_MANIFEST_MISSING_REQUIRED_DEFAULT_NAMESPACE"></span><span id="error_sxs_manifest_missing_required_default_namespace"></span>**ERROR\_SXS\_MANIFEST\_MISSING\_REQUIRED\_DEFAULT\_NAMESPACE**
   

14018 (0x36C2)
 



The manifest is missing the required default namespace specification on the assembly element.


   

<span id="ERROR_SXS_MANIFEST_INVALID_REQUIRED_DEFAULT_NAMESPACE"></span><span id="error_sxs_manifest_invalid_required_default_namespace"></span>**ERROR\_SXS\_MANIFEST\_INVALID\_REQUIRED\_DEFAULT\_NAMESPACE**
   

14019 (0x36C3)
 



The manifest has a default namespace specified on the assembly element but its value is not "urn:schemas-microsoft-com:asm.v1".


   

<span id="ERROR_SXS_PRIVATE_MANIFEST_CROSS_PATH_WITH_REPARSE_POINT"></span><span id="error_sxs_private_manifest_cross_path_with_reparse_point"></span>**ERROR\_SXS\_PRIVATE\_MANIFEST\_CROSS\_PATH\_WITH\_REPARSE\_POINT**
   

14020 (0x36C4)
 



The private manifest probed has crossed a path with an unsupported reparse point.


   

<span id="ERROR_SXS_DUPLICATE_DLL_NAME"></span><span id="error_sxs_duplicate_dll_name"></span>**ERROR\_SXS\_DUPLICATE\_DLL\_NAME**
   

14021 (0x36C5)
 



Two or more components referenced directly or indirectly by the application manifest have files by the same name.


   

<span id="ERROR_SXS_DUPLICATE_WINDOWCLASS_NAME"></span><span id="error_sxs_duplicate_windowclass_name"></span>**ERROR\_SXS\_DUPLICATE\_WINDOWCLASS\_NAME**
   

14022 (0x36C6)
 



Two or more components referenced directly or indirectly by the application manifest have window classes with the same name.


   

<span id="ERROR_SXS_DUPLICATE_CLSID"></span><span id="error_sxs_duplicate_clsid"></span>**ERROR\_SXS\_DUPLICATE\_CLSID**
   

14023 (0x36C7)
 



Two or more components referenced directly or indirectly by the application manifest have the same COM server CLSIDs.


   

<span id="ERROR_SXS_DUPLICATE_IID"></span><span id="error_sxs_duplicate_iid"></span>**ERROR\_SXS\_DUPLICATE\_IID**
   

14024 (0x36C8)
 



Two or more components referenced directly or indirectly by the application manifest have proxies for the same COM interface IIDs.


   

<span id="ERROR_SXS_DUPLICATE_TLBID"></span><span id="error_sxs_duplicate_tlbid"></span>**ERROR\_SXS\_DUPLICATE\_TLBID**
   

14025 (0x36C9)
 



Two or more components referenced directly or indirectly by the application manifest have the same COM type library TLBIDs.


   

<span id="ERROR_SXS_DUPLICATE_PROGID"></span><span id="error_sxs_duplicate_progid"></span>**ERROR\_SXS\_DUPLICATE\_PROGID**
   

14026 (0x36CA)
 



Two or more components referenced directly or indirectly by the application manifest have the same COM ProgIDs.


   

<span id="ERROR_SXS_DUPLICATE_ASSEMBLY_NAME"></span><span id="error_sxs_duplicate_assembly_name"></span>**ERROR\_SXS\_DUPLICATE\_ASSEMBLY\_NAME**
   

14027 (0x36CB)
 



Two or more components referenced directly or indirectly by the application manifest are different versions of the same component which is not permitted.


   

<span id="ERROR_SXS_FILE_HASH_MISMATCH"></span><span id="error_sxs_file_hash_mismatch"></span>**ERROR\_SXS\_FILE\_HASH\_MISMATCH**
   

14028 (0x36CC)
 



A component's file does not match the verification information present in the component manifest.


   

<span id="ERROR_SXS_POLICY_PARSE_ERROR"></span><span id="error_sxs_policy_parse_error"></span>**ERROR\_SXS\_POLICY\_PARSE\_ERROR**
   

14029 (0x36CD)
 



The policy manifest contains one or more syntax errors.


   

<span id="ERROR_SXS_XML_E_MISSINGQUOTE"></span><span id="error_sxs_xml_e_missingquote"></span>**ERROR\_SXS\_XML\_E\_MISSINGQUOTE**
   

14030 (0x36CE)
 



Manifest Parse Error : A string literal was expected, but no opening quote character was found.


   

<span id="ERROR_SXS_XML_E_COMMENTSYNTAX"></span><span id="error_sxs_xml_e_commentsyntax"></span>**ERROR\_SXS\_XML\_E\_COMMENTSYNTAX**
   

14031 (0x36CF)
 



Manifest Parse Error : Incorrect syntax was used in a comment.


   

<span id="ERROR_SXS_XML_E_BADSTARTNAMECHAR"></span><span id="error_sxs_xml_e_badstartnamechar"></span>**ERROR\_SXS\_XML\_E\_BADSTARTNAMECHAR**
   

14032 (0x36D0)
 



Manifest Parse Error : A name was started with an invalid character.


   

<span id="ERROR_SXS_XML_E_BADNAMECHAR"></span><span id="error_sxs_xml_e_badnamechar"></span>**ERROR\_SXS\_XML\_E\_BADNAMECHAR**
   

14033 (0x36D1)
 



Manifest Parse Error : A name contained an invalid character.


   

<span id="ERROR_SXS_XML_E_BADCHARINSTRING"></span><span id="error_sxs_xml_e_badcharinstring"></span>**ERROR\_SXS\_XML\_E\_BADCHARINSTRING**
   

14034 (0x36D2)
 



Manifest Parse Error : A string literal contained an invalid character.


   

<span id="ERROR_SXS_XML_E_XMLDECLSYNTAX"></span><span id="error_sxs_xml_e_xmldeclsyntax"></span>**ERROR\_SXS\_XML\_E\_XMLDECLSYNTAX**
   

14035 (0x36D3)
 



Manifest Parse Error : Invalid syntax for an xml declaration.


   

<span id="ERROR_SXS_XML_E_BADCHARDATA"></span><span id="error_sxs_xml_e_badchardata"></span>**ERROR\_SXS\_XML\_E\_BADCHARDATA**
   

14036 (0x36D4)
 



Manifest Parse Error : An Invalid character was found in text content.


   

<span id="ERROR_SXS_XML_E_MISSINGWHITESPACE"></span><span id="error_sxs_xml_e_missingwhitespace"></span>**ERROR\_SXS\_XML\_E\_MISSINGWHITESPACE**
   

14037 (0x36D5)
 



Manifest Parse Error : Required white space was missing.


   

<span id="ERROR_SXS_XML_E_EXPECTINGTAGEND"></span><span id="error_sxs_xml_e_expectingtagend"></span>**ERROR\_SXS\_XML\_E\_EXPECTINGTAGEND**
   

14038 (0x36D6)
 



Manifest Parse Error : The character '>' was expected.


   

<span id="ERROR_SXS_XML_E_MISSINGSEMICOLON"></span><span id="error_sxs_xml_e_missingsemicolon"></span>**ERROR\_SXS\_XML\_E\_MISSINGSEMICOLON**
   

14039 (0x36D7)
 



Manifest Parse Error : A semi colon character was expected.


   

<span id="ERROR_SXS_XML_E_UNBALANCEDPAREN"></span><span id="error_sxs_xml_e_unbalancedparen"></span>**ERROR\_SXS\_XML\_E\_UNBALANCEDPAREN**
   

14040 (0x36D8)
 



Manifest Parse Error : Unbalanced parentheses.


   

<span id="ERROR_SXS_XML_E_INTERNALERROR"></span><span id="error_sxs_xml_e_internalerror"></span>**ERROR\_SXS\_XML\_E\_INTERNALERROR**
   

14041 (0x36D9)
 



Manifest Parse Error : Internal error.


   

<span id="ERROR_SXS_XML_E_UNEXPECTED_WHITESPACE"></span><span id="error_sxs_xml_e_unexpected_whitespace"></span>**ERROR\_SXS\_XML\_E\_UNEXPECTED\_WHITESPACE**
   

14042 (0x36DA)
 



Manifest Parse Error : Whitespace is not allowed at this location.


   

<span id="ERROR_SXS_XML_E_INCOMPLETE_ENCODING"></span><span id="error_sxs_xml_e_incomplete_encoding"></span>**ERROR\_SXS\_XML\_E\_INCOMPLETE\_ENCODING**
   

14043 (0x36DB)
 



Manifest Parse Error : End of file reached in invalid state for current encoding.


   

<span id="ERROR_SXS_XML_E_MISSING_PAREN"></span><span id="error_sxs_xml_e_missing_paren"></span>**ERROR\_SXS\_XML\_E\_MISSING\_PAREN**
   

14044 (0x36DC)
 



Manifest Parse Error : Missing parenthesis.


   

<span id="ERROR_SXS_XML_E_EXPECTINGCLOSEQUOTE"></span><span id="error_sxs_xml_e_expectingclosequote"></span>**ERROR\_SXS\_XML\_E\_EXPECTINGCLOSEQUOTE**
   

14045 (0x36DD)
 



Manifest Parse Error : A single or double closing quote character (\\' or \\") is missing.


   

<span id="ERROR_SXS_XML_E_MULTIPLE_COLONS"></span><span id="error_sxs_xml_e_multiple_colons"></span>**ERROR\_SXS\_XML\_E\_MULTIPLE\_COLONS**
   

14046 (0x36DE)
 



Manifest Parse Error : Multiple colons are not allowed in a name.


   

<span id="ERROR_SXS_XML_E_INVALID_DECIMAL"></span><span id="error_sxs_xml_e_invalid_decimal"></span>**ERROR\_SXS\_XML\_E\_INVALID\_DECIMAL**
   

14047 (0x36DF)
 



Manifest Parse Error : Invalid character for decimal digit.


   

<span id="ERROR_SXS_XML_E_INVALID_HEXIDECIMAL"></span><span id="error_sxs_xml_e_invalid_hexidecimal"></span>**ERROR\_SXS\_XML\_E\_INVALID\_HEXIDECIMAL**
   

14048 (0x36E0)
 



Manifest Parse Error : Invalid character for hexadecimal digit.


   

<span id="ERROR_SXS_XML_E_INVALID_UNICODE"></span><span id="error_sxs_xml_e_invalid_unicode"></span>**ERROR\_SXS\_XML\_E\_INVALID\_UNICODE**
   

14049 (0x36E1)
 



Manifest Parse Error : Invalid unicode character value for this platform.


   

<span id="ERROR_SXS_XML_E_WHITESPACEORQUESTIONMARK"></span><span id="error_sxs_xml_e_whitespaceorquestionmark"></span>**ERROR\_SXS\_XML\_E\_WHITESPACEORQUESTIONMARK**
   

14050 (0x36E2)
 



Manifest Parse Error : Expecting whitespace or '?'.


   

<span id="ERROR_SXS_XML_E_UNEXPECTEDENDTAG"></span><span id="error_sxs_xml_e_unexpectedendtag"></span>**ERROR\_SXS\_XML\_E\_UNEXPECTEDENDTAG**
   

14051 (0x36E3)
 



Manifest Parse Error : End tag was not expected at this location.


   

<span id="ERROR_SXS_XML_E_UNCLOSEDTAG"></span><span id="error_sxs_xml_e_unclosedtag"></span>**ERROR\_SXS\_XML\_E\_UNCLOSEDTAG**
   

14052 (0x36E4)
 



Manifest Parse Error : The following tags were not closed: %1.


   

<span id="ERROR_SXS_XML_E_DUPLICATEATTRIBUTE"></span><span id="error_sxs_xml_e_duplicateattribute"></span>**ERROR\_SXS\_XML\_E\_DUPLICATEATTRIBUTE**
   

14053 (0x36E5)
 



Manifest Parse Error : Duplicate attribute.


   

<span id="ERROR_SXS_XML_E_MULTIPLEROOTS"></span><span id="error_sxs_xml_e_multipleroots"></span>**ERROR\_SXS\_XML\_E\_MULTIPLEROOTS**
   

14054 (0x36E6)
 



Manifest Parse Error : Only one top level element is allowed in an XML document.


   

<span id="ERROR_SXS_XML_E_INVALIDATROOTLEVEL"></span><span id="error_sxs_xml_e_invalidatrootlevel"></span>**ERROR\_SXS\_XML\_E\_INVALIDATROOTLEVEL**
   

14055 (0x36E7)
 



Manifest Parse Error : Invalid at the top level of the document.


   

<span id="ERROR_SXS_XML_E_BADXMLDECL"></span><span id="error_sxs_xml_e_badxmldecl"></span>**ERROR\_SXS\_XML\_E\_BADXMLDECL**
   

14056 (0x36E8)
 



Manifest Parse Error : Invalid xml declaration.


   

<span id="ERROR_SXS_XML_E_MISSINGROOT"></span><span id="error_sxs_xml_e_missingroot"></span>**ERROR\_SXS\_XML\_E\_MISSINGROOT**
   

14057 (0x36E9)
 



Manifest Parse Error : XML document must have a top level element.


   

<span id="ERROR_SXS_XML_E_UNEXPECTEDEOF"></span><span id="error_sxs_xml_e_unexpectedeof"></span>**ERROR\_SXS\_XML\_E\_UNEXPECTEDEOF**
   

14058 (0x36EA)
 



Manifest Parse Error : Unexpected end of file.


   

<span id="ERROR_SXS_XML_E_BADPEREFINSUBSET"></span><span id="error_sxs_xml_e_badperefinsubset"></span>**ERROR\_SXS\_XML\_E\_BADPEREFINSUBSET**
   

14059 (0x36EB)
 



Manifest Parse Error : Parameter entities cannot be used inside markup declarations in an internal subset.


   

<span id="ERROR_SXS_XML_E_UNCLOSEDSTARTTAG"></span><span id="error_sxs_xml_e_unclosedstarttag"></span>**ERROR\_SXS\_XML\_E\_UNCLOSEDSTARTTAG**
   

14060 (0x36EC)
 



Manifest Parse Error : Element was not closed.


   

<span id="ERROR_SXS_XML_E_UNCLOSEDENDTAG"></span><span id="error_sxs_xml_e_unclosedendtag"></span>**ERROR\_SXS\_XML\_E\_UNCLOSEDENDTAG**
   

14061 (0x36ED)
 



Manifest Parse Error : End element was missing the character '>'.


   

<span id="ERROR_SXS_XML_E_UNCLOSEDSTRING"></span><span id="error_sxs_xml_e_unclosedstring"></span>**ERROR\_SXS\_XML\_E\_UNCLOSEDSTRING**
   

14062 (0x36EE)
 



Manifest Parse Error : A string literal was not closed.


   

<span id="ERROR_SXS_XML_E_UNCLOSEDCOMMENT"></span><span id="error_sxs_xml_e_unclosedcomment"></span>**ERROR\_SXS\_XML\_E\_UNCLOSEDCOMMENT**
   

14063 (0x36EF)
 



Manifest Parse Error : A comment was not closed.


   

<span id="ERROR_SXS_XML_E_UNCLOSEDDECL"></span><span id="error_sxs_xml_e_uncloseddecl"></span>**ERROR\_SXS\_XML\_E\_UNCLOSEDDECL**
   

14064 (0x36F0)
 



Manifest Parse Error : A declaration was not closed.


   

<span id="ERROR_SXS_XML_E_UNCLOSEDCDATA"></span><span id="error_sxs_xml_e_unclosedcdata"></span>**ERROR\_SXS\_XML\_E\_UNCLOSEDCDATA**
   

14065 (0x36F1)
 



Manifest Parse Error : A CDATA section was not closed.


   

<span id="ERROR_SXS_XML_E_RESERVEDNAMESPACE"></span><span id="error_sxs_xml_e_reservednamespace"></span>**ERROR\_SXS\_XML\_E\_RESERVEDNAMESPACE**
   

14066 (0x36F2)
 



Manifest Parse Error : The namespace prefix is not allowed to start with the reserved string "xml".


   

<span id="ERROR_SXS_XML_E_INVALIDENCODING"></span><span id="error_sxs_xml_e_invalidencoding"></span>**ERROR\_SXS\_XML\_E\_INVALIDENCODING**
   

14067 (0x36F3)
 



Manifest Parse Error : System does not support the specified encoding.


   

<span id="ERROR_SXS_XML_E_INVALIDSWITCH"></span><span id="error_sxs_xml_e_invalidswitch"></span>**ERROR\_SXS\_XML\_E\_INVALIDSWITCH**
   

14068 (0x36F4)
 



Manifest Parse Error : Switch from current encoding to specified encoding not supported.


   

<span id="ERROR_SXS_XML_E_BADXMLCASE"></span><span id="error_sxs_xml_e_badxmlcase"></span>**ERROR\_SXS\_XML\_E\_BADXMLCASE**
   

14069 (0x36F5)
 



Manifest Parse Error : The name 'xml' is reserved and must be lower case.


   

<span id="ERROR_SXS_XML_E_INVALID_STANDALONE"></span><span id="error_sxs_xml_e_invalid_standalone"></span>**ERROR\_SXS\_XML\_E\_INVALID\_STANDALONE**
   

14070 (0x36F6)
 



Manifest Parse Error : The standalone attribute must have the value 'yes' or 'no'.


   

<span id="ERROR_SXS_XML_E_UNEXPECTED_STANDALONE"></span><span id="error_sxs_xml_e_unexpected_standalone"></span>**ERROR\_SXS\_XML\_E\_UNEXPECTED\_STANDALONE**
   

14071 (0x36F7)
 



Manifest Parse Error : The standalone attribute cannot be used in external entities.


   

<span id="ERROR_SXS_XML_E_INVALID_VERSION"></span><span id="error_sxs_xml_e_invalid_version"></span>**ERROR\_SXS\_XML\_E\_INVALID\_VERSION**
   

14072 (0x36F8)
 



Manifest Parse Error : Invalid version number.


   

<span id="ERROR_SXS_XML_E_MISSINGEQUALS"></span><span id="error_sxs_xml_e_missingequals"></span>**ERROR\_SXS\_XML\_E\_MISSINGEQUALS**
   

14073 (0x36F9)
 



Manifest Parse Error : Missing equals sign between attribute and attribute value.


   

<span id="ERROR_SXS_PROTECTION_RECOVERY_FAILED"></span><span id="error_sxs_protection_recovery_failed"></span>**ERROR\_SXS\_PROTECTION\_RECOVERY\_FAILED**
   

14074 (0x36FA)
 



Assembly Protection Error : Unable to recover the specified assembly.


   

<span id="ERROR_SXS_PROTECTION_PUBLIC_KEY_TOO_SHORT"></span><span id="error_sxs_protection_public_key_too_short"></span>**ERROR\_SXS\_PROTECTION\_PUBLIC\_KEY\_TOO\_SHORT**
   

14075 (0x36FB)
 



Assembly Protection Error : The public key for an assembly was too short to be allowed.


   

<span id="ERROR_SXS_PROTECTION_CATALOG_NOT_VALID"></span><span id="error_sxs_protection_catalog_not_valid"></span>**ERROR\_SXS\_PROTECTION\_CATALOG\_NOT\_VALID**
   

14076 (0x36FC)
 



Assembly Protection Error : The catalog for an assembly is not valid, or does not match the assembly's manifest.


   

<span id="ERROR_SXS_UNTRANSLATABLE_HRESULT"></span><span id="error_sxs_untranslatable_hresult"></span>**ERROR\_SXS\_UNTRANSLATABLE\_HRESULT**
   

14077 (0x36FD)
 



An HRESULT could not be translated to a corresponding Win32 error code.


   

<span id="ERROR_SXS_PROTECTION_CATALOG_FILE_MISSING"></span><span id="error_sxs_protection_catalog_file_missing"></span>**ERROR\_SXS\_PROTECTION\_CATALOG\_FILE\_MISSING**
   

14078 (0x36FE)
 



Assembly Protection Error : The catalog for an assembly is missing.


   

<span id="ERROR_SXS_MISSING_ASSEMBLY_IDENTITY_ATTRIBUTE"></span><span id="error_sxs_missing_assembly_identity_attribute"></span>**ERROR\_SXS\_MISSING\_ASSEMBLY\_IDENTITY\_ATTRIBUTE**
   

14079 (0x36FF)
 



The supplied assembly identity is missing one or more attributes which must be present in this context.


   

<span id="ERROR_SXS_INVALID_ASSEMBLY_IDENTITY_ATTRIBUTE_NAME"></span><span id="error_sxs_invalid_assembly_identity_attribute_name"></span>**ERROR\_SXS\_INVALID\_ASSEMBLY\_IDENTITY\_ATTRIBUTE\_NAME**
   

14080 (0x3700)
 



The supplied assembly identity has one or more attribute names that contain characters not permitted in XML names.


   

<span id="ERROR_SXS_ASSEMBLY_MISSING"></span><span id="error_sxs_assembly_missing"></span>**ERROR\_SXS\_ASSEMBLY\_MISSING**
   

14081 (0x3701)
 



The referenced assembly could not be found.


   

<span id="ERROR_SXS_CORRUPT_ACTIVATION_STACK"></span><span id="error_sxs_corrupt_activation_stack"></span>**ERROR\_SXS\_CORRUPT\_ACTIVATION\_STACK**
   

14082 (0x3702)
 



The activation context activation stack for the running thread of execution is corrupt.


   

<span id="ERROR_SXS_CORRUPTION"></span><span id="error_sxs_corruption"></span>**ERROR\_SXS\_CORRUPTION**
   

14083 (0x3703)
 



The application isolation metadata for this process or thread has become corrupt.


   

<span id="ERROR_SXS_EARLY_DEACTIVATION"></span><span id="error_sxs_early_deactivation"></span>**ERROR\_SXS\_EARLY\_DEACTIVATION**
   

14084 (0x3704)
 



The activation context being deactivated is not the most recently activated one.


   

<span id="ERROR_SXS_INVALID_DEACTIVATION"></span><span id="error_sxs_invalid_deactivation"></span>**ERROR\_SXS\_INVALID\_DEACTIVATION**
   

14085 (0x3705)
 



The activation context being deactivated is not active for the current thread of execution.


   

<span id="ERROR_SXS_MULTIPLE_DEACTIVATION"></span><span id="error_sxs_multiple_deactivation"></span>**ERROR\_SXS\_MULTIPLE\_DEACTIVATION**
   

14086 (0x3706)
 



The activation context being deactivated has already been deactivated.


   

<span id="ERROR_SXS_PROCESS_TERMINATION_REQUESTED"></span><span id="error_sxs_process_termination_requested"></span>**ERROR\_SXS\_PROCESS\_TERMINATION\_REQUESTED**
   

14087 (0x3707)
 



A component used by the isolation facility has requested to terminate the process.


   

<span id="ERROR_SXS_RELEASE_ACTIVATION_CONTEXT"></span><span id="error_sxs_release_activation_context"></span>**ERROR\_SXS\_RELEASE\_ACTIVATION\_CONTEXT**
   

14088 (0x3708)
 



A kernel mode component is releasing a reference on an activation context.


   

<span id="ERROR_SXS_SYSTEM_DEFAULT_ACTIVATION_CONTEXT_EMPTY"></span><span id="error_sxs_system_default_activation_context_empty"></span>**ERROR\_SXS\_SYSTEM\_DEFAULT\_ACTIVATION\_CONTEXT\_EMPTY**
   

14089 (0x3709)
 



The activation context of system default assembly could not be generated.


   

<span id="ERROR_SXS_INVALID_IDENTITY_ATTRIBUTE_VALUE"></span><span id="error_sxs_invalid_identity_attribute_value"></span>**ERROR\_SXS\_INVALID\_IDENTITY\_ATTRIBUTE\_VALUE**
   

14090 (0x370A)
 



The value of an attribute in an identity is not within the legal range.


   

<span id="ERROR_SXS_INVALID_IDENTITY_ATTRIBUTE_NAME"></span><span id="error_sxs_invalid_identity_attribute_name"></span>**ERROR\_SXS\_INVALID\_IDENTITY\_ATTRIBUTE\_NAME**
   

14091 (0x370B)
 



The name of an attribute in an identity is not within the legal range.


   

<span id="ERROR_SXS_IDENTITY_DUPLICATE_ATTRIBUTE"></span><span id="error_sxs_identity_duplicate_attribute"></span>**ERROR\_SXS\_IDENTITY\_DUPLICATE\_ATTRIBUTE**
   

14092 (0x370C)
 



An identity contains two definitions for the same attribute.


   

<span id="ERROR_SXS_IDENTITY_PARSE_ERROR"></span><span id="error_sxs_identity_parse_error"></span>**ERROR\_SXS\_IDENTITY\_PARSE\_ERROR**
   

14093 (0x370D)
 



The identity string is malformed. This may be due to a trailing comma, more than two unnamed attributes, missing attribute name or missing attribute value.


   

<span id="ERROR_MALFORMED_SUBSTITUTION_STRING"></span><span id="error_malformed_substitution_string"></span>**ERROR\_MALFORMED\_SUBSTITUTION\_STRING**
   

14094 (0x370E)
 



A string containing localized substitutable content was malformed. Either a dollar sign ($) was followed by something other than a left parenthesis or another dollar sign or an substitution's right parenthesis was not found.


   

<span id="ERROR_SXS_INCORRECT_PUBLIC_KEY_TOKEN"></span><span id="error_sxs_incorrect_public_key_token"></span>**ERROR\_SXS\_INCORRECT\_PUBLIC\_KEY\_TOKEN**
   

14095 (0x370F)
 



The public key token does not correspond to the public key specified.


   

<span id="ERROR_UNMAPPED_SUBSTITUTION_STRING"></span><span id="error_unmapped_substitution_string"></span>**ERROR\_UNMAPPED\_SUBSTITUTION\_STRING**
   

14096 (0x3710)
 



A substitution string had no mapping.


   

<span id="ERROR_SXS_ASSEMBLY_NOT_LOCKED"></span><span id="error_sxs_assembly_not_locked"></span>**ERROR\_SXS\_ASSEMBLY\_NOT\_LOCKED**
   

14097 (0x3711)
 



The component must be locked before making the request.


   

<span id="ERROR_SXS_COMPONENT_STORE_CORRUPT"></span><span id="error_sxs_component_store_corrupt"></span>**ERROR\_SXS\_COMPONENT\_STORE\_CORRUPT**
   

14098 (0x3712)
 



The component store has been corrupted.


   

<span id="ERROR_ADVANCED_INSTALLER_FAILED"></span><span id="error_advanced_installer_failed"></span>**ERROR\_ADVANCED\_INSTALLER\_FAILED**
   

14099 (0x3713)
 



An advanced installer failed during setup or servicing.


   

<span id="ERROR_XML_ENCODING_MISMATCH"></span><span id="error_xml_encoding_mismatch"></span>**ERROR\_XML\_ENCODING\_MISMATCH**
   

14100 (0x3714)
 



The character encoding in the XML declaration did not match the encoding used in the document.


   

<span id="ERROR_SXS_MANIFEST_IDENTITY_SAME_BUT_CONTENTS_DIFFERENT"></span><span id="error_sxs_manifest_identity_same_but_contents_different"></span>**ERROR\_SXS\_MANIFEST\_IDENTITY\_SAME\_BUT\_CONTENTS\_DIFFERENT**
   

14101 (0x3715)
 



The identities of the manifests are identical but their contents are different.


   

<span id="ERROR_SXS_IDENTITIES_DIFFERENT"></span><span id="error_sxs_identities_different"></span>**ERROR\_SXS\_IDENTITIES\_DIFFERENT**
   

14102 (0x3716)
 



The component identities are different.


   

<span id="ERROR_SXS_ASSEMBLY_IS_NOT_A_DEPLOYMENT"></span><span id="error_sxs_assembly_is_not_a_deployment"></span>**ERROR\_SXS\_ASSEMBLY\_IS\_NOT\_A\_DEPLOYMENT**
   

14103 (0x3717)
 



The assembly is not a deployment.


   

<span id="ERROR_SXS_FILE_NOT_PART_OF_ASSEMBLY"></span><span id="error_sxs_file_not_part_of_assembly"></span>**ERROR\_SXS\_FILE\_NOT\_PART\_OF\_ASSEMBLY**
   

14104 (0x3718)
 



The file is not a part of the assembly.


   

<span id="ERROR_SXS_MANIFEST_TOO_BIG"></span><span id="error_sxs_manifest_too_big"></span>**ERROR\_SXS\_MANIFEST\_TOO\_BIG**
   

14105 (0x3719)
 



The size of the manifest exceeds the maximum allowed.


   

<span id="ERROR_SXS_SETTING_NOT_REGISTERED"></span><span id="error_sxs_setting_not_registered"></span>**ERROR\_SXS\_SETTING\_NOT\_REGISTERED**
   

14106 (0x371A)
 



The setting is not registered.


   

<span id="ERROR_SXS_TRANSACTION_CLOSURE_INCOMPLETE"></span><span id="error_sxs_transaction_closure_incomplete"></span>**ERROR\_SXS\_TRANSACTION\_CLOSURE\_INCOMPLETE**
   

14107 (0x371B)
 



One or more required members of the transaction are not present.


   

<span id="ERROR_SMI_PRIMITIVE_INSTALLER_FAILED"></span><span id="error_smi_primitive_installer_failed"></span>**ERROR\_SMI\_PRIMITIVE\_INSTALLER\_FAILED**
   

14108 (0x371C)
 



The SMI primitive installer failed during setup or servicing.


   

<span id="ERROR_GENERIC_COMMAND_FAILED"></span><span id="error_generic_command_failed"></span>**ERROR\_GENERIC\_COMMAND\_FAILED**
   

14109 (0x371D)
 



A generic command executable returned a result that indicates failure.


   

<span id="ERROR_SXS_FILE_HASH_MISSING"></span><span id="error_sxs_file_hash_missing"></span>**ERROR\_SXS\_FILE\_HASH\_MISSING**
   

14110 (0x371E)
 



A component is missing file verification information in its manifest.


   

<span id="ERROR_EVT_INVALID_CHANNEL_PATH"></span><span id="error_evt_invalid_channel_path"></span>**ERROR\_EVT\_INVALID\_CHANNEL\_PATH**
   

15000 (0x3A98)
 



The specified channel path is invalid.


   

<span id="ERROR_EVT_INVALID_QUERY"></span><span id="error_evt_invalid_query"></span>**ERROR\_EVT\_INVALID\_QUERY**
   

15001 (0x3A99)
 



The specified query is invalid.


   

<span id="ERROR_EVT_PUBLISHER_METADATA_NOT_FOUND"></span><span id="error_evt_publisher_metadata_not_found"></span>**ERROR\_EVT\_PUBLISHER\_METADATA\_NOT\_FOUND**
   

15002 (0x3A9A)
 



The publisher metadata cannot be found in the resource.


   

<span id="ERROR_EVT_EVENT_TEMPLATE_NOT_FOUND"></span><span id="error_evt_event_template_not_found"></span>**ERROR\_EVT\_EVENT\_TEMPLATE\_NOT\_FOUND**
   

15003 (0x3A9B)
 



The template for an event definition cannot be found in the resource (error = %1).


   

<span id="ERROR_EVT_INVALID_PUBLISHER_NAME"></span><span id="error_evt_invalid_publisher_name"></span>**ERROR\_EVT\_INVALID\_PUBLISHER\_NAME**
   

15004 (0x3A9C)
 



The specified publisher name is invalid.


   

<span id="ERROR_EVT_INVALID_EVENT_DATA"></span><span id="error_evt_invalid_event_data"></span>**ERROR\_EVT\_INVALID\_EVENT\_DATA**
   

15005 (0x3A9D)
 



The event data raised by the publisher is not compatible with the event template definition in the publisher's manifest.


   

<span id="ERROR_EVT_CHANNEL_NOT_FOUND"></span><span id="error_evt_channel_not_found"></span>**ERROR\_EVT\_CHANNEL\_NOT\_FOUND**
   

15007 (0x3A9F)
 



The specified channel could not be found. Check channel configuration.


   

<span id="ERROR_EVT_MALFORMED_XML_TEXT"></span><span id="error_evt_malformed_xml_text"></span>**ERROR\_EVT\_MALFORMED\_XML\_TEXT**
   

15008 (0x3AA0)
 



The specified xml text was not well-formed. See Extended Error for more details.


   

<span id="ERROR_EVT_SUBSCRIPTION_TO_DIRECT_CHANNEL"></span><span id="error_evt_subscription_to_direct_channel"></span>**ERROR\_EVT\_SUBSCRIPTION\_TO\_DIRECT\_CHANNEL**
   

15009 (0x3AA1)
 



The caller is trying to subscribe to a direct channel which is not allowed. The events for a direct channel go directly to a logfile and cannot be subscribed to.


   

<span id="ERROR_EVT_CONFIGURATION_ERROR"></span><span id="error_evt_configuration_error"></span>**ERROR\_EVT\_CONFIGURATION\_ERROR**
   

15010 (0x3AA2)
 



Configuration error.


   

<span id="ERROR_EVT_QUERY_RESULT_STALE"></span><span id="error_evt_query_result_stale"></span>**ERROR\_EVT\_QUERY\_RESULT\_STALE**
   

15011 (0x3AA3)
 



The query result is stale / invalid. This may be due to the log being cleared or rolling over after the query result was created. Users should handle this code by releasing the query result object and reissuing the query.


   

<span id="ERROR_EVT_QUERY_RESULT_INVALID_POSITION"></span><span id="error_evt_query_result_invalid_position"></span>**ERROR\_EVT\_QUERY\_RESULT\_INVALID\_POSITION**
   

15012 (0x3AA4)
 



Query result is currently at an invalid position.


   

<span id="ERROR_EVT_NON_VALIDATING_MSXML"></span><span id="error_evt_non_validating_msxml"></span>**ERROR\_EVT\_NON\_VALIDATING\_MSXML**
   

15013 (0x3AA5)
 



Registered MSXML doesn't support validation.


   

<span id="ERROR_EVT_FILTER_ALREADYSCOPED"></span><span id="error_evt_filter_alreadyscoped"></span>**ERROR\_EVT\_FILTER\_ALREADYSCOPED**
   

15014 (0x3AA6)
 



An expression can only be followed by a change of scope operation if it itself evaluates to a node set and is not already part of some other change of scope operation.


   

<span id="ERROR_EVT_FILTER_NOTELTSET"></span><span id="error_evt_filter_noteltset"></span>**ERROR\_EVT\_FILTER\_NOTELTSET**
   

15015 (0x3AA7)
 



Can't perform a step operation from a term that does not represent an element set.


   

<span id="ERROR_EVT_FILTER_INVARG"></span><span id="error_evt_filter_invarg"></span>**ERROR\_EVT\_FILTER\_INVARG**
   

15016 (0x3AA8)
 



Left hand side arguments to binary operators must be either attributes, nodes or variables and right hand side arguments must be constants.


   

<span id="ERROR_EVT_FILTER_INVTEST"></span><span id="error_evt_filter_invtest"></span>**ERROR\_EVT\_FILTER\_INVTEST**
   

15017 (0x3AA9)
 



A step operation must involve either a node test or, in the case of a predicate, an algebraic expression against which to test each node in the node set identified by the preceding node set can be evaluated.


   

<span id="ERROR_EVT_FILTER_INVTYPE"></span><span id="error_evt_filter_invtype"></span>**ERROR\_EVT\_FILTER\_INVTYPE**
   

15018 (0x3AAA)
 



This data type is currently unsupported.


   

<span id="ERROR_EVT_FILTER_PARSEERR"></span><span id="error_evt_filter_parseerr"></span>**ERROR\_EVT\_FILTER\_PARSEERR**
   

15019 (0x3AAB)
 



A syntax error occurred at position %1!d!.


   

<span id="ERROR_EVT_FILTER_UNSUPPORTEDOP"></span><span id="error_evt_filter_unsupportedop"></span>**ERROR\_EVT\_FILTER\_UNSUPPORTEDOP**
   

15020 (0x3AAC)
 



This operator is unsupported by this implementation of the filter.


   

<span id="ERROR_EVT_FILTER_UNEXPECTEDTOKEN"></span><span id="error_evt_filter_unexpectedtoken"></span>**ERROR\_EVT\_FILTER\_UNEXPECTEDTOKEN**
   

15021 (0x3AAD)
 



The token encountered was unexpected.


   

<span id="ERROR_EVT_INVALID_OPERATION_OVER_ENABLED_DIRECT_CHANNEL"></span><span id="error_evt_invalid_operation_over_enabled_direct_channel"></span>**ERROR\_EVT\_INVALID\_OPERATION\_OVER\_ENABLED\_DIRECT\_CHANNEL**
   

15022 (0x3AAE)
 



The requested operation cannot be performed over an enabled direct channel. The channel must first be disabled before performing the requested operation.


   

<span id="ERROR_EVT_INVALID_CHANNEL_PROPERTY_VALUE"></span><span id="error_evt_invalid_channel_property_value"></span>**ERROR\_EVT\_INVALID\_CHANNEL\_PROPERTY\_VALUE**
   

15023 (0x3AAF)
 



Channel property %1!s! contains invalid value. The value has invalid type, is outside of valid range, can't be updated or is not supported by this type of channel.


   

<span id="ERROR_EVT_INVALID_PUBLISHER_PROPERTY_VALUE"></span><span id="error_evt_invalid_publisher_property_value"></span>**ERROR\_EVT\_INVALID\_PUBLISHER\_PROPERTY\_VALUE**
   

15024 (0x3AB0)
 



Publisher property %1!s! contains invalid value. The value has invalid type, is outside of valid range, can't be updated or is not supported by this type of publisher.


   

<span id="ERROR_EVT_CHANNEL_CANNOT_ACTIVATE"></span><span id="error_evt_channel_cannot_activate"></span>**ERROR\_EVT\_CHANNEL\_CANNOT\_ACTIVATE**
   

15025 (0x3AB1)
 



The channel fails to activate.


   

<span id="ERROR_EVT_FILTER_TOO_COMPLEX"></span><span id="error_evt_filter_too_complex"></span>**ERROR\_EVT\_FILTER\_TOO\_COMPLEX**
   

15026 (0x3AB2)
 



The xpath expression exceeded supported complexity. Please simplify it or split it into two or more simple expressions.


   

<span id="ERROR_EVT_MESSAGE_NOT_FOUND"></span><span id="error_evt_message_not_found"></span>**ERROR\_EVT\_MESSAGE\_NOT\_FOUND**
   

15027 (0x3AB3)
 



the message resource is present but the message is not found in the string/message table.


   

<span id="ERROR_EVT_MESSAGE_ID_NOT_FOUND"></span><span id="error_evt_message_id_not_found"></span>**ERROR\_EVT\_MESSAGE\_ID\_NOT\_FOUND**
   

15028 (0x3AB4)
 



The message id for the desired message could not be found.


   

<span id="ERROR_EVT_UNRESOLVED_VALUE_INSERT"></span><span id="error_evt_unresolved_value_insert"></span>**ERROR\_EVT\_UNRESOLVED\_VALUE\_INSERT**
   

15029 (0x3AB5)
 



The substitution string for insert index (%1) could not be found.


   

<span id="ERROR_EVT_UNRESOLVED_PARAMETER_INSERT"></span><span id="error_evt_unresolved_parameter_insert"></span>**ERROR\_EVT\_UNRESOLVED\_PARAMETER\_INSERT**
   

15030 (0x3AB6)
 



The description string for parameter reference (%1) could not be found.


   

<span id="ERROR_EVT_MAX_INSERTS_REACHED"></span><span id="error_evt_max_inserts_reached"></span>**ERROR\_EVT\_MAX\_INSERTS\_REACHED**
   

15031 (0x3AB7)
 



The maximum number of replacements has been reached.


   

<span id="ERROR_EVT_EVENT_DEFINITION_NOT_FOUND"></span><span id="error_evt_event_definition_not_found"></span>**ERROR\_EVT\_EVENT\_DEFINITION\_NOT\_FOUND**
   

15032 (0x3AB8)
 



The event definition could not be found for event id (%1).


   

<span id="ERROR_EVT_MESSAGE_LOCALE_NOT_FOUND"></span><span id="error_evt_message_locale_not_found"></span>**ERROR\_EVT\_MESSAGE\_LOCALE\_NOT\_FOUND**
   

15033 (0x3AB9)
 



The locale specific resource for the desired message is not present.


   

<span id="ERROR_EVT_VERSION_TOO_OLD"></span><span id="error_evt_version_too_old"></span>**ERROR\_EVT\_VERSION\_TOO\_OLD**
   

15034 (0x3ABA)
 



The resource is too old to be compatible.


   

<span id="ERROR_EVT_VERSION_TOO_NEW"></span><span id="error_evt_version_too_new"></span>**ERROR\_EVT\_VERSION\_TOO\_NEW**
   

15035 (0x3ABB)
 



The resource is too new to be compatible.


   

<span id="ERROR_EVT_CANNOT_OPEN_CHANNEL_OF_QUERY"></span><span id="error_evt_cannot_open_channel_of_query"></span>**ERROR\_EVT\_CANNOT\_OPEN\_CHANNEL\_OF\_QUERY**
   

15036 (0x3ABC)
 



The channel at index %1!d! of the query can't be opened.


   

<span id="ERROR_EVT_PUBLISHER_DISABLED"></span><span id="error_evt_publisher_disabled"></span>**ERROR\_EVT\_PUBLISHER\_DISABLED**
   

15037 (0x3ABD)
 



The publisher has been disabled and its resource is not available. This usually occurs when the publisher is in the process of being uninstalled or upgraded.


   

<span id="ERROR_EVT_FILTER_OUT_OF_RANGE"></span><span id="error_evt_filter_out_of_range"></span>**ERROR\_EVT\_FILTER\_OUT\_OF\_RANGE**
   

15038 (0x3ABE)
 



Attempted to create a numeric type that is outside of its valid range.


   

<span id="ERROR_EC_SUBSCRIPTION_CANNOT_ACTIVATE"></span><span id="error_ec_subscription_cannot_activate"></span>**ERROR\_EC\_SUBSCRIPTION\_CANNOT\_ACTIVATE**
   

15080 (0x3AE8)
 



The subscription fails to activate.


   

<span id="ERROR_EC_LOG_DISABLED"></span><span id="error_ec_log_disabled"></span>**ERROR\_EC\_LOG\_DISABLED**
   

15081 (0x3AE9)
 



The log of the subscription is in disabled state, and cannot be used to forward events to. The log must first be enabled before the subscription can be activated.


   

<span id="ERROR_EC_CIRCULAR_FORWARDING"></span><span id="error_ec_circular_forwarding"></span>**ERROR\_EC\_CIRCULAR\_FORWARDING**
   

15082 (0x3AEA)
 



When forwarding events from local machine to itself, the query of the subscription can't contain target log of the subscription.


   

<span id="ERROR_EC_CREDSTORE_FULL"></span><span id="error_ec_credstore_full"></span>**ERROR\_EC\_CREDSTORE\_FULL**
   

15083 (0x3AEB)
 



The credential store that is used to save credentials is full.


   

<span id="ERROR_EC_CRED_NOT_FOUND"></span><span id="error_ec_cred_not_found"></span>**ERROR\_EC\_CRED\_NOT\_FOUND**
   

15084 (0x3AEC)
 



The credential used by this subscription can't be found in credential store.


   

<span id="ERROR_EC_NO_ACTIVE_CHANNEL"></span><span id="error_ec_no_active_channel"></span>**ERROR\_EC\_NO\_ACTIVE\_CHANNEL**
   

15085 (0x3AED)
 



No active channel is found for the query.


   

<span id="ERROR_MUI_FILE_NOT_FOUND"></span><span id="error_mui_file_not_found"></span>**ERROR\_MUI\_FILE\_NOT\_FOUND**
   

15100 (0x3AFC)
 



The resource loader failed to find MUI file.


   

<span id="ERROR_MUI_INVALID_FILE"></span><span id="error_mui_invalid_file"></span>**ERROR\_MUI\_INVALID\_FILE**
   

15101 (0x3AFD)
 



The resource loader failed to load MUI file because the file fail to pass validation.


   

<span id="ERROR_MUI_INVALID_RC_CONFIG"></span><span id="error_mui_invalid_rc_config"></span>**ERROR\_MUI\_INVALID\_RC\_CONFIG**
   

15102 (0x3AFE)
 



The RC Manifest is corrupted with garbage data or unsupported version or missing required item.


   

<span id="ERROR_MUI_INVALID_LOCALE_NAME"></span><span id="error_mui_invalid_locale_name"></span>**ERROR\_MUI\_INVALID\_LOCALE\_NAME**
   

15103 (0x3AFF)
 



The RC Manifest has invalid culture name.


   

<span id="ERROR_MUI_INVALID_ULTIMATEFALLBACK_NAME"></span><span id="error_mui_invalid_ultimatefallback_name"></span>**ERROR\_MUI\_INVALID\_ULTIMATEFALLBACK\_NAME**
   

15104 (0x3B00)
 



The RC Manifest has invalid ultimatefallback name.


   

<span id="ERROR_MUI_FILE_NOT_LOADED"></span><span id="error_mui_file_not_loaded"></span>**ERROR\_MUI\_FILE\_NOT\_LOADED**
   

15105 (0x3B01)
 



The resource loader cache doesn't have loaded MUI entry.


   

<span id="ERROR_RESOURCE_ENUM_USER_STOP"></span><span id="error_resource_enum_user_stop"></span>**ERROR\_RESOURCE\_ENUM\_USER\_STOP**
   

15106 (0x3B02)
 



User stopped resource enumeration.


   

<span id="ERROR_MUI_INTLSETTINGS_UILANG_NOT_INSTALLED"></span><span id="error_mui_intlsettings_uilang_not_installed"></span>**ERROR\_MUI\_INTLSETTINGS\_UILANG\_NOT\_INSTALLED**
   

15107 (0x3B03)
 



UI language installation failed.


   

<span id="ERROR_MUI_INTLSETTINGS_INVALID_LOCALE_NAME"></span><span id="error_mui_intlsettings_invalid_locale_name"></span>**ERROR\_MUI\_INTLSETTINGS\_INVALID\_LOCALE\_NAME**
   

15108 (0x3B04)
 



Locale installation failed.


   

<span id="ERROR_MRM_RUNTIME_NO_DEFAULT_OR_NEUTRAL_RESOURCE"></span><span id="error_mrm_runtime_no_default_or_neutral_resource"></span>**ERROR\_MRM\_RUNTIME\_NO\_DEFAULT\_OR\_NEUTRAL\_RESOURCE**
   

15110 (0x3B06)
 



A resource does not have default or neutral value.


   

<span id="ERROR_MRM_INVALID_PRICONFIG"></span><span id="error_mrm_invalid_priconfig"></span>**ERROR\_MRM\_INVALID\_PRICONFIG**
   

15111 (0x3B07)
 



Invalid PRI config file.


   

<span id="ERROR_MRM_INVALID_FILE_TYPE"></span><span id="error_mrm_invalid_file_type"></span>**ERROR\_MRM\_INVALID\_FILE\_TYPE**
   

15112 (0x3B08)
 



Invalid file type.


   

<span id="ERROR_MRM_UNKNOWN_QUALIFIER"></span><span id="error_mrm_unknown_qualifier"></span>**ERROR\_MRM\_UNKNOWN\_QUALIFIER**
   

15113 (0x3B09)
 



Unknown qualifier.


   

<span id="ERROR_MRM_INVALID_QUALIFIER_VALUE"></span><span id="error_mrm_invalid_qualifier_value"></span>**ERROR\_MRM\_INVALID\_QUALIFIER\_VALUE**
   

15114 (0x3B0A)
 



Invalid qualifier value.


   

<span id="ERROR_MRM_NO_CANDIDATE"></span><span id="error_mrm_no_candidate"></span>**ERROR\_MRM\_NO\_CANDIDATE**
   

15115 (0x3B0B)
 



No Candidate found.


   

<span id="ERROR_MRM_NO_MATCH_OR_DEFAULT_CANDIDATE"></span><span id="error_mrm_no_match_or_default_candidate"></span>**ERROR\_MRM\_NO\_MATCH\_OR\_DEFAULT\_CANDIDATE**
   

15116 (0x3B0C)
 



The ResourceMap or NamedResource has an item that does not have default or neutral resource..


   

<span id="ERROR_MRM_RESOURCE_TYPE_MISMATCH"></span><span id="error_mrm_resource_type_mismatch"></span>**ERROR\_MRM\_RESOURCE\_TYPE\_MISMATCH**
   

15117 (0x3B0D)
 



Invalid ResourceCandidate type.


   

<span id="ERROR_MRM_DUPLICATE_MAP_NAME"></span><span id="error_mrm_duplicate_map_name"></span>**ERROR\_MRM\_DUPLICATE\_MAP\_NAME**
   

15118 (0x3B0E)
 



Duplicate Resource Map.


   

<span id="ERROR_MRM_DUPLICATE_ENTRY"></span><span id="error_mrm_duplicate_entry"></span>**ERROR\_MRM\_DUPLICATE\_ENTRY**
   

15119 (0x3B0F)
 



Duplicate Entry.


   

<span id="ERROR_MRM_INVALID_RESOURCE_IDENTIFIER"></span><span id="error_mrm_invalid_resource_identifier"></span>**ERROR\_MRM\_INVALID\_RESOURCE\_IDENTIFIER**
   

15120 (0x3B10)
 



Invalid Resource Identifier.


   

<span id="ERROR_MRM_FILEPATH_TOO_LONG"></span><span id="error_mrm_filepath_too_long"></span>**ERROR\_MRM\_FILEPATH\_TOO\_LONG**
   

15121 (0x3B11)
 



Filepath too long.


   

<span id="ERROR_MRM_UNSUPPORTED_DIRECTORY_TYPE"></span><span id="error_mrm_unsupported_directory_type"></span>**ERROR\_MRM\_UNSUPPORTED\_DIRECTORY\_TYPE**
   

15122 (0x3B12)
 



Unsupported directory type.


   

<span id="ERROR_MRM_INVALID_PRI_FILE"></span><span id="error_mrm_invalid_pri_file"></span>**ERROR\_MRM\_INVALID\_PRI\_FILE**
   

15126 (0x3B16)
 



Invalid PRI File.


   

<span id="ERROR_MRM_NAMED_RESOURCE_NOT_FOUND"></span><span id="error_mrm_named_resource_not_found"></span>**ERROR\_MRM\_NAMED\_RESOURCE\_NOT\_FOUND**
   

15127 (0x3B17)
 



NamedResource Not Found.


   

<span id="ERROR_MRM_MAP_NOT_FOUND"></span><span id="error_mrm_map_not_found"></span>**ERROR\_MRM\_MAP\_NOT\_FOUND**
   

15135 (0x3B1F)
 



ResourceMap Not Found.


   

<span id="ERROR_MRM_UNSUPPORTED_PROFILE_TYPE"></span><span id="error_mrm_unsupported_profile_type"></span>**ERROR\_MRM\_UNSUPPORTED\_PROFILE\_TYPE**
   

15136 (0x3B20)
 



Unsupported MRT profile type.


   

<span id="ERROR_MRM_INVALID_QUALIFIER_OPERATOR"></span><span id="error_mrm_invalid_qualifier_operator"></span>**ERROR\_MRM\_INVALID\_QUALIFIER\_OPERATOR**
   

15137 (0x3B21)
 



Invalid qualifier operator.


   

<span id="ERROR_MRM_INDETERMINATE_QUALIFIER_VALUE"></span><span id="error_mrm_indeterminate_qualifier_value"></span>**ERROR\_MRM\_INDETERMINATE\_QUALIFIER\_VALUE**
   

15138 (0x3B22)
 



Unable to determine qualifier value or qualifier value has not been set.


   

<span id="ERROR_MRM_AUTOMERGE_ENABLED"></span><span id="error_mrm_automerge_enabled"></span>**ERROR\_MRM\_AUTOMERGE\_ENABLED**
   

15139 (0x3B23)
 



Automerge is enabled in the PRI file.


   

<span id="ERROR_MRM_TOO_MANY_RESOURCES"></span><span id="error_mrm_too_many_resources"></span>**ERROR\_MRM\_TOO\_MANY\_RESOURCES**
   

15140 (0x3B24)
 



Too many resources defined for package.


   

<span id="ERROR_MCA_INVALID_CAPABILITIES_STRING"></span><span id="error_mca_invalid_capabilities_string"></span>**ERROR\_MCA\_INVALID\_CAPABILITIES\_STRING**
   

15200 (0x3B60)
 



The monitor returned a DDC/CI capabilities string that did not comply with the ACCESS.bus 3.0, DDC/CI 1.1 or MCCS 2 Revision 1 specification.


   

<span id="ERROR_MCA_INVALID_VCP_VERSION"></span><span id="error_mca_invalid_vcp_version"></span>**ERROR\_MCA\_INVALID\_VCP\_VERSION**
   

15201 (0x3B61)
 



The monitor's VCP Version (0xDF) VCP code returned an invalid version value.


   

<span id="ERROR_MCA_MONITOR_VIOLATES_MCCS_SPECIFICATION"></span><span id="error_mca_monitor_violates_mccs_specification"></span>**ERROR\_MCA\_MONITOR\_VIOLATES\_MCCS\_SPECIFICATION**
   

15202 (0x3B62)
 



The monitor does not comply with the MCCS specification it claims to support.


   

<span id="ERROR_MCA_MCCS_VERSION_MISMATCH"></span><span id="error_mca_mccs_version_mismatch"></span>**ERROR\_MCA\_MCCS\_VERSION\_MISMATCH**
   

15203 (0x3B63)
 



The MCCS version in a monitor's mccs\_ver capability does not match the MCCS version the monitor reports when the VCP Version (0xDF) VCP code is used.


   

<span id="ERROR_MCA_UNSUPPORTED_MCCS_VERSION"></span><span id="error_mca_unsupported_mccs_version"></span>**ERROR\_MCA\_UNSUPPORTED\_MCCS\_VERSION**
   

15204 (0x3B64)
 



The Monitor Configuration API only works with monitors that support the MCCS 1.0 specification, MCCS 2.0 specification or the MCCS 2.0 Revision 1 specification.


   

<span id="ERROR_MCA_INTERNAL_ERROR"></span><span id="error_mca_internal_error"></span>**ERROR\_MCA\_INTERNAL\_ERROR**
   

15205 (0x3B65)
 



An internal Monitor Configuration API error occurred.


   

<span id="ERROR_MCA_INVALID_TECHNOLOGY_TYPE_RETURNED"></span><span id="error_mca_invalid_technology_type_returned"></span>**ERROR\_MCA\_INVALID\_TECHNOLOGY\_TYPE\_RETURNED**
   

15206 (0x3B66)
 



The monitor returned an invalid monitor technology type. CRT, Plasma and LCD (TFT) are examples of monitor technology types. This error implies that the monitor violated the MCCS 2.0 or MCCS 2.0 Revision 1 specification.


   

<span id="ERROR_MCA_UNSUPPORTED_COLOR_TEMPERATURE"></span><span id="error_mca_unsupported_color_temperature"></span>**ERROR\_MCA\_UNSUPPORTED\_COLOR\_TEMPERATURE**
   

15207 (0x3B67)
 



The caller of [**SetMonitorColorTemperature**](/windows/win32/api/highlevelmonitorconfigurationapi/nf-highlevelmonitorconfigurationapi-setmonitorcolortemperature) specified a color temperature that the current monitor did not support. This error implies that the monitor violated the MCCS 2.0 or MCCS 2.0 Revision 1 specification.


   

<span id="ERROR_AMBIGUOUS_SYSTEM_DEVICE"></span><span id="error_ambiguous_system_device"></span>**ERROR\_AMBIGUOUS\_SYSTEM\_DEVICE**
   

15250 (0x3B92)
 



The requested system device cannot be identified due to multiple indistinguishable devices potentially matching the identification criteria.


   

<span id="ERROR_SYSTEM_DEVICE_NOT_FOUND"></span><span id="error_system_device_not_found"></span>**ERROR\_SYSTEM\_DEVICE\_NOT\_FOUND**
   

15299 (0x3BC3)
 



The requested system device cannot be found.


   

<span id="ERROR_HASH_NOT_SUPPORTED"></span><span id="error_hash_not_supported"></span>**ERROR\_HASH\_NOT\_SUPPORTED**
   

15300 (0x3BC4)
 



Hash generation for the specified hash version and hash type is not enabled on the server.


   

<span id="ERROR_HASH_NOT_PRESENT"></span><span id="error_hash_not_present"></span>**ERROR\_HASH\_NOT\_PRESENT**
   

15301 (0x3BC5)
 



The hash requested from the server is not available or no longer valid.


   

<span id="ERROR_SECONDARY_IC_PROVIDER_NOT_REGISTERED"></span><span id="error_secondary_ic_provider_not_registered"></span>**ERROR\_SECONDARY\_IC\_PROVIDER\_NOT\_REGISTERED**
   

15321 (0x3BD9)
 



The secondary interrupt controller instance that manages the specified interrupt is not registered.


   

<span id="ERROR_GPIO_CLIENT_INFORMATION_INVALID"></span><span id="error_gpio_client_information_invalid"></span>**ERROR\_GPIO\_CLIENT\_INFORMATION\_INVALID**
   

15322 (0x3BDA)
 



The information supplied by the GPIO client driver is invalid.


   

<span id="ERROR_GPIO_VERSION_NOT_SUPPORTED"></span><span id="error_gpio_version_not_supported"></span>**ERROR\_GPIO\_VERSION\_NOT\_SUPPORTED**
   

15323 (0x3BDB)
 



The version specified by the GPIO client driver is not supported.


   

<span id="ERROR_GPIO_INVALID_REGISTRATION_PACKET"></span><span id="error_gpio_invalid_registration_packet"></span>**ERROR\_GPIO\_INVALID\_REGISTRATION\_PACKET**
   

15324 (0x3BDC)
 



The registration packet supplied by the GPIO client driver is not valid.


   

<span id="ERROR_GPIO_OPERATION_DENIED"></span><span id="error_gpio_operation_denied"></span>**ERROR\_GPIO\_OPERATION\_DENIED**
   

15325 (0x3BDD)
 



The requested operation is not supported for the specified handle.


   

<span id="ERROR_GPIO_INCOMPATIBLE_CONNECT_MODE"></span><span id="error_gpio_incompatible_connect_mode"></span>**ERROR\_GPIO\_INCOMPATIBLE\_CONNECT\_MODE**
   

15326 (0x3BDE)
 



The requested connect mode conflicts with an existing mode on one or more of the specified pins.


   

<span id="ERROR_GPIO_INTERRUPT_ALREADY_UNMASKED"></span><span id="error_gpio_interrupt_already_unmasked"></span>**ERROR\_GPIO\_INTERRUPT\_ALREADY\_UNMASKED**
   

15327 (0x3BDF)
 



The interrupt requested to be unmasked is not masked.


   

<span id="ERROR_CANNOT_SWITCH_RUNLEVEL"></span><span id="error_cannot_switch_runlevel"></span>**ERROR\_CANNOT\_SWITCH\_RUNLEVEL**
   

15400 (0x3C28)
 



The requested run level switch cannot be completed successfully.


   

<span id="ERROR_INVALID_RUNLEVEL_SETTING"></span><span id="error_invalid_runlevel_setting"></span>**ERROR\_INVALID\_RUNLEVEL\_SETTING**
   

15401 (0x3C29)
 



The service has an invalid run level setting. The run level for a service must not be higher than the run level of its dependent services.


   

<span id="ERROR_RUNLEVEL_SWITCH_TIMEOUT"></span><span id="error_runlevel_switch_timeout"></span>**ERROR\_RUNLEVEL\_SWITCH\_TIMEOUT**
   

15402 (0x3C2A)
 



The requested run level switch cannot be completed successfully since one or more services will not stop or restart within the specified timeout.


   

<span id="ERROR_RUNLEVEL_SWITCH_AGENT_TIMEOUT"></span><span id="error_runlevel_switch_agent_timeout"></span>**ERROR\_RUNLEVEL\_SWITCH\_AGENT\_TIMEOUT**
   

15403 (0x3C2B)
 



A run level switch agent did not respond within the specified timeout.


   

<span id="ERROR_RUNLEVEL_SWITCH_IN_PROGRESS"></span><span id="error_runlevel_switch_in_progress"></span>**ERROR\_RUNLEVEL\_SWITCH\_IN\_PROGRESS**
   

15404 (0x3C2C)
 



A run level switch is currently in progress.


   

<span id="ERROR_SERVICES_FAILED_AUTOSTART"></span><span id="error_services_failed_autostart"></span>**ERROR\_SERVICES\_FAILED\_AUTOSTART**
   

15405 (0x3C2D)
 



One or more services failed to start during the service startup phase of a run level switch.


   

<span id="ERROR_COM_TASK_STOP_PENDING"></span><span id="error_com_task_stop_pending"></span>**ERROR\_COM\_TASK\_STOP\_PENDING**
   

15501 (0x3C8D)
 



The task stop request cannot be completed immediately since task needs more time to shutdown.


   

<span id="ERROR_INSTALL_OPEN_PACKAGE_FAILED"></span><span id="error_install_open_package_failed"></span>**ERROR\_INSTALL\_OPEN\_PACKAGE\_FAILED**
   

15600 (0x3CF0)
 



Package could not be opened.


   

<span id="ERROR_INSTALL_PACKAGE_NOT_FOUND"></span><span id="error_install_package_not_found"></span>**ERROR\_INSTALL\_PACKAGE\_NOT\_FOUND**
   

15601 (0x3CF1)
 



Package was not found.


   

<span id="ERROR_INSTALL_INVALID_PACKAGE"></span><span id="error_install_invalid_package"></span>**ERROR\_INSTALL\_INVALID\_PACKAGE**
   

15602 (0x3CF2)
 



Package data is invalid.


   

<span id="ERROR_INSTALL_RESOLVE_DEPENDENCY_FAILED"></span><span id="error_install_resolve_dependency_failed"></span>**ERROR\_INSTALL\_RESOLVE\_DEPENDENCY\_FAILED**
   

15603 (0x3CF3)
 



Package failed updates, dependency or conflict validation.


   

<span id="ERROR_INSTALL_OUT_OF_DISK_SPACE"></span><span id="error_install_out_of_disk_space"></span>**ERROR\_INSTALL\_OUT\_OF\_DISK\_SPACE**
   

15604 (0x3CF4)
 



There is not enough disk space on your computer. Please free up some space and try again.


   

<span id="ERROR_INSTALL_NETWORK_FAILURE"></span><span id="error_install_network_failure"></span>**ERROR\_INSTALL\_NETWORK\_FAILURE**
   

15605 (0x3CF5)
 



There was a problem downloading your product.


   

<span id="ERROR_INSTALL_REGISTRATION_FAILURE"></span><span id="error_install_registration_failure"></span>**ERROR\_INSTALL\_REGISTRATION\_FAILURE**
   

15606 (0x3CF6)
 



Package could not be registered.


   

<span id="ERROR_INSTALL_DEREGISTRATION_FAILURE"></span><span id="error_install_deregistration_failure"></span>**ERROR\_INSTALL\_DEREGISTRATION\_FAILURE**
   

15607 (0x3CF7)
 



Package could not be unregistered.


   

<span id="ERROR_INSTALL_CANCEL"></span><span id="error_install_cancel"></span>**ERROR\_INSTALL\_CANCEL**
   

15608 (0x3CF8)
 



User cancelled the install request.


   

<span id="ERROR_INSTALL_FAILED"></span><span id="error_install_failed"></span>**ERROR\_INSTALL\_FAILED**
   

15609 (0x3CF9)
 



Install failed. Please contact your software vendor.


   

<span id="ERROR_REMOVE_FAILED"></span><span id="error_remove_failed"></span>**ERROR\_REMOVE\_FAILED**
   

15610 (0x3CFA)
 



Removal failed. Please contact your software vendor.


   

<span id="ERROR_PACKAGE_ALREADY_EXISTS"></span><span id="error_package_already_exists"></span>**ERROR\_PACKAGE\_ALREADY\_EXISTS**
   

15611 (0x3CFB)
 



The provided package is already installed, and reinstallation of the package was blocked. Check the AppXDeployment-Server event log for details.


   

<span id="ERROR_NEEDS_REMEDIATION"></span><span id="error_needs_remediation"></span>**ERROR\_NEEDS\_REMEDIATION**
   

15612 (0x3CFC)
 



The application cannot be started. Try reinstalling the application to fix the problem.


   

<span id="ERROR_INSTALL_PREREQUISITE_FAILED"></span><span id="error_install_prerequisite_failed"></span>**ERROR\_INSTALL\_PREREQUISITE\_FAILED**
   

15613 (0x3CFD)
 



A Prerequisite for an install could not be satisfied.


   

<span id="ERROR_PACKAGE_REPOSITORY_CORRUPTED"></span><span id="error_package_repository_corrupted"></span>**ERROR\_PACKAGE\_REPOSITORY\_CORRUPTED**
   

15614 (0x3CFE)
 



The package repository is corrupted.


   

<span id="ERROR_INSTALL_POLICY_FAILURE"></span><span id="error_install_policy_failure"></span>**ERROR\_INSTALL\_POLICY\_FAILURE**
   

15615 (0x3CFF)
 



To install this application you need either a Windows developer license or a sideloading-enabled system.


   

<span id="ERROR_PACKAGE_UPDATING"></span><span id="error_package_updating"></span>**ERROR\_PACKAGE\_UPDATING**
   

15616 (0x3D00)
 



The application cannot be started because it is currently updating.


   

<span id="ERROR_DEPLOYMENT_BLOCKED_BY_POLICY"></span><span id="error_deployment_blocked_by_policy"></span>**ERROR\_DEPLOYMENT\_BLOCKED\_BY\_POLICY**
   

15617 (0x3D01)
 



The package deployment operation is blocked by policy. Please contact your system administrator.


   

<span id="ERROR_PACKAGES_IN_USE"></span><span id="error_packages_in_use"></span>**ERROR\_PACKAGES\_IN\_USE**
   

15618 (0x3D02)
 



The package could not be installed because resources it modifies are currently in use.


   

<span id="ERROR_RECOVERY_FILE_CORRUPT"></span><span id="error_recovery_file_corrupt"></span>**ERROR\_RECOVERY\_FILE\_CORRUPT**
   

15619 (0x3D03)
 



The package could not be recovered because necessary data for recovery have been corrupted.


   

<span id="ERROR_INVALID_STAGED_SIGNATURE"></span><span id="error_invalid_staged_signature"></span>**ERROR\_INVALID\_STAGED\_SIGNATURE**
   

15620 (0x3D04)
 



The signature is invalid. To register in developer mode, AppxSignature.p7x and AppxBlockMap.xml must be valid or should not be present.


   

<span id="ERROR_DELETING_EXISTING_APPLICATIONDATA_STORE_FAILED"></span><span id="error_deleting_existing_applicationdata_store_failed"></span>**ERROR\_DELETING\_EXISTING\_APPLICATIONDATA\_STORE\_FAILED**
   

15621 (0x3D05)
 



An error occurred while deleting the package's previously existing application data.


   

<span id="ERROR_INSTALL_PACKAGE_DOWNGRADE"></span><span id="error_install_package_downgrade"></span>**ERROR\_INSTALL\_PACKAGE\_DOWNGRADE**
   

15622 (0x3D06)
 



The package could not be installed because a higher version of this package is already installed.


   

<span id="ERROR_SYSTEM_NEEDS_REMEDIATION"></span><span id="error_system_needs_remediation"></span>**ERROR\_SYSTEM\_NEEDS\_REMEDIATION**
   

15623 (0x3D07)
 



An error in a system binary was detected. Try refreshing the PC to fix the problem.


   

<span id="ERROR_APPX_INTEGRITY_FAILURE_CLR_NGEN"></span><span id="error_appx_integrity_failure_clr_ngen"></span>**ERROR\_APPX\_INTEGRITY\_FAILURE\_CLR\_NGEN**
   

15624 (0x3D08)
 



A corrupted CLR NGEN binary was detected on the system.


   

<span id="ERROR_RESILIENCY_FILE_CORRUPT"></span><span id="error_resiliency_file_corrupt"></span>**ERROR\_RESILIENCY\_FILE\_CORRUPT**
   

15625 (0x3D09)
 



The operation could not be resumed because necessary data for recovery have been corrupted.


   

<span id="ERROR_INSTALL_FIREWALL_SERVICE_NOT_RUNNING"></span><span id="error_install_firewall_service_not_running"></span>**ERROR\_INSTALL\_FIREWALL\_SERVICE\_NOT\_RUNNING**
   

15626 (0x3D0A)
 



The package could not be installed because the Windows Firewall service is not running. Enable the Windows Firewall service and try again.


   

<span id="APPMODEL_ERROR_NO_PACKAGE"></span><span id="appmodel_error_no_package"></span>**APPMODEL\_ERROR\_NO\_PACKAGE**
   

15700 (0x3D54)
 



The process has no package identity.


   

<span id="APPMODEL_ERROR_PACKAGE_RUNTIME_CORRUPT"></span><span id="appmodel_error_package_runtime_corrupt"></span>**APPMODEL\_ERROR\_PACKAGE\_RUNTIME\_CORRUPT**
   

15701 (0x3D55)
 



The package runtime information is corrupted.


   

<span id="APPMODEL_ERROR_PACKAGE_IDENTITY_CORRUPT"></span><span id="appmodel_error_package_identity_corrupt"></span>**APPMODEL\_ERROR\_PACKAGE\_IDENTITY\_CORRUPT**
   

15702 (0x3D56)
 



The package identity is corrupted.


   

<span id="APPMODEL_ERROR_NO_APPLICATION"></span><span id="appmodel_error_no_application"></span>**APPMODEL\_ERROR\_NO\_APPLICATION**
   

15703 (0x3D57)
 



The process has no application identity.


   

<span id="ERROR_STATE_LOAD_STORE_FAILED"></span><span id="error_state_load_store_failed"></span>**ERROR\_STATE\_LOAD\_STORE\_FAILED**
   

15800 (0x3DB8)
 



Loading the state store failed.


   

<span id="ERROR_STATE_GET_VERSION_FAILED"></span><span id="error_state_get_version_failed"></span>**ERROR\_STATE\_GET\_VERSION\_FAILED**
   

15801 (0x3DB9)
 



Retrieving the state version for the application failed.


   

<span id="ERROR_STATE_SET_VERSION_FAILED"></span><span id="error_state_set_version_failed"></span>**ERROR\_STATE\_SET\_VERSION\_FAILED**
   

15802 (0x3DBA)
 



Setting the state version for the application failed.


   

<span id="ERROR_STATE_STRUCTURED_RESET_FAILED"></span><span id="error_state_structured_reset_failed"></span>**ERROR\_STATE\_STRUCTURED\_RESET\_FAILED**
   

15803 (0x3DBB)
 



Resetting the structured state of the application failed.


   

<span id="ERROR_STATE_OPEN_CONTAINER_FAILED"></span><span id="error_state_open_container_failed"></span>**ERROR\_STATE\_OPEN\_CONTAINER\_FAILED**
   

15804 (0x3DBC)
 



State Manager failed to open the container.


   

<span id="ERROR_STATE_CREATE_CONTAINER_FAILED"></span><span id="error_state_create_container_failed"></span>**ERROR\_STATE\_CREATE\_CONTAINER\_FAILED**
   

15805 (0x3DBD)
 



State Manager failed to create the container.


   

<span id="ERROR_STATE_DELETE_CONTAINER_FAILED"></span><span id="error_state_delete_container_failed"></span>**ERROR\_STATE\_DELETE\_CONTAINER\_FAILED**
   

15806 (0x3DBE)
 



State Manager failed to delete the container.


   

<span id="ERROR_STATE_READ_SETTING_FAILED"></span><span id="error_state_read_setting_failed"></span>**ERROR\_STATE\_READ\_SETTING\_FAILED**
   

15807 (0x3DBF)
 



State Manager failed to read the setting.


   

<span id="ERROR_STATE_WRITE_SETTING_FAILED"></span><span id="error_state_write_setting_failed"></span>**ERROR\_STATE\_WRITE\_SETTING\_FAILED**
   

15808 (0x3DC0)
 



State Manager failed to write the setting.


   

<span id="ERROR_STATE_DELETE_SETTING_FAILED"></span><span id="error_state_delete_setting_failed"></span>**ERROR\_STATE\_DELETE\_SETTING\_FAILED**
   

15809 (0x3DC1)
 



State Manager failed to delete the setting.


   

<span id="ERROR_STATE_QUERY_SETTING_FAILED"></span><span id="error_state_query_setting_failed"></span>**ERROR\_STATE\_QUERY\_SETTING\_FAILED**
   

15810 (0x3DC2)
 



State Manager failed to query the setting.


   

<span id="ERROR_STATE_READ_COMPOSITE_SETTING_FAILED"></span><span id="error_state_read_composite_setting_failed"></span>**ERROR\_STATE\_READ\_COMPOSITE\_SETTING\_FAILED**
   

15811 (0x3DC3)
 



State Manager failed to read the composite setting.


   

<span id="ERROR_STATE_WRITE_COMPOSITE_SETTING_FAILED"></span><span id="error_state_write_composite_setting_failed"></span>**ERROR\_STATE\_WRITE\_COMPOSITE\_SETTING\_FAILED**
   

15812 (0x3DC4)
 



State Manager failed to write the composite setting.


   

<span id="ERROR_STATE_ENUMERATE_CONTAINER_FAILED"></span><span id="error_state_enumerate_container_failed"></span>**ERROR\_STATE\_ENUMERATE\_CONTAINER\_FAILED**
   

15813 (0x3DC5)
 



State Manager failed to enumerate the containers.


   

<span id="ERROR_STATE_ENUMERATE_SETTINGS_FAILED"></span><span id="error_state_enumerate_settings_failed"></span>**ERROR\_STATE\_ENUMERATE\_SETTINGS\_FAILED**
   

15814 (0x3DC6)
 



State Manager failed to enumerate the settings.


   

<span id="ERROR_STATE_COMPOSITE_SETTING_VALUE_SIZE_LIMIT_EXCEEDED"></span><span id="error_state_composite_setting_value_size_limit_exceeded"></span>**ERROR\_STATE\_COMPOSITE\_SETTING\_VALUE\_SIZE\_LIMIT\_EXCEEDED**
   

15815 (0x3DC7)
 



The size of the state manager composite setting value has exceeded the limit.


   

<span id="ERROR_STATE_SETTING_VALUE_SIZE_LIMIT_EXCEEDED"></span><span id="error_state_setting_value_size_limit_exceeded"></span>**ERROR\_STATE\_SETTING\_VALUE\_SIZE\_LIMIT\_EXCEEDED**
   

15816 (0x3DC8)
 



The size of the state manager setting value has exceeded the limit.


   

<span id="ERROR_STATE_SETTING_NAME_SIZE_LIMIT_EXCEEDED"></span><span id="error_state_setting_name_size_limit_exceeded"></span>**ERROR\_STATE\_SETTING\_NAME\_SIZE\_LIMIT\_EXCEEDED**
   

15817 (0x3DC9)
 



The length of the state manager setting name has exceeded the limit.


   

<span id="ERROR_STATE_CONTAINER_NAME_SIZE_LIMIT_EXCEEDED"></span><span id="error_state_container_name_size_limit_exceeded"></span>**ERROR\_STATE\_CONTAINER\_NAME\_SIZE\_LIMIT\_EXCEEDED**
   

15818 (0x3DCA)
 



The length of the state manager container name has exceeded the limit.


   

<span id="ERROR_API_UNAVAILABLE"></span><span id="error_api_unavailable"></span>**ERROR\_API\_UNAVAILABLE**
   

15841 (0x3DE1)
 



This API cannot be used in the context of the caller's application type.


   

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   |  WinError.h  |



## See also

 

[System Error Codes](system-error-codes.md)
 

 

 
