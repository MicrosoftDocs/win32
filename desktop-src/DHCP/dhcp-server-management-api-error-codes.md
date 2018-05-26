---
title: DHCP Server Management API Error Codes
description: The following error codes are returned by DHCP Server Management API functions.
ms.assetid: 6370313f-d7db-4ff1-b0e0-7fa47474facb
topic_type:
- apiref
api_name:
- ERROR_DHCP_REGISTRY_INIT_FAILED
- ERROR_DHCP_DATABASE_INIT_FAILED
- ERROR_DHCP_RPC_INIT_FAILED
- ERROR_DHCP_NETWORK_INIT_FAILED
- ERROR_DHCP_SUBNET_EXISTS
- ERROR_DHCP_SUBNET_NOT_PRESENT
- ERROR_DHCP_PRIMARY_NOT_FOUND
- ERROR_DHCP_ELEMENT_CANT_REMOVE
- ERROR_DHCP_OPTION_EXISTS
- ERROR_DHCP_OPTION_NOT_PRESENT
- ERROR_DHCP_ADDRESS_NOT_AVAILABLE
- ERROR_DHCP_RANGE_FULL
- ERROR_DHCP_JET_ERROR
- ERROR_DHCP_CLIENT_EXISTS
- ERROR_DHCP_INVALID_DHCP_MESSAGE
- ERROR_DHCP_INVALID_DHCP_CLIENT
- ERROR_DHCP_SERVICE_PAUSED
- ERROR_DHCP_NOT_RESERVED_CLIENT
- ERROR_DHCP_RESERVED_CLIENT
- ERROR_DHCP_RANGE_TOO_SMALL
- ERROR_DHCP_IPRANGE_EXISTS
- ERROR_DHCP_RESERVEDIP_EXISTS
- ERROR_DHCP_INVALID_RANGE
- ERROR_DHCP_RANGE_EXTENDED
- ERROR_DHCP_RANGE_EXTENSION_TOO_SMALL
- ERROR_DHCP_WARNING_RANGE_EXTENDED_LESS
- ERROR_DHCP_JET_CONV_REQUIRED
- ERROR_DHCP_SERVER_INVALID_BOOT_FILE_TABLE
- ERROR_DHCP_SERVER_UNKNOWN_BOOT_FILE_NAME
- ERROR_DHCP_SUPER_SCOPE_NAME_TOO_LONG
- ERROR_DHCP_IP_ADDRESS_IN_USE
- ERROR_DHCP_LOG_FILE_PATH_TOO_LONG
- ERROR_DHCP_UNSUPPORTED_CLIENT
- ERROR_DHCP_SERVER_INTERFACE_NOTIFICATION_EVENT
- ERROR_DHCP_JET97_CONV_REQUIRED
- ERROR_DHCP_ROGUE_INIT_FAILED
- ERROR_DHCP_ROGUE_SAMSHUTDOWN
- ERROR_DHCP_ROGUE_NOT_AUTHORIZED
- ERROR_DHCP_ROGUE_DS_UNREACHABLE
- ERROR_DHCP_ROGUE_DS_CONFLICT
- ERROR_DHCP_ROGUE_NOT_OUR_ENTERPRISE
- ERROR_DHCP_STANDALONE_IN_DS
- ERROR_DHCP_CLASS_NOT_FOUND
- ERROR_DHCP_CLASS_ALREADY_EXISTS
- ERROR_DHCP_SCOPE_NAME_TOO_LONG
- ERROR_DHCP_DEFAULT_SCOPE_EXISTS
- ERROR_DHCP_CANT_CHANGE_ATTRIBUTE
- ERROR_DHCP_IPRANGE_CONV_ILLEGAL
- ERROR_DHCP_NETWORK_CHANGED
- ERROR_DHCP_CANNOT_MODIFY_BINDINGS
- ERROR_DHCP_SUBNET_EXISTS
- ERROR_DHCP_MSCOPE_EXISTS
- ERROR_DHCP_MSCOPE_RANGE_TOO_SMALL
- ERROR_DDS_NO_DS_AVAILABLE
- ERROR_DDS_NO_DHCP_ROOT
- ERROR_DDS_UNEXPECTED_ERROR
- ERROR_DDS_TOO_MANY_ERRORS
- ERROR_DDS_DHCP_SERVER_NOT_FOUND
- ERROR_DDS_OPTION_ALREADY_EXISTS
- ERROR_DDS_OPTION_DOES_NOT_EXIST
- ERROR_DDS_CLASS_EXISTS
- ERROR_DDS_CLASS_DOES_NOT_EXIST
- ERROR_DDS_SERVER_ALREADY_EXISTS
- ERROR_DDS_SERVER_DOES_NOT_EXIST
- ERROR_DDS_SERVER_ADDRESS_MISMATCH
- ERROR_DDS_SUBNET_EXISTS
- ERROR_DDS_SUBNET_HAS_DIFF_SUPER_SCOPE
- ERROR_DDS_SUBNET_NOT_PRESENT
- ERROR_DDS_RESERVATION_NOT_PRESENT
- ERROR_DDS_RESERVATION_CONFLICT
- ERROR_DDS_POSSIBLE_RANGE_CONFLICT
- ERROR_DDS_RANGE_DOES_NOT_EXIST
- ERROR_DHCP_DELETE_BUILTIN_CLASS
- ERROR_DHCP_INVALID_SUBNET_PREFIX
- ERROR_DHCP_INVALID_DELAY
- ERROR_DHCP_LINKLAYER_ADDRESS_EXISTS
- ERROR_DHCP_LINKLAYER_ADDRESS_RESERVATION_EXISTS
- ERROR_DHCP_LINKLAYER_ADDRESS_DOES_NOT_EXIST
- ERROR_DHCP_HARDWARE_ADDRESS_TYPE_ALREADY_EXEMPT
- ERROR_DHCP_UNDEFINED_HARDWARE_ADDRESS_TYPE
- ERROR_DHCP_OPTION_TYPE_MISMATCH
- ERROR_DHCP_POLICY_BAD_PARENT_EXPR
- ERROR_DHCP_POLICY_EXISTS
- ERROR_DHCP_POLICY_RANGE_EXISTS
- ERROR_DHCP_POLICY_RANGE_BAD
- ERROR_DHCP_RANGE_INVALID_IN_SERVER_POLICY
- ERROR_DHCP_INVALID_POLICY_EXPRESSION
- ERROR_DHCP_INVALID_PROCESSING_ORDER
- ERROR_DHCP_POLICY_NOT_FOUND
- ERROR_SCOPE_RANGE_POLICY_RANGE_CONFLICT
- ERROR_DHCP_FO_SCOPE_ALREADY_IN_RELATIONSHIP
- ERROR_DHCP_FO_RELATIONSHIP_EXISTS
- ERROR_DHCP_FO_RELATIONSHIP_DOES_NOT_EXIST
- ERROR_DHCP_FO_SCOPE_NOT_IN_RELATIONSHIP
- ERROR_DHCP_FO_RELATION_IS_SECONDARY
- ERROR_DHCP_FO_NOT_SUPPORTED
- ERROR_DHCP_FO_TIME_OUT_OF_SYNC
- ERROR_DHCP_FO_STATE_NOT_NORMAL
- ERROR_DHCP_NO_ADMIN_PERMISSION
- ERROR_DHCP_SERVER_NOT_REACHABLE
- ERROR_DHCP_SERVER_NOT_RUNNING
- ERROR_DHCP_SERVER_NAME_NOT_RESOLVED
- ERROR_DHCP_FO_RELATIONSHIP_NAME_TOO_LONG
- ERROR_DHCP_REACHED_END_OF_SELECTION
- ERROR_DHCP_FO_ADDSCOPE_LEASES_NOT_SYNCED
- ERROR_DHCP_FO_MAX_RELATIONSHIPS
- ERROR_DHCP_FO_IPRANGE_TYPE_CONV_ILLEGAL
- ERROR_DHCP_FO_MAX_ADD_SCOPES
- ERROR_DHCP_FO_BOOT_NOT_SUPPORTED
- ERROR_DHCP_FO_RANGE_PART_OF_REL
api_location:
- Dhcpsapi.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DHCP Server Management API Error Codes

The following error codes are returned by DHCP Server Management API functions.

<dl> <dt>

<span id="ERROR_DHCP_REGISTRY_INIT_FAILED"></span><span id="error_dhcp_registry_init_failed"></span>**ERROR\_DHCP\_REGISTRY\_INIT\_FAILED**
</dt> <dd> <dl> <dt>

20000
</dt> <dt>



The DHCP server registry initialization parameters are incorrect.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_DATABASE_INIT_FAILED"></span><span id="error_dhcp_database_init_failed"></span>**ERROR\_DHCP\_DATABASE\_INIT\_FAILED**
</dt> <dd> <dl> <dt>

20001
</dt> <dt>



The DHCP server was unable to open the database of DHCP clients.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_RPC_INIT_FAILED"></span><span id="error_dhcp_rpc_init_failed"></span>**ERROR\_DHCP\_RPC\_INIT\_FAILED**
</dt> <dd> <dl> <dt>

20002
</dt> <dt>



The DHCP server was unable to start as a Remote Procedure Call (RPC) server.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_NETWORK_INIT_FAILED"></span><span id="error_dhcp_network_init_failed"></span>**ERROR\_DHCP\_NETWORK\_INIT\_FAILED**
</dt> <dd> <dl> <dt>

20003
</dt> <dt>



The DHCP server was unable to establish a socket connection.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_SUBNET_EXISTS"></span><span id="error_dhcp_subnet_exists"></span>**ERROR\_DHCP\_SUBNET\_EXISTS**
</dt> <dd> <dl> <dt>

20004
</dt> <dt>



The specified subnet already exists on the DHCP server.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_SUBNET_NOT_PRESENT"></span><span id="error_dhcp_subnet_not_present"></span>**ERROR\_DHCP\_SUBNET\_NOT\_PRESENT**
</dt> <dd> <dl> <dt>

20005
</dt> <dt>



The specified subnet does not exist on the DHCP server.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_PRIMARY_NOT_FOUND"></span><span id="error_dhcp_primary_not_found"></span>**ERROR\_DHCP\_PRIMARY\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

20006
</dt> <dt>



The primary host information for the specified subnet was not found on the DHCP server.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_ELEMENT_CANT_REMOVE"></span><span id="error_dhcp_element_cant_remove"></span>**ERROR\_DHCP\_ELEMENT\_CANT\_REMOVE**
</dt> <dd> <dl> <dt>

20007
</dt> <dt>



The specified DHCP element has been used by a client and cannot be removed.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_OPTION_EXISTS"></span><span id="error_dhcp_option_exists"></span>**ERROR\_DHCP\_OPTION\_EXISTS**
</dt> <dd> <dl> <dt>

20009
</dt> <dt>



The specified option already exists on the DHCP server.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_OPTION_NOT_PRESENT"></span><span id="error_dhcp_option_not_present"></span>**ERROR\_DHCP\_OPTION\_NOT\_PRESENT**
</dt> <dd> <dl> <dt>

20010
</dt> <dt>



The specified option does not exist on the DHCP server.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_ADDRESS_NOT_AVAILABLE"></span><span id="error_dhcp_address_not_available"></span>**ERROR\_DHCP\_ADDRESS\_NOT\_AVAILABLE**
</dt> <dd> <dl> <dt>

20011
</dt> <dt>



The specified IP address is not available.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_RANGE_FULL"></span><span id="error_dhcp_range_full"></span>**ERROR\_DHCP\_RANGE\_FULL**
</dt> <dd> <dl> <dt>

20012
</dt> <dt>



The specified IP address range has all of its member addresses leased.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_JET_ERROR"></span><span id="error_dhcp_jet_error"></span>**ERROR\_DHCP\_JET\_ERROR**
</dt> <dd> <dl> <dt>

20013
</dt> <dt>



An error occurred while accessing the DHCP JET database. For more information about this error, please look at the DHCP server event log.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_CLIENT_EXISTS"></span><span id="error_dhcp_client_exists"></span>**ERROR\_DHCP\_CLIENT\_EXISTS**
</dt> <dd> <dl> <dt>

20014
</dt> <dt>



The specified client already exists in the database.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_INVALID_DHCP_MESSAGE"></span><span id="error_dhcp_invalid_dhcp_message"></span>**ERROR\_DHCP\_INVALID\_DHCP\_MESSAGE**
</dt> <dd> <dl> <dt>

20015
</dt> <dt>



The DHCP server received an invalid message.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_INVALID_DHCP_CLIENT"></span><span id="error_dhcp_invalid_dhcp_client"></span>**ERROR\_DHCP\_INVALID\_DHCP\_CLIENT**
</dt> <dd> <dl> <dt>

20016
</dt> <dt>



The DHCP server received an invalid message from the client.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_SERVICE_PAUSED"></span><span id="error_dhcp_service_paused"></span>**ERROR\_DHCP\_SERVICE\_PAUSED**
</dt> <dd> <dl> <dt>

20017
</dt> <dt>



The DHCP server is currently paused.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_NOT_RESERVED_CLIENT"></span><span id="error_dhcp_not_reserved_client"></span>**ERROR\_DHCP\_NOT\_RESERVED\_CLIENT**
</dt> <dd> <dl> <dt>

20018
</dt> <dt>



The specified DHCP client is not a reserved client.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_RESERVED_CLIENT"></span><span id="error_dhcp_reserved_client"></span>**ERROR\_DHCP\_RESERVED\_CLIENT**
</dt> <dd> <dl> <dt>

20019
</dt> <dt>



The specified DHCP client is a reserved client.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_RANGE_TOO_SMALL"></span><span id="error_dhcp_range_too_small"></span>**ERROR\_DHCP\_RANGE\_TOO\_SMALL**
</dt> <dd> <dl> <dt>

20020
</dt> <dt>



The specified IP address range is too small.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_IPRANGE_EXISTS"></span><span id="error_dhcp_iprange_exists"></span>**ERROR\_DHCP\_IPRANGE\_EXISTS**
</dt> <dd> <dl> <dt>

20021
</dt> <dt>



The specified IP address range is already defined on the DHCP server.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_RESERVEDIP_EXISTS"></span><span id="error_dhcp_reservedip_exists"></span>**ERROR\_DHCP\_RESERVEDIP\_EXISTS**
</dt> <dd> <dl> <dt>

20022
</dt> <dt>



The specified IP address is currently taken by another client.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_INVALID_RANGE"></span><span id="error_dhcp_invalid_range"></span>**ERROR\_DHCP\_INVALID\_RANGE**
</dt> <dd> <dl> <dt>

20023
</dt> <dt>



The specified IP address range either overlaps with an existing range or is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_RANGE_EXTENDED"></span><span id="error_dhcp_range_extended"></span>**ERROR\_DHCP\_RANGE\_EXTENDED**
</dt> <dd> <dl> <dt>

20024
</dt> <dt>



The specified IP address range is an extension of an existing range.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_RANGE_EXTENSION_TOO_SMALL"></span><span id="error_dhcp_range_extension_too_small"></span>**ERROR\_DHCP\_RANGE\_EXTENSION\_TOO\_SMALL**
</dt> <dd> <dl> <dt>

20025
</dt> <dt>



The specified IP address range extension is too small. The number of addresses in the extension must be a multiple of 32.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_WARNING_RANGE_EXTENDED_LESS"></span><span id="error_dhcp_warning_range_extended_less"></span>**ERROR\_DHCP\_WARNING\_RANGE\_EXTENDED\_LESS**
</dt> <dd> <dl> <dt>

20026
</dt> <dt>



An attempt was made to extend the IP address range to a value less than the specified backward extension. The number of addresses in the extension must be a multiple of 32.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_JET_CONV_REQUIRED"></span><span id="error_dhcp_jet_conv_required"></span>**ERROR\_DHCP\_JET\_CONV\_REQUIRED**
</dt> <dd> <dl> <dt>

20027
</dt> <dt>



The DHCP database needs to be upgraded to a newer format. For more information, refer to the DHCP server event log.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_SERVER_INVALID_BOOT_FILE_TABLE"></span><span id="error_dhcp_server_invalid_boot_file_table"></span>**ERROR\_DHCP\_SERVER\_INVALID\_BOOT\_FILE\_TABLE**
</dt> <dd> <dl> <dt>

20028
</dt> <dt>



The format of the bootstrap protocol file table is incorrect. The correct format is:

``` syntax
<requested boot file name 1>,<boot file server name 1>, <boot file name 1>
<requested boot file name 2>,<boot file server name 2>, <boot file name 2>
...
```


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_SERVER_UNKNOWN_BOOT_FILE_NAME"></span><span id="error_dhcp_server_unknown_boot_file_name"></span>**ERROR\_DHCP\_SERVER\_UNKNOWN\_BOOT\_FILE\_NAME**
</dt> <dd> <dl> <dt>

20029
</dt> <dt>



A boot file name specified in the bootstrap protocol file table is unrecognized or invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_SUPER_SCOPE_NAME_TOO_LONG"></span><span id="error_dhcp_super_scope_name_too_long"></span>**ERROR\_DHCP\_SUPER\_SCOPE\_NAME\_TOO\_LONG**
</dt> <dd> <dl> <dt>

20030
</dt> <dt>



The specified superscope name is too long.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_IP_ADDRESS_IN_USE"></span><span id="error_dhcp_ip_address_in_use"></span>**ERROR\_DHCP\_IP\_ADDRESS\_IN\_USE**
</dt> <dd> <dl> <dt>

20032
</dt> <dt>



The specified IP address is already in use.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_LOG_FILE_PATH_TOO_LONG"></span><span id="error_dhcp_log_file_path_too_long"></span>**ERROR\_DHCP\_LOG\_FILE\_PATH\_TOO\_LONG**
</dt> <dd> <dl> <dt>

20033
</dt> <dt>



The specified path to the DHCP audit log file is too long.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_UNSUPPORTED_CLIENT"></span><span id="error_dhcp_unsupported_client"></span>**ERROR\_DHCP\_UNSUPPORTED\_CLIENT**
</dt> <dd> <dl> <dt>

20034
</dt> <dt>



The DHCP server received a request for a valid IP address not administered by the server.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_SERVER_INTERFACE_NOTIFICATION_EVENT"></span><span id="error_dhcp_server_interface_notification_event"></span>**ERROR\_DHCP\_SERVER\_INTERFACE\_NOTIFICATION\_EVENT**
</dt> <dd> <dl> <dt>

20035
</dt> <dt>



The DHCP server failed to receive a notification when the interface list changed, therefore some of the interfaces will not be enabled on the server.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_JET97_CONV_REQUIRED"></span><span id="error_dhcp_jet97_conv_required"></span>**ERROR\_DHCP\_JET97\_CONV\_REQUIRED**
</dt> <dd> <dl> <dt>

20036
</dt> <dt>



The DHCP database needs to be upgraded to a newer format (JET97). For more information, refer to the DHCP server event log.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_ROGUE_INIT_FAILED"></span><span id="error_dhcp_rogue_init_failed"></span>**ERROR\_DHCP\_ROGUE\_INIT\_FAILED**
</dt> <dd> <dl> <dt>

20037
</dt> <dt>



The DHCP server cannot determine if it has the authority to run, and is not servicing clients on the network. This rogue status may be due to network problems or insufficient server resources.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_ROGUE_SAMSHUTDOWN"></span><span id="error_dhcp_rogue_samshutdown"></span>**ERROR\_DHCP\_ROGUE\_SAMSHUTDOWN**
</dt> <dd> <dl> <dt>

20038
</dt> <dt>



The DHCP service is shutting down because another DHCP server is active on the network.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_ROGUE_NOT_AUTHORIZED"></span><span id="error_dhcp_rogue_not_authorized"></span>**ERROR\_DHCP\_ROGUE\_NOT\_AUTHORIZED**
</dt> <dd> <dl> <dt>

20039
</dt> <dt>



The DHCP server does not have the authority to run, and is not servicing clients on the network.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_ROGUE_DS_UNREACHABLE"></span><span id="error_dhcp_rogue_ds_unreachable"></span>**ERROR\_DHCP\_ROGUE\_DS\_UNREACHABLE**
</dt> <dd> <dl> <dt>

20040
</dt> <dt>



The DHCP server is unable to contact the directory service for this domain. The DHCP server will continue to attempt to contact the directory service. During this time, no clients on the network will be serviced.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_ROGUE_DS_CONFLICT"></span><span id="error_dhcp_rogue_ds_conflict"></span>**ERROR\_DHCP\_ROGUE\_DS\_CONFLICT**
</dt> <dd> <dl> <dt>

20041
</dt> <dt>



The DHCP server's authorization information conflicts with that of another DHCP server on the network.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_ROGUE_NOT_OUR_ENTERPRISE"></span><span id="error_dhcp_rogue_not_our_enterprise"></span>**ERROR\_DHCP\_ROGUE\_NOT\_OUR\_ENTERPRISE**
</dt> <dd> <dl> <dt>

20042
</dt> <dt>



The DHCP server is ignoring a request from another DHCP server because the second server is a member of a different directory service enterprise.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_STANDALONE_IN_DS"></span><span id="error_dhcp_standalone_in_ds"></span>**ERROR\_DHCP\_STANDALONE\_IN\_DS**
</dt> <dd> <dl> <dt>

20043
</dt> <dt>



The DHCP server has detected a directory service environment on the network. If there is a directory service on the network, the DHCP server can only run if it is a part of the directory service. Since the server ostensibly belongs to a workgroup, it is terminating.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_CLASS_NOT_FOUND"></span><span id="error_dhcp_class_not_found"></span>**ERROR\_DHCP\_CLASS\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

20044
</dt> <dt>



The specified DHCP class name is unknown or invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_CLASS_ALREADY_EXISTS"></span><span id="error_dhcp_class_already_exists"></span>**ERROR\_DHCP\_CLASS\_ALREADY\_EXISTS**
</dt> <dd> <dl> <dt>

20045
</dt> <dt>



The specified DHCP class name (or information) is already in use.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_SCOPE_NAME_TOO_LONG"></span><span id="error_dhcp_scope_name_too_long"></span>**ERROR\_DHCP\_SCOPE\_NAME\_TOO\_LONG**
</dt> <dd> <dl> <dt>

20046
</dt> <dt>



The specified DHCP scope name is too long; the scope name must not exceed 256 characters.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_DEFAULT_SCOPE_EXISTS"></span><span id="error_dhcp_default_scope_exists"></span>**ERROR\_DHCP\_DEFAULT\_SCOPE\_EXISTS**
</dt> <dd> <dl> <dt>

20047
</dt> <dt>



The default scope is already configured on the server.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_CANT_CHANGE_ATTRIBUTE"></span><span id="error_dhcp_cant_change_attribute"></span>**ERROR\_DHCP\_CANT\_CHANGE\_ATTRIBUTE**
</dt> <dd> <dl> <dt>

20048
</dt> <dt>



The Dynamic BOOTP attribute cannot be turned on or off.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_IPRANGE_CONV_ILLEGAL"></span><span id="error_dhcp_iprange_conv_illegal"></span>**ERROR\_DHCP\_IPRANGE\_CONV\_ILLEGAL**
</dt> <dd> <dl> <dt>

20049
</dt> <dt>



Conversion of a scope to a "DHCP Only" scope or to a "BOOTP Only" scope is not allowed when the scope contains other DHCP and BOOTP clients. Either the DHCP or BOOTP clients should be specifically deleted before converting the scope to the other type.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_NETWORK_CHANGED"></span><span id="error_dhcp_network_changed"></span>**ERROR\_DHCP\_NETWORK\_CHANGED**
</dt> <dd> <dl> <dt>

20050
</dt> <dt>



The network has changed. Retry this operation after checking for network changes. Network changes may be caused by interfaces that are new or invalid, or by IP addresses that are new or invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_CANNOT_MODIFY_BINDINGS"></span><span id="error_dhcp_cannot_modify_bindings"></span>**ERROR\_DHCP\_CANNOT\_MODIFY\_BINDINGS**
</dt> <dd> <dl> <dt>

20051
</dt> <dt>



The bindings to internal IP addresses cannot be modified.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_SUBNET_EXISTS"></span><span id="error_dhcp_subnet_exists"></span>**ERROR\_DHCP\_SUBNET\_EXISTS**
</dt> <dd> <dl> <dt>

20052
</dt> <dt>



The DHCP scope parameters are incorrect. Either the scope already exists, or its properties are inconsistent with the subnet address and mask of an existing scope.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_MSCOPE_EXISTS"></span><span id="error_dhcp_mscope_exists"></span>**ERROR\_DHCP\_MSCOPE\_EXISTS**
</dt> <dd> <dl> <dt>

20053
</dt> <dt>



The DHCP multicast scope parameters are incorrect. Either the scope already exists, or its properties are inconsistent with the subnet address and mask of an existing scope.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_MSCOPE_RANGE_TOO_SMALL"></span><span id="error_dhcp_mscope_range_too_small"></span>**ERROR\_DHCP\_MSCOPE\_RANGE\_TOO\_SMALL**
</dt> <dd> <dl> <dt>

20054
</dt> <dt>



The multicast scope range must have at least 256 IP addresses.


</dt> </dl> </dd> <dt>

<span id="ERROR_DDS_NO_DS_AVAILABLE"></span><span id="error_dds_no_ds_available"></span>**ERROR\_DDS\_NO\_DS\_AVAILABLE**
</dt> <dd> <dl> <dt>

20070
</dt> <dt>



The DHCP server could not contact Active Directory.


</dt> </dl> </dd> <dt>

<span id="ERROR_DDS_NO_DHCP_ROOT"></span><span id="error_dds_no_dhcp_root"></span>**ERROR\_DDS\_NO\_DHCP\_ROOT**
</dt> <dd> <dl> <dt>

20071
</dt> <dt>



The DHCP service root could not be found in Active Directory.


</dt> </dl> </dd> <dt>

<span id="ERROR_DDS_UNEXPECTED_ERROR"></span><span id="error_dds_unexpected_error"></span>**ERROR\_DDS\_UNEXPECTED\_ERROR**
</dt> <dd> <dl> <dt>

20072
</dt> <dt>



An unexpected error occurred while accessing Active Directory.


</dt> </dl> </dd> <dt>

<span id="ERROR_DDS_TOO_MANY_ERRORS"></span><span id="error_dds_too_many_errors"></span>**ERROR\_DDS\_TOO\_MANY\_ERRORS**
</dt> <dd> <dl> <dt>

20073
</dt> <dt>



There were too many errors to proceed.


</dt> </dl> </dd> <dt>

<span id="ERROR_DDS_DHCP_SERVER_NOT_FOUND"></span><span id="error_dds_dhcp_server_not_found"></span>**ERROR\_DDS\_DHCP\_SERVER\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

20074
</dt> <dt>



A DHCP service could not be found.


</dt> </dl> </dd> <dt>

<span id="ERROR_DDS_OPTION_ALREADY_EXISTS"></span><span id="error_dds_option_already_exists"></span>**ERROR\_DDS\_OPTION\_ALREADY\_EXISTS**
</dt> <dd> <dl> <dt>

20075
</dt> <dt>



The specified DHCP options are already present in Active Directory.


</dt> </dl> </dd> <dt>

<span id="ERROR_DDS_OPTION_DOES_NOT_EXIST"></span><span id="error_dds_option_does_not_exist"></span>**ERROR\_DDS\_OPTION\_DOES\_NOT\_EXIST**
</dt> <dd> <dl> <dt>

20076
</dt> <dt>



The specified DHCP options are not present in Active Directory.


</dt> </dl> </dd> <dt>

<span id="ERROR_DDS_CLASS_EXISTS"></span><span id="error_dds_class_exists"></span>**ERROR\_DDS\_CLASS\_EXISTS**
</dt> <dd> <dl> <dt>

20077
</dt> <dt>



The specified DHCP classes are already present in Active Directory.


</dt> </dl> </dd> <dt>

<span id="ERROR_DDS_CLASS_DOES_NOT_EXIST"></span><span id="error_dds_class_does_not_exist"></span>**ERROR\_DDS\_CLASS\_DOES\_NOT\_EXIST**
</dt> <dd> <dl> <dt>

20078
</dt> <dt>



The specified DHCP classes are not present in Active Directory.


</dt> </dl> </dd> <dt>

<span id="ERROR_DDS_SERVER_ALREADY_EXISTS"></span><span id="error_dds_server_already_exists"></span>**ERROR\_DDS\_SERVER\_ALREADY\_EXISTS**
</dt> <dd> <dl> <dt>

20079
</dt> <dt>



The specified DHCP servers are already present in Active Directory.


</dt> </dl> </dd> <dt>

<span id="ERROR_DDS_SERVER_DOES_NOT_EXIST"></span><span id="error_dds_server_does_not_exist"></span>**ERROR\_DDS\_SERVER\_DOES\_NOT\_EXIST**
</dt> <dd> <dl> <dt>

20080
</dt> <dt>



The specified DHCP servers are not present in Active Directory.


</dt> </dl> </dd> <dt>

<span id="ERROR_DDS_SERVER_ADDRESS_MISMATCH"></span><span id="error_dds_server_address_mismatch"></span>**ERROR\_DDS\_SERVER\_ADDRESS\_MISMATCH**
</dt> <dd> <dl> <dt>

20081
</dt> <dt>



The specified DHCP server address does not correspond to the identified DHCP server name.


</dt> </dl> </dd> <dt>

<span id="ERROR_DDS_SUBNET_EXISTS"></span><span id="error_dds_subnet_exists"></span>**ERROR\_DDS\_SUBNET\_EXISTS**
</dt> <dd> <dl> <dt>

20082
</dt> <dt>



The specified subnets are already present in Active Directory.


</dt> </dl> </dd> <dt>

<span id="ERROR_DDS_SUBNET_HAS_DIFF_SUPER_SCOPE"></span><span id="error_dds_subnet_has_diff_super_scope"></span>**ERROR\_DDS\_SUBNET\_HAS\_DIFF\_SUPER\_SCOPE**
</dt> <dd> <dl> <dt>

20083
</dt> <dt>



The specified subnet belongs to a different superscope.


</dt> </dl> </dd> <dt>

<span id="ERROR_DDS_SUBNET_NOT_PRESENT"></span><span id="error_dds_subnet_not_present"></span>**ERROR\_DDS\_SUBNET\_NOT\_PRESENT**
</dt> <dd> <dl> <dt>

20084
</dt> <dt>



The specified subnet is not present in Active Directory.


</dt> </dl> </dd> <dt>

<span id="ERROR_DDS_RESERVATION_NOT_PRESENT"></span><span id="error_dds_reservation_not_present"></span>**ERROR\_DDS\_RESERVATION\_NOT\_PRESENT**
</dt> <dd> <dl> <dt>

20085
</dt> <dt>



The specified reservation is not present in Active Directory.


</dt> </dl> </dd> <dt>

<span id="ERROR_DDS_RESERVATION_CONFLICT"></span><span id="error_dds_reservation_conflict"></span>**ERROR\_DDS\_RESERVATION\_CONFLICT**
</dt> <dd> <dl> <dt>

20086
</dt> <dt>



The specified reservation conflicts with another reservation present in Active Directory.


</dt> </dl> </dd> <dt>

<span id="ERROR_DDS_POSSIBLE_RANGE_CONFLICT"></span><span id="error_dds_possible_range_conflict"></span>**ERROR\_DDS\_POSSIBLE\_RANGE\_CONFLICT**
</dt> <dd> <dl> <dt>

20087
</dt> <dt>



The specified IP address range conflicts with another IP range present in Active Directory.


</dt> </dl> </dd> <dt>

<span id="ERROR_DDS_RANGE_DOES_NOT_EXIST"></span><span id="error_dds_range_does_not_exist"></span>**ERROR\_DDS\_RANGE\_DOES\_NOT\_EXIST**
</dt> <dd> <dl> <dt>

20088
</dt> <dt>



The specified IP address range is not present in Active Directory.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_DELETE_BUILTIN_CLASS"></span><span id="error_dhcp_delete_builtin_class"></span>**ERROR\_DHCP\_DELETE\_BUILTIN\_CLASS**
</dt> <dd> <dl> <dt>

20089
</dt> <dt>



Windows 7 or later: This class cannot be deleted.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_INVALID_SUBNET_PREFIX"></span><span id="error_dhcp_invalid_subnet_prefix"></span>**ERROR\_DHCP\_INVALID\_SUBNET\_PREFIX**
</dt> <dd> <dl> <dt>

20091
</dt> <dt>



Windows 7 or later: The given subnet prefix is invalid. It represents either a non-unicast or link local address range.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_INVALID_DELAY"></span><span id="error_dhcp_invalid_delay"></span>**ERROR\_DHCP\_INVALID\_DELAY**
</dt> <dd> <dl> <dt>

20092
</dt> <dt>



Windows 7 or later: The given delay value is invalid. The valid value is from 0 to 1000.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_LINKLAYER_ADDRESS_EXISTS"></span><span id="error_dhcp_linklayer_address_exists"></span>**ERROR\_DHCP\_LINKLAYER\_ADDRESS\_EXISTS**
</dt> <dd> <dl> <dt>

20093
</dt> <dt>



Windows 7 or later: Address or Address pattern is already contained in one of the list.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_LINKLAYER_ADDRESS_RESERVATION_EXISTS"></span><span id="error_dhcp_linklayer_address_reservation_exists"></span>**ERROR\_DHCP\_LINKLAYER\_ADDRESS\_RESERVATION\_EXISTS**
</dt> <dd> <dl> <dt>

20094
</dt> <dt>



Windows 7 or later: Address to be added to Deny list or to be deleted from allow list, has an associated reservation.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_LINKLAYER_ADDRESS_DOES_NOT_EXIST"></span><span id="error_dhcp_linklayer_address_does_not_exist"></span>**ERROR\_DHCP\_LINKLAYER\_ADDRESS\_DOES\_NOT\_EXIST**
</dt> <dd> <dl> <dt>

20095
</dt> <dt>



Windows 7 or later: Address or Address pattern is not contained in either list.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_HARDWARE_ADDRESS_TYPE_ALREADY_EXEMPT"></span><span id="error_dhcp_hardware_address_type_already_exempt"></span>**ERROR\_DHCP\_HARDWARE\_ADDRESS\_TYPE\_ALREADY\_EXEMPT**
</dt> <dd> <dl> <dt>

20101
</dt> <dt>



Windows 7 or later: This Hardware Type is already exempt.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_UNDEFINED_HARDWARE_ADDRESS_TYPE"></span><span id="error_dhcp_undefined_hardware_address_type"></span>**ERROR\_DHCP\_UNDEFINED\_HARDWARE\_ADDRESS\_TYPE**
</dt> <dd> <dl> <dt>

20102
</dt> <dt>



Windows 7 or later: You are trying to delete an undefined Hardware Type.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_OPTION_TYPE_MISMATCH"></span><span id="error_dhcp_option_type_mismatch"></span>**ERROR\_DHCP\_OPTION\_TYPE\_MISMATCH**
</dt> <dd> <dl> <dt>

20103
</dt> <dt>



Windows 7 or later: Conflict in types for the same option on Host and Added DHCP Servers.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_POLICY_BAD_PARENT_EXPR"></span><span id="error_dhcp_policy_bad_parent_expr"></span>**ERROR\_DHCP\_POLICY\_BAD\_PARENT\_EXPR**
</dt> <dd> <dl> <dt>

20104
</dt> <dt>



Windows 8 or later: The parent expression specified does not exist.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_POLICY_EXISTS"></span><span id="error_dhcp_policy_exists"></span>**ERROR\_DHCP\_POLICY\_EXISTS**
</dt> <dd> <dl> <dt>

20105
</dt> <dt>



Windows 8 or later: The DHCP server policy already exists.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_POLICY_RANGE_EXISTS"></span><span id="error_dhcp_policy_range_exists"></span>**ERROR\_DHCP\_POLICY\_RANGE\_EXISTS**
</dt> <dd> <dl> <dt>

20106
</dt> <dt>



Windows 8 or later: The DHCP server policy range specified already exists in the given scope.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_POLICY_RANGE_BAD"></span><span id="error_dhcp_policy_range_bad"></span>**ERROR\_DHCP\_POLICY\_RANGE\_BAD**
</dt> <dd> <dl> <dt>

20107
</dt> <dt>



Windows 8 or later: The DHCP server policy range specified is invalid or does not match the given subnet.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_RANGE_INVALID_IN_SERVER_POLICY"></span><span id="error_dhcp_range_invalid_in_server_policy"></span>**ERROR\_DHCP\_RANGE\_INVALID\_IN\_SERVER\_POLICY**
</dt> <dd> <dl> <dt>

20108
</dt> <dt>



Windows 8 or later: DHCP server policy ranges can only be added to scope level policies.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_INVALID_POLICY_EXPRESSION"></span><span id="error_dhcp_invalid_policy_expression"></span>**ERROR\_DHCP\_INVALID\_POLICY\_EXPRESSION**
</dt> <dd> <dl> <dt>

20109
</dt> <dt>



Windows 8 or later: The DHCP server policy contains an invalid expression.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_INVALID_PROCESSING_ORDER"></span><span id="error_dhcp_invalid_processing_order"></span>**ERROR\_DHCP\_INVALID\_PROCESSING\_ORDER**
</dt> <dd> <dl> <dt>

20110
</dt> <dt>



Windows 8 or later: The processing order specified for the DHCP server policy is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_POLICY_NOT_FOUND"></span><span id="error_dhcp_policy_not_found"></span>**ERROR\_DHCP\_POLICY\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

20111
</dt> <dt>



Windows 8 or later: The DHCP server policy was not found.


</dt> </dl> </dd> <dt>

<span id="ERROR_SCOPE_RANGE_POLICY_RANGE_CONFLICT"></span><span id="error_scope_range_policy_range_conflict"></span>**ERROR\_SCOPE\_RANGE\_POLICY\_RANGE\_CONFLICT**
</dt> <dd> <dl> <dt>

20112
</dt> <dt>



Windows 8 or later: There is an IP address range configured for a policy in this scope. This operation on the scope IP address range cannot be performed until the policy IP address range is suitably modified. Please change the IP address range of the policy before performing this operation.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_FO_SCOPE_ALREADY_IN_RELATIONSHIP"></span><span id="error_dhcp_fo_scope_already_in_relationship"></span>**ERROR\_DHCP\_FO\_SCOPE\_ALREADY\_IN\_RELATIONSHIP**
</dt> <dd> <dl> <dt>

20113
</dt> <dt>



Windows 8 or later: The DHCP scope is already in a failover relationship.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_FO_RELATIONSHIP_EXISTS"></span><span id="error_dhcp_fo_relationship_exists"></span>**ERROR\_DHCP\_FO\_RELATIONSHIP\_EXISTS**
</dt> <dd> <dl> <dt>

20114
</dt> <dt>



Windows 8 or later: The DHCP failover relationship already exists.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_FO_RELATIONSHIP_DOES_NOT_EXIST"></span><span id="error_dhcp_fo_relationship_does_not_exist"></span>**ERROR\_DHCP\_FO\_RELATIONSHIP\_DOES\_NOT\_EXIST**
</dt> <dd> <dl> <dt>

20115
</dt> <dt>



Windows 8 or later: The DHCP failover relationship does not exist.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_FO_SCOPE_NOT_IN_RELATIONSHIP"></span><span id="error_dhcp_fo_scope_not_in_relationship"></span>**ERROR\_DHCP\_FO\_SCOPE\_NOT\_IN\_RELATIONSHIP**
</dt> <dd> <dl> <dt>

20116
</dt> <dt>



Windows 8 or later: The DHCP scope is not part of a failover relationship.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_FO_RELATION_IS_SECONDARY"></span><span id="error_dhcp_fo_relation_is_secondary"></span>**ERROR\_DHCP\_FO\_RELATION\_IS\_SECONDARY**
</dt> <dd> <dl> <dt>

20117
</dt> <dt>



Windows 8 or later: The DHCP failover relationship is a secondary.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_FO_NOT_SUPPORTED"></span><span id="error_dhcp_fo_not_supported"></span>**ERROR\_DHCP\_FO\_NOT\_SUPPORTED**
</dt> <dd> <dl> <dt>

20118
</dt> <dt>



Windows 8 or later: The DHCP failover is not supported.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_FO_TIME_OUT_OF_SYNC"></span><span id="error_dhcp_fo_time_out_of_sync"></span>**ERROR\_DHCP\_FO\_TIME\_OUT\_OF\_SYNC**
</dt> <dd> <dl> <dt>

20119
</dt> <dt>



Windows 8 or later: The DHCP servers in the failover relationship have timed out of synchronization.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_FO_STATE_NOT_NORMAL"></span><span id="error_dhcp_fo_state_not_normal"></span>**ERROR\_DHCP\_FO\_STATE\_NOT\_NORMAL**
</dt> <dd> <dl> <dt>

20120
</dt> <dt>



Windows 8 or later: The DHCP failover relationship state is not NORMAL.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_NO_ADMIN_PERMISSION"></span><span id="error_dhcp_no_admin_permission"></span>**ERROR\_DHCP\_NO\_ADMIN\_PERMISSION**
</dt> <dd> <dl> <dt>

20121
</dt> <dt>



Windows 8 or later: The user does not have administrative permissions for the DHCP server.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_SERVER_NOT_REACHABLE"></span><span id="error_dhcp_server_not_reachable"></span>**ERROR\_DHCP\_SERVER\_NOT\_REACHABLE**
</dt> <dd> <dl> <dt>

20122
</dt> <dt>



Windows 8 or later: The specified DHCP server is not reachable. Please provide a DHCP server that is reachable.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_SERVER_NOT_RUNNING"></span><span id="error_dhcp_server_not_running"></span>**ERROR\_DHCP\_SERVER\_NOT\_RUNNING**
</dt> <dd> <dl> <dt>

20123
</dt> <dt>



Windows 8 or later: The DHCP Server Service is not running on the specified server. Please ensure that the DHCP Server service is running on the specified computer.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_SERVER_NAME_NOT_RESOLVED"></span><span id="error_dhcp_server_name_not_resolved"></span>**ERROR\_DHCP\_SERVER\_NAME\_NOT\_RESOLVED**
</dt> <dd> <dl> <dt>

20124
</dt> <dt>



Windows 8 or later: Unable to resolve DNS name.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_FO_RELATIONSHIP_NAME_TOO_LONG"></span><span id="error_dhcp_fo_relationship_name_too_long"></span>**ERROR\_DHCP\_FO\_RELATIONSHIP\_NAME\_TOO\_LONG**
</dt> <dd> <dl> <dt>

20125
</dt> <dt>



Windows 8 or later: The specified DHCP failover relationship name is too long. The name is limited to a maximum of 126 characters.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_REACHED_END_OF_SELECTION"></span><span id="error_dhcp_reached_end_of_selection"></span>**ERROR\_DHCP\_REACHED\_END\_OF\_SELECTION**
</dt> <dd> <dl> <dt>

20126
</dt> <dt>



Windows 8 or later: The specified DHCP Server has reached the end of the selected range while finding the free IP address.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_FO_ADDSCOPE_LEASES_NOT_SYNCED"></span><span id="error_dhcp_fo_addscope_leases_not_synced"></span>**ERROR\_DHCP\_FO\_ADDSCOPE\_LEASES\_NOT\_SYNCED**
</dt> <dd> <dl> <dt>

20127
</dt> <dt>



Windows 8 or later: The synchronization of leases in the scopes being added to the failover relationship failed.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_FO_MAX_RELATIONSHIPS"></span><span id="error_dhcp_fo_max_relationships"></span>**ERROR\_DHCP\_FO\_MAX\_RELATIONSHIPS**
</dt> <dd> <dl> <dt>

20128
</dt> <dt>



Windows 8 or later: The relationship cannot be created on the DHCP server as the maximum number of allowed relationship has been exceeded.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_FO_IPRANGE_TYPE_CONV_ILLEGAL"></span><span id="error_dhcp_fo_iprange_type_conv_illegal"></span>**ERROR\_DHCP\_FO\_IPRANGE\_TYPE\_CONV\_ILLEGAL**
</dt> <dd> <dl> <dt>

20129
</dt> <dt>



Windows 8 or later: A Scope configured for failover cannot be changed to type BOOTP or BOTH.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_FO_MAX_ADD_SCOPES"></span><span id="error_dhcp_fo_max_add_scopes"></span>**ERROR\_DHCP\_FO\_MAX\_ADD\_SCOPES**
</dt> <dd> <dl> <dt>

20130
</dt> <dt>



Windows 8 or later: The number of scopes being added to the failover relationship exceeds the max number of scopes which can be added to a failover relationship at one time.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_FO_BOOT_NOT_SUPPORTED"></span><span id="error_dhcp_fo_boot_not_supported"></span>**ERROR\_DHCP\_FO\_BOOT\_NOT\_SUPPORTED**
</dt> <dd> <dl> <dt>

20131
</dt> <dt>



Windows 8 or later: A scope supporting BOOTP clients cannot be added to a failover relationship.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_FO_RANGE_PART_OF_REL"></span><span id="error_dhcp_fo_range_part_of_rel"></span>**ERROR\_DHCP\_FO\_RANGE\_PART\_OF\_REL**
</dt> <dd> <dl> <dt>

20132
</dt> <dt>



Windows 8 or later: An IP address range of a scope which is part of a failover relationship cannot be deleted. The scope will need to be removed from the failover relationship before deleting the range.


</dt> </dl> </dd> </dl>

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Dhcpsapi.h</dt> </dl> |



 

 





