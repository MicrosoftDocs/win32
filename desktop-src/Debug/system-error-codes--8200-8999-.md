---
description: Describes error codes 8200-8999 defined in the WinError.h header file and is intended for developers.
ms.assetid: f16fdfa3-b080-47ee-a7dd-241fe2d24278
title: System Error Codes (8200-8999) (WinError.h)
ms.topic: reference
ms.date: 07/15/2024
---

# System Error Codes (8200-8999)

The following list describes [system error codes](system-error-codes.md) for errors 8200 to 8999. They are returned by the [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) function when many functions fail. To retrieve the description text for the error in your application, use the [**FormatMessage**](/windows/desktop/api/WinBase/nf-winbase-formatmessage) function with the **FORMAT\_MESSAGE\_FROM\_SYSTEM** flag.

> [!NOTE]
> This information is intended for developers debugging system errors. For other errors, such as issues with Windows Update, see the list of resources on the [Error codes](system-error-codes.md) page.

 

<span id="ERROR_DS_NOT_INSTALLED"></span><span id="error_ds_not_installed"></span>**ERROR\_DS\_NOT\_INSTALLED**
   

8200 (0x2008)
 



An error occurred while installing the directory service. For more information, see the event log.


   

<span id="ERROR_DS_MEMBERSHIP_EVALUATED_LOCALLY"></span><span id="error_ds_membership_evaluated_locally"></span>**ERROR\_DS\_MEMBERSHIP\_EVALUATED\_LOCALLY**
   

8201 (0x2009)
 



The directory service evaluated group memberships locally.


   

<span id="ERROR_DS_NO_ATTRIBUTE_OR_VALUE"></span><span id="error_ds_no_attribute_or_value"></span>**ERROR\_DS\_NO\_ATTRIBUTE\_OR\_VALUE**
   

8202 (0x200A)
 



The specified directory service attribute or value does not exist.


   

<span id="ERROR_DS_INVALID_ATTRIBUTE_SYNTAX"></span><span id="error_ds_invalid_attribute_syntax"></span>**ERROR\_DS\_INVALID\_ATTRIBUTE\_SYNTAX**
   

8203 (0x200B)
 



The attribute syntax specified to the directory service is invalid.


   

<span id="ERROR_DS_ATTRIBUTE_TYPE_UNDEFINED"></span><span id="error_ds_attribute_type_undefined"></span>**ERROR\_DS\_ATTRIBUTE\_TYPE\_UNDEFINED**
   

8204 (0x200C)
 



The attribute type specified to the directory service is not defined.


   

<span id="ERROR_DS_ATTRIBUTE_OR_VALUE_EXISTS"></span><span id="error_ds_attribute_or_value_exists"></span>**ERROR\_DS\_ATTRIBUTE\_OR\_VALUE\_EXISTS**
   

8205 (0x200D)
 



The specified directory service attribute or value already exists.


   

<span id="ERROR_DS_BUSY"></span><span id="error_ds_busy"></span>**ERROR\_DS\_BUSY**
   

8206 (0x200E)
 



The directory service is busy.


   

<span id="ERROR_DS_UNAVAILABLE"></span><span id="error_ds_unavailable"></span>**ERROR\_DS\_UNAVAILABLE**
   

8207 (0x200F)
 



The directory service is unavailable.


   

<span id="ERROR_DS_NO_RIDS_ALLOCATED"></span><span id="error_ds_no_rids_allocated"></span>**ERROR\_DS\_NO\_RIDS\_ALLOCATED**
   

8208 (0x2010)
 



The directory service was unable to allocate a relative identifier.


   

<span id="ERROR_DS_NO_MORE_RIDS"></span><span id="error_ds_no_more_rids"></span>**ERROR\_DS\_NO\_MORE\_RIDS**
   

8209 (0x2011)
 



The directory service has exhausted the pool of relative identifiers.


   

<span id="ERROR_DS_INCORRECT_ROLE_OWNER"></span><span id="error_ds_incorrect_role_owner"></span>**ERROR\_DS\_INCORRECT\_ROLE\_OWNER**
   

8210 (0x2012)
 



The requested operation could not be performed because the directory service is not the master for that type of operation.


   

<span id="ERROR_DS_RIDMGR_INIT_ERROR"></span><span id="error_ds_ridmgr_init_error"></span>**ERROR\_DS\_RIDMGR\_INIT\_ERROR**
   

8211 (0x2013)
 



The directory service was unable to initialize the subsystem that allocates relative identifiers.


   

<span id="ERROR_DS_OBJ_CLASS_VIOLATION"></span><span id="error_ds_obj_class_violation"></span>**ERROR\_DS\_OBJ\_CLASS\_VIOLATION**
   

8212 (0x2014)
 



The requested operation did not satisfy one or more constraints associated with the class of the object.


   

<span id="ERROR_DS_CANT_ON_NON_LEAF"></span><span id="error_ds_cant_on_non_leaf"></span>**ERROR\_DS\_CANT\_ON\_NON\_LEAF**
   

8213 (0x2015)
 



The directory service can perform the requested operation only on a leaf object.


   

<span id="ERROR_DS_CANT_ON_RDN"></span><span id="error_ds_cant_on_rdn"></span>**ERROR\_DS\_CANT\_ON\_RDN**
   

8214 (0x2016)
 



The directory service cannot perform the requested operation on the RDN attribute of an object.


   

<span id="ERROR_DS_CANT_MOD_OBJ_CLASS"></span><span id="error_ds_cant_mod_obj_class"></span>**ERROR\_DS\_CANT\_MOD\_OBJ\_CLASS**
   

8215 (0x2017)
 



The directory service detected an attempt to modify the object class of an object.


   

<span id="ERROR_DS_CROSS_DOM_MOVE_ERROR"></span><span id="error_ds_cross_dom_move_error"></span>**ERROR\_DS\_CROSS\_DOM\_MOVE\_ERROR**
   

8216 (0x2018)
 



The requested cross-domain move operation could not be performed.


   

<span id="ERROR_DS_GC_NOT_AVAILABLE"></span><span id="error_ds_gc_not_available"></span>**ERROR\_DS\_GC\_NOT\_AVAILABLE**
   

8217 (0x2019)
 



Unable to contact the global catalog server.


   

<span id="ERROR_SHARED_POLICY"></span><span id="error_shared_policy"></span>**ERROR\_SHARED\_POLICY**
   

8218 (0x201A)
 



The policy object is shared and can only be modified at the root.


   

<span id="ERROR_POLICY_OBJECT_NOT_FOUND"></span><span id="error_policy_object_not_found"></span>**ERROR\_POLICY\_OBJECT\_NOT\_FOUND**
   

8219 (0x201B)
 



The policy object does not exist.


   

<span id="ERROR_POLICY_ONLY_IN_DS"></span><span id="error_policy_only_in_ds"></span>**ERROR\_POLICY\_ONLY\_IN\_DS**
   

8220 (0x201C)
 



The requested policy information is only in the directory service.


   

<span id="ERROR_PROMOTION_ACTIVE"></span><span id="error_promotion_active"></span>**ERROR\_PROMOTION\_ACTIVE**
   

8221 (0x201D)
 



A domain controller promotion is currently active.


   

<span id="ERROR_NO_PROMOTION_ACTIVE"></span><span id="error_no_promotion_active"></span>**ERROR\_NO\_PROMOTION\_ACTIVE**
   

8222 (0x201E)
 



A domain controller promotion is not currently active.


   

<span id="ERROR_DS_OPERATIONS_ERROR"></span><span id="error_ds_operations_error"></span>**ERROR\_DS\_OPERATIONS\_ERROR**
   

8224 (0x2020)
 



An operations error occurred.


   

<span id="ERROR_DS_PROTOCOL_ERROR"></span><span id="error_ds_protocol_error"></span>**ERROR\_DS\_PROTOCOL\_ERROR**
   

8225 (0x2021)
 



A protocol error occurred.


   

<span id="ERROR_DS_TIMELIMIT_EXCEEDED"></span><span id="error_ds_timelimit_exceeded"></span>**ERROR\_DS\_TIMELIMIT\_EXCEEDED**
   

8226 (0x2022)
 



The time limit for this request was exceeded.


   

<span id="ERROR_DS_SIZELIMIT_EXCEEDED"></span><span id="error_ds_sizelimit_exceeded"></span>**ERROR\_DS\_SIZELIMIT\_EXCEEDED**
   

8227 (0x2023)
 



The size limit for this request was exceeded.


   

<span id="ERROR_DS_ADMIN_LIMIT_EXCEEDED"></span><span id="error_ds_admin_limit_exceeded"></span>**ERROR\_DS\_ADMIN\_LIMIT\_EXCEEDED**
   

8228 (0x2024)
 



The administrative limit for this request was exceeded.


   

<span id="ERROR_DS_COMPARE_FALSE"></span><span id="error_ds_compare_false"></span>**ERROR\_DS\_COMPARE\_FALSE**
   

8229 (0x2025)
 



The compare response was false.


   

<span id="ERROR_DS_COMPARE_TRUE"></span><span id="error_ds_compare_true"></span>**ERROR\_DS\_COMPARE\_TRUE**
   

8230 (0x2026)
 



The compare response was true.


   

<span id="ERROR_DS_AUTH_METHOD_NOT_SUPPORTED"></span><span id="error_ds_auth_method_not_supported"></span>**ERROR\_DS\_AUTH\_METHOD\_NOT\_SUPPORTED**
   

8231 (0x2027)
 



The requested authentication method is not supported by the server.


   

<span id="ERROR_DS_STRONG_AUTH_REQUIRED"></span><span id="error_ds_strong_auth_required"></span>**ERROR\_DS\_STRONG\_AUTH\_REQUIRED**
   

8232 (0x2028)
 



A more secure authentication method is required for this server.


   

<span id="ERROR_DS_INAPPROPRIATE_AUTH"></span><span id="error_ds_inappropriate_auth"></span>**ERROR\_DS\_INAPPROPRIATE\_AUTH**
   

8233 (0x2029)
 



Inappropriate authentication.


   

<span id="ERROR_DS_AUTH_UNKNOWN"></span><span id="error_ds_auth_unknown"></span>**ERROR\_DS\_AUTH\_UNKNOWN**
   

8234 (0x202A)
 



The authentication mechanism is unknown.


   

<span id="ERROR_DS_REFERRAL"></span><span id="error_ds_referral"></span>**ERROR\_DS\_REFERRAL**
   

8235 (0x202B)
 



A referral was returned from the server.


   

<span id="ERROR_DS_UNAVAILABLE_CRIT_EXTENSION"></span><span id="error_ds_unavailable_crit_extension"></span>**ERROR\_DS\_UNAVAILABLE\_CRIT\_EXTENSION**
   

8236 (0x202C)
 



The server does not support the requested critical extension.


   

<span id="ERROR_DS_CONFIDENTIALITY_REQUIRED"></span><span id="error_ds_confidentiality_required"></span>**ERROR\_DS\_CONFIDENTIALITY\_REQUIRED**
   

8237 (0x202D)
 



This request requires a secure connection.


   

<span id="ERROR_DS_INAPPROPRIATE_MATCHING"></span><span id="error_ds_inappropriate_matching"></span>**ERROR\_DS\_INAPPROPRIATE\_MATCHING**
   

8238 (0x202E)
 



Inappropriate matching.


   

<span id="ERROR_DS_CONSTRAINT_VIOLATION"></span><span id="error_ds_constraint_violation"></span>**ERROR\_DS\_CONSTRAINT\_VIOLATION**
   

8239 (0x202F)
 



A constraint violation occurred.


   

<span id="ERROR_DS_NO_SUCH_OBJECT"></span><span id="error_ds_no_such_object"></span>**ERROR\_DS\_NO\_SUCH\_OBJECT**
   

8240 (0x2030)
 



There is no such object on the server.


   

<span id="ERROR_DS_ALIAS_PROBLEM"></span><span id="error_ds_alias_problem"></span>**ERROR\_DS\_ALIAS\_PROBLEM**
   

8241 (0x2031)
 



There is an alias problem.


   

<span id="ERROR_DS_INVALID_DN_SYNTAX"></span><span id="error_ds_invalid_dn_syntax"></span>**ERROR\_DS\_INVALID\_DN\_SYNTAX**
   

8242 (0x2032)
 



An invalid dn syntax has been specified.


   

<span id="ERROR_DS_IS_LEAF"></span><span id="error_ds_is_leaf"></span>**ERROR\_DS\_IS\_LEAF**
   

8243 (0x2033)
 



The object is a leaf object.


   

<span id="ERROR_DS_ALIAS_DEREF_PROBLEM"></span><span id="error_ds_alias_deref_problem"></span>**ERROR\_DS\_ALIAS\_DEREF\_PROBLEM**
   

8244 (0x2034)
 



There is an alias dereferencing problem.


   

<span id="ERROR_DS_UNWILLING_TO_PERFORM"></span><span id="error_ds_unwilling_to_perform"></span>**ERROR\_DS\_UNWILLING\_TO\_PERFORM**
   

8245 (0x2035)
 



The server is unwilling to process the request.


   

<span id="ERROR_DS_LOOP_DETECT"></span><span id="error_ds_loop_detect"></span>**ERROR\_DS\_LOOP\_DETECT**
   

8246 (0x2036)
 



A loop has been detected.


   

<span id="ERROR_DS_NAMING_VIOLATION"></span><span id="error_ds_naming_violation"></span>**ERROR\_DS\_NAMING\_VIOLATION**
   

8247 (0x2037)
 



There is a naming violation.


   

<span id="ERROR_DS_OBJECT_RESULTS_TOO_LARGE"></span><span id="error_ds_object_results_too_large"></span>**ERROR\_DS\_OBJECT\_RESULTS\_TOO\_LARGE**
   

8248 (0x2038)
 



The result set is too large.


   

<span id="ERROR_DS_AFFECTS_MULTIPLE_DSAS"></span><span id="error_ds_affects_multiple_dsas"></span>**ERROR\_DS\_AFFECTS\_MULTIPLE\_DSAS**
   

8249 (0x2039)
 



The operation affects multiple DSAs.


   

<span id="ERROR_DS_SERVER_DOWN"></span><span id="error_ds_server_down"></span>**ERROR\_DS\_SERVER\_DOWN**
   

8250 (0x203A)
 



The server is not operational.


   

<span id="ERROR_DS_LOCAL_ERROR"></span><span id="error_ds_local_error"></span>**ERROR\_DS\_LOCAL\_ERROR**
   

8251 (0x203B)
 



A local error has occurred.


   

<span id="ERROR_DS_ENCODING_ERROR"></span><span id="error_ds_encoding_error"></span>**ERROR\_DS\_ENCODING\_ERROR**
   

8252 (0x203C)
 



An encoding error has occurred.


   

<span id="ERROR_DS_DECODING_ERROR"></span><span id="error_ds_decoding_error"></span>**ERROR\_DS\_DECODING\_ERROR**
   

8253 (0x203D)
 



A decoding error has occurred.


   

<span id="ERROR_DS_FILTER_UNKNOWN"></span><span id="error_ds_filter_unknown"></span>**ERROR\_DS\_FILTER\_UNKNOWN**
   

8254 (0x203E)
 



The search filter cannot be recognized.


   

<span id="ERROR_DS_PARAM_ERROR"></span><span id="error_ds_param_error"></span>**ERROR\_DS\_PARAM\_ERROR**
   

8255 (0x203F)
 



One or more parameters are illegal.


   

<span id="ERROR_DS_NOT_SUPPORTED"></span><span id="error_ds_not_supported"></span>**ERROR\_DS\_NOT\_SUPPORTED**
   

8256 (0x2040)
 



The specified method is not supported.


   

<span id="ERROR_DS_NO_RESULTS_RETURNED"></span><span id="error_ds_no_results_returned"></span>**ERROR\_DS\_NO\_RESULTS\_RETURNED**
   

8257 (0x2041)
 



No results were returned.


   

<span id="ERROR_DS_CONTROL_NOT_FOUND"></span><span id="error_ds_control_not_found"></span>**ERROR\_DS\_CONTROL\_NOT\_FOUND**
   

8258 (0x2042)
 



The specified control is not supported by the server.


   

<span id="ERROR_DS_CLIENT_LOOP"></span><span id="error_ds_client_loop"></span>**ERROR\_DS\_CLIENT\_LOOP**
   

8259 (0x2043)
 



A referral loop was detected by the client.


   

<span id="ERROR_DS_REFERRAL_LIMIT_EXCEEDED"></span><span id="error_ds_referral_limit_exceeded"></span>**ERROR\_DS\_REFERRAL\_LIMIT\_EXCEEDED**
   

8260 (0x2044)
 



The preset referral limit was exceeded.


   

<span id="ERROR_DS_SORT_CONTROL_MISSING"></span><span id="error_ds_sort_control_missing"></span>**ERROR\_DS\_SORT\_CONTROL\_MISSING**
   

8261 (0x2045)
 



The search requires a SORT control.


   

<span id="ERROR_DS_OFFSET_RANGE_ERROR"></span><span id="error_ds_offset_range_error"></span>**ERROR\_DS\_OFFSET\_RANGE\_ERROR**
   

8262 (0x2046)
 



The search results exceed the offset range specified.


   

<span id="ERROR_DS_RIDMGR_DISABLED"></span><span id="error_ds_ridmgr_disabled"></span>**ERROR\_DS\_RIDMGR\_DISABLED**
   

8263 (0x2047)
 



The directory service detected the subsystem that allocates relative identifiers is disabled. This can occur as a protective mechanism when the system determines a significant portion of relative identifiers (RIDs) have been exhausted. Please see <https://go.microsoft.com/fwlink/p/?linkid=228610> for recommended diagnostic steps and the procedure to re-enable account creation.


   

<span id="ERROR_DS_ROOT_MUST_BE_NC"></span><span id="error_ds_root_must_be_nc"></span>**ERROR\_DS\_ROOT\_MUST\_BE\_NC**
   

8301 (0x206D)
 



The root object must be the head of a naming context. The root object cannot have an instantiated parent.


   

<span id="ERROR_DS_ADD_REPLICA_INHIBITED"></span><span id="error_ds_add_replica_inhibited"></span>**ERROR\_DS\_ADD\_REPLICA\_INHIBITED**
   

8302 (0x206E)
 



The add replica operation cannot be performed. The naming context must be writeable in order to create the replica.


   

<span id="ERROR_DS_ATT_NOT_DEF_IN_SCHEMA"></span><span id="error_ds_att_not_def_in_schema"></span>**ERROR\_DS\_ATT\_NOT\_DEF\_IN\_SCHEMA**
   

8303 (0x206F)
 



A reference to an attribute that is not defined in the schema occurred.


   

<span id="ERROR_DS_MAX_OBJ_SIZE_EXCEEDED"></span><span id="error_ds_max_obj_size_exceeded"></span>**ERROR\_DS\_MAX\_OBJ\_SIZE\_EXCEEDED**
   

8304 (0x2070)
 



The maximum size of an object has been exceeded.


   

<span id="ERROR_DS_OBJ_STRING_NAME_EXISTS"></span><span id="error_ds_obj_string_name_exists"></span>**ERROR\_DS\_OBJ\_STRING\_NAME\_EXISTS**
   

8305 (0x2071)
 



An attempt was made to add an object to the directory with a name that is already in use.


   

<span id="ERROR_DS_NO_RDN_DEFINED_IN_SCHEMA"></span><span id="error_ds_no_rdn_defined_in_schema"></span>**ERROR\_DS\_NO\_RDN\_DEFINED\_IN\_SCHEMA**
   

8306 (0x2072)
 



An attempt was made to add an object of a class that does not have an RDN defined in the schema.


   

<span id="ERROR_DS_RDN_DOESNT_MATCH_SCHEMA"></span><span id="error_ds_rdn_doesnt_match_schema"></span>**ERROR\_DS\_RDN\_DOESNT\_MATCH\_SCHEMA**
   

8307 (0x2073)
 



An attempt was made to add an object using an RDN that is not the RDN defined in the schema.


   

<span id="ERROR_DS_NO_REQUESTED_ATTS_FOUND"></span><span id="error_ds_no_requested_atts_found"></span>**ERROR\_DS\_NO\_REQUESTED\_ATTS\_FOUND**
   

8308 (0x2074)
 



None of the requested attributes were found on the objects.


   

<span id="ERROR_DS_USER_BUFFER_TO_SMALL"></span><span id="error_ds_user_buffer_to_small"></span>**ERROR\_DS\_USER\_BUFFER\_TO\_SMALL**
   

8309 (0x2075)
 



The user buffer is too small.


   

<span id="ERROR_DS_ATT_IS_NOT_ON_OBJ"></span><span id="error_ds_att_is_not_on_obj"></span>**ERROR\_DS\_ATT\_IS\_NOT\_ON\_OBJ**
   

8310 (0x2076)
 



The attribute specified in the operation is not present on the object.


   

<span id="ERROR_DS_ILLEGAL_MOD_OPERATION"></span><span id="error_ds_illegal_mod_operation"></span>**ERROR\_DS\_ILLEGAL\_MOD\_OPERATION**
   

8311 (0x2077)
 



Illegal modify operation. Some aspect of the modification is not permitted.


   

<span id="ERROR_DS_OBJ_TOO_LARGE"></span><span id="error_ds_obj_too_large"></span>**ERROR\_DS\_OBJ\_TOO\_LARGE**
   

8312 (0x2078)
 



The specified object is too large.


   

<span id="ERROR_DS_BAD_INSTANCE_TYPE"></span><span id="error_ds_bad_instance_type"></span>**ERROR\_DS\_BAD\_INSTANCE\_TYPE**
   

8313 (0x2079)
 



The specified instance type is not valid.


   

<span id="ERROR_DS_MASTERDSA_REQUIRED"></span><span id="error_ds_masterdsa_required"></span>**ERROR\_DS\_MASTERDSA\_REQUIRED**
   

8314 (0x207A)
 



The operation must be performed at a master DSA.


   

<span id="ERROR_DS_OBJECT_CLASS_REQUIRED"></span><span id="error_ds_object_class_required"></span>**ERROR\_DS\_OBJECT\_CLASS\_REQUIRED**
   

8315 (0x207B)
 



The object class attribute must be specified.


   

<span id="ERROR_DS_MISSING_REQUIRED_ATT"></span><span id="error_ds_missing_required_att"></span>**ERROR\_DS\_MISSING\_REQUIRED\_ATT**
   

8316 (0x207C)
 



A required attribute is missing.


   

<span id="ERROR_DS_ATT_NOT_DEF_FOR_CLASS"></span><span id="error_ds_att_not_def_for_class"></span>**ERROR\_DS\_ATT\_NOT\_DEF\_FOR\_CLASS**
   

8317 (0x207D)
 



An attempt was made to modify an object to include an attribute that is not legal for its class.


   

<span id="ERROR_DS_ATT_ALREADY_EXISTS"></span><span id="error_ds_att_already_exists"></span>**ERROR\_DS\_ATT\_ALREADY\_EXISTS**
   

8318 (0x207E)
 



The specified attribute is already present on the object.


   

<span id="ERROR_DS_CANT_ADD_ATT_VALUES"></span><span id="error_ds_cant_add_att_values"></span>**ERROR\_DS\_CANT\_ADD\_ATT\_VALUES**
   

8320 (0x2080)
 



The specified attribute is not present, or has no values.


   

<span id="ERROR_DS_SINGLE_VALUE_CONSTRAINT"></span><span id="error_ds_single_value_constraint"></span>**ERROR\_DS\_SINGLE\_VALUE\_CONSTRAINT**
   

8321 (0x2081)
 



Multiple values were specified for an attribute that can have only one value.


   

<span id="ERROR_DS_RANGE_CONSTRAINT"></span><span id="error_ds_range_constraint"></span>**ERROR\_DS\_RANGE\_CONSTRAINT**
   

8322 (0x2082)
 



A value for the attribute was not in the acceptable range of values.


   

<span id="ERROR_DS_ATT_VAL_ALREADY_EXISTS"></span><span id="error_ds_att_val_already_exists"></span>**ERROR\_DS\_ATT\_VAL\_ALREADY\_EXISTS**
   

8323 (0x2083)
 



The specified value already exists.


   

<span id="ERROR_DS_CANT_REM_MISSING_ATT"></span><span id="error_ds_cant_rem_missing_att"></span>**ERROR\_DS\_CANT\_REM\_MISSING\_ATT**
   

8324 (0x2084)
 



The attribute cannot be removed because it is not present on the object.


   

<span id="ERROR_DS_CANT_REM_MISSING_ATT_VAL"></span><span id="error_ds_cant_rem_missing_att_val"></span>**ERROR\_DS\_CANT\_REM\_MISSING\_ATT\_VAL**
   

8325 (0x2085)
 



The attribute value cannot be removed because it is not present on the object.


   

<span id="ERROR_DS_ROOT_CANT_BE_SUBREF"></span><span id="error_ds_root_cant_be_subref"></span>**ERROR\_DS\_ROOT\_CANT\_BE\_SUBREF**
   

8326 (0x2086)
 



The specified root object cannot be a subref.


   

<span id="ERROR_DS_NO_CHAINING"></span><span id="error_ds_no_chaining"></span>**ERROR\_DS\_NO\_CHAINING**
   

8327 (0x2087)
 



Chaining is not permitted.


   

<span id="ERROR_DS_NO_CHAINED_EVAL"></span><span id="error_ds_no_chained_eval"></span>**ERROR\_DS\_NO\_CHAINED\_EVAL**
   

8328 (0x2088)
 



Chained evaluation is not permitted.


   

<span id="ERROR_DS_NO_PARENT_OBJECT"></span><span id="error_ds_no_parent_object"></span>**ERROR\_DS\_NO\_PARENT\_OBJECT**
   

8329 (0x2089)
 



The operation could not be performed because the object's parent is either uninstantiated or deleted.


   

<span id="ERROR_DS_PARENT_IS_AN_ALIAS"></span><span id="error_ds_parent_is_an_alias"></span>**ERROR\_DS\_PARENT\_IS\_AN\_ALIAS**
   

8330 (0x208A)
 



Having a parent that is an alias is not permitted. Aliases are leaf objects.


   

<span id="ERROR_DS_CANT_MIX_MASTER_AND_REPS"></span><span id="error_ds_cant_mix_master_and_reps"></span>**ERROR\_DS\_CANT\_MIX\_MASTER\_AND\_REPS**
   

8331 (0x208B)
 



The object and parent must be of the same type, either both masters or both replicas.


   

<span id="ERROR_DS_CHILDREN_EXIST"></span><span id="error_ds_children_exist"></span>**ERROR\_DS\_CHILDREN\_EXIST**
   

8332 (0x208C)
 



The operation cannot be performed because child objects exist. This operation can only be performed on a leaf object.


   

<span id="ERROR_DS_OBJ_NOT_FOUND"></span><span id="error_ds_obj_not_found"></span>**ERROR\_DS\_OBJ\_NOT\_FOUND**
   

8333 (0x208D)
 



Directory object not found.


   

<span id="ERROR_DS_ALIASED_OBJ_MISSING"></span><span id="error_ds_aliased_obj_missing"></span>**ERROR\_DS\_ALIASED\_OBJ\_MISSING**
   

8334 (0x208E)
 



The aliased object is missing.


   

<span id="ERROR_DS_BAD_NAME_SYNTAX"></span><span id="error_ds_bad_name_syntax"></span>**ERROR\_DS\_BAD\_NAME\_SYNTAX**
   

8335 (0x208F)
 



The object name has bad syntax.


   

<span id="ERROR_DS_ALIAS_POINTS_TO_ALIAS"></span><span id="error_ds_alias_points_to_alias"></span>**ERROR\_DS\_ALIAS\_POINTS\_TO\_ALIAS**
   

8336 (0x2090)
 



It is not permitted for an alias to refer to another alias.


   

<span id="ERROR_DS_CANT_DEREF_ALIAS"></span><span id="error_ds_cant_deref_alias"></span>**ERROR\_DS\_CANT\_DEREF\_ALIAS**
   

8337 (0x2091)
 



The alias cannot be dereferenced.


   

<span id="ERROR_DS_OUT_OF_SCOPE"></span><span id="error_ds_out_of_scope"></span>**ERROR\_DS\_OUT\_OF\_SCOPE**
   

8338 (0x2092)
 



The operation is out of scope.


   

<span id="ERROR_DS_OBJECT_BEING_REMOVED"></span><span id="error_ds_object_being_removed"></span>**ERROR\_DS\_OBJECT\_BEING\_REMOVED**
   

8339 (0x2093)
 



The operation cannot continue because the object is in the process of being removed.


   

<span id="ERROR_DS_CANT_DELETE_DSA_OBJ"></span><span id="error_ds_cant_delete_dsa_obj"></span>**ERROR\_DS\_CANT\_DELETE\_DSA\_OBJ**
   

8340 (0x2094)
 



The DSA object cannot be deleted.


   

<span id="ERROR_DS_GENERIC_ERROR"></span><span id="error_ds_generic_error"></span>**ERROR\_DS\_GENERIC\_ERROR**
   

8341 (0x2095)
 



A directory service error has occurred.


   

<span id="ERROR_DS_DSA_MUST_BE_INT_MASTER"></span><span id="error_ds_dsa_must_be_int_master"></span>**ERROR\_DS\_DSA\_MUST\_BE\_INT\_MASTER**
   

8342 (0x2096)
 



The operation can only be performed on an internal master DSA object.


   

<span id="ERROR_DS_CLASS_NOT_DSA"></span><span id="error_ds_class_not_dsa"></span>**ERROR\_DS\_CLASS\_NOT\_DSA**
   

8343 (0x2097)
 



The object must be of class DSA.


   

<span id="ERROR_DS_INSUFF_ACCESS_RIGHTS"></span><span id="error_ds_insuff_access_rights"></span>**ERROR\_DS\_INSUFF\_ACCESS\_RIGHTS**
   

8344 (0x2098)
 



Insufficient access rights to perform the operation.


   

<span id="ERROR_DS_ILLEGAL_SUPERIOR"></span><span id="error_ds_illegal_superior"></span>**ERROR\_DS\_ILLEGAL\_SUPERIOR**
   

8345 (0x2099)
 



The object cannot be added because the parent is not on the list of possible superiors.


   

<span id="ERROR_DS_ATTRIBUTE_OWNED_BY_SAM"></span><span id="error_ds_attribute_owned_by_sam"></span>**ERROR\_DS\_ATTRIBUTE\_OWNED\_BY\_SAM**
   

8346 (0x209A)
 



Access to the attribute is not permitted because the attribute is owned by the Security Accounts Manager (SAM).


   

<span id="ERROR_DS_NAME_TOO_MANY_PARTS"></span><span id="error_ds_name_too_many_parts"></span>**ERROR\_DS\_NAME\_TOO\_MANY\_PARTS**
   

8347 (0x209B)
 



The name has too many parts.


   

<span id="ERROR_DS_NAME_TOO_LONG"></span><span id="error_ds_name_too_long"></span>**ERROR\_DS\_NAME\_TOO\_LONG**
   

8348 (0x209C)
 



The name is too long.


   

<span id="ERROR_DS_NAME_VALUE_TOO_LONG"></span><span id="error_ds_name_value_too_long"></span>**ERROR\_DS\_NAME\_VALUE\_TOO\_LONG**
   

8349 (0x209D)
 



The name value is too long.


   

<span id="ERROR_DS_NAME_UNPARSEABLE"></span><span id="error_ds_name_unparseable"></span>**ERROR\_DS\_NAME\_UNPARSEABLE**
   

8350 (0x209E)
 



The directory service encountered an error parsing a name.


   

<span id="ERROR_DS_NAME_TYPE_UNKNOWN"></span><span id="error_ds_name_type_unknown"></span>**ERROR\_DS\_NAME\_TYPE\_UNKNOWN**
   

8351 (0x209F)
 



The directory service cannot get the attribute type for a name.


   

<span id="ERROR_DS_NOT_AN_OBJECT"></span><span id="error_ds_not_an_object"></span>**ERROR\_DS\_NOT\_AN\_OBJECT**
   

8352 (0x20A0)
 



The name does not identify an object; the name identifies a phantom.


   

<span id="ERROR_DS_SEC_DESC_TOO_SHORT"></span><span id="error_ds_sec_desc_too_short"></span>**ERROR\_DS\_SEC\_DESC\_TOO\_SHORT**
   

8353 (0x20A1)
 



The security descriptor is too short.


   

<span id="ERROR_DS_SEC_DESC_INVALID"></span><span id="error_ds_sec_desc_invalid"></span>**ERROR\_DS\_SEC\_DESC\_INVALID**
   

8354 (0x20A2)
 



The security descriptor is invalid.


   

<span id="ERROR_DS_NO_DELETED_NAME"></span><span id="error_ds_no_deleted_name"></span>**ERROR\_DS\_NO\_DELETED\_NAME**
   

8355 (0x20A3)
 



Failed to create name for deleted object.


   

<span id="ERROR_DS_SUBREF_MUST_HAVE_PARENT"></span><span id="error_ds_subref_must_have_parent"></span>**ERROR\_DS\_SUBREF\_MUST\_HAVE\_PARENT**
   

8356 (0x20A4)
 



The parent of a new subref must exist.


   

<span id="ERROR_DS_NCNAME_MUST_BE_NC"></span><span id="error_ds_ncname_must_be_nc"></span>**ERROR\_DS\_NCNAME\_MUST\_BE\_NC**
   

8357 (0x20A5)
 



The object must be a naming context.


   

<span id="ERROR_DS_CANT_ADD_SYSTEM_ONLY"></span><span id="error_ds_cant_add_system_only"></span>**ERROR\_DS\_CANT\_ADD\_SYSTEM\_ONLY**
   

8358 (0x20A6)
 



It is not permitted to add an attribute which is owned by the system.


   

<span id="ERROR_DS_CLASS_MUST_BE_CONCRETE"></span><span id="error_ds_class_must_be_concrete"></span>**ERROR\_DS\_CLASS\_MUST\_BE\_CONCRETE**
   

8359 (0x20A7)
 



The class of the object must be structural; you cannot instantiate an abstract class.


   

<span id="ERROR_DS_INVALID_DMD"></span><span id="error_ds_invalid_dmd"></span>**ERROR\_DS\_INVALID\_DMD**
   

8360 (0x20A8)
 



The schema object could not be found.


   

<span id="ERROR_DS_OBJ_GUID_EXISTS"></span><span id="error_ds_obj_guid_exists"></span>**ERROR\_DS\_OBJ\_GUID\_EXISTS**
   

8361 (0x20A9)
 



A local object with this GUID (dead or alive) already exists.


   

<span id="ERROR_DS_NOT_ON_BACKLINK"></span><span id="error_ds_not_on_backlink"></span>**ERROR\_DS\_NOT\_ON\_BACKLINK**
   

8362 (0x20AA)
 



The operation cannot be performed on a back link.


   

<span id="ERROR_DS_NO_CROSSREF_FOR_NC"></span><span id="error_ds_no_crossref_for_nc"></span>**ERROR\_DS\_NO\_CROSSREF\_FOR\_NC**
   

8363 (0x20AB)
 



The cross reference for the specified naming context could not be found.


   

<span id="ERROR_DS_SHUTTING_DOWN"></span><span id="error_ds_shutting_down"></span>**ERROR\_DS\_SHUTTING\_DOWN**
   

8364 (0x20AC)
 



The operation could not be performed because the directory service is shutting down.


   

<span id="ERROR_DS_UNKNOWN_OPERATION"></span><span id="error_ds_unknown_operation"></span>**ERROR\_DS\_UNKNOWN\_OPERATION**
   

8365 (0x20AD)
 



The directory service request is invalid.


   

<span id="ERROR_DS_INVALID_ROLE_OWNER"></span><span id="error_ds_invalid_role_owner"></span>**ERROR\_DS\_INVALID\_ROLE\_OWNER**
   

8366 (0x20AE)
 



The role owner attribute could not be read.


   

<span id="ERROR_DS_COULDNT_CONTACT_FSMO"></span><span id="error_ds_couldnt_contact_fsmo"></span>**ERROR\_DS\_COULDNT\_CONTACT\_FSMO**
   

8367 (0x20AF)
 



The requested FSMO operation failed. The current FSMO holder could not be contacted.


   

<span id="ERROR_DS_CROSS_NC_DN_RENAME"></span><span id="error_ds_cross_nc_dn_rename"></span>**ERROR\_DS\_CROSS\_NC\_DN\_RENAME**
   

8368 (0x20B0)
 



Modification of a DN across a naming context is not permitted.


   

<span id="ERROR_DS_CANT_MOD_SYSTEM_ONLY"></span><span id="error_ds_cant_mod_system_only"></span>**ERROR\_DS\_CANT\_MOD\_SYSTEM\_ONLY**
   

8369 (0x20B1)
 



The attribute cannot be modified because it is owned by the system.


   

<span id="ERROR_DS_REPLICATOR_ONLY"></span><span id="error_ds_replicator_only"></span>**ERROR\_DS\_REPLICATOR\_ONLY**
   

8370 (0x20B2)
 



Only the replicator can perform this function.


   

<span id="ERROR_DS_OBJ_CLASS_NOT_DEFINED"></span><span id="error_ds_obj_class_not_defined"></span>**ERROR\_DS\_OBJ\_CLASS\_NOT\_DEFINED**
   

8371 (0x20B3)
 



The specified class is not defined.


   

<span id="ERROR_DS_OBJ_CLASS_NOT_SUBCLASS"></span><span id="error_ds_obj_class_not_subclass"></span>**ERROR\_DS\_OBJ\_CLASS\_NOT\_SUBCLASS**
   

8372 (0x20B4)
 



The specified class is not a subclass.


   

<span id="ERROR_DS_NAME_REFERENCE_INVALID"></span><span id="error_ds_name_reference_invalid"></span>**ERROR\_DS\_NAME\_REFERENCE\_INVALID**
   

8373 (0x20B5)
 



The name reference is invalid.


   

<span id="ERROR_DS_CROSS_REF_EXISTS"></span><span id="error_ds_cross_ref_exists"></span>**ERROR\_DS\_CROSS\_REF\_EXISTS**
   

8374 (0x20B6)
 



A cross reference already exists.


   

<span id="ERROR_DS_CANT_DEL_MASTER_CROSSREF"></span><span id="error_ds_cant_del_master_crossref"></span>**ERROR\_DS\_CANT\_DEL\_MASTER\_CROSSREF**
   

8375 (0x20B7)
 



It is not permitted to delete a master cross reference.


   

<span id="ERROR_DS_SUBTREE_NOTIFY_NOT_NC_HEAD"></span><span id="error_ds_subtree_notify_not_nc_head"></span>**ERROR\_DS\_SUBTREE\_NOTIFY\_NOT\_NC\_HEAD**
   

8376 (0x20B8)
 



Subtree notifications are only supported on NC heads.


   

<span id="ERROR_DS_NOTIFY_FILTER_TOO_COMPLEX"></span><span id="error_ds_notify_filter_too_complex"></span>**ERROR\_DS\_NOTIFY\_FILTER\_TOO\_COMPLEX**
   

8377 (0x20B9)
 



Notification filter is too complex.


   

<span id="ERROR_DS_DUP_RDN"></span><span id="error_ds_dup_rdn"></span>**ERROR\_DS\_DUP\_RDN**
   

8378 (0x20BA)
 



Schema update failed: duplicate RDN.


   

<span id="ERROR_DS_DUP_OID"></span><span id="error_ds_dup_oid"></span>**ERROR\_DS\_DUP\_OID**
   

8379 (0x20BB)
 



Schema update failed: duplicate OID.


   

<span id="ERROR_DS_DUP_MAPI_ID"></span><span id="error_ds_dup_mapi_id"></span>**ERROR\_DS\_DUP\_MAPI\_ID**
   

8380 (0x20BC)
 



Schema update failed: duplicate MAPI identifier.


   

<span id="ERROR_DS_DUP_SCHEMA_ID_GUID"></span><span id="error_ds_dup_schema_id_guid"></span>**ERROR\_DS\_DUP\_SCHEMA\_ID\_GUID**
   

8381 (0x20BD)
 



Schema update failed: duplicate schema-id GUID.


   

<span id="ERROR_DS_DUP_LDAP_DISPLAY_NAME"></span><span id="error_ds_dup_ldap_display_name"></span>**ERROR\_DS\_DUP\_LDAP\_DISPLAY\_NAME**
   

8382 (0x20BE)
 



Schema update failed: duplicate LDAP display name.


   

<span id="ERROR_DS_SEMANTIC_ATT_TEST"></span><span id="error_ds_semantic_att_test"></span>**ERROR\_DS\_SEMANTIC\_ATT\_TEST**
   

8383 (0x20BF)
 



Schema update failed: range-lower less than range upper.


   

<span id="ERROR_DS_SYNTAX_MISMATCH"></span><span id="error_ds_syntax_mismatch"></span>**ERROR\_DS\_SYNTAX\_MISMATCH**
   

8384 (0x20C0)
 



Schema update failed: syntax mismatch.


   

<span id="ERROR_DS_EXISTS_IN_MUST_HAVE"></span><span id="error_ds_exists_in_must_have"></span>**ERROR\_DS\_EXISTS\_IN\_MUST\_HAVE**
   

8385 (0x20C1)
 



Schema deletion failed: attribute is used in must-contain.


   

<span id="ERROR_DS_EXISTS_IN_MAY_HAVE"></span><span id="error_ds_exists_in_may_have"></span>**ERROR\_DS\_EXISTS\_IN\_MAY\_HAVE**
   

8386 (0x20C2)
 



Schema deletion failed: attribute is used in may-contain.


   

<span id="ERROR_DS_NONEXISTENT_MAY_HAVE"></span><span id="error_ds_nonexistent_may_have"></span>**ERROR\_DS\_NONEXISTENT\_MAY\_HAVE**
   

8387 (0x20C3)
 



Schema update failed: attribute in may-contain does not exist.


   

<span id="ERROR_DS_NONEXISTENT_MUST_HAVE"></span><span id="error_ds_nonexistent_must_have"></span>**ERROR\_DS\_NONEXISTENT\_MUST\_HAVE**
   

8388 (0x20C4)
 



Schema update failed: attribute in must-contain does not exist.


   

<span id="ERROR_DS_AUX_CLS_TEST_FAIL"></span><span id="error_ds_aux_cls_test_fail"></span>**ERROR\_DS\_AUX\_CLS\_TEST\_FAIL**
   

8389 (0x20C5)
 



Schema update failed: class in aux-class list does not exist or is not an auxiliary class.


   

<span id="ERROR_DS_NONEXISTENT_POSS_SUP"></span><span id="error_ds_nonexistent_poss_sup"></span>**ERROR\_DS\_NONEXISTENT\_POSS\_SUP**
   

8390 (0x20C6)
 



Schema update failed: class in poss-superiors does not exist.


   

<span id="ERROR_DS_SUB_CLS_TEST_FAIL"></span><span id="error_ds_sub_cls_test_fail"></span>**ERROR\_DS\_SUB\_CLS\_TEST\_FAIL**
   

8391 (0x20C7)
 



Schema update failed: class in subclassof list does not exist or does not satisfy hierarchy rules.


   

<span id="ERROR_DS_BAD_RDN_ATT_ID_SYNTAX"></span><span id="error_ds_bad_rdn_att_id_syntax"></span>**ERROR\_DS\_BAD\_RDN\_ATT\_ID\_SYNTAX**
   

8392 (0x20C8)
 



Schema update failed: Rdn-Att-Id has wrong syntax.


   

<span id="ERROR_DS_EXISTS_IN_AUX_CLS"></span><span id="error_ds_exists_in_aux_cls"></span>**ERROR\_DS\_EXISTS\_IN\_AUX\_CLS**
   

8393 (0x20C9)
 



Schema deletion failed: class is used as auxiliary class.


   

<span id="ERROR_DS_EXISTS_IN_SUB_CLS"></span><span id="error_ds_exists_in_sub_cls"></span>**ERROR\_DS\_EXISTS\_IN\_SUB\_CLS**
   

8394 (0x20CA)
 



Schema deletion failed: class is used as sub class.


   

<span id="ERROR_DS_EXISTS_IN_POSS_SUP"></span><span id="error_ds_exists_in_poss_sup"></span>**ERROR\_DS\_EXISTS\_IN\_POSS\_SUP**
   

8395 (0x20CB)
 



Schema deletion failed: class is used as poss superior.


   

<span id="ERROR_DS_RECALCSCHEMA_FAILED"></span><span id="error_ds_recalcschema_failed"></span>**ERROR\_DS\_RECALCSCHEMA\_FAILED**
   

8396 (0x20CC)
 



Schema update failed in recalculating validation cache.


   

<span id="ERROR_DS_TREE_DELETE_NOT_FINISHED"></span><span id="error_ds_tree_delete_not_finished"></span>**ERROR\_DS\_TREE\_DELETE\_NOT\_FINISHED**
   

8397 (0x20CD)
 



The tree deletion is not finished. The request must be made again to continue deleting the tree.


   

<span id="ERROR_DS_CANT_DELETE"></span><span id="error_ds_cant_delete"></span>**ERROR\_DS\_CANT\_DELETE**
   

8398 (0x20CE)
 



The requested delete operation could not be performed.


   

<span id="ERROR_DS_ATT_SCHEMA_REQ_ID"></span><span id="error_ds_att_schema_req_id"></span>**ERROR\_DS\_ATT\_SCHEMA\_REQ\_ID**
   

8399 (0x20CF)
 



Cannot read the governs class identifier for the schema record.


   

<span id="ERROR_DS_BAD_ATT_SCHEMA_SYNTAX"></span><span id="error_ds_bad_att_schema_syntax"></span>**ERROR\_DS\_BAD\_ATT\_SCHEMA\_SYNTAX**
   

8400 (0x20D0)
 



The attribute schema has bad syntax.


   

<span id="ERROR_DS_CANT_CACHE_ATT"></span><span id="error_ds_cant_cache_att"></span>**ERROR\_DS\_CANT\_CACHE\_ATT**
   

8401 (0x20D1)
 



The attribute could not be cached.


   

<span id="ERROR_DS_CANT_CACHE_CLASS"></span><span id="error_ds_cant_cache_class"></span>**ERROR\_DS\_CANT\_CACHE\_CLASS**
   

8402 (0x20D2)
 



The class could not be cached.


   

<span id="ERROR_DS_CANT_REMOVE_ATT_CACHE"></span><span id="error_ds_cant_remove_att_cache"></span>**ERROR\_DS\_CANT\_REMOVE\_ATT\_CACHE**
   

8403 (0x20D3)
 



The attribute could not be removed from the cache.


   

<span id="ERROR_DS_CANT_REMOVE_CLASS_CACHE"></span><span id="error_ds_cant_remove_class_cache"></span>**ERROR\_DS\_CANT\_REMOVE\_CLASS\_CACHE**
   

8404 (0x20D4)
 



The class could not be removed from the cache.


   

<span id="ERROR_DS_CANT_RETRIEVE_DN"></span><span id="error_ds_cant_retrieve_dn"></span>**ERROR\_DS\_CANT\_RETRIEVE\_DN**
   

8405 (0x20D5)
 



The distinguished name attribute could not be read.


   

<span id="ERROR_DS_MISSING_SUPREF"></span><span id="error_ds_missing_supref"></span>**ERROR\_DS\_MISSING\_SUPREF**
   

8406 (0x20D6)
 



No superior reference has been configured for the directory service. The directory service is therefore unable to issue referrals to objects outside this forest.


   

<span id="ERROR_DS_CANT_RETRIEVE_INSTANCE"></span><span id="error_ds_cant_retrieve_instance"></span>**ERROR\_DS\_CANT\_RETRIEVE\_INSTANCE**
   

8407 (0x20D7)
 



The instance type attribute could not be retrieved.


   

<span id="ERROR_DS_CODE_INCONSISTENCY"></span><span id="error_ds_code_inconsistency"></span>**ERROR\_DS\_CODE\_INCONSISTENCY**
   

8408 (0x20D8)
 



An internal error has occurred.


   

<span id="ERROR_DS_DATABASE_ERROR"></span><span id="error_ds_database_error"></span>**ERROR\_DS\_DATABASE\_ERROR**
   

8409 (0x20D9)
 



A database error has occurred.


   

<span id="ERROR_DS_GOVERNSID_MISSING"></span><span id="error_ds_governsid_missing"></span>**ERROR\_DS\_GOVERNSID\_MISSING**
   

8410 (0x20DA)
 



The attribute GOVERNSID is missing.


   

<span id="ERROR_DS_MISSING_EXPECTED_ATT"></span><span id="error_ds_missing_expected_att"></span>**ERROR\_DS\_MISSING\_EXPECTED\_ATT**
   

8411 (0x20DB)
 



An expected attribute is missing.


   

<span id="ERROR_DS_NCNAME_MISSING_CR_REF"></span><span id="error_ds_ncname_missing_cr_ref"></span>**ERROR\_DS\_NCNAME\_MISSING\_CR\_REF**
   

8412 (0x20DC)
 



The specified naming context is missing a cross reference.


   

<span id="ERROR_DS_SECURITY_CHECKING_ERROR"></span><span id="error_ds_security_checking_error"></span>**ERROR\_DS\_SECURITY\_CHECKING\_ERROR**
   

8413 (0x20DD)
 



A security checking error has occurred.


   

<span id="ERROR_DS_SCHEMA_NOT_LOADED"></span><span id="error_ds_schema_not_loaded"></span>**ERROR\_DS\_SCHEMA\_NOT\_LOADED**
   

8414 (0x20DE)
 



The schema is not loaded.


   

<span id="ERROR_DS_SCHEMA_ALLOC_FAILED"></span><span id="error_ds_schema_alloc_failed"></span>**ERROR\_DS\_SCHEMA\_ALLOC\_FAILED**
   

8415 (0x20DF)
 



Schema allocation failed. Please check if the machine is running low on memory.


   

<span id="ERROR_DS_ATT_SCHEMA_REQ_SYNTAX"></span><span id="error_ds_att_schema_req_syntax"></span>**ERROR\_DS\_ATT\_SCHEMA\_REQ\_SYNTAX**
   

8416 (0x20E0)
 



Failed to obtain the required syntax for the attribute schema.


   

<span id="ERROR_DS_GCVERIFY_ERROR"></span><span id="error_ds_gcverify_error"></span>**ERROR\_DS\_GCVERIFY\_ERROR**
   

8417 (0x20E1)
 



The global catalog verification failed. The global catalog is not available or does not support the operation. Some part of the directory is currently not available.


   

<span id="ERROR_DS_DRA_SCHEMA_MISMATCH"></span><span id="error_ds_dra_schema_mismatch"></span>**ERROR\_DS\_DRA\_SCHEMA\_MISMATCH**
   

8418 (0x20E2)
 



The replication operation failed because of a schema mismatch between the servers involved.


   

<span id="ERROR_DS_CANT_FIND_DSA_OBJ"></span><span id="error_ds_cant_find_dsa_obj"></span>**ERROR\_DS\_CANT\_FIND\_DSA\_OBJ**
   

8419 (0x20E3)
 



The DSA object could not be found.


   

<span id="ERROR_DS_CANT_FIND_EXPECTED_NC"></span><span id="error_ds_cant_find_expected_nc"></span>**ERROR\_DS\_CANT\_FIND\_EXPECTED\_NC**
   

8420 (0x20E4)
 



The naming context could not be found.


   

<span id="ERROR_DS_CANT_FIND_NC_IN_CACHE"></span><span id="error_ds_cant_find_nc_in_cache"></span>**ERROR\_DS\_CANT\_FIND\_NC\_IN\_CACHE**
   

8421 (0x20E5)
 



The naming context could not be found in the cache.


   

<span id="ERROR_DS_CANT_RETRIEVE_CHILD"></span><span id="error_ds_cant_retrieve_child"></span>**ERROR\_DS\_CANT\_RETRIEVE\_CHILD**
   

8422 (0x20E6)
 



The child object could not be retrieved.


   

<span id="ERROR_DS_SECURITY_ILLEGAL_MODIFY"></span><span id="error_ds_security_illegal_modify"></span>**ERROR\_DS\_SECURITY\_ILLEGAL\_MODIFY**
   

8423 (0x20E7)
 



The modification was not permitted for security reasons.


   

<span id="ERROR_DS_CANT_REPLACE_HIDDEN_REC"></span><span id="error_ds_cant_replace_hidden_rec"></span>**ERROR\_DS\_CANT\_REPLACE\_HIDDEN\_REC**
   

8424 (0x20E8)
 



The operation cannot replace the hidden record.


   

<span id="ERROR_DS_BAD_HIERARCHY_FILE"></span><span id="error_ds_bad_hierarchy_file"></span>**ERROR\_DS\_BAD\_HIERARCHY\_FILE**
   

8425 (0x20E9)
 



The hierarchy file is invalid.


   

<span id="ERROR_DS_BUILD_HIERARCHY_TABLE_FAILED"></span><span id="error_ds_build_hierarchy_table_failed"></span>**ERROR\_DS\_BUILD\_HIERARCHY\_TABLE\_FAILED**
   

8426 (0x20EA)
 



The attempt to build the hierarchy table failed.


   

<span id="ERROR_DS_CONFIG_PARAM_MISSING"></span><span id="error_ds_config_param_missing"></span>**ERROR\_DS\_CONFIG\_PARAM\_MISSING**
   

8427 (0x20EB)
 



The directory configuration parameter is missing from the registry.


   

<span id="ERROR_DS_COUNTING_AB_INDICES_FAILED"></span><span id="error_ds_counting_ab_indices_failed"></span>**ERROR\_DS\_COUNTING\_AB\_INDICES\_FAILED**
   

8428 (0x20EC)
 



The attempt to count the address book indices failed.


   

<span id="ERROR_DS_HIERARCHY_TABLE_MALLOC_FAILED"></span><span id="error_ds_hierarchy_table_malloc_failed"></span>**ERROR\_DS\_HIERARCHY\_TABLE\_MALLOC\_FAILED**
   

8429 (0x20ED)
 



The allocation of the hierarchy table failed.


   

<span id="ERROR_DS_INTERNAL_FAILURE"></span><span id="error_ds_internal_failure"></span>**ERROR\_DS\_INTERNAL\_FAILURE**
   

8430 (0x20EE)
 



The directory service encountered an internal failure.


   

<span id="ERROR_DS_UNKNOWN_ERROR"></span><span id="error_ds_unknown_error"></span>**ERROR\_DS\_UNKNOWN\_ERROR**
   

8431 (0x20EF)
 



The directory service encountered an unknown failure.


   

<span id="ERROR_DS_ROOT_REQUIRES_CLASS_TOP"></span><span id="error_ds_root_requires_class_top"></span>**ERROR\_DS\_ROOT\_REQUIRES\_CLASS\_TOP**
   

8432 (0x20F0)
 



A root object requires a class of 'top'.


   

<span id="ERROR_DS_REFUSING_FSMO_ROLES"></span><span id="error_ds_refusing_fsmo_roles"></span>**ERROR\_DS\_REFUSING\_FSMO\_ROLES**
   

8433 (0x20F1)
 



This directory server is shutting down, and cannot take ownership of new floating single-master operation roles.


   

<span id="ERROR_DS_MISSING_FSMO_SETTINGS"></span><span id="error_ds_missing_fsmo_settings"></span>**ERROR\_DS\_MISSING\_FSMO\_SETTINGS**
   

8434 (0x20F2)
 



The directory service is missing mandatory configuration information, and is unable to determine the ownership of floating single-master operation roles.


   

<span id="ERROR_DS_UNABLE_TO_SURRENDER_ROLES"></span><span id="error_ds_unable_to_surrender_roles"></span>**ERROR\_DS\_UNABLE\_TO\_SURRENDER\_ROLES**
   

8435 (0x20F3)
 



The directory service was unable to transfer ownership of one or more floating single-master operation roles to other servers.


   

<span id="ERROR_DS_DRA_GENERIC"></span><span id="error_ds_dra_generic"></span>**ERROR\_DS\_DRA\_GENERIC**
   

8436 (0x20F4)
 



The replication operation failed.


   

<span id="ERROR_DS_DRA_INVALID_PARAMETER"></span><span id="error_ds_dra_invalid_parameter"></span>**ERROR\_DS\_DRA\_INVALID\_PARAMETER**
   

8437 (0x20F5)
 



An invalid parameter was specified for this replication operation.


   

<span id="ERROR_DS_DRA_BUSY"></span><span id="error_ds_dra_busy"></span>**ERROR\_DS\_DRA\_BUSY**
   

8438 (0x20F6)
 



The directory service is too busy to complete the replication operation at this time.


   

<span id="ERROR_DS_DRA_BAD_DN"></span><span id="error_ds_dra_bad_dn"></span>**ERROR\_DS\_DRA\_BAD\_DN**
   

8439 (0x20F7)
 



The distinguished name specified for this replication operation is invalid.


   

<span id="ERROR_DS_DRA_BAD_NC"></span><span id="error_ds_dra_bad_nc"></span>**ERROR\_DS\_DRA\_BAD\_NC**
   

8440 (0x20F8)
 



The naming context specified for this replication operation is invalid.


   

<span id="ERROR_DS_DRA_DN_EXISTS"></span><span id="error_ds_dra_dn_exists"></span>**ERROR\_DS\_DRA\_DN\_EXISTS**
   

8441 (0x20F9)
 



The distinguished name specified for this replication operation already exists.


   

<span id="ERROR_DS_DRA_INTERNAL_ERROR"></span><span id="error_ds_dra_internal_error"></span>**ERROR\_DS\_DRA\_INTERNAL\_ERROR**
   

8442 (0x20FA)
 



The replication system encountered an internal error.


   

<span id="ERROR_DS_DRA_INCONSISTENT_DIT"></span><span id="error_ds_dra_inconsistent_dit"></span>**ERROR\_DS\_DRA\_INCONSISTENT\_DIT**
   

8443 (0x20FB)
 



The replication operation encountered a database inconsistency.


   

<span id="ERROR_DS_DRA_CONNECTION_FAILED"></span><span id="error_ds_dra_connection_failed"></span>**ERROR\_DS\_DRA\_CONNECTION\_FAILED**
   

8444 (0x20FC)
 



The server specified for this replication operation could not be contacted.


   

<span id="ERROR_DS_DRA_BAD_INSTANCE_TYPE"></span><span id="error_ds_dra_bad_instance_type"></span>**ERROR\_DS\_DRA\_BAD\_INSTANCE\_TYPE**
   

8445 (0x20FD)
 



The replication operation encountered an object with an invalid instance type.


   

<span id="ERROR_DS_DRA_OUT_OF_MEM"></span><span id="error_ds_dra_out_of_mem"></span>**ERROR\_DS\_DRA\_OUT\_OF\_MEM**
   

8446 (0x20FE)
 



The replication operation failed to allocate memory.


   

<span id="ERROR_DS_DRA_MAIL_PROBLEM"></span><span id="error_ds_dra_mail_problem"></span>**ERROR\_DS\_DRA\_MAIL\_PROBLEM**
   

8447 (0x20FF)
 



The replication operation encountered an error with the mail system.


   

<span id="ERROR_DS_DRA_REF_ALREADY_EXISTS"></span><span id="error_ds_dra_ref_already_exists"></span>**ERROR\_DS\_DRA\_REF\_ALREADY\_EXISTS**
   

8448 (0x2100)
 



The replication reference information for the target server already exists.


   

<span id="ERROR_DS_DRA_REF_NOT_FOUND"></span><span id="error_ds_dra_ref_not_found"></span>**ERROR\_DS\_DRA\_REF\_NOT\_FOUND**
   

8449 (0x2101)
 



The replication reference information for the target server does not exist.


   

<span id="ERROR_DS_DRA_OBJ_IS_REP_SOURCE"></span><span id="error_ds_dra_obj_is_rep_source"></span>**ERROR\_DS\_DRA\_OBJ\_IS\_REP\_SOURCE**
   

8450 (0x2102)
 



The naming context cannot be removed because it is replicated to another server.


   

<span id="ERROR_DS_DRA_DB_ERROR"></span><span id="error_ds_dra_db_error"></span>**ERROR\_DS\_DRA\_DB\_ERROR**
   

8451 (0x2103)
 



The replication operation encountered a database error.


   

<span id="ERROR_DS_DRA_NO_REPLICA"></span><span id="error_ds_dra_no_replica"></span>**ERROR\_DS\_DRA\_NO\_REPLICA**
   

8452 (0x2104)
 



The naming context is in the process of being removed or is not replicated from the specified server.


   

<span id="ERROR_DS_DRA_ACCESS_DENIED"></span><span id="error_ds_dra_access_denied"></span>**ERROR\_DS\_DRA\_ACCESS\_DENIED**
   

8453 (0x2105)
 



Replication access was denied.


   

<span id="ERROR_DS_DRA_NOT_SUPPORTED"></span><span id="error_ds_dra_not_supported"></span>**ERROR\_DS\_DRA\_NOT\_SUPPORTED**
   

8454 (0x2106)
 



The requested operation is not supported by this version of the directory service.


   

<span id="ERROR_DS_DRA_RPC_CANCELLED"></span><span id="error_ds_dra_rpc_cancelled"></span>**ERROR\_DS\_DRA\_RPC\_CANCELLED**
   

8455 (0x2107)
 



The replication remote procedure call was cancelled.


   

<span id="ERROR_DS_DRA_SOURCE_DISABLED"></span><span id="error_ds_dra_source_disabled"></span>**ERROR\_DS\_DRA\_SOURCE\_DISABLED**
   

8456 (0x2108)
 



The source server is currently rejecting replication requests.


   

<span id="ERROR_DS_DRA_SINK_DISABLED"></span><span id="error_ds_dra_sink_disabled"></span>**ERROR\_DS\_DRA\_SINK\_DISABLED**
   

8457 (0x2109)
 



The destination server is currently rejecting replication requests.


   

<span id="ERROR_DS_DRA_NAME_COLLISION"></span><span id="error_ds_dra_name_collision"></span>**ERROR\_DS\_DRA\_NAME\_COLLISION**
   

8458 (0x210A)
 



The replication operation failed due to a collision of object names.


   

<span id="ERROR_DS_DRA_SOURCE_REINSTALLED"></span><span id="error_ds_dra_source_reinstalled"></span>**ERROR\_DS\_DRA\_SOURCE\_REINSTALLED**
   

8459 (0x210B)
 



The replication source has been reinstalled.


   

<span id="ERROR_DS_DRA_MISSING_PARENT"></span><span id="error_ds_dra_missing_parent"></span>**ERROR\_DS\_DRA\_MISSING\_PARENT**
   

8460 (0x210C)
 



The replication operation failed because a required parent object is missing.


   

<span id="ERROR_DS_DRA_PREEMPTED"></span><span id="error_ds_dra_preempted"></span>**ERROR\_DS\_DRA\_PREEMPTED**
   

8461 (0x210D)
 



The replication operation was preempted.


   

<span id="ERROR_DS_DRA_ABANDON_SYNC"></span><span id="error_ds_dra_abandon_sync"></span>**ERROR\_DS\_DRA\_ABANDON\_SYNC**
   

8462 (0x210E)
 



The replication synchronization attempt was abandoned because of a lack of updates.


   

<span id="ERROR_DS_DRA_SHUTDOWN"></span><span id="error_ds_dra_shutdown"></span>**ERROR\_DS\_DRA\_SHUTDOWN**
   

8463 (0x210F)
 



The replication operation was terminated because the system is shutting down.


   

<span id="ERROR_DS_DRA_INCOMPATIBLE_PARTIAL_SET"></span><span id="error_ds_dra_incompatible_partial_set"></span>**ERROR\_DS\_DRA\_INCOMPATIBLE\_PARTIAL\_SET**
   

8464 (0x2110)
 



Synchronization attempt failed because the destination DC is currently waiting to synchronize new partial attributes from source. This condition is normal if a recent schema change modified the partial attribute set. The destination partial attribute set is not a subset of source partial attribute set.


   

<span id="ERROR_DS_DRA_SOURCE_IS_PARTIAL_REPLICA"></span><span id="error_ds_dra_source_is_partial_replica"></span>**ERROR\_DS\_DRA\_SOURCE\_IS\_PARTIAL\_REPLICA**
   

8465 (0x2111)
 



The replication synchronization attempt failed because a master replica attempted to sync from a partial replica.


   

<span id="ERROR_DS_DRA_EXTN_CONNECTION_FAILED"></span><span id="error_ds_dra_extn_connection_failed"></span>**ERROR\_DS\_DRA\_EXTN\_CONNECTION\_FAILED**
   

8466 (0x2112)
 



The server specified for this replication operation was contacted, but that server was unable to contact an additional server needed to complete the operation.


   

<span id="ERROR_DS_INSTALL_SCHEMA_MISMATCH"></span><span id="error_ds_install_schema_mismatch"></span>**ERROR\_DS\_INSTALL\_SCHEMA\_MISMATCH**
   

8467 (0x2113)
 



The version of the directory service schema of the source forest is not compatible with the version of directory service on this computer.


   

<span id="ERROR_DS_DUP_LINK_ID"></span><span id="error_ds_dup_link_id"></span>**ERROR\_DS\_DUP\_LINK\_ID**
   

8468 (0x2114)
 



Schema update failed: An attribute with the same link identifier already exists.


   

<span id="ERROR_DS_NAME_ERROR_RESOLVING"></span><span id="error_ds_name_error_resolving"></span>**ERROR\_DS\_NAME\_ERROR\_RESOLVING**
   

8469 (0x2115)
 



Name translation: Generic processing error.


   

<span id="ERROR_DS_NAME_ERROR_NOT_FOUND"></span><span id="error_ds_name_error_not_found"></span>**ERROR\_DS\_NAME\_ERROR\_NOT\_FOUND**
   

8470 (0x2116)
 



Name translation: Could not find the name or insufficient right to see name.


   

<span id="ERROR_DS_NAME_ERROR_NOT_UNIQUE"></span><span id="error_ds_name_error_not_unique"></span>**ERROR\_DS\_NAME\_ERROR\_NOT\_UNIQUE**
   

8471 (0x2117)
 



Name translation: Input name mapped to more than one output name.


   

<span id="ERROR_DS_NAME_ERROR_NO_MAPPING"></span><span id="error_ds_name_error_no_mapping"></span>**ERROR\_DS\_NAME\_ERROR\_NO\_MAPPING**
   

8472 (0x2118)
 



Name translation: Input name found, but not the associated output format.


   

<span id="ERROR_DS_NAME_ERROR_DOMAIN_ONLY"></span><span id="error_ds_name_error_domain_only"></span>**ERROR\_DS\_NAME\_ERROR\_DOMAIN\_ONLY**
   

8473 (0x2119)
 



Name translation: Unable to resolve completely, only the domain was found.


   

<span id="ERROR_DS_NAME_ERROR_NO_SYNTACTICAL_MAPPING"></span><span id="error_ds_name_error_no_syntactical_mapping"></span>**ERROR\_DS\_NAME\_ERROR\_NO\_SYNTACTICAL\_MAPPING**
   

8474 (0x211A)
 



Name translation: Unable to perform purely syntactical mapping at the client without going out to the wire.


   

<span id="ERROR_DS_CONSTRUCTED_ATT_MOD"></span><span id="error_ds_constructed_att_mod"></span>**ERROR\_DS\_CONSTRUCTED\_ATT\_MOD**
   

8475 (0x211B)
 



Modification of a constructed attribute is not allowed.


   

<span id="ERROR_DS_WRONG_OM_OBJ_CLASS"></span><span id="error_ds_wrong_om_obj_class"></span>**ERROR\_DS\_WRONG\_OM\_OBJ\_CLASS**
   

8476 (0x211C)
 



The OM-Object-Class specified is incorrect for an attribute with the specified syntax.


   

<span id="ERROR_DS_DRA_REPL_PENDING"></span><span id="error_ds_dra_repl_pending"></span>**ERROR\_DS\_DRA\_REPL\_PENDING**
   

8477 (0x211D)
 



The replication request has been posted; waiting for reply.


   

<span id="ERROR_DS_DS_REQUIRED"></span><span id="error_ds_ds_required"></span>**ERROR\_DS\_DS\_REQUIRED**
   

8478 (0x211E)
 



The requested operation requires a directory service, and none was available.


   

<span id="ERROR_DS_INVALID_LDAP_DISPLAY_NAME"></span><span id="error_ds_invalid_ldap_display_name"></span>**ERROR\_DS\_INVALID\_LDAP\_DISPLAY\_NAME**
   

8479 (0x211F)
 



The LDAP display name of the class or attribute contains non-ASCII characters.


   

<span id="ERROR_DS_NON_BASE_SEARCH"></span><span id="error_ds_non_base_search"></span>**ERROR\_DS\_NON\_BASE\_SEARCH**
   

8480 (0x2120)
 



The requested search operation is only supported for base searches.


   

<span id="ERROR_DS_CANT_RETRIEVE_ATTS"></span><span id="error_ds_cant_retrieve_atts"></span>**ERROR\_DS\_CANT\_RETRIEVE\_ATTS**
   

8481 (0x2121)
 



The search failed to retrieve attributes from the database.


   

<span id="ERROR_DS_BACKLINK_WITHOUT_LINK"></span><span id="error_ds_backlink_without_link"></span>**ERROR\_DS\_BACKLINK\_WITHOUT\_LINK**
   

8482 (0x2122)
 



The schema update operation tried to add a backward link attribute that has no corresponding forward link.


   

<span id="ERROR_DS_EPOCH_MISMATCH"></span><span id="error_ds_epoch_mismatch"></span>**ERROR\_DS\_EPOCH\_MISMATCH**
   

8483 (0x2123)
 



Source and destination of a cross-domain move do not agree on the object's epoch number. Either source or destination does not have the latest version of the object.


   

<span id="ERROR_DS_SRC_NAME_MISMATCH"></span><span id="error_ds_src_name_mismatch"></span>**ERROR\_DS\_SRC\_NAME\_MISMATCH**
   

8484 (0x2124)
 



Source and destination of a cross-domain move do not agree on the object's current name. Either source or destination does not have the latest version of the object.


   

<span id="ERROR_DS_SRC_AND_DST_NC_IDENTICAL"></span><span id="error_ds_src_and_dst_nc_identical"></span>**ERROR\_DS\_SRC\_AND\_DST\_NC\_IDENTICAL**
   

8485 (0x2125)
 



Source and destination for the cross-domain move operation are identical. Caller should use local move operation instead of cross-domain move operation.


   

<span id="ERROR_DS_DST_NC_MISMATCH"></span><span id="error_ds_dst_nc_mismatch"></span>**ERROR\_DS\_DST\_NC\_MISMATCH**
   

8486 (0x2126)
 



Source and destination for a cross-domain move are not in agreement on the naming contexts in the forest. Either source or destination does not have the latest version of the Partitions container.


   

<span id="ERROR_DS_NOT_AUTHORITIVE_FOR_DST_NC"></span><span id="error_ds_not_authoritive_for_dst_nc"></span>**ERROR\_DS\_NOT\_AUTHORITIVE\_FOR\_DST\_NC**
   

8487 (0x2127)
 



Destination of a cross-domain move is not authoritative for the destination naming context.


   

<span id="ERROR_DS_SRC_GUID_MISMATCH"></span><span id="error_ds_src_guid_mismatch"></span>**ERROR\_DS\_SRC\_GUID\_MISMATCH**
   

8488 (0x2128)
 



Source and destination of a cross-domain move do not agree on the identity of the source object. Either source or destination does not have the latest version of the source object.


   

<span id="ERROR_DS_CANT_MOVE_DELETED_OBJECT"></span><span id="error_ds_cant_move_deleted_object"></span>**ERROR\_DS\_CANT\_MOVE\_DELETED\_OBJECT**
   

8489 (0x2129)
 



Object being moved across-domains is already known to be deleted by the destination server. The source server does not have the latest version of the source object.


   

<span id="ERROR_DS_PDC_OPERATION_IN_PROGRESS"></span><span id="error_ds_pdc_operation_in_progress"></span>**ERROR\_DS\_PDC\_OPERATION\_IN\_PROGRESS**
   

8490 (0x212A)
 



Another operation which requires exclusive access to the PDC FSMO is already in progress.


   

<span id="ERROR_DS_CROSS_DOMAIN_CLEANUP_REQD"></span><span id="error_ds_cross_domain_cleanup_reqd"></span>**ERROR\_DS\_CROSS\_DOMAIN\_CLEANUP\_REQD**
   

8491 (0x212B)
 



A cross-domain move operation failed such that two versions of the moved object exist - one each in the source and destination domains. The destination object needs to be removed to restore the system to a consistent state.


   

<span id="ERROR_DS_ILLEGAL_XDOM_MOVE_OPERATION"></span><span id="error_ds_illegal_xdom_move_operation"></span>**ERROR\_DS\_ILLEGAL\_XDOM\_MOVE\_OPERATION**
   

8492 (0x212C)
 



This object may not be moved across domain boundaries either because cross-domain moves for this class are disallowed, or the object has some special characteristics, e.g.: trust account or restricted RID, which prevent its move.


   

<span id="ERROR_DS_CANT_WITH_ACCT_GROUP_MEMBERSHPS"></span><span id="error_ds_cant_with_acct_group_membershps"></span>**ERROR\_DS\_CANT\_WITH\_ACCT\_GROUP\_MEMBERSHPS**
   

8493 (0x212D)
 



Can't move objects with memberships across domain boundaries as once moved, this would violate the membership conditions of the account group. Remove the object from any account group memberships and retry.


   

<span id="ERROR_DS_NC_MUST_HAVE_NC_PARENT"></span><span id="error_ds_nc_must_have_nc_parent"></span>**ERROR\_DS\_NC\_MUST\_HAVE\_NC\_PARENT**
   

8494 (0x212E)
 



A naming context head must be the immediate child of another naming context head, not of an interior node.


   

<span id="ERROR_DS_CR_IMPOSSIBLE_TO_VALIDATE"></span><span id="error_ds_cr_impossible_to_validate"></span>**ERROR\_DS\_CR\_IMPOSSIBLE\_TO\_VALIDATE**
   

8495 (0x212F)
 



The directory cannot validate the proposed naming context name because it does not hold a replica of the naming context above the proposed naming context. Please ensure that the domain naming master role is held by a server that is configured as a global catalog server, and that the server is up to date with its replication partners. (Applies only to Windows 2000 Domain Naming masters.)


   

<span id="ERROR_DS_DST_DOMAIN_NOT_NATIVE"></span><span id="error_ds_dst_domain_not_native"></span>**ERROR\_DS\_DST\_DOMAIN\_NOT\_NATIVE**
   

8496 (0x2130)
 



Destination domain must be in native mode.


   

<span id="ERROR_DS_MISSING_INFRASTRUCTURE_CONTAINER"></span><span id="error_ds_missing_infrastructure_container"></span>**ERROR\_DS\_MISSING\_INFRASTRUCTURE\_CONTAINER**
   

8497 (0x2131)
 



The operation cannot be performed because the server does not have an infrastructure container in the domain of interest.


   

<span id="ERROR_DS_CANT_MOVE_ACCOUNT_GROUP"></span><span id="error_ds_cant_move_account_group"></span>**ERROR\_DS\_CANT\_MOVE\_ACCOUNT\_GROUP**
   

8498 (0x2132)
 



Cross-domain move of non-empty account groups is not allowed.


   

<span id="ERROR_DS_CANT_MOVE_RESOURCE_GROUP"></span><span id="error_ds_cant_move_resource_group"></span>**ERROR\_DS\_CANT\_MOVE\_RESOURCE\_GROUP**
   

8499 (0x2133)
 



Cross-domain move of non-empty resource groups is not allowed.


   

<span id="ERROR_DS_INVALID_SEARCH_FLAG"></span><span id="error_ds_invalid_search_flag"></span>**ERROR\_DS\_INVALID\_SEARCH\_FLAG**
   

8500 (0x2134)
 



The search flags for the attribute are invalid. The ANR bit is valid only on attributes of Unicode or Teletex strings.


   

<span id="ERROR_DS_NO_TREE_DELETE_ABOVE_NC"></span><span id="error_ds_no_tree_delete_above_nc"></span>**ERROR\_DS\_NO\_TREE\_DELETE\_ABOVE\_NC**
   

8501 (0x2135)
 



Tree deletions starting at an object which has an NC head as a descendant are not allowed.


   

<span id="ERROR_DS_COULDNT_LOCK_TREE_FOR_DELETE"></span><span id="error_ds_couldnt_lock_tree_for_delete"></span>**ERROR\_DS\_COULDNT\_LOCK\_TREE\_FOR\_DELETE**
   

8502 (0x2136)
 



The directory service failed to lock a tree in preparation for a tree deletion because the tree was in use.


   

<span id="ERROR_DS_COULDNT_IDENTIFY_OBJECTS_FOR_TREE_DELETE"></span><span id="error_ds_couldnt_identify_objects_for_tree_delete"></span>**ERROR\_DS\_COULDNT\_IDENTIFY\_OBJECTS\_FOR\_TREE\_DELETE**
   

8503 (0x2137)
 



The directory service failed to identify the list of objects to delete while attempting a tree deletion.


   

<span id="ERROR_DS_SAM_INIT_FAILURE"></span><span id="error_ds_sam_init_failure"></span>**ERROR\_DS\_SAM\_INIT\_FAILURE**
   

8504 (0x2138)
 



Security Accounts Manager initialization failed because of the following error: %1. Error Status: 0x%2. Please shutdown this system and reboot into Directory Services Restore Mode, check the event log for more detailed information.


   

<span id="ERROR_DS_SENSITIVE_GROUP_VIOLATION"></span><span id="error_ds_sensitive_group_violation"></span>**ERROR\_DS\_SENSITIVE\_GROUP\_VIOLATION**
   

8505 (0x2139)
 



Only an administrator can modify the membership list of an administrative group.


   

<span id="ERROR_DS_CANT_MOD_PRIMARYGROUPID"></span><span id="error_ds_cant_mod_primarygroupid"></span>**ERROR\_DS\_CANT\_MOD\_PRIMARYGROUPID**
   

8506 (0x213A)
 



Cannot change the primary group ID of a domain controller account.


   

<span id="ERROR_DS_ILLEGAL_BASE_SCHEMA_MOD"></span><span id="error_ds_illegal_base_schema_mod"></span>**ERROR\_DS\_ILLEGAL\_BASE\_SCHEMA\_MOD**
   

8507 (0x213B)
 



An attempt is made to modify the base schema.


   

<span id="ERROR_DS_NONSAFE_SCHEMA_CHANGE"></span><span id="error_ds_nonsafe_schema_change"></span>**ERROR\_DS\_NONSAFE\_SCHEMA\_CHANGE**
   

8508 (0x213C)
 



Adding a new mandatory attribute to an existing class, deleting a mandatory attribute from an existing class, or adding an optional attribute to the special class Top that is not a backlink attribute (directly or through inheritance, for example, by adding or deleting an auxiliary class) is not allowed.


   

<span id="ERROR_DS_SCHEMA_UPDATE_DISALLOWED"></span><span id="error_ds_schema_update_disallowed"></span>**ERROR\_DS\_SCHEMA\_UPDATE\_DISALLOWED**
   

8509 (0x213D)
 



Schema update is not allowed on this DC because the DC is not the schema FSMO Role Owner.


   

<span id="ERROR_DS_CANT_CREATE_UNDER_SCHEMA"></span><span id="error_ds_cant_create_under_schema"></span>**ERROR\_DS\_CANT\_CREATE\_UNDER\_SCHEMA**
   

8510 (0x213E)
 



An object of this class cannot be created under the schema container. You can only create attribute-schema and class-schema objects under the schema container.


   

<span id="ERROR_DS_INSTALL_NO_SRC_SCH_VERSION"></span><span id="error_ds_install_no_src_sch_version"></span>**ERROR\_DS\_INSTALL\_NO\_SRC\_SCH\_VERSION**
   

8511 (0x213F)
 



The replica/child install failed to get the objectVersion attribute on the schema container on the source DC. Either the attribute is missing on the schema container or the credentials supplied do not have permission to read it.


   

<span id="ERROR_DS_INSTALL_NO_SCH_VERSION_IN_INIFILE"></span><span id="error_ds_install_no_sch_version_in_inifile"></span>**ERROR\_DS\_INSTALL\_NO\_SCH\_VERSION\_IN\_INIFILE**
   

8512 (0x2140)
 



The replica/child install failed to read the objectVersion attribute in the SCHEMA section of the file schema.ini in the system32 directory.


   

<span id="ERROR_DS_INVALID_GROUP_TYPE"></span><span id="error_ds_invalid_group_type"></span>**ERROR\_DS\_INVALID\_GROUP\_TYPE**
   

8513 (0x2141)
 



The specified group type is invalid.


   

<span id="ERROR_DS_NO_NEST_GLOBALGROUP_IN_MIXEDDOMAIN"></span><span id="error_ds_no_nest_globalgroup_in_mixeddomain"></span>**ERROR\_DS\_NO\_NEST\_GLOBALGROUP\_IN\_MIXEDDOMAIN**
   

8514 (0x2142)
 



You cannot nest global groups in a mixed domain if the group is security-enabled.


   

<span id="ERROR_DS_NO_NEST_LOCALGROUP_IN_MIXEDDOMAIN"></span><span id="error_ds_no_nest_localgroup_in_mixeddomain"></span>**ERROR\_DS\_NO\_NEST\_LOCALGROUP\_IN\_MIXEDDOMAIN**
   

8515 (0x2143)
 



You cannot nest local groups in a mixed domain if the group is security-enabled.


   

<span id="ERROR_DS_GLOBAL_CANT_HAVE_LOCAL_MEMBER"></span><span id="error_ds_global_cant_have_local_member"></span>**ERROR\_DS\_GLOBAL\_CANT\_HAVE\_LOCAL\_MEMBER**
   

8516 (0x2144)
 



A global group cannot have a local group as a member.


   

<span id="ERROR_DS_GLOBAL_CANT_HAVE_UNIVERSAL_MEMBER"></span><span id="error_ds_global_cant_have_universal_member"></span>**ERROR\_DS\_GLOBAL\_CANT\_HAVE\_UNIVERSAL\_MEMBER**
   

8517 (0x2145)
 



A global group cannot have a universal group as a member.


   

<span id="ERROR_DS_UNIVERSAL_CANT_HAVE_LOCAL_MEMBER"></span><span id="error_ds_universal_cant_have_local_member"></span>**ERROR\_DS\_UNIVERSAL\_CANT\_HAVE\_LOCAL\_MEMBER**
   

8518 (0x2146)
 



A universal group cannot have a local group as a member.


   

<span id="ERROR_DS_GLOBAL_CANT_HAVE_CROSSDOMAIN_MEMBER"></span><span id="error_ds_global_cant_have_crossdomain_member"></span>**ERROR\_DS\_GLOBAL\_CANT\_HAVE\_CROSSDOMAIN\_MEMBER**
   

8519 (0x2147)
 



A global group cannot have a cross-domain member.


   

<span id="ERROR_DS_LOCAL_CANT_HAVE_CROSSDOMAIN_LOCAL_MEMBER"></span><span id="error_ds_local_cant_have_crossdomain_local_member"></span>**ERROR\_DS\_LOCAL\_CANT\_HAVE\_CROSSDOMAIN\_LOCAL\_MEMBER**
   

8520 (0x2148)
 



A local group cannot have another cross domain local group as a member.


   

<span id="ERROR_DS_HAVE_PRIMARY_MEMBERS"></span><span id="error_ds_have_primary_members"></span>**ERROR\_DS\_HAVE\_PRIMARY\_MEMBERS**
   

8521 (0x2149)
 



A group with primary members cannot change to a security-disabled group.


   

<span id="ERROR_DS_STRING_SD_CONVERSION_FAILED"></span><span id="error_ds_string_sd_conversion_failed"></span>**ERROR\_DS\_STRING\_SD\_CONVERSION\_FAILED**
   

8522 (0x214A)
 



The schema cache load failed to convert the string default SD on a class-schema object.


   

<span id="ERROR_DS_NAMING_MASTER_GC"></span><span id="error_ds_naming_master_gc"></span>**ERROR\_DS\_NAMING\_MASTER\_GC**
   

8523 (0x214B)
 



Only DSAs configured to be Global Catalog servers should be allowed to hold the Domain Naming Master FSMO role. (Applies only to Windows 2000 servers.)


   

<span id="ERROR_DS_DNS_LOOKUP_FAILURE"></span><span id="error_ds_dns_lookup_failure"></span>**ERROR\_DS\_DNS\_LOOKUP\_FAILURE**
   

8524 (0x214C)
 



The DSA operation is unable to proceed because of a DNS lookup failure.


   

<span id="ERROR_DS_COULDNT_UPDATE_SPNS"></span><span id="error_ds_couldnt_update_spns"></span>**ERROR\_DS\_COULDNT\_UPDATE\_SPNS**
   

8525 (0x214D)
 



While processing a change to the DNS Host Name for an object, the Service Principal Name values could not be kept in sync.


   

<span id="ERROR_DS_CANT_RETRIEVE_SD"></span><span id="error_ds_cant_retrieve_sd"></span>**ERROR\_DS\_CANT\_RETRIEVE\_SD**
   

8526 (0x214E)
 



The Security Descriptor attribute could not be read.


   

<span id="ERROR_DS_KEY_NOT_UNIQUE"></span><span id="error_ds_key_not_unique"></span>**ERROR\_DS\_KEY\_NOT\_UNIQUE**
   

8527 (0x214F)
 



The object requested was not found, but an object with that key was found.


   

<span id="ERROR_DS_WRONG_LINKED_ATT_SYNTAX"></span><span id="error_ds_wrong_linked_att_syntax"></span>**ERROR\_DS\_WRONG\_LINKED\_ATT\_SYNTAX**
   

8528 (0x2150)
 



The syntax of the linked attribute being added is incorrect. Forward links can only have syntax 2.5.5.1, 2.5.5.7, and 2.5.5.14, and backlinks can only have syntax 2.5.5.1.


   

<span id="ERROR_DS_SAM_NEED_BOOTKEY_PASSWORD"></span><span id="error_ds_sam_need_bootkey_password"></span>**ERROR\_DS\_SAM\_NEED\_BOOTKEY\_PASSWORD**
   

8529 (0x2151)
 



Security Account Manager needs to get the boot password.


   

<span id="ERROR_DS_SAM_NEED_BOOTKEY_FLOPPY"></span><span id="error_ds_sam_need_bootkey_floppy"></span>**ERROR\_DS\_SAM\_NEED\_BOOTKEY\_FLOPPY**
   

8530 (0x2152)
 



Security Account Manager needs to get the boot key from floppy disk.


   

<span id="ERROR_DS_CANT_START"></span><span id="error_ds_cant_start"></span>**ERROR\_DS\_CANT\_START**
   

8531 (0x2153)
 



Directory Service cannot start.


   

<span id="ERROR_DS_INIT_FAILURE"></span><span id="error_ds_init_failure"></span>**ERROR\_DS\_INIT\_FAILURE**
   

8532 (0x2154)
 



Directory Services could not start.


   

<span id="ERROR_DS_NO_PKT_PRIVACY_ON_CONNECTION"></span><span id="error_ds_no_pkt_privacy_on_connection"></span>**ERROR\_DS\_NO\_PKT\_PRIVACY\_ON\_CONNECTION**
   

8533 (0x2155)
 



The connection between client and server requires packet privacy or better.


   

<span id="ERROR_DS_SOURCE_DOMAIN_IN_FOREST"></span><span id="error_ds_source_domain_in_forest"></span>**ERROR\_DS\_SOURCE\_DOMAIN\_IN\_FOREST**
   

8534 (0x2156)
 



The source domain may not be in the same forest as destination.


   

<span id="ERROR_DS_DESTINATION_DOMAIN_NOT_IN_FOREST"></span><span id="error_ds_destination_domain_not_in_forest"></span>**ERROR\_DS\_DESTINATION\_DOMAIN\_NOT\_IN\_FOREST**
   

8535 (0x2157)
 



The destination domain must be in the forest.


   

<span id="ERROR_DS_DESTINATION_AUDITING_NOT_ENABLED"></span><span id="error_ds_destination_auditing_not_enabled"></span>**ERROR\_DS\_DESTINATION\_AUDITING\_NOT\_ENABLED**
   

8536 (0x2158)
 



The operation requires that destination domain auditing be enabled.


   

<span id="ERROR_DS_CANT_FIND_DC_FOR_SRC_DOMAIN"></span><span id="error_ds_cant_find_dc_for_src_domain"></span>**ERROR\_DS\_CANT\_FIND\_DC\_FOR\_SRC\_DOMAIN**
   

8537 (0x2159)
 



The operation couldn't locate a DC for the source domain.


   

<span id="ERROR_DS_SRC_OBJ_NOT_GROUP_OR_USER"></span><span id="error_ds_src_obj_not_group_or_user"></span>**ERROR\_DS\_SRC\_OBJ\_NOT\_GROUP\_OR\_USER**
   

8538 (0x215A)
 



The source object must be a group or user.


   

<span id="ERROR_DS_SRC_SID_EXISTS_IN_FOREST"></span><span id="error_ds_src_sid_exists_in_forest"></span>**ERROR\_DS\_SRC\_SID\_EXISTS\_IN\_FOREST**
   

8539 (0x215B)
 



The source object's SID already exists in destination forest.


   

<span id="ERROR_DS_SRC_AND_DST_OBJECT_CLASS_MISMATCH"></span><span id="error_ds_src_and_dst_object_class_mismatch"></span>**ERROR\_DS\_SRC\_AND\_DST\_OBJECT\_CLASS\_MISMATCH**
   

8540 (0x215C)
 



The source and destination object must be of the same type.


   

<span id="ERROR_SAM_INIT_FAILURE"></span><span id="error_sam_init_failure"></span>**ERROR\_SAM\_INIT\_FAILURE**
   

8541 (0x215D)
 



Security Accounts Manager initialization failed because of the following error: %1. Error Status: 0x%2. Click OK to shut down the system and reboot into Safe Mode. Check the event log for detailed information.


   

<span id="ERROR_DS_DRA_SCHEMA_INFO_SHIP"></span><span id="error_ds_dra_schema_info_ship"></span>**ERROR\_DS\_DRA\_SCHEMA\_INFO\_SHIP**
   

8542 (0x215E)
 



Schema information could not be included in the replication request.


   

<span id="ERROR_DS_DRA_SCHEMA_CONFLICT"></span><span id="error_ds_dra_schema_conflict"></span>**ERROR\_DS\_DRA\_SCHEMA\_CONFLICT**
   

8543 (0x215F)
 



The replication operation could not be completed due to a schema incompatibility.


   

<span id="ERROR_DS_DRA_EARLIER_SCHEMA_CONFLICT"></span><span id="error_ds_dra_earlier_schema_conflict"></span>**ERROR\_DS\_DRA\_EARLIER\_SCHEMA\_CONFLICT**
   

8544 (0x2160)
 



The replication operation could not be completed due to a previous schema incompatibility.


   

<span id="ERROR_DS_DRA_OBJ_NC_MISMATCH"></span><span id="error_ds_dra_obj_nc_mismatch"></span>**ERROR\_DS\_DRA\_OBJ\_NC\_MISMATCH**
   

8545 (0x2161)
 



The replication update could not be applied because either the source or the destination has not yet received information regarding a recent cross-domain move operation.


   

<span id="ERROR_DS_NC_STILL_HAS_DSAS"></span><span id="error_ds_nc_still_has_dsas"></span>**ERROR\_DS\_NC\_STILL\_HAS\_DSAS**
   

8546 (0x2162)
 



The requested domain could not be deleted because there exist domain controllers that still host this domain.


   

<span id="ERROR_DS_GC_REQUIRED"></span><span id="error_ds_gc_required"></span>**ERROR\_DS\_GC\_REQUIRED**
   

8547 (0x2163)
 



The requested operation can be performed only on a global catalog server.


   

<span id="ERROR_DS_LOCAL_MEMBER_OF_LOCAL_ONLY"></span><span id="error_ds_local_member_of_local_only"></span>**ERROR\_DS\_LOCAL\_MEMBER\_OF\_LOCAL\_ONLY**
   

8548 (0x2164)
 



A local group can only be a member of other local groups in the same domain.


   

<span id="ERROR_DS_NO_FPO_IN_UNIVERSAL_GROUPS"></span><span id="error_ds_no_fpo_in_universal_groups"></span>**ERROR\_DS\_NO\_FPO\_IN\_UNIVERSAL\_GROUPS**
   

8549 (0x2165)
 



Foreign security principals cannot be members of universal groups.


   

<span id="ERROR_DS_CANT_ADD_TO_GC"></span><span id="error_ds_cant_add_to_gc"></span>**ERROR\_DS\_CANT\_ADD\_TO\_GC**
   

8550 (0x2166)
 



The attribute is not allowed to be replicated to the GC because of security reasons.


   

<span id="ERROR_DS_NO_CHECKPOINT_WITH_PDC"></span><span id="error_ds_no_checkpoint_with_pdc"></span>**ERROR\_DS\_NO\_CHECKPOINT\_WITH\_PDC**
   

8551 (0x2167)
 



The checkpoint with the PDC could not be taken because there too many modifications being processed currently.


   

<span id="ERROR_DS_SOURCE_AUDITING_NOT_ENABLED"></span><span id="error_ds_source_auditing_not_enabled"></span>**ERROR\_DS\_SOURCE\_AUDITING\_NOT\_ENABLED**
   

8552 (0x2168)
 



The operation requires that source domain auditing be enabled.


   

<span id="ERROR_DS_CANT_CREATE_IN_NONDOMAIN_NC"></span><span id="error_ds_cant_create_in_nondomain_nc"></span>**ERROR\_DS\_CANT\_CREATE\_IN\_NONDOMAIN\_NC**
   

8553 (0x2169)
 



Security principal objects can only be created inside domain naming contexts.


   

<span id="ERROR_DS_INVALID_NAME_FOR_SPN"></span><span id="error_ds_invalid_name_for_spn"></span>**ERROR\_DS\_INVALID\_NAME\_FOR\_SPN**
   

8554 (0x216A)
 



A Service Principal Name (SPN) could not be constructed because the provided hostname is not in the necessary format.


   

<span id="ERROR_DS_FILTER_USES_CONTRUCTED_ATTRS"></span><span id="error_ds_filter_uses_contructed_attrs"></span>**ERROR\_DS\_FILTER\_USES\_CONTRUCTED\_ATTRS**
   

8555 (0x216B)
 



A Filter was passed that uses constructed attributes.


   

<span id="ERROR_DS_UNICODEPWD_NOT_IN_QUOTES"></span><span id="error_ds_unicodepwd_not_in_quotes"></span>**ERROR\_DS\_UNICODEPWD\_NOT\_IN\_QUOTES**
   

8556 (0x216C)
 



The unicodePwd attribute value must be enclosed in double quotes.


   

<span id="ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED"></span><span id="error_ds_machine_account_quota_exceeded"></span>**ERROR\_DS\_MACHINE\_ACCOUNT\_QUOTA\_EXCEEDED**
   

8557 (0x216D)
 



Your computer could not be joined to the domain. You have exceeded the maximum number of computer accounts you are allowed to create in this domain. Contact your system administrator to have this limit reset or increased.


   

<span id="ERROR_DS_MUST_BE_RUN_ON_DST_DC"></span><span id="error_ds_must_be_run_on_dst_dc"></span>**ERROR\_DS\_MUST\_BE\_RUN\_ON\_DST\_DC**
   

8558 (0x216E)
 



For security reasons, the operation must be run on the destination DC.


   

<span id="ERROR_DS_SRC_DC_MUST_BE_SP4_OR_GREATER"></span><span id="error_ds_src_dc_must_be_sp4_or_greater"></span>**ERROR\_DS\_SRC\_DC\_MUST\_BE\_SP4\_OR\_GREATER**
   

8559 (0x216F)
 



For security reasons, the source DC must be NT4SP4 or greater.


   

<span id="ERROR_DS_CANT_TREE_DELETE_CRITICAL_OBJ"></span><span id="error_ds_cant_tree_delete_critical_obj"></span>**ERROR\_DS\_CANT\_TREE\_DELETE\_CRITICAL\_OBJ**
   

8560 (0x2170)
 



Critical Directory Service System objects cannot be deleted during tree delete operations. The tree delete may have been partially performed.


   

<span id="ERROR_DS_INIT_FAILURE_CONSOLE"></span><span id="error_ds_init_failure_console"></span>**ERROR\_DS\_INIT\_FAILURE\_CONSOLE**
   

8561 (0x2171)
 



Directory Services could not start because of the following error: %1. Error Status: 0x%2. Please click OK to shutdown the system. You can use the recovery console to diagnose the system further.


   

<span id="ERROR_DS_SAM_INIT_FAILURE_CONSOLE"></span><span id="error_ds_sam_init_failure_console"></span>**ERROR\_DS\_SAM\_INIT\_FAILURE\_CONSOLE**
   

8562 (0x2172)
 



Security Accounts Manager initialization failed because of the following error: %1. Error Status: 0x%2. Please click OK to shutdown the system. You can use the recovery console to diagnose the system further.


   

<span id="ERROR_DS_FOREST_VERSION_TOO_HIGH"></span><span id="error_ds_forest_version_too_high"></span>**ERROR\_DS\_FOREST\_VERSION\_TOO\_HIGH**
   

8563 (0x2173)
 



The version of the operating system is incompatible with the current AD DS forest functional level or AD LDS Configuration Set functional level. You must upgrade to a new version of the operating system before this server can become an AD DS Domain Controller or add an AD LDS Instance in this AD DS Forest or AD LDS Configuration Set.


   

<span id="ERROR_DS_DOMAIN_VERSION_TOO_HIGH"></span><span id="error_ds_domain_version_too_high"></span>**ERROR\_DS\_DOMAIN\_VERSION\_TOO\_HIGH**
   

8564 (0x2174)
 



The version of the operating system installed is incompatible with the current domain functional level. You must upgrade to a new version of the operating system before this server can become a domain controller in this domain.


   

<span id="ERROR_DS_FOREST_VERSION_TOO_LOW"></span><span id="error_ds_forest_version_too_low"></span>**ERROR\_DS\_FOREST\_VERSION\_TOO\_LOW**
   

8565 (0x2175)
 



The version of the operating system installed on this server no longer supports the current AD DS Forest functional level or AD LDS Configuration Set functional level. You must raise the AD DS Forest functional level or AD LDS Configuration Set functional level before this server can become an AD DS Domain Controller or an AD LDS Instance in this Forest or Configuration Set.


   

<span id="ERROR_DS_DOMAIN_VERSION_TOO_LOW"></span><span id="error_ds_domain_version_too_low"></span>**ERROR\_DS\_DOMAIN\_VERSION\_TOO\_LOW**
   

8566 (0x2176)
 



The version of the operating system installed on this server no longer supports the current domain functional level. You must raise the domain functional level before this server can become a domain controller in this domain.


   

<span id="ERROR_DS_INCOMPATIBLE_VERSION"></span><span id="error_ds_incompatible_version"></span>**ERROR\_DS\_INCOMPATIBLE\_VERSION**
   

8567 (0x2177)
 



The version of the operating system installed on this server is incompatible with the functional level of the domain or forest.


   

<span id="ERROR_DS_LOW_DSA_VERSION"></span><span id="error_ds_low_dsa_version"></span>**ERROR\_DS\_LOW\_DSA\_VERSION**
   

8568 (0x2178)
 



The functional level of the domain (or forest) cannot be raised to the requested value, because there exist one or more domain controllers in the domain (or forest) that are at a lower incompatible functional level.


   

<span id="ERROR_DS_NO_BEHAVIOR_VERSION_IN_MIXEDDOMAIN"></span><span id="error_ds_no_behavior_version_in_mixeddomain"></span>**ERROR\_DS\_NO\_BEHAVIOR\_VERSION\_IN\_MIXEDDOMAIN**
   

8569 (0x2179)
 



The forest functional level cannot be raised to the requested value since one or more domains are still in mixed domain mode. All domains in the forest must be in native mode, for you to raise the forest functional level.


   

<span id="ERROR_DS_NOT_SUPPORTED_SORT_ORDER"></span><span id="error_ds_not_supported_sort_order"></span>**ERROR\_DS\_NOT\_SUPPORTED\_SORT\_ORDER**
   

8570 (0x217A)
 



The sort order requested is not supported.


   

<span id="ERROR_DS_NAME_NOT_UNIQUE"></span><span id="error_ds_name_not_unique"></span>**ERROR\_DS\_NAME\_NOT\_UNIQUE**
   

8571 (0x217B)
 



The requested name already exists as a unique identifier.


   

<span id="ERROR_DS_MACHINE_ACCOUNT_CREATED_PRENT4"></span><span id="error_ds_machine_account_created_prent4"></span>**ERROR\_DS\_MACHINE\_ACCOUNT\_CREATED\_PRENT4**
   

8572 (0x217C)
 



The machine account was created pre-NT4. The account needs to be recreated.


   

<span id="ERROR_DS_OUT_OF_VERSION_STORE"></span><span id="error_ds_out_of_version_store"></span>**ERROR\_DS\_OUT\_OF\_VERSION\_STORE**
   

8573 (0x217D)
 



The database is out of version store.


   

<span id="ERROR_DS_INCOMPATIBLE_CONTROLS_USED"></span><span id="error_ds_incompatible_controls_used"></span>**ERROR\_DS\_INCOMPATIBLE\_CONTROLS\_USED**
   

8574 (0x217E)
 



Unable to continue operation because multiple conflicting controls were used.


   

<span id="ERROR_DS_NO_REF_DOMAIN"></span><span id="error_ds_no_ref_domain"></span>**ERROR\_DS\_NO\_REF\_DOMAIN**
   

8575 (0x217F)
 



Unable to find a valid security descriptor reference domain for this partition.


   

<span id="ERROR_DS_RESERVED_LINK_ID"></span><span id="error_ds_reserved_link_id"></span>**ERROR\_DS\_RESERVED\_LINK\_ID**
   

8576 (0x2180)
 



Schema update failed: The link identifier is reserved.


   

<span id="ERROR_DS_LINK_ID_NOT_AVAILABLE"></span><span id="error_ds_link_id_not_available"></span>**ERROR\_DS\_LINK\_ID\_NOT\_AVAILABLE**
   

8577 (0x2181)
 



Schema update failed: There are no link identifiers available.


   

<span id="ERROR_DS_AG_CANT_HAVE_UNIVERSAL_MEMBER"></span><span id="error_ds_ag_cant_have_universal_member"></span>**ERROR\_DS\_AG\_CANT\_HAVE\_UNIVERSAL\_MEMBER**
   

8578 (0x2182)
 



An account group cannot have a universal group as a member.


   

<span id="ERROR_DS_MODIFYDN_DISALLOWED_BY_INSTANCE_TYPE"></span><span id="error_ds_modifydn_disallowed_by_instance_type"></span>**ERROR\_DS\_MODIFYDN\_DISALLOWED\_BY\_INSTANCE\_TYPE**
   

8579 (0x2183)
 



Rename or move operations on naming context heads or read-only objects are not allowed.


   

<span id="ERROR_DS_NO_OBJECT_MOVE_IN_SCHEMA_NC"></span><span id="error_ds_no_object_move_in_schema_nc"></span>**ERROR\_DS\_NO\_OBJECT\_MOVE\_IN\_SCHEMA\_NC**
   

8580 (0x2184)
 



Move operations on objects in the schema naming context are not allowed.


   

<span id="ERROR_DS_MODIFYDN_DISALLOWED_BY_FLAG"></span><span id="error_ds_modifydn_disallowed_by_flag"></span>**ERROR\_DS\_MODIFYDN\_DISALLOWED\_BY\_FLAG**
   

8581 (0x2185)
 



A system flag has been set on the object and does not allow the object to be moved or renamed.


   

<span id="ERROR_DS_MODIFYDN_WRONG_GRANDPARENT"></span><span id="error_ds_modifydn_wrong_grandparent"></span>**ERROR\_DS\_MODIFYDN\_WRONG\_GRANDPARENT**
   

8582 (0x2186)
 



This object is not allowed to change its grandparent container. Moves are not forbidden on this object, but are restricted to sibling containers.


   

<span id="ERROR_DS_NAME_ERROR_TRUST_REFERRAL"></span><span id="error_ds_name_error_trust_referral"></span>**ERROR\_DS\_NAME\_ERROR\_TRUST\_REFERRAL**
   

8583 (0x2187)
 



Unable to resolve completely, a referral to another forest is generated.


   

<span id="ERROR_NOT_SUPPORTED_ON_STANDARD_SERVER"></span><span id="error_not_supported_on_standard_server"></span>**ERROR\_NOT\_SUPPORTED\_ON\_STANDARD\_SERVER**
   

8584 (0x2188)
 



The requested action is not supported on standard server.


   

<span id="ERROR_DS_CANT_ACCESS_REMOTE_PART_OF_AD"></span><span id="error_ds_cant_access_remote_part_of_ad"></span>**ERROR\_DS\_CANT\_ACCESS\_REMOTE\_PART\_OF\_AD**
   

8585 (0x2189)
 



Could not access a partition of the directory service located on a remote server. Make sure at least one server is running for the partition in question.


   

<span id="ERROR_DS_CR_IMPOSSIBLE_TO_VALIDATE_V2"></span><span id="error_ds_cr_impossible_to_validate_v2"></span>**ERROR\_DS\_CR\_IMPOSSIBLE\_TO\_VALIDATE\_V2**
   

8586 (0x218A)
 



The directory cannot validate the proposed naming context (or partition) name because it does not hold a replica nor can it contact a replica of the naming context above the proposed naming context. Please ensure that the parent naming context is properly registered in DNS, and at least one replica of this naming context is reachable by the Domain Naming master.


   

<span id="ERROR_DS_THREAD_LIMIT_EXCEEDED"></span><span id="error_ds_thread_limit_exceeded"></span>**ERROR\_DS\_THREAD\_LIMIT\_EXCEEDED**
   

8587 (0x218B)
 



The thread limit for this request was exceeded.


   

<span id="ERROR_DS_NOT_CLOSEST"></span><span id="error_ds_not_closest"></span>**ERROR\_DS\_NOT\_CLOSEST**
   

8588 (0x218C)
 



The Global catalog server is not in the closest site.


   

<span id="ERROR_DS_CANT_DERIVE_SPN_WITHOUT_SERVER_REF"></span><span id="error_ds_cant_derive_spn_without_server_ref"></span>**ERROR\_DS\_CANT\_DERIVE\_SPN\_WITHOUT\_SERVER\_REF**
   

8589 (0x218D)
 



The DS cannot derive a service principal name (SPN) with which to mutually authenticate the target server because the corresponding server object in the local DS database has no serverReference attribute.


   

<span id="ERROR_DS_SINGLE_USER_MODE_FAILED"></span><span id="error_ds_single_user_mode_failed"></span>**ERROR\_DS\_SINGLE\_USER\_MODE\_FAILED**
   

8590 (0x218E)
 



The Directory Service failed to enter single user mode.


   

<span id="ERROR_DS_NTDSCRIPT_SYNTAX_ERROR"></span><span id="error_ds_ntdscript_syntax_error"></span>**ERROR\_DS\_NTDSCRIPT\_SYNTAX\_ERROR**
   

8591 (0x218F)
 



The Directory Service cannot parse the script because of a syntax error.


   

<span id="ERROR_DS_NTDSCRIPT_PROCESS_ERROR"></span><span id="error_ds_ntdscript_process_error"></span>**ERROR\_DS\_NTDSCRIPT\_PROCESS\_ERROR**
   

8592 (0x2190)
 



The Directory Service cannot process the script because of an error.


   

<span id="ERROR_DS_DIFFERENT_REPL_EPOCHS"></span><span id="error_ds_different_repl_epochs"></span>**ERROR\_DS\_DIFFERENT\_REPL\_EPOCHS**
   

8593 (0x2191)
 



The directory service cannot perform the requested operation because the servers involved are of different replication epochs (which is usually related to a domain rename that is in progress).


   

<span id="ERROR_DS_DRS_EXTENSIONS_CHANGED"></span><span id="error_ds_drs_extensions_changed"></span>**ERROR\_DS\_DRS\_EXTENSIONS\_CHANGED**
   

8594 (0x2192)
 



The directory service binding must be renegotiated due to a change in the server extensions information.


   

<span id="ERROR_DS_REPLICA_SET_CHANGE_NOT_ALLOWED_ON_DISABLED_CR"></span><span id="error_ds_replica_set_change_not_allowed_on_disabled_cr"></span>**ERROR\_DS\_REPLICA\_SET\_CHANGE\_NOT\_ALLOWED\_ON\_DISABLED\_CR**
   

8595 (0x2193)
 



Operation not allowed on a disabled cross ref.


   

<span id="ERROR_DS_NO_MSDS_INTID"></span><span id="error_ds_no_msds_intid"></span>**ERROR\_DS\_NO\_MSDS\_INTID**
   

8596 (0x2194)
 



Schema update failed: No values for msDS-IntId are available.


   

<span id="ERROR_DS_DUP_MSDS_INTID"></span><span id="error_ds_dup_msds_intid"></span>**ERROR\_DS\_DUP\_MSDS\_INTID**
   

8597 (0x2195)
 



Schema update failed: Duplicate msDS-INtId. Retry the operation.


   

<span id="ERROR_DS_EXISTS_IN_RDNATTID"></span><span id="error_ds_exists_in_rdnattid"></span>**ERROR\_DS\_EXISTS\_IN\_RDNATTID**
   

8598 (0x2196)
 



Schema deletion failed: attribute is used in rDNAttID.


   

<span id="ERROR_DS_AUTHORIZATION_FAILED"></span><span id="error_ds_authorization_failed"></span>**ERROR\_DS\_AUTHORIZATION\_FAILED**
   

8599 (0x2197)
 



The directory service failed to authorize the request.


   

<span id="ERROR_DS_INVALID_SCRIPT"></span><span id="error_ds_invalid_script"></span>**ERROR\_DS\_INVALID\_SCRIPT**
   

8600 (0x2198)
 



The Directory Service cannot process the script because it is invalid.


   

<span id="ERROR_DS_REMOTE_CROSSREF_OP_FAILED"></span><span id="error_ds_remote_crossref_op_failed"></span>**ERROR\_DS\_REMOTE\_CROSSREF\_OP\_FAILED**
   

8601 (0x2199)
 



The remote create cross reference operation failed on the Domain Naming Master FSMO. The operation's error is in the extended data.


   

<span id="ERROR_DS_CROSS_REF_BUSY"></span><span id="error_ds_cross_ref_busy"></span>**ERROR\_DS\_CROSS\_REF\_BUSY**
   

8602 (0x219A)
 



A cross reference is in use locally with the same name.


   

<span id="ERROR_DS_CANT_DERIVE_SPN_FOR_DELETED_DOMAIN"></span><span id="error_ds_cant_derive_spn_for_deleted_domain"></span>**ERROR\_DS\_CANT\_DERIVE\_SPN\_FOR\_DELETED\_DOMAIN**
   

8603 (0x219B)
 



The DS cannot derive a service principal name (SPN) with which to mutually authenticate the target server because the server's domain has been deleted from the forest.


   

<span id="ERROR_DS_CANT_DEMOTE_WITH_WRITEABLE_NC"></span><span id="error_ds_cant_demote_with_writeable_nc"></span>**ERROR\_DS\_CANT\_DEMOTE\_WITH\_WRITEABLE\_NC**
   

8604 (0x219C)
 



Writeable NCs prevent this DC from demoting.


   

<span id="ERROR_DS_DUPLICATE_ID_FOUND"></span><span id="error_ds_duplicate_id_found"></span>**ERROR\_DS\_DUPLICATE\_ID\_FOUND**
   

8605 (0x219D)
 



The requested object has a non-unique identifier and cannot be retrieved.


   

<span id="ERROR_DS_INSUFFICIENT_ATTR_TO_CREATE_OBJECT"></span><span id="error_ds_insufficient_attr_to_create_object"></span>**ERROR\_DS\_INSUFFICIENT\_ATTR\_TO\_CREATE\_OBJECT**
   

8606 (0x219E)
 



Insufficient attributes were given to create an object. This object may not exist because it may have been deleted and already garbage collected.


   

<span id="ERROR_DS_GROUP_CONVERSION_ERROR"></span><span id="error_ds_group_conversion_error"></span>**ERROR\_DS\_GROUP\_CONVERSION\_ERROR**
   

8607 (0x219F)
 



The group cannot be converted due to attribute restrictions on the requested group type.


   

<span id="ERROR_DS_CANT_MOVE_APP_BASIC_GROUP"></span><span id="error_ds_cant_move_app_basic_group"></span>**ERROR\_DS\_CANT\_MOVE\_APP\_BASIC\_GROUP**
   

8608 (0x21A0)
 



Cross-domain move of non-empty basic application groups is not allowed.


   

<span id="ERROR_DS_CANT_MOVE_APP_QUERY_GROUP"></span><span id="error_ds_cant_move_app_query_group"></span>**ERROR\_DS\_CANT\_MOVE\_APP\_QUERY\_GROUP**
   

8609 (0x21A1)
 



Cross-domain move of non-empty query based application groups is not allowed.


   

<span id="ERROR_DS_ROLE_NOT_VERIFIED"></span><span id="error_ds_role_not_verified"></span>**ERROR\_DS\_ROLE\_NOT\_VERIFIED**
   

8610 (0x21A2)
 



The FSMO role ownership could not be verified because its directory partition has not replicated successfully with at least one replication partner.


   

<span id="ERROR_DS_WKO_CONTAINER_CANNOT_BE_SPECIAL"></span><span id="error_ds_wko_container_cannot_be_special"></span>**ERROR\_DS\_WKO\_CONTAINER\_CANNOT\_BE\_SPECIAL**
   

8611 (0x21A3)
 



The target container for a redirection of a well known object container cannot already be a special container.


   

<span id="ERROR_DS_DOMAIN_RENAME_IN_PROGRESS"></span><span id="error_ds_domain_rename_in_progress"></span>**ERROR\_DS\_DOMAIN\_RENAME\_IN\_PROGRESS**
   

8612 (0x21A4)
 



The Directory Service cannot perform the requested operation because a domain rename operation is in progress.


   

<span id="ERROR_DS_EXISTING_AD_CHILD_NC"></span><span id="error_ds_existing_ad_child_nc"></span>**ERROR\_DS\_EXISTING\_AD\_CHILD\_NC**
   

8613 (0x21A5)
 



The directory service detected a child partition below the requested partition name. The partition hierarchy must be created in a top down method.


   

<span id="ERROR_DS_REPL_LIFETIME_EXCEEDED"></span><span id="error_ds_repl_lifetime_exceeded"></span>**ERROR\_DS\_REPL\_LIFETIME\_EXCEEDED**
   

8614 (0x21A6)
 



The directory service cannot replicate with this server because the time since the last replication with this server has exceeded the tombstone lifetime.


   

<span id="ERROR_DS_DISALLOWED_IN_SYSTEM_CONTAINER"></span><span id="error_ds_disallowed_in_system_container"></span>**ERROR\_DS\_DISALLOWED\_IN\_SYSTEM\_CONTAINER**
   

8615 (0x21A7)
 



The requested operation is not allowed on an object under the system container.


   

<span id="ERROR_DS_LDAP_SEND_QUEUE_FULL"></span><span id="error_ds_ldap_send_queue_full"></span>**ERROR\_DS\_LDAP\_SEND\_QUEUE\_FULL**
   

8616 (0x21A8)
 



The LDAP servers network send queue has filled up because the client is not processing the results of its requests fast enough. No more requests will be processed until the client catches up. If the client does not catch up then it will be disconnected.


   

<span id="ERROR_DS_DRA_OUT_SCHEDULE_WINDOW"></span><span id="error_ds_dra_out_schedule_window"></span>**ERROR\_DS\_DRA\_OUT\_SCHEDULE\_WINDOW**
   

8617 (0x21A9)
 



The scheduled replication did not take place because the system was too busy to execute the request within the schedule window. The replication queue is overloaded. Consider reducing the number of partners or decreasing the scheduled replication frequency.


   

<span id="ERROR_DS_POLICY_NOT_KNOWN"></span><span id="error_ds_policy_not_known"></span>**ERROR\_DS\_POLICY\_NOT\_KNOWN**
   

8618 (0x21AA)
 



At this time, it cannot be determined if the branch replication policy is available on the hub domain controller. Please retry at a later time to account for replication latencies.


   

<span id="ERROR_NO_SITE_SETTINGS_OBJECT"></span><span id="error_no_site_settings_object"></span>**ERROR\_NO\_SITE\_SETTINGS\_OBJECT**
   

8619 (0x21AB)
 



The site settings object for the specified site does not exist.


   

<span id="ERROR_NO_SECRETS"></span><span id="error_no_secrets"></span>**ERROR\_NO\_SECRETS**
   

8620 (0x21AC)
 



The local account store does not contain secret material for the specified account.


   

<span id="ERROR_NO_WRITABLE_DC_FOUND"></span><span id="error_no_writable_dc_found"></span>**ERROR\_NO\_WRITABLE\_DC\_FOUND**
   

8621 (0x21AD)
 



Could not find a writable domain controller in the domain.


   

<span id="ERROR_DS_NO_SERVER_OBJECT"></span><span id="error_ds_no_server_object"></span>**ERROR\_DS\_NO\_SERVER\_OBJECT**
   

8622 (0x21AE)
 



The server object for the domain controller does not exist.


   

<span id="ERROR_DS_NO_NTDSA_OBJECT"></span><span id="error_ds_no_ntdsa_object"></span>**ERROR\_DS\_NO\_NTDSA\_OBJECT**
   

8623 (0x21AF)
 



The NTDS Settings object for the domain controller does not exist.


   

<span id="ERROR_DS_NON_ASQ_SEARCH"></span><span id="error_ds_non_asq_search"></span>**ERROR\_DS\_NON\_ASQ\_SEARCH**
   

8624 (0x21B0)
 



The requested search operation is not supported for ASQ searches.


   

<span id="ERROR_DS_AUDIT_FAILURE"></span><span id="error_ds_audit_failure"></span>**ERROR\_DS\_AUDIT\_FAILURE**
   

8625 (0x21B1)
 



A required audit event could not be generated for the operation.


   

<span id="ERROR_DS_INVALID_SEARCH_FLAG_SUBTREE"></span><span id="error_ds_invalid_search_flag_subtree"></span>**ERROR\_DS\_INVALID\_SEARCH\_FLAG\_SUBTREE**
   

8626 (0x21B2)
 



The search flags for the attribute are invalid. The subtree index bit is valid only on single valued attributes.


   

<span id="ERROR_DS_INVALID_SEARCH_FLAG_TUPLE"></span><span id="error_ds_invalid_search_flag_tuple"></span>**ERROR\_DS\_INVALID\_SEARCH\_FLAG\_TUPLE**
   

8627 (0x21B3)
 



The search flags for the attribute are invalid. The tuple index bit is valid only on attributes of Unicode strings.


   

<span id="ERROR_DS_HIERARCHY_TABLE_TOO_DEEP"></span><span id="error_ds_hierarchy_table_too_deep"></span>**ERROR\_DS\_HIERARCHY\_TABLE\_TOO\_DEEP**
   

8628 (0x21B4)
 



The address books are nested too deeply. Failed to build the hierarchy table.


   

<span id="ERROR_DS_DRA_CORRUPT_UTD_VECTOR"></span><span id="error_ds_dra_corrupt_utd_vector"></span>**ERROR\_DS\_DRA\_CORRUPT\_UTD\_VECTOR**
   

8629 (0x21B5)
 



The specified up-to-date-ness vector is corrupt.


   

<span id="ERROR_DS_DRA_SECRETS_DENIED"></span><span id="error_ds_dra_secrets_denied"></span>**ERROR\_DS\_DRA\_SECRETS\_DENIED**
   

8630 (0x21B6)
 



The request to replicate secrets is denied.


   

<span id="ERROR_DS_RESERVED_MAPI_ID"></span><span id="error_ds_reserved_mapi_id"></span>**ERROR\_DS\_RESERVED\_MAPI\_ID**
   

8631 (0x21B7)
 



Schema update failed: The MAPI identifier is reserved.


   

<span id="ERROR_DS_MAPI_ID_NOT_AVAILABLE"></span><span id="error_ds_mapi_id_not_available"></span>**ERROR\_DS\_MAPI\_ID\_NOT\_AVAILABLE**
   

8632 (0x21B8)
 



Schema update failed: There are no MAPI identifiers available.


   

<span id="ERROR_DS_DRA_MISSING_KRBTGT_SECRET"></span><span id="error_ds_dra_missing_krbtgt_secret"></span>**ERROR\_DS\_DRA\_MISSING\_KRBTGT\_SECRET**
   

8633 (0x21B9)
 



The replication operation failed because the required attributes of the local krbtgt object are missing.


   

<span id="ERROR_DS_DOMAIN_NAME_EXISTS_IN_FOREST"></span><span id="error_ds_domain_name_exists_in_forest"></span>**ERROR\_DS\_DOMAIN\_NAME\_EXISTS\_IN\_FOREST**
   

8634 (0x21BA)
 



The domain name of the trusted domain already exists in the forest.


   

<span id="ERROR_DS_FLAT_NAME_EXISTS_IN_FOREST"></span><span id="error_ds_flat_name_exists_in_forest"></span>**ERROR\_DS\_FLAT\_NAME\_EXISTS\_IN\_FOREST**
   

8635 (0x21BB)
 



The flat name of the trusted domain already exists in the forest.


   

<span id="ERROR_INVALID_USER_PRINCIPAL_NAME"></span><span id="error_invalid_user_principal_name"></span>**ERROR\_INVALID\_USER\_PRINCIPAL\_NAME**
   

8636 (0x21BC)
 



The User Principal Name (UPN) is invalid.


   

<span id="ERROR_DS_OID_MAPPED_GROUP_CANT_HAVE_MEMBERS"></span><span id="error_ds_oid_mapped_group_cant_have_members"></span>**ERROR\_DS\_OID\_MAPPED\_GROUP\_CANT\_HAVE\_MEMBERS**
   

8637 (0x21BD)
 



OID mapped groups cannot have members.


   

<span id="ERROR_DS_OID_NOT_FOUND"></span><span id="error_ds_oid_not_found"></span>**ERROR\_DS\_OID\_NOT\_FOUND**
   

8638 (0x21BE)
 



The specified OID cannot be found.


   

<span id="ERROR_DS_DRA_RECYCLED_TARGET"></span><span id="error_ds_dra_recycled_target"></span>**ERROR\_DS\_DRA\_RECYCLED\_TARGET**
   

8639 (0x21BF)
 



The replication operation failed because the target object referred by a link value is recycled.


   

<span id="ERROR_DS_DISALLOWED_NC_REDIRECT"></span><span id="error_ds_disallowed_nc_redirect"></span>**ERROR\_DS\_DISALLOWED\_NC\_REDIRECT**
   

8640 (0x21C0)
 



The redirect operation failed because the target object is in a NC different from the domain NC of the current domain controller.


   

<span id="ERROR_DS_HIGH_ADLDS_FFL"></span><span id="error_ds_high_adlds_ffl"></span>**ERROR\_DS\_HIGH\_ADLDS\_FFL**
   

8641 (0x21C1)
 



The functional level of the AD LDS configuration set cannot be lowered to the requested value.


   

<span id="ERROR_DS_HIGH_DSA_VERSION"></span><span id="error_ds_high_dsa_version"></span>**ERROR\_DS\_HIGH\_DSA\_VERSION**
   

8642 (0x21C2)
 



The functional level of the domain (or forest) cannot be lowered to the requested value.


   

<span id="ERROR_DS_LOW_ADLDS_FFL"></span><span id="error_ds_low_adlds_ffl"></span>**ERROR\_DS\_LOW\_ADLDS\_FFL**
   

8643 (0x21C3)
 



The functional level of the AD LDS configuration set cannot be raised to the requested value, because there exist one or more ADLDS instances that are at a lower incompatible functional level.


   

<span id="ERROR_DOMAIN_SID_SAME_AS_LOCAL_WORKSTATION"></span><span id="error_domain_sid_same_as_local_workstation"></span>**ERROR\_DOMAIN\_SID\_SAME\_AS\_LOCAL\_WORKSTATION**
   

8644 (0x21C4)
 



The domain join cannot be completed because the SID of the domain you attempted to join was identical to the SID of this machine. This is a symptom of an improperly cloned operating system install. You should run sysprep on this machine in order to generate a new machine SID. Please see <https://go.microsoft.com/fwlink/p/?linkid=168895> for more information.


   

<span id="ERROR_DS_UNDELETE_SAM_VALIDATION_FAILED"></span><span id="error_ds_undelete_sam_validation_failed"></span>**ERROR\_DS\_UNDELETE\_SAM\_VALIDATION\_FAILED**
   

8645 (0x21C5)
 



The undelete operation failed because the Sam Account Name or Additional Sam Account Name of the object being undeleted conflicts with an existing live object.


   

<span id="ERROR_INCORRECT_ACCOUNT_TYPE"></span><span id="error_incorrect_account_type"></span>**ERROR\_INCORRECT\_ACCOUNT\_TYPE**
   

8646 (0x21C6)
 



The system is not authoritative for the specified account and therefore cannot complete the operation. Please retry the operation using the provider associated with this account. If this is an online provider please use the provider's online site.


   


## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   |  WinError.h  |



## See also

 

[System Error Codes](system-error-codes.md)
 

 

 




