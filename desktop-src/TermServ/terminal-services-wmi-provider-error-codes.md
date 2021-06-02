---
title: Remote Desktop Services WMI provider error codes (Wbemcli.h)
description: Errors returned by the Remote Desktop Services WMI provider. For a list of other WMI errors, see WMI Error Constants.
ms.assetid: 1e68c41d-f321-4bc5-ba30-b69f5ba741eb
ms.tgt_platform: multiple
topic_type:
- apiref
api_name:
- WBEM_E_FAILED
- WBEM_E_NOT_FOUND
- WBEM_E_PROVIDER_FAILURE
- WBEM_E_TYPE_MISMATCH
- WBEM_E_OUT_OF_MEMORY
- WBEM_E_INVALID_PARAMETER
- WBEM_E_NOT_AVAILABLE
- WBEM_E_NOT_SUPPORTED
- WBEM_E_INVALID_NAMESPACE
- WBEM_E_INVALID_OBJECT
- WBEM_E_INITIALIZATION_FAILURE
- WBEM_E_INVALID_OPERATION
- WBEM_E_INVALID_QUERY
- WBEM_E_INVALID_QUERY_TYPE
- WBEM_E_ALREADY_EXISTS
- WBEM_E_INVALID_SYNTAX
- WBEM_E_READ_ONLY
- WBEM_E_PROVIDER_NOT_CAPABLE
- WBEM_E_ILLEGAL_NULL
- WBEM_E_VALUE_OUT_OF_RANGE
- WBEM_E_INVALID_METHOD
- WBEM_E_INVALID_METHOD_PARAMETERS
- WBEM_E_INVALID_OBJECT_PATH
api_location:
- Wbemcli.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Remote Desktop Services WMI provider error codes

The following list lists the WMI errors returned by the Remote Desktop Services WMI provider. For a list of other WMI errors, see [**WMI Error Constants**](/windows/desktop/WmiSdk/wmi-error-constants).

<dl> <dt>

<span id="WBEM_E_FAILED"></span><span id="wbem_e_failed"></span>**WBEM\_E\_FAILED**
</dt> <dd> <dl> <dt>

2147749889 (0x80041001)
</dt> <dt>



The method call failed.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_NOT_FOUND"></span><span id="wbem_e_not_found"></span>**WBEM\_E\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

2147749890 (0x80041002)
</dt> <dt>



The object could not be found.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_PROVIDER_FAILURE"></span><span id="wbem_e_provider_failure"></span>**WBEM\_E\_PROVIDER\_FAILURE**
</dt> <dd> <dl> <dt>

2147749892 (0x80041004)
</dt> <dt>



The provider has failed at some time other than during initialization.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_TYPE_MISMATCH"></span><span id="wbem_e_type_mismatch"></span>**WBEM\_E\_TYPE\_MISMATCH**
</dt> <dd> <dl> <dt>

2147749893 (0x80041005)
</dt> <dt>



A type mismatch has occurred.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_OUT_OF_MEMORY"></span><span id="wbem_e_out_of_memory"></span>**WBEM\_E\_OUT\_OF\_MEMORY**
</dt> <dd> <dl> <dt>

2147749894 (0x80041006)
</dt> <dt>



There was not enough memory for the operation.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_INVALID_PARAMETER"></span><span id="wbem_e_invalid_parameter"></span>**WBEM\_E\_INVALID\_PARAMETER**
</dt> <dd> <dl> <dt>

2147749896 (0x80041008)
</dt> <dt>



One of the parameters to the call is not correct.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_NOT_AVAILABLE"></span><span id="wbem_e_not_available"></span>**WBEM\_E\_NOT\_AVAILABLE**
</dt> <dd> <dl> <dt>

2147749897 (0x80041009)
</dt> <dt>



The resource, typically a remote server, is not currently available.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_NOT_SUPPORTED"></span><span id="wbem_e_not_supported"></span>**WBEM\_E\_NOT\_SUPPORTED**
</dt> <dd> <dl> <dt>

2147749900 (0x8004100C)
</dt> <dt>



The feature or operation is not supported.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_INVALID_NAMESPACE"></span><span id="wbem_e_invalid_namespace"></span>**WBEM\_E\_INVALID\_NAMESPACE**
</dt> <dd> <dl> <dt>

2147749902 (0x8004100E)
</dt> <dt>



The specified namespace could not be found.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_INVALID_OBJECT"></span><span id="wbem_e_invalid_object"></span>**WBEM\_E\_INVALID\_OBJECT**
</dt> <dd> <dl> <dt>

2147749903 (0x8004100F)
</dt> <dt>



The specified instance is not valid.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_INITIALIZATION_FAILURE"></span><span id="wbem_e_initialization_failure"></span>**WBEM\_E\_INITIALIZATION\_FAILURE**
</dt> <dd> <dl> <dt>

2147749908 (0x80041014)
</dt> <dt>



A module, such as a provider, failed to initialize for internal reasons.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_INVALID_OPERATION"></span><span id="wbem_e_invalid_operation"></span>**WBEM\_E\_INVALID\_OPERATION**
</dt> <dd> <dl> <dt>

2147749910 (0x80041016)
</dt> <dt>



The requested operation is not valid. This error usually applies to invalid attempts to delete classes or properties. This error is returned on an attempt to modify a server-override property through group policy control.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_INVALID_QUERY"></span><span id="wbem_e_invalid_query"></span>**WBEM\_E\_INVALID\_QUERY**
</dt> <dd> <dl> <dt>

2147749911 (0x80041017)
</dt> <dt>



The query was not syntactically valid.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_INVALID_QUERY_TYPE"></span><span id="wbem_e_invalid_query_type"></span>**WBEM\_E\_INVALID\_QUERY\_TYPE**
</dt> <dd> <dl> <dt>

2147749912 (0x80041018)
</dt> <dt>



The requested query language is not supported.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_ALREADY_EXISTS"></span><span id="wbem_e_already_exists"></span>**WBEM\_E\_ALREADY\_EXISTS**
</dt> <dd> <dl> <dt>

2147749913 (0x80041019)
</dt> <dt>



In a put operation, the **wbemChangeFlagCreateOnly** flag was specified, but the instance already exists.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_INVALID_SYNTAX"></span><span id="wbem_e_invalid_syntax"></span>**WBEM\_E\_INVALID\_SYNTAX**
</dt> <dd> <dl> <dt>

2147749921 (0x80041021)
</dt> <dt>



Query is not syntactically valid.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_READ_ONLY"></span><span id="wbem_e_read_only"></span>**WBEM\_E\_READ\_ONLY**
</dt> <dd> <dl> <dt>

2147749923 (0x80041023)
</dt> <dt>



The property that you are attempting to modify is read-only.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_PROVIDER_NOT_CAPABLE"></span><span id="wbem_e_provider_not_capable"></span>**WBEM\_E\_PROVIDER\_NOT\_CAPABLE**
</dt> <dd> <dl> <dt>

2147749924 (0x80041024)
</dt> <dt>



The provider cannot perform the requested operation. The operation could include a query that is too complex, retrieving an instance, creating a class, updating a class, deleting a class, or enumerating a class.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_ILLEGAL_NULL"></span><span id="wbem_e_illegal_null"></span>**WBEM\_E\_ILLEGAL\_NULL**
</dt> <dd> <dl> <dt>

2147749928 (0x80041028)
</dt> <dt>



A value of **Nothing**/**NULL** was specified for a property that cannot be **Nothing**/**NULL**, such as one that is marked by a [**Key**](/windows/desktop/WmiSdk/key-qualifier), [**Indexed**](/windows/desktop/WmiSdk/optional-qualifiers), or [**Not\_Null**](/windows/desktop/WmiSdk/optional-qualifiers) qualifier.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_VALUE_OUT_OF_RANGE"></span><span id="wbem_e_value_out_of_range"></span>**WBEM\_E\_VALUE\_OUT\_OF\_RANGE**
</dt> <dd> <dl> <dt>

2147749931 (0x8004102B)
</dt> <dt>



The request was made with an out-of-range value, or is incompatible with the type.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_INVALID_METHOD"></span><span id="wbem_e_invalid_method"></span>**WBEM\_E\_INVALID\_METHOD**
</dt> <dd> <dl> <dt>

2147749934 (0x8004102E)
</dt> <dt>



The requested method is not available.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_INVALID_METHOD_PARAMETERS"></span><span id="wbem_e_invalid_method_parameters"></span>**WBEM\_E\_INVALID\_METHOD\_PARAMETERS**
</dt> <dd> <dl> <dt>

2147749935 (0x8004102F)
</dt> <dt>



The parameters provided for the method are not valid.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_INVALID_OBJECT_PATH"></span><span id="wbem_e_invalid_object_path"></span>**WBEM\_E\_INVALID\_OBJECT\_PATH**
</dt> <dd> <dl> <dt>

2147749946 (0x8004103A)
</dt> <dt>



The specified object path was not valid.


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                       |
| Header<br/>                   | <dl> <dt>Wbemcli.h</dt> </dl> |



 

