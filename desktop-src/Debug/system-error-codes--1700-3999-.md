---
description: Describes error codes 1700-3999 defined in the WinError.h header file and is intended for developers.
ms.assetid: 7e57c087-53e4-443d-9227-21d9eb3cc71f
title: System Error Codes (1700-3999) (WinError.h)
ms.topic: reference
ms.date: 07/18/2019
---

# System Error Codes (1700-3999)

> [!NOTE]
> This information is intended for developers debugging system errors. For other errors, such as issues with Windows Update, there is a list of resources on the [Error codes](system-error-codes.md) page.

The following list describes [system error codes](system-error-codes.md) for errors 1700 to 3999. They are returned by the [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) function when many functions fail. To retrieve the description text for the error in your application, use the [**FormatMessage**](/windows/desktop/api/WinBase/nf-winbase-formatmessage) function with the **FORMAT\_MESSAGE\_FROM\_SYSTEM** flag.

<dl> <dt>

<span id="RPC_S_INVALID_STRING_BINDING"></span><span id="rpc_s_invalid_string_binding"></span>**RPC\_S\_INVALID\_STRING\_BINDING**
</dt> <dd> <dl> <dt>

1700 (0x6A4)
</dt> <dt>



The string binding is invalid.


</dt> </dl> </dd> <dt>

<span id="RPC_S_WRONG_KIND_OF_BINDING"></span><span id="rpc_s_wrong_kind_of_binding"></span>**RPC\_S\_WRONG\_KIND\_OF\_BINDING**
</dt> <dd> <dl> <dt>

1701 (0x6A5)
</dt> <dt>



The binding handle is not the correct type.


</dt> </dl> </dd> <dt>

<span id="RPC_S_INVALID_BINDING"></span><span id="rpc_s_invalid_binding"></span>**RPC\_S\_INVALID\_BINDING**
</dt> <dd> <dl> <dt>

1702 (0x6A6)
</dt> <dt>



The binding handle is invalid.


</dt> </dl> </dd> <dt>

<span id="RPC_S_PROTSEQ_NOT_SUPPORTED"></span><span id="rpc_s_protseq_not_supported"></span>**RPC\_S\_PROTSEQ\_NOT\_SUPPORTED**
</dt> <dd> <dl> <dt>

1703 (0x6A7)
</dt> <dt>



The RPC protocol sequence is not supported.


</dt> </dl> </dd> <dt>

<span id="RPC_S_INVALID_RPC_PROTSEQ"></span><span id="rpc_s_invalid_rpc_protseq"></span>**RPC\_S\_INVALID\_RPC\_PROTSEQ**
</dt> <dd> <dl> <dt>

1704 (0x6A8)
</dt> <dt>



The RPC protocol sequence is invalid.


</dt> </dl> </dd> <dt>

<span id="RPC_S_INVALID_STRING_UUID"></span><span id="rpc_s_invalid_string_uuid"></span>**RPC\_S\_INVALID\_STRING\_UUID**
</dt> <dd> <dl> <dt>

1705 (0x6A9)
</dt> <dt>



The string universal unique identifier (UUID) is invalid.


</dt> </dl> </dd> <dt>

<span id="RPC_S_INVALID_ENDPOINT_FORMAT"></span><span id="rpc_s_invalid_endpoint_format"></span>**RPC\_S\_INVALID\_ENDPOINT\_FORMAT**
</dt> <dd> <dl> <dt>

1706 (0x6AA)
</dt> <dt>



The endpoint format is invalid.


</dt> </dl> </dd> <dt>

<span id="RPC_S_INVALID_NET_ADDR"></span><span id="rpc_s_invalid_net_addr"></span>**RPC\_S\_INVALID\_NET\_ADDR**
</dt> <dd> <dl> <dt>

1707 (0x6AB)
</dt> <dt>



The network address is invalid.


</dt> </dl> </dd> <dt>

<span id="RPC_S_NO_ENDPOINT_FOUND"></span><span id="rpc_s_no_endpoint_found"></span>**RPC\_S\_NO\_ENDPOINT\_FOUND**
</dt> <dd> <dl> <dt>

1708 (0x6AC)
</dt> <dt>



No endpoint was found.


</dt> </dl> </dd> <dt>

<span id="RPC_S_INVALID_TIMEOUT"></span><span id="rpc_s_invalid_timeout"></span>**RPC\_S\_INVALID\_TIMEOUT**
</dt> <dd> <dl> <dt>

1709 (0x6AD)
</dt> <dt>



The timeout value is invalid.


</dt> </dl> </dd> <dt>

<span id="RPC_S_OBJECT_NOT_FOUND"></span><span id="rpc_s_object_not_found"></span>**RPC\_S\_OBJECT\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

1710 (0x6AE)
</dt> <dt>



The object universal unique identifier (UUID) was not found.


</dt> </dl> </dd> <dt>

<span id="RPC_S_ALREADY_REGISTERED"></span><span id="rpc_s_already_registered"></span>**RPC\_S\_ALREADY\_REGISTERED**
</dt> <dd> <dl> <dt>

1711 (0x6AF)
</dt> <dt>



The object universal unique identifier (UUID) has already been registered.


</dt> </dl> </dd> <dt>

<span id="RPC_S_TYPE_ALREADY_REGISTERED"></span><span id="rpc_s_type_already_registered"></span>**RPC\_S\_TYPE\_ALREADY\_REGISTERED**
</dt> <dd> <dl> <dt>

1712 (0x6B0)
</dt> <dt>



The type universal unique identifier (UUID) has already been registered.


</dt> </dl> </dd> <dt>

<span id="RPC_S_ALREADY_LISTENING"></span><span id="rpc_s_already_listening"></span>**RPC\_S\_ALREADY\_LISTENING**
</dt> <dd> <dl> <dt>

1713 (0x6B1)
</dt> <dt>



The RPC server is already listening.


</dt> </dl> </dd> <dt>

<span id="RPC_S_NO_PROTSEQS_REGISTERED"></span><span id="rpc_s_no_protseqs_registered"></span>**RPC\_S\_NO\_PROTSEQS\_REGISTERED**
</dt> <dd> <dl> <dt>

1714 (0x6B2)
</dt> <dt>



No protocol sequences have been registered.


</dt> </dl> </dd> <dt>

<span id="RPC_S_NOT_LISTENING"></span><span id="rpc_s_not_listening"></span>**RPC\_S\_NOT\_LISTENING**
</dt> <dd> <dl> <dt>

1715 (0x6B3)
</dt> <dt>



The RPC server is not listening.


</dt> </dl> </dd> <dt>

<span id="RPC_S_UNKNOWN_MGR_TYPE"></span><span id="rpc_s_unknown_mgr_type"></span>**RPC\_S\_UNKNOWN\_MGR\_TYPE**
</dt> <dd> <dl> <dt>

1716 (0x6B4)
</dt> <dt>



The manager type is unknown.


</dt> </dl> </dd> <dt>

<span id="RPC_S_UNKNOWN_IF"></span><span id="rpc_s_unknown_if"></span>**RPC\_S\_UNKNOWN\_IF**
</dt> <dd> <dl> <dt>

1717 (0x6B5)
</dt> <dt>



The interface is unknown.


</dt> </dl> </dd> <dt>

<span id="RPC_S_NO_BINDINGS"></span><span id="rpc_s_no_bindings"></span>**RPC\_S\_NO\_BINDINGS**
</dt> <dd> <dl> <dt>

1718 (0x6B6)
</dt> <dt>



There are no bindings.


</dt> </dl> </dd> <dt>

<span id="RPC_S_NO_PROTSEQS"></span><span id="rpc_s_no_protseqs"></span>**RPC\_S\_NO\_PROTSEQS**
</dt> <dd> <dl> <dt>

1719 (0x6B7)
</dt> <dt>



There are no protocol sequences.


</dt> </dl> </dd> <dt>

<span id="RPC_S_CANT_CREATE_ENDPOINT"></span><span id="rpc_s_cant_create_endpoint"></span>**RPC\_S\_CANT\_CREATE\_ENDPOINT**
</dt> <dd> <dl> <dt>

1720 (0x6B8)
</dt> <dt>



The endpoint cannot be created.


</dt> </dl> </dd> <dt>

<span id="RPC_S_OUT_OF_RESOURCES"></span><span id="rpc_s_out_of_resources"></span>**RPC\_S\_OUT\_OF\_RESOURCES**
</dt> <dd> <dl> <dt>

1721 (0x6B9)
</dt> <dt>



Not enough resources are available to complete this operation.


</dt> </dl> </dd> <dt>

<span id="RPC_S_SERVER_UNAVAILABLE"></span><span id="rpc_s_server_unavailable"></span>**RPC\_S\_SERVER\_UNAVAILABLE**
</dt> <dd> <dl> <dt>

1722 (0x6BA)
</dt> <dt>



The RPC server is unavailable.


</dt> </dl> </dd> <dt>

<span id="RPC_S_SERVER_TOO_BUSY"></span><span id="rpc_s_server_too_busy"></span>**RPC\_S\_SERVER\_TOO\_BUSY**
</dt> <dd> <dl> <dt>

1723 (0x6BB)
</dt> <dt>



The RPC server is too busy to complete this operation.


</dt> </dl> </dd> <dt>

<span id="RPC_S_INVALID_NETWORK_OPTIONS"></span><span id="rpc_s_invalid_network_options"></span>**RPC\_S\_INVALID\_NETWORK\_OPTIONS**
</dt> <dd> <dl> <dt>

1724 (0x6BC)
</dt> <dt>



The network options are invalid.


</dt> </dl> </dd> <dt>

<span id="RPC_S_NO_CALL_ACTIVE"></span><span id="rpc_s_no_call_active"></span>**RPC\_S\_NO\_CALL\_ACTIVE**
</dt> <dd> <dl> <dt>

1725 (0x6BD)
</dt> <dt>



There are no remote procedure calls active on this thread.


</dt> </dl> </dd> <dt>

<span id="RPC_S_CALL_FAILED"></span><span id="rpc_s_call_failed"></span>**RPC\_S\_CALL\_FAILED**
</dt> <dd> <dl> <dt>

1726 (0x6BE)
</dt> <dt>



The remote procedure call failed.


</dt> </dl> </dd> <dt>

<span id="RPC_S_CALL_FAILED_DNE"></span><span id="rpc_s_call_failed_dne"></span>**RPC\_S\_CALL\_FAILED\_DNE**
</dt> <dd> <dl> <dt>

1727 (0x6BF)
</dt> <dt>



The remote procedure call failed and did not execute.


</dt> </dl> </dd> <dt>

<span id="RPC_S_PROTOCOL_ERROR"></span><span id="rpc_s_protocol_error"></span>**RPC\_S\_PROTOCOL\_ERROR**
</dt> <dd> <dl> <dt>

1728 (0x6C0)
</dt> <dt>



A remote procedure call (RPC) protocol error occurred.


</dt> </dl> </dd> <dt>

<span id="RPC_S_PROXY_ACCESS_DENIED"></span><span id="rpc_s_proxy_access_denied"></span>**RPC\_S\_PROXY\_ACCESS\_DENIED**
</dt> <dd> <dl> <dt>

1729 (0x6C1)
</dt> <dt>



Access to the HTTP proxy is denied.


</dt> </dl> </dd> <dt>

<span id="RPC_S_UNSUPPORTED_TRANS_SYN"></span><span id="rpc_s_unsupported_trans_syn"></span>**RPC\_S\_UNSUPPORTED\_TRANS\_SYN**
</dt> <dd> <dl> <dt>

1730 (0x6C2)
</dt> <dt>



The transfer syntax is not supported by the RPC server.


</dt> </dl> </dd> <dt>

<span id="RPC_S_UNSUPPORTED_TYPE"></span><span id="rpc_s_unsupported_type"></span>**RPC\_S\_UNSUPPORTED\_TYPE**
</dt> <dd> <dl> <dt>

1732 (0x6C4)
</dt> <dt>



The universal unique identifier (UUID) type is not supported.


</dt> </dl> </dd> <dt>

<span id="RPC_S_INVALID_TAG"></span><span id="rpc_s_invalid_tag"></span>**RPC\_S\_INVALID\_TAG**
</dt> <dd> <dl> <dt>

1733 (0x6C5)
</dt> <dt>



The tag is invalid.


</dt> </dl> </dd> <dt>

<span id="RPC_S_INVALID_BOUND"></span><span id="rpc_s_invalid_bound"></span>**RPC\_S\_INVALID\_BOUND**
</dt> <dd> <dl> <dt>

1734 (0x6C6)
</dt> <dt>



The array bounds are invalid.


</dt> </dl> </dd> <dt>

<span id="RPC_S_NO_ENTRY_NAME"></span><span id="rpc_s_no_entry_name"></span>**RPC\_S\_NO\_ENTRY\_NAME**
</dt> <dd> <dl> <dt>

1735 (0x6C7)
</dt> <dt>



The binding does not contain an entry name.


</dt> </dl> </dd> <dt>

<span id="RPC_S_INVALID_NAME_SYNTAX"></span><span id="rpc_s_invalid_name_syntax"></span>**RPC\_S\_INVALID\_NAME\_SYNTAX**
</dt> <dd> <dl> <dt>

1736 (0x6C8)
</dt> <dt>



The name syntax is invalid.


</dt> </dl> </dd> <dt>

<span id="RPC_S_UNSUPPORTED_NAME_SYNTAX"></span><span id="rpc_s_unsupported_name_syntax"></span>**RPC\_S\_UNSUPPORTED\_NAME\_SYNTAX**
</dt> <dd> <dl> <dt>

1737 (0x6C9)
</dt> <dt>



The name syntax is not supported.


</dt> </dl> </dd> <dt>

<span id="RPC_S_UUID_NO_ADDRESS"></span><span id="rpc_s_uuid_no_address"></span>**RPC\_S\_UUID\_NO\_ADDRESS**
</dt> <dd> <dl> <dt>

1739 (0x6CB)
</dt> <dt>



No network address is available to use to construct a universal unique identifier (UUID).


</dt> </dl> </dd> <dt>

<span id="RPC_S_DUPLICATE_ENDPOINT"></span><span id="rpc_s_duplicate_endpoint"></span>**RPC\_S\_DUPLICATE\_ENDPOINT**
</dt> <dd> <dl> <dt>

1740 (0x6CC)
</dt> <dt>



The endpoint is a duplicate.


</dt> </dl> </dd> <dt>

<span id="RPC_S_UNKNOWN_AUTHN_TYPE"></span><span id="rpc_s_unknown_authn_type"></span>**RPC\_S\_UNKNOWN\_AUTHN\_TYPE**
</dt> <dd> <dl> <dt>

1741 (0x6CD)
</dt> <dt>



The authentication type is unknown.


</dt> </dl> </dd> <dt>

<span id="RPC_S_MAX_CALLS_TOO_SMALL"></span><span id="rpc_s_max_calls_too_small"></span>**RPC\_S\_MAX\_CALLS\_TOO\_SMALL**
</dt> <dd> <dl> <dt>

1742 (0x6CE)
</dt> <dt>



The maximum number of calls is too small.


</dt> </dl> </dd> <dt>

<span id="RPC_S_STRING_TOO_LONG"></span><span id="rpc_s_string_too_long"></span>**RPC\_S\_STRING\_TOO\_LONG**
</dt> <dd> <dl> <dt>

1743 (0x6CF)
</dt> <dt>



The string is too long.


</dt> </dl> </dd> <dt>

<span id="RPC_S_PROTSEQ_NOT_FOUND"></span><span id="rpc_s_protseq_not_found"></span>**RPC\_S\_PROTSEQ\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

1744 (0x6D0)
</dt> <dt>



The RPC protocol sequence was not found.


</dt> </dl> </dd> <dt>

<span id="RPC_S_PROCNUM_OUT_OF_RANGE"></span><span id="rpc_s_procnum_out_of_range"></span>**RPC\_S\_PROCNUM\_OUT\_OF\_RANGE**
</dt> <dd> <dl> <dt>

1745 (0x6D1)
</dt> <dt>



The procedure number is out of range.


</dt> </dl> </dd> <dt>

<span id="RPC_S_BINDING_HAS_NO_AUTH"></span><span id="rpc_s_binding_has_no_auth"></span>**RPC\_S\_BINDING\_HAS\_NO\_AUTH**
</dt> <dd> <dl> <dt>

1746 (0x6D2)
</dt> <dt>



The binding does not contain any authentication information.


</dt> </dl> </dd> <dt>

<span id="RPC_S_UNKNOWN_AUTHN_SERVICE"></span><span id="rpc_s_unknown_authn_service"></span>**RPC\_S\_UNKNOWN\_AUTHN\_SERVICE**
</dt> <dd> <dl> <dt>

1747 (0x6D3)
</dt> <dt>



The authentication service is unknown.


</dt> </dl> </dd> <dt>

<span id="RPC_S_UNKNOWN_AUTHN_LEVEL"></span><span id="rpc_s_unknown_authn_level"></span>**RPC\_S\_UNKNOWN\_AUTHN\_LEVEL**
</dt> <dd> <dl> <dt>

1748 (0x6D4)
</dt> <dt>



The authentication level is unknown.


</dt> </dl> </dd> <dt>

<span id="RPC_S_INVALID_AUTH_IDENTITY"></span><span id="rpc_s_invalid_auth_identity"></span>**RPC\_S\_INVALID\_AUTH\_IDENTITY**
</dt> <dd> <dl> <dt>

1749 (0x6D5)
</dt> <dt>



The security context is invalid.


</dt> </dl> </dd> <dt>

<span id="RPC_S_UNKNOWN_AUTHZ_SERVICE"></span><span id="rpc_s_unknown_authz_service"></span>**RPC\_S\_UNKNOWN\_AUTHZ\_SERVICE**
</dt> <dd> <dl> <dt>

1750 (0x6D6)
</dt> <dt>



The authorization service is unknown.


</dt> </dl> </dd> <dt>

<span id="EPT_S_INVALID_ENTRY"></span><span id="ept_s_invalid_entry"></span>**EPT\_S\_INVALID\_ENTRY**
</dt> <dd> <dl> <dt>

1751 (0x6D7)
</dt> <dt>



The entry is invalid.


</dt> </dl> </dd> <dt>

<span id="EPT_S_CANT_PERFORM_OP"></span><span id="ept_s_cant_perform_op"></span>**EPT\_S\_CANT\_PERFORM\_OP**
</dt> <dd> <dl> <dt>

1752 (0x6D8)
</dt> <dt>



The server endpoint cannot perform the operation.


</dt> </dl> </dd> <dt>

<span id="EPT_S_NOT_REGISTERED"></span><span id="ept_s_not_registered"></span>**EPT\_S\_NOT\_REGISTERED**
</dt> <dd> <dl> <dt>

1753 (0x6D9)
</dt> <dt>



There are no more endpoints available from the endpoint mapper.


</dt> </dl> </dd> <dt>

<span id="RPC_S_NOTHING_TO_EXPORT"></span><span id="rpc_s_nothing_to_export"></span>**RPC\_S\_NOTHING\_TO\_EXPORT**
</dt> <dd> <dl> <dt>

1754 (0x6DA)
</dt> <dt>



No interfaces have been exported.


</dt> </dl> </dd> <dt>

<span id="RPC_S_INCOMPLETE_NAME"></span><span id="rpc_s_incomplete_name"></span>**RPC\_S\_INCOMPLETE\_NAME**
</dt> <dd> <dl> <dt>

1755 (0x6DB)
</dt> <dt>



The entry name is incomplete.


</dt> </dl> </dd> <dt>

<span id="RPC_S_INVALID_VERS_OPTION"></span><span id="rpc_s_invalid_vers_option"></span>**RPC\_S\_INVALID\_VERS\_OPTION**
</dt> <dd> <dl> <dt>

1756 (0x6DC)
</dt> <dt>



The version option is invalid.


</dt> </dl> </dd> <dt>

<span id="RPC_S_NO_MORE_MEMBERS"></span><span id="rpc_s_no_more_members"></span>**RPC\_S\_NO\_MORE\_MEMBERS**
</dt> <dd> <dl> <dt>

1757 (0x6DD)
</dt> <dt>



There are no more members.


</dt> </dl> </dd> <dt>

<span id="RPC_S_NOT_ALL_OBJS_UNEXPORTED"></span><span id="rpc_s_not_all_objs_unexported"></span>**RPC\_S\_NOT\_ALL\_OBJS\_UNEXPORTED**
</dt> <dd> <dl> <dt>

1758 (0x6DE)
</dt> <dt>



There is nothing to unexport.


</dt> </dl> </dd> <dt>

<span id="RPC_S_INTERFACE_NOT_FOUND"></span><span id="rpc_s_interface_not_found"></span>**RPC\_S\_INTERFACE\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

1759 (0x6DF)
</dt> <dt>



The interface was not found.


</dt> </dl> </dd> <dt>

<span id="RPC_S_ENTRY_ALREADY_EXISTS"></span><span id="rpc_s_entry_already_exists"></span>**RPC\_S\_ENTRY\_ALREADY\_EXISTS**
</dt> <dd> <dl> <dt>

1760 (0x6E0)
</dt> <dt>



The entry already exists.


</dt> </dl> </dd> <dt>

<span id="RPC_S_ENTRY_NOT_FOUND"></span><span id="rpc_s_entry_not_found"></span>**RPC\_S\_ENTRY\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

1761 (0x6E1)
</dt> <dt>



The entry is not found.


</dt> </dl> </dd> <dt>

<span id="RPC_S_NAME_SERVICE_UNAVAILABLE"></span><span id="rpc_s_name_service_unavailable"></span>**RPC\_S\_NAME\_SERVICE\_UNAVAILABLE**
</dt> <dd> <dl> <dt>

1762 (0x6E2)
</dt> <dt>



The name service is unavailable.


</dt> </dl> </dd> <dt>

<span id="RPC_S_INVALID_NAF_ID"></span><span id="rpc_s_invalid_naf_id"></span>**RPC\_S\_INVALID\_NAF\_ID**
</dt> <dd> <dl> <dt>

1763 (0x6E3)
</dt> <dt>



The network address family is invalid.


</dt> </dl> </dd> <dt>

<span id="RPC_S_CANNOT_SUPPORT"></span><span id="rpc_s_cannot_support"></span>**RPC\_S\_CANNOT\_SUPPORT**
</dt> <dd> <dl> <dt>

1764 (0x6E4)
</dt> <dt>



The requested operation is not supported.


</dt> </dl> </dd> <dt>

<span id="RPC_S_NO_CONTEXT_AVAILABLE"></span><span id="rpc_s_no_context_available"></span>**RPC\_S\_NO\_CONTEXT\_AVAILABLE**
</dt> <dd> <dl> <dt>

1765 (0x6E5)
</dt> <dt>



No security context is available to allow impersonation.


</dt> </dl> </dd> <dt>

<span id="RPC_S_INTERNAL_ERROR"></span><span id="rpc_s_internal_error"></span>**RPC\_S\_INTERNAL\_ERROR**
</dt> <dd> <dl> <dt>

1766 (0x6E6)
</dt> <dt>



An internal error occurred in a remote procedure call (RPC).


</dt> </dl> </dd> <dt>

<span id="RPC_S_ZERO_DIVIDE"></span><span id="rpc_s_zero_divide"></span>**RPC\_S\_ZERO\_DIVIDE**
</dt> <dd> <dl> <dt>

1767 (0x6E7)
</dt> <dt>



The RPC server attempted an integer division by zero.


</dt> </dl> </dd> <dt>

<span id="RPC_S_ADDRESS_ERROR"></span><span id="rpc_s_address_error"></span>**RPC\_S\_ADDRESS\_ERROR**
</dt> <dd> <dl> <dt>

1768 (0x6E8)
</dt> <dt>



An addressing error occurred in the RPC server.


</dt> </dl> </dd> <dt>

<span id="RPC_S_FP_DIV_ZERO"></span><span id="rpc_s_fp_div_zero"></span>**RPC\_S\_FP\_DIV\_ZERO**
</dt> <dd> <dl> <dt>

1769 (0x6E9)
</dt> <dt>



A floating-point operation at the RPC server caused a division by zero.


</dt> </dl> </dd> <dt>

<span id="RPC_S_FP_UNDERFLOW"></span><span id="rpc_s_fp_underflow"></span>**RPC\_S\_FP\_UNDERFLOW**
</dt> <dd> <dl> <dt>

1770 (0x6EA)
</dt> <dt>



A floating-point underflow occurred at the RPC server.


</dt> </dl> </dd> <dt>

<span id="RPC_S_FP_OVERFLOW"></span><span id="rpc_s_fp_overflow"></span>**RPC\_S\_FP\_OVERFLOW**
</dt> <dd> <dl> <dt>

1771 (0x6EB)
</dt> <dt>



A floating-point overflow occurred at the RPC server.


</dt> </dl> </dd> <dt>

<span id="RPC_X_NO_MORE_ENTRIES"></span><span id="rpc_x_no_more_entries"></span>**RPC\_X\_NO\_MORE\_ENTRIES**
</dt> <dd> <dl> <dt>

1772 (0x6EC)
</dt> <dt>



The list of RPC servers available for the binding of auto handles has been exhausted.


</dt> </dl> </dd> <dt>

<span id="RPC_X_SS_CHAR_TRANS_OPEN_FAIL"></span><span id="rpc_x_ss_char_trans_open_fail"></span>**RPC\_X\_SS\_CHAR\_TRANS\_OPEN\_FAIL**
</dt> <dd> <dl> <dt>

1773 (0x6ED)
</dt> <dt>



Unable to open the character translation table file.


</dt> </dl> </dd> <dt>

<span id="RPC_X_SS_CHAR_TRANS_SHORT_FILE"></span><span id="rpc_x_ss_char_trans_short_file"></span>**RPC\_X\_SS\_CHAR\_TRANS\_SHORT\_FILE**
</dt> <dd> <dl> <dt>

1774 (0x6EE)
</dt> <dt>



The file containing the character translation table has fewer than 512 bytes.


</dt> </dl> </dd> <dt>

<span id="RPC_X_SS_IN_NULL_CONTEXT"></span><span id="rpc_x_ss_in_null_context"></span>**RPC\_X\_SS\_IN\_NULL\_CONTEXT**
</dt> <dd> <dl> <dt>

1775 (0x6EF)
</dt> <dt>



A null context handle was passed from the client to the host during a remote procedure call.


</dt> </dl> </dd> <dt>

<span id="RPC_X_SS_CONTEXT_DAMAGED"></span><span id="rpc_x_ss_context_damaged"></span>**RPC\_X\_SS\_CONTEXT\_DAMAGED**
</dt> <dd> <dl> <dt>

1777 (0x6F1)
</dt> <dt>



The context handle changed during a remote procedure call.


</dt> </dl> </dd> <dt>

<span id="RPC_X_SS_HANDLES_MISMATCH"></span><span id="rpc_x_ss_handles_mismatch"></span>**RPC\_X\_SS\_HANDLES\_MISMATCH**
</dt> <dd> <dl> <dt>

1778 (0x6F2)
</dt> <dt>



The binding handles passed to a remote procedure call do not match.


</dt> </dl> </dd> <dt>

<span id="RPC_X_SS_CANNOT_GET_CALL_HANDLE"></span><span id="rpc_x_ss_cannot_get_call_handle"></span>**RPC\_X\_SS\_CANNOT\_GET\_CALL\_HANDLE**
</dt> <dd> <dl> <dt>

1779 (0x6F3)
</dt> <dt>



The stub is unable to get the remote procedure call handle.


</dt> </dl> </dd> <dt>

<span id="RPC_X_NULL_REF_POINTER"></span><span id="rpc_x_null_ref_pointer"></span>**RPC\_X\_NULL\_REF\_POINTER**
</dt> <dd> <dl> <dt>

1780 (0x6F4)
</dt> <dt>



A null reference pointer was passed to the stub.


</dt> </dl> </dd> <dt>

<span id="RPC_X_ENUM_VALUE_OUT_OF_RANGE"></span><span id="rpc_x_enum_value_out_of_range"></span>**RPC\_X\_ENUM\_VALUE\_OUT\_OF\_RANGE**
</dt> <dd> <dl> <dt>

1781 (0x6F5)
</dt> <dt>



The enumeration value is out of range.


</dt> </dl> </dd> <dt>

<span id="RPC_X_BYTE_COUNT_TOO_SMALL"></span><span id="rpc_x_byte_count_too_small"></span>**RPC\_X\_BYTE\_COUNT\_TOO\_SMALL**
</dt> <dd> <dl> <dt>

1782 (0x6F6)
</dt> <dt>



The byte count is too small.


</dt> </dl> </dd> <dt>

<span id="RPC_X_BAD_STUB_DATA"></span><span id="rpc_x_bad_stub_data"></span>**RPC\_X\_BAD\_STUB\_DATA**
</dt> <dd> <dl> <dt>

1783 (0x6F7)
</dt> <dt>



The stub received bad data.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_USER_BUFFER"></span><span id="error_invalid_user_buffer"></span>**ERROR\_INVALID\_USER\_BUFFER**
</dt> <dd> <dl> <dt>

1784 (0x6F8)
</dt> <dt>



The supplied user buffer is not valid for the requested operation.


</dt> </dl> </dd> <dt>

<span id="ERROR_UNRECOGNIZED_MEDIA"></span><span id="error_unrecognized_media"></span>**ERROR\_UNRECOGNIZED\_MEDIA**
</dt> <dd> <dl> <dt>

1785 (0x6F9)
</dt> <dt>



The disk media is not recognized. It may not be formatted.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_TRUST_LSA_SECRET"></span><span id="error_no_trust_lsa_secret"></span>**ERROR\_NO\_TRUST\_LSA\_SECRET**
</dt> <dd> <dl> <dt>

1786 (0x6FA)
</dt> <dt>



The workstation does not have a trust secret.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_TRUST_SAM_ACCOUNT"></span><span id="error_no_trust_sam_account"></span>**ERROR\_NO\_TRUST\_SAM\_ACCOUNT**
</dt> <dd> <dl> <dt>

1787 (0x6FB)
</dt> <dt>



The security database on the server does not have a computer account for this workstation trust relationship.


</dt> </dl> </dd> <dt>

<span id="ERROR_TRUSTED_DOMAIN_FAILURE"></span><span id="error_trusted_domain_failure"></span>**ERROR\_TRUSTED\_DOMAIN\_FAILURE**
</dt> <dd> <dl> <dt>

1788 (0x6FC)
</dt> <dt>



The trust relationship between the primary domain and the trusted domain failed.


</dt> </dl> </dd> <dt>

<span id="ERROR_TRUSTED_RELATIONSHIP_FAILURE"></span><span id="error_trusted_relationship_failure"></span>**ERROR\_TRUSTED\_RELATIONSHIP\_FAILURE**
</dt> <dd> <dl> <dt>

1789 (0x6FD)
</dt> <dt>



The trust relationship between this workstation and the primary domain failed.


</dt> </dl> </dd> <dt>

<span id="ERROR_TRUST_FAILURE"></span><span id="error_trust_failure"></span>**ERROR\_TRUST\_FAILURE**
</dt> <dd> <dl> <dt>

1790 (0x6FE)
</dt> <dt>



The network logon failed.


</dt> </dl> </dd> <dt>

<span id="RPC_S_CALL_IN_PROGRESS"></span><span id="rpc_s_call_in_progress"></span>**RPC\_S\_CALL\_IN\_PROGRESS**
</dt> <dd> <dl> <dt>

1791 (0x6FF)
</dt> <dt>



A remote procedure call is already in progress for this thread.


</dt> </dl> </dd> <dt>

<span id="ERROR_NETLOGON_NOT_STARTED"></span><span id="error_netlogon_not_started"></span>**ERROR\_NETLOGON\_NOT\_STARTED**
</dt> <dd> <dl> <dt>

1792 (0x700)
</dt> <dt>



An attempt was made to logon, but the network logon service was not started.


</dt> </dl> </dd> <dt>

<span id="ERROR_ACCOUNT_EXPIRED"></span><span id="error_account_expired"></span>**ERROR\_ACCOUNT\_EXPIRED**
</dt> <dd> <dl> <dt>

1793 (0x701)
</dt> <dt>



The user's account has expired.


</dt> </dl> </dd> <dt>

<span id="ERROR_REDIRECTOR_HAS_OPEN_HANDLES"></span><span id="error_redirector_has_open_handles"></span>**ERROR\_REDIRECTOR\_HAS\_OPEN\_HANDLES**
</dt> <dd> <dl> <dt>

1794 (0x702)
</dt> <dt>



The redirector is in use and cannot be unloaded.


</dt> </dl> </dd> <dt>

<span id="ERROR_PRINTER_DRIVER_ALREADY_INSTALLED"></span><span id="error_printer_driver_already_installed"></span>**ERROR\_PRINTER\_DRIVER\_ALREADY\_INSTALLED**
</dt> <dd> <dl> <dt>

1795 (0x703)
</dt> <dt>



The specified printer driver is already installed.


</dt> </dl> </dd> <dt>

<span id="ERROR_UNKNOWN_PORT"></span><span id="error_unknown_port"></span>**ERROR\_UNKNOWN\_PORT**
</dt> <dd> <dl> <dt>

1796 (0x704)
</dt> <dt>



The specified port is unknown.


</dt> </dl> </dd> <dt>

<span id="ERROR_UNKNOWN_PRINTER_DRIVER"></span><span id="error_unknown_printer_driver"></span>**ERROR\_UNKNOWN\_PRINTER\_DRIVER**
</dt> <dd> <dl> <dt>

1797 (0x705)
</dt> <dt>



The printer driver is unknown.


</dt> </dl> </dd> <dt>

<span id="ERROR_UNKNOWN_PRINTPROCESSOR"></span><span id="error_unknown_printprocessor"></span>**ERROR\_UNKNOWN\_PRINTPROCESSOR**
</dt> <dd> <dl> <dt>

1798 (0x706)
</dt> <dt>



The print processor is unknown.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_SEPARATOR_FILE"></span><span id="error_invalid_separator_file"></span>**ERROR\_INVALID\_SEPARATOR\_FILE**
</dt> <dd> <dl> <dt>

1799 (0x707)
</dt> <dt>



The specified separator file is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_PRIORITY"></span><span id="error_invalid_priority"></span>**ERROR\_INVALID\_PRIORITY**
</dt> <dd> <dl> <dt>

1800 (0x708)
</dt> <dt>



The specified priority is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_PRINTER_NAME"></span><span id="error_invalid_printer_name"></span>**ERROR\_INVALID\_PRINTER\_NAME**
</dt> <dd> <dl> <dt>

1801 (0x709)
</dt> <dt>



The printer name is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_PRINTER_ALREADY_EXISTS"></span><span id="error_printer_already_exists"></span>**ERROR\_PRINTER\_ALREADY\_EXISTS**
</dt> <dd> <dl> <dt>

1802 (0x70A)
</dt> <dt>



The printer already exists.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_PRINTER_COMMAND"></span><span id="error_invalid_printer_command"></span>**ERROR\_INVALID\_PRINTER\_COMMAND**
</dt> <dd> <dl> <dt>

1803 (0x70B)
</dt> <dt>



The printer command is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_DATATYPE"></span><span id="error_invalid_datatype"></span>**ERROR\_INVALID\_DATATYPE**
</dt> <dd> <dl> <dt>

1804 (0x70C)
</dt> <dt>



The specified datatype is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_ENVIRONMENT"></span><span id="error_invalid_environment"></span>**ERROR\_INVALID\_ENVIRONMENT**
</dt> <dd> <dl> <dt>

1805 (0x70D)
</dt> <dt>



The environment specified is invalid.


</dt> </dl> </dd> <dt>

<span id="RPC_S_NO_MORE_BINDINGS"></span><span id="rpc_s_no_more_bindings"></span>**RPC\_S\_NO\_MORE\_BINDINGS**
</dt> <dd> <dl> <dt>

1806 (0x70E)
</dt> <dt>



There are no more bindings.


</dt> </dl> </dd> <dt>

<span id="ERROR_NOLOGON_INTERDOMAIN_TRUST_ACCOUNT"></span><span id="error_nologon_interdomain_trust_account"></span>**ERROR\_NOLOGON\_INTERDOMAIN\_TRUST\_ACCOUNT**
</dt> <dd> <dl> <dt>

1807 (0x70F)
</dt> <dt>



The account used is an interdomain trust account. Use your global user account or local user account to access this server.


</dt> </dl> </dd> <dt>

<span id="ERROR_NOLOGON_WORKSTATION_TRUST_ACCOUNT"></span><span id="error_nologon_workstation_trust_account"></span>**ERROR\_NOLOGON\_WORKSTATION\_TRUST\_ACCOUNT**
</dt> <dd> <dl> <dt>

1808 (0x710)
</dt> <dt>



The account used is a computer account. Use your global user account or local user account to access this server.


</dt> </dl> </dd> <dt>

<span id="ERROR_NOLOGON_SERVER_TRUST_ACCOUNT"></span><span id="error_nologon_server_trust_account"></span>**ERROR\_NOLOGON\_SERVER\_TRUST\_ACCOUNT**
</dt> <dd> <dl> <dt>

1809 (0x711)
</dt> <dt>



The account used is a server trust account. Use your global user account or local user account to access this server.


</dt> </dl> </dd> <dt>

<span id="ERROR_DOMAIN_TRUST_INCONSISTENT"></span><span id="error_domain_trust_inconsistent"></span>**ERROR\_DOMAIN\_TRUST\_INCONSISTENT**
</dt> <dd> <dl> <dt>

1810 (0x712)
</dt> <dt>



The name or security ID (SID) of the domain specified is inconsistent with the trust information for that domain.


</dt> </dl> </dd> <dt>

<span id="ERROR_SERVER_HAS_OPEN_HANDLES"></span><span id="error_server_has_open_handles"></span>**ERROR\_SERVER\_HAS\_OPEN\_HANDLES**
</dt> <dd> <dl> <dt>

1811 (0x713)
</dt> <dt>



The server is in use and cannot be unloaded.


</dt> </dl> </dd> <dt>

<span id="ERROR_RESOURCE_DATA_NOT_FOUND"></span><span id="error_resource_data_not_found"></span>**ERROR\_RESOURCE\_DATA\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

1812 (0x714)
</dt> <dt>



The specified image file did not contain a resource section.


</dt> </dl> </dd> <dt>

<span id="ERROR_RESOURCE_TYPE_NOT_FOUND"></span><span id="error_resource_type_not_found"></span>**ERROR\_RESOURCE\_TYPE\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

1813 (0x715)
</dt> <dt>



The specified resource type cannot be found in the image file.


</dt> </dl> </dd> <dt>

<span id="ERROR_RESOURCE_NAME_NOT_FOUND"></span><span id="error_resource_name_not_found"></span>**ERROR\_RESOURCE\_NAME\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

1814 (0x716)
</dt> <dt>



The specified resource name cannot be found in the image file.


</dt> </dl> </dd> <dt>

<span id="ERROR_RESOURCE_LANG_NOT_FOUND"></span><span id="error_resource_lang_not_found"></span>**ERROR\_RESOURCE\_LANG\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

1815 (0x717)
</dt> <dt>



The specified resource language ID cannot be found in the image file.


</dt> </dl> </dd> <dt>

<span id="ERROR_NOT_ENOUGH_QUOTA"></span><span id="error_not_enough_quota"></span>**ERROR\_NOT\_ENOUGH\_QUOTA**
</dt> <dd> <dl> <dt>

1816 (0x718)
</dt> <dt>



Not enough quota is available to process this command.


</dt> </dl> </dd> <dt>

<span id="RPC_S_NO_INTERFACES"></span><span id="rpc_s_no_interfaces"></span>**RPC\_S\_NO\_INTERFACES**
</dt> <dd> <dl> <dt>

1817 (0x719)
</dt> <dt>



No interfaces have been registered.


</dt> </dl> </dd> <dt>

<span id="RPC_S_CALL_CANCELLED"></span><span id="rpc_s_call_cancelled"></span>**RPC\_S\_CALL\_CANCELLED**
</dt> <dd> <dl> <dt>

1818 (0x71A)
</dt> <dt>



The remote procedure call was cancelled.


</dt> </dl> </dd> <dt>

<span id="RPC_S_BINDING_INCOMPLETE"></span><span id="rpc_s_binding_incomplete"></span>**RPC\_S\_BINDING\_INCOMPLETE**
</dt> <dd> <dl> <dt>

1819 (0x71B)
</dt> <dt>



The binding handle does not contain all required information.


</dt> </dl> </dd> <dt>

<span id="RPC_S_COMM_FAILURE"></span><span id="rpc_s_comm_failure"></span>**RPC\_S\_COMM\_FAILURE**
</dt> <dd> <dl> <dt>

1820 (0x71C)
</dt> <dt>



A communications failure occurred during a remote procedure call.


</dt> </dl> </dd> <dt>

<span id="RPC_S_UNSUPPORTED_AUTHN_LEVEL"></span><span id="rpc_s_unsupported_authn_level"></span>**RPC\_S\_UNSUPPORTED\_AUTHN\_LEVEL**
</dt> <dd> <dl> <dt>

1821 (0x71D)
</dt> <dt>



The requested authentication level is not supported.


</dt> </dl> </dd> <dt>

<span id="RPC_S_NO_PRINC_NAME"></span><span id="rpc_s_no_princ_name"></span>**RPC\_S\_NO\_PRINC\_NAME**
</dt> <dd> <dl> <dt>

1822 (0x71E)
</dt> <dt>



No principal name registered.


</dt> </dl> </dd> <dt>

<span id="RPC_S_NOT_RPC_ERROR"></span><span id="rpc_s_not_rpc_error"></span>**RPC\_S\_NOT\_RPC\_ERROR**
</dt> <dd> <dl> <dt>

1823 (0x71F)
</dt> <dt>



The error specified is not a valid Windows RPC error code.


</dt> </dl> </dd> <dt>

<span id="RPC_S_UUID_LOCAL_ONLY"></span><span id="rpc_s_uuid_local_only"></span>**RPC\_S\_UUID\_LOCAL\_ONLY**
</dt> <dd> <dl> <dt>

1824 (0x720)
</dt> <dt>



A UUID that is valid only on this computer has been allocated.


</dt> </dl> </dd> <dt>

<span id="RPC_S_SEC_PKG_ERROR"></span><span id="rpc_s_sec_pkg_error"></span>**RPC\_S\_SEC\_PKG\_ERROR**
</dt> <dd> <dl> <dt>

1825 (0x721)
</dt> <dt>



A security package specific error occurred.


</dt> </dl> </dd> <dt>

<span id="RPC_S_NOT_CANCELLED"></span><span id="rpc_s_not_cancelled"></span>**RPC\_S\_NOT\_CANCELLED**
</dt> <dd> <dl> <dt>

1826 (0x722)
</dt> <dt>



Thread is not canceled.


</dt> </dl> </dd> <dt>

<span id="RPC_X_INVALID_ES_ACTION"></span><span id="rpc_x_invalid_es_action"></span>**RPC\_X\_INVALID\_ES\_ACTION**
</dt> <dd> <dl> <dt>

1827 (0x723)
</dt> <dt>



Invalid operation on the encoding/decoding handle.


</dt> </dl> </dd> <dt>

<span id="RPC_X_WRONG_ES_VERSION"></span><span id="rpc_x_wrong_es_version"></span>**RPC\_X\_WRONG\_ES\_VERSION**
</dt> <dd> <dl> <dt>

1828 (0x724)
</dt> <dt>



Incompatible version of the serializing package.


</dt> </dl> </dd> <dt>

<span id="RPC_X_WRONG_STUB_VERSION"></span><span id="rpc_x_wrong_stub_version"></span>**RPC\_X\_WRONG\_STUB\_VERSION**
</dt> <dd> <dl> <dt>

1829 (0x725)
</dt> <dt>



Incompatible version of the RPC stub.


</dt> </dl> </dd> <dt>

<span id="RPC_X_INVALID_PIPE_OBJECT"></span><span id="rpc_x_invalid_pipe_object"></span>**RPC\_X\_INVALID\_PIPE\_OBJECT**
</dt> <dd> <dl> <dt>

1830 (0x726)
</dt> <dt>



The RPC pipe object is invalid or corrupted.


</dt> </dl> </dd> <dt>

<span id="RPC_X_WRONG_PIPE_ORDER"></span><span id="rpc_x_wrong_pipe_order"></span>**RPC\_X\_WRONG\_PIPE\_ORDER**
</dt> <dd> <dl> <dt>

1831 (0x727)
</dt> <dt>



An invalid operation was attempted on an RPC pipe object.


</dt> </dl> </dd> <dt>

<span id="RPC_X_WRONG_PIPE_VERSION"></span><span id="rpc_x_wrong_pipe_version"></span>**RPC\_X\_WRONG\_PIPE\_VERSION**
</dt> <dd> <dl> <dt>

1832 (0x728)
</dt> <dt>



Unsupported RPC pipe version.


</dt> </dl> </dd> <dt>

<span id="RPC_S_COOKIE_AUTH_FAILED"></span><span id="rpc_s_cookie_auth_failed"></span>**RPC\_S\_COOKIE\_AUTH\_FAILED**
</dt> <dd> <dl> <dt>

1833 (0x729)
</dt> <dt>



HTTP proxy server rejected the connection because the cookie authentication failed.


</dt> </dl> </dd> <dt>

<span id="RPC_S_GROUP_MEMBER_NOT_FOUND"></span><span id="rpc_s_group_member_not_found"></span>**RPC\_S\_GROUP\_MEMBER\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

1898 (0x76A)
</dt> <dt>



The group member was not found.


</dt> </dl> </dd> <dt>

<span id="EPT_S_CANT_CREATE"></span><span id="ept_s_cant_create"></span>**EPT\_S\_CANT\_CREATE**
</dt> <dd> <dl> <dt>

1899 (0x76B)
</dt> <dt>



The endpoint mapper database entry could not be created.


</dt> </dl> </dd> <dt>

<span id="RPC_S_INVALID_OBJECT"></span><span id="rpc_s_invalid_object"></span>**RPC\_S\_INVALID\_OBJECT**
</dt> <dd> <dl> <dt>

1900 (0x76C)
</dt> <dt>



The object universal unique identifier (UUID) is the nil UUID.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_TIME"></span><span id="error_invalid_time"></span>**ERROR\_INVALID\_TIME**
</dt> <dd> <dl> <dt>

1901 (0x76D)
</dt> <dt>



The specified time is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_FORM_NAME"></span><span id="error_invalid_form_name"></span>**ERROR\_INVALID\_FORM\_NAME**
</dt> <dd> <dl> <dt>

1902 (0x76E)
</dt> <dt>



The specified form name is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_FORM_SIZE"></span><span id="error_invalid_form_size"></span>**ERROR\_INVALID\_FORM\_SIZE**
</dt> <dd> <dl> <dt>

1903 (0x76F)
</dt> <dt>



The specified form size is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_ALREADY_WAITING"></span><span id="error_already_waiting"></span>**ERROR\_ALREADY\_WAITING**
</dt> <dd> <dl> <dt>

1904 (0x770)
</dt> <dt>



The specified printer handle is already being waited on.


</dt> </dl> </dd> <dt>

<span id="ERROR_PRINTER_DELETED"></span><span id="error_printer_deleted"></span>**ERROR\_PRINTER\_DELETED**
</dt> <dd> <dl> <dt>

1905 (0x771)
</dt> <dt>



The specified printer has been deleted.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_PRINTER_STATE"></span><span id="error_invalid_printer_state"></span>**ERROR\_INVALID\_PRINTER\_STATE**
</dt> <dd> <dl> <dt>

1906 (0x772)
</dt> <dt>



The state of the printer is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_PASSWORD_MUST_CHANGE"></span><span id="error_password_must_change"></span>**ERROR\_PASSWORD\_MUST\_CHANGE**
</dt> <dd> <dl> <dt>

1907 (0x773)
</dt> <dt>



The user's password must be changed before signing in.


</dt> </dl> </dd> <dt>

<span id="ERROR_DOMAIN_CONTROLLER_NOT_FOUND"></span><span id="error_domain_controller_not_found"></span>**ERROR\_DOMAIN\_CONTROLLER\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

1908 (0x774)
</dt> <dt>



Could not find the domain controller for this domain.


</dt> </dl> </dd> <dt>

<span id="ERROR_ACCOUNT_LOCKED_OUT"></span><span id="error_account_locked_out"></span>**ERROR\_ACCOUNT\_LOCKED\_OUT**
</dt> <dd> <dl> <dt>

1909 (0x775)
</dt> <dt>



The referenced account is currently locked out and may not be logged on to.


</dt> </dl> </dd> <dt>

<span id="OR_INVALID_OXID"></span><span id="or_invalid_oxid"></span>**OR\_INVALID\_OXID**
</dt> <dd> <dl> <dt>

1910 (0x776)
</dt> <dt>



The object exporter specified was not found.


</dt> </dl> </dd> <dt>

<span id="OR_INVALID_OID"></span><span id="or_invalid_oid"></span>**OR\_INVALID\_OID**
</dt> <dd> <dl> <dt>

1911 (0x777)
</dt> <dt>



The object specified was not found.


</dt> </dl> </dd> <dt>

<span id="OR_INVALID_SET"></span><span id="or_invalid_set"></span>**OR\_INVALID\_SET**
</dt> <dd> <dl> <dt>

1912 (0x778)
</dt> <dt>



The object resolver set specified was not found.


</dt> </dl> </dd> <dt>

<span id="RPC_S_SEND_INCOMPLETE"></span><span id="rpc_s_send_incomplete"></span>**RPC\_S\_SEND\_INCOMPLETE**
</dt> <dd> <dl> <dt>

1913 (0x779)
</dt> <dt>



Some data remains to be sent in the request buffer.


</dt> </dl> </dd> <dt>

<span id="RPC_S_INVALID_ASYNC_HANDLE"></span><span id="rpc_s_invalid_async_handle"></span>**RPC\_S\_INVALID\_ASYNC\_HANDLE**
</dt> <dd> <dl> <dt>

1914 (0x77A)
</dt> <dt>



Invalid asynchronous remote procedure call handle.


</dt> </dl> </dd> <dt>

<span id="RPC_S_INVALID_ASYNC_CALL"></span><span id="rpc_s_invalid_async_call"></span>**RPC\_S\_INVALID\_ASYNC\_CALL**
</dt> <dd> <dl> <dt>

1915 (0x77B)
</dt> <dt>



Invalid asynchronous RPC call handle for this operation.


</dt> </dl> </dd> <dt>

<span id="RPC_X_PIPE_CLOSED"></span><span id="rpc_x_pipe_closed"></span>**RPC\_X\_PIPE\_CLOSED**
</dt> <dd> <dl> <dt>

1916 (0x77C)
</dt> <dt>



The RPC pipe object has already been closed.


</dt> </dl> </dd> <dt>

<span id="RPC_X_PIPE_DISCIPLINE_ERROR"></span><span id="rpc_x_pipe_discipline_error"></span>**RPC\_X\_PIPE\_DISCIPLINE\_ERROR**
</dt> <dd> <dl> <dt>

1917 (0x77D)
</dt> <dt>



The RPC call completed before all pipes were processed.


</dt> </dl> </dd> <dt>

<span id="RPC_X_PIPE_EMPTY"></span><span id="rpc_x_pipe_empty"></span>**RPC\_X\_PIPE\_EMPTY**
</dt> <dd> <dl> <dt>

1918 (0x77E)
</dt> <dt>



No more data is available from the RPC pipe.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_SITENAME"></span><span id="error_no_sitename"></span>**ERROR\_NO\_SITENAME**
</dt> <dd> <dl> <dt>

1919 (0x77F)
</dt> <dt>



No site name is available for this machine.


</dt> </dl> </dd> <dt>

<span id="ERROR_CANT_ACCESS_FILE"></span><span id="error_cant_access_file"></span>**ERROR\_CANT\_ACCESS\_FILE**
</dt> <dd> <dl> <dt>

1920 (0x780)
</dt> <dt>



The file cannot be accessed by the system.


</dt> </dl> </dd> <dt>

<span id="ERROR_CANT_RESOLVE_FILENAME"></span><span id="error_cant_resolve_filename"></span>**ERROR\_CANT\_RESOLVE\_FILENAME**
</dt> <dd> <dl> <dt>

1921 (0x781)
</dt> <dt>



The name of the file cannot be resolved by the system.


</dt> </dl> </dd> <dt>

<span id="RPC_S_ENTRY_TYPE_MISMATCH"></span><span id="rpc_s_entry_type_mismatch"></span>**RPC\_S\_ENTRY\_TYPE\_MISMATCH**
</dt> <dd> <dl> <dt>

1922 (0x782)
</dt> <dt>



The entry is not of the expected type.


</dt> </dl> </dd> <dt>

<span id="RPC_S_NOT_ALL_OBJS_EXPORTED"></span><span id="rpc_s_not_all_objs_exported"></span>**RPC\_S\_NOT\_ALL\_OBJS\_EXPORTED**
</dt> <dd> <dl> <dt>

1923 (0x783)
</dt> <dt>



Not all object UUIDs could be exported to the specified entry.


</dt> </dl> </dd> <dt>

<span id="RPC_S_INTERFACE_NOT_EXPORTED"></span><span id="rpc_s_interface_not_exported"></span>**RPC\_S\_INTERFACE\_NOT\_EXPORTED**
</dt> <dd> <dl> <dt>

1924 (0x784)
</dt> <dt>



Interface could not be exported to the specified entry.


</dt> </dl> </dd> <dt>

<span id="RPC_S_PROFILE_NOT_ADDED"></span><span id="rpc_s_profile_not_added"></span>**RPC\_S\_PROFILE\_NOT\_ADDED**
</dt> <dd> <dl> <dt>

1925 (0x785)
</dt> <dt>



The specified profile entry could not be added.


</dt> </dl> </dd> <dt>

<span id="RPC_S_PRF_ELT_NOT_ADDED"></span><span id="rpc_s_prf_elt_not_added"></span>**RPC\_S\_PRF\_ELT\_NOT\_ADDED**
</dt> <dd> <dl> <dt>

1926 (0x786)
</dt> <dt>



The specified profile element could not be added.


</dt> </dl> </dd> <dt>

<span id="RPC_S_PRF_ELT_NOT_REMOVED"></span><span id="rpc_s_prf_elt_not_removed"></span>**RPC\_S\_PRF\_ELT\_NOT\_REMOVED**
</dt> <dd> <dl> <dt>

1927 (0x787)
</dt> <dt>



The specified profile element could not be removed.


</dt> </dl> </dd> <dt>

<span id="RPC_S_GRP_ELT_NOT_ADDED"></span><span id="rpc_s_grp_elt_not_added"></span>**RPC\_S\_GRP\_ELT\_NOT\_ADDED**
</dt> <dd> <dl> <dt>

1928 (0x788)
</dt> <dt>



The group element could not be added.


</dt> </dl> </dd> <dt>

<span id="RPC_S_GRP_ELT_NOT_REMOVED"></span><span id="rpc_s_grp_elt_not_removed"></span>**RPC\_S\_GRP\_ELT\_NOT\_REMOVED**
</dt> <dd> <dl> <dt>

1929 (0x789)
</dt> <dt>



The group element could not be removed.


</dt> </dl> </dd> <dt>

<span id="ERROR_KM_DRIVER_BLOCKED"></span><span id="error_km_driver_blocked"></span>**ERROR\_KM\_DRIVER\_BLOCKED**
</dt> <dd> <dl> <dt>

1930 (0x78A)
</dt> <dt>



The printer driver is not compatible with a policy enabled on your computer that blocks NT 4.0 drivers.


</dt> </dl> </dd> <dt>

<span id="ERROR_CONTEXT_EXPIRED"></span><span id="error_context_expired"></span>**ERROR\_CONTEXT\_EXPIRED**
</dt> <dd> <dl> <dt>

1931 (0x78B)
</dt> <dt>



The context has expired and can no longer be used.


</dt> </dl> </dd> <dt>

<span id="ERROR_PER_USER_TRUST_QUOTA_EXCEEDED"></span><span id="error_per_user_trust_quota_exceeded"></span>**ERROR\_PER\_USER\_TRUST\_QUOTA\_EXCEEDED**
</dt> <dd> <dl> <dt>

1932 (0x78C)
</dt> <dt>



The current user's delegated trust creation quota has been exceeded.


</dt> </dl> </dd> <dt>

<span id="ERROR_ALL_USER_TRUST_QUOTA_EXCEEDED"></span><span id="error_all_user_trust_quota_exceeded"></span>**ERROR\_ALL\_USER\_TRUST\_QUOTA\_EXCEEDED**
</dt> <dd> <dl> <dt>

1933 (0x78D)
</dt> <dt>



The total delegated trust creation quota has been exceeded.


</dt> </dl> </dd> <dt>

<span id="ERROR_USER_DELETE_TRUST_QUOTA_EXCEEDED"></span><span id="error_user_delete_trust_quota_exceeded"></span>**ERROR\_USER\_DELETE\_TRUST\_QUOTA\_EXCEEDED**
</dt> <dd> <dl> <dt>

1934 (0x78E)
</dt> <dt>



The current user's delegated trust deletion quota has been exceeded.


</dt> </dl> </dd> <dt>

<span id="ERROR_AUTHENTICATION_FIREWALL_FAILED"></span><span id="error_authentication_firewall_failed"></span>**ERROR\_AUTHENTICATION\_FIREWALL\_FAILED**
</dt> <dd> <dl> <dt>

1935 (0x78F)
</dt> <dt>



The computer you are signing into is protected by an authentication firewall. The specified account is not allowed to authenticate to the computer.


</dt> </dl> </dd> <dt>

<span id="ERROR_REMOTE_PRINT_CONNECTIONS_BLOCKED"></span><span id="error_remote_print_connections_blocked"></span>**ERROR\_REMOTE\_PRINT\_CONNECTIONS\_BLOCKED**
</dt> <dd> <dl> <dt>

1936 (0x790)
</dt> <dt>



Remote connections to the Print Spooler are blocked by a policy set on your machine.


</dt> </dl> </dd> <dt>

<span id="ERROR_NTLM_BLOCKED"></span><span id="error_ntlm_blocked"></span>**ERROR\_NTLM\_BLOCKED**
</dt> <dd> <dl> <dt>

1937 (0x791)
</dt> <dt>



Authentication failed because NTLM authentication has been disabled.


</dt> </dl> </dd> <dt>

<span id="ERROR_PASSWORD_CHANGE_REQUIRED"></span><span id="error_password_change_required"></span>**ERROR\_PASSWORD\_CHANGE\_REQUIRED**
</dt> <dd> <dl> <dt>

1938 (0x792)
</dt> <dt>



Logon Failure: EAS policy requires that the user change their password before this operation can be performed.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_PIXEL_FORMAT"></span><span id="error_invalid_pixel_format"></span>**ERROR\_INVALID\_PIXEL\_FORMAT**
</dt> <dd> <dl> <dt>

2000 (0x7D0)
</dt> <dt>



The pixel format is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_BAD_DRIVER"></span><span id="error_bad_driver"></span>**ERROR\_BAD\_DRIVER**
</dt> <dd> <dl> <dt>

2001 (0x7D1)
</dt> <dt>



The specified driver is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_WINDOW_STYLE"></span><span id="error_invalid_window_style"></span>**ERROR\_INVALID\_WINDOW\_STYLE**
</dt> <dd> <dl> <dt>

2002 (0x7D2)
</dt> <dt>



The window style or class attribute is invalid for this operation.


</dt> </dl> </dd> <dt>

<span id="ERROR_METAFILE_NOT_SUPPORTED"></span><span id="error_metafile_not_supported"></span>**ERROR\_METAFILE\_NOT\_SUPPORTED**
</dt> <dd> <dl> <dt>

2003 (0x7D3)
</dt> <dt>



The requested metafile operation is not supported.


</dt> </dl> </dd> <dt>

<span id="ERROR_TRANSFORM_NOT_SUPPORTED"></span><span id="error_transform_not_supported"></span>**ERROR\_TRANSFORM\_NOT\_SUPPORTED**
</dt> <dd> <dl> <dt>

2004 (0x7D4)
</dt> <dt>



The requested transformation operation is not supported.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLIPPING_NOT_SUPPORTED"></span><span id="error_clipping_not_supported"></span>**ERROR\_CLIPPING\_NOT\_SUPPORTED**
</dt> <dd> <dl> <dt>

2005 (0x7D5)
</dt> <dt>



The requested clipping operation is not supported.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_CMM"></span><span id="error_invalid_cmm"></span>**ERROR\_INVALID\_CMM**
</dt> <dd> <dl> <dt>

2010 (0x7DA)
</dt> <dt>



The specified color management module is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_PROFILE"></span><span id="error_invalid_profile"></span>**ERROR\_INVALID\_PROFILE**
</dt> <dd> <dl> <dt>

2011 (0x7DB)
</dt> <dt>



The specified color profile is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_TAG_NOT_FOUND"></span><span id="error_tag_not_found"></span>**ERROR\_TAG\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

2012 (0x7DC)
</dt> <dt>



The specified tag was not found.


</dt> </dl> </dd> <dt>

<span id="ERROR_TAG_NOT_PRESENT"></span><span id="error_tag_not_present"></span>**ERROR\_TAG\_NOT\_PRESENT**
</dt> <dd> <dl> <dt>

2013 (0x7DD)
</dt> <dt>



A required tag is not present.


</dt> </dl> </dd> <dt>

<span id="ERROR_DUPLICATE_TAG"></span><span id="error_duplicate_tag"></span>**ERROR\_DUPLICATE\_TAG**
</dt> <dd> <dl> <dt>

2014 (0x7DE)
</dt> <dt>



The specified tag is already present.


</dt> </dl> </dd> <dt>

<span id="ERROR_PROFILE_NOT_ASSOCIATED_WITH_DEVICE"></span><span id="error_profile_not_associated_with_device"></span>**ERROR\_PROFILE\_NOT\_ASSOCIATED\_WITH\_DEVICE**
</dt> <dd> <dl> <dt>

2015 (0x7DF)
</dt> <dt>



The specified color profile is not associated with the specified device.


</dt> </dl> </dd> <dt>

<span id="ERROR_PROFILE_NOT_FOUND"></span><span id="error_profile_not_found"></span>**ERROR\_PROFILE\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

2016 (0x7E0)
</dt> <dt>



The specified color profile was not found.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_COLORSPACE"></span><span id="error_invalid_colorspace"></span>**ERROR\_INVALID\_COLORSPACE**
</dt> <dd> <dl> <dt>

2017 (0x7E1)
</dt> <dt>



The specified color space is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_ICM_NOT_ENABLED"></span><span id="error_icm_not_enabled"></span>**ERROR\_ICM\_NOT\_ENABLED**
</dt> <dd> <dl> <dt>

2018 (0x7E2)
</dt> <dt>



Image Color Management is not enabled.


</dt> </dl> </dd> <dt>

<span id="ERROR_DELETING_ICM_XFORM"></span><span id="error_deleting_icm_xform"></span>**ERROR\_DELETING\_ICM\_XFORM**
</dt> <dd> <dl> <dt>

2019 (0x7E3)
</dt> <dt>



There was an error while deleting the color transform.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_TRANSFORM"></span><span id="error_invalid_transform"></span>**ERROR\_INVALID\_TRANSFORM**
</dt> <dd> <dl> <dt>

2020 (0x7E4)
</dt> <dt>



The specified color transform is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_COLORSPACE_MISMATCH"></span><span id="error_colorspace_mismatch"></span>**ERROR\_COLORSPACE\_MISMATCH**
</dt> <dd> <dl> <dt>

2021 (0x7E5)
</dt> <dt>



The specified transform does not match the bitmap's color space.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_COLORINDEX"></span><span id="error_invalid_colorindex"></span>**ERROR\_INVALID\_COLORINDEX**
</dt> <dd> <dl> <dt>

2022 (0x7E6)
</dt> <dt>



The specified named color index is not present in the profile.


</dt> </dl> </dd> <dt>

<span id="ERROR_PROFILE_DOES_NOT_MATCH_DEVICE"></span><span id="error_profile_does_not_match_device"></span>**ERROR\_PROFILE\_DOES\_NOT\_MATCH\_DEVICE**
</dt> <dd> <dl> <dt>

2023 (0x7E7)
</dt> <dt>



The specified profile is intended for a device of a different type than the specified device.


</dt> </dl> </dd> <dt>

<span id="ERROR_CONNECTED_OTHER_PASSWORD"></span><span id="error_connected_other_password"></span>**ERROR\_CONNECTED\_OTHER\_PASSWORD**
</dt> <dd> <dl> <dt>

2108 (0x83C)
</dt> <dt>



The network connection was made successfully, but the user had to be prompted for a password other than the one originally specified.


</dt> </dl> </dd> <dt>

<span id="ERROR_CONNECTED_OTHER_PASSWORD_DEFAULT"></span><span id="error_connected_other_password_default"></span>**ERROR\_CONNECTED\_OTHER\_PASSWORD\_DEFAULT**
</dt> <dd> <dl> <dt>

2109 (0x83D)
</dt> <dt>



The network connection was made successfully using default credentials.


</dt> </dl> </dd> <dt>

<span id="ERROR_BAD_USERNAME"></span><span id="error_bad_username"></span>**ERROR\_BAD\_USERNAME**
</dt> <dd> <dl> <dt>

2202 (0x89A)
</dt> <dt>



The specified username is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_NOT_CONNECTED"></span><span id="error_not_connected"></span>**ERROR\_NOT\_CONNECTED**
</dt> <dd> <dl> <dt>

2250 (0x8CA)
</dt> <dt>



This network connection does not exist.


</dt> </dl> </dd> <dt>

<span id="ERROR_OPEN_FILES"></span><span id="error_open_files"></span>**ERROR\_OPEN\_FILES**
</dt> <dd> <dl> <dt>

2401 (0x961)
</dt> <dt>



This network connection has files open or requests pending.


</dt> </dl> </dd> <dt>

<span id="ERROR_ACTIVE_CONNECTIONS"></span><span id="error_active_connections"></span>**ERROR\_ACTIVE\_CONNECTIONS**
</dt> <dd> <dl> <dt>

2402 (0x962)
</dt> <dt>



Active connections still exist.


</dt> </dl> </dd> <dt>

<span id="ERROR_DEVICE_IN_USE"></span><span id="error_device_in_use"></span>**ERROR\_DEVICE\_IN\_USE**
</dt> <dd> <dl> <dt>

2404 (0x964)
</dt> <dt>



The device is in use by an active process and cannot be disconnected.


</dt> </dl> </dd> <dt>

<span id="ERROR_UNKNOWN_PRINT_MONITOR"></span><span id="error_unknown_print_monitor"></span>**ERROR\_UNKNOWN\_PRINT\_MONITOR**
</dt> <dd> <dl> <dt>

3000 (0xBB8)
</dt> <dt>



The specified print monitor is unknown.


</dt> </dl> </dd> <dt>

<span id="ERROR_PRINTER_DRIVER_IN_USE"></span><span id="error_printer_driver_in_use"></span>**ERROR\_PRINTER\_DRIVER\_IN\_USE**
</dt> <dd> <dl> <dt>

3001 (0xBB9)
</dt> <dt>



The specified printer driver is currently in use.


</dt> </dl> </dd> <dt>

<span id="ERROR_SPOOL_FILE_NOT_FOUND"></span><span id="error_spool_file_not_found"></span>**ERROR\_SPOOL\_FILE\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

3002 (0xBBA)
</dt> <dt>



The spool file was not found.


</dt> </dl> </dd> <dt>

<span id="ERROR_SPL_NO_STARTDOC"></span><span id="error_spl_no_startdoc"></span>**ERROR\_SPL\_NO\_STARTDOC**
</dt> <dd> <dl> <dt>

3003 (0xBBB)
</dt> <dt>



A StartDocPrinter call was not issued.


</dt> </dl> </dd> <dt>

<span id="ERROR_SPL_NO_ADDJOB"></span><span id="error_spl_no_addjob"></span>**ERROR\_SPL\_NO\_ADDJOB**
</dt> <dd> <dl> <dt>

3004 (0xBBC)
</dt> <dt>



An AddJob call was not issued.


</dt> </dl> </dd> <dt>

<span id="ERROR_PRINT_PROCESSOR_ALREADY_INSTALLED"></span><span id="error_print_processor_already_installed"></span>**ERROR\_PRINT\_PROCESSOR\_ALREADY\_INSTALLED**
</dt> <dd> <dl> <dt>

3005 (0xBBD)
</dt> <dt>



The specified print processor has already been installed.


</dt> </dl> </dd> <dt>

<span id="ERROR_PRINT_MONITOR_ALREADY_INSTALLED"></span><span id="error_print_monitor_already_installed"></span>**ERROR\_PRINT\_MONITOR\_ALREADY\_INSTALLED**
</dt> <dd> <dl> <dt>

3006 (0xBBE)
</dt> <dt>



The specified print monitor has already been installed.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_PRINT_MONITOR"></span><span id="error_invalid_print_monitor"></span>**ERROR\_INVALID\_PRINT\_MONITOR**
</dt> <dd> <dl> <dt>

3007 (0xBBF)
</dt> <dt>



The specified print monitor does not have the required functions.


</dt> </dl> </dd> <dt>

<span id="ERROR_PRINT_MONITOR_IN_USE"></span><span id="error_print_monitor_in_use"></span>**ERROR\_PRINT\_MONITOR\_IN\_USE**
</dt> <dd> <dl> <dt>

3008 (0xBC0)
</dt> <dt>



The specified print monitor is currently in use.


</dt> </dl> </dd> <dt>

<span id="ERROR_PRINTER_HAS_JOBS_QUEUED"></span><span id="error_printer_has_jobs_queued"></span>**ERROR\_PRINTER\_HAS\_JOBS\_QUEUED**
</dt> <dd> <dl> <dt>

3009 (0xBC1)
</dt> <dt>



The requested operation is not allowed when there are jobs queued to the printer.


</dt> </dl> </dd> <dt>

<span id="ERROR_SUCCESS_REBOOT_REQUIRED"></span><span id="error_success_reboot_required"></span>**ERROR\_SUCCESS\_REBOOT\_REQUIRED**
</dt> <dd> <dl> <dt>

3010 (0xBC2)
</dt> <dt>



The requested operation is successful. Changes will not be effective until the system is rebooted.


</dt> </dl> </dd> <dt>

<span id="ERROR_SUCCESS_RESTART_REQUIRED"></span><span id="error_success_restart_required"></span>**ERROR\_SUCCESS\_RESTART\_REQUIRED**
</dt> <dd> <dl> <dt>

3011 (0xBC3)
</dt> <dt>



The requested operation is successful. Changes will not be effective until the service is restarted.


</dt> </dl> </dd> <dt>

<span id="ERROR_PRINTER_NOT_FOUND"></span><span id="error_printer_not_found"></span>**ERROR\_PRINTER\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

3012 (0xBC4)
</dt> <dt>



No printers were found.


</dt> </dl> </dd> <dt>

<span id="ERROR_PRINTER_DRIVER_WARNED"></span><span id="error_printer_driver_warned"></span>**ERROR\_PRINTER\_DRIVER\_WARNED**
</dt> <dd> <dl> <dt>

3013 (0xBC5)
</dt> <dt>



The printer driver is known to be unreliable.


</dt> </dl> </dd> <dt>

<span id="ERROR_PRINTER_DRIVER_BLOCKED"></span><span id="error_printer_driver_blocked"></span>**ERROR\_PRINTER\_DRIVER\_BLOCKED**
</dt> <dd> <dl> <dt>

3014 (0xBC6)
</dt> <dt>



The printer driver is known to harm the system.


</dt> </dl> </dd> <dt>

<span id="ERROR_PRINTER_DRIVER_PACKAGE_IN_USE"></span><span id="error_printer_driver_package_in_use"></span>**ERROR\_PRINTER\_DRIVER\_PACKAGE\_IN\_USE**
</dt> <dd> <dl> <dt>

3015 (0xBC7)
</dt> <dt>



The specified printer driver package is currently in use.


</dt> </dl> </dd> <dt>

<span id="ERROR_CORE_DRIVER_PACKAGE_NOT_FOUND"></span><span id="error_core_driver_package_not_found"></span>**ERROR\_CORE\_DRIVER\_PACKAGE\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

3016 (0xBC8)
</dt> <dt>



Unable to find a core driver package that is required by the printer driver package.


</dt> </dl> </dd> <dt>

<span id="ERROR_FAIL_REBOOT_REQUIRED"></span><span id="error_fail_reboot_required"></span>**ERROR\_FAIL\_REBOOT\_REQUIRED**
</dt> <dd> <dl> <dt>

3017 (0xBC9)
</dt> <dt>



The requested operation failed. A system reboot is required to roll back changes made.


</dt> </dl> </dd> <dt>

<span id="ERROR_FAIL_REBOOT_INITIATED"></span><span id="error_fail_reboot_initiated"></span>**ERROR\_FAIL\_REBOOT\_INITIATED**
</dt> <dd> <dl> <dt>

3018 (0xBCA)
</dt> <dt>



The requested operation failed. A system reboot has been initiated to roll back changes made.


</dt> </dl> </dd> <dt>

<span id="ERROR_PRINTER_DRIVER_DOWNLOAD_NEEDED"></span><span id="error_printer_driver_download_needed"></span>**ERROR\_PRINTER\_DRIVER\_DOWNLOAD\_NEEDED**
</dt> <dd> <dl> <dt>

3019 (0xBCB)
</dt> <dt>



The specified printer driver was not found on the system and needs to be downloaded.


</dt> </dl> </dd> <dt>

<span id="ERROR_PRINT_JOB_RESTART_REQUIRED"></span><span id="error_print_job_restart_required"></span>**ERROR\_PRINT\_JOB\_RESTART\_REQUIRED**
</dt> <dd> <dl> <dt>

3020 (0xBCC)
</dt> <dt>



The requested print job has failed to print. A print system update requires the job to be resubmitted.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_PRINTER_DRIVER_MANIFEST"></span><span id="error_invalid_printer_driver_manifest"></span>**ERROR\_INVALID\_PRINTER\_DRIVER\_MANIFEST**
</dt> <dd> <dl> <dt>

3021 (0xBCD)
</dt> <dt>



The printer driver does not contain a valid manifest, or contains too many manifests.


</dt> </dl> </dd> <dt>

<span id="ERROR_PRINTER_NOT_SHAREABLE"></span><span id="error_printer_not_shareable"></span>**ERROR\_PRINTER\_NOT\_SHAREABLE**
</dt> <dd> <dl> <dt>

3022 (0xBCE)
</dt> <dt>



The specified printer cannot be shared.


</dt> </dl> </dd> <dt>

<span id="ERROR_REQUEST_PAUSED"></span><span id="error_request_paused"></span>**ERROR\_REQUEST\_PAUSED**
</dt> <dd> <dl> <dt>

3050 (0xBEA)
</dt> <dt>



The operation was paused.


</dt> </dl> </dd> <dt>

<span id="ERROR_IO_REISSUE_AS_CACHED"></span><span id="error_io_reissue_as_cached"></span>**ERROR\_IO\_REISSUE\_AS\_CACHED**
</dt> <dd> <dl> <dt>

3950 (0xF6E)
</dt> <dt>



Reissue the given operation as a cached IO operation.


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

 

 




