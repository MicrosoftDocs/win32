---
description: If an error occurs, WMI returns an error code as an HRESULT value. These codes may be returned by scripts, C++ applications, or Wmic.
ms.assetid: b560f37c-da22-4745-8d1f-b27afdf572ec
ms.tgt_platform: multiple
title: WMI Error Constants (WbemCli.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WMI Error Constants

If an error occurs, WMI returns an error code as an **HRESULT** value. These codes may be returned by scripts, C++ applications, or [**Wmic**](wmic.md).

> [!Note]
>
> The following documentation is targeted for developers and IT administrators. If you are an end-user that has experienced an error message concerning WMI, you should go to [Microsoft Support](https://support.microsoft.com/) and search for the error code you see on the error message. For more information about troubleshooting problems with WMI scripts and the WMI service, see [WMI Isn't Working!](/previous-versions/tn-archive/ff406382(v=msdn.10)).
>
> If WMI returns error messages, be aware that they may not indicate problems in the WMI service or in WMI providers. Failures can originate in other parts of the operating system and emerge as errors through WMI. Under any circumstances, do not delete the WMI repository as a first action because deleting the repository can cause damage to the system or to installed applications.
>
> To obtain more information about the source of the problem, you can download and run the [WMI Diagnosis Utility](https://www.microsoft.com/downloads/en/details.aspx?familyid=d7ba3cd6-18d1-4d05-b11e-4c64192ae97d&displaylang=en) diagnostic command line tool. This tool produces a report that can usually isolate the source of the problem and provide instructions on how to fix it. The report also aids Microsoft support services in assisting you. You can download the WMI Diagnosis Utility [here](https://www.microsoft.com/downloads/details.aspx?FamilyID=d7ba3cd6-18d1-4d05-b11e-4c64192ae97d).

 

Some methods in WMI classes can return system and network error codes (64 for example). You can check the definition of these types of error codes by using the **net helpmsg** command in the command prompt window. For example, the command **net helpmsg 64** returns the message: The specified network name is no longer available.

The following list lists some common ranges of errors.

<dl> <dt>

<span id="0x80041068_-_0x80041099"></span><span id="0X80041068_-_0X80041099"></span>0x80041068 - 0x80041099
</dt> <dd>

Errors that originate in WMI itself.

A specific WMI operation failed because of

-   An error in the request, for example, a WQL query fails or the account does not have the correct permissions.
-   A WMI infrastructure problem, such as incorrect CIM or DCOM registration.

</dd> <dt>

<span id="0x8007xxxx"></span><span id="0X8007XXXX"></span>0x8007xxxx
</dt> <dd>

Errors originating in the core operating system. WMI may return this type of error because of an external failure, for example, DCOM security failure.

</dd> <dt>

<span id="0x80040xxx"></span><span id="0X80040XXX"></span>0x80040xxx
</dt> <dd>

Errors originating in DCOM. For example, the DCOM configuration for operations to a remote computer may be incorrect.

</dd> <dt>

<span id="0x8005xxxx"></span><span id="0X8005XXXX"></span>0x8005xxxx
</dt> <dd>

Error originating from ADSI (Active Directory Service Interfaces) or LDAP (Lightweight Directory Access Protocol), for example, an Active Directory access failure when using the WMI Active Directory providers.

</dd> </dl>

Some methods in WMI classes can return system and network error codes (64 for example). You can check the definition of these types of error codes by using the **net helpmsg** command in the command prompt window. For example, the command **net helpmsg 64** returns the message: The specified network name is no longer available. In C++, you can call [**FormatMessage**](/windows/desktop/api/winbase/nf-winbase-formatmessage) and specify **C:\\Windows\\System32\\wbem\\wmiutils.dll** as the message module.

<dl> <dt>

<span id="WBEM_E_FAILED"></span><span id="wbem_e_failed"></span>**WBEM\_E\_FAILED**
</dt> <dd> <dl> <dt>

2147749889 (0x80041001)
</dt> <dt>



Call failed.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_NOT_FOUND"></span><span id="wbem_e_not_found"></span>**WBEM\_E\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

2147749890 (0x80041002)
</dt> <dt>



Object cannot be found.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_ACCESS_DENIED"></span><span id="wbem_e_access_denied"></span>**WBEM\_E\_ACCESS\_DENIED**
</dt> <dd> <dl> <dt>

2147749891 (0x80041003)
</dt> <dt>



Current user does not have permission to perform the action.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_PROVIDER_FAILURE"></span><span id="wbem_e_provider_failure"></span>**WBEM\_E\_PROVIDER\_FAILURE**
</dt> <dd> <dl> <dt>

2147749892 (0x80041004)
</dt> <dt>



Provider has failed at some time other than during initialization.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_TYPE_MISMATCH"></span><span id="wbem_e_type_mismatch"></span>**WBEM\_E\_TYPE\_MISMATCH**
</dt> <dd> <dl> <dt>

2147749893 (0x80041005)
</dt> <dt>



Type mismatch occurred.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_OUT_OF_MEMORY"></span><span id="wbem_e_out_of_memory"></span>**WBEM\_E\_OUT\_OF\_MEMORY**
</dt> <dd> <dl> <dt>

2147749894 (0x80041006)
</dt> <dt>



Not enough memory for the operation.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_INVALID_CONTEXT"></span><span id="wbem_e_invalid_context"></span>**WBEM\_E\_INVALID\_CONTEXT**
</dt> <dd> <dl> <dt>

2147749895 (0x80041007)
</dt> <dt>



The [**IWbemContext**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemcontext) object is not valid.


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



Resource, typically a remote server, is not currently available.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_CRITICAL_ERROR"></span><span id="wbem_e_critical_error"></span>**WBEM\_E\_CRITICAL\_ERROR**
</dt> <dd> <dl> <dt>

2147749898 (0x8004100A)
</dt> <dt>



Internal, critical, and unexpected error occurred. Report the error to Microsoft Technical Support.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_INVALID_STREAM"></span><span id="wbem_e_invalid_stream"></span>**WBEM\_E\_INVALID\_STREAM**
</dt> <dd> <dl> <dt>

2147749899 (0x8004100B)
</dt> <dt>



One or more network packets were corrupted during a remote session.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_NOT_SUPPORTED"></span><span id="wbem_e_not_supported"></span>**WBEM\_E\_NOT\_SUPPORTED**
</dt> <dd> <dl> <dt>

2147749900 (0x8004100C)
</dt> <dt>



Feature or operation is not supported.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_INVALID_SUPERCLASS"></span><span id="wbem_e_invalid_superclass"></span>**WBEM\_E\_INVALID\_SUPERCLASS**
</dt> <dd> <dl> <dt>

2147749901 (0x8004100D)
</dt> <dt>



Parent class specified is not valid.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_INVALID_NAMESPACE"></span><span id="wbem_e_invalid_namespace"></span>**WBEM\_E\_INVALID\_NAMESPACE**
</dt> <dd> <dl> <dt>

2147749902 (0x8004100E)
</dt> <dt>



Namespace specified cannot be found.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_INVALID_OBJECT"></span><span id="wbem_e_invalid_object"></span>**WBEM\_E\_INVALID\_OBJECT**
</dt> <dd> <dl> <dt>

2147749903 (0x8004100F)
</dt> <dt>



Specified instance is not valid.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_INVALID_CLASS"></span><span id="wbem_e_invalid_class"></span>**WBEM\_E\_INVALID\_CLASS**
</dt> <dd> <dl> <dt>

2147749904 (0x80041010)
</dt> <dt>



Specified class is not valid.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_PROVIDER_NOT_FOUND"></span><span id="wbem_e_provider_not_found"></span>**WBEM\_E\_PROVIDER\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

2147749905 (0x80041011)
</dt> <dt>



Provider referenced in the schema does not have a corresponding registration.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_INVALID_PROVIDER_REGISTRATION"></span><span id="wbem_e_invalid_provider_registration"></span>**WBEM\_E\_INVALID\_PROVIDER\_REGISTRATION**
</dt> <dd> <dl> <dt>

2147749906
</dt> <dt>



Provider referenced in the schema has an incorrect or incomplete registration.

This error may be caused by many conditions, including the following:

-   A missing [\#pragma namespace](pragma-namespace.md) command in the Managed Object Format (MOF) file used to register the provider. The provider may be registered in the wrong WMI namespace.
-   Failure to retrieve the COM registration.
-   Hosting model is not valid. For more information, see [Provider Hosting and Security](provider-hosting-and-security.md).
-   An class specified in the registration is not valid.
-   Failure to create an instance of or inherit from the [**\_\_Win32Provider**](--win32provider.md) class to create the provider registration in the MOF file.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_PROVIDER_LOAD_FAILURE"></span><span id="wbem_e_provider_load_failure"></span>**WBEM\_E\_PROVIDER\_LOAD\_FAILURE**
</dt> <dd> <dl> <dt>

2147749907 (0x80041013)
</dt> <dt>



COM cannot locate a provider referenced in the schema.

This error may be caused by many conditions, including the following:

-   Provider is using a WMI DLL that does not match the .lib file used when the provider was built.
-   Provider's DLL, or any of the DLLs on which it depends, is corrupt.
-   Provider failed to export [**DllRegisterServer**](/windows/win32/api/olectl/nf-olectl-dllregisterserver).
-   In-process provider was not registered using the **regsvr32** command.
-   Out-of-process provider was not registered using the **/regserver** switch. For example, **myprog.exe /regserver**.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_INITIALIZATION_FAILURE"></span><span id="wbem_e_initialization_failure"></span>**WBEM\_E\_INITIALIZATION\_FAILURE**
</dt> <dd> <dl> <dt>

2147749908 (0x80041014)
</dt> <dt>



Component, such as a provider, failed to initialize for internal reasons.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_TRANSPORT_FAILURE"></span><span id="wbem_e_transport_failure"></span>**WBEM\_E\_TRANSPORT\_FAILURE**
</dt> <dd> <dl> <dt>

2147749909 (0x80041015)
</dt> <dt>



Networking error that prevents normal operation has occurred.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_INVALID_OPERATION"></span><span id="wbem_e_invalid_operation"></span>**WBEM\_E\_INVALID\_OPERATION**
</dt> <dd> <dl> <dt>

2147749910 (0x80041016)
</dt> <dt>



Requested operation is not valid. This error usually applies to invalid attempts to delete classes or properties.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_INVALID_QUERY"></span><span id="wbem_e_invalid_query"></span>**WBEM\_E\_INVALID\_QUERY**
</dt> <dd> <dl> <dt>

2147749911 (0x80041017)
</dt> <dt>



Query was not syntactically valid.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_INVALID_QUERY_TYPE"></span><span id="wbem_e_invalid_query_type"></span>**WBEM\_E\_INVALID\_QUERY\_TYPE**
</dt> <dd> <dl> <dt>

2147749912 (0x80041018)
</dt> <dt>



Requested query language is not supported.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_ALREADY_EXISTS"></span><span id="wbem_e_already_exists"></span>**WBEM\_E\_ALREADY\_EXISTS**
</dt> <dd> <dl> <dt>

2147749913 (0x80041019)
</dt> <dt>



In a put operation, the **wbemChangeFlagCreateOnly** flag was specified, but the instance already exists.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_OVERRIDE_NOT_ALLOWED"></span><span id="wbem_e_override_not_allowed"></span>**WBEM\_E\_OVERRIDE\_NOT\_ALLOWED**
</dt> <dd> <dl> <dt>

2147749914 (0x8004101A)
</dt> <dt>



Not possible to perform the add operation on this qualifier because the owning object does not permit overrides.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_PROPAGATED_QUALIFIER"></span><span id="wbem_e_propagated_qualifier"></span>**WBEM\_E\_PROPAGATED\_QUALIFIER**
</dt> <dd> <dl> <dt>

2147749915 (0x8004101B)
</dt> <dt>



User attempted to delete a qualifier that was not owned. The qualifier was inherited from a parent class.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_PROPAGATED_PROPERTY"></span><span id="wbem_e_propagated_property"></span>**WBEM\_E\_PROPAGATED\_PROPERTY**
</dt> <dd> <dl> <dt>

2147749916 (0x8004101C)
</dt> <dt>



User attempted to delete a property that was not owned. The property was inherited from a parent class.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_UNEXPECTED"></span><span id="wbem_e_unexpected"></span>**WBEM\_E\_UNEXPECTED**
</dt> <dd> <dl> <dt>

2147749917 (0x8004101D)
</dt> <dt>



Client made an unexpected and illegal sequence of calls, such as calling [**EndEnumeration**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemclassobject-endenumeration) before calling [**BeginEnumeration**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemclassobject-beginenumeration).


</dt> </dl> </dd> <dt>

<span id="WBEM_E_ILLEGAL_OPERATION"></span><span id="wbem_e_illegal_operation"></span>**WBEM\_E\_ILLEGAL\_OPERATION**
</dt> <dd> <dl> <dt>

2147749918 (0x8004101E)
</dt> <dt>



User requested an illegal operation, such as spawning a class from an instance.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_CANNOT_BE_KEY"></span><span id="wbem_e_cannot_be_key"></span>**WBEM\_E\_CANNOT\_BE\_KEY**
</dt> <dd> <dl> <dt>

2147749919 (0x8004101F)
</dt> <dt>



Illegal attempt to specify a key qualifier on a property that cannot be a key. The keys are specified in the class definition for an object and cannot be altered on a per-instance basis.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_INCOMPLETE_CLASS"></span><span id="wbem_e_incomplete_class"></span>**WBEM\_E\_INCOMPLETE\_CLASS**
</dt> <dd> <dl> <dt>

2147749920 (0x80041020)
</dt> <dt>



Current object is not a valid class definition. Either it is incomplete or it has not been registered with WMI using [**SWbemObject.Put\_**](swbemobject-put-.md).


</dt> </dl> </dd> <dt>

<span id="WBEM_E_INVALID_SYNTAX"></span><span id="wbem_e_invalid_syntax"></span>**WBEM\_E\_INVALID\_SYNTAX**
</dt> <dd> <dl> <dt>

2147749921 (0x80041021)
</dt> <dt>



Query is syntactically not valid.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_NONDECORATED_OBJECT"></span><span id="wbem_e_nondecorated_object"></span>**WBEM\_E\_NONDECORATED\_OBJECT**
</dt> <dd> <dl> <dt>

2147749922 (0x80041022)
</dt> <dt>



Reserved for future use.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_READ_ONLY"></span><span id="wbem_e_read_only"></span>**WBEM\_E\_READ\_ONLY**
</dt> <dd> <dl> <dt>

2147749923 (0x80041023)
</dt> <dt>



An attempt was made to modify a read-only property.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_PROVIDER_NOT_CAPABLE"></span><span id="wbem_e_provider_not_capable"></span>**WBEM\_E\_PROVIDER\_NOT\_CAPABLE**
</dt> <dd> <dl> <dt>

2147749924 (0x80041024)
</dt> <dt>



Provider cannot perform the requested operation. This can include a query that is too complex, retrieving an instance, creating or updating a class, deleting a class, or enumerating a class.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_CLASS_HAS_CHILDREN"></span><span id="wbem_e_class_has_children"></span>**WBEM\_E\_CLASS\_HAS\_CHILDREN**
</dt> <dd> <dl> <dt>

2147749925 (0x80041025)
</dt> <dt>



Attempt was made to make a change that invalidates a subclass.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_CLASS_HAS_INSTANCES"></span><span id="wbem_e_class_has_instances"></span>**WBEM\_E\_CLASS\_HAS\_INSTANCES**
</dt> <dd> <dl> <dt>

2147749926 (0x80041026)
</dt> <dt>



Attempt was made to delete or modify a class that has instances.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_QUERY_NOT_IMPLEMENTED"></span><span id="wbem_e_query_not_implemented"></span>**WBEM\_E\_QUERY\_NOT\_IMPLEMENTED**
</dt> <dd> <dl> <dt>

2147749927 (0x80041027)
</dt> <dt>



Reserved for future use.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_ILLEGAL_NULL"></span><span id="wbem_e_illegal_null"></span>**WBEM\_E\_ILLEGAL\_NULL**
</dt> <dd> <dl> <dt>

2147749928 (0x80041028)
</dt> <dt>



Value of Nothing/**NULL** was specified for a property that must have a value, such as one that is marked by a [**Key**](key-qualifier.md), [**Indexed**](optional-qualifiers.md), or **Not\_Null** qualifier.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_INVALID_QUALIFIER_TYPE"></span><span id="wbem_e_invalid_qualifier_type"></span>**WBEM\_E\_INVALID\_QUALIFIER\_TYPE**
</dt> <dd> <dl> <dt>

2147749929 (0x80041029)
</dt> <dt>



Variant value for a qualifier was provided that is not a legal qualifier type.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_INVALID_PROPERTY_TYPE"></span><span id="wbem_e_invalid_property_type"></span>**WBEM\_E\_INVALID\_PROPERTY\_TYPE**
</dt> <dd> <dl> <dt>

2147749930 (0x8004102A)
</dt> <dt>



CIM type specified for a property is not valid.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_VALUE_OUT_OF_RANGE"></span><span id="wbem_e_value_out_of_range"></span>**WBEM\_E\_VALUE\_OUT\_OF\_RANGE**
</dt> <dd> <dl> <dt>

2147749931 (0x8004102B)
</dt> <dt>



Request was made with an out-of-range value or it is incompatible with the type.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_CANNOT_BE_SINGLETON"></span><span id="wbem_e_cannot_be_singleton"></span>**WBEM\_E\_CANNOT\_BE\_SINGLETON**
</dt> <dd> <dl> <dt>

2147749932 (0x8004102C)
</dt> <dt>



Illegal attempt was made to make a class singleton, such as when the class is derived from a non-singleton class.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_INVALID_CIM_TYPE"></span><span id="wbem_e_invalid_cim_type"></span>**WBEM\_E\_INVALID\_CIM\_TYPE**
</dt> <dd> <dl> <dt>

2147749933 (0x8004102D)
</dt> <dt>



CIM type specified is not valid.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_INVALID_METHOD"></span><span id="wbem_e_invalid_method"></span>**WBEM\_E\_INVALID\_METHOD**
</dt> <dd> <dl> <dt>

2147749934 (0x8004102E)
</dt> <dt>



Requested method is not available.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_INVALID_METHOD_PARAMETERS"></span><span id="wbem_e_invalid_method_parameters"></span>**WBEM\_E\_INVALID\_METHOD\_PARAMETERS**
</dt> <dd> <dl> <dt>

2147749935 (0x8004102F)
</dt> <dt>



Parameters provided for the method are not valid.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_SYSTEM_PROPERTY"></span><span id="wbem_e_system_property"></span>**WBEM\_E\_SYSTEM\_PROPERTY**
</dt> <dd> <dl> <dt>

2147749936 (0x80041030)
</dt> <dt>



There was an attempt to get qualifiers on a system property.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_INVALID_PROPERTY"></span><span id="wbem_e_invalid_property"></span>**WBEM\_E\_INVALID\_PROPERTY**
</dt> <dd> <dl> <dt>

2147749937 (0x80041031)
</dt> <dt>



Property type is not recognized.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_CALL_CANCELLED"></span><span id="wbem_e_call_cancelled"></span>**WBEM\_E\_CALL\_CANCELLED**
</dt> <dd> <dl> <dt>

2147749938 (0x80041032)
</dt> <dt>



Asynchronous process has been canceled internally or by the user. Note that due to the timing and nature of the asynchronous operation, the operation may not have been truly canceled.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_SHUTTING_DOWN"></span><span id="wbem_e_shutting_down"></span>**WBEM\_E\_SHUTTING\_DOWN**
</dt> <dd> <dl> <dt>

2147749939 (0x80041033)
</dt> <dt>



User has requested an operation while WMI is in the process of shutting down.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_PROPAGATED_METHOD"></span><span id="wbem_e_propagated_method"></span>**WBEM\_E\_PROPAGATED\_METHOD**
</dt> <dd> <dl> <dt>

2147749940 (0x80041034)
</dt> <dt>



Attempt was made to reuse an existing method name from a parent class and the signatures do not match.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_UNSUPPORTED_PARAMETER"></span><span id="wbem_e_unsupported_parameter"></span>**WBEM\_E\_UNSUPPORTED\_PARAMETER**
</dt> <dd> <dl> <dt>

2147749941 (0x80041035)
</dt> <dt>



One or more parameter values, such as a query text, is too complex or unsupported. WMI is therefore requested to retry the operation with simpler parameters.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_MISSING_PARAMETER_ID"></span><span id="wbem_e_missing_parameter_id"></span>**WBEM\_E\_MISSING\_PARAMETER\_ID**
</dt> <dd> <dl> <dt>

2147749942 (0x80041036)
</dt> <dt>



Parameter was missing from the method call.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_INVALID_PARAMETER_ID"></span><span id="wbem_e_invalid_parameter_id"></span>**WBEM\_E\_INVALID\_PARAMETER\_ID**
</dt> <dd> <dl> <dt>

2147749943 (0x80041037)
</dt> <dt>



Method parameter has an [**ID**](standard-wmi-qualifiers.md) qualifier that is not valid.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_NONCONSECUTIVE_PARAMETER_IDS"></span><span id="wbem_e_nonconsecutive_parameter_ids"></span>**WBEM\_E\_NONCONSECUTIVE\_PARAMETER\_IDS**
</dt> <dd> <dl> <dt>

2147749944 (0x80041038)
</dt> <dt>



One or more of the method parameters have [**ID**](standard-wmi-qualifiers.md) qualifiers that are out of sequence.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_PARAMETER_ID_ON_RETVAL"></span><span id="wbem_e_parameter_id_on_retval"></span>**WBEM\_E\_PARAMETER\_ID\_ON\_RETVAL**
</dt> <dd> <dl> <dt>

2147749945 (0x80041039)
</dt> <dt>



Return value for a method has an [**ID**](standard-wmi-qualifiers.md) qualifier.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_INVALID_OBJECT_PATH"></span><span id="wbem_e_invalid_object_path"></span>**WBEM\_E\_INVALID\_OBJECT\_PATH**
</dt> <dd> <dl> <dt>

2147749946 (0x8004103A)
</dt> <dt>



Specified object path was not valid.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_OUT_OF_DISK_SPACE"></span><span id="wbem_e_out_of_disk_space"></span>**WBEM\_E\_OUT\_OF\_DISK\_SPACE**
</dt> <dd> <dl> <dt>

2147749947 (0x8004103B)
</dt> <dt>



Disk is out of space or the 4 GB limit on WMI repository (CIM repository) size is reached.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_BUFFER_TOO_SMALL"></span><span id="wbem_e_buffer_too_small"></span>**WBEM\_E\_BUFFER\_TOO\_SMALL**
</dt> <dd> <dl> <dt>

2147749948 (0x8004103C)
</dt> <dt>



Supplied buffer was too small to hold all of the objects in the enumerator or to read a string property.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_UNSUPPORTED_PUT_EXTENSION"></span><span id="wbem_e_unsupported_put_extension"></span>**WBEM\_E\_UNSUPPORTED\_PUT\_EXTENSION**
</dt> <dd> <dl> <dt>

2147749949 (0x8004103D)
</dt> <dt>



Provider does not support the requested put operation.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_UNKNOWN_OBJECT_TYPE"></span><span id="wbem_e_unknown_object_type"></span>**WBEM\_E\_UNKNOWN\_OBJECT\_TYPE**
</dt> <dd> <dl> <dt>

2147749950 (0x8004103E)
</dt> <dt>



Object with an incorrect type or version was encountered during marshaling.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_UNKNOWN_PACKET_TYPE"></span><span id="wbem_e_unknown_packet_type"></span>**WBEM\_E\_UNKNOWN\_PACKET\_TYPE**
</dt> <dd> <dl> <dt>

2147749951 (0x8004103F)
</dt> <dt>



Packet with an incorrect type or version was encountered during marshaling.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_MARSHAL_VERSION_MISMATCH"></span><span id="wbem_e_marshal_version_mismatch"></span>**WBEM\_E\_MARSHAL\_VERSION\_MISMATCH**
</dt> <dd> <dl> <dt>

2147749952 (0x80041040)
</dt> <dt>



Packet has an unsupported version.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_MARSHAL_INVALID_SIGNATURE"></span><span id="wbem_e_marshal_invalid_signature"></span>**WBEM\_E\_MARSHAL\_INVALID\_SIGNATURE**
</dt> <dd> <dl> <dt>

2147749953 (0x80041041)
</dt> <dt>



Packet appears to be corrupt.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_INVALID_QUALIFIER"></span><span id="wbem_e_invalid_qualifier"></span>**WBEM\_E\_INVALID\_QUALIFIER**
</dt> <dd> <dl> <dt>

2147749954 (0x80041042)
</dt> <dt>



Attempt was made to mismatch qualifiers, such as putting \[key\] on an object instead of a property.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_INVALID_DUPLICATE_PARAMETER"></span><span id="wbem_e_invalid_duplicate_parameter"></span>**WBEM\_E\_INVALID\_DUPLICATE\_PARAMETER**
</dt> <dd> <dl> <dt>

2147749955 (0x80041043)
</dt> <dt>



Duplicate parameter was declared in a CIM method.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_TOO_MUCH_DATA"></span><span id="wbem_e_too_much_data"></span>**WBEM\_E\_TOO\_MUCH\_DATA**
</dt> <dd> <dl> <dt>

2147749956 (0x80041044)
</dt> <dt>



Reserved for future use.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_SERVER_TOO_BUSY"></span><span id="wbem_e_server_too_busy"></span>**WBEM\_E\_SERVER\_TOO\_BUSY**
</dt> <dd> <dl> <dt>

2147749957 (0x80041045)
</dt> <dt>



Call to [**IWbemObjectSink::Indicate**](/windows/desktop/api/Wbemcli/nf-wbemcli-iwbemobjectsink-indicate) has failed. The provider can refire the event.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_INVALID_FLAVOR"></span><span id="wbem_e_invalid_flavor"></span>**WBEM\_E\_INVALID\_FLAVOR**
</dt> <dd> <dl> <dt>

2147749958 (0x80041046)
</dt> <dt>



Specified qualifier flavor was not valid.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_CIRCULAR_REFERENCE"></span><span id="wbem_e_circular_reference"></span>**WBEM\_E\_CIRCULAR\_REFERENCE**
</dt> <dd> <dl> <dt>

2147749959 (0x80041047)
</dt> <dt>



Attempt was made to create a reference that is circular (for example, deriving a class from itself).


</dt> </dl> </dd> <dt>

<span id="WBEM_E_UNSUPPORTED_CLASS_UPDATE"></span><span id="wbem_e_unsupported_class_update"></span>**WBEM\_E\_UNSUPPORTED\_CLASS\_UPDATE**
</dt> <dd> <dl> <dt>

2147749960 (0x80041048)
</dt> <dt>



Specified class is not supported.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_CANNOT_CHANGE_KEY_INHERITANCE"></span><span id="wbem_e_cannot_change_key_inheritance"></span>**WBEM\_E\_CANNOT\_CHANGE\_KEY\_INHERITANCE**
</dt> <dd> <dl> <dt>

2147749961 (0x80041049)
</dt> <dt>



Attempt was made to change a key when instances or subclasses are already using the key.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_CANNOT_CHANGE_INDEX_INHERITANCE"></span><span id="wbem_e_cannot_change_index_inheritance"></span>**WBEM\_E\_CANNOT\_CHANGE\_INDEX\_INHERITANCE**
</dt> <dd> <dl> <dt>

2147749968 (0x80041050)
</dt> <dt>



An attempt was made to change an index when instances or subclasses are already using the index.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_TOO_MANY_PROPERTIES"></span><span id="wbem_e_too_many_properties"></span>**WBEM\_E\_TOO\_MANY\_PROPERTIES**
</dt> <dd> <dl> <dt>

2147749969 (0x80041051)
</dt> <dt>



Attempt was made to create more properties than the current version of the class supports.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_UPDATE_TYPE_MISMATCH"></span><span id="wbem_e_update_type_mismatch"></span>**WBEM\_E\_UPDATE\_TYPE\_MISMATCH**
</dt> <dd> <dl> <dt>

2147749970 (0x80041052)
</dt> <dt>



Property was redefined with a conflicting type in a derived class.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_UPDATE_OVERRIDE_NOT_ALLOWED"></span><span id="wbem_e_update_override_not_allowed"></span>**WBEM\_E\_UPDATE\_OVERRIDE\_NOT\_ALLOWED**
</dt> <dd> <dl> <dt>

2147749971 (0x80041053)
</dt> <dt>



Attempt was made in a derived class to override a qualifier that cannot be overridden.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_UPDATE_PROPAGATED_METHOD"></span><span id="wbem_e_update_propagated_method"></span>**WBEM\_E\_UPDATE\_PROPAGATED\_METHOD**
</dt> <dd> <dl> <dt>

2147749972 (0x80041054)
</dt> <dt>



Method was re-declared with a conflicting signature in a derived class.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_METHOD_NOT_IMPLEMENTED"></span><span id="wbem_e_method_not_implemented"></span>**WBEM\_E\_METHOD\_NOT\_IMPLEMENTED**
</dt> <dd> <dl> <dt>

2147749973 (0x80041055)
</dt> <dt>



Attempt was made to execute a method not marked with \[implemented\] in any relevant class.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_METHOD_DISABLED"></span><span id="wbem_e_method_disabled"></span>**WBEM\_E\_METHOD\_DISABLED**
</dt> <dd> <dl> <dt>


</dt> <dt>



Attempt was made to execute a method marked with \[disabled\].


</dt> </dl> </dd> <dt>

<span id="WBEM_E_REFRESHER_BUSY"></span><span id="wbem_e_refresher_busy"></span>**WBEM\_E\_REFRESHER\_BUSY**
</dt> <dd> <dl> <dt>

2147749975 (0x80041057)
</dt> <dt>



Refresher is busy with another operation.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_UNPARSABLE_QUERY"></span><span id="wbem_e_unparsable_query"></span>**WBEM\_E\_UNPARSABLE\_QUERY**
</dt> <dd> <dl> <dt>

2147749976 (0x80041058)
</dt> <dt>



Filtering query is syntactically not valid.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_NOT_EVENT_CLASS"></span><span id="wbem_e_not_event_class"></span>**WBEM\_E\_NOT\_EVENT\_CLASS**
</dt> <dd> <dl> <dt>

2147749977 (0x80041059)
</dt> <dt>



The FROM clause of a filtering query references a class that is not an event class (not derived from [**\_\_Event**](--event.md)).


</dt> </dl> </dd> <dt>

<span id="WBEM_E_MISSING_GROUP_WITHIN"></span><span id="wbem_e_missing_group_within"></span>**WBEM\_E\_MISSING\_GROUP\_WITHIN**
</dt> <dd> <dl> <dt>

2147749978 (0x8004105A)
</dt> <dt>



A GROUP BY clause was used without the corresponding GROUP WITHIN clause.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_MISSING_AGGREGATION_LIST"></span><span id="wbem_e_missing_aggregation_list"></span>**WBEM\_E\_MISSING\_AGGREGATION\_LIST**
</dt> <dd> <dl> <dt>

2147749979 (0x8004105B)
</dt> <dt>



A GROUP BY clause was used. Aggregation on all properties is not supported.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_PROPERTY_NOT_AN_OBJECT"></span><span id="wbem_e_property_not_an_object"></span>**WBEM\_E\_PROPERTY\_NOT\_AN\_OBJECT**
</dt> <dd> <dl> <dt>

2147749980 (0x8004105C)
</dt> <dt>



Dot notation was used on a property that is not an embedded object.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_AGGREGATING_BY_OBJECT"></span><span id="wbem_e_aggregating_by_object"></span>**WBEM\_E\_AGGREGATING\_BY\_OBJECT**
</dt> <dd> <dl> <dt>

2147749981 (0x8004105D)
</dt> <dt>



A GROUP BY clause references a property that is an embedded object without using dot notation.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_UNINTERPRETABLE_PROVIDER_QUERY"></span><span id="wbem_e_uninterpretable_provider_query"></span>**WBEM\_E\_UNINTERPRETABLE\_PROVIDER\_QUERY**
</dt> <dd> <dl> <dt>

2147749983 (0x8004105F)
</dt> <dt>



Event provider registration query ([**\_\_EventProviderRegistration**](--eventproviderregistration.md)) did not specify the classes for which events were provided.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_BACKUP_RESTORE_WINMGMT_RUNNING"></span><span id="wbem_e_backup_restore_winmgmt_running"></span>**WBEM\_E\_BACKUP\_RESTORE\_WINMGMT\_RUNNING**
</dt> <dd> <dl> <dt>

2147749984 (0x80041060)
</dt> <dt>



Request was made to back up or restore the repository while it was in use by WinMgmt.exe, or by the SVCHOST process that contains the WMI service.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_QUEUE_OVERFLOW"></span><span id="wbem_e_queue_overflow"></span>**WBEM\_E\_QUEUE\_OVERFLOW**
</dt> <dd> <dl> <dt>

2147749985 (0x80041061)
</dt> <dt>



Asynchronous delivery queue overflowed from the event consumer being too slow.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_PRIVILEGE_NOT_HELD"></span><span id="wbem_e_privilege_not_held"></span>**WBEM\_E\_PRIVILEGE\_NOT\_HELD**
</dt> <dd> <dl> <dt>

2147749986 (0x80041062)
</dt> <dt>



Operation failed because the client did not have the necessary security privilege.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_INVALID_OPERATOR"></span><span id="wbem_e_invalid_operator"></span>**WBEM\_E\_INVALID\_OPERATOR**
</dt> <dd> <dl> <dt>

2147749987 (0x80041063)
</dt> <dt>



Operator is not valid for this property type.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_LOCAL_CREDENTIALS"></span><span id="wbem_e_local_credentials"></span>**WBEM\_E\_LOCAL\_CREDENTIALS**
</dt> <dd> <dl> <dt>

2147749988 (0x80041064)
</dt> <dt>



User specified a username/password/authority on a local connection. The user must use a blank username/password and rely on default security.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_CANNOT_BE_ABSTRACT"></span><span id="wbem_e_cannot_be_abstract"></span>**WBEM\_E\_CANNOT\_BE\_ABSTRACT**
</dt> <dd> <dl> <dt>

2147749989 (0x80041065)
</dt> <dt>



Class was made abstract when its parent class is not abstract.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_AMENDED_OBJECT"></span><span id="wbem_e_amended_object"></span>**WBEM\_E\_AMENDED\_OBJECT**
</dt> <dd> <dl> <dt>

2147749990 (0x80041066)
</dt> <dt>



Amended object was written without the **WBEM\_FLAG\_USE\_AMENDED\_QUALIFIERS** flag being specified.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_CLIENT_TOO_SLOW"></span><span id="wbem_e_client_too_slow"></span>**WBEM\_E\_CLIENT\_TOO\_SLOW**
</dt> <dd> <dl> <dt>

2147749991 (0x80041067)
</dt> <dt>



Client did not retrieve objects quickly enough from an enumeration. This constant is returned when a client creates an enumeration object, but does not retrieve objects from the enumerator in a timely fashion, causing the enumerator's object caches to back up.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_NULL_SECURITY_DESCRIPTOR"></span><span id="wbem_e_null_security_descriptor"></span>**WBEM\_E\_NULL\_SECURITY\_DESCRIPTOR**
</dt> <dd> <dl> <dt>

2147749992 (0x80041068)
</dt> <dt>



Null security descriptor was used.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_TIMED_OUT"></span><span id="wbem_e_timed_out"></span>**WBEM\_E\_TIMED\_OUT**
</dt> <dd> <dl> <dt>

2147749993 (0x80041069)
</dt> <dt>



Operation timed out.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_INVALID_ASSOCIATION"></span><span id="wbem_e_invalid_association"></span>**WBEM\_E\_INVALID\_ASSOCIATION**
</dt> <dd> <dl> <dt>

2147749994
</dt> <dt>



Association is not valid.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_AMBIGUOUS_OPERATION"></span><span id="wbem_e_ambiguous_operation"></span>**WBEM\_E\_AMBIGUOUS\_OPERATION**
</dt> <dd> <dl> <dt>

2147749995 (0x8004106B)
</dt> <dt>



Operation was ambiguous.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_QUOTA_VIOLATION"></span><span id="wbem_e_quota_violation"></span>**WBEM\_E\_QUOTA\_VIOLATION**
</dt> <dd> <dl> <dt>

2147749996 (0x8004106C)
</dt> <dt>



WMI is taking up too much memory. This can be caused by low memory availability or excessive memory consumption by WMI.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_TRANSACTION_CONFLICT"></span><span id="wbem_e_transaction_conflict"></span>**WBEM\_E\_TRANSACTION\_CONFLICT**
</dt> <dd> <dl> <dt>

2147749997 (0x8004106D)
</dt> <dt>



Operation resulted in a transaction conflict.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_FORCED_ROLLBACK"></span><span id="wbem_e_forced_rollback"></span>**WBEM\_E\_FORCED\_ROLLBACK**
</dt> <dd> <dl> <dt>

2147749998 (0x8004106E)
</dt> <dt>



Transaction forced a rollback.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_UNSUPPORTED_LOCALE"></span><span id="wbem_e_unsupported_locale"></span>**WBEM\_E\_UNSUPPORTED\_LOCALE**
</dt> <dd> <dl> <dt>

2147749999 (0x8004106F)
</dt> <dt>



Locale used in the call is not supported.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_HANDLE_OUT_OF_DATE"></span><span id="wbem_e_handle_out_of_date"></span>**WBEM\_E\_HANDLE\_OUT\_OF\_DATE**
</dt> <dd> <dl> <dt>

2147750000 (0x80041070)
</dt> <dt>



Object handle is out-of-date.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_CONNECTION_FAILED"></span><span id="wbem_e_connection_failed"></span>**WBEM\_E\_CONNECTION\_FAILED**
</dt> <dd> <dl> <dt>

2147750001 (0x80041071)
</dt> <dt>



Connection to the SQL database failed.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_INVALID_HANDLE_REQUEST"></span><span id="wbem_e_invalid_handle_request"></span>**WBEM\_E\_INVALID\_HANDLE\_REQUEST**
</dt> <dd> <dl> <dt>

2147750002 (0x80041072)
</dt> <dt>



Handle request was not valid.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_PROPERTY_NAME_TOO_WIDE"></span><span id="wbem_e_property_name_too_wide"></span>**WBEM\_E\_PROPERTY\_NAME\_TOO\_WIDE**
</dt> <dd> <dl> <dt>

2147750003 (0x80041073)
</dt> <dt>



Property name contains more than 255 characters.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_CLASS_NAME_TOO_WIDE"></span><span id="wbem_e_class_name_too_wide"></span>**WBEM\_E\_CLASS\_NAME\_TOO\_WIDE**
</dt> <dd> <dl> <dt>

2147750004 (0x80041074)
</dt> <dt>



Class name contains more than 255 characters.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_METHOD_NAME_TOO_WIDE"></span><span id="wbem_e_method_name_too_wide"></span>**WBEM\_E\_METHOD\_NAME\_TOO\_WIDE**
</dt> <dd> <dl> <dt>

2147750005 (0x80041075)
</dt> <dt>



Method name contains more than 255 characters.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_QUALIFIER_NAME_TOO_WIDE"></span><span id="wbem_e_qualifier_name_too_wide"></span>**WBEM\_E\_QUALIFIER\_NAME\_TOO\_WIDE**
</dt> <dd> <dl> <dt>

2147750006 (0x80041076)
</dt> <dt>



Qualifier name contains more than 255 characters.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_RERUN_COMMAND"></span><span id="wbem_e_rerun_command"></span>**WBEM\_E\_RERUN\_COMMAND**
</dt> <dd> <dl> <dt>

2147750007 (0x80041077)
</dt> <dt>



The SQL command must be rerun because there is a deadlock in SQL. This can be returned only when data is being stored in an SQL database.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_DATABASE_VER_MISMATCH"></span><span id="wbem_e_database_ver_mismatch"></span>**WBEM\_E\_DATABASE\_VER\_MISMATCH**
</dt> <dd> <dl> <dt>

2147750008 (0x80041078)
</dt> <dt>



The database version does not match the version that the repository driver processes.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_VETO_DELETE"></span><span id="wbem_e_veto_delete"></span>**WBEM\_E\_VETO\_DELETE**
</dt> <dd> <dl> <dt>

2147750009 (0x80041079)
</dt> <dt>



WMI cannot execute the delete operation because the provider does not allow it.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_VETO_PUT"></span><span id="wbem_e_veto_put"></span>**WBEM\_E\_VETO\_PUT**
</dt> <dd> <dl> <dt>

2147750010 (0x8004107A)
</dt> <dt>



WMI cannot execute the put operation because the provider does not allow it.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_INVALID_LOCALE"></span><span id="wbem_e_invalid_locale"></span>**WBEM\_E\_INVALID\_LOCALE**
</dt> <dd> <dl> <dt>

2147750016 (0x80041080)
</dt> <dt>



Specified locale identifier was not valid for the operation.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_PROVIDER_SUSPENDED"></span><span id="wbem_e_provider_suspended"></span>**WBEM\_E\_PROVIDER\_SUSPENDED**
</dt> <dd> <dl> <dt>

2147750017 (0x80041081)
</dt> <dt>



Provider is suspended.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_SYNCHRONIZATION_REQUIRED"></span><span id="wbem_e_synchronization_required"></span>**WBEM\_E\_SYNCHRONIZATION\_REQUIRED**
</dt> <dd> <dl> <dt>

2147750018 (0x80041082)
</dt> <dt>



Object must be written to the WMI repository and retrieved again before the requested operation can succeed. This constant is returned when an object must be committed and retrieved to see the property value.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_NO_SCHEMA"></span><span id="wbem_e_no_schema"></span>**WBEM\_E\_NO\_SCHEMA**
</dt> <dd> <dl> <dt>

2147750019 (0x80041083)
</dt> <dt>



Operation cannot be completed; no schema is available.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_PROVIDER_ALREADY_REGISTERED"></span><span id="wbem_e_provider_already_registered"></span>**WBEM\_E\_PROVIDER\_ALREADY\_REGISTERED**
</dt> <dd> <dl> <dt>

02147750020 (0x119FD010)
</dt> <dt>



Provider cannot be registered because it is already registered.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_PROVIDER_NOT_REGISTERED"></span><span id="wbem_e_provider_not_registered"></span>**WBEM\_E\_PROVIDER\_NOT\_REGISTERED**
</dt> <dd> <dl> <dt>

2147750021 (0x80041085)
</dt> <dt>



Provider was not registered.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_FATAL_TRANSPORT_ERROR"></span><span id="wbem_e_fatal_transport_error"></span>**WBEM\_E\_FATAL\_TRANSPORT\_ERROR**
</dt> <dd> <dl> <dt>

2147750022 (0x80041086)
</dt> <dt>



A fatal transport error occurred.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_ENCRYPTED_CONNECTION_REQUIRED"></span><span id="wbem_e_encrypted_connection_required"></span>**WBEM\_E\_ENCRYPTED\_CONNECTION\_REQUIRED**
</dt> <dd> <dl> <dt>

2147750023 (0x80041087)
</dt> <dt>



User attempted to set a computer name or domain without an encrypted connection.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_PROVIDER_TIMED_OUT"></span><span id="wbem_e_provider_timed_out"></span>**WBEM\_E\_PROVIDER\_TIMED\_OUT**
</dt> <dd> <dl> <dt>

2147750024 (0x80041088)
</dt> <dt>



A provider failed to report results within the specified timeout.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_NO_KEY"></span><span id="wbem_e_no_key"></span>**WBEM\_E\_NO\_KEY**
</dt> <dd> <dl> <dt>

2147750025 (0x80041089)
</dt> <dt>



User attempted to put an instance with no defined key.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_PROVIDER_DISABLED"></span><span id="wbem_e_provider_disabled"></span>**WBEM\_E\_PROVIDER\_DISABLED**
</dt> <dd> <dl> <dt>

2147750026 (0x8004108A)
</dt> <dt>



User attempted to register a provider instance but the COM server for the provider instance was unloaded.


</dt> </dl> </dd> <dt>

<span id="WBEMESS_E_REGISTRATION_TOO_BROAD"></span><span id="wbemess_e_registration_too_broad"></span>**WBEMESS\_E\_REGISTRATION\_TOO\_BROAD**
</dt> <dd> <dl> <dt>

2147753985 (0x80042001)
</dt> <dt>



Provider registration overlaps with the system event domain.


</dt> </dl> </dd> <dt>

<span id="WBEMESS_E_REGISTRATION_TOO_PRECISE"></span><span id="wbemess_e_registration_too_precise"></span>**WBEMESS\_E\_REGISTRATION\_TOO\_PRECISE**
</dt> <dd> <dl> <dt>

2147753986 (0x80042002)
</dt> <dt>



A WITHIN clause was not used in this query.


</dt> </dl> </dd> <dt>

<span id="WBEMESS_E_AUTHZ_NOT_PRIVILEGED"></span><span id="wbemess_e_authz_not_privileged"></span>**WBEMESS\_E\_AUTHZ\_NOT\_PRIVILEGED**
</dt> <dd> <dl> <dt>

2147753987 (0x80042003)
</dt> <dt>



This computer does not have the necessary domain permissions to support the security functions that relate to the created subscription instance. Contact the Domain Administrator to get this computer added to the Windows Authorization Access Group.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_RETRY_LATER"></span><span id="wbem_e_retry_later"></span>**WBEM\_E\_RETRY\_LATER**
</dt> <dd> <dl> <dt>

2147758081 (0x80043001)
</dt> <dt>



Reserved for future use.


</dt> </dl> </dd> <dt>

<span id="WBEM_E_RESOURCE_CONTENTION"></span><span id="wbem_e_resource_contention"></span>**WBEM\_E\_RESOURCE\_CONTENTION**
</dt> <dd> <dl> <dt>

2147758082 (0x80043002)
</dt> <dt>



Reserved for future use.


</dt> </dl> </dd> <dt>

<span id="WBEMMOF_E_EXPECTED_QUALIFIER_NAME"></span><span id="wbemmof_e_expected_qualifier_name"></span>**WBEMMOF\_E\_EXPECTED\_QUALIFIER\_NAME**
</dt> <dd> <dl> <dt>

2147762177 (0x80044001)
</dt> <dt>



Expected a qualifier name.


</dt> </dl> </dd> <dt>

<span id="WBEMMOF_E_EXPECTED_SEMI"></span><span id="wbemmof_e_expected_semi"></span>**WBEMMOF\_E\_EXPECTED\_SEMI**
</dt> <dd> <dl> <dt>

2147762178 (0x80044002)
</dt> <dt>



Expected semicolon or '='.


</dt> </dl> </dd> <dt>

<span id="WBEMMOF_E_EXPECTED_OPEN_BRACE"></span><span id="wbemmof_e_expected_open_brace"></span>**WBEMMOF\_E\_EXPECTED\_OPEN\_BRACE**
</dt> <dd> <dl> <dt>

2147762179 (0x80044003)
</dt> <dt>



Expected an opening brace.


</dt> </dl> </dd> <dt>

<span id="WBEMMOF_E_EXPECTED_CLOSE_BRACE"></span><span id="wbemmof_e_expected_close_brace"></span>**WBEMMOF\_E\_EXPECTED\_CLOSE\_BRACE**
</dt> <dd> <dl> <dt>

2147762180 (0x80044004)
</dt> <dt>



Missing closing brace or an illegal array element.


</dt> </dl> </dd> <dt>

<span id="WBEMMOF_E_EXPECTED_CLOSE_BRACKET"></span><span id="wbemmof_e_expected_close_bracket"></span>**WBEMMOF\_E\_EXPECTED\_CLOSE\_BRACKET**
</dt> <dd> <dl> <dt>

2147762181 (0x80044005)
</dt> <dt>



Expected a closing bracket.


</dt> </dl> </dd> <dt>

<span id="WBEMMOF_E_EXPECTED_CLOSE_PAREN"></span><span id="wbemmof_e_expected_close_paren"></span>**WBEMMOF\_E\_EXPECTED\_CLOSE\_PAREN**
</dt> <dd> <dl> <dt>

2147762182 (0x80044006)
</dt> <dt>



Expected closing parenthesis.


</dt> </dl> </dd> <dt>

<span id="WBEMMOF_E_ILLEGAL_CONSTANT_VALUE"></span><span id="wbemmof_e_illegal_constant_value"></span>**WBEMMOF\_E\_ILLEGAL\_CONSTANT\_VALUE**
</dt> <dd> <dl> <dt>

2147762183 (0x80044007)
</dt> <dt>



Numeric value out of range or strings without quotes.


</dt> </dl> </dd> <dt>

<span id="WBEMMOF_E_EXPECTED_TYPE_IDENTIFIER"></span><span id="wbemmof_e_expected_type_identifier"></span>**WBEMMOF\_E\_EXPECTED\_TYPE\_IDENTIFIER**
</dt> <dd> <dl> <dt>

2147762184 (0x80044008)
</dt> <dt>



Expected a type identifier.


</dt> </dl> </dd> <dt>

<span id="WBEMMOF_E_EXPECTED_OPEN_PAREN"></span><span id="wbemmof_e_expected_open_paren"></span>**WBEMMOF\_E\_EXPECTED\_OPEN\_PAREN**
</dt> <dd> <dl> <dt>

2147762185 (0x80044009)
</dt> <dt>



Expected an open parenthesis.


</dt> </dl> </dd> <dt>

<span id="WBEMMOF_E_UNRECOGNIZED_TOKEN"></span><span id="wbemmof_e_unrecognized_token"></span>**WBEMMOF\_E\_UNRECOGNIZED\_TOKEN**
</dt> <dd> <dl> <dt>

2147762186 (0x8004400A)
</dt> <dt>



Unexpected token in the file.


</dt> </dl> </dd> <dt>

<span id="WBEMMOF_E_UNRECOGNIZED_TYPE"></span><span id="wbemmof_e_unrecognized_type"></span>**WBEMMOF\_E\_UNRECOGNIZED\_TYPE**
</dt> <dd> <dl> <dt>

2147762187 (0x8004400B)
</dt> <dt>



Unrecognized or unsupported type identifier.


</dt> </dl> </dd> <dt>

<span id="WBEMMOF_E_EXPECTED_PROPERTY_NAME"></span><span id="wbemmof_e_expected_property_name"></span>**WBEMMOF\_E\_EXPECTED\_PROPERTY\_NAME**
</dt> <dd> <dl> <dt>

2147762187 (0x8004400B)
</dt> <dt>



Expected property or method name.


</dt> </dl> </dd> <dt>

<span id="WBEMMOF_E_TYPEDEF_NOT_SUPPORTED"></span><span id="wbemmof_e_typedef_not_supported"></span>**WBEMMOF\_E\_TYPEDEF\_NOT\_SUPPORTED**
</dt> <dd> <dl> <dt>

2147762189 (0x8004400D)
</dt> <dt>



Typedefs and enumerated types are not supported.


</dt> </dl> </dd> <dt>

<span id="WBEMMOF_E_UNEXPECTED_ALIAS"></span><span id="wbemmof_e_unexpected_alias"></span>**WBEMMOF\_E\_UNEXPECTED\_ALIAS**
</dt> <dd> <dl> <dt>

2147762190 (0x8004400E)
</dt> <dt>



Only a reference to a class object can have an alias value.


</dt> </dl> </dd> <dt>

<span id="WBEMMOF_E_UNEXPECTED_ARRAY_INIT"></span><span id="wbemmof_e_unexpected_array_init"></span>**WBEMMOF\_E\_UNEXPECTED\_ARRAY\_INIT**
</dt> <dd> <dl> <dt>

2147762191 (0x8004400F)
</dt> <dt>



Unexpected array initialization. Arrays must be declared with \[\].


</dt> </dl> </dd> <dt>

<span id="WBEMMOF_E_INVALID_AMENDMENT_SYNTAX"></span><span id="wbemmof_e_invalid_amendment_syntax"></span>**WBEMMOF\_E\_INVALID\_AMENDMENT\_SYNTAX**
</dt> <dd> <dl> <dt>

2147762192 (0x80044010)
</dt> <dt>



Namespace path syntax is not valid.


</dt> </dl> </dd> <dt>

<span id="WBEMMOF_E_INVALID_DUPLICATE_AMENDMENT"></span><span id="wbemmof_e_invalid_duplicate_amendment"></span>**WBEMMOF\_E\_INVALID\_DUPLICATE\_AMENDMENT**
</dt> <dd> <dl> <dt>

2147762193 (0x80044011)
</dt> <dt>



Duplicate amendment specifiers.


</dt> </dl> </dd> <dt>

<span id="WBEMMOF_E_INVALID_PRAGMA"></span><span id="wbemmof_e_invalid_pragma"></span>**WBEMMOF\_E\_INVALID\_PRAGMA**
</dt> <dd> <dl> <dt>

2147762194 (0x80044012)
</dt> <dt>



[\#pragma](pragma-namespace.md) must be followed by a valid keyword.


</dt> </dl> </dd> <dt>

<span id="WBEMMOF_E_INVALID_NAMESPACE_SYNTAX"></span><span id="wbemmof_e_invalid_namespace_syntax"></span>**WBEMMOF\_E\_INVALID\_NAMESPACE\_SYNTAX**
</dt> <dd> <dl> <dt>

2147762195 (0x80044013)
</dt> <dt>



Namespace path syntax is not valid.


</dt> </dl> </dd> <dt>

<span id="WBEMMOF_E_EXPECTED_CLASS_NAME"></span><span id="wbemmof_e_expected_class_name"></span>**WBEMMOF\_E\_EXPECTED\_CLASS\_NAME**
</dt> <dd> <dl> <dt>

2147762196 (0x80044014)
</dt> <dt>



Unexpected character in class name must be an identifier.


</dt> </dl> </dd> <dt>

<span id="WBEMMOF_E_TYPE_MISMATCH"></span><span id="wbemmof_e_type_mismatch"></span>**WBEMMOF\_E\_TYPE\_MISMATCH**
</dt> <dd> <dl> <dt>

2147762197 (0x80044015)
</dt> <dt>



The value specified cannot be made into the appropriate type.


</dt> </dl> </dd> <dt>

<span id="WBEMMOF_E_EXPECTED_ALIAS_NAME"></span><span id="wbemmof_e_expected_alias_name"></span>**WBEMMOF\_E\_EXPECTED\_ALIAS\_NAME**
</dt> <dd> <dl> <dt>

2147762198 (0x80044016)
</dt> <dt>



Dollar sign must be followed by an alias name as an identifier.


</dt> </dl> </dd> <dt>

<span id="WBEMMOF_E_INVALID_CLASS_DECLARATION"></span><span id="wbemmof_e_invalid_class_declaration"></span>**WBEMMOF\_E\_INVALID\_CLASS\_DECLARATION**
</dt> <dd> <dl> <dt>

2147762199 (0x80044017)
</dt> <dt>



Class declaration is not valid.


</dt> </dl> </dd> <dt>

<span id="WBEMMOF_E_INVALID_INSTANCE_DECLARATION"></span><span id="wbemmof_e_invalid_instance_declaration"></span>**WBEMMOF\_E\_INVALID\_INSTANCE\_DECLARATION**
</dt> <dd> <dl> <dt>

2147762200 (0x80044018)
</dt> <dt>



The instance declaration is not valid. It must start with "instance of"


</dt> </dl> </dd> <dt>

<span id="WBEMMOF_E_EXPECTED_DOLLAR"></span><span id="wbemmof_e_expected_dollar"></span>**WBEMMOF\_E\_EXPECTED\_DOLLAR**
</dt> <dd> <dl> <dt>

2147762201 (0x80044019)
</dt> <dt>



Expected dollar sign. An alias in the form "$name" must follow the "as" keyword.


</dt> </dl> </dd> <dt>

<span id="WBEMMOF_E_CIMTYPE_QUALIFIER"></span><span id="wbemmof_e_cimtype_qualifier"></span>**WBEMMOF\_E\_CIMTYPE\_QUALIFIER**
</dt> <dd> <dl> <dt>

2147762202 (0x8004401A)
</dt> <dt>



"CIMTYPE" qualifier cannot be specified directly in a MOF file. Use standard type notation.


</dt> </dl> </dd> <dt>

<span id="WBEMMOF_E_DUPLICATE_PROPERTY"></span><span id="wbemmof_e_duplicate_property"></span>**WBEMMOF\_E\_DUPLICATE\_PROPERTY**
</dt> <dd> <dl> <dt>

2147762203 (0x8004401B)
</dt> <dt>



Duplicate property name was found in the MOF.


</dt> </dl> </dd> <dt>

<span id="WBEMMOF_E_INVALID_NAMESPACE_SPECIFICATION"></span><span id="wbemmof_e_invalid_namespace_specification"></span>**WBEMMOF\_E\_INVALID\_NAMESPACE\_SPECIFICATION**
</dt> <dd> <dl> <dt>

2147762204 (0x8004401C)
</dt> <dt>



Namespace syntax is not valid. References to other servers are not allowed.


</dt> </dl> </dd> <dt>

<span id="WBEMMOF_E_OUT_OF_RANGE"></span><span id="wbemmof_e_out_of_range"></span>**WBEMMOF\_E\_OUT\_OF\_RANGE**
</dt> <dd> <dl> <dt>

2147762205 (0x8004401D)
</dt> <dt>



Value out of range.


</dt> </dl> </dd> <dt>

<span id="WBEMMOF_E_INVALID_FILE"></span><span id="wbemmof_e_invalid_file"></span>**WBEMMOF\_E\_INVALID\_FILE**
</dt> <dd> <dl> <dt>

2147762206 (0x8004401E)
</dt> <dt>



The file is not a valid text MOF file or binary MOF file.


</dt> </dl> </dd> <dt>

<span id="WBEMMOF_E_ALIASES_IN_EMBEDDED"></span><span id="wbemmof_e_aliases_in_embedded"></span>**WBEMMOF\_E\_ALIASES\_IN\_EMBEDDED**
</dt> <dd> <dl> <dt>

2147762207 (0x8004401F)
</dt> <dt>



Embedded objects cannot be aliases.


</dt> </dl> </dd> <dt>

<span id="WBEMMOF_E_NULL_ARRAY_ELEM"></span><span id="wbemmof_e_null_array_elem"></span>**WBEMMOF\_E\_NULL\_ARRAY\_ELEM**
</dt> <dd> <dl> <dt>

2147762208 (0x80044020)
</dt> <dt>



NULL elements in an array are not supported.


</dt> </dl> </dd> <dt>

<span id="WBEMMOF_E_DUPLICATE_QUALIFIER"></span><span id="wbemmof_e_duplicate_qualifier"></span>**WBEMMOF\_E\_DUPLICATE\_QUALIFIER**
</dt> <dd> <dl> <dt>

2147762209 (0x80044021)
</dt> <dt>



Qualifier was used more than once on the object.


</dt> </dl> </dd> <dt>

<span id="WBEMMOF_E_EXPECTED_FLAVOR_TYPE"></span><span id="wbemmof_e_expected_flavor_type"></span>**WBEMMOF\_E\_EXPECTED\_FLAVOR\_TYPE**
</dt> <dd> <dl> <dt>

2147762210 (0x80044022)
</dt> <dt>



Expected a flavor type such as **ToInstance**, **ToSubClass**, **EnableOverride**, or **DisableOverride**.


</dt> </dl> </dd> <dt>

<span id="WBEMMOF_E_INCOMPATIBLE_FLAVOR_TYPES"></span><span id="wbemmof_e_incompatible_flavor_types"></span>**WBEMMOF\_E\_INCOMPATIBLE\_FLAVOR\_TYPES**
</dt> <dd> <dl> <dt>

2147762211 (0x80044023)
</dt> <dt>



Combining **EnableOverride** and **DisableOverride** on same qualifier is not legal.


</dt> </dl> </dd> <dt>

<span id="WBEMMOF_E_MULTIPLE_ALIASES"></span><span id="wbemmof_e_multiple_aliases"></span>**WBEMMOF\_E\_MULTIPLE\_ALIASES**
</dt> <dd> <dl> <dt>

2147762212 (0x80044024)
</dt> <dt>



An alias cannot be used twice.


</dt> </dl> </dd> <dt>

<span id="WBEMMOF_E_INCOMPATIBLE_FLAVOR_TYPES2"></span><span id="wbemmof_e_incompatible_flavor_types2"></span>**WBEMMOF\_E\_INCOMPATIBLE\_FLAVOR\_TYPES2**
</dt> <dd> <dl> <dt>

2147762213 (0x80044025)
</dt> <dt>



Combining **Restricted**, and **ToInstance** or **ToSubClass** is not legal.


</dt> </dl> </dd> <dt>

<span id="WBEMMOF_E_NO_ARRAYS_RETURNED"></span><span id="wbemmof_e_no_arrays_returned"></span>**WBEMMOF\_E\_NO\_ARRAYS\_RETURNED**
</dt> <dd> <dl> <dt>

2147762214 (0x80044026)
</dt> <dt>



Methods cannot return array values.


</dt> </dl> </dd> <dt>

<span id="WBEMMOF_E_MUST_BE_IN_OR_OUT"></span><span id="wbemmof_e_must_be_in_or_out"></span>**WBEMMOF\_E\_MUST\_BE\_IN\_OR\_OUT**
</dt> <dd> <dl> <dt>

2147762215 (0x80044027)
</dt> <dt>



Arguments must have an **In** or **Out** qualifier.


</dt> </dl> </dd> <dt>

<span id="WBEMMOF_E_INVALID_FLAGS_SYNTAX"></span><span id="wbemmof_e_invalid_flags_syntax"></span>**WBEMMOF\_E\_INVALID\_FLAGS\_SYNTAX**
</dt> <dd> <dl> <dt>

2147762216 (0x80044028)
</dt> <dt>



Flags syntax is not valid.


</dt> </dl> </dd> <dt>

<span id="WBEMMOF_E_EXPECTED_BRACE_OR_BAD_TYPE"></span><span id="wbemmof_e_expected_brace_or_bad_type"></span>**WBEMMOF\_E\_EXPECTED\_BRACE\_OR\_BAD\_TYPE**
</dt> <dd> <dl> <dt>

2147762217 (0x80044029)
</dt> <dt>



The final brace and semi-colon for a class are missing.


</dt> </dl> </dd> <dt>

<span id="WBEMMOF_E_UNSUPPORTED_CIMV22_QUAL_VALUE"></span><span id="wbemmof_e_unsupported_cimv22_qual_value"></span>**WBEMMOF\_E\_UNSUPPORTED\_CIMV22\_QUAL\_VALUE**
</dt> <dd> <dl> <dt>

2147762218 (0x8004402A)
</dt> <dt>



A CIM version 2.2 feature is not supported for a qualifier value.


</dt> </dl> </dd> <dt>

<span id="WBEMMOF_E_UNSUPPORTED_CIMV22_DATA_TYPE"></span><span id="wbemmof_e_unsupported_cimv22_data_type"></span>**WBEMMOF\_E\_UNSUPPORTED\_CIMV22\_DATA\_TYPE**
</dt> <dd> <dl> <dt>

2147762219 (0x8004402B)
</dt> <dt>



The CIM version 2.2 data type is not supported.


</dt> </dl> </dd> <dt>

<span id="WBEMMOF_E_INVALID_DELETEINSTANCE_SYNTAX"></span><span id="wbemmof_e_invalid_deleteinstance_syntax"></span>**WBEMMOF\_E\_INVALID\_DELETEINSTANCE\_SYNTAX**
</dt> <dd> <dl> <dt>

2147762220 (0x8004402C)
</dt> <dt>



The delete instance syntax is not valid. It should be `#pragma DeleteInstance("instancepath", FAIL|NOFAIL)`


</dt> </dl> </dd> <dt>

<span id="WBEMMOF_E_INVALID_QUALIFIER_SYNTAX"></span><span id="wbemmof_e_invalid_qualifier_syntax"></span>**WBEMMOF\_E\_INVALID\_QUALIFIER\_SYNTAX**
</dt> <dd> <dl> <dt>

2147762221 (0x8004402D)
</dt> <dt>



The qualifier syntax is not valid. It should be `qualifiername:type=value,scope(class|instance), flavorname`.


</dt> </dl> </dd> <dt>

<span id="WBEMMOF_E_QUALIFIER_USED_OUTSIDE_SCOPE"></span><span id="wbemmof_e_qualifier_used_outside_scope"></span>**WBEMMOF\_E\_QUALIFIER\_USED\_OUTSIDE\_SCOPE**
</dt> <dd> <dl> <dt>

2147762222 (0x8004402E)
</dt> <dt>



The qualifier is used outside of its scope.


</dt> </dl> </dd> <dt>

<span id="WBEMMOF_E_ERROR_CREATING_TEMP_FILE"></span><span id="wbemmof_e_error_creating_temp_file"></span>**WBEMMOF\_E\_ERROR\_CREATING\_TEMP\_FILE**
</dt> <dd> <dl> <dt>

2147762223 (0x8004402F)
</dt> <dt>



Error creating temporary file. The temporary file is an intermediate stage in the MOF compilation.


</dt> </dl> </dd> <dt>

<span id="WBEMMOF_E_ERROR_INVALID_INCLUDE_FILE"></span><span id="wbemmof_e_error_invalid_include_file"></span>**WBEMMOF\_E\_ERROR\_INVALID\_INCLUDE\_FILE**
</dt> <dd> <dl> <dt>

2147762224 (0x80044030)
</dt> <dt>



A file included in the MOF by the preprocessor command [\#include](-include.md) is not valid.


</dt> </dl> </dd> <dt>

<span id="WBEMMOF_E_INVALID_DELETECLASS_SYNTAX"></span><span id="wbemmof_e_invalid_deleteclass_syntax"></span>**WBEMMOF\_E\_INVALID\_DELETECLASS\_SYNTAX**
</dt> <dd> <dl> <dt>

2147762225 (0x80044031)
</dt> <dt>



The syntax for the preprocessor commands [\#pragma deleteinstance](pragma-deleteinstance.md) or [\#pragma deleteclass](pragma-deleteclass.md) is not valid.


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Header<br/>                   | <dl> <dt>WbemCli.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>WbemCli.idl</dt> </dl> |



## See also

<dl> <dt>

[WMI Return Codes](wmi-return-codes.md)
</dt> </dl>

 

