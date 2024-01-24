---
title: WFP Error Codes (Winerror.h)
description: (WFP) specific error codes.
ms.assetid: 11f3085a-f044-4a78-b47a-59b9086562bf
topic_type:
- apiref
api_name:
- FWP_E_CALLOUT_NOT_FOUND
- FWP_E_CONDITION_NOT_FOUND
- FWP_E_FILTER_NOT_FOUND
- FWP_E_LAYER_NOT_FOUND
- FWP_E_PROVIDER_NOT_FOUND
- FWP_E_PROVIDER_CONTEXT_NOT_FOUND
- FWP_E_SUBLAYER_NOT_FOUND
- FWP_E_NOT_FOUND
- FWP_E_ALREADY_EXISTS
- FWP_E_IN_USE
- FWP_E_DYNAMIC_SESSION_IN_PROGRESS
- FWP_E_WRONG_SESSION
- FWP_E_NO_TXN_IN_PROGRESS
- FWP_E_TXN_IN_PROGRESS
- FWP_E_TXN_ABORTED
- FWP_E_SESSION_ABORTED
- FWP_E_INCOMPATIBLE_TXN
- FWP_E_TIMEOUT
- FWP_E_NET_EVENTS_DISABLED
- FWP_E_INCOMPATIBLE_LAYER
- FWP_E_KM_CLIENTS_ONLY
- FWP_E_LIFETIME_MISMATCH
- FWP_E_BUILTIN_OBJECT
- FWP_E_TOO_MANY_CALLOUTS
- FWP_E_NOTIFICATION_DROPPED
- FWP_E_TRAFFIC_MISMATCH
- FWP_E_INCOMPATIBLE_SA_STATE
- FWP_E_NULL_POINTER
- FWP_E_INVALID_ENUMERATOR
- FWP_E_INVALID_FLAGS
- FWP_E_INVALID_NET_MASK
- FWP_E_INVALID_RANGE
- FWP_E_INVALID_INTERVAL
- FWP_E_ZERO_LENGTH_ARRAY
- FWP_E_NULL_DISPLAY_NAME
- FWP_E_INVALID_ACTION_TYPE
- FWP_E_INVALID_WEIGHT
- FWP_E_MATCH_TYPE_MISMATCH
- FWP_E_TYPE_MISMATCH
- FWP_E_OUT_OF_BOUNDS
- FWP_E_RESERVED
- FWP_E_DUPLICATE_CONDITION
- FWP_E_DUPLICATE_KEYMOD
- FWP_E_ACTION_INCOMPATIBLE_WITH_LAYER
- FWP_E_ACTION_INCOMPATIBLE_WITH_SUBLAYER
- FWP_E_CONTEXT_INCOMPATIBLE_WITH_LAYER
- FWP_E_CONTEXT_INCOMPATIBLE_WITH_CALLOUT
- FWP_E_INCOMPATIBLE_AUTH_METHOD
- FWP_E_INCOMPATIBLE_DH_GROUP
- FWP_E_EM_NOT_SUPPORTED
- FWP_E_NEVER_MATCH
- FWP_E_PROVIDER_CONTEXT_MISMATCH
- FWP_E_INVALID_PARAMETER
- FWP_E_TOO_MANY_SUBLAYERS
- FWP_E_CALLOUT_NOTIFICATION_FAILED
- FWP_E_INVALID_AUTH_TRANSFORM
- FWP_E_INVALID_CIPHER_TRANSFORM
api_location:
- winerror.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WFP Error Codes

Windows Filtering Platform (WFP) specific error codes are as follows.

<dl> <dt>

<span id="FWP_E_CALLOUT_NOT_FOUND"></span><span id="fwp_e_callout_not_found"></span>**FWP\_E\_CALLOUT\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

0x80320001
</dt> <dt>



The callout does not exist.


</dt> </dl> </dd> <dt>

<span id="FWP_E_CONDITION_NOT_FOUND"></span><span id="fwp_e_condition_not_found"></span>**FWP\_E\_CONDITION\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

0x80320002
</dt> <dt>



The filter condition does not exist.


</dt> </dl> </dd> <dt>

<span id="FWP_E_FILTER_NOT_FOUND"></span><span id="fwp_e_filter_not_found"></span>**FWP\_E\_FILTER\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

0x80320003
</dt> <dt>



The filter does not exist.


</dt> </dl> </dd> <dt>

<span id="FWP_E_LAYER_NOT_FOUND"></span><span id="fwp_e_layer_not_found"></span>**FWP\_E\_LAYER\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

0x80320004
</dt> <dt>



The layer does not exist.


</dt> </dl> </dd> <dt>

<span id="FWP_E_PROVIDER_NOT_FOUND"></span><span id="fwp_e_provider_not_found"></span>**FWP\_E\_PROVIDER\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

0x80320005
</dt> <dt>



The provider does not exist.


</dt> </dl> </dd> <dt>

<span id="FWP_E_PROVIDER_CONTEXT_NOT_FOUND"></span><span id="fwp_e_provider_context_not_found"></span>**FWP\_E\_PROVIDER\_CONTEXT\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

0x80320006
</dt> <dt>



The provider context does not exist.


</dt> </dl> </dd> <dt>

<span id="FWP_E_SUBLAYER_NOT_FOUND"></span><span id="fwp_e_sublayer_not_found"></span>**FWP\_E\_SUBLAYER\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

0x80320007
</dt> <dt>



The sub-layer does not exist.


</dt> </dl> </dd> <dt>

<span id="FWP_E_NOT_FOUND"></span><span id="fwp_e_not_found"></span>**FWP\_E\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

0x80320008
</dt> <dt>



The object does not exist.

The [IPsecSaContext\*](fwp-ipsec-functions.md) functions return this error if the SA context ID is not found.


</dt> </dl> </dd> <dt>

<span id="FWP_E_ALREADY_EXISTS"></span><span id="fwp_e_already_exists"></span>**FWP\_E\_ALREADY\_EXISTS**
</dt> <dd> <dl> <dt>

0x80320009
</dt> <dt>



An object with that GUID or LUID already exists.


</dt> </dl> </dd> <dt>

<span id="FWP_E_IN_USE"></span><span id="fwp_e_in_use"></span>**FWP\_E\_IN\_USE**
</dt> <dd> <dl> <dt>

0x8032000A
</dt> <dt>



The object is referenced by other objects, so it cannot be deleted.


</dt> </dl> </dd> <dt>

<span id="FWP_E_DYNAMIC_SESSION_IN_PROGRESS"></span><span id="fwp_e_dynamic_session_in_progress"></span>**FWP\_E\_DYNAMIC\_SESSION\_IN\_PROGRESS**
</dt> <dd> <dl> <dt>

0x8032000B
</dt> <dt>



The call is not allowed from within a dynamic session.


</dt> </dl> </dd> <dt>

<span id="FWP_E_WRONG_SESSION"></span><span id="fwp_e_wrong_session"></span>**FWP\_E\_WRONG\_SESSION**
</dt> <dd> <dl> <dt>

0x8032000C
</dt> <dt>



The call was made from the wrong session, so it cannot be completed.


</dt> </dl> </dd> <dt>

<span id="FWP_E_NO_TXN_IN_PROGRESS"></span><span id="fwp_e_no_txn_in_progress"></span>**FWP\_E\_NO\_TXN\_IN\_PROGRESS**
</dt> <dd> <dl> <dt>

0x8032000D
</dt> <dt>



The call must be made from within an explicit transaction.


</dt> </dl> </dd> <dt>

<span id="FWP_E_TXN_IN_PROGRESS"></span><span id="fwp_e_txn_in_progress"></span>**FWP\_E\_TXN\_IN\_PROGRESS**
</dt> <dd> <dl> <dt>

0x8032000E
</dt> <dt>



The call is not allowed from within an explicit transaction.


</dt> </dl> </dd> <dt>

<span id="FWP_E_TXN_ABORTED"></span><span id="fwp_e_txn_aborted"></span>**FWP\_E\_TXN\_ABORTED**
</dt> <dd> <dl> <dt>

0x8032000F
</dt> <dt>



The explicit transaction has been forcibly canceled.


</dt> </dl> </dd> <dt>

<span id="FWP_E_SESSION_ABORTED"></span><span id="fwp_e_session_aborted"></span>**FWP\_E\_SESSION\_ABORTED**
</dt> <dd> <dl> <dt>

0x80320010
</dt> <dt>



The session has been canceled.

The session handle needs to be closed by calling [**FwpmEngineClose0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmengineclose0), even though it is no longer valid; otherwise, the client-side state will be leaked. A new session should be created by calling [**FwpmEngineOpen0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmengineopen0).


</dt> </dl> </dd> <dt>

<span id="FWP_E_INCOMPATIBLE_TXN"></span><span id="fwp_e_incompatible_txn"></span>**FWP\_E\_INCOMPATIBLE\_TXN**
</dt> <dd> <dl> <dt>

0x80320011
</dt> <dt>



The call is not allowed from within a read-only transaction.


</dt> </dl> </dd> <dt>

<span id="FWP_E_TIMEOUT"></span><span id="fwp_e_timeout"></span>**FWP\_E\_TIMEOUT**
</dt> <dd> <dl> <dt>

0x80320012
</dt> <dt>



The call timed out while waiting to acquire the transaction lock.


</dt> </dl> </dd> <dt>

<span id="FWP_E_NET_EVENTS_DISABLED"></span><span id="fwp_e_net_events_disabled"></span>**FWP\_E\_NET\_EVENTS\_DISABLED**
</dt> <dd> <dl> <dt>

0x80320013
</dt> <dt>



The collection of network diagnostic events is disabled.


</dt> </dl> </dd> <dt>

<span id="FWP_E_INCOMPATIBLE_LAYER"></span><span id="fwp_e_incompatible_layer"></span>**FWP\_E\_INCOMPATIBLE\_LAYER**
</dt> <dd> <dl> <dt>

0x80320014
</dt> <dt>



The operation is not supported by the specified layer.


</dt> </dl> </dd> <dt>

<span id="FWP_E_KM_CLIENTS_ONLY"></span><span id="fwp_e_km_clients_only"></span>**FWP\_E\_KM\_CLIENTS\_ONLY**
</dt> <dd> <dl> <dt>

0x80320015
</dt> <dt>



The call is allowed for kernel-mode callers only.


</dt> </dl> </dd> <dt>

<span id="FWP_E_LIFETIME_MISMATCH"></span><span id="fwp_e_lifetime_mismatch"></span>**FWP\_E\_LIFETIME\_MISMATCH**
</dt> <dd> <dl> <dt>

0x80320016
</dt> <dt>



The call tried to associate two objects with incompatible lifetimes.

See [Object Management](object-management.md) for more information on object lifetime and object association.


</dt> </dl> </dd> <dt>

<span id="FWP_E_BUILTIN_OBJECT"></span><span id="fwp_e_builtin_object"></span>**FWP\_E\_BUILTIN\_OBJECT**
</dt> <dd> <dl> <dt>

0x80320017
</dt> <dt>



The object is built-in, so it cannot be deleted.


</dt> </dl> </dd> <dt>

<span id="FWP_E_TOO_MANY_CALLOUTS"></span><span id="fwp_e_too_many_callouts"></span>**FWP\_E\_TOO\_MANY\_CALLOUTS**
</dt> <dd> <dl> <dt>

0x80320018
</dt> <dt>



The maximum number of callouts has been reached.

At most, 100,000 callouts can be registered at the same time.


</dt> </dl> </dd> <dt>

<span id="FWP_E_NOTIFICATION_DROPPED"></span><span id="fwp_e_notification_dropped"></span>**FWP\_E\_NOTIFICATION\_DROPPED**
</dt> <dd> <dl> <dt>

0x80320019
</dt> <dt>



A notification could not be delivered because a message queue is at its maximum capacity.


</dt> </dl> </dd> <dt>

<span id="FWP_E_TRAFFIC_MISMATCH"></span><span id="fwp_e_traffic_mismatch"></span>**FWP\_E\_TRAFFIC\_MISMATCH**
</dt> <dd> <dl> <dt>

0x8032001A
</dt> <dt>



The network traffic parameters do not match those for the security association context.

[**IPsecSaContextGetSpi0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecsacontextgetspi0) can be called multiple times, but the caller must specify the same [**IPSEC\_TRAFFIC0**](/windows/desktop/api/Ipsectypes/ns-ipsectypes-ipsec_traffic0) each time. This error is returned if a subsequent call supplies a different **IPSEC\_TRAFFIC0**.


</dt> </dl> </dd> <dt>

<span id="FWP_E_INCOMPATIBLE_SA_STATE"></span><span id="fwp_e_incompatible_sa_state"></span>**FWP\_E\_INCOMPATIBLE\_SA\_STATE**
</dt> <dd> <dl> <dt>

0x8032001B
</dt> <dt>



The call is not allowed for the current security association (SA) state.

The SA context functions must be called in a specific order:

-   [**IPsecSaContextCreate0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecsacontextcreate0)
-   [**IPsecSaContextGetSpi0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecsacontextgetspi0)
-   [**IPsecSaContextAddInbound0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecsacontextaddinbound0)
-   [**IPsecSaContextAddOutbound0**](/windows/desktop/api/Fwpmu/nf-fwpmu-ipsecsacontextaddoutbound0)

This error is returned if they are called out of order.


</dt> </dl> </dd> <dt>

<span id="FWP_E_NULL_POINTER"></span><span id="fwp_e_null_pointer"></span>**FWP\_E\_NULL\_POINTER**
</dt> <dd> <dl> <dt>

0x8032001C
</dt> <dt>



A required pointer is null.


</dt> </dl> </dd> <dt>

<span id="FWP_E_INVALID_ENUMERATOR"></span><span id="fwp_e_invalid_enumerator"></span>**FWP\_E\_INVALID\_ENUMERATOR**
</dt> <dd> <dl> <dt>

0x8032001D
</dt> <dt>



An enumerator value in a structure is out of range.


</dt> </dl> </dd> <dt>

<span id="FWP_E_INVALID_FLAGS"></span><span id="fwp_e_invalid_flags"></span>**FWP\_E\_INVALID\_FLAGS**
</dt> <dd> <dl> <dt>

0x8032001E
</dt> <dt>



The flags field contains an invalid value.


</dt> </dl> </dd> <dt>

<span id="FWP_E_INVALID_NET_MASK"></span><span id="fwp_e_invalid_net_mask"></span>**FWP\_E\_INVALID\_NET\_MASK**
</dt> <dd> <dl> <dt>

0x8032001F
</dt> <dt>



A network mask is not valid.


</dt> </dl> </dd> <dt>

<span id="FWP_E_INVALID_RANGE"></span><span id="fwp_e_invalid_range"></span>**FWP\_E\_INVALID\_RANGE**
</dt> <dd> <dl> <dt>

0x80320020
</dt> <dt>



An [**FWP\_RANGE0**](/windows/desktop/api/Fwptypes/ns-fwptypes-fwp_range0) structure is not valid.


</dt> </dl> </dd> <dt>

<span id="FWP_E_INVALID_INTERVAL"></span><span id="fwp_e_invalid_interval"></span>**FWP\_E\_INVALID\_INTERVAL**
</dt> <dd> <dl> <dt>

0x80320021
</dt> <dt>



The time interval is not valid.


</dt> </dl> </dd> <dt>

<span id="FWP_E_ZERO_LENGTH_ARRAY"></span><span id="fwp_e_zero_length_array"></span>**FWP\_E\_ZERO\_LENGTH\_ARRAY**
</dt> <dd> <dl> <dt>

0x80320022
</dt> <dt>



An array that must contain at least one element has zero length.


</dt> </dl> </dd> <dt>

<span id="FWP_E_NULL_DISPLAY_NAME"></span><span id="fwp_e_null_display_name"></span>**FWP\_E\_NULL\_DISPLAY\_NAME**
</dt> <dd> <dl> <dt>

0x80320023
</dt> <dt>



The **displayData.name** field cannot be null.


</dt> </dl> </dd> <dt>

<span id="FWP_E_INVALID_ACTION_TYPE"></span><span id="fwp_e_invalid_action_type"></span>**FWP\_E\_INVALID\_ACTION\_TYPE**
</dt> <dd> <dl> <dt>

0x80320024
</dt> <dt>



The action type is not one of the allowed action types for a filter.


</dt> </dl> </dd> <dt>

<span id="FWP_E_INVALID_WEIGHT"></span><span id="fwp_e_invalid_weight"></span>**FWP\_E\_INVALID\_WEIGHT**
</dt> <dd> <dl> <dt>

0x80320025
</dt> <dt>



The filter weight is not valid.

See [Filter Weight Assignment](filter-weight-assignment.md) for more information.


</dt> </dl> </dd> <dt>

<span id="FWP_E_MATCH_TYPE_MISMATCH"></span><span id="fwp_e_match_type_mismatch"></span>**FWP\_E\_MATCH\_TYPE\_MISMATCH**
</dt> <dd> <dl> <dt>

0x80320026
</dt> <dt>



A filter condition contains a match type that is not compatible with the operands.

See [**FWP\_MATCH\_TYPE**](/windows/desktop/api/Fwptypes/ne-fwptypes-fwp_match_type) for more information.


</dt> </dl> </dd> <dt>

<span id="FWP_E_TYPE_MISMATCH"></span><span id="fwp_e_type_mismatch"></span>**FWP\_E\_TYPE\_MISMATCH**
</dt> <dd> <dl> <dt>

0x80320027
</dt> <dt>



An [**FWP\_VALUE0**](/windows/desktop/api/Fwptypes/ns-fwptypes-fwp_value0) structure or an [**FWPM\_CONDITION\_VALUE0**](/windows/desktop/api/Fwptypes/ns-fwptypes-fwp_condition_value0) structure is of the wrong type.


</dt> </dl> </dd> <dt>

<span id="FWP_E_OUT_OF_BOUNDS"></span><span id="fwp_e_out_of_bounds"></span>**FWP\_E\_OUT\_OF\_BOUNDS**
</dt> <dd> <dl> <dt>

0x80320028
</dt> <dt>



An integer value is outside the allowed range.


</dt> </dl> </dd> <dt>

<span id="FWP_E_RESERVED"></span><span id="fwp_e_reserved"></span>**FWP\_E\_RESERVED**
</dt> <dd> <dl> <dt>

0x80320029
</dt> <dt>



A reserved field is nonzero.


</dt> </dl> </dd> <dt>

<span id="FWP_E_DUPLICATE_CONDITION"></span><span id="fwp_e_duplicate_condition"></span>**FWP\_E\_DUPLICATE\_CONDITION**
</dt> <dd> <dl> <dt>

0x8032002A
</dt> <dt>



A filter cannot contain multiple conditions operating on a single field.


</dt> </dl> </dd> <dt>

<span id="FWP_E_DUPLICATE_KEYMOD"></span><span id="fwp_e_duplicate_keymod"></span>**FWP\_E\_DUPLICATE\_KEYMOD**
</dt> <dd> <dl> <dt>

0x8032002B
</dt> <dt>



A policy cannot contain the same keying module more than once.


</dt> </dl> </dd> <dt>

<span id="FWP_E_ACTION_INCOMPATIBLE_WITH_LAYER"></span><span id="fwp_e_action_incompatible_with_layer"></span>**FWP\_E\_ACTION\_INCOMPATIBLE\_WITH\_LAYER**
</dt> <dd> <dl> <dt>

0x8032002C
</dt> <dt>



The action type is not compatible with the layer.


</dt> </dl> </dd> <dt>

<span id="FWP_E_ACTION_INCOMPATIBLE_WITH_SUBLAYER"></span><span id="fwp_e_action_incompatible_with_sublayer"></span>**FWP\_E\_ACTION\_INCOMPATIBLE\_WITH\_SUBLAYER**
</dt> <dd> <dl> <dt>

0x8032002D
</dt> <dt>



The action type is not compatible with the sub-layer.


</dt> </dl> </dd> <dt>

<span id="FWP_E_CONTEXT_INCOMPATIBLE_WITH_LAYER"></span><span id="fwp_e_context_incompatible_with_layer"></span>**FWP\_E\_CONTEXT\_INCOMPATIBLE\_WITH\_LAYER**
</dt> <dd> <dl> <dt>

0x8032002E
</dt> <dt>



The raw context or the provider context is not compatible with the layer.


</dt> </dl> </dd> <dt>

<span id="FWP_E_CONTEXT_INCOMPATIBLE_WITH_CALLOUT"></span><span id="fwp_e_context_incompatible_with_callout"></span>**FWP\_E\_CONTEXT\_INCOMPATIBLE\_WITH\_CALLOUT**
</dt> <dd> <dl> <dt>

0x8032002F
</dt> <dt>



The raw context or the provider context is not compatible with the callout.


</dt> </dl> </dd> <dt>

<span id="FWP_E_INCOMPATIBLE_AUTH_METHOD"></span><span id="fwp_e_incompatible_auth_method"></span>**FWP\_E\_INCOMPATIBLE\_AUTH\_METHOD**
</dt> <dd> <dl> <dt>

0x80320030
</dt> <dt>



The authentication method is not compatible with the policy type.


</dt> </dl> </dd> <dt>

<span id="FWP_E_INCOMPATIBLE_DH_GROUP"></span><span id="fwp_e_incompatible_dh_group"></span>**FWP\_E\_INCOMPATIBLE\_DH\_GROUP**
</dt> <dd> <dl> <dt>

0x80320031L
</dt> <dt>



The Diffie-Hellman group is not compatible with the policy type.


</dt> </dl> </dd> <dt>

<span id="FWP_E_EM_NOT_SUPPORTED"></span><span id="fwp_e_em_not_supported"></span>**FWP\_E\_EM\_NOT\_SUPPORTED**
</dt> <dd> <dl> <dt>

0x80320032
</dt> <dt>



An IKE policy cannot contain an Extended Mode policy.


</dt> </dl> </dd> <dt>

<span id="FWP_E_NEVER_MATCH"></span><span id="fwp_e_never_match"></span>**FWP\_E\_NEVER\_MATCH**
</dt> <dd> <dl> <dt>

0x80320033
</dt> <dt>



The enumeration template or subscription will never match any objects.


</dt> </dl> </dd> <dt>

<span id="FWP_E_PROVIDER_CONTEXT_MISMATCH"></span><span id="fwp_e_provider_context_mismatch"></span>**FWP\_E\_PROVIDER\_CONTEXT\_MISMATCH**
</dt> <dd> <dl> <dt>

0x80320034
</dt> <dt>



The provider context is of the wrong type.


</dt> </dl> </dd> <dt>

<span id="FWP_E_INVALID_PARAMETER"></span><span id="fwp_e_invalid_parameter"></span>**FWP\_E\_INVALID\_PARAMETER**
</dt> <dd> <dl> <dt>

0x80320035
</dt> <dt>



The parameter is incorrect.

Possible reasons for this error:

-   [**FwpmIPsecTunnelAdd0**](/windows/desktop/api/Fwpmu/nf-fwpmu-fwpmipsectunneladd0) was called without setting the flag **FWPM\_TUNNEL\_FLAG\_POINT\_TO\_POINT** and with conditions other than local/remote address.
-   An invalid Unicode string, or a Unicode string that contains unprintable characters.


</dt> </dl> </dd> <dt>

<span id="FWP_E_TOO_MANY_SUBLAYERS"></span><span id="fwp_e_too_many_sublayers"></span>**FWP\_E\_TOO\_MANY\_SUBLAYERS**
</dt> <dd> <dl> <dt>

0x80320036
</dt> <dt>



The maximum number of sublayers has been reached.

WFP supports at most 2 6 sublayers.


</dt> </dl> </dd> <dt>

<span id="FWP_E_CALLOUT_NOTIFICATION_FAILED"></span><span id="fwp_e_callout_notification_failed"></span>**FWP\_E\_CALLOUT\_NOTIFICATION\_FAILED**
</dt> <dd> <dl> <dt>

0x80320037
</dt> <dt>



The notification function for a callout returned an error.


</dt> </dl> </dd> <dt>

<span id="FWP_E_INVALID_AUTH_TRANSFORM"></span><span id="fwp_e_invalid_auth_transform"></span>**FWP\_E\_INVALID\_AUTH\_TRANSFORM**
</dt> <dd> <dl> <dt>

0x80320038
</dt> <dt>



The IPsec authentication transform is not valid.


</dt> </dl> </dd> <dt>

<span id="FWP_E_INVALID_CIPHER_TRANSFORM"></span><span id="fwp_e_invalid_cipher_transform"></span>**FWP\_E\_INVALID\_CIPHER\_TRANSFORM**
</dt> <dd> <dl> <dt>

0x80320039
</dt> <dt>



The IPsec cipher transform is not valid.


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Winerror.h</dt> </dl> |



 

 





