---
description: Describes error codes 8200-8999 defined in the WinError.h header file and is intended for developers.
ms.assetid: f16fdfa3-b080-47ee-a7dd-241fe2d24278
title: System Error Codes (8200-8999) (WinError.h)
ms.topic: reference
ms.date: 07/18/2019
---

# System Error Codes (8200-8999)

> [!NOTE]
> This information is intended for developers debugging system errors. For other errors, such as issues with Windows Update, there is a list of resources on the [Error codes](system-error-codes.md) page.

The following list describes [system error codes](system-error-codes.md) for errors 8200 to 8999. They are returned by the [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) function when many functions fail. To retrieve the description text for the error in your application, use the [**FormatMessage**](/windows/desktop/api/WinBase/nf-winbase-formatmessage) function with the **FORMAT\_MESSAGE\_FROM\_SYSTEM** flag.

<dl> <dt>

<span id="ERROR_DS_NOT_INSTALLED"></span><span id="error_ds_not_installed"></span>**ERROR\_DS\_NOT\_INSTALLED**
</dt> <dd> <dl> <dt>

8200 (0x2008)
</dt> <dt>



An error occurred while installing the directory service. For more information, see the event log.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_MEMBERSHIP_EVALUATED_LOCALLY"></span><span id="error_ds_membership_evaluated_locally"></span>**ERROR\_DS\_MEMBERSHIP\_EVALUATED\_LOCALLY**
</dt> <dd> <dl> <dt>

8201 (0x2009)
</dt> <dt>



The directory service evaluated group memberships locally.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NO_ATTRIBUTE_OR_VALUE"></span><span id="error_ds_no_attribute_or_value"></span>**ERROR\_DS\_NO\_ATTRIBUTE\_OR\_VALUE**
</dt> <dd> <dl> <dt>

8202 (0x200A)
</dt> <dt>



The specified directory service attribute or value does not exist.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_INVALID_ATTRIBUTE_SYNTAX"></span><span id="error_ds_invalid_attribute_syntax"></span>**ERROR\_DS\_INVALID\_ATTRIBUTE\_SYNTAX**
</dt> <dd> <dl> <dt>

8203 (0x200B)
</dt> <dt>



The attribute syntax specified to the directory service is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_ATTRIBUTE_TYPE_UNDEFINED"></span><span id="error_ds_attribute_type_undefined"></span>**ERROR\_DS\_ATTRIBUTE\_TYPE\_UNDEFINED**
</dt> <dd> <dl> <dt>

8204 (0x200C)
</dt> <dt>



The attribute type specified to the directory service is not defined.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_ATTRIBUTE_OR_VALUE_EXISTS"></span><span id="error_ds_attribute_or_value_exists"></span>**ERROR\_DS\_ATTRIBUTE\_OR\_VALUE\_EXISTS**
</dt> <dd> <dl> <dt>

8205 (0x200D)
</dt> <dt>



The specified directory service attribute or value already exists.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_BUSY"></span><span id="error_ds_busy"></span>**ERROR\_DS\_BUSY**
</dt> <dd> <dl> <dt>

8206 (0x200E)
</dt> <dt>



The directory service is busy.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_UNAVAILABLE"></span><span id="error_ds_unavailable"></span>**ERROR\_DS\_UNAVAILABLE**
</dt> <dd> <dl> <dt>

8207 (0x200F)
</dt> <dt>



The directory service is unavailable.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NO_RIDS_ALLOCATED"></span><span id="error_ds_no_rids_allocated"></span>**ERROR\_DS\_NO\_RIDS\_ALLOCATED**
</dt> <dd> <dl> <dt>

8208 (0x2010)
</dt> <dt>



The directory service was unable to allocate a relative identifier.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NO_MORE_RIDS"></span><span id="error_ds_no_more_rids"></span>**ERROR\_DS\_NO\_MORE\_RIDS**
</dt> <dd> <dl> <dt>

8209 (0x2011)
</dt> <dt>



The directory service has exhausted the pool of relative identifiers.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_INCORRECT_ROLE_OWNER"></span><span id="error_ds_incorrect_role_owner"></span>**ERROR\_DS\_INCORRECT\_ROLE\_OWNER**
</dt> <dd> <dl> <dt>

8210 (0x2012)
</dt> <dt>



The requested operation could not be performed because the directory service is not the master for that type of operation.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_RIDMGR_INIT_ERROR"></span><span id="error_ds_ridmgr_init_error"></span>**ERROR\_DS\_RIDMGR\_INIT\_ERROR**
</dt> <dd> <dl> <dt>

8211 (0x2013)
</dt> <dt>



The directory service was unable to initialize the subsystem that allocates relative identifiers.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_OBJ_CLASS_VIOLATION"></span><span id="error_ds_obj_class_violation"></span>**ERROR\_DS\_OBJ\_CLASS\_VIOLATION**
</dt> <dd> <dl> <dt>

8212 (0x2014)
</dt> <dt>



The requested operation did not satisfy one or more constraints associated with the class of the object.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CANT_ON_NON_LEAF"></span><span id="error_ds_cant_on_non_leaf"></span>**ERROR\_DS\_CANT\_ON\_NON\_LEAF**
</dt> <dd> <dl> <dt>

8213 (0x2015)
</dt> <dt>



The directory service can perform the requested operation only on a leaf object.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CANT_ON_RDN"></span><span id="error_ds_cant_on_rdn"></span>**ERROR\_DS\_CANT\_ON\_RDN**
</dt> <dd> <dl> <dt>

8214 (0x2016)
</dt> <dt>



The directory service cannot perform the requested operation on the RDN attribute of an object.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CANT_MOD_OBJ_CLASS"></span><span id="error_ds_cant_mod_obj_class"></span>**ERROR\_DS\_CANT\_MOD\_OBJ\_CLASS**
</dt> <dd> <dl> <dt>

8215 (0x2017)
</dt> <dt>



The directory service detected an attempt to modify the object class of an object.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CROSS_DOM_MOVE_ERROR"></span><span id="error_ds_cross_dom_move_error"></span>**ERROR\_DS\_CROSS\_DOM\_MOVE\_ERROR**
</dt> <dd> <dl> <dt>

8216 (0x2018)
</dt> <dt>



The requested cross-domain move operation could not be performed.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_GC_NOT_AVAILABLE"></span><span id="error_ds_gc_not_available"></span>**ERROR\_DS\_GC\_NOT\_AVAILABLE**
</dt> <dd> <dl> <dt>

8217 (0x2019)
</dt> <dt>



Unable to contact the global catalog server.


</dt> </dl> </dd> <dt>

<span id="ERROR_SHARED_POLICY"></span><span id="error_shared_policy"></span>**ERROR\_SHARED\_POLICY**
</dt> <dd> <dl> <dt>

8218 (0x201A)
</dt> <dt>



The policy object is shared and can only be modified at the root.


</dt> </dl> </dd> <dt>

<span id="ERROR_POLICY_OBJECT_NOT_FOUND"></span><span id="error_policy_object_not_found"></span>**ERROR\_POLICY\_OBJECT\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

8219 (0x201B)
</dt> <dt>



The policy object does not exist.


</dt> </dl> </dd> <dt>

<span id="ERROR_POLICY_ONLY_IN_DS"></span><span id="error_policy_only_in_ds"></span>**ERROR\_POLICY\_ONLY\_IN\_DS**
</dt> <dd> <dl> <dt>

8220 (0x201C)
</dt> <dt>



The requested policy information is only in the directory service.


</dt> </dl> </dd> <dt>

<span id="ERROR_PROMOTION_ACTIVE"></span><span id="error_promotion_active"></span>**ERROR\_PROMOTION\_ACTIVE**
</dt> <dd> <dl> <dt>

8221 (0x201D)
</dt> <dt>



A domain controller promotion is currently active.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_PROMOTION_ACTIVE"></span><span id="error_no_promotion_active"></span>**ERROR\_NO\_PROMOTION\_ACTIVE**
</dt> <dd> <dl> <dt>

8222 (0x201E)
</dt> <dt>



A domain controller promotion is not currently active.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_OPERATIONS_ERROR"></span><span id="error_ds_operations_error"></span>**ERROR\_DS\_OPERATIONS\_ERROR**
</dt> <dd> <dl> <dt>

8224 (0x2020)
</dt> <dt>



An operations error occurred.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_PROTOCOL_ERROR"></span><span id="error_ds_protocol_error"></span>**ERROR\_DS\_PROTOCOL\_ERROR**
</dt> <dd> <dl> <dt>

8225 (0x2021)
</dt> <dt>



A protocol error occurred.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_TIMELIMIT_EXCEEDED"></span><span id="error_ds_timelimit_exceeded"></span>**ERROR\_DS\_TIMELIMIT\_EXCEEDED**
</dt> <dd> <dl> <dt>

8226 (0x2022)
</dt> <dt>



The time limit for this request was exceeded.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_SIZELIMIT_EXCEEDED"></span><span id="error_ds_sizelimit_exceeded"></span>**ERROR\_DS\_SIZELIMIT\_EXCEEDED**
</dt> <dd> <dl> <dt>

8227 (0x2023)
</dt> <dt>



The size limit for this request was exceeded.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_ADMIN_LIMIT_EXCEEDED"></span><span id="error_ds_admin_limit_exceeded"></span>**ERROR\_DS\_ADMIN\_LIMIT\_EXCEEDED**
</dt> <dd> <dl> <dt>

8228 (0x2024)
</dt> <dt>



The administrative limit for this request was exceeded.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_COMPARE_FALSE"></span><span id="error_ds_compare_false"></span>**ERROR\_DS\_COMPARE\_FALSE**
</dt> <dd> <dl> <dt>

8229 (0x2025)
</dt> <dt>



The compare response was false.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_COMPARE_TRUE"></span><span id="error_ds_compare_true"></span>**ERROR\_DS\_COMPARE\_TRUE**
</dt> <dd> <dl> <dt>

8230 (0x2026)
</dt> <dt>



The compare response was true.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_AUTH_METHOD_NOT_SUPPORTED"></span><span id="error_ds_auth_method_not_supported"></span>**ERROR\_DS\_AUTH\_METHOD\_NOT\_SUPPORTED**
</dt> <dd> <dl> <dt>

8231 (0x2027)
</dt> <dt>



The requested authentication method is not supported by the server.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_STRONG_AUTH_REQUIRED"></span><span id="error_ds_strong_auth_required"></span>**ERROR\_DS\_STRONG\_AUTH\_REQUIRED**
</dt> <dd> <dl> <dt>

8232 (0x2028)
</dt> <dt>



A more secure authentication method is required for this server.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_INAPPROPRIATE_AUTH"></span><span id="error_ds_inappropriate_auth"></span>**ERROR\_DS\_INAPPROPRIATE\_AUTH**
</dt> <dd> <dl> <dt>

8233 (0x2029)
</dt> <dt>



Inappropriate authentication.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_AUTH_UNKNOWN"></span><span id="error_ds_auth_unknown"></span>**ERROR\_DS\_AUTH\_UNKNOWN**
</dt> <dd> <dl> <dt>

8234 (0x202A)
</dt> <dt>



The authentication mechanism is unknown.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_REFERRAL"></span><span id="error_ds_referral"></span>**ERROR\_DS\_REFERRAL**
</dt> <dd> <dl> <dt>

8235 (0x202B)
</dt> <dt>



A referral was returned from the server.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_UNAVAILABLE_CRIT_EXTENSION"></span><span id="error_ds_unavailable_crit_extension"></span>**ERROR\_DS\_UNAVAILABLE\_CRIT\_EXTENSION**
</dt> <dd> <dl> <dt>

8236 (0x202C)
</dt> <dt>



The server does not support the requested critical extension.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CONFIDENTIALITY_REQUIRED"></span><span id="error_ds_confidentiality_required"></span>**ERROR\_DS\_CONFIDENTIALITY\_REQUIRED**
</dt> <dd> <dl> <dt>

8237 (0x202D)
</dt> <dt>



This request requires a secure connection.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_INAPPROPRIATE_MATCHING"></span><span id="error_ds_inappropriate_matching"></span>**ERROR\_DS\_INAPPROPRIATE\_MATCHING**
</dt> <dd> <dl> <dt>

8238 (0x202E)
</dt> <dt>



Inappropriate matching.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CONSTRAINT_VIOLATION"></span><span id="error_ds_constraint_violation"></span>**ERROR\_DS\_CONSTRAINT\_VIOLATION**
</dt> <dd> <dl> <dt>

8239 (0x202F)
</dt> <dt>



A constraint violation occurred.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NO_SUCH_OBJECT"></span><span id="error_ds_no_such_object"></span>**ERROR\_DS\_NO\_SUCH\_OBJECT**
</dt> <dd> <dl> <dt>

8240 (0x2030)
</dt> <dt>



There is no such object on the server.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_ALIAS_PROBLEM"></span><span id="error_ds_alias_problem"></span>**ERROR\_DS\_ALIAS\_PROBLEM**
</dt> <dd> <dl> <dt>

8241 (0x2031)
</dt> <dt>



There is an alias problem.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_INVALID_DN_SYNTAX"></span><span id="error_ds_invalid_dn_syntax"></span>**ERROR\_DS\_INVALID\_DN\_SYNTAX**
</dt> <dd> <dl> <dt>

8242 (0x2032)
</dt> <dt>



An invalid dn syntax has been specified.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_IS_LEAF"></span><span id="error_ds_is_leaf"></span>**ERROR\_DS\_IS\_LEAF**
</dt> <dd> <dl> <dt>

8243 (0x2033)
</dt> <dt>



The object is a leaf object.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_ALIAS_DEREF_PROBLEM"></span><span id="error_ds_alias_deref_problem"></span>**ERROR\_DS\_ALIAS\_DEREF\_PROBLEM**
</dt> <dd> <dl> <dt>

8244 (0x2034)
</dt> <dt>



There is an alias dereferencing problem.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_UNWILLING_TO_PERFORM"></span><span id="error_ds_unwilling_to_perform"></span>**ERROR\_DS\_UNWILLING\_TO\_PERFORM**
</dt> <dd> <dl> <dt>

8245 (0x2035)
</dt> <dt>



The server is unwilling to process the request.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_LOOP_DETECT"></span><span id="error_ds_loop_detect"></span>**ERROR\_DS\_LOOP\_DETECT**
</dt> <dd> <dl> <dt>

8246 (0x2036)
</dt> <dt>



A loop has been detected.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NAMING_VIOLATION"></span><span id="error_ds_naming_violation"></span>**ERROR\_DS\_NAMING\_VIOLATION**
</dt> <dd> <dl> <dt>

8247 (0x2037)
</dt> <dt>



There is a naming violation.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_OBJECT_RESULTS_TOO_LARGE"></span><span id="error_ds_object_results_too_large"></span>**ERROR\_DS\_OBJECT\_RESULTS\_TOO\_LARGE**
</dt> <dd> <dl> <dt>

8248 (0x2038)
</dt> <dt>



The result set is too large.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_AFFECTS_MULTIPLE_DSAS"></span><span id="error_ds_affects_multiple_dsas"></span>**ERROR\_DS\_AFFECTS\_MULTIPLE\_DSAS**
</dt> <dd> <dl> <dt>

8249 (0x2039)
</dt> <dt>



The operation affects multiple DSAs.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_SERVER_DOWN"></span><span id="error_ds_server_down"></span>**ERROR\_DS\_SERVER\_DOWN**
</dt> <dd> <dl> <dt>

8250 (0x203A)
</dt> <dt>



The server is not operational.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_LOCAL_ERROR"></span><span id="error_ds_local_error"></span>**ERROR\_DS\_LOCAL\_ERROR**
</dt> <dd> <dl> <dt>

8251 (0x203B)
</dt> <dt>



A local error has occurred.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_ENCODING_ERROR"></span><span id="error_ds_encoding_error"></span>**ERROR\_DS\_ENCODING\_ERROR**
</dt> <dd> <dl> <dt>

8252 (0x203C)
</dt> <dt>



An encoding error has occurred.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DECODING_ERROR"></span><span id="error_ds_decoding_error"></span>**ERROR\_DS\_DECODING\_ERROR**
</dt> <dd> <dl> <dt>

8253 (0x203D)
</dt> <dt>



A decoding error has occurred.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_FILTER_UNKNOWN"></span><span id="error_ds_filter_unknown"></span>**ERROR\_DS\_FILTER\_UNKNOWN**
</dt> <dd> <dl> <dt>

8254 (0x203E)
</dt> <dt>



The search filter cannot be recognized.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_PARAM_ERROR"></span><span id="error_ds_param_error"></span>**ERROR\_DS\_PARAM\_ERROR**
</dt> <dd> <dl> <dt>

8255 (0x203F)
</dt> <dt>



One or more parameters are illegal.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NOT_SUPPORTED"></span><span id="error_ds_not_supported"></span>**ERROR\_DS\_NOT\_SUPPORTED**
</dt> <dd> <dl> <dt>

8256 (0x2040)
</dt> <dt>



The specified method is not supported.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NO_RESULTS_RETURNED"></span><span id="error_ds_no_results_returned"></span>**ERROR\_DS\_NO\_RESULTS\_RETURNED**
</dt> <dd> <dl> <dt>

8257 (0x2041)
</dt> <dt>



No results were returned.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CONTROL_NOT_FOUND"></span><span id="error_ds_control_not_found"></span>**ERROR\_DS\_CONTROL\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

8258 (0x2042)
</dt> <dt>



The specified control is not supported by the server.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CLIENT_LOOP"></span><span id="error_ds_client_loop"></span>**ERROR\_DS\_CLIENT\_LOOP**
</dt> <dd> <dl> <dt>

8259 (0x2043)
</dt> <dt>



A referral loop was detected by the client.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_REFERRAL_LIMIT_EXCEEDED"></span><span id="error_ds_referral_limit_exceeded"></span>**ERROR\_DS\_REFERRAL\_LIMIT\_EXCEEDED**
</dt> <dd> <dl> <dt>

8260 (0x2044)
</dt> <dt>



The preset referral limit was exceeded.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_SORT_CONTROL_MISSING"></span><span id="error_ds_sort_control_missing"></span>**ERROR\_DS\_SORT\_CONTROL\_MISSING**
</dt> <dd> <dl> <dt>

8261 (0x2045)
</dt> <dt>



The search requires a SORT control.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_OFFSET_RANGE_ERROR"></span><span id="error_ds_offset_range_error"></span>**ERROR\_DS\_OFFSET\_RANGE\_ERROR**
</dt> <dd> <dl> <dt>

8262 (0x2046)
</dt> <dt>



The search results exceed the offset range specified.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_RIDMGR_DISABLED"></span><span id="error_ds_ridmgr_disabled"></span>**ERROR\_DS\_RIDMGR\_DISABLED**
</dt> <dd> <dl> <dt>

8263 (0x2047)
</dt> <dt>



The directory service detected the subsystem that allocates relative identifiers is disabled. This can occur as a protective mechanism when the system determines a significant portion of relative identifiers (RIDs) have been exhausted. Please see <https://go.microsoft.com/fwlink/p/?linkid=228610> for recommended diagnostic steps and the procedure to re-enable account creation.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_ROOT_MUST_BE_NC"></span><span id="error_ds_root_must_be_nc"></span>**ERROR\_DS\_ROOT\_MUST\_BE\_NC**
</dt> <dd> <dl> <dt>

8301 (0x206D)
</dt> <dt>



The root object must be the head of a naming context. The root object cannot have an instantiated parent.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_ADD_REPLICA_INHIBITED"></span><span id="error_ds_add_replica_inhibited"></span>**ERROR\_DS\_ADD\_REPLICA\_INHIBITED**
</dt> <dd> <dl> <dt>

8302 (0x206E)
</dt> <dt>



The add replica operation cannot be performed. The naming context must be writeable in order to create the replica.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_ATT_NOT_DEF_IN_SCHEMA"></span><span id="error_ds_att_not_def_in_schema"></span>**ERROR\_DS\_ATT\_NOT\_DEF\_IN\_SCHEMA**
</dt> <dd> <dl> <dt>

8303 (0x206F)
</dt> <dt>



A reference to an attribute that is not defined in the schema occurred.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_MAX_OBJ_SIZE_EXCEEDED"></span><span id="error_ds_max_obj_size_exceeded"></span>**ERROR\_DS\_MAX\_OBJ\_SIZE\_EXCEEDED**
</dt> <dd> <dl> <dt>

8304 (0x2070)
</dt> <dt>



The maximum size of an object has been exceeded.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_OBJ_STRING_NAME_EXISTS"></span><span id="error_ds_obj_string_name_exists"></span>**ERROR\_DS\_OBJ\_STRING\_NAME\_EXISTS**
</dt> <dd> <dl> <dt>

8305 (0x2071)
</dt> <dt>



An attempt was made to add an object to the directory with a name that is already in use.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NO_RDN_DEFINED_IN_SCHEMA"></span><span id="error_ds_no_rdn_defined_in_schema"></span>**ERROR\_DS\_NO\_RDN\_DEFINED\_IN\_SCHEMA**
</dt> <dd> <dl> <dt>

8306 (0x2072)
</dt> <dt>



An attempt was made to add an object of a class that does not have an RDN defined in the schema.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_RDN_DOESNT_MATCH_SCHEMA"></span><span id="error_ds_rdn_doesnt_match_schema"></span>**ERROR\_DS\_RDN\_DOESNT\_MATCH\_SCHEMA**
</dt> <dd> <dl> <dt>

8307 (0x2073)
</dt> <dt>



An attempt was made to add an object using an RDN that is not the RDN defined in the schema.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NO_REQUESTED_ATTS_FOUND"></span><span id="error_ds_no_requested_atts_found"></span>**ERROR\_DS\_NO\_REQUESTED\_ATTS\_FOUND**
</dt> <dd> <dl> <dt>

8308 (0x2074)
</dt> <dt>



None of the requested attributes were found on the objects.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_USER_BUFFER_TO_SMALL"></span><span id="error_ds_user_buffer_to_small"></span>**ERROR\_DS\_USER\_BUFFER\_TO\_SMALL**
</dt> <dd> <dl> <dt>

8309 (0x2075)
</dt> <dt>



The user buffer is too small.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_ATT_IS_NOT_ON_OBJ"></span><span id="error_ds_att_is_not_on_obj"></span>**ERROR\_DS\_ATT\_IS\_NOT\_ON\_OBJ**
</dt> <dd> <dl> <dt>

8310 (0x2076)
</dt> <dt>



The attribute specified in the operation is not present on the object.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_ILLEGAL_MOD_OPERATION"></span><span id="error_ds_illegal_mod_operation"></span>**ERROR\_DS\_ILLEGAL\_MOD\_OPERATION**
</dt> <dd> <dl> <dt>

8311 (0x2077)
</dt> <dt>



Illegal modify operation. Some aspect of the modification is not permitted.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_OBJ_TOO_LARGE"></span><span id="error_ds_obj_too_large"></span>**ERROR\_DS\_OBJ\_TOO\_LARGE**
</dt> <dd> <dl> <dt>

8312 (0x2078)
</dt> <dt>



The specified object is too large.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_BAD_INSTANCE_TYPE"></span><span id="error_ds_bad_instance_type"></span>**ERROR\_DS\_BAD\_INSTANCE\_TYPE**
</dt> <dd> <dl> <dt>

8313 (0x2079)
</dt> <dt>



The specified instance type is not valid.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_MASTERDSA_REQUIRED"></span><span id="error_ds_masterdsa_required"></span>**ERROR\_DS\_MASTERDSA\_REQUIRED**
</dt> <dd> <dl> <dt>

8314 (0x207A)
</dt> <dt>



The operation must be performed at a master DSA.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_OBJECT_CLASS_REQUIRED"></span><span id="error_ds_object_class_required"></span>**ERROR\_DS\_OBJECT\_CLASS\_REQUIRED**
</dt> <dd> <dl> <dt>

8315 (0x207B)
</dt> <dt>



The object class attribute must be specified.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_MISSING_REQUIRED_ATT"></span><span id="error_ds_missing_required_att"></span>**ERROR\_DS\_MISSING\_REQUIRED\_ATT**
</dt> <dd> <dl> <dt>

8316 (0x207C)
</dt> <dt>



A required attribute is missing.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_ATT_NOT_DEF_FOR_CLASS"></span><span id="error_ds_att_not_def_for_class"></span>**ERROR\_DS\_ATT\_NOT\_DEF\_FOR\_CLASS**
</dt> <dd> <dl> <dt>

8317 (0x207D)
</dt> <dt>



An attempt was made to modify an object to include an attribute that is not legal for its class.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_ATT_ALREADY_EXISTS"></span><span id="error_ds_att_already_exists"></span>**ERROR\_DS\_ATT\_ALREADY\_EXISTS**
</dt> <dd> <dl> <dt>

8318 (0x207E)
</dt> <dt>



The specified attribute is already present on the object.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CANT_ADD_ATT_VALUES"></span><span id="error_ds_cant_add_att_values"></span>**ERROR\_DS\_CANT\_ADD\_ATT\_VALUES**
</dt> <dd> <dl> <dt>

8320 (0x2080)
</dt> <dt>



The specified attribute is not present, or has no values.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_SINGLE_VALUE_CONSTRAINT"></span><span id="error_ds_single_value_constraint"></span>**ERROR\_DS\_SINGLE\_VALUE\_CONSTRAINT**
</dt> <dd> <dl> <dt>

8321 (0x2081)
</dt> <dt>



Multiple values were specified for an attribute that can have only one value.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_RANGE_CONSTRAINT"></span><span id="error_ds_range_constraint"></span>**ERROR\_DS\_RANGE\_CONSTRAINT**
</dt> <dd> <dl> <dt>

8322 (0x2082)
</dt> <dt>



A value for the attribute was not in the acceptable range of values.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_ATT_VAL_ALREADY_EXISTS"></span><span id="error_ds_att_val_already_exists"></span>**ERROR\_DS\_ATT\_VAL\_ALREADY\_EXISTS**
</dt> <dd> <dl> <dt>

8323 (0x2083)
</dt> <dt>



The specified value already exists.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CANT_REM_MISSING_ATT"></span><span id="error_ds_cant_rem_missing_att"></span>**ERROR\_DS\_CANT\_REM\_MISSING\_ATT**
</dt> <dd> <dl> <dt>

8324 (0x2084)
</dt> <dt>



The attribute cannot be removed because it is not present on the object.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CANT_REM_MISSING_ATT_VAL"></span><span id="error_ds_cant_rem_missing_att_val"></span>**ERROR\_DS\_CANT\_REM\_MISSING\_ATT\_VAL**
</dt> <dd> <dl> <dt>

8325 (0x2085)
</dt> <dt>



The attribute value cannot be removed because it is not present on the object.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_ROOT_CANT_BE_SUBREF"></span><span id="error_ds_root_cant_be_subref"></span>**ERROR\_DS\_ROOT\_CANT\_BE\_SUBREF**
</dt> <dd> <dl> <dt>

8326 (0x2086)
</dt> <dt>



The specified root object cannot be a subref.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NO_CHAINING"></span><span id="error_ds_no_chaining"></span>**ERROR\_DS\_NO\_CHAINING**
</dt> <dd> <dl> <dt>

8327 (0x2087)
</dt> <dt>



Chaining is not permitted.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NO_CHAINED_EVAL"></span><span id="error_ds_no_chained_eval"></span>**ERROR\_DS\_NO\_CHAINED\_EVAL**
</dt> <dd> <dl> <dt>

8328 (0x2088)
</dt> <dt>



Chained evaluation is not permitted.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NO_PARENT_OBJECT"></span><span id="error_ds_no_parent_object"></span>**ERROR\_DS\_NO\_PARENT\_OBJECT**
</dt> <dd> <dl> <dt>

8329 (0x2089)
</dt> <dt>



The operation could not be performed because the object's parent is either uninstantiated or deleted.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_PARENT_IS_AN_ALIAS"></span><span id="error_ds_parent_is_an_alias"></span>**ERROR\_DS\_PARENT\_IS\_AN\_ALIAS**
</dt> <dd> <dl> <dt>

8330 (0x208A)
</dt> <dt>



Having a parent that is an alias is not permitted. Aliases are leaf objects.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CANT_MIX_MASTER_AND_REPS"></span><span id="error_ds_cant_mix_master_and_reps"></span>**ERROR\_DS\_CANT\_MIX\_MASTER\_AND\_REPS**
</dt> <dd> <dl> <dt>

8331 (0x208B)
</dt> <dt>



The object and parent must be of the same type, either both masters or both replicas.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CHILDREN_EXIST"></span><span id="error_ds_children_exist"></span>**ERROR\_DS\_CHILDREN\_EXIST**
</dt> <dd> <dl> <dt>

8332 (0x208C)
</dt> <dt>



The operation cannot be performed because child objects exist. This operation can only be performed on a leaf object.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_OBJ_NOT_FOUND"></span><span id="error_ds_obj_not_found"></span>**ERROR\_DS\_OBJ\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

8333 (0x208D)
</dt> <dt>



Directory object not found.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_ALIASED_OBJ_MISSING"></span><span id="error_ds_aliased_obj_missing"></span>**ERROR\_DS\_ALIASED\_OBJ\_MISSING**
</dt> <dd> <dl> <dt>

8334 (0x208E)
</dt> <dt>



The aliased object is missing.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_BAD_NAME_SYNTAX"></span><span id="error_ds_bad_name_syntax"></span>**ERROR\_DS\_BAD\_NAME\_SYNTAX**
</dt> <dd> <dl> <dt>

8335 (0x208F)
</dt> <dt>



The object name has bad syntax.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_ALIAS_POINTS_TO_ALIAS"></span><span id="error_ds_alias_points_to_alias"></span>**ERROR\_DS\_ALIAS\_POINTS\_TO\_ALIAS**
</dt> <dd> <dl> <dt>

8336 (0x2090)
</dt> <dt>



It is not permitted for an alias to refer to another alias.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CANT_DEREF_ALIAS"></span><span id="error_ds_cant_deref_alias"></span>**ERROR\_DS\_CANT\_DEREF\_ALIAS**
</dt> <dd> <dl> <dt>

8337 (0x2091)
</dt> <dt>



The alias cannot be dereferenced.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_OUT_OF_SCOPE"></span><span id="error_ds_out_of_scope"></span>**ERROR\_DS\_OUT\_OF\_SCOPE**
</dt> <dd> <dl> <dt>

8338 (0x2092)
</dt> <dt>



The operation is out of scope.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_OBJECT_BEING_REMOVED"></span><span id="error_ds_object_being_removed"></span>**ERROR\_DS\_OBJECT\_BEING\_REMOVED**
</dt> <dd> <dl> <dt>

8339 (0x2093)
</dt> <dt>



The operation cannot continue because the object is in the process of being removed.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CANT_DELETE_DSA_OBJ"></span><span id="error_ds_cant_delete_dsa_obj"></span>**ERROR\_DS\_CANT\_DELETE\_DSA\_OBJ**
</dt> <dd> <dl> <dt>

8340 (0x2094)
</dt> <dt>



The DSA object cannot be deleted.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_GENERIC_ERROR"></span><span id="error_ds_generic_error"></span>**ERROR\_DS\_GENERIC\_ERROR**
</dt> <dd> <dl> <dt>

8341 (0x2095)
</dt> <dt>



A directory service error has occurred.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DSA_MUST_BE_INT_MASTER"></span><span id="error_ds_dsa_must_be_int_master"></span>**ERROR\_DS\_DSA\_MUST\_BE\_INT\_MASTER**
</dt> <dd> <dl> <dt>

8342 (0x2096)
</dt> <dt>



The operation can only be performed on an internal master DSA object.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CLASS_NOT_DSA"></span><span id="error_ds_class_not_dsa"></span>**ERROR\_DS\_CLASS\_NOT\_DSA**
</dt> <dd> <dl> <dt>

8343 (0x2097)
</dt> <dt>



The object must be of class DSA.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_INSUFF_ACCESS_RIGHTS"></span><span id="error_ds_insuff_access_rights"></span>**ERROR\_DS\_INSUFF\_ACCESS\_RIGHTS**
</dt> <dd> <dl> <dt>

8344 (0x2098)
</dt> <dt>



Insufficient access rights to perform the operation.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_ILLEGAL_SUPERIOR"></span><span id="error_ds_illegal_superior"></span>**ERROR\_DS\_ILLEGAL\_SUPERIOR**
</dt> <dd> <dl> <dt>

8345 (0x2099)
</dt> <dt>



The object cannot be added because the parent is not on the list of possible superiors.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_ATTRIBUTE_OWNED_BY_SAM"></span><span id="error_ds_attribute_owned_by_sam"></span>**ERROR\_DS\_ATTRIBUTE\_OWNED\_BY\_SAM**
</dt> <dd> <dl> <dt>

8346 (0x209A)
</dt> <dt>



Access to the attribute is not permitted because the attribute is owned by the Security Accounts Manager (SAM).


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NAME_TOO_MANY_PARTS"></span><span id="error_ds_name_too_many_parts"></span>**ERROR\_DS\_NAME\_TOO\_MANY\_PARTS**
</dt> <dd> <dl> <dt>

8347 (0x209B)
</dt> <dt>



The name has too many parts.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NAME_TOO_LONG"></span><span id="error_ds_name_too_long"></span>**ERROR\_DS\_NAME\_TOO\_LONG**
</dt> <dd> <dl> <dt>

8348 (0x209C)
</dt> <dt>



The name is too long.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NAME_VALUE_TOO_LONG"></span><span id="error_ds_name_value_too_long"></span>**ERROR\_DS\_NAME\_VALUE\_TOO\_LONG**
</dt> <dd> <dl> <dt>

8349 (0x209D)
</dt> <dt>



The name value is too long.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NAME_UNPARSEABLE"></span><span id="error_ds_name_unparseable"></span>**ERROR\_DS\_NAME\_UNPARSEABLE**
</dt> <dd> <dl> <dt>

8350 (0x209E)
</dt> <dt>



The directory service encountered an error parsing a name.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NAME_TYPE_UNKNOWN"></span><span id="error_ds_name_type_unknown"></span>**ERROR\_DS\_NAME\_TYPE\_UNKNOWN**
</dt> <dd> <dl> <dt>

8351 (0x209F)
</dt> <dt>



The directory service cannot get the attribute type for a name.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NOT_AN_OBJECT"></span><span id="error_ds_not_an_object"></span>**ERROR\_DS\_NOT\_AN\_OBJECT**
</dt> <dd> <dl> <dt>

8352 (0x20A0)
</dt> <dt>



The name does not identify an object; the name identifies a phantom.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_SEC_DESC_TOO_SHORT"></span><span id="error_ds_sec_desc_too_short"></span>**ERROR\_DS\_SEC\_DESC\_TOO\_SHORT**
</dt> <dd> <dl> <dt>

8353 (0x20A1)
</dt> <dt>



The security descriptor is too short.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_SEC_DESC_INVALID"></span><span id="error_ds_sec_desc_invalid"></span>**ERROR\_DS\_SEC\_DESC\_INVALID**
</dt> <dd> <dl> <dt>

8354 (0x20A2)
</dt> <dt>



The security descriptor is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NO_DELETED_NAME"></span><span id="error_ds_no_deleted_name"></span>**ERROR\_DS\_NO\_DELETED\_NAME**
</dt> <dd> <dl> <dt>

8355 (0x20A3)
</dt> <dt>



Failed to create name for deleted object.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_SUBREF_MUST_HAVE_PARENT"></span><span id="error_ds_subref_must_have_parent"></span>**ERROR\_DS\_SUBREF\_MUST\_HAVE\_PARENT**
</dt> <dd> <dl> <dt>

8356 (0x20A4)
</dt> <dt>



The parent of a new subref must exist.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NCNAME_MUST_BE_NC"></span><span id="error_ds_ncname_must_be_nc"></span>**ERROR\_DS\_NCNAME\_MUST\_BE\_NC**
</dt> <dd> <dl> <dt>

8357 (0x20A5)
</dt> <dt>



The object must be a naming context.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CANT_ADD_SYSTEM_ONLY"></span><span id="error_ds_cant_add_system_only"></span>**ERROR\_DS\_CANT\_ADD\_SYSTEM\_ONLY**
</dt> <dd> <dl> <dt>

8358 (0x20A6)
</dt> <dt>



It is not permitted to add an attribute which is owned by the system.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CLASS_MUST_BE_CONCRETE"></span><span id="error_ds_class_must_be_concrete"></span>**ERROR\_DS\_CLASS\_MUST\_BE\_CONCRETE**
</dt> <dd> <dl> <dt>

8359 (0x20A7)
</dt> <dt>



The class of the object must be structural; you cannot instantiate an abstract class.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_INVALID_DMD"></span><span id="error_ds_invalid_dmd"></span>**ERROR\_DS\_INVALID\_DMD**
</dt> <dd> <dl> <dt>

8360 (0x20A8)
</dt> <dt>



The schema object could not be found.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_OBJ_GUID_EXISTS"></span><span id="error_ds_obj_guid_exists"></span>**ERROR\_DS\_OBJ\_GUID\_EXISTS**
</dt> <dd> <dl> <dt>

8361 (0x20A9)
</dt> <dt>



A local object with this GUID (dead or alive) already exists.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NOT_ON_BACKLINK"></span><span id="error_ds_not_on_backlink"></span>**ERROR\_DS\_NOT\_ON\_BACKLINK**
</dt> <dd> <dl> <dt>

8362 (0x20AA)
</dt> <dt>



The operation cannot be performed on a back link.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NO_CROSSREF_FOR_NC"></span><span id="error_ds_no_crossref_for_nc"></span>**ERROR\_DS\_NO\_CROSSREF\_FOR\_NC**
</dt> <dd> <dl> <dt>

8363 (0x20AB)
</dt> <dt>



The cross reference for the specified naming context could not be found.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_SHUTTING_DOWN"></span><span id="error_ds_shutting_down"></span>**ERROR\_DS\_SHUTTING\_DOWN**
</dt> <dd> <dl> <dt>

8364 (0x20AC)
</dt> <dt>



The operation could not be performed because the directory service is shutting down.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_UNKNOWN_OPERATION"></span><span id="error_ds_unknown_operation"></span>**ERROR\_DS\_UNKNOWN\_OPERATION**
</dt> <dd> <dl> <dt>

8365 (0x20AD)
</dt> <dt>



The directory service request is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_INVALID_ROLE_OWNER"></span><span id="error_ds_invalid_role_owner"></span>**ERROR\_DS\_INVALID\_ROLE\_OWNER**
</dt> <dd> <dl> <dt>

8366 (0x20AE)
</dt> <dt>



The role owner attribute could not be read.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_COULDNT_CONTACT_FSMO"></span><span id="error_ds_couldnt_contact_fsmo"></span>**ERROR\_DS\_COULDNT\_CONTACT\_FSMO**
</dt> <dd> <dl> <dt>

8367 (0x20AF)
</dt> <dt>



The requested FSMO operation failed. The current FSMO holder could not be contacted.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CROSS_NC_DN_RENAME"></span><span id="error_ds_cross_nc_dn_rename"></span>**ERROR\_DS\_CROSS\_NC\_DN\_RENAME**
</dt> <dd> <dl> <dt>

8368 (0x20B0)
</dt> <dt>



Modification of a DN across a naming context is not permitted.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CANT_MOD_SYSTEM_ONLY"></span><span id="error_ds_cant_mod_system_only"></span>**ERROR\_DS\_CANT\_MOD\_SYSTEM\_ONLY**
</dt> <dd> <dl> <dt>

8369 (0x20B1)
</dt> <dt>



The attribute cannot be modified because it is owned by the system.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_REPLICATOR_ONLY"></span><span id="error_ds_replicator_only"></span>**ERROR\_DS\_REPLICATOR\_ONLY**
</dt> <dd> <dl> <dt>

8370 (0x20B2)
</dt> <dt>



Only the replicator can perform this function.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_OBJ_CLASS_NOT_DEFINED"></span><span id="error_ds_obj_class_not_defined"></span>**ERROR\_DS\_OBJ\_CLASS\_NOT\_DEFINED**
</dt> <dd> <dl> <dt>

8371 (0x20B3)
</dt> <dt>



The specified class is not defined.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_OBJ_CLASS_NOT_SUBCLASS"></span><span id="error_ds_obj_class_not_subclass"></span>**ERROR\_DS\_OBJ\_CLASS\_NOT\_SUBCLASS**
</dt> <dd> <dl> <dt>

8372 (0x20B4)
</dt> <dt>



The specified class is not a subclass.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NAME_REFERENCE_INVALID"></span><span id="error_ds_name_reference_invalid"></span>**ERROR\_DS\_NAME\_REFERENCE\_INVALID**
</dt> <dd> <dl> <dt>

8373 (0x20B5)
</dt> <dt>



The name reference is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CROSS_REF_EXISTS"></span><span id="error_ds_cross_ref_exists"></span>**ERROR\_DS\_CROSS\_REF\_EXISTS**
</dt> <dd> <dl> <dt>

8374 (0x20B6)
</dt> <dt>



A cross reference already exists.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CANT_DEL_MASTER_CROSSREF"></span><span id="error_ds_cant_del_master_crossref"></span>**ERROR\_DS\_CANT\_DEL\_MASTER\_CROSSREF**
</dt> <dd> <dl> <dt>

8375 (0x20B7)
</dt> <dt>



It is not permitted to delete a master cross reference.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_SUBTREE_NOTIFY_NOT_NC_HEAD"></span><span id="error_ds_subtree_notify_not_nc_head"></span>**ERROR\_DS\_SUBTREE\_NOTIFY\_NOT\_NC\_HEAD**
</dt> <dd> <dl> <dt>

8376 (0x20B8)
</dt> <dt>



Subtree notifications are only supported on NC heads.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NOTIFY_FILTER_TOO_COMPLEX"></span><span id="error_ds_notify_filter_too_complex"></span>**ERROR\_DS\_NOTIFY\_FILTER\_TOO\_COMPLEX**
</dt> <dd> <dl> <dt>

8377 (0x20B9)
</dt> <dt>



Notification filter is too complex.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DUP_RDN"></span><span id="error_ds_dup_rdn"></span>**ERROR\_DS\_DUP\_RDN**
</dt> <dd> <dl> <dt>

8378 (0x20BA)
</dt> <dt>



Schema update failed: duplicate RDN.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DUP_OID"></span><span id="error_ds_dup_oid"></span>**ERROR\_DS\_DUP\_OID**
</dt> <dd> <dl> <dt>

8379 (0x20BB)
</dt> <dt>



Schema update failed: duplicate OID.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DUP_MAPI_ID"></span><span id="error_ds_dup_mapi_id"></span>**ERROR\_DS\_DUP\_MAPI\_ID**
</dt> <dd> <dl> <dt>

8380 (0x20BC)
</dt> <dt>



Schema update failed: duplicate MAPI identifier.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DUP_SCHEMA_ID_GUID"></span><span id="error_ds_dup_schema_id_guid"></span>**ERROR\_DS\_DUP\_SCHEMA\_ID\_GUID**
</dt> <dd> <dl> <dt>

8381 (0x20BD)
</dt> <dt>



Schema update failed: duplicate schema-id GUID.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DUP_LDAP_DISPLAY_NAME"></span><span id="error_ds_dup_ldap_display_name"></span>**ERROR\_DS\_DUP\_LDAP\_DISPLAY\_NAME**
</dt> <dd> <dl> <dt>

8382 (0x20BE)
</dt> <dt>



Schema update failed: duplicate LDAP display name.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_SEMANTIC_ATT_TEST"></span><span id="error_ds_semantic_att_test"></span>**ERROR\_DS\_SEMANTIC\_ATT\_TEST**
</dt> <dd> <dl> <dt>

8383 (0x20BF)
</dt> <dt>



Schema update failed: range-lower less than range upper.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_SYNTAX_MISMATCH"></span><span id="error_ds_syntax_mismatch"></span>**ERROR\_DS\_SYNTAX\_MISMATCH**
</dt> <dd> <dl> <dt>

8384 (0x20C0)
</dt> <dt>



Schema update failed: syntax mismatch.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_EXISTS_IN_MUST_HAVE"></span><span id="error_ds_exists_in_must_have"></span>**ERROR\_DS\_EXISTS\_IN\_MUST\_HAVE**
</dt> <dd> <dl> <dt>

8385 (0x20C1)
</dt> <dt>



Schema deletion failed: attribute is used in must-contain.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_EXISTS_IN_MAY_HAVE"></span><span id="error_ds_exists_in_may_have"></span>**ERROR\_DS\_EXISTS\_IN\_MAY\_HAVE**
</dt> <dd> <dl> <dt>

8386 (0x20C2)
</dt> <dt>



Schema deletion failed: attribute is used in may-contain.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NONEXISTENT_MAY_HAVE"></span><span id="error_ds_nonexistent_may_have"></span>**ERROR\_DS\_NONEXISTENT\_MAY\_HAVE**
</dt> <dd> <dl> <dt>

8387 (0x20C3)
</dt> <dt>



Schema update failed: attribute in may-contain does not exist.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NONEXISTENT_MUST_HAVE"></span><span id="error_ds_nonexistent_must_have"></span>**ERROR\_DS\_NONEXISTENT\_MUST\_HAVE**
</dt> <dd> <dl> <dt>

8388 (0x20C4)
</dt> <dt>



Schema update failed: attribute in must-contain does not exist.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_AUX_CLS_TEST_FAIL"></span><span id="error_ds_aux_cls_test_fail"></span>**ERROR\_DS\_AUX\_CLS\_TEST\_FAIL**
</dt> <dd> <dl> <dt>

8389 (0x20C5)
</dt> <dt>



Schema update failed: class in aux-class list does not exist or is not an auxiliary class.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NONEXISTENT_POSS_SUP"></span><span id="error_ds_nonexistent_poss_sup"></span>**ERROR\_DS\_NONEXISTENT\_POSS\_SUP**
</dt> <dd> <dl> <dt>

8390 (0x20C6)
</dt> <dt>



Schema update failed: class in poss-superiors does not exist.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_SUB_CLS_TEST_FAIL"></span><span id="error_ds_sub_cls_test_fail"></span>**ERROR\_DS\_SUB\_CLS\_TEST\_FAIL**
</dt> <dd> <dl> <dt>

8391 (0x20C7)
</dt> <dt>



Schema update failed: class in subclassof list does not exist or does not satisfy hierarchy rules.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_BAD_RDN_ATT_ID_SYNTAX"></span><span id="error_ds_bad_rdn_att_id_syntax"></span>**ERROR\_DS\_BAD\_RDN\_ATT\_ID\_SYNTAX**
</dt> <dd> <dl> <dt>

8392 (0x20C8)
</dt> <dt>



Schema update failed: Rdn-Att-Id has wrong syntax.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_EXISTS_IN_AUX_CLS"></span><span id="error_ds_exists_in_aux_cls"></span>**ERROR\_DS\_EXISTS\_IN\_AUX\_CLS**
</dt> <dd> <dl> <dt>

8393 (0x20C9)
</dt> <dt>



Schema deletion failed: class is used as auxiliary class.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_EXISTS_IN_SUB_CLS"></span><span id="error_ds_exists_in_sub_cls"></span>**ERROR\_DS\_EXISTS\_IN\_SUB\_CLS**
</dt> <dd> <dl> <dt>

8394 (0x20CA)
</dt> <dt>



Schema deletion failed: class is used as sub class.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_EXISTS_IN_POSS_SUP"></span><span id="error_ds_exists_in_poss_sup"></span>**ERROR\_DS\_EXISTS\_IN\_POSS\_SUP**
</dt> <dd> <dl> <dt>

8395 (0x20CB)
</dt> <dt>



Schema deletion failed: class is used as poss superior.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_RECALCSCHEMA_FAILED"></span><span id="error_ds_recalcschema_failed"></span>**ERROR\_DS\_RECALCSCHEMA\_FAILED**
</dt> <dd> <dl> <dt>

8396 (0x20CC)
</dt> <dt>



Schema update failed in recalculating validation cache.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_TREE_DELETE_NOT_FINISHED"></span><span id="error_ds_tree_delete_not_finished"></span>**ERROR\_DS\_TREE\_DELETE\_NOT\_FINISHED**
</dt> <dd> <dl> <dt>

8397 (0x20CD)
</dt> <dt>



The tree deletion is not finished. The request must be made again to continue deleting the tree.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CANT_DELETE"></span><span id="error_ds_cant_delete"></span>**ERROR\_DS\_CANT\_DELETE**
</dt> <dd> <dl> <dt>

8398 (0x20CE)
</dt> <dt>



The requested delete operation could not be performed.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_ATT_SCHEMA_REQ_ID"></span><span id="error_ds_att_schema_req_id"></span>**ERROR\_DS\_ATT\_SCHEMA\_REQ\_ID**
</dt> <dd> <dl> <dt>

8399 (0x20CF)
</dt> <dt>



Cannot read the governs class identifier for the schema record.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_BAD_ATT_SCHEMA_SYNTAX"></span><span id="error_ds_bad_att_schema_syntax"></span>**ERROR\_DS\_BAD\_ATT\_SCHEMA\_SYNTAX**
</dt> <dd> <dl> <dt>

8400 (0x20D0)
</dt> <dt>



The attribute schema has bad syntax.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CANT_CACHE_ATT"></span><span id="error_ds_cant_cache_att"></span>**ERROR\_DS\_CANT\_CACHE\_ATT**
</dt> <dd> <dl> <dt>

8401 (0x20D1)
</dt> <dt>



The attribute could not be cached.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CANT_CACHE_CLASS"></span><span id="error_ds_cant_cache_class"></span>**ERROR\_DS\_CANT\_CACHE\_CLASS**
</dt> <dd> <dl> <dt>

8402 (0x20D2)
</dt> <dt>



The class could not be cached.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CANT_REMOVE_ATT_CACHE"></span><span id="error_ds_cant_remove_att_cache"></span>**ERROR\_DS\_CANT\_REMOVE\_ATT\_CACHE**
</dt> <dd> <dl> <dt>

8403 (0x20D3)
</dt> <dt>



The attribute could not be removed from the cache.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CANT_REMOVE_CLASS_CACHE"></span><span id="error_ds_cant_remove_class_cache"></span>**ERROR\_DS\_CANT\_REMOVE\_CLASS\_CACHE**
</dt> <dd> <dl> <dt>

8404 (0x20D4)
</dt> <dt>



The class could not be removed from the cache.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CANT_RETRIEVE_DN"></span><span id="error_ds_cant_retrieve_dn"></span>**ERROR\_DS\_CANT\_RETRIEVE\_DN**
</dt> <dd> <dl> <dt>

8405 (0x20D5)
</dt> <dt>



The distinguished name attribute could not be read.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_MISSING_SUPREF"></span><span id="error_ds_missing_supref"></span>**ERROR\_DS\_MISSING\_SUPREF**
</dt> <dd> <dl> <dt>

8406 (0x20D6)
</dt> <dt>



No superior reference has been configured for the directory service. The directory service is therefore unable to issue referrals to objects outside this forest.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CANT_RETRIEVE_INSTANCE"></span><span id="error_ds_cant_retrieve_instance"></span>**ERROR\_DS\_CANT\_RETRIEVE\_INSTANCE**
</dt> <dd> <dl> <dt>

8407 (0x20D7)
</dt> <dt>



The instance type attribute could not be retrieved.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CODE_INCONSISTENCY"></span><span id="error_ds_code_inconsistency"></span>**ERROR\_DS\_CODE\_INCONSISTENCY**
</dt> <dd> <dl> <dt>

8408 (0x20D8)
</dt> <dt>



An internal error has occurred.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DATABASE_ERROR"></span><span id="error_ds_database_error"></span>**ERROR\_DS\_DATABASE\_ERROR**
</dt> <dd> <dl> <dt>

8409 (0x20D9)
</dt> <dt>



A database error has occurred.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_GOVERNSID_MISSING"></span><span id="error_ds_governsid_missing"></span>**ERROR\_DS\_GOVERNSID\_MISSING**
</dt> <dd> <dl> <dt>

8410 (0x20DA)
</dt> <dt>



The attribute GOVERNSID is missing.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_MISSING_EXPECTED_ATT"></span><span id="error_ds_missing_expected_att"></span>**ERROR\_DS\_MISSING\_EXPECTED\_ATT**
</dt> <dd> <dl> <dt>

8411 (0x20DB)
</dt> <dt>



An expected attribute is missing.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NCNAME_MISSING_CR_REF"></span><span id="error_ds_ncname_missing_cr_ref"></span>**ERROR\_DS\_NCNAME\_MISSING\_CR\_REF**
</dt> <dd> <dl> <dt>

8412 (0x20DC)
</dt> <dt>



The specified naming context is missing a cross reference.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_SECURITY_CHECKING_ERROR"></span><span id="error_ds_security_checking_error"></span>**ERROR\_DS\_SECURITY\_CHECKING\_ERROR**
</dt> <dd> <dl> <dt>

8413 (0x20DD)
</dt> <dt>



A security checking error has occurred.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_SCHEMA_NOT_LOADED"></span><span id="error_ds_schema_not_loaded"></span>**ERROR\_DS\_SCHEMA\_NOT\_LOADED**
</dt> <dd> <dl> <dt>

8414 (0x20DE)
</dt> <dt>



The schema is not loaded.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_SCHEMA_ALLOC_FAILED"></span><span id="error_ds_schema_alloc_failed"></span>**ERROR\_DS\_SCHEMA\_ALLOC\_FAILED**
</dt> <dd> <dl> <dt>

8415 (0x20DF)
</dt> <dt>



Schema allocation failed. Please check if the machine is running low on memory.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_ATT_SCHEMA_REQ_SYNTAX"></span><span id="error_ds_att_schema_req_syntax"></span>**ERROR\_DS\_ATT\_SCHEMA\_REQ\_SYNTAX**
</dt> <dd> <dl> <dt>

8416 (0x20E0)
</dt> <dt>



Failed to obtain the required syntax for the attribute schema.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_GCVERIFY_ERROR"></span><span id="error_ds_gcverify_error"></span>**ERROR\_DS\_GCVERIFY\_ERROR**
</dt> <dd> <dl> <dt>

8417 (0x20E1)
</dt> <dt>



The global catalog verification failed. The global catalog is not available or does not support the operation. Some part of the directory is currently not available.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DRA_SCHEMA_MISMATCH"></span><span id="error_ds_dra_schema_mismatch"></span>**ERROR\_DS\_DRA\_SCHEMA\_MISMATCH**
</dt> <dd> <dl> <dt>

8418 (0x20E2)
</dt> <dt>



The replication operation failed because of a schema mismatch between the servers involved.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CANT_FIND_DSA_OBJ"></span><span id="error_ds_cant_find_dsa_obj"></span>**ERROR\_DS\_CANT\_FIND\_DSA\_OBJ**
</dt> <dd> <dl> <dt>

8419 (0x20E3)
</dt> <dt>



The DSA object could not be found.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CANT_FIND_EXPECTED_NC"></span><span id="error_ds_cant_find_expected_nc"></span>**ERROR\_DS\_CANT\_FIND\_EXPECTED\_NC**
</dt> <dd> <dl> <dt>

8420 (0x20E4)
</dt> <dt>



The naming context could not be found.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CANT_FIND_NC_IN_CACHE"></span><span id="error_ds_cant_find_nc_in_cache"></span>**ERROR\_DS\_CANT\_FIND\_NC\_IN\_CACHE**
</dt> <dd> <dl> <dt>

8421 (0x20E5)
</dt> <dt>



The naming context could not be found in the cache.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CANT_RETRIEVE_CHILD"></span><span id="error_ds_cant_retrieve_child"></span>**ERROR\_DS\_CANT\_RETRIEVE\_CHILD**
</dt> <dd> <dl> <dt>

8422 (0x20E6)
</dt> <dt>



The child object could not be retrieved.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_SECURITY_ILLEGAL_MODIFY"></span><span id="error_ds_security_illegal_modify"></span>**ERROR\_DS\_SECURITY\_ILLEGAL\_MODIFY**
</dt> <dd> <dl> <dt>

8423 (0x20E7)
</dt> <dt>



The modification was not permitted for security reasons.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CANT_REPLACE_HIDDEN_REC"></span><span id="error_ds_cant_replace_hidden_rec"></span>**ERROR\_DS\_CANT\_REPLACE\_HIDDEN\_REC**
</dt> <dd> <dl> <dt>

8424 (0x20E8)
</dt> <dt>



The operation cannot replace the hidden record.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_BAD_HIERARCHY_FILE"></span><span id="error_ds_bad_hierarchy_file"></span>**ERROR\_DS\_BAD\_HIERARCHY\_FILE**
</dt> <dd> <dl> <dt>

8425 (0x20E9)
</dt> <dt>



The hierarchy file is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_BUILD_HIERARCHY_TABLE_FAILED"></span><span id="error_ds_build_hierarchy_table_failed"></span>**ERROR\_DS\_BUILD\_HIERARCHY\_TABLE\_FAILED**
</dt> <dd> <dl> <dt>

8426 (0x20EA)
</dt> <dt>



The attempt to build the hierarchy table failed.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CONFIG_PARAM_MISSING"></span><span id="error_ds_config_param_missing"></span>**ERROR\_DS\_CONFIG\_PARAM\_MISSING**
</dt> <dd> <dl> <dt>

8427 (0x20EB)
</dt> <dt>



The directory configuration parameter is missing from the registry.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_COUNTING_AB_INDICES_FAILED"></span><span id="error_ds_counting_ab_indices_failed"></span>**ERROR\_DS\_COUNTING\_AB\_INDICES\_FAILED**
</dt> <dd> <dl> <dt>

8428 (0x20EC)
</dt> <dt>



The attempt to count the address book indices failed.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_HIERARCHY_TABLE_MALLOC_FAILED"></span><span id="error_ds_hierarchy_table_malloc_failed"></span>**ERROR\_DS\_HIERARCHY\_TABLE\_MALLOC\_FAILED**
</dt> <dd> <dl> <dt>

8429 (0x20ED)
</dt> <dt>



The allocation of the hierarchy table failed.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_INTERNAL_FAILURE"></span><span id="error_ds_internal_failure"></span>**ERROR\_DS\_INTERNAL\_FAILURE**
</dt> <dd> <dl> <dt>

8430 (0x20EE)
</dt> <dt>



The directory service encountered an internal failure.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_UNKNOWN_ERROR"></span><span id="error_ds_unknown_error"></span>**ERROR\_DS\_UNKNOWN\_ERROR**
</dt> <dd> <dl> <dt>

8431 (0x20EF)
</dt> <dt>



The directory service encountered an unknown failure.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_ROOT_REQUIRES_CLASS_TOP"></span><span id="error_ds_root_requires_class_top"></span>**ERROR\_DS\_ROOT\_REQUIRES\_CLASS\_TOP**
</dt> <dd> <dl> <dt>

8432 (0x20F0)
</dt> <dt>



A root object requires a class of 'top'.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_REFUSING_FSMO_ROLES"></span><span id="error_ds_refusing_fsmo_roles"></span>**ERROR\_DS\_REFUSING\_FSMO\_ROLES**
</dt> <dd> <dl> <dt>

8433 (0x20F1)
</dt> <dt>



This directory server is shutting down, and cannot take ownership of new floating single-master operation roles.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_MISSING_FSMO_SETTINGS"></span><span id="error_ds_missing_fsmo_settings"></span>**ERROR\_DS\_MISSING\_FSMO\_SETTINGS**
</dt> <dd> <dl> <dt>

8434 (0x20F2)
</dt> <dt>



The directory service is missing mandatory configuration information, and is unable to determine the ownership of floating single-master operation roles.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_UNABLE_TO_SURRENDER_ROLES"></span><span id="error_ds_unable_to_surrender_roles"></span>**ERROR\_DS\_UNABLE\_TO\_SURRENDER\_ROLES**
</dt> <dd> <dl> <dt>

8435 (0x20F3)
</dt> <dt>



The directory service was unable to transfer ownership of one or more floating single-master operation roles to other servers.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DRA_GENERIC"></span><span id="error_ds_dra_generic"></span>**ERROR\_DS\_DRA\_GENERIC**
</dt> <dd> <dl> <dt>

8436 (0x20F4)
</dt> <dt>



The replication operation failed.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DRA_INVALID_PARAMETER"></span><span id="error_ds_dra_invalid_parameter"></span>**ERROR\_DS\_DRA\_INVALID\_PARAMETER**
</dt> <dd> <dl> <dt>

8437 (0x20F5)
</dt> <dt>



An invalid parameter was specified for this replication operation.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DRA_BUSY"></span><span id="error_ds_dra_busy"></span>**ERROR\_DS\_DRA\_BUSY**
</dt> <dd> <dl> <dt>

8438 (0x20F6)
</dt> <dt>



The directory service is too busy to complete the replication operation at this time.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DRA_BAD_DN"></span><span id="error_ds_dra_bad_dn"></span>**ERROR\_DS\_DRA\_BAD\_DN**
</dt> <dd> <dl> <dt>

8439 (0x20F7)
</dt> <dt>



The distinguished name specified for this replication operation is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DRA_BAD_NC"></span><span id="error_ds_dra_bad_nc"></span>**ERROR\_DS\_DRA\_BAD\_NC**
</dt> <dd> <dl> <dt>

8440 (0x20F8)
</dt> <dt>



The naming context specified for this replication operation is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DRA_DN_EXISTS"></span><span id="error_ds_dra_dn_exists"></span>**ERROR\_DS\_DRA\_DN\_EXISTS**
</dt> <dd> <dl> <dt>

8441 (0x20F9)
</dt> <dt>



The distinguished name specified for this replication operation already exists.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DRA_INTERNAL_ERROR"></span><span id="error_ds_dra_internal_error"></span>**ERROR\_DS\_DRA\_INTERNAL\_ERROR**
</dt> <dd> <dl> <dt>

8442 (0x20FA)
</dt> <dt>



The replication system encountered an internal error.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DRA_INCONSISTENT_DIT"></span><span id="error_ds_dra_inconsistent_dit"></span>**ERROR\_DS\_DRA\_INCONSISTENT\_DIT**
</dt> <dd> <dl> <dt>

8443 (0x20FB)
</dt> <dt>



The replication operation encountered a database inconsistency.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DRA_CONNECTION_FAILED"></span><span id="error_ds_dra_connection_failed"></span>**ERROR\_DS\_DRA\_CONNECTION\_FAILED**
</dt> <dd> <dl> <dt>

8444 (0x20FC)
</dt> <dt>



The server specified for this replication operation could not be contacted.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DRA_BAD_INSTANCE_TYPE"></span><span id="error_ds_dra_bad_instance_type"></span>**ERROR\_DS\_DRA\_BAD\_INSTANCE\_TYPE**
</dt> <dd> <dl> <dt>

8445 (0x20FD)
</dt> <dt>



The replication operation encountered an object with an invalid instance type.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DRA_OUT_OF_MEM"></span><span id="error_ds_dra_out_of_mem"></span>**ERROR\_DS\_DRA\_OUT\_OF\_MEM**
</dt> <dd> <dl> <dt>

8446 (0x20FE)
</dt> <dt>



The replication operation failed to allocate memory.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DRA_MAIL_PROBLEM"></span><span id="error_ds_dra_mail_problem"></span>**ERROR\_DS\_DRA\_MAIL\_PROBLEM**
</dt> <dd> <dl> <dt>

8447 (0x20FF)
</dt> <dt>



The replication operation encountered an error with the mail system.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DRA_REF_ALREADY_EXISTS"></span><span id="error_ds_dra_ref_already_exists"></span>**ERROR\_DS\_DRA\_REF\_ALREADY\_EXISTS**
</dt> <dd> <dl> <dt>

8448 (0x2100)
</dt> <dt>



The replication reference information for the target server already exists.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DRA_REF_NOT_FOUND"></span><span id="error_ds_dra_ref_not_found"></span>**ERROR\_DS\_DRA\_REF\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

8449 (0x2101)
</dt> <dt>



The replication reference information for the target server does not exist.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DRA_OBJ_IS_REP_SOURCE"></span><span id="error_ds_dra_obj_is_rep_source"></span>**ERROR\_DS\_DRA\_OBJ\_IS\_REP\_SOURCE**
</dt> <dd> <dl> <dt>

8450 (0x2102)
</dt> <dt>



The naming context cannot be removed because it is replicated to another server.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DRA_DB_ERROR"></span><span id="error_ds_dra_db_error"></span>**ERROR\_DS\_DRA\_DB\_ERROR**
</dt> <dd> <dl> <dt>

8451 (0x2103)
</dt> <dt>



The replication operation encountered a database error.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DRA_NO_REPLICA"></span><span id="error_ds_dra_no_replica"></span>**ERROR\_DS\_DRA\_NO\_REPLICA**
</dt> <dd> <dl> <dt>

8452 (0x2104)
</dt> <dt>



The naming context is in the process of being removed or is not replicated from the specified server.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DRA_ACCESS_DENIED"></span><span id="error_ds_dra_access_denied"></span>**ERROR\_DS\_DRA\_ACCESS\_DENIED**
</dt> <dd> <dl> <dt>

8453 (0x2105)
</dt> <dt>



Replication access was denied.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DRA_NOT_SUPPORTED"></span><span id="error_ds_dra_not_supported"></span>**ERROR\_DS\_DRA\_NOT\_SUPPORTED**
</dt> <dd> <dl> <dt>

8454 (0x2106)
</dt> <dt>



The requested operation is not supported by this version of the directory service.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DRA_RPC_CANCELLED"></span><span id="error_ds_dra_rpc_cancelled"></span>**ERROR\_DS\_DRA\_RPC\_CANCELLED**
</dt> <dd> <dl> <dt>

8455 (0x2107)
</dt> <dt>



The replication remote procedure call was cancelled.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DRA_SOURCE_DISABLED"></span><span id="error_ds_dra_source_disabled"></span>**ERROR\_DS\_DRA\_SOURCE\_DISABLED**
</dt> <dd> <dl> <dt>

8456 (0x2108)
</dt> <dt>



The source server is currently rejecting replication requests.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DRA_SINK_DISABLED"></span><span id="error_ds_dra_sink_disabled"></span>**ERROR\_DS\_DRA\_SINK\_DISABLED**
</dt> <dd> <dl> <dt>

8457 (0x2109)
</dt> <dt>



The destination server is currently rejecting replication requests.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DRA_NAME_COLLISION"></span><span id="error_ds_dra_name_collision"></span>**ERROR\_DS\_DRA\_NAME\_COLLISION**
</dt> <dd> <dl> <dt>

8458 (0x210A)
</dt> <dt>



The replication operation failed due to a collision of object names.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DRA_SOURCE_REINSTALLED"></span><span id="error_ds_dra_source_reinstalled"></span>**ERROR\_DS\_DRA\_SOURCE\_REINSTALLED**
</dt> <dd> <dl> <dt>

8459 (0x210B)
</dt> <dt>



The replication source has been reinstalled.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DRA_MISSING_PARENT"></span><span id="error_ds_dra_missing_parent"></span>**ERROR\_DS\_DRA\_MISSING\_PARENT**
</dt> <dd> <dl> <dt>

8460 (0x210C)
</dt> <dt>



The replication operation failed because a required parent object is missing.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DRA_PREEMPTED"></span><span id="error_ds_dra_preempted"></span>**ERROR\_DS\_DRA\_PREEMPTED**
</dt> <dd> <dl> <dt>

8461 (0x210D)
</dt> <dt>



The replication operation was preempted.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DRA_ABANDON_SYNC"></span><span id="error_ds_dra_abandon_sync"></span>**ERROR\_DS\_DRA\_ABANDON\_SYNC**
</dt> <dd> <dl> <dt>

8462 (0x210E)
</dt> <dt>



The replication synchronization attempt was abandoned because of a lack of updates.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DRA_SHUTDOWN"></span><span id="error_ds_dra_shutdown"></span>**ERROR\_DS\_DRA\_SHUTDOWN**
</dt> <dd> <dl> <dt>

8463 (0x210F)
</dt> <dt>



The replication operation was terminated because the system is shutting down.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DRA_INCOMPATIBLE_PARTIAL_SET"></span><span id="error_ds_dra_incompatible_partial_set"></span>**ERROR\_DS\_DRA\_INCOMPATIBLE\_PARTIAL\_SET**
</dt> <dd> <dl> <dt>

8464 (0x2110)
</dt> <dt>



Synchronization attempt failed because the destination DC is currently waiting to synchronize new partial attributes from source. This condition is normal if a recent schema change modified the partial attribute set. The destination partial attribute set is not a subset of source partial attribute set.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DRA_SOURCE_IS_PARTIAL_REPLICA"></span><span id="error_ds_dra_source_is_partial_replica"></span>**ERROR\_DS\_DRA\_SOURCE\_IS\_PARTIAL\_REPLICA**
</dt> <dd> <dl> <dt>

8465 (0x2111)
</dt> <dt>



The replication synchronization attempt failed because a master replica attempted to sync from a partial replica.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DRA_EXTN_CONNECTION_FAILED"></span><span id="error_ds_dra_extn_connection_failed"></span>**ERROR\_DS\_DRA\_EXTN\_CONNECTION\_FAILED**
</dt> <dd> <dl> <dt>

8466 (0x2112)
</dt> <dt>



The server specified for this replication operation was contacted, but that server was unable to contact an additional server needed to complete the operation.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_INSTALL_SCHEMA_MISMATCH"></span><span id="error_ds_install_schema_mismatch"></span>**ERROR\_DS\_INSTALL\_SCHEMA\_MISMATCH**
</dt> <dd> <dl> <dt>

8467 (0x2113)
</dt> <dt>



The version of the directory service schema of the source forest is not compatible with the version of directory service on this computer.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DUP_LINK_ID"></span><span id="error_ds_dup_link_id"></span>**ERROR\_DS\_DUP\_LINK\_ID**
</dt> <dd> <dl> <dt>

8468 (0x2114)
</dt> <dt>



Schema update failed: An attribute with the same link identifier already exists.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NAME_ERROR_RESOLVING"></span><span id="error_ds_name_error_resolving"></span>**ERROR\_DS\_NAME\_ERROR\_RESOLVING**
</dt> <dd> <dl> <dt>

8469 (0x2115)
</dt> <dt>



Name translation: Generic processing error.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NAME_ERROR_NOT_FOUND"></span><span id="error_ds_name_error_not_found"></span>**ERROR\_DS\_NAME\_ERROR\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

8470 (0x2116)
</dt> <dt>



Name translation: Could not find the name or insufficient right to see name.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NAME_ERROR_NOT_UNIQUE"></span><span id="error_ds_name_error_not_unique"></span>**ERROR\_DS\_NAME\_ERROR\_NOT\_UNIQUE**
</dt> <dd> <dl> <dt>

8471 (0x2117)
</dt> <dt>



Name translation: Input name mapped to more than one output name.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NAME_ERROR_NO_MAPPING"></span><span id="error_ds_name_error_no_mapping"></span>**ERROR\_DS\_NAME\_ERROR\_NO\_MAPPING**
</dt> <dd> <dl> <dt>

8472 (0x2118)
</dt> <dt>



Name translation: Input name found, but not the associated output format.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NAME_ERROR_DOMAIN_ONLY"></span><span id="error_ds_name_error_domain_only"></span>**ERROR\_DS\_NAME\_ERROR\_DOMAIN\_ONLY**
</dt> <dd> <dl> <dt>

8473 (0x2119)
</dt> <dt>



Name translation: Unable to resolve completely, only the domain was found.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NAME_ERROR_NO_SYNTACTICAL_MAPPING"></span><span id="error_ds_name_error_no_syntactical_mapping"></span>**ERROR\_DS\_NAME\_ERROR\_NO\_SYNTACTICAL\_MAPPING**
</dt> <dd> <dl> <dt>

8474 (0x211A)
</dt> <dt>



Name translation: Unable to perform purely syntactical mapping at the client without going out to the wire.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CONSTRUCTED_ATT_MOD"></span><span id="error_ds_constructed_att_mod"></span>**ERROR\_DS\_CONSTRUCTED\_ATT\_MOD**
</dt> <dd> <dl> <dt>

8475 (0x211B)
</dt> <dt>



Modification of a constructed attribute is not allowed.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_WRONG_OM_OBJ_CLASS"></span><span id="error_ds_wrong_om_obj_class"></span>**ERROR\_DS\_WRONG\_OM\_OBJ\_CLASS**
</dt> <dd> <dl> <dt>

8476 (0x211C)
</dt> <dt>



The OM-Object-Class specified is incorrect for an attribute with the specified syntax.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DRA_REPL_PENDING"></span><span id="error_ds_dra_repl_pending"></span>**ERROR\_DS\_DRA\_REPL\_PENDING**
</dt> <dd> <dl> <dt>

8477 (0x211D)
</dt> <dt>



The replication request has been posted; waiting for reply.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DS_REQUIRED"></span><span id="error_ds_ds_required"></span>**ERROR\_DS\_DS\_REQUIRED**
</dt> <dd> <dl> <dt>

8478 (0x211E)
</dt> <dt>



The requested operation requires a directory service, and none was available.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_INVALID_LDAP_DISPLAY_NAME"></span><span id="error_ds_invalid_ldap_display_name"></span>**ERROR\_DS\_INVALID\_LDAP\_DISPLAY\_NAME**
</dt> <dd> <dl> <dt>

8479 (0x211F)
</dt> <dt>



The LDAP display name of the class or attribute contains non-ASCII characters.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NON_BASE_SEARCH"></span><span id="error_ds_non_base_search"></span>**ERROR\_DS\_NON\_BASE\_SEARCH**
</dt> <dd> <dl> <dt>

8480 (0x2120)
</dt> <dt>



The requested search operation is only supported for base searches.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CANT_RETRIEVE_ATTS"></span><span id="error_ds_cant_retrieve_atts"></span>**ERROR\_DS\_CANT\_RETRIEVE\_ATTS**
</dt> <dd> <dl> <dt>

8481 (0x2121)
</dt> <dt>



The search failed to retrieve attributes from the database.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_BACKLINK_WITHOUT_LINK"></span><span id="error_ds_backlink_without_link"></span>**ERROR\_DS\_BACKLINK\_WITHOUT\_LINK**
</dt> <dd> <dl> <dt>

8482 (0x2122)
</dt> <dt>



The schema update operation tried to add a backward link attribute that has no corresponding forward link.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_EPOCH_MISMATCH"></span><span id="error_ds_epoch_mismatch"></span>**ERROR\_DS\_EPOCH\_MISMATCH**
</dt> <dd> <dl> <dt>

8483 (0x2123)
</dt> <dt>



Source and destination of a cross-domain move do not agree on the object's epoch number. Either source or destination does not have the latest version of the object.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_SRC_NAME_MISMATCH"></span><span id="error_ds_src_name_mismatch"></span>**ERROR\_DS\_SRC\_NAME\_MISMATCH**
</dt> <dd> <dl> <dt>

8484 (0x2124)
</dt> <dt>



Source and destination of a cross-domain move do not agree on the object's current name. Either source or destination does not have the latest version of the object.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_SRC_AND_DST_NC_IDENTICAL"></span><span id="error_ds_src_and_dst_nc_identical"></span>**ERROR\_DS\_SRC\_AND\_DST\_NC\_IDENTICAL**
</dt> <dd> <dl> <dt>

8485 (0x2125)
</dt> <dt>



Source and destination for the cross-domain move operation are identical. Caller should use local move operation instead of cross-domain move operation.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DST_NC_MISMATCH"></span><span id="error_ds_dst_nc_mismatch"></span>**ERROR\_DS\_DST\_NC\_MISMATCH**
</dt> <dd> <dl> <dt>

8486 (0x2126)
</dt> <dt>



Source and destination for a cross-domain move are not in agreement on the naming contexts in the forest. Either source or destination does not have the latest version of the Partitions container.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NOT_AUTHORITIVE_FOR_DST_NC"></span><span id="error_ds_not_authoritive_for_dst_nc"></span>**ERROR\_DS\_NOT\_AUTHORITIVE\_FOR\_DST\_NC**
</dt> <dd> <dl> <dt>

8487 (0x2127)
</dt> <dt>



Destination of a cross-domain move is not authoritative for the destination naming context.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_SRC_GUID_MISMATCH"></span><span id="error_ds_src_guid_mismatch"></span>**ERROR\_DS\_SRC\_GUID\_MISMATCH**
</dt> <dd> <dl> <dt>

8488 (0x2128)
</dt> <dt>



Source and destination of a cross-domain move do not agree on the identity of the source object. Either source or destination does not have the latest version of the source object.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CANT_MOVE_DELETED_OBJECT"></span><span id="error_ds_cant_move_deleted_object"></span>**ERROR\_DS\_CANT\_MOVE\_DELETED\_OBJECT**
</dt> <dd> <dl> <dt>

8489 (0x2129)
</dt> <dt>



Object being moved across-domains is already known to be deleted by the destination server. The source server does not have the latest version of the source object.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_PDC_OPERATION_IN_PROGRESS"></span><span id="error_ds_pdc_operation_in_progress"></span>**ERROR\_DS\_PDC\_OPERATION\_IN\_PROGRESS**
</dt> <dd> <dl> <dt>

8490 (0x212A)
</dt> <dt>



Another operation which requires exclusive access to the PDC FSMO is already in progress.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CROSS_DOMAIN_CLEANUP_REQD"></span><span id="error_ds_cross_domain_cleanup_reqd"></span>**ERROR\_DS\_CROSS\_DOMAIN\_CLEANUP\_REQD**
</dt> <dd> <dl> <dt>

8491 (0x212B)
</dt> <dt>



A cross-domain move operation failed such that two versions of the moved object exist - one each in the source and destination domains. The destination object needs to be removed to restore the system to a consistent state.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_ILLEGAL_XDOM_MOVE_OPERATION"></span><span id="error_ds_illegal_xdom_move_operation"></span>**ERROR\_DS\_ILLEGAL\_XDOM\_MOVE\_OPERATION**
</dt> <dd> <dl> <dt>

8492 (0x212C)
</dt> <dt>



This object may not be moved across domain boundaries either because cross-domain moves for this class are disallowed, or the object has some special characteristics, e.g.: trust account or restricted RID, which prevent its move.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CANT_WITH_ACCT_GROUP_MEMBERSHPS"></span><span id="error_ds_cant_with_acct_group_membershps"></span>**ERROR\_DS\_CANT\_WITH\_ACCT\_GROUP\_MEMBERSHPS**
</dt> <dd> <dl> <dt>

8493 (0x212D)
</dt> <dt>



Can't move objects with memberships across domain boundaries as once moved, this would violate the membership conditions of the account group. Remove the object from any account group memberships and retry.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NC_MUST_HAVE_NC_PARENT"></span><span id="error_ds_nc_must_have_nc_parent"></span>**ERROR\_DS\_NC\_MUST\_HAVE\_NC\_PARENT**
</dt> <dd> <dl> <dt>

8494 (0x212E)
</dt> <dt>



A naming context head must be the immediate child of another naming context head, not of an interior node.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CR_IMPOSSIBLE_TO_VALIDATE"></span><span id="error_ds_cr_impossible_to_validate"></span>**ERROR\_DS\_CR\_IMPOSSIBLE\_TO\_VALIDATE**
</dt> <dd> <dl> <dt>

8495 (0x212F)
</dt> <dt>



The directory cannot validate the proposed naming context name because it does not hold a replica of the naming context above the proposed naming context. Please ensure that the domain naming master role is held by a server that is configured as a global catalog server, and that the server is up to date with its replication partners. (Applies only to Windows 2000 Domain Naming masters.)


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DST_DOMAIN_NOT_NATIVE"></span><span id="error_ds_dst_domain_not_native"></span>**ERROR\_DS\_DST\_DOMAIN\_NOT\_NATIVE**
</dt> <dd> <dl> <dt>

8496 (0x2130)
</dt> <dt>



Destination domain must be in native mode.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_MISSING_INFRASTRUCTURE_CONTAINER"></span><span id="error_ds_missing_infrastructure_container"></span>**ERROR\_DS\_MISSING\_INFRASTRUCTURE\_CONTAINER**
</dt> <dd> <dl> <dt>

8497 (0x2131)
</dt> <dt>



The operation cannot be performed because the server does not have an infrastructure container in the domain of interest.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CANT_MOVE_ACCOUNT_GROUP"></span><span id="error_ds_cant_move_account_group"></span>**ERROR\_DS\_CANT\_MOVE\_ACCOUNT\_GROUP**
</dt> <dd> <dl> <dt>

8498 (0x2132)
</dt> <dt>



Cross-domain move of non-empty account groups is not allowed.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CANT_MOVE_RESOURCE_GROUP"></span><span id="error_ds_cant_move_resource_group"></span>**ERROR\_DS\_CANT\_MOVE\_RESOURCE\_GROUP**
</dt> <dd> <dl> <dt>

8499 (0x2133)
</dt> <dt>



Cross-domain move of non-empty resource groups is not allowed.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_INVALID_SEARCH_FLAG"></span><span id="error_ds_invalid_search_flag"></span>**ERROR\_DS\_INVALID\_SEARCH\_FLAG**
</dt> <dd> <dl> <dt>

8500 (0x2134)
</dt> <dt>



The search flags for the attribute are invalid. The ANR bit is valid only on attributes of Unicode or Teletex strings.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NO_TREE_DELETE_ABOVE_NC"></span><span id="error_ds_no_tree_delete_above_nc"></span>**ERROR\_DS\_NO\_TREE\_DELETE\_ABOVE\_NC**
</dt> <dd> <dl> <dt>

8501 (0x2135)
</dt> <dt>



Tree deletions starting at an object which has an NC head as a descendant are not allowed.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_COULDNT_LOCK_TREE_FOR_DELETE"></span><span id="error_ds_couldnt_lock_tree_for_delete"></span>**ERROR\_DS\_COULDNT\_LOCK\_TREE\_FOR\_DELETE**
</dt> <dd> <dl> <dt>

8502 (0x2136)
</dt> <dt>



The directory service failed to lock a tree in preparation for a tree deletion because the tree was in use.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_COULDNT_IDENTIFY_OBJECTS_FOR_TREE_DELETE"></span><span id="error_ds_couldnt_identify_objects_for_tree_delete"></span>**ERROR\_DS\_COULDNT\_IDENTIFY\_OBJECTS\_FOR\_TREE\_DELETE**
</dt> <dd> <dl> <dt>

8503 (0x2137)
</dt> <dt>



The directory service failed to identify the list of objects to delete while attempting a tree deletion.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_SAM_INIT_FAILURE"></span><span id="error_ds_sam_init_failure"></span>**ERROR\_DS\_SAM\_INIT\_FAILURE**
</dt> <dd> <dl> <dt>

8504 (0x2138)
</dt> <dt>



Security Accounts Manager initialization failed because of the following error: %1. Error Status: 0x%2. Please shutdown this system and reboot into Directory Services Restore Mode, check the event log for more detailed information.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_SENSITIVE_GROUP_VIOLATION"></span><span id="error_ds_sensitive_group_violation"></span>**ERROR\_DS\_SENSITIVE\_GROUP\_VIOLATION**
</dt> <dd> <dl> <dt>

8505 (0x2139)
</dt> <dt>



Only an administrator can modify the membership list of an administrative group.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CANT_MOD_PRIMARYGROUPID"></span><span id="error_ds_cant_mod_primarygroupid"></span>**ERROR\_DS\_CANT\_MOD\_PRIMARYGROUPID**
</dt> <dd> <dl> <dt>

8506 (0x213A)
</dt> <dt>



Cannot change the primary group ID of a domain controller account.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_ILLEGAL_BASE_SCHEMA_MOD"></span><span id="error_ds_illegal_base_schema_mod"></span>**ERROR\_DS\_ILLEGAL\_BASE\_SCHEMA\_MOD**
</dt> <dd> <dl> <dt>

8507 (0x213B)
</dt> <dt>



An attempt is made to modify the base schema.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NONSAFE_SCHEMA_CHANGE"></span><span id="error_ds_nonsafe_schema_change"></span>**ERROR\_DS\_NONSAFE\_SCHEMA\_CHANGE**
</dt> <dd> <dl> <dt>

8508 (0x213C)
</dt> <dt>



Adding a new mandatory attribute to an existing class, deleting a mandatory attribute from an existing class, or adding an optional attribute to the special class Top that is not a backlink attribute (directly or through inheritance, for example, by adding or deleting an auxiliary class) is not allowed.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_SCHEMA_UPDATE_DISALLOWED"></span><span id="error_ds_schema_update_disallowed"></span>**ERROR\_DS\_SCHEMA\_UPDATE\_DISALLOWED**
</dt> <dd> <dl> <dt>

8509 (0x213D)
</dt> <dt>



Schema update is not allowed on this DC because the DC is not the schema FSMO Role Owner.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CANT_CREATE_UNDER_SCHEMA"></span><span id="error_ds_cant_create_under_schema"></span>**ERROR\_DS\_CANT\_CREATE\_UNDER\_SCHEMA**
</dt> <dd> <dl> <dt>

8510 (0x213E)
</dt> <dt>



An object of this class cannot be created under the schema container. You can only create attribute-schema and class-schema objects under the schema container.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_INSTALL_NO_SRC_SCH_VERSION"></span><span id="error_ds_install_no_src_sch_version"></span>**ERROR\_DS\_INSTALL\_NO\_SRC\_SCH\_VERSION**
</dt> <dd> <dl> <dt>

8511 (0x213F)
</dt> <dt>



The replica/child install failed to get the objectVersion attribute on the schema container on the source DC. Either the attribute is missing on the schema container or the credentials supplied do not have permission to read it.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_INSTALL_NO_SCH_VERSION_IN_INIFILE"></span><span id="error_ds_install_no_sch_version_in_inifile"></span>**ERROR\_DS\_INSTALL\_NO\_SCH\_VERSION\_IN\_INIFILE**
</dt> <dd> <dl> <dt>

8512 (0x2140)
</dt> <dt>



The replica/child install failed to read the objectVersion attribute in the SCHEMA section of the file schema.ini in the system32 directory.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_INVALID_GROUP_TYPE"></span><span id="error_ds_invalid_group_type"></span>**ERROR\_DS\_INVALID\_GROUP\_TYPE**
</dt> <dd> <dl> <dt>

8513 (0x2141)
</dt> <dt>



The specified group type is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NO_NEST_GLOBALGROUP_IN_MIXEDDOMAIN"></span><span id="error_ds_no_nest_globalgroup_in_mixeddomain"></span>**ERROR\_DS\_NO\_NEST\_GLOBALGROUP\_IN\_MIXEDDOMAIN**
</dt> <dd> <dl> <dt>

8514 (0x2142)
</dt> <dt>



You cannot nest global groups in a mixed domain if the group is security-enabled.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NO_NEST_LOCALGROUP_IN_MIXEDDOMAIN"></span><span id="error_ds_no_nest_localgroup_in_mixeddomain"></span>**ERROR\_DS\_NO\_NEST\_LOCALGROUP\_IN\_MIXEDDOMAIN**
</dt> <dd> <dl> <dt>

8515 (0x2143)
</dt> <dt>



You cannot nest local groups in a mixed domain if the group is security-enabled.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_GLOBAL_CANT_HAVE_LOCAL_MEMBER"></span><span id="error_ds_global_cant_have_local_member"></span>**ERROR\_DS\_GLOBAL\_CANT\_HAVE\_LOCAL\_MEMBER**
</dt> <dd> <dl> <dt>

8516 (0x2144)
</dt> <dt>



A global group cannot have a local group as a member.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_GLOBAL_CANT_HAVE_UNIVERSAL_MEMBER"></span><span id="error_ds_global_cant_have_universal_member"></span>**ERROR\_DS\_GLOBAL\_CANT\_HAVE\_UNIVERSAL\_MEMBER**
</dt> <dd> <dl> <dt>

8517 (0x2145)
</dt> <dt>



A global group cannot have a universal group as a member.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_UNIVERSAL_CANT_HAVE_LOCAL_MEMBER"></span><span id="error_ds_universal_cant_have_local_member"></span>**ERROR\_DS\_UNIVERSAL\_CANT\_HAVE\_LOCAL\_MEMBER**
</dt> <dd> <dl> <dt>

8518 (0x2146)
</dt> <dt>



A universal group cannot have a local group as a member.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_GLOBAL_CANT_HAVE_CROSSDOMAIN_MEMBER"></span><span id="error_ds_global_cant_have_crossdomain_member"></span>**ERROR\_DS\_GLOBAL\_CANT\_HAVE\_CROSSDOMAIN\_MEMBER**
</dt> <dd> <dl> <dt>

8519 (0x2147)
</dt> <dt>



A global group cannot have a cross-domain member.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_LOCAL_CANT_HAVE_CROSSDOMAIN_LOCAL_MEMBER"></span><span id="error_ds_local_cant_have_crossdomain_local_member"></span>**ERROR\_DS\_LOCAL\_CANT\_HAVE\_CROSSDOMAIN\_LOCAL\_MEMBER**
</dt> <dd> <dl> <dt>

8520 (0x2148)
</dt> <dt>



A local group cannot have another cross domain local group as a member.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_HAVE_PRIMARY_MEMBERS"></span><span id="error_ds_have_primary_members"></span>**ERROR\_DS\_HAVE\_PRIMARY\_MEMBERS**
</dt> <dd> <dl> <dt>

8521 (0x2149)
</dt> <dt>



A group with primary members cannot change to a security-disabled group.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_STRING_SD_CONVERSION_FAILED"></span><span id="error_ds_string_sd_conversion_failed"></span>**ERROR\_DS\_STRING\_SD\_CONVERSION\_FAILED**
</dt> <dd> <dl> <dt>

8522 (0x214A)
</dt> <dt>



The schema cache load failed to convert the string default SD on a class-schema object.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NAMING_MASTER_GC"></span><span id="error_ds_naming_master_gc"></span>**ERROR\_DS\_NAMING\_MASTER\_GC**
</dt> <dd> <dl> <dt>

8523 (0x214B)
</dt> <dt>



Only DSAs configured to be Global Catalog servers should be allowed to hold the Domain Naming Master FSMO role. (Applies only to Windows 2000 servers.)


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DNS_LOOKUP_FAILURE"></span><span id="error_ds_dns_lookup_failure"></span>**ERROR\_DS\_DNS\_LOOKUP\_FAILURE**
</dt> <dd> <dl> <dt>

8524 (0x214C)
</dt> <dt>



The DSA operation is unable to proceed because of a DNS lookup failure.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_COULDNT_UPDATE_SPNS"></span><span id="error_ds_couldnt_update_spns"></span>**ERROR\_DS\_COULDNT\_UPDATE\_SPNS**
</dt> <dd> <dl> <dt>

8525 (0x214D)
</dt> <dt>



While processing a change to the DNS Host Name for an object, the Service Principal Name values could not be kept in sync.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CANT_RETRIEVE_SD"></span><span id="error_ds_cant_retrieve_sd"></span>**ERROR\_DS\_CANT\_RETRIEVE\_SD**
</dt> <dd> <dl> <dt>

8526 (0x214E)
</dt> <dt>



The Security Descriptor attribute could not be read.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_KEY_NOT_UNIQUE"></span><span id="error_ds_key_not_unique"></span>**ERROR\_DS\_KEY\_NOT\_UNIQUE**
</dt> <dd> <dl> <dt>

8527 (0x214F)
</dt> <dt>



The object requested was not found, but an object with that key was found.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_WRONG_LINKED_ATT_SYNTAX"></span><span id="error_ds_wrong_linked_att_syntax"></span>**ERROR\_DS\_WRONG\_LINKED\_ATT\_SYNTAX**
</dt> <dd> <dl> <dt>

8528 (0x2150)
</dt> <dt>



The syntax of the linked attribute being added is incorrect. Forward links can only have syntax 2.5.5.1, 2.5.5.7, and 2.5.5.14, and backlinks can only have syntax 2.5.5.1.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_SAM_NEED_BOOTKEY_PASSWORD"></span><span id="error_ds_sam_need_bootkey_password"></span>**ERROR\_DS\_SAM\_NEED\_BOOTKEY\_PASSWORD**
</dt> <dd> <dl> <dt>

8529 (0x2151)
</dt> <dt>



Security Account Manager needs to get the boot password.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_SAM_NEED_BOOTKEY_FLOPPY"></span><span id="error_ds_sam_need_bootkey_floppy"></span>**ERROR\_DS\_SAM\_NEED\_BOOTKEY\_FLOPPY**
</dt> <dd> <dl> <dt>

8530 (0x2152)
</dt> <dt>



Security Account Manager needs to get the boot key from floppy disk.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CANT_START"></span><span id="error_ds_cant_start"></span>**ERROR\_DS\_CANT\_START**
</dt> <dd> <dl> <dt>

8531 (0x2153)
</dt> <dt>



Directory Service cannot start.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_INIT_FAILURE"></span><span id="error_ds_init_failure"></span>**ERROR\_DS\_INIT\_FAILURE**
</dt> <dd> <dl> <dt>

8532 (0x2154)
</dt> <dt>



Directory Services could not start.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NO_PKT_PRIVACY_ON_CONNECTION"></span><span id="error_ds_no_pkt_privacy_on_connection"></span>**ERROR\_DS\_NO\_PKT\_PRIVACY\_ON\_CONNECTION**
</dt> <dd> <dl> <dt>

8533 (0x2155)
</dt> <dt>



The connection between client and server requires packet privacy or better.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_SOURCE_DOMAIN_IN_FOREST"></span><span id="error_ds_source_domain_in_forest"></span>**ERROR\_DS\_SOURCE\_DOMAIN\_IN\_FOREST**
</dt> <dd> <dl> <dt>

8534 (0x2156)
</dt> <dt>



The source domain may not be in the same forest as destination.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DESTINATION_DOMAIN_NOT_IN_FOREST"></span><span id="error_ds_destination_domain_not_in_forest"></span>**ERROR\_DS\_DESTINATION\_DOMAIN\_NOT\_IN\_FOREST**
</dt> <dd> <dl> <dt>

8535 (0x2157)
</dt> <dt>



The destination domain must be in the forest.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DESTINATION_AUDITING_NOT_ENABLED"></span><span id="error_ds_destination_auditing_not_enabled"></span>**ERROR\_DS\_DESTINATION\_AUDITING\_NOT\_ENABLED**
</dt> <dd> <dl> <dt>

8536 (0x2158)
</dt> <dt>



The operation requires that destination domain auditing be enabled.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CANT_FIND_DC_FOR_SRC_DOMAIN"></span><span id="error_ds_cant_find_dc_for_src_domain"></span>**ERROR\_DS\_CANT\_FIND\_DC\_FOR\_SRC\_DOMAIN**
</dt> <dd> <dl> <dt>

8537 (0x2159)
</dt> <dt>



The operation couldn't locate a DC for the source domain.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_SRC_OBJ_NOT_GROUP_OR_USER"></span><span id="error_ds_src_obj_not_group_or_user"></span>**ERROR\_DS\_SRC\_OBJ\_NOT\_GROUP\_OR\_USER**
</dt> <dd> <dl> <dt>

8538 (0x215A)
</dt> <dt>



The source object must be a group or user.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_SRC_SID_EXISTS_IN_FOREST"></span><span id="error_ds_src_sid_exists_in_forest"></span>**ERROR\_DS\_SRC\_SID\_EXISTS\_IN\_FOREST**
</dt> <dd> <dl> <dt>

8539 (0x215B)
</dt> <dt>



The source object's SID already exists in destination forest.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_SRC_AND_DST_OBJECT_CLASS_MISMATCH"></span><span id="error_ds_src_and_dst_object_class_mismatch"></span>**ERROR\_DS\_SRC\_AND\_DST\_OBJECT\_CLASS\_MISMATCH**
</dt> <dd> <dl> <dt>

8540 (0x215C)
</dt> <dt>



The source and destination object must be of the same type.


</dt> </dl> </dd> <dt>

<span id="ERROR_SAM_INIT_FAILURE"></span><span id="error_sam_init_failure"></span>**ERROR\_SAM\_INIT\_FAILURE**
</dt> <dd> <dl> <dt>

8541 (0x215D)
</dt> <dt>



Security Accounts Manager initialization failed because of the following error: %1. Error Status: 0x%2. Click OK to shut down the system and reboot into Safe Mode. Check the event log for detailed information.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DRA_SCHEMA_INFO_SHIP"></span><span id="error_ds_dra_schema_info_ship"></span>**ERROR\_DS\_DRA\_SCHEMA\_INFO\_SHIP**
</dt> <dd> <dl> <dt>

8542 (0x215E)
</dt> <dt>



Schema information could not be included in the replication request.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DRA_SCHEMA_CONFLICT"></span><span id="error_ds_dra_schema_conflict"></span>**ERROR\_DS\_DRA\_SCHEMA\_CONFLICT**
</dt> <dd> <dl> <dt>

8543 (0x215F)
</dt> <dt>



The replication operation could not be completed due to a schema incompatibility.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DRA_EARLIER_SCHEMA_CONFLICT"></span><span id="error_ds_dra_earlier_schema_conflict"></span>**ERROR\_DS\_DRA\_EARLIER\_SCHEMA\_CONFLICT**
</dt> <dd> <dl> <dt>

8544 (0x2160)
</dt> <dt>



The replication operation could not be completed due to a previous schema incompatibility.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DRA_OBJ_NC_MISMATCH"></span><span id="error_ds_dra_obj_nc_mismatch"></span>**ERROR\_DS\_DRA\_OBJ\_NC\_MISMATCH**
</dt> <dd> <dl> <dt>

8545 (0x2161)
</dt> <dt>



The replication update could not be applied because either the source or the destination has not yet received information regarding a recent cross-domain move operation.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NC_STILL_HAS_DSAS"></span><span id="error_ds_nc_still_has_dsas"></span>**ERROR\_DS\_NC\_STILL\_HAS\_DSAS**
</dt> <dd> <dl> <dt>

8546 (0x2162)
</dt> <dt>



The requested domain could not be deleted because there exist domain controllers that still host this domain.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_GC_REQUIRED"></span><span id="error_ds_gc_required"></span>**ERROR\_DS\_GC\_REQUIRED**
</dt> <dd> <dl> <dt>

8547 (0x2163)
</dt> <dt>



The requested operation can be performed only on a global catalog server.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_LOCAL_MEMBER_OF_LOCAL_ONLY"></span><span id="error_ds_local_member_of_local_only"></span>**ERROR\_DS\_LOCAL\_MEMBER\_OF\_LOCAL\_ONLY**
</dt> <dd> <dl> <dt>

8548 (0x2164)
</dt> <dt>



A local group can only be a member of other local groups in the same domain.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NO_FPO_IN_UNIVERSAL_GROUPS"></span><span id="error_ds_no_fpo_in_universal_groups"></span>**ERROR\_DS\_NO\_FPO\_IN\_UNIVERSAL\_GROUPS**
</dt> <dd> <dl> <dt>

8549 (0x2165)
</dt> <dt>



Foreign security principals cannot be members of universal groups.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CANT_ADD_TO_GC"></span><span id="error_ds_cant_add_to_gc"></span>**ERROR\_DS\_CANT\_ADD\_TO\_GC**
</dt> <dd> <dl> <dt>

8550 (0x2166)
</dt> <dt>



The attribute is not allowed to be replicated to the GC because of security reasons.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NO_CHECKPOINT_WITH_PDC"></span><span id="error_ds_no_checkpoint_with_pdc"></span>**ERROR\_DS\_NO\_CHECKPOINT\_WITH\_PDC**
</dt> <dd> <dl> <dt>

8551 (0x2167)
</dt> <dt>



The checkpoint with the PDC could not be taken because there too many modifications being processed currently.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_SOURCE_AUDITING_NOT_ENABLED"></span><span id="error_ds_source_auditing_not_enabled"></span>**ERROR\_DS\_SOURCE\_AUDITING\_NOT\_ENABLED**
</dt> <dd> <dl> <dt>

8552 (0x2168)
</dt> <dt>



The operation requires that source domain auditing be enabled.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CANT_CREATE_IN_NONDOMAIN_NC"></span><span id="error_ds_cant_create_in_nondomain_nc"></span>**ERROR\_DS\_CANT\_CREATE\_IN\_NONDOMAIN\_NC**
</dt> <dd> <dl> <dt>

8553 (0x2169)
</dt> <dt>



Security principal objects can only be created inside domain naming contexts.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_INVALID_NAME_FOR_SPN"></span><span id="error_ds_invalid_name_for_spn"></span>**ERROR\_DS\_INVALID\_NAME\_FOR\_SPN**
</dt> <dd> <dl> <dt>

8554 (0x216A)
</dt> <dt>



A Service Principal Name (SPN) could not be constructed because the provided hostname is not in the necessary format.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_FILTER_USES_CONTRUCTED_ATTRS"></span><span id="error_ds_filter_uses_contructed_attrs"></span>**ERROR\_DS\_FILTER\_USES\_CONTRUCTED\_ATTRS**
</dt> <dd> <dl> <dt>

8555 (0x216B)
</dt> <dt>



A Filter was passed that uses constructed attributes.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_UNICODEPWD_NOT_IN_QUOTES"></span><span id="error_ds_unicodepwd_not_in_quotes"></span>**ERROR\_DS\_UNICODEPWD\_NOT\_IN\_QUOTES**
</dt> <dd> <dl> <dt>

8556 (0x216C)
</dt> <dt>



The unicodePwd attribute value must be enclosed in double quotes.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED"></span><span id="error_ds_machine_account_quota_exceeded"></span>**ERROR\_DS\_MACHINE\_ACCOUNT\_QUOTA\_EXCEEDED**
</dt> <dd> <dl> <dt>

8557 (0x216D)
</dt> <dt>



Your computer could not be joined to the domain. You have exceeded the maximum number of computer accounts you are allowed to create in this domain. Contact your system administrator to have this limit reset or increased.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_MUST_BE_RUN_ON_DST_DC"></span><span id="error_ds_must_be_run_on_dst_dc"></span>**ERROR\_DS\_MUST\_BE\_RUN\_ON\_DST\_DC**
</dt> <dd> <dl> <dt>

8558 (0x216E)
</dt> <dt>



For security reasons, the operation must be run on the destination DC.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_SRC_DC_MUST_BE_SP4_OR_GREATER"></span><span id="error_ds_src_dc_must_be_sp4_or_greater"></span>**ERROR\_DS\_SRC\_DC\_MUST\_BE\_SP4\_OR\_GREATER**
</dt> <dd> <dl> <dt>

8559 (0x216F)
</dt> <dt>



For security reasons, the source DC must be NT4SP4 or greater.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CANT_TREE_DELETE_CRITICAL_OBJ"></span><span id="error_ds_cant_tree_delete_critical_obj"></span>**ERROR\_DS\_CANT\_TREE\_DELETE\_CRITICAL\_OBJ**
</dt> <dd> <dl> <dt>

8560 (0x2170)
</dt> <dt>



Critical Directory Service System objects cannot be deleted during tree delete operations. The tree delete may have been partially performed.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_INIT_FAILURE_CONSOLE"></span><span id="error_ds_init_failure_console"></span>**ERROR\_DS\_INIT\_FAILURE\_CONSOLE**
</dt> <dd> <dl> <dt>

8561 (0x2171)
</dt> <dt>



Directory Services could not start because of the following error: %1. Error Status: 0x%2. Please click OK to shutdown the system. You can use the recovery console to diagnose the system further.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_SAM_INIT_FAILURE_CONSOLE"></span><span id="error_ds_sam_init_failure_console"></span>**ERROR\_DS\_SAM\_INIT\_FAILURE\_CONSOLE**
</dt> <dd> <dl> <dt>

8562 (0x2172)
</dt> <dt>



Security Accounts Manager initialization failed because of the following error: %1. Error Status: 0x%2. Please click OK to shutdown the system. You can use the recovery console to diagnose the system further.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_FOREST_VERSION_TOO_HIGH"></span><span id="error_ds_forest_version_too_high"></span>**ERROR\_DS\_FOREST\_VERSION\_TOO\_HIGH**
</dt> <dd> <dl> <dt>

8563 (0x2173)
</dt> <dt>



The version of the operating system is incompatible with the current AD DS forest functional level or AD LDS Configuration Set functional level. You must upgrade to a new version of the operating system before this server can become an AD DS Domain Controller or add an AD LDS Instance in this AD DS Forest or AD LDS Configuration Set.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DOMAIN_VERSION_TOO_HIGH"></span><span id="error_ds_domain_version_too_high"></span>**ERROR\_DS\_DOMAIN\_VERSION\_TOO\_HIGH**
</dt> <dd> <dl> <dt>

8564 (0x2174)
</dt> <dt>



The version of the operating system installed is incompatible with the current domain functional level. You must upgrade to a new version of the operating system before this server can become a domain controller in this domain.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_FOREST_VERSION_TOO_LOW"></span><span id="error_ds_forest_version_too_low"></span>**ERROR\_DS\_FOREST\_VERSION\_TOO\_LOW**
</dt> <dd> <dl> <dt>

8565 (0x2175)
</dt> <dt>



The version of the operating system installed on this server no longer supports the current AD DS Forest functional level or AD LDS Configuration Set functional level. You must raise the AD DS Forest functional level or AD LDS Configuration Set functional level before this server can become an AD DS Domain Controller or an AD LDS Instance in this Forest or Configuration Set.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DOMAIN_VERSION_TOO_LOW"></span><span id="error_ds_domain_version_too_low"></span>**ERROR\_DS\_DOMAIN\_VERSION\_TOO\_LOW**
</dt> <dd> <dl> <dt>

8566 (0x2176)
</dt> <dt>



The version of the operating system installed on this server no longer supports the current domain functional level. You must raise the domain functional level before this server can become a domain controller in this domain.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_INCOMPATIBLE_VERSION"></span><span id="error_ds_incompatible_version"></span>**ERROR\_DS\_INCOMPATIBLE\_VERSION**
</dt> <dd> <dl> <dt>

8567 (0x2177)
</dt> <dt>



The version of the operating system installed on this server is incompatible with the functional level of the domain or forest.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_LOW_DSA_VERSION"></span><span id="error_ds_low_dsa_version"></span>**ERROR\_DS\_LOW\_DSA\_VERSION**
</dt> <dd> <dl> <dt>

8568 (0x2178)
</dt> <dt>



The functional level of the domain (or forest) cannot be raised to the requested value, because there exist one or more domain controllers in the domain (or forest) that are at a lower incompatible functional level.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NO_BEHAVIOR_VERSION_IN_MIXEDDOMAIN"></span><span id="error_ds_no_behavior_version_in_mixeddomain"></span>**ERROR\_DS\_NO\_BEHAVIOR\_VERSION\_IN\_MIXEDDOMAIN**
</dt> <dd> <dl> <dt>

8569 (0x2179)
</dt> <dt>



The forest functional level cannot be raised to the requested value since one or more domains are still in mixed domain mode. All domains in the forest must be in native mode, for you to raise the forest functional level.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NOT_SUPPORTED_SORT_ORDER"></span><span id="error_ds_not_supported_sort_order"></span>**ERROR\_DS\_NOT\_SUPPORTED\_SORT\_ORDER**
</dt> <dd> <dl> <dt>

8570 (0x217A)
</dt> <dt>



The sort order requested is not supported.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NAME_NOT_UNIQUE"></span><span id="error_ds_name_not_unique"></span>**ERROR\_DS\_NAME\_NOT\_UNIQUE**
</dt> <dd> <dl> <dt>

8571 (0x217B)
</dt> <dt>



The requested name already exists as a unique identifier.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_MACHINE_ACCOUNT_CREATED_PRENT4"></span><span id="error_ds_machine_account_created_prent4"></span>**ERROR\_DS\_MACHINE\_ACCOUNT\_CREATED\_PRENT4**
</dt> <dd> <dl> <dt>

8572 (0x217C)
</dt> <dt>



The machine account was created pre-NT4. The account needs to be recreated.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_OUT_OF_VERSION_STORE"></span><span id="error_ds_out_of_version_store"></span>**ERROR\_DS\_OUT\_OF\_VERSION\_STORE**
</dt> <dd> <dl> <dt>

8573 (0x217D)
</dt> <dt>



The database is out of version store.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_INCOMPATIBLE_CONTROLS_USED"></span><span id="error_ds_incompatible_controls_used"></span>**ERROR\_DS\_INCOMPATIBLE\_CONTROLS\_USED**
</dt> <dd> <dl> <dt>

8574 (0x217E)
</dt> <dt>



Unable to continue operation because multiple conflicting controls were used.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NO_REF_DOMAIN"></span><span id="error_ds_no_ref_domain"></span>**ERROR\_DS\_NO\_REF\_DOMAIN**
</dt> <dd> <dl> <dt>

8575 (0x217F)
</dt> <dt>



Unable to find a valid security descriptor reference domain for this partition.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_RESERVED_LINK_ID"></span><span id="error_ds_reserved_link_id"></span>**ERROR\_DS\_RESERVED\_LINK\_ID**
</dt> <dd> <dl> <dt>

8576 (0x2180)
</dt> <dt>



Schema update failed: The link identifier is reserved.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_LINK_ID_NOT_AVAILABLE"></span><span id="error_ds_link_id_not_available"></span>**ERROR\_DS\_LINK\_ID\_NOT\_AVAILABLE**
</dt> <dd> <dl> <dt>

8577 (0x2181)
</dt> <dt>



Schema update failed: There are no link identifiers available.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_AG_CANT_HAVE_UNIVERSAL_MEMBER"></span><span id="error_ds_ag_cant_have_universal_member"></span>**ERROR\_DS\_AG\_CANT\_HAVE\_UNIVERSAL\_MEMBER**
</dt> <dd> <dl> <dt>

8578 (0x2182)
</dt> <dt>



An account group cannot have a universal group as a member.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_MODIFYDN_DISALLOWED_BY_INSTANCE_TYPE"></span><span id="error_ds_modifydn_disallowed_by_instance_type"></span>**ERROR\_DS\_MODIFYDN\_DISALLOWED\_BY\_INSTANCE\_TYPE**
</dt> <dd> <dl> <dt>

8579 (0x2183)
</dt> <dt>



Rename or move operations on naming context heads or read-only objects are not allowed.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NO_OBJECT_MOVE_IN_SCHEMA_NC"></span><span id="error_ds_no_object_move_in_schema_nc"></span>**ERROR\_DS\_NO\_OBJECT\_MOVE\_IN\_SCHEMA\_NC**
</dt> <dd> <dl> <dt>

8580 (0x2184)
</dt> <dt>



Move operations on objects in the schema naming context are not allowed.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_MODIFYDN_DISALLOWED_BY_FLAG"></span><span id="error_ds_modifydn_disallowed_by_flag"></span>**ERROR\_DS\_MODIFYDN\_DISALLOWED\_BY\_FLAG**
</dt> <dd> <dl> <dt>

8581 (0x2185)
</dt> <dt>



A system flag has been set on the object and does not allow the object to be moved or renamed.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_MODIFYDN_WRONG_GRANDPARENT"></span><span id="error_ds_modifydn_wrong_grandparent"></span>**ERROR\_DS\_MODIFYDN\_WRONG\_GRANDPARENT**
</dt> <dd> <dl> <dt>

8582 (0x2186)
</dt> <dt>



This object is not allowed to change its grandparent container. Moves are not forbidden on this object, but are restricted to sibling containers.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NAME_ERROR_TRUST_REFERRAL"></span><span id="error_ds_name_error_trust_referral"></span>**ERROR\_DS\_NAME\_ERROR\_TRUST\_REFERRAL**
</dt> <dd> <dl> <dt>

8583 (0x2187)
</dt> <dt>



Unable to resolve completely, a referral to another forest is generated.


</dt> </dl> </dd> <dt>

<span id="ERROR_NOT_SUPPORTED_ON_STANDARD_SERVER"></span><span id="error_not_supported_on_standard_server"></span>**ERROR\_NOT\_SUPPORTED\_ON\_STANDARD\_SERVER**
</dt> <dd> <dl> <dt>

8584 (0x2188)
</dt> <dt>



The requested action is not supported on standard server.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CANT_ACCESS_REMOTE_PART_OF_AD"></span><span id="error_ds_cant_access_remote_part_of_ad"></span>**ERROR\_DS\_CANT\_ACCESS\_REMOTE\_PART\_OF\_AD**
</dt> <dd> <dl> <dt>

8585 (0x2189)
</dt> <dt>



Could not access a partition of the directory service located on a remote server. Make sure at least one server is running for the partition in question.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CR_IMPOSSIBLE_TO_VALIDATE_V2"></span><span id="error_ds_cr_impossible_to_validate_v2"></span>**ERROR\_DS\_CR\_IMPOSSIBLE\_TO\_VALIDATE\_V2**
</dt> <dd> <dl> <dt>

8586 (0x218A)
</dt> <dt>



The directory cannot validate the proposed naming context (or partition) name because it does not hold a replica nor can it contact a replica of the naming context above the proposed naming context. Please ensure that the parent naming context is properly registered in DNS, and at least one replica of this naming context is reachable by the Domain Naming master.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_THREAD_LIMIT_EXCEEDED"></span><span id="error_ds_thread_limit_exceeded"></span>**ERROR\_DS\_THREAD\_LIMIT\_EXCEEDED**
</dt> <dd> <dl> <dt>

8587 (0x218B)
</dt> <dt>



The thread limit for this request was exceeded.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NOT_CLOSEST"></span><span id="error_ds_not_closest"></span>**ERROR\_DS\_NOT\_CLOSEST**
</dt> <dd> <dl> <dt>

8588 (0x218C)
</dt> <dt>



The Global catalog server is not in the closest site.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CANT_DERIVE_SPN_WITHOUT_SERVER_REF"></span><span id="error_ds_cant_derive_spn_without_server_ref"></span>**ERROR\_DS\_CANT\_DERIVE\_SPN\_WITHOUT\_SERVER\_REF**
</dt> <dd> <dl> <dt>

8589 (0x218D)
</dt> <dt>



The DS cannot derive a service principal name (SPN) with which to mutually authenticate the target server because the corresponding server object in the local DS database has no serverReference attribute.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_SINGLE_USER_MODE_FAILED"></span><span id="error_ds_single_user_mode_failed"></span>**ERROR\_DS\_SINGLE\_USER\_MODE\_FAILED**
</dt> <dd> <dl> <dt>

8590 (0x218E)
</dt> <dt>



The Directory Service failed to enter single user mode.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NTDSCRIPT_SYNTAX_ERROR"></span><span id="error_ds_ntdscript_syntax_error"></span>**ERROR\_DS\_NTDSCRIPT\_SYNTAX\_ERROR**
</dt> <dd> <dl> <dt>

8591 (0x218F)
</dt> <dt>



The Directory Service cannot parse the script because of a syntax error.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NTDSCRIPT_PROCESS_ERROR"></span><span id="error_ds_ntdscript_process_error"></span>**ERROR\_DS\_NTDSCRIPT\_PROCESS\_ERROR**
</dt> <dd> <dl> <dt>

8592 (0x2190)
</dt> <dt>



The Directory Service cannot process the script because of an error.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DIFFERENT_REPL_EPOCHS"></span><span id="error_ds_different_repl_epochs"></span>**ERROR\_DS\_DIFFERENT\_REPL\_EPOCHS**
</dt> <dd> <dl> <dt>

8593 (0x2191)
</dt> <dt>



The directory service cannot perform the requested operation because the servers involved are of different replication epochs (which is usually related to a domain rename that is in progress).


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DRS_EXTENSIONS_CHANGED"></span><span id="error_ds_drs_extensions_changed"></span>**ERROR\_DS\_DRS\_EXTENSIONS\_CHANGED**
</dt> <dd> <dl> <dt>

8594 (0x2192)
</dt> <dt>



The directory service binding must be renegotiated due to a change in the server extensions information.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_REPLICA_SET_CHANGE_NOT_ALLOWED_ON_DISABLED_CR"></span><span id="error_ds_replica_set_change_not_allowed_on_disabled_cr"></span>**ERROR\_DS\_REPLICA\_SET\_CHANGE\_NOT\_ALLOWED\_ON\_DISABLED\_CR**
</dt> <dd> <dl> <dt>

8595 (0x2193)
</dt> <dt>



Operation not allowed on a disabled cross ref.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NO_MSDS_INTID"></span><span id="error_ds_no_msds_intid"></span>**ERROR\_DS\_NO\_MSDS\_INTID**
</dt> <dd> <dl> <dt>

8596 (0x2194)
</dt> <dt>



Schema update failed: No values for msDS-IntId are available.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DUP_MSDS_INTID"></span><span id="error_ds_dup_msds_intid"></span>**ERROR\_DS\_DUP\_MSDS\_INTID**
</dt> <dd> <dl> <dt>

8597 (0x2195)
</dt> <dt>



Schema update failed: Duplicate msDS-INtId. Retry the operation.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_EXISTS_IN_RDNATTID"></span><span id="error_ds_exists_in_rdnattid"></span>**ERROR\_DS\_EXISTS\_IN\_RDNATTID**
</dt> <dd> <dl> <dt>

8598 (0x2196)
</dt> <dt>



Schema deletion failed: attribute is used in rDNAttID.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_AUTHORIZATION_FAILED"></span><span id="error_ds_authorization_failed"></span>**ERROR\_DS\_AUTHORIZATION\_FAILED**
</dt> <dd> <dl> <dt>

8599 (0x2197)
</dt> <dt>



The directory service failed to authorize the request.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_INVALID_SCRIPT"></span><span id="error_ds_invalid_script"></span>**ERROR\_DS\_INVALID\_SCRIPT**
</dt> <dd> <dl> <dt>

8600 (0x2198)
</dt> <dt>



The Directory Service cannot process the script because it is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_REMOTE_CROSSREF_OP_FAILED"></span><span id="error_ds_remote_crossref_op_failed"></span>**ERROR\_DS\_REMOTE\_CROSSREF\_OP\_FAILED**
</dt> <dd> <dl> <dt>

8601 (0x2199)
</dt> <dt>



The remote create cross reference operation failed on the Domain Naming Master FSMO. The operation's error is in the extended data.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CROSS_REF_BUSY"></span><span id="error_ds_cross_ref_busy"></span>**ERROR\_DS\_CROSS\_REF\_BUSY**
</dt> <dd> <dl> <dt>

8602 (0x219A)
</dt> <dt>



A cross reference is in use locally with the same name.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CANT_DERIVE_SPN_FOR_DELETED_DOMAIN"></span><span id="error_ds_cant_derive_spn_for_deleted_domain"></span>**ERROR\_DS\_CANT\_DERIVE\_SPN\_FOR\_DELETED\_DOMAIN**
</dt> <dd> <dl> <dt>

8603 (0x219B)
</dt> <dt>



The DS cannot derive a service principal name (SPN) with which to mutually authenticate the target server because the server's domain has been deleted from the forest.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CANT_DEMOTE_WITH_WRITEABLE_NC"></span><span id="error_ds_cant_demote_with_writeable_nc"></span>**ERROR\_DS\_CANT\_DEMOTE\_WITH\_WRITEABLE\_NC**
</dt> <dd> <dl> <dt>

8604 (0x219C)
</dt> <dt>



Writeable NCs prevent this DC from demoting.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DUPLICATE_ID_FOUND"></span><span id="error_ds_duplicate_id_found"></span>**ERROR\_DS\_DUPLICATE\_ID\_FOUND**
</dt> <dd> <dl> <dt>

8605 (0x219D)
</dt> <dt>



The requested object has a non-unique identifier and cannot be retrieved.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_INSUFFICIENT_ATTR_TO_CREATE_OBJECT"></span><span id="error_ds_insufficient_attr_to_create_object"></span>**ERROR\_DS\_INSUFFICIENT\_ATTR\_TO\_CREATE\_OBJECT**
</dt> <dd> <dl> <dt>

8606 (0x219E)
</dt> <dt>



Insufficient attributes were given to create an object. This object may not exist because it may have been deleted and already garbage collected.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_GROUP_CONVERSION_ERROR"></span><span id="error_ds_group_conversion_error"></span>**ERROR\_DS\_GROUP\_CONVERSION\_ERROR**
</dt> <dd> <dl> <dt>

8607 (0x219F)
</dt> <dt>



The group cannot be converted due to attribute restrictions on the requested group type.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CANT_MOVE_APP_BASIC_GROUP"></span><span id="error_ds_cant_move_app_basic_group"></span>**ERROR\_DS\_CANT\_MOVE\_APP\_BASIC\_GROUP**
</dt> <dd> <dl> <dt>

8608 (0x21A0)
</dt> <dt>



Cross-domain move of non-empty basic application groups is not allowed.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_CANT_MOVE_APP_QUERY_GROUP"></span><span id="error_ds_cant_move_app_query_group"></span>**ERROR\_DS\_CANT\_MOVE\_APP\_QUERY\_GROUP**
</dt> <dd> <dl> <dt>

8609 (0x21A1)
</dt> <dt>



Cross-domain move of non-empty query based application groups is not allowed.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_ROLE_NOT_VERIFIED"></span><span id="error_ds_role_not_verified"></span>**ERROR\_DS\_ROLE\_NOT\_VERIFIED**
</dt> <dd> <dl> <dt>

8610 (0x21A2)
</dt> <dt>



The FSMO role ownership could not be verified because its directory partition has not replicated successfully with at least one replication partner.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_WKO_CONTAINER_CANNOT_BE_SPECIAL"></span><span id="error_ds_wko_container_cannot_be_special"></span>**ERROR\_DS\_WKO\_CONTAINER\_CANNOT\_BE\_SPECIAL**
</dt> <dd> <dl> <dt>

8611 (0x21A3)
</dt> <dt>



The target container for a redirection of a well known object container cannot already be a special container.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DOMAIN_RENAME_IN_PROGRESS"></span><span id="error_ds_domain_rename_in_progress"></span>**ERROR\_DS\_DOMAIN\_RENAME\_IN\_PROGRESS**
</dt> <dd> <dl> <dt>

8612 (0x21A4)
</dt> <dt>



The Directory Service cannot perform the requested operation because a domain rename operation is in progress.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_EXISTING_AD_CHILD_NC"></span><span id="error_ds_existing_ad_child_nc"></span>**ERROR\_DS\_EXISTING\_AD\_CHILD\_NC**
</dt> <dd> <dl> <dt>

8613 (0x21A5)
</dt> <dt>



The directory service detected a child partition below the requested partition name. The partition hierarchy must be created in a top down method.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_REPL_LIFETIME_EXCEEDED"></span><span id="error_ds_repl_lifetime_exceeded"></span>**ERROR\_DS\_REPL\_LIFETIME\_EXCEEDED**
</dt> <dd> <dl> <dt>

8614 (0x21A6)
</dt> <dt>



The directory service cannot replicate with this server because the time since the last replication with this server has exceeded the tombstone lifetime.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DISALLOWED_IN_SYSTEM_CONTAINER"></span><span id="error_ds_disallowed_in_system_container"></span>**ERROR\_DS\_DISALLOWED\_IN\_SYSTEM\_CONTAINER**
</dt> <dd> <dl> <dt>

8615 (0x21A7)
</dt> <dt>



The requested operation is not allowed on an object under the system container.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_LDAP_SEND_QUEUE_FULL"></span><span id="error_ds_ldap_send_queue_full"></span>**ERROR\_DS\_LDAP\_SEND\_QUEUE\_FULL**
</dt> <dd> <dl> <dt>

8616 (0x21A8)
</dt> <dt>



The LDAP servers network send queue has filled up because the client is not processing the results of its requests fast enough. No more requests will be processed until the client catches up. If the client does not catch up then it will be disconnected.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DRA_OUT_SCHEDULE_WINDOW"></span><span id="error_ds_dra_out_schedule_window"></span>**ERROR\_DS\_DRA\_OUT\_SCHEDULE\_WINDOW**
</dt> <dd> <dl> <dt>

8617 (0x21A9)
</dt> <dt>



The scheduled replication did not take place because the system was too busy to execute the request within the schedule window. The replication queue is overloaded. Consider reducing the number of partners or decreasing the scheduled replication frequency.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_POLICY_NOT_KNOWN"></span><span id="error_ds_policy_not_known"></span>**ERROR\_DS\_POLICY\_NOT\_KNOWN**
</dt> <dd> <dl> <dt>

8618 (0x21AA)
</dt> <dt>



At this time, it cannot be determined if the branch replication policy is available on the hub domain controller. Please retry at a later time to account for replication latencies.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_SITE_SETTINGS_OBJECT"></span><span id="error_no_site_settings_object"></span>**ERROR\_NO\_SITE\_SETTINGS\_OBJECT**
</dt> <dd> <dl> <dt>

8619 (0x21AB)
</dt> <dt>



The site settings object for the specified site does not exist.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_SECRETS"></span><span id="error_no_secrets"></span>**ERROR\_NO\_SECRETS**
</dt> <dd> <dl> <dt>

8620 (0x21AC)
</dt> <dt>



The local account store does not contain secret material for the specified account.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_WRITABLE_DC_FOUND"></span><span id="error_no_writable_dc_found"></span>**ERROR\_NO\_WRITABLE\_DC\_FOUND**
</dt> <dd> <dl> <dt>

8621 (0x21AD)
</dt> <dt>



Could not find a writable domain controller in the domain.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NO_SERVER_OBJECT"></span><span id="error_ds_no_server_object"></span>**ERROR\_DS\_NO\_SERVER\_OBJECT**
</dt> <dd> <dl> <dt>

8622 (0x21AE)
</dt> <dt>



The server object for the domain controller does not exist.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NO_NTDSA_OBJECT"></span><span id="error_ds_no_ntdsa_object"></span>**ERROR\_DS\_NO\_NTDSA\_OBJECT**
</dt> <dd> <dl> <dt>

8623 (0x21AF)
</dt> <dt>



The NTDS Settings object for the domain controller does not exist.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_NON_ASQ_SEARCH"></span><span id="error_ds_non_asq_search"></span>**ERROR\_DS\_NON\_ASQ\_SEARCH**
</dt> <dd> <dl> <dt>

8624 (0x21B0)
</dt> <dt>



The requested search operation is not supported for ASQ searches.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_AUDIT_FAILURE"></span><span id="error_ds_audit_failure"></span>**ERROR\_DS\_AUDIT\_FAILURE**
</dt> <dd> <dl> <dt>

8625 (0x21B1)
</dt> <dt>



A required audit event could not be generated for the operation.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_INVALID_SEARCH_FLAG_SUBTREE"></span><span id="error_ds_invalid_search_flag_subtree"></span>**ERROR\_DS\_INVALID\_SEARCH\_FLAG\_SUBTREE**
</dt> <dd> <dl> <dt>

8626 (0x21B2)
</dt> <dt>



The search flags for the attribute are invalid. The subtree index bit is valid only on single valued attributes.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_INVALID_SEARCH_FLAG_TUPLE"></span><span id="error_ds_invalid_search_flag_tuple"></span>**ERROR\_DS\_INVALID\_SEARCH\_FLAG\_TUPLE**
</dt> <dd> <dl> <dt>

8627 (0x21B3)
</dt> <dt>



The search flags for the attribute are invalid. The tuple index bit is valid only on attributes of Unicode strings.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_HIERARCHY_TABLE_TOO_DEEP"></span><span id="error_ds_hierarchy_table_too_deep"></span>**ERROR\_DS\_HIERARCHY\_TABLE\_TOO\_DEEP**
</dt> <dd> <dl> <dt>

8628 (0x21B4)
</dt> <dt>



The address books are nested too deeply. Failed to build the hierarchy table.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DRA_CORRUPT_UTD_VECTOR"></span><span id="error_ds_dra_corrupt_utd_vector"></span>**ERROR\_DS\_DRA\_CORRUPT\_UTD\_VECTOR**
</dt> <dd> <dl> <dt>

8629 (0x21B5)
</dt> <dt>



The specified up-to-date-ness vector is corrupt.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DRA_SECRETS_DENIED"></span><span id="error_ds_dra_secrets_denied"></span>**ERROR\_DS\_DRA\_SECRETS\_DENIED**
</dt> <dd> <dl> <dt>

8630 (0x21B6)
</dt> <dt>



The request to replicate secrets is denied.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_RESERVED_MAPI_ID"></span><span id="error_ds_reserved_mapi_id"></span>**ERROR\_DS\_RESERVED\_MAPI\_ID**
</dt> <dd> <dl> <dt>

8631 (0x21B7)
</dt> <dt>



Schema update failed: The MAPI identifier is reserved.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_MAPI_ID_NOT_AVAILABLE"></span><span id="error_ds_mapi_id_not_available"></span>**ERROR\_DS\_MAPI\_ID\_NOT\_AVAILABLE**
</dt> <dd> <dl> <dt>

8632 (0x21B8)
</dt> <dt>



Schema update failed: There are no MAPI identifiers available.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DRA_MISSING_KRBTGT_SECRET"></span><span id="error_ds_dra_missing_krbtgt_secret"></span>**ERROR\_DS\_DRA\_MISSING\_KRBTGT\_SECRET**
</dt> <dd> <dl> <dt>

8633 (0x21B9)
</dt> <dt>



The replication operation failed because the required attributes of the local krbtgt object are missing.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DOMAIN_NAME_EXISTS_IN_FOREST"></span><span id="error_ds_domain_name_exists_in_forest"></span>**ERROR\_DS\_DOMAIN\_NAME\_EXISTS\_IN\_FOREST**
</dt> <dd> <dl> <dt>

8634 (0x21BA)
</dt> <dt>



The domain name of the trusted domain already exists in the forest.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_FLAT_NAME_EXISTS_IN_FOREST"></span><span id="error_ds_flat_name_exists_in_forest"></span>**ERROR\_DS\_FLAT\_NAME\_EXISTS\_IN\_FOREST**
</dt> <dd> <dl> <dt>

8635 (0x21BB)
</dt> <dt>



The flat name of the trusted domain already exists in the forest.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_USER_PRINCIPAL_NAME"></span><span id="error_invalid_user_principal_name"></span>**ERROR\_INVALID\_USER\_PRINCIPAL\_NAME**
</dt> <dd> <dl> <dt>

8636 (0x21BC)
</dt> <dt>



The User Principal Name (UPN) is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_OID_MAPPED_GROUP_CANT_HAVE_MEMBERS"></span><span id="error_ds_oid_mapped_group_cant_have_members"></span>**ERROR\_DS\_OID\_MAPPED\_GROUP\_CANT\_HAVE\_MEMBERS**
</dt> <dd> <dl> <dt>

8637 (0x21BD)
</dt> <dt>



OID mapped groups cannot have members.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_OID_NOT_FOUND"></span><span id="error_ds_oid_not_found"></span>**ERROR\_DS\_OID\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

8638 (0x21BE)
</dt> <dt>



The specified OID cannot be found.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DRA_RECYCLED_TARGET"></span><span id="error_ds_dra_recycled_target"></span>**ERROR\_DS\_DRA\_RECYCLED\_TARGET**
</dt> <dd> <dl> <dt>

8639 (0x21BF)
</dt> <dt>



The replication operation failed because the target object referred by a link value is recycled.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_DISALLOWED_NC_REDIRECT"></span><span id="error_ds_disallowed_nc_redirect"></span>**ERROR\_DS\_DISALLOWED\_NC\_REDIRECT**
</dt> <dd> <dl> <dt>

8640 (0x21C0)
</dt> <dt>



The redirect operation failed because the target object is in a NC different from the domain NC of the current domain controller.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_HIGH_ADLDS_FFL"></span><span id="error_ds_high_adlds_ffl"></span>**ERROR\_DS\_HIGH\_ADLDS\_FFL**
</dt> <dd> <dl> <dt>

8641 (0x21C1)
</dt> <dt>



The functional level of the AD LDS configuration set cannot be lowered to the requested value.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_HIGH_DSA_VERSION"></span><span id="error_ds_high_dsa_version"></span>**ERROR\_DS\_HIGH\_DSA\_VERSION**
</dt> <dd> <dl> <dt>

8642 (0x21C2)
</dt> <dt>



The functional level of the domain (or forest) cannot be lowered to the requested value.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_LOW_ADLDS_FFL"></span><span id="error_ds_low_adlds_ffl"></span>**ERROR\_DS\_LOW\_ADLDS\_FFL**
</dt> <dd> <dl> <dt>

8643 (0x21C3)
</dt> <dt>



The functional level of the AD LDS configuration set cannot be raised to the requested value, because there exist one or more ADLDS instances that are at a lower incompatible functional level.


</dt> </dl> </dd> <dt>

<span id="ERROR_DOMAIN_SID_SAME_AS_LOCAL_WORKSTATION"></span><span id="error_domain_sid_same_as_local_workstation"></span>**ERROR\_DOMAIN\_SID\_SAME\_AS\_LOCAL\_WORKSTATION**
</dt> <dd> <dl> <dt>

8644 (0x21C4)
</dt> <dt>



The domain join cannot be completed because the SID of the domain you attempted to join was identical to the SID of this machine. This is a symptom of an improperly cloned operating system install. You should run sysprep on this machine in order to generate a new machine SID. Please see <https://go.microsoft.com/fwlink/p/?linkid=168895> for more information.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_UNDELETE_SAM_VALIDATION_FAILED"></span><span id="error_ds_undelete_sam_validation_failed"></span>**ERROR\_DS\_UNDELETE\_SAM\_VALIDATION\_FAILED**
</dt> <dd> <dl> <dt>

8645 (0x21C5)
</dt> <dt>



The undelete operation failed because the Sam Account Name or Additional Sam Account Name of the object being undeleted conflicts with an existing live object.


</dt> </dl> </dd> <dt>

<span id="ERROR_INCORRECT_ACCOUNT_TYPE"></span><span id="error_incorrect_account_type"></span>**ERROR\_INCORRECT\_ACCOUNT\_TYPE**
</dt> <dd> <dl> <dt>

8646 (0x21C6)
</dt> <dt>



The system is not authoritative for the specified account and therefore cannot complete the operation. Please retry the operation using the provider associated with this account. If this is an online provider please use the provider's online site.


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

 

 




