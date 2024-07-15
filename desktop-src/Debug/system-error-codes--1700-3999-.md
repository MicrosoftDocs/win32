---
description: Describes error codes 1700-3999 defined in the WinError.h header file and is intended for developers.
ms.assetid: 7e57c087-53e4-443d-9227-21d9eb3cc71f
title: System Error Codes (1700-3999) (WinError.h)
ms.topic: reference
ms.date: 07/18/2019
---

# System Error Codes (1700-3999)

The following list describes [system error codes](system-error-codes.md) for errors 1700 to 3999. They are returned by the [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) function when many functions fail. To retrieve the description text for the error in your application, use the [**FormatMessage**](/windows/desktop/api/WinBase/nf-winbase-formatmessage) function with the **FORMAT\_MESSAGE\_FROM\_SYSTEM** flag.

> [!NOTE]
> This information is intended for developers debugging system errors. For other errors, such as issues with Windows Update, see the list of resources on the [Error codes](system-error-codes.md) page.

 

<span id="RPC_S_INVALID_STRING_BINDING"></span><span id="rpc_s_invalid_string_binding"></span>**RPC\_S\_INVALID\_STRING\_BINDING**
   

1700 (0x6A4)
 



The string binding is invalid.


   

<span id="RPC_S_WRONG_KIND_OF_BINDING"></span><span id="rpc_s_wrong_kind_of_binding"></span>**RPC\_S\_WRONG\_KIND\_OF\_BINDING**
   

1701 (0x6A5)
 



The binding handle is not the correct type.


   

<span id="RPC_S_INVALID_BINDING"></span><span id="rpc_s_invalid_binding"></span>**RPC\_S\_INVALID\_BINDING**
   

1702 (0x6A6)
 



The binding handle is invalid.


   

<span id="RPC_S_PROTSEQ_NOT_SUPPORTED"></span><span id="rpc_s_protseq_not_supported"></span>**RPC\_S\_PROTSEQ\_NOT\_SUPPORTED**
   

1703 (0x6A7)
 



The RPC protocol sequence is not supported.


   

<span id="RPC_S_INVALID_RPC_PROTSEQ"></span><span id="rpc_s_invalid_rpc_protseq"></span>**RPC\_S\_INVALID\_RPC\_PROTSEQ**
   

1704 (0x6A8)
 



The RPC protocol sequence is invalid.


   

<span id="RPC_S_INVALID_STRING_UUID"></span><span id="rpc_s_invalid_string_uuid"></span>**RPC\_S\_INVALID\_STRING\_UUID**
   

1705 (0x6A9)
 



The string universal unique identifier (UUID) is invalid.


   

<span id="RPC_S_INVALID_ENDPOINT_FORMAT"></span><span id="rpc_s_invalid_endpoint_format"></span>**RPC\_S\_INVALID\_ENDPOINT\_FORMAT**
   

1706 (0x6AA)
 



The endpoint format is invalid.


   

<span id="RPC_S_INVALID_NET_ADDR"></span><span id="rpc_s_invalid_net_addr"></span>**RPC\_S\_INVALID\_NET\_ADDR**
   

1707 (0x6AB)
 



The network address is invalid.


   

<span id="RPC_S_NO_ENDPOINT_FOUND"></span><span id="rpc_s_no_endpoint_found"></span>**RPC\_S\_NO\_ENDPOINT\_FOUND**
   

1708 (0x6AC)
 



No endpoint was found.


   

<span id="RPC_S_INVALID_TIMEOUT"></span><span id="rpc_s_invalid_timeout"></span>**RPC\_S\_INVALID\_TIMEOUT**
   

1709 (0x6AD)
 



The timeout value is invalid.


   

<span id="RPC_S_OBJECT_NOT_FOUND"></span><span id="rpc_s_object_not_found"></span>**RPC\_S\_OBJECT\_NOT\_FOUND**
   

1710 (0x6AE)
 



The object universal unique identifier (UUID) was not found.


   

<span id="RPC_S_ALREADY_REGISTERED"></span><span id="rpc_s_already_registered"></span>**RPC\_S\_ALREADY\_REGISTERED**
   

1711 (0x6AF)
 



The object universal unique identifier (UUID) has already been registered.


   

<span id="RPC_S_TYPE_ALREADY_REGISTERED"></span><span id="rpc_s_type_already_registered"></span>**RPC\_S\_TYPE\_ALREADY\_REGISTERED**
   

1712 (0x6B0)
 



The type universal unique identifier (UUID) has already been registered.


   

<span id="RPC_S_ALREADY_LISTENING"></span><span id="rpc_s_already_listening"></span>**RPC\_S\_ALREADY\_LISTENING**
   

1713 (0x6B1)
 



The RPC server is already listening.


   

<span id="RPC_S_NO_PROTSEQS_REGISTERED"></span><span id="rpc_s_no_protseqs_registered"></span>**RPC\_S\_NO\_PROTSEQS\_REGISTERED**
   

1714 (0x6B2)
 



No protocol sequences have been registered.


   

<span id="RPC_S_NOT_LISTENING"></span><span id="rpc_s_not_listening"></span>**RPC\_S\_NOT\_LISTENING**
   

1715 (0x6B3)
 



The RPC server is not listening.


   

<span id="RPC_S_UNKNOWN_MGR_TYPE"></span><span id="rpc_s_unknown_mgr_type"></span>**RPC\_S\_UNKNOWN\_MGR\_TYPE**
   

1716 (0x6B4)
 



The manager type is unknown.


   

<span id="RPC_S_UNKNOWN_IF"></span><span id="rpc_s_unknown_if"></span>**RPC\_S\_UNKNOWN\_IF**
   

1717 (0x6B5)
 



The interface is unknown.


   

<span id="RPC_S_NO_BINDINGS"></span><span id="rpc_s_no_bindings"></span>**RPC\_S\_NO\_BINDINGS**
   

1718 (0x6B6)
 



There are no bindings.


   

<span id="RPC_S_NO_PROTSEQS"></span><span id="rpc_s_no_protseqs"></span>**RPC\_S\_NO\_PROTSEQS**
   

1719 (0x6B7)
 



There are no protocol sequences.


   

<span id="RPC_S_CANT_CREATE_ENDPOINT"></span><span id="rpc_s_cant_create_endpoint"></span>**RPC\_S\_CANT\_CREATE\_ENDPOINT**
   

1720 (0x6B8)
 



The endpoint cannot be created.


   

<span id="RPC_S_OUT_OF_RESOURCES"></span><span id="rpc_s_out_of_resources"></span>**RPC\_S\_OUT\_OF\_RESOURCES**
   

1721 (0x6B9)
 



Not enough resources are available to complete this operation.


   

<span id="RPC_S_SERVER_UNAVAILABLE"></span><span id="rpc_s_server_unavailable"></span>**RPC\_S\_SERVER\_UNAVAILABLE**
   

1722 (0x6BA)
 



The RPC server is unavailable.


   

<span id="RPC_S_SERVER_TOO_BUSY"></span><span id="rpc_s_server_too_busy"></span>**RPC\_S\_SERVER\_TOO\_BUSY**
   

1723 (0x6BB)
 



The RPC server is too busy to complete this operation.


   

<span id="RPC_S_INVALID_NETWORK_OPTIONS"></span><span id="rpc_s_invalid_network_options"></span>**RPC\_S\_INVALID\_NETWORK\_OPTIONS**
   

1724 (0x6BC)
 



The network options are invalid.


   

<span id="RPC_S_NO_CALL_ACTIVE"></span><span id="rpc_s_no_call_active"></span>**RPC\_S\_NO\_CALL\_ACTIVE**
   

1725 (0x6BD)
 



There are no remote procedure calls active on this thread.


   

<span id="RPC_S_CALL_FAILED"></span><span id="rpc_s_call_failed"></span>**RPC\_S\_CALL\_FAILED**
   

1726 (0x6BE)
 



The remote procedure call failed.


   

<span id="RPC_S_CALL_FAILED_DNE"></span><span id="rpc_s_call_failed_dne"></span>**RPC\_S\_CALL\_FAILED\_DNE**
   

1727 (0x6BF)
 



The remote procedure call failed and did not execute.


   

<span id="RPC_S_PROTOCOL_ERROR"></span><span id="rpc_s_protocol_error"></span>**RPC\_S\_PROTOCOL\_ERROR**
   

1728 (0x6C0)
 



A remote procedure call (RPC) protocol error occurred.


   

<span id="RPC_S_PROXY_ACCESS_DENIED"></span><span id="rpc_s_proxy_access_denied"></span>**RPC\_S\_PROXY\_ACCESS\_DENIED**
   

1729 (0x6C1)
 



Access to the HTTP proxy is denied.


   

<span id="RPC_S_UNSUPPORTED_TRANS_SYN"></span><span id="rpc_s_unsupported_trans_syn"></span>**RPC\_S\_UNSUPPORTED\_TRANS\_SYN**
   

1730 (0x6C2)
 



The transfer syntax is not supported by the RPC server.


   

<span id="RPC_S_UNSUPPORTED_TYPE"></span><span id="rpc_s_unsupported_type"></span>**RPC\_S\_UNSUPPORTED\_TYPE**
   

1732 (0x6C4)
 



The universal unique identifier (UUID) type is not supported.


   

<span id="RPC_S_INVALID_TAG"></span><span id="rpc_s_invalid_tag"></span>**RPC\_S\_INVALID\_TAG**
   

1733 (0x6C5)
 



The tag is invalid.


   

<span id="RPC_S_INVALID_BOUND"></span><span id="rpc_s_invalid_bound"></span>**RPC\_S\_INVALID\_BOUND**
   

1734 (0x6C6)
 



The array bounds are invalid.


   

<span id="RPC_S_NO_ENTRY_NAME"></span><span id="rpc_s_no_entry_name"></span>**RPC\_S\_NO\_ENTRY\_NAME**
   

1735 (0x6C7)
 



The binding does not contain an entry name.


   

<span id="RPC_S_INVALID_NAME_SYNTAX"></span><span id="rpc_s_invalid_name_syntax"></span>**RPC\_S\_INVALID\_NAME\_SYNTAX**
   

1736 (0x6C8)
 



The name syntax is invalid.


   

<span id="RPC_S_UNSUPPORTED_NAME_SYNTAX"></span><span id="rpc_s_unsupported_name_syntax"></span>**RPC\_S\_UNSUPPORTED\_NAME\_SYNTAX**
   

1737 (0x6C9)
 



The name syntax is not supported.


   

<span id="RPC_S_UUID_NO_ADDRESS"></span><span id="rpc_s_uuid_no_address"></span>**RPC\_S\_UUID\_NO\_ADDRESS**
   

1739 (0x6CB)
 



No network address is available to use to construct a universal unique identifier (UUID).


   

<span id="RPC_S_DUPLICATE_ENDPOINT"></span><span id="rpc_s_duplicate_endpoint"></span>**RPC\_S\_DUPLICATE\_ENDPOINT**
   

1740 (0x6CC)
 



The endpoint is a duplicate.


   

<span id="RPC_S_UNKNOWN_AUTHN_TYPE"></span><span id="rpc_s_unknown_authn_type"></span>**RPC\_S\_UNKNOWN\_AUTHN\_TYPE**
   

1741 (0x6CD)
 



The authentication type is unknown.


   

<span id="RPC_S_MAX_CALLS_TOO_SMALL"></span><span id="rpc_s_max_calls_too_small"></span>**RPC\_S\_MAX\_CALLS\_TOO\_SMALL**
   

1742 (0x6CE)
 



The maximum number of calls is too small.


   

<span id="RPC_S_STRING_TOO_LONG"></span><span id="rpc_s_string_too_long"></span>**RPC\_S\_STRING\_TOO\_LONG**
   

1743 (0x6CF)
 



The string is too long.


   

<span id="RPC_S_PROTSEQ_NOT_FOUND"></span><span id="rpc_s_protseq_not_found"></span>**RPC\_S\_PROTSEQ\_NOT\_FOUND**
   

1744 (0x6D0)
 



The RPC protocol sequence was not found.


   

<span id="RPC_S_PROCNUM_OUT_OF_RANGE"></span><span id="rpc_s_procnum_out_of_range"></span>**RPC\_S\_PROCNUM\_OUT\_OF\_RANGE**
   

1745 (0x6D1)
 



The procedure number is out of range.


   

<span id="RPC_S_BINDING_HAS_NO_AUTH"></span><span id="rpc_s_binding_has_no_auth"></span>**RPC\_S\_BINDING\_HAS\_NO\_AUTH**
   

1746 (0x6D2)
 



The binding does not contain any authentication information.


   

<span id="RPC_S_UNKNOWN_AUTHN_SERVICE"></span><span id="rpc_s_unknown_authn_service"></span>**RPC\_S\_UNKNOWN\_AUTHN\_SERVICE**
   

1747 (0x6D3)
 



The authentication service is unknown.


   

<span id="RPC_S_UNKNOWN_AUTHN_LEVEL"></span><span id="rpc_s_unknown_authn_level"></span>**RPC\_S\_UNKNOWN\_AUTHN\_LEVEL**
   

1748 (0x6D4)
 



The authentication level is unknown.


   

<span id="RPC_S_INVALID_AUTH_IDENTITY"></span><span id="rpc_s_invalid_auth_identity"></span>**RPC\_S\_INVALID\_AUTH\_IDENTITY**
   

1749 (0x6D5)
 



The security context is invalid.


   

<span id="RPC_S_UNKNOWN_AUTHZ_SERVICE"></span><span id="rpc_s_unknown_authz_service"></span>**RPC\_S\_UNKNOWN\_AUTHZ\_SERVICE**
   

1750 (0x6D6)
 



The authorization service is unknown.


   

<span id="EPT_S_INVALID_ENTRY"></span><span id="ept_s_invalid_entry"></span>**EPT\_S\_INVALID\_ENTRY**
   

1751 (0x6D7)
 



The entry is invalid.


   

<span id="EPT_S_CANT_PERFORM_OP"></span><span id="ept_s_cant_perform_op"></span>**EPT\_S\_CANT\_PERFORM\_OP**
   

1752 (0x6D8)
 



The server endpoint cannot perform the operation.


   

<span id="EPT_S_NOT_REGISTERED"></span><span id="ept_s_not_registered"></span>**EPT\_S\_NOT\_REGISTERED**
   

1753 (0x6D9)
 



There are no more endpoints available from the endpoint mapper.


   

<span id="RPC_S_NOTHING_TO_EXPORT"></span><span id="rpc_s_nothing_to_export"></span>**RPC\_S\_NOTHING\_TO\_EXPORT**
   

1754 (0x6DA)
 



No interfaces have been exported.


   

<span id="RPC_S_INCOMPLETE_NAME"></span><span id="rpc_s_incomplete_name"></span>**RPC\_S\_INCOMPLETE\_NAME**
   

1755 (0x6DB)
 



The entry name is incomplete.


   

<span id="RPC_S_INVALID_VERS_OPTION"></span><span id="rpc_s_invalid_vers_option"></span>**RPC\_S\_INVALID\_VERS\_OPTION**
   

1756 (0x6DC)
 



The version option is invalid.


   

<span id="RPC_S_NO_MORE_MEMBERS"></span><span id="rpc_s_no_more_members"></span>**RPC\_S\_NO\_MORE\_MEMBERS**
   

1757 (0x6DD)
 



There are no more members.


   

<span id="RPC_S_NOT_ALL_OBJS_UNEXPORTED"></span><span id="rpc_s_not_all_objs_unexported"></span>**RPC\_S\_NOT\_ALL\_OBJS\_UNEXPORTED**
   

1758 (0x6DE)
 



There is nothing to unexport.


   

<span id="RPC_S_INTERFACE_NOT_FOUND"></span><span id="rpc_s_interface_not_found"></span>**RPC\_S\_INTERFACE\_NOT\_FOUND**
   

1759 (0x6DF)
 



The interface was not found.


   

<span id="RPC_S_ENTRY_ALREADY_EXISTS"></span><span id="rpc_s_entry_already_exists"></span>**RPC\_S\_ENTRY\_ALREADY\_EXISTS**
   

1760 (0x6E0)
 



The entry already exists.


   

<span id="RPC_S_ENTRY_NOT_FOUND"></span><span id="rpc_s_entry_not_found"></span>**RPC\_S\_ENTRY\_NOT\_FOUND**
   

1761 (0x6E1)
 



The entry is not found.


   

<span id="RPC_S_NAME_SERVICE_UNAVAILABLE"></span><span id="rpc_s_name_service_unavailable"></span>**RPC\_S\_NAME\_SERVICE\_UNAVAILABLE**
   

1762 (0x6E2)
 



The name service is unavailable.


   

<span id="RPC_S_INVALID_NAF_ID"></span><span id="rpc_s_invalid_naf_id"></span>**RPC\_S\_INVALID\_NAF\_ID**
   

1763 (0x6E3)
 



The network address family is invalid.


   

<span id="RPC_S_CANNOT_SUPPORT"></span><span id="rpc_s_cannot_support"></span>**RPC\_S\_CANNOT\_SUPPORT**
   

1764 (0x6E4)
 



The requested operation is not supported.


   

<span id="RPC_S_NO_CONTEXT_AVAILABLE"></span><span id="rpc_s_no_context_available"></span>**RPC\_S\_NO\_CONTEXT\_AVAILABLE**
   

1765 (0x6E5)
 



No security context is available to allow impersonation.


   

<span id="RPC_S_INTERNAL_ERROR"></span><span id="rpc_s_internal_error"></span>**RPC\_S\_INTERNAL\_ERROR**
   

1766 (0x6E6)
 



An internal error occurred in a remote procedure call (RPC).


   

<span id="RPC_S_ZERO_DIVIDE"></span><span id="rpc_s_zero_divide"></span>**RPC\_S\_ZERO\_DIVIDE**
   

1767 (0x6E7)
 



The RPC server attempted an integer division by zero.


   

<span id="RPC_S_ADDRESS_ERROR"></span><span id="rpc_s_address_error"></span>**RPC\_S\_ADDRESS\_ERROR**
   

1768 (0x6E8)
 



An addressing error occurred in the RPC server.


   

<span id="RPC_S_FP_DIV_ZERO"></span><span id="rpc_s_fp_div_zero"></span>**RPC\_S\_FP\_DIV\_ZERO**
   

1769 (0x6E9)
 



A floating-point operation at the RPC server caused a division by zero.


   

<span id="RPC_S_FP_UNDERFLOW"></span><span id="rpc_s_fp_underflow"></span>**RPC\_S\_FP\_UNDERFLOW**
   

1770 (0x6EA)
 



A floating-point underflow occurred at the RPC server.


   

<span id="RPC_S_FP_OVERFLOW"></span><span id="rpc_s_fp_overflow"></span>**RPC\_S\_FP\_OVERFLOW**
   

1771 (0x6EB)
 



A floating-point overflow occurred at the RPC server.


   

<span id="RPC_X_NO_MORE_ENTRIES"></span><span id="rpc_x_no_more_entries"></span>**RPC\_X\_NO\_MORE\_ENTRIES**
   

1772 (0x6EC)
 



The list of RPC servers available for the binding of auto handles has been exhausted.


   

<span id="RPC_X_SS_CHAR_TRANS_OPEN_FAIL"></span><span id="rpc_x_ss_char_trans_open_fail"></span>**RPC\_X\_SS\_CHAR\_TRANS\_OPEN\_FAIL**
   

1773 (0x6ED)
 



Unable to open the character translation table file.


   

<span id="RPC_X_SS_CHAR_TRANS_SHORT_FILE"></span><span id="rpc_x_ss_char_trans_short_file"></span>**RPC\_X\_SS\_CHAR\_TRANS\_SHORT\_FILE**
   

1774 (0x6EE)
 



The file containing the character translation table has fewer than 512 bytes.


   

<span id="RPC_X_SS_IN_NULL_CONTEXT"></span><span id="rpc_x_ss_in_null_context"></span>**RPC\_X\_SS\_IN\_NULL\_CONTEXT**
   

1775 (0x6EF)
 



A null context handle was passed from the client to the host during a remote procedure call.


   

<span id="RPC_X_SS_CONTEXT_DAMAGED"></span><span id="rpc_x_ss_context_damaged"></span>**RPC\_X\_SS\_CONTEXT\_DAMAGED**
   

1777 (0x6F1)
 



The context handle changed during a remote procedure call.


   

<span id="RPC_X_SS_HANDLES_MISMATCH"></span><span id="rpc_x_ss_handles_mismatch"></span>**RPC\_X\_SS\_HANDLES\_MISMATCH**
   

1778 (0x6F2)
 



The binding handles passed to a remote procedure call do not match.


   

<span id="RPC_X_SS_CANNOT_GET_CALL_HANDLE"></span><span id="rpc_x_ss_cannot_get_call_handle"></span>**RPC\_X\_SS\_CANNOT\_GET\_CALL\_HANDLE**
   

1779 (0x6F3)
 



The stub is unable to get the remote procedure call handle.


   

<span id="RPC_X_NULL_REF_POINTER"></span><span id="rpc_x_null_ref_pointer"></span>**RPC\_X\_NULL\_REF\_POINTER**
   

1780 (0x6F4)
 



A null reference pointer was passed to the stub.


   

<span id="RPC_X_ENUM_VALUE_OUT_OF_RANGE"></span><span id="rpc_x_enum_value_out_of_range"></span>**RPC\_X\_ENUM\_VALUE\_OUT\_OF\_RANGE**
   

1781 (0x6F5)
 



The enumeration value is out of range.


   

<span id="RPC_X_BYTE_COUNT_TOO_SMALL"></span><span id="rpc_x_byte_count_too_small"></span>**RPC\_X\_BYTE\_COUNT\_TOO\_SMALL**
   

1782 (0x6F6)
 



The byte count is too small.


   

<span id="RPC_X_BAD_STUB_DATA"></span><span id="rpc_x_bad_stub_data"></span>**RPC\_X\_BAD\_STUB\_DATA**
   

1783 (0x6F7)
 



The stub received bad data.


   

<span id="ERROR_INVALID_USER_BUFFER"></span><span id="error_invalid_user_buffer"></span>**ERROR\_INVALID\_USER\_BUFFER**
   

1784 (0x6F8)
 



The supplied user buffer is not valid for the requested operation.


   

<span id="ERROR_UNRECOGNIZED_MEDIA"></span><span id="error_unrecognized_media"></span>**ERROR\_UNRECOGNIZED\_MEDIA**
   

1785 (0x6F9)
 



The disk media is not recognized. It may not be formatted.


   

<span id="ERROR_NO_TRUST_LSA_SECRET"></span><span id="error_no_trust_lsa_secret"></span>**ERROR\_NO\_TRUST\_LSA\_SECRET**
   

1786 (0x6FA)
 



The workstation does not have a trust secret.


   

<span id="ERROR_NO_TRUST_SAM_ACCOUNT"></span><span id="error_no_trust_sam_account"></span>**ERROR\_NO\_TRUST\_SAM\_ACCOUNT**
   

1787 (0x6FB)
 



The security database on the server does not have a computer account for this workstation trust relationship.


   

<span id="ERROR_TRUSTED_DOMAIN_FAILURE"></span><span id="error_trusted_domain_failure"></span>**ERROR\_TRUSTED\_DOMAIN\_FAILURE**
   

1788 (0x6FC)
 



The trust relationship between the primary domain and the trusted domain failed.


   

<span id="ERROR_TRUSTED_RELATIONSHIP_FAILURE"></span><span id="error_trusted_relationship_failure"></span>**ERROR\_TRUSTED\_RELATIONSHIP\_FAILURE**
   

1789 (0x6FD)
 



The trust relationship between this workstation and the primary domain failed.


   

<span id="ERROR_TRUST_FAILURE"></span><span id="error_trust_failure"></span>**ERROR\_TRUST\_FAILURE**
   

1790 (0x6FE)
 



The network logon failed.


   

<span id="RPC_S_CALL_IN_PROGRESS"></span><span id="rpc_s_call_in_progress"></span>**RPC\_S\_CALL\_IN\_PROGRESS**
   

1791 (0x6FF)
 



A remote procedure call is already in progress for this thread.


   

<span id="ERROR_NETLOGON_NOT_STARTED"></span><span id="error_netlogon_not_started"></span>**ERROR\_NETLOGON\_NOT\_STARTED**
   

1792 (0x700)
 



An attempt was made to logon, but the network logon service was not started.


   

<span id="ERROR_ACCOUNT_EXPIRED"></span><span id="error_account_expired"></span>**ERROR\_ACCOUNT\_EXPIRED**
   

1793 (0x701)
 



The user's account has expired.


   

<span id="ERROR_REDIRECTOR_HAS_OPEN_HANDLES"></span><span id="error_redirector_has_open_handles"></span>**ERROR\_REDIRECTOR\_HAS\_OPEN\_HANDLES**
   

1794 (0x702)
 



The redirector is in use and cannot be unloaded.


   

<span id="ERROR_PRINTER_DRIVER_ALREADY_INSTALLED"></span><span id="error_printer_driver_already_installed"></span>**ERROR\_PRINTER\_DRIVER\_ALREADY\_INSTALLED**
   

1795 (0x703)
 



The specified printer driver is already installed.


   

<span id="ERROR_UNKNOWN_PORT"></span><span id="error_unknown_port"></span>**ERROR\_UNKNOWN\_PORT**
   

1796 (0x704)
 



The specified port is unknown.


   

<span id="ERROR_UNKNOWN_PRINTER_DRIVER"></span><span id="error_unknown_printer_driver"></span>**ERROR\_UNKNOWN\_PRINTER\_DRIVER**
   

1797 (0x705)
 



The printer driver is unknown.


   

<span id="ERROR_UNKNOWN_PRINTPROCESSOR"></span><span id="error_unknown_printprocessor"></span>**ERROR\_UNKNOWN\_PRINTPROCESSOR**
   

1798 (0x706)
 



The print processor is unknown.


   

<span id="ERROR_INVALID_SEPARATOR_FILE"></span><span id="error_invalid_separator_file"></span>**ERROR\_INVALID\_SEPARATOR\_FILE**
   

1799 (0x707)
 



The specified separator file is invalid.


   

<span id="ERROR_INVALID_PRIORITY"></span><span id="error_invalid_priority"></span>**ERROR\_INVALID\_PRIORITY**
   

1800 (0x708)
 



The specified priority is invalid.


   

<span id="ERROR_INVALID_PRINTER_NAME"></span><span id="error_invalid_printer_name"></span>**ERROR\_INVALID\_PRINTER\_NAME**
   

1801 (0x709)
 



The printer name is invalid.


   

<span id="ERROR_PRINTER_ALREADY_EXISTS"></span><span id="error_printer_already_exists"></span>**ERROR\_PRINTER\_ALREADY\_EXISTS**
   

1802 (0x70A)
 



The printer already exists.


   

<span id="ERROR_INVALID_PRINTER_COMMAND"></span><span id="error_invalid_printer_command"></span>**ERROR\_INVALID\_PRINTER\_COMMAND**
   

1803 (0x70B)
 



The printer command is invalid.


   

<span id="ERROR_INVALID_DATATYPE"></span><span id="error_invalid_datatype"></span>**ERROR\_INVALID\_DATATYPE**
   

1804 (0x70C)
 



The specified datatype is invalid.


   

<span id="ERROR_INVALID_ENVIRONMENT"></span><span id="error_invalid_environment"></span>**ERROR\_INVALID\_ENVIRONMENT**
   

1805 (0x70D)
 



The environment specified is invalid.


   

<span id="RPC_S_NO_MORE_BINDINGS"></span><span id="rpc_s_no_more_bindings"></span>**RPC\_S\_NO\_MORE\_BINDINGS**
   

1806 (0x70E)
 



There are no more bindings.


   

<span id="ERROR_NOLOGON_INTERDOMAIN_TRUST_ACCOUNT"></span><span id="error_nologon_interdomain_trust_account"></span>**ERROR\_NOLOGON\_INTERDOMAIN\_TRUST\_ACCOUNT**
   

1807 (0x70F)
 



The account used is an interdomain trust account. Use your global user account or local user account to access this server.


   

<span id="ERROR_NOLOGON_WORKSTATION_TRUST_ACCOUNT"></span><span id="error_nologon_workstation_trust_account"></span>**ERROR\_NOLOGON\_WORKSTATION\_TRUST\_ACCOUNT**
   

1808 (0x710)
 



The account used is a computer account. Use your global user account or local user account to access this server.


   

<span id="ERROR_NOLOGON_SERVER_TRUST_ACCOUNT"></span><span id="error_nologon_server_trust_account"></span>**ERROR\_NOLOGON\_SERVER\_TRUST\_ACCOUNT**
   

1809 (0x711)
 



The account used is a server trust account. Use your global user account or local user account to access this server.


   

<span id="ERROR_DOMAIN_TRUST_INCONSISTENT"></span><span id="error_domain_trust_inconsistent"></span>**ERROR\_DOMAIN\_TRUST\_INCONSISTENT**
   

1810 (0x712)
 



The name or security ID (SID) of the domain specified is inconsistent with the trust information for that domain.


   

<span id="ERROR_SERVER_HAS_OPEN_HANDLES"></span><span id="error_server_has_open_handles"></span>**ERROR\_SERVER\_HAS\_OPEN\_HANDLES**
   

1811 (0x713)
 



The server is in use and cannot be unloaded.


   

<span id="ERROR_RESOURCE_DATA_NOT_FOUND"></span><span id="error_resource_data_not_found"></span>**ERROR\_RESOURCE\_DATA\_NOT\_FOUND**
   

1812 (0x714)
 



The specified image file did not contain a resource section.


   

<span id="ERROR_RESOURCE_TYPE_NOT_FOUND"></span><span id="error_resource_type_not_found"></span>**ERROR\_RESOURCE\_TYPE\_NOT\_FOUND**
   

1813 (0x715)
 



The specified resource type cannot be found in the image file.


   

<span id="ERROR_RESOURCE_NAME_NOT_FOUND"></span><span id="error_resource_name_not_found"></span>**ERROR\_RESOURCE\_NAME\_NOT\_FOUND**
   

1814 (0x716)
 



The specified resource name cannot be found in the image file.


   

<span id="ERROR_RESOURCE_LANG_NOT_FOUND"></span><span id="error_resource_lang_not_found"></span>**ERROR\_RESOURCE\_LANG\_NOT\_FOUND**
   

1815 (0x717)
 



The specified resource language ID cannot be found in the image file.


   

<span id="ERROR_NOT_ENOUGH_QUOTA"></span><span id="error_not_enough_quota"></span>**ERROR\_NOT\_ENOUGH\_QUOTA**
   

1816 (0x718)
 



Not enough quota is available to process this command.


   

<span id="RPC_S_NO_INTERFACES"></span><span id="rpc_s_no_interfaces"></span>**RPC\_S\_NO\_INTERFACES**
   

1817 (0x719)
 



No interfaces have been registered.


   

<span id="RPC_S_CALL_CANCELLED"></span><span id="rpc_s_call_cancelled"></span>**RPC\_S\_CALL\_CANCELLED**
   

1818 (0x71A)
 



The remote procedure call was cancelled.


   

<span id="RPC_S_BINDING_INCOMPLETE"></span><span id="rpc_s_binding_incomplete"></span>**RPC\_S\_BINDING\_INCOMPLETE**
   

1819 (0x71B)
 



The binding handle does not contain all required information.


   

<span id="RPC_S_COMM_FAILURE"></span><span id="rpc_s_comm_failure"></span>**RPC\_S\_COMM\_FAILURE**
   

1820 (0x71C)
 



A communications failure occurred during a remote procedure call.


   

<span id="RPC_S_UNSUPPORTED_AUTHN_LEVEL"></span><span id="rpc_s_unsupported_authn_level"></span>**RPC\_S\_UNSUPPORTED\_AUTHN\_LEVEL**
   

1821 (0x71D)
 



The requested authentication level is not supported.


   

<span id="RPC_S_NO_PRINC_NAME"></span><span id="rpc_s_no_princ_name"></span>**RPC\_S\_NO\_PRINC\_NAME**
   

1822 (0x71E)
 



No principal name registered.


   

<span id="RPC_S_NOT_RPC_ERROR"></span><span id="rpc_s_not_rpc_error"></span>**RPC\_S\_NOT\_RPC\_ERROR**
   

1823 (0x71F)
 



The error specified is not a valid Windows RPC error code.


   

<span id="RPC_S_UUID_LOCAL_ONLY"></span><span id="rpc_s_uuid_local_only"></span>**RPC\_S\_UUID\_LOCAL\_ONLY**
   

1824 (0x720)
 



A UUID that is valid only on this computer has been allocated.


   

<span id="RPC_S_SEC_PKG_ERROR"></span><span id="rpc_s_sec_pkg_error"></span>**RPC\_S\_SEC\_PKG\_ERROR**
   

1825 (0x721)
 



A security package specific error occurred.


   

<span id="RPC_S_NOT_CANCELLED"></span><span id="rpc_s_not_cancelled"></span>**RPC\_S\_NOT\_CANCELLED**
   

1826 (0x722)
 



Thread is not canceled.


   

<span id="RPC_X_INVALID_ES_ACTION"></span><span id="rpc_x_invalid_es_action"></span>**RPC\_X\_INVALID\_ES\_ACTION**
   

1827 (0x723)
 



Invalid operation on the encoding/decoding handle.


   

<span id="RPC_X_WRONG_ES_VERSION"></span><span id="rpc_x_wrong_es_version"></span>**RPC\_X\_WRONG\_ES\_VERSION**
   

1828 (0x724)
 



Incompatible version of the serializing package.


   

<span id="RPC_X_WRONG_STUB_VERSION"></span><span id="rpc_x_wrong_stub_version"></span>**RPC\_X\_WRONG\_STUB\_VERSION**
   

1829 (0x725)
 



Incompatible version of the RPC stub.


   

<span id="RPC_X_INVALID_PIPE_OBJECT"></span><span id="rpc_x_invalid_pipe_object"></span>**RPC\_X\_INVALID\_PIPE\_OBJECT**
   

1830 (0x726)
 



The RPC pipe object is invalid or corrupted.


   

<span id="RPC_X_WRONG_PIPE_ORDER"></span><span id="rpc_x_wrong_pipe_order"></span>**RPC\_X\_WRONG\_PIPE\_ORDER**
   

1831 (0x727)
 



An invalid operation was attempted on an RPC pipe object.


   

<span id="RPC_X_WRONG_PIPE_VERSION"></span><span id="rpc_x_wrong_pipe_version"></span>**RPC\_X\_WRONG\_PIPE\_VERSION**
   

1832 (0x728)
 



Unsupported RPC pipe version.


   

<span id="RPC_S_COOKIE_AUTH_FAILED"></span><span id="rpc_s_cookie_auth_failed"></span>**RPC\_S\_COOKIE\_AUTH\_FAILED**
   

1833 (0x729)
 



HTTP proxy server rejected the connection because the cookie authentication failed.


   

<span id="RPC_S_GROUP_MEMBER_NOT_FOUND"></span><span id="rpc_s_group_member_not_found"></span>**RPC\_S\_GROUP\_MEMBER\_NOT\_FOUND**
   

1898 (0x76A)
 



The group member was not found.


   

<span id="EPT_S_CANT_CREATE"></span><span id="ept_s_cant_create"></span>**EPT\_S\_CANT\_CREATE**
   

1899 (0x76B)
 



The endpoint mapper database entry could not be created.


   

<span id="RPC_S_INVALID_OBJECT"></span><span id="rpc_s_invalid_object"></span>**RPC\_S\_INVALID\_OBJECT**
   

1900 (0x76C)
 



The object universal unique identifier (UUID) is the nil UUID.


   

<span id="ERROR_INVALID_TIME"></span><span id="error_invalid_time"></span>**ERROR\_INVALID\_TIME**
   

1901 (0x76D)
 



The specified time is invalid.


   

<span id="ERROR_INVALID_FORM_NAME"></span><span id="error_invalid_form_name"></span>**ERROR\_INVALID\_FORM\_NAME**
   

1902 (0x76E)
 



The specified form name is invalid.


   

<span id="ERROR_INVALID_FORM_SIZE"></span><span id="error_invalid_form_size"></span>**ERROR\_INVALID\_FORM\_SIZE**
   

1903 (0x76F)
 



The specified form size is invalid.


   

<span id="ERROR_ALREADY_WAITING"></span><span id="error_already_waiting"></span>**ERROR\_ALREADY\_WAITING**
   

1904 (0x770)
 



The specified printer handle is already being waited on.


   

<span id="ERROR_PRINTER_DELETED"></span><span id="error_printer_deleted"></span>**ERROR\_PRINTER\_DELETED**
   

1905 (0x771)
 



The specified printer has been deleted.


   

<span id="ERROR_INVALID_PRINTER_STATE"></span><span id="error_invalid_printer_state"></span>**ERROR\_INVALID\_PRINTER\_STATE**
   

1906 (0x772)
 



The state of the printer is invalid.


   

<span id="ERROR_PASSWORD_MUST_CHANGE"></span><span id="error_password_must_change"></span>**ERROR\_PASSWORD\_MUST\_CHANGE**
   

1907 (0x773)
 



The user's password must be changed before signing in.


   

<span id="ERROR_DOMAIN_CONTROLLER_NOT_FOUND"></span><span id="error_domain_controller_not_found"></span>**ERROR\_DOMAIN\_CONTROLLER\_NOT\_FOUND**
   

1908 (0x774)
 



Could not find the domain controller for this domain.


   

<span id="ERROR_ACCOUNT_LOCKED_OUT"></span><span id="error_account_locked_out"></span>**ERROR\_ACCOUNT\_LOCKED\_OUT**
   

1909 (0x775)
 



The referenced account is currently locked out and may not be logged on to.


   

<span id="OR_INVALID_OXID"></span><span id="or_invalid_oxid"></span>**OR\_INVALID\_OXID**
   

1910 (0x776)
 



The object exporter specified was not found.


   

<span id="OR_INVALID_OID"></span><span id="or_invalid_oid"></span>**OR\_INVALID\_OID**
   

1911 (0x777)
 



The object specified was not found.


   

<span id="OR_INVALID_SET"></span><span id="or_invalid_set"></span>**OR\_INVALID\_SET**
   

1912 (0x778)
 



The object resolver set specified was not found.


   

<span id="RPC_S_SEND_INCOMPLETE"></span><span id="rpc_s_send_incomplete"></span>**RPC\_S\_SEND\_INCOMPLETE**
   

1913 (0x779)
 



Some data remains to be sent in the request buffer.


   

<span id="RPC_S_INVALID_ASYNC_HANDLE"></span><span id="rpc_s_invalid_async_handle"></span>**RPC\_S\_INVALID\_ASYNC\_HANDLE**
   

1914 (0x77A)
 



Invalid asynchronous remote procedure call handle.


   

<span id="RPC_S_INVALID_ASYNC_CALL"></span><span id="rpc_s_invalid_async_call"></span>**RPC\_S\_INVALID\_ASYNC\_CALL**
   

1915 (0x77B)
 



Invalid asynchronous RPC call handle for this operation.


   

<span id="RPC_X_PIPE_CLOSED"></span><span id="rpc_x_pipe_closed"></span>**RPC\_X\_PIPE\_CLOSED**
   

1916 (0x77C)
 



The RPC pipe object has already been closed.


   

<span id="RPC_X_PIPE_DISCIPLINE_ERROR"></span><span id="rpc_x_pipe_discipline_error"></span>**RPC\_X\_PIPE\_DISCIPLINE\_ERROR**
   

1917 (0x77D)
 



The RPC call completed before all pipes were processed.


   

<span id="RPC_X_PIPE_EMPTY"></span><span id="rpc_x_pipe_empty"></span>**RPC\_X\_PIPE\_EMPTY**
   

1918 (0x77E)
 



No more data is available from the RPC pipe.


   

<span id="ERROR_NO_SITENAME"></span><span id="error_no_sitename"></span>**ERROR\_NO\_SITENAME**
   

1919 (0x77F)
 



No site name is available for this machine.


   

<span id="ERROR_CANT_ACCESS_FILE"></span><span id="error_cant_access_file"></span>**ERROR\_CANT\_ACCESS\_FILE**
   

1920 (0x780)
 



The file cannot be accessed by the system.


   

<span id="ERROR_CANT_RESOLVE_FILENAME"></span><span id="error_cant_resolve_filename"></span>**ERROR\_CANT\_RESOLVE\_FILENAME**
   

1921 (0x781)
 



The name of the file cannot be resolved by the system.


   

<span id="RPC_S_ENTRY_TYPE_MISMATCH"></span><span id="rpc_s_entry_type_mismatch"></span>**RPC\_S\_ENTRY\_TYPE\_MISMATCH**
   

1922 (0x782)
 



The entry is not of the expected type.


   

<span id="RPC_S_NOT_ALL_OBJS_EXPORTED"></span><span id="rpc_s_not_all_objs_exported"></span>**RPC\_S\_NOT\_ALL\_OBJS\_EXPORTED**
   

1923 (0x783)
 



Not all object UUIDs could be exported to the specified entry.


   

<span id="RPC_S_INTERFACE_NOT_EXPORTED"></span><span id="rpc_s_interface_not_exported"></span>**RPC\_S\_INTERFACE\_NOT\_EXPORTED**
   

1924 (0x784)
 



Interface could not be exported to the specified entry.


   

<span id="RPC_S_PROFILE_NOT_ADDED"></span><span id="rpc_s_profile_not_added"></span>**RPC\_S\_PROFILE\_NOT\_ADDED**
   

1925 (0x785)
 



The specified profile entry could not be added.


   

<span id="RPC_S_PRF_ELT_NOT_ADDED"></span><span id="rpc_s_prf_elt_not_added"></span>**RPC\_S\_PRF\_ELT\_NOT\_ADDED**
   

1926 (0x786)
 



The specified profile element could not be added.


   

<span id="RPC_S_PRF_ELT_NOT_REMOVED"></span><span id="rpc_s_prf_elt_not_removed"></span>**RPC\_S\_PRF\_ELT\_NOT\_REMOVED**
   

1927 (0x787)
 



The specified profile element could not be removed.


   

<span id="RPC_S_GRP_ELT_NOT_ADDED"></span><span id="rpc_s_grp_elt_not_added"></span>**RPC\_S\_GRP\_ELT\_NOT\_ADDED**
   

1928 (0x788)
 



The group element could not be added.


   

<span id="RPC_S_GRP_ELT_NOT_REMOVED"></span><span id="rpc_s_grp_elt_not_removed"></span>**RPC\_S\_GRP\_ELT\_NOT\_REMOVED**
   

1929 (0x789)
 



The group element could not be removed.


   

<span id="ERROR_KM_DRIVER_BLOCKED"></span><span id="error_km_driver_blocked"></span>**ERROR\_KM\_DRIVER\_BLOCKED**
   

1930 (0x78A)
 



The printer driver is not compatible with a policy enabled on your computer that blocks NT 4.0 drivers.


   

<span id="ERROR_CONTEXT_EXPIRED"></span><span id="error_context_expired"></span>**ERROR\_CONTEXT\_EXPIRED**
   

1931 (0x78B)
 



The context has expired and can no longer be used.


   

<span id="ERROR_PER_USER_TRUST_QUOTA_EXCEEDED"></span><span id="error_per_user_trust_quota_exceeded"></span>**ERROR\_PER\_USER\_TRUST\_QUOTA\_EXCEEDED**
   

1932 (0x78C)
 



The current user's delegated trust creation quota has been exceeded.


   

<span id="ERROR_ALL_USER_TRUST_QUOTA_EXCEEDED"></span><span id="error_all_user_trust_quota_exceeded"></span>**ERROR\_ALL\_USER\_TRUST\_QUOTA\_EXCEEDED**
   

1933 (0x78D)
 



The total delegated trust creation quota has been exceeded.


   

<span id="ERROR_USER_DELETE_TRUST_QUOTA_EXCEEDED"></span><span id="error_user_delete_trust_quota_exceeded"></span>**ERROR\_USER\_DELETE\_TRUST\_QUOTA\_EXCEEDED**
   

1934 (0x78E)
 



The current user's delegated trust deletion quota has been exceeded.


   

<span id="ERROR_AUTHENTICATION_FIREWALL_FAILED"></span><span id="error_authentication_firewall_failed"></span>**ERROR\_AUTHENTICATION\_FIREWALL\_FAILED**
   

1935 (0x78F)
 



The computer you are signing into is protected by an authentication firewall. The specified account is not allowed to authenticate to the computer.


   

<span id="ERROR_REMOTE_PRINT_CONNECTIONS_BLOCKED"></span><span id="error_remote_print_connections_blocked"></span>**ERROR\_REMOTE\_PRINT\_CONNECTIONS\_BLOCKED**
   

1936 (0x790)
 



Remote connections to the Print Spooler are blocked by a policy set on your machine.


   

<span id="ERROR_NTLM_BLOCKED"></span><span id="error_ntlm_blocked"></span>**ERROR\_NTLM\_BLOCKED**
   

1937 (0x791)
 



Authentication failed because NTLM authentication has been disabled.


   

<span id="ERROR_PASSWORD_CHANGE_REQUIRED"></span><span id="error_password_change_required"></span>**ERROR\_PASSWORD\_CHANGE\_REQUIRED**
   

1938 (0x792)
 



Logon Failure: EAS policy requires that the user change their password before this operation can be performed.


   

<span id="ERROR_INVALID_PIXEL_FORMAT"></span><span id="error_invalid_pixel_format"></span>**ERROR\_INVALID\_PIXEL\_FORMAT**
   

2000 (0x7D0)
 



The pixel format is invalid.


   

<span id="ERROR_BAD_DRIVER"></span><span id="error_bad_driver"></span>**ERROR\_BAD\_DRIVER**
   

2001 (0x7D1)
 



The specified driver is invalid.


   

<span id="ERROR_INVALID_WINDOW_STYLE"></span><span id="error_invalid_window_style"></span>**ERROR\_INVALID\_WINDOW\_STYLE**
   

2002 (0x7D2)
 



The window style or class attribute is invalid for this operation.


   

<span id="ERROR_METAFILE_NOT_SUPPORTED"></span><span id="error_metafile_not_supported"></span>**ERROR\_METAFILE\_NOT\_SUPPORTED**
   

2003 (0x7D3)
 



The requested metafile operation is not supported.


   

<span id="ERROR_TRANSFORM_NOT_SUPPORTED"></span><span id="error_transform_not_supported"></span>**ERROR\_TRANSFORM\_NOT\_SUPPORTED**
   

2004 (0x7D4)
 



The requested transformation operation is not supported.


   

<span id="ERROR_CLIPPING_NOT_SUPPORTED"></span><span id="error_clipping_not_supported"></span>**ERROR\_CLIPPING\_NOT\_SUPPORTED**
   

2005 (0x7D5)
 



The requested clipping operation is not supported.


   

<span id="ERROR_INVALID_CMM"></span><span id="error_invalid_cmm"></span>**ERROR\_INVALID\_CMM**
   

2010 (0x7DA)
 



The specified color management module is invalid.


   

<span id="ERROR_INVALID_PROFILE"></span><span id="error_invalid_profile"></span>**ERROR\_INVALID\_PROFILE**
   

2011 (0x7DB)
 



The specified color profile is invalid.


   

<span id="ERROR_TAG_NOT_FOUND"></span><span id="error_tag_not_found"></span>**ERROR\_TAG\_NOT\_FOUND**
   

2012 (0x7DC)
 



The specified tag was not found.


   

<span id="ERROR_TAG_NOT_PRESENT"></span><span id="error_tag_not_present"></span>**ERROR\_TAG\_NOT\_PRESENT**
   

2013 (0x7DD)
 



A required tag is not present.


   

<span id="ERROR_DUPLICATE_TAG"></span><span id="error_duplicate_tag"></span>**ERROR\_DUPLICATE\_TAG**
   

2014 (0x7DE)
 



The specified tag is already present.


   

<span id="ERROR_PROFILE_NOT_ASSOCIATED_WITH_DEVICE"></span><span id="error_profile_not_associated_with_device"></span>**ERROR\_PROFILE\_NOT\_ASSOCIATED\_WITH\_DEVICE**
   

2015 (0x7DF)
 



The specified color profile is not associated with the specified device.


   

<span id="ERROR_PROFILE_NOT_FOUND"></span><span id="error_profile_not_found"></span>**ERROR\_PROFILE\_NOT\_FOUND**
   

2016 (0x7E0)
 



The specified color profile was not found.


   

<span id="ERROR_INVALID_COLORSPACE"></span><span id="error_invalid_colorspace"></span>**ERROR\_INVALID\_COLORSPACE**
   

2017 (0x7E1)
 



The specified color space is invalid.


   

<span id="ERROR_ICM_NOT_ENABLED"></span><span id="error_icm_not_enabled"></span>**ERROR\_ICM\_NOT\_ENABLED**
   

2018 (0x7E2)
 



Image Color Management is not enabled.


   

<span id="ERROR_DELETING_ICM_XFORM"></span><span id="error_deleting_icm_xform"></span>**ERROR\_DELETING\_ICM\_XFORM**
   

2019 (0x7E3)
 



There was an error while deleting the color transform.


   

<span id="ERROR_INVALID_TRANSFORM"></span><span id="error_invalid_transform"></span>**ERROR\_INVALID\_TRANSFORM**
   

2020 (0x7E4)
 



The specified color transform is invalid.


   

<span id="ERROR_COLORSPACE_MISMATCH"></span><span id="error_colorspace_mismatch"></span>**ERROR\_COLORSPACE\_MISMATCH**
   

2021 (0x7E5)
 



The specified transform does not match the bitmap's color space.


   

<span id="ERROR_INVALID_COLORINDEX"></span><span id="error_invalid_colorindex"></span>**ERROR\_INVALID\_COLORINDEX**
   

2022 (0x7E6)
 



The specified named color index is not present in the profile.


   

<span id="ERROR_PROFILE_DOES_NOT_MATCH_DEVICE"></span><span id="error_profile_does_not_match_device"></span>**ERROR\_PROFILE\_DOES\_NOT\_MATCH\_DEVICE**
   

2023 (0x7E7)
 



The specified profile is intended for a device of a different type than the specified device.


   

<span id="ERROR_CONNECTED_OTHER_PASSWORD"></span><span id="error_connected_other_password"></span>**ERROR\_CONNECTED\_OTHER\_PASSWORD**
   

2108 (0x83C)
 



The network connection was made successfully, but the user had to be prompted for a password other than the one originally specified.


   

<span id="ERROR_CONNECTED_OTHER_PASSWORD_DEFAULT"></span><span id="error_connected_other_password_default"></span>**ERROR\_CONNECTED\_OTHER\_PASSWORD\_DEFAULT**
   

2109 (0x83D)
 



The network connection was made successfully using default credentials.


   

<span id="ERROR_BAD_USERNAME"></span><span id="error_bad_username"></span>**ERROR\_BAD\_USERNAME**
   

2202 (0x89A)
 



The specified username is invalid.


   

<span id="ERROR_NOT_CONNECTED"></span><span id="error_not_connected"></span>**ERROR\_NOT\_CONNECTED**
   

2250 (0x8CA)
 



This network connection does not exist.


   

<span id="ERROR_OPEN_FILES"></span><span id="error_open_files"></span>**ERROR\_OPEN\_FILES**
   

2401 (0x961)
 



This network connection has files open or requests pending.


   

<span id="ERROR_ACTIVE_CONNECTIONS"></span><span id="error_active_connections"></span>**ERROR\_ACTIVE\_CONNECTIONS**
   

2402 (0x962)
 



Active connections still exist.


   

<span id="ERROR_DEVICE_IN_USE"></span><span id="error_device_in_use"></span>**ERROR\_DEVICE\_IN\_USE**
   

2404 (0x964)
 



The device is in use by an active process and cannot be disconnected.


   

<span id="ERROR_UNKNOWN_PRINT_MONITOR"></span><span id="error_unknown_print_monitor"></span>**ERROR\_UNKNOWN\_PRINT\_MONITOR**
   

3000 (0xBB8)
 



The specified print monitor is unknown.


   

<span id="ERROR_PRINTER_DRIVER_IN_USE"></span><span id="error_printer_driver_in_use"></span>**ERROR\_PRINTER\_DRIVER\_IN\_USE**
   

3001 (0xBB9)
 



The specified printer driver is currently in use.


   

<span id="ERROR_SPOOL_FILE_NOT_FOUND"></span><span id="error_spool_file_not_found"></span>**ERROR\_SPOOL\_FILE\_NOT\_FOUND**
   

3002 (0xBBA)
 



The spool file was not found.


   

<span id="ERROR_SPL_NO_STARTDOC"></span><span id="error_spl_no_startdoc"></span>**ERROR\_SPL\_NO\_STARTDOC**
   

3003 (0xBBB)
 



A StartDocPrinter call was not issued.


   

<span id="ERROR_SPL_NO_ADDJOB"></span><span id="error_spl_no_addjob"></span>**ERROR\_SPL\_NO\_ADDJOB**
   

3004 (0xBBC)
 



An AddJob call was not issued.


   

<span id="ERROR_PRINT_PROCESSOR_ALREADY_INSTALLED"></span><span id="error_print_processor_already_installed"></span>**ERROR\_PRINT\_PROCESSOR\_ALREADY\_INSTALLED**
   

3005 (0xBBD)
 



The specified print processor has already been installed.


   

<span id="ERROR_PRINT_MONITOR_ALREADY_INSTALLED"></span><span id="error_print_monitor_already_installed"></span>**ERROR\_PRINT\_MONITOR\_ALREADY\_INSTALLED**
   

3006 (0xBBE)
 



The specified print monitor has already been installed.


   

<span id="ERROR_INVALID_PRINT_MONITOR"></span><span id="error_invalid_print_monitor"></span>**ERROR\_INVALID\_PRINT\_MONITOR**
   

3007 (0xBBF)
 



The specified print monitor does not have the required functions.


   

<span id="ERROR_PRINT_MONITOR_IN_USE"></span><span id="error_print_monitor_in_use"></span>**ERROR\_PRINT\_MONITOR\_IN\_USE**
   

3008 (0xBC0)
 



The specified print monitor is currently in use.


   

<span id="ERROR_PRINTER_HAS_JOBS_QUEUED"></span><span id="error_printer_has_jobs_queued"></span>**ERROR\_PRINTER\_HAS\_JOBS\_QUEUED**
   

3009 (0xBC1)
 



The requested operation is not allowed when there are jobs queued to the printer.


   

<span id="ERROR_SUCCESS_REBOOT_REQUIRED"></span><span id="error_success_reboot_required"></span>**ERROR\_SUCCESS\_REBOOT\_REQUIRED**
   

3010 (0xBC2)
 



The requested operation is successful. Changes will not be effective until the system is rebooted.


   

<span id="ERROR_SUCCESS_RESTART_REQUIRED"></span><span id="error_success_restart_required"></span>**ERROR\_SUCCESS\_RESTART\_REQUIRED**
   

3011 (0xBC3)
 



The requested operation is successful. Changes will not be effective until the service is restarted.


   

<span id="ERROR_PRINTER_NOT_FOUND"></span><span id="error_printer_not_found"></span>**ERROR\_PRINTER\_NOT\_FOUND**
   

3012 (0xBC4)
 



No printers were found.


   

<span id="ERROR_PRINTER_DRIVER_WARNED"></span><span id="error_printer_driver_warned"></span>**ERROR\_PRINTER\_DRIVER\_WARNED**
   

3013 (0xBC5)
 



The printer driver is known to be unreliable.


   

<span id="ERROR_PRINTER_DRIVER_BLOCKED"></span><span id="error_printer_driver_blocked"></span>**ERROR\_PRINTER\_DRIVER\_BLOCKED**
   

3014 (0xBC6)
 



The printer driver is known to harm the system.


   

<span id="ERROR_PRINTER_DRIVER_PACKAGE_IN_USE"></span><span id="error_printer_driver_package_in_use"></span>**ERROR\_PRINTER\_DRIVER\_PACKAGE\_IN\_USE**
   

3015 (0xBC7)
 



The specified printer driver package is currently in use.


   

<span id="ERROR_CORE_DRIVER_PACKAGE_NOT_FOUND"></span><span id="error_core_driver_package_not_found"></span>**ERROR\_CORE\_DRIVER\_PACKAGE\_NOT\_FOUND**
   

3016 (0xBC8)
 



Unable to find a core driver package that is required by the printer driver package.


   

<span id="ERROR_FAIL_REBOOT_REQUIRED"></span><span id="error_fail_reboot_required"></span>**ERROR\_FAIL\_REBOOT\_REQUIRED**
   

3017 (0xBC9)
 



The requested operation failed. A system reboot is required to roll back changes made.


   

<span id="ERROR_FAIL_REBOOT_INITIATED"></span><span id="error_fail_reboot_initiated"></span>**ERROR\_FAIL\_REBOOT\_INITIATED**
   

3018 (0xBCA)
 



The requested operation failed. A system reboot has been initiated to roll back changes made.


   

<span id="ERROR_PRINTER_DRIVER_DOWNLOAD_NEEDED"></span><span id="error_printer_driver_download_needed"></span>**ERROR\_PRINTER\_DRIVER\_DOWNLOAD\_NEEDED**
   

3019 (0xBCB)
 



The specified printer driver was not found on the system and needs to be downloaded.


   

<span id="ERROR_PRINT_JOB_RESTART_REQUIRED"></span><span id="error_print_job_restart_required"></span>**ERROR\_PRINT\_JOB\_RESTART\_REQUIRED**
   

3020 (0xBCC)
 



The requested print job has failed to print. A print system update requires the job to be resubmitted.


   

<span id="ERROR_INVALID_PRINTER_DRIVER_MANIFEST"></span><span id="error_invalid_printer_driver_manifest"></span>**ERROR\_INVALID\_PRINTER\_DRIVER\_MANIFEST**
   

3021 (0xBCD)
 



The printer driver does not contain a valid manifest, or contains too many manifests.


   

<span id="ERROR_PRINTER_NOT_SHAREABLE"></span><span id="error_printer_not_shareable"></span>**ERROR\_PRINTER\_NOT\_SHAREABLE**
   

3022 (0xBCE)
 



The specified printer cannot be shared.


   

<span id="ERROR_REQUEST_PAUSED"></span><span id="error_request_paused"></span>**ERROR\_REQUEST\_PAUSED**
   

3050 (0xBEA)
 



The operation was paused.


   

<span id="ERROR_IO_REISSUE_AS_CACHED"></span><span id="error_io_reissue_as_cached"></span>**ERROR\_IO\_REISSUE\_AS\_CACHED**
   

3950 (0xF6E)
 



Reissue the given operation as a cached IO operation.


   


## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   |  WinError.h  |



## See also

 

[System Error Codes](system-error-codes.md)
 

 

 




