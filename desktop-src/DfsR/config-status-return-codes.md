---
title: CONFIG\_STATUS Return Codes
description: The following error codes can be returned by the configuration WMI classes for DFSR.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a097bc77-e9b7-4756-98b8-7a64f838e5f3
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-replication
- windows-management-instrumentation
ms.tgt_platform: multiple
topic_type:
- apiref
api_name:
- CONFIG_STATUS Return Codes
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CONFIG\_STATUS Return Codes

The following error codes can be returned by the configuration WMI classes for DFSR.

<dl> <dt>

<span id="CONFIG_STATUS_SUCCESS"></span><span id="config_status_success"></span>**CONFIG\_STATUS\_SUCCESS**
</dt> <dd>

0

Success.

</dd> <dt>

<span id="CONFIG_STATUS_REG_KEY_NOT_FOUND"></span><span id="config_status_reg_key_not_found"></span>**CONFIG\_STATUS\_REG\_KEY\_NOT\_FOUND**
</dt> <dd>

1

Registry key is not found.

</dd> <dt>

<span id="CONFIG_STATUS_REG_KEY_NOT_ACCESSIBLE"></span><span id="config_status_reg_key_not_accessible"></span>**CONFIG\_STATUS\_REG\_KEY\_NOT\_ACCESSIBLE**
</dt> <dd>

2

Registry key is not accessible.

</dd> <dt>

<span id="CONFIG_STATUS_REG_VALUE_NOT_FOUND"></span><span id="config_status_reg_value_not_found"></span>**CONFIG\_STATUS\_REG\_VALUE\_NOT\_FOUND**
</dt> <dd>

3

Registry value is not found.

</dd> <dt>

<span id="CONFIG_STATUS_REG_VALUE_INVALID"></span><span id="config_status_reg_value_invalid"></span>**CONFIG\_STATUS\_REG\_VALUE\_INVALID**
</dt> <dd>

4

Registry value is not valid.

</dd> <dt>

<span id="CONFIG_STATUS_REG_ERROR"></span><span id="config_status_reg_error"></span>**CONFIG\_STATUS\_REG\_ERROR**
</dt> <dd>

5

Generic registry error.

</dd> <dt>

<span id="CONFIG_STATUS_XML_NOT_INSTALLED"></span><span id="config_status_xml_not_installed"></span>**CONFIG\_STATUS\_XML\_NOT\_INSTALLED**
</dt> <dd>

6

MSXML.dll is not installed.

</dd> <dt>

<span id="CONFIG_STATUS_XML_EMPTY_DOM"></span><span id="config_status_xml_empty_dom"></span>**CONFIG\_STATUS\_XML\_EMPTY\_DOM**
</dt> <dd>

7

Missing XML DOM.

</dd> <dt>

<span id="CONFIG_STATUS_XML_INVALID_DOM"></span><span id="config_status_xml_invalid_dom"></span>**CONFIG\_STATUS\_XML\_INVALID\_DOM**
</dt> <dd>

8

XML DOM is not valid.

</dd> <dt>

<span id="CONFIG_STATUS_XML_FILE_NOT_FOUND"></span><span id="config_status_xml_file_not_found"></span>**CONFIG\_STATUS\_XML\_FILE\_NOT\_FOUND**
</dt> <dd>

9

XML file not found.

</dd> <dt>

<span id="CONFIG_STATUS_XML_FILE_NOT_ACCESSIBLE"></span><span id="config_status_xml_file_not_accessible"></span>**CONFIG\_STATUS\_XML\_FILE\_NOT\_ACCESSIBLE**
</dt> <dd>

10

XML file not accessible

</dd> <dt>

<span id="CONFIG_STATUS_XML_ERROR"></span><span id="config_status_xml_error"></span>**CONFIG\_STATUS\_XML\_ERROR**
</dt> <dd>

11

Generic XML error.

</dd> <dt>

<span id="CONFIG_STATUS_AD_CANNOT_CONNECT"></span><span id="config_status_ad_cannot_connect"></span>**CONFIG\_STATUS\_AD\_CANNOT\_CONNECT**
</dt> <dd>

12

Cannot connect to AD.

</dd> <dt>

<span id="CONFIG_STATUS_AD_ERROR"></span><span id="config_status_ad_error"></span>**CONFIG\_STATUS\_AD\_ERROR**
</dt> <dd>

14

Generic AD error.

</dd> <dt>

<span id="CONFIG_STATUS_PARAM_ERRORS"></span><span id="config_status_param_errors"></span>**CONFIG\_STATUS\_PARAM\_ERRORS**
</dt> <dd>

15

Bad XML\\AD parameter.

</dd> <dt>

<span id="CONFIG_STATUS_PARAM_WARNINGS"></span><span id="config_status_param_warnings"></span>**CONFIG\_STATUS\_PARAM\_WARNINGS**
</dt> <dd>

16

Bad XML\\AD parameter.

</dd> <dt>

<span id="CONFIG_STATUS_INVALID_FILE_PATH"></span><span id="config_status_invalid_file_path"></span>**CONFIG\_STATUS\_INVALID\_FILE\_PATH**
</dt> <dd>

17

File path is not valid.

</dd> <dt>

<span id="CONFIG_STATUS_VOLUME_NOT_FOUND"></span><span id="config_status_volume_not_found"></span>**CONFIG\_STATUS\_VOLUME\_NOT\_FOUND**
</dt> <dd>

18

Volume not found.

</dd> <dt>

<span id="CONFIG_STATUS_OUT_OF_MEMORY"></span><span id="config_status_out_of_memory"></span>**CONFIG\_STATUS\_OUT\_OF\_MEMORY**
</dt> <dd>

22

Out of memory.

</dd> <dt>

<span id="CONFIG_STATUS_SOURCE_MISMATCH"></span><span id="config_status_source_mismatch"></span>**CONFIG\_STATUS\_SOURCE\_MISMATCH**
</dt> <dd>

23

Configuration source mismatch.

</dd> <dt>

<span id="CONFIG_STATUS_ACCESS_DENIED"></span><span id="config_status_access_denied"></span>**CONFIG\_STATUS\_ACCESS\_DENIED**
</dt> <dd>

24

Access denied.

</dd> <dt>

<span id="CONFIG_STATUS_GHOSTING_NOT_SUPPORTED"></span><span id="config_status_ghosting_not_supported"></span>**CONFIG\_STATUS\_GHOSTING\_NOT\_SUPPORTED**
</dt> <dd>

25

Ghosting is not supported.

</dd> <dt>

<span id="CONFIG_STATUS_REPLICATIONGROUP_NOT_EMPTY"></span><span id="config_status_replicationgroup_not_empty"></span>**CONFIG\_STATUS\_REPLICATIONGROUP\_NOT\_EMPTY**
</dt> <dd>

26

The replication group is not empty.

</dd> <dt>

<span id="CONFIG_STATUS_REPLICATIONGROUP_ALREADY_EXISTS"></span><span id="config_status_replicationgroup_already_exists"></span>**CONFIG\_STATUS\_REPLICATIONGROUP\_ALREADY\_EXISTS**
</dt> <dd>

27

27

</dd> <dt>

<span id="CONFIG_STATUS_MEMBER_NOT_FOUND"></span><span id="config_status_member_not_found"></span>**CONFIG\_STATUS\_MEMBER\_NOT\_FOUND**
</dt> <dd>

28

The member is not found.

</dd> <dt>

<span id="CONFIG_STATUS_MEMBER_EXISTS"></span><span id="config_status_member_exists"></span>**CONFIG\_STATUS\_MEMBER\_EXISTS**
</dt> <dd>

29

The member exists.

</dd> <dt>

<span id="CONFIG_STATUS_MEMBER_EXIST"></span><span id="config_status_member_exist"></span>**CONFIG\_STATUS\_MEMBER\_EXIST**
</dt> <dd>

30

The member exists.

</dd> <dt>

<span id="CONFIG_STATUS_MEMBER_NOT_EXIST"></span><span id="config_status_member_not_exist"></span>**CONFIG\_STATUS\_MEMBER\_NOT\_EXIST**
</dt> <dd>

31

The member does exist.

</dd> <dt>

<span id="CONFIG_STATUS_AD_CONFIG_NOT_MODIFIABLE"></span><span id="config_status_ad_config_not_modifiable"></span>**CONFIG\_STATUS\_AD\_CONFIG\_NOT\_MODIFIABLE**
</dt> <dd>

32

The Active Directory (AD) configuration is not modifiable.

</dd> <dt>

<span id="CONFIG_STATUS_CONNECTION_NOT_FOUND"></span><span id="config_status_connection_not_found"></span>**CONFIG\_STATUS\_CONNECTION\_NOT\_FOUND**
</dt> <dd>

33

The connection was not found.

</dd> <dt>

<span id="CONFIG_STATUS_CONNECTION_EXIST"></span><span id="config_status_connection_exist"></span>**CONFIG\_STATUS\_CONNECTION\_EXIST**
</dt> <dd>

34

The connection exists.

</dd> <dt>

<span id="CONFIG_STATUS_REPLICATIONGROUPTYPE_NOT_SUPPORTED"></span><span id="config_status_replicationgrouptype_not_supported"></span>**CONFIG\_STATUS\_REPLICATIONGROUPTYPE\_NOT\_SUPPORTED**
</dt> <dd>

35

The replication group type is not supported.

</dd> <dt>

<span id="CONFIG_STATUS_PROPERTY_READONLY"></span><span id="config_status_property_readonly"></span>**CONFIG\_STATUS\_PROPERTY\_READONLY**
</dt> <dd>

36

The property is read-only.

</dd> <dt>

<span id="CONFIG_STATUS_REPLICATIONGROUP_INVALID_TOPLOLOGY"></span><span id="config_status_replicationgroup_invalid_toplology"></span>**CONFIG\_STATUS\_REPLICATIONGROUP\_INVALID\_TOPLOLOGY**
</dt> <dd>

37

The replication group has an invalid topology.

</dd> <dt>

<span id="CONFIG_STATUS_PARAM_ERROR_READONLY"></span><span id="config_status_param_error_readonly"></span>**CONFIG\_STATUS\_PARAM\_ERROR\_READONLY**
</dt> <dd>

38

The output parameter is read-only.

</dd> <dt>

<span id="CONFIG_STATUS_PARAM_ERROR_CREATEONLY"></span><span id="config_status_param_error_createonly"></span>**CONFIG\_STATUS\_PARAM\_ERROR\_CREATEONLY**
</dt> <dd>

39

The output parameter is create-only.

</dd> <dt>

<span id="CONFIG_STATUS_ERROR"></span><span id="config_status_error"></span>**CONFIG\_STATUS\_ERROR**
</dt> <dd>

40

Generic error.

</dd> </dl>

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |
| End of client support<br/>    | Windows 7<br/>           |



## See also

<dl> <dt>

[DFSR WMI Classes](dfsr-wmi-classes.md)
</dt> </dl>

 

 





