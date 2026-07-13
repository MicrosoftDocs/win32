---
description: A specialized class that contains information about the severity, cause, recommended actions and other data related to the failure of a CIM Operation. Instances of this type MAY be included as part of the response to a CIM Operation.
ms.assetid: a7dc450d-7dbd-4097-a186-0e42f100fbfe
title: CIM_Error WMI class
ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_Error
- CIM_Error.ErrorType
- CIM_Error.OtherErrorType
- CIM_Error.OwningEntity
- CIM_Error.MessageID
- CIM_Error.Message
- CIM_Error.MessageArguments
- CIM_Error.PerceivedSeverity
- CIM_Error.ProbableCause
- CIM_Error.ProbableCauseDescription
- CIM_Error.RecommendedActions
- CIM_Error.ErrorSource
- CIM_Error.ErrorSourceFormat
- CIM_Error.OtherErrorSourceFormat
- CIM_Error.CIMStatusCode
- CIM_Error.CIMStatusCodeDescription
api_type: 
- DllExport
api_location: 
- netTCPIP.dll
ROBOTS: INDEX,FOLLOW
---

# CIM_Error WMI class

A specialized class that contains information about the severity, cause, recommended actions and other data related to the failure of a CIM Operation. Instances of this type MAY be included as part of the response to a CIM Operation.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Indication, Exception, UMLPackagePath("CIM::Interop"), Version("2.22.1"), AMENDMENT]
class CIM_Error
{
  uint16 ErrorType;
  string OtherErrorType;
  string OwningEntity;
  string MessageID;
  string Message;
  string MessageArguments[];
  uint16 PerceivedSeverity;
  uint16 ProbableCause;
  string ProbableCauseDescription;
  string RecommendedActions[];
  string ErrorSource;
  uint16 ErrorSourceFormat = 0;
  string OtherErrorSourceFormat;
  uint32 CIMStatusCode;
  string CIMStatusCodeDescription;
};
```

## Members

The **CIM\_Error** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_Error** class has these properties.

<dl> <dt>

**CIMStatusCode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/win32/wmisdk/standard-qualifiers) ("CIM\_Error.CIMStatusCodeDescription")
</dt> </dl>

The CIM status code that characterizes this instance. This property defines the status codes that can be return by a conforming CIM Server or Listener. Note that not all status codes are valid for each operation. The specification for each operation should define the status codes that may be returned by that operation.

The possible values are.



| Value                                                                                                                                                                                                                                                                                                                | Meaning                                                                                   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| <span id="CIM_ERR_FAILED"></span><span id="cim_err_failed"></span><dl> <dt>**CIM\_ERR\_FAILED**</dt> <dt>1</dt> </dl>                                                                                             | A general error occurred that is not covered by a more specific error code.<br/>    |
| <span id="CIM_ERR_ACCESS_DENIED"></span><span id="cim_err_access_denied"></span><dl> <dt>**CIM\_ERR\_ACCESS\_DENIED**</dt> <dt>2</dt> </dl>                                                                       | Access to a CIM resource was not available to the client.<br/>                      |
| <span id="CIM_ERR_INVALID_NAMESPACE"></span><span id="cim_err_invalid_namespace"></span><dl> <dt>**CIM\_ERR\_INVALID\_NAMESPACE**</dt> <dt>3</dt> </dl>                                                           | The target namespace does not exist.<br/>                                           |
| <span id="CIM_ERR_INVALID_PARAMETER"></span><span id="cim_err_invalid_parameter"></span><dl> <dt>**CIM\_ERR\_INVALID\_PARAMETER**</dt> <dt>4</dt> </dl>                                                           | One or more parameter values passed to the method were not valid.<br/>              |
| <span id="CIM_ERR_INVALID_CLASS"></span><span id="cim_err_invalid_class"></span><dl> <dt>**CIM\_ERR\_INVALID\_CLASS**</dt> <dt>5</dt> </dl>                                                                       | The specified class does not exist.<br/>                                            |
| <span id="CIM_ERR_NOT_FOUND"></span><span id="cim_err_not_found"></span><dl> <dt>**CIM\_ERR\_NOT\_FOUND**</dt> <dt>6</dt> </dl>                                                                                   | The requested object could not be found. <br/>                                      |
| <span id="CIM_ERR_NOT_SUPPORTED"></span><span id="cim_err_not_supported"></span><dl> <dt>**CIM\_ERR\_NOT\_SUPPORTED**</dt> <dt>7</dt> </dl>                                                                       | The requested operation is not supported.<br/>                                      |
| <span id="CIM_ERR_CLASS_HAS_CHILDREN"></span><span id="cim_err_class_has_children"></span><dl> <dt>**CIM\_ERR\_CLASS\_HAS\_CHILDREN**</dt> <dt>8</dt> </dl>                                                       | Operation cannot be carried out on this class since it has instances.<br/>          |
| <span id="CIM_ERR_CLASS_HAS_INSTANCES"></span><span id="cim_err_class_has_instances"></span><dl> <dt>**CIM\_ERR\_CLASS\_HAS\_INSTANCES**</dt> <dt>9</dt> </dl>                                                    | Operation cannot be carried out on this class since it has instances.<br/>          |
| <span id="CIM_ERR_INVALID_SUPERCLASS"></span><span id="cim_err_invalid_superclass"></span><dl> <dt>**CIM\_ERR\_INVALID\_SUPERCLASS**</dt> <dt>10</dt> </dl>                                                       | Operation cannot be carried out since the specified superclass does not exist.<br/> |
| <span id="CIM_ERR_ALREADY_EXISTS"></span><span id="cim_err_already_exists"></span><dl> <dt>**CIM\_ERR\_ALREADY\_EXISTS**</dt> <dt>11</dt> </dl>                                                                   | Operation cannot be carried out because an object already exists.<br/>              |
| <span id="CIM_ERR_NO_SUCH_PROPERTY"></span><span id="cim_err_no_such_property"></span><dl> <dt>**CIM\_ERR\_NO\_SUCH\_PROPERTY**</dt> <dt>12</dt> </dl>                                                            | The specified Property does not exist.<br/>                                         |
| <span id="CIM_ERR_TYPE_MISMATCH"></span><span id="cim_err_type_mismatch"></span><dl> <dt>**CIM\_ERR\_TYPE\_MISMATCH**</dt> <dt>13</dt> </dl>                                                                      | The value supplied is incompatible with the type.<br/>                              |
| <span id="CIM_ERR_QUERY_LANGUAGE_NOT_SUPPORTED"></span><span id="cim_err_query_language_not_supported"></span><dl> <dt>**CIM\_ERR\_QUERY\_LANGUAGE\_NOT\_SUPPORTED**</dt> <dt>14</dt> </dl>                       | The query language is not recognized or supported.<br/>                             |
| <span id="CIM_ERR_INVALID_QUERY"></span><span id="cim_err_invalid_query"></span><dl> <dt>**CIM\_ERR\_INVALID\_QUERY**</dt> <dt>15</dt> </dl>                                                                      | The query is not valid for the specified query language.<br/>                       |
| <span id="CIM_ERR_METHOD_NOT_AVAILABLE"></span><span id="cim_err_method_not_available"></span><dl> <dt>**CIM\_ERR\_METHOD\_NOT\_AVAILABLE**</dt> <dt>16</dt> </dl>                                                | The extrinsic Method could not be executed.<br/>                                    |
| <span id="CIM_ERR_METHOD_NOT_FOUND"></span><span id="cim_err_method_not_found"></span><dl> <dt>**CIM\_ERR\_METHOD\_NOT\_FOUND**</dt> <dt>17</dt> </dl>                                                            | The specified extrinsic Method does not exist.<br/>                                 |
| <span id="CIM_ERR_UNEXPECTED_RESPONSE"></span><span id="cim_err_unexpected_response"></span><dl> <dt>**CIM\_ERR\_UNEXPECTED\_RESPONSE**</dt> <dt>18</dt> </dl>                                                    | The returned response to the asynchronous operation was not expected.<br/>          |
| <span id="CIM_ERR_INVALID_RESPONSE_DESTINATION"></span><span id="cim_err_invalid_response_destination"></span><dl> <dt>**CIM\_ERR\_INVALID\_RESPONSE\_DESTINATION**</dt> <dt>19</dt> </dl>                        | The specified destination for the asynchronous response is not valid.<br/>          |
| <span id="CIM_ERR_NAMESPACE_NOT_EMPTY"></span><span id="cim_err_namespace_not_empty"></span><dl> <dt>**CIM\_ERR\_NAMESPACE\_NOT\_EMPTY**</dt> <dt>20</dt> </dl>                                                   | The specified namespace is not empty.<br/>                                          |
| <span id="CIM_ERR_INVALID_ENUMERATION_CONTEXT"></span><span id="cim_err_invalid_enumeration_context"></span><dl> <dt>**CIM\_ERR\_INVALID\_ENUMERATION\_CONTEXT**</dt> <dt>21</dt> </dl>                           | The enumeration context supplied is not valid.<br/>                                 |
| <span id="CIM_ERR_INVALID_OPERATION_TIMEOUT"></span><span id="cim_err_invalid_operation_timeout"></span><dl> <dt>**CIM\_ERR\_INVALID\_OPERATION\_TIMEOUT**</dt> <dt>22</dt> </dl>                                 | The specified Namespace is not empty.<br/>                                          |
| <span id="CIM_ERR_PULL_HAS_BEEN_ABANDONED"></span><span id="cim_err_pull_has_been_abandoned"></span><dl> <dt>**CIM\_ERR\_PULL\_HAS\_BEEN\_ABANDONED**</dt> <dt>23</dt> </dl>                                      | The specified Namespace is not empty.<br/>                                          |
| <span id="CIM_ERR_PULL_CANNOT_BE_ABANDONED"></span><span id="cim_err_pull_cannot_be_abandoned"></span><dl> <dt>**CIM\_ERR\_PULL\_CANNOT\_BE\_ABANDONED**</dt> <dt>24</dt> </dl>                                   | The attempt to abandon a pull operation has failed.<br/>                            |
| <span id="CIM_ERR_FILTERED_ENUMERATION_NOT_SUPPORTED"></span><span id="cim_err_filtered_enumeration_not_supported"></span><dl> <dt>**CIM\_ERR\_FILTERED\_ENUMERATION\_NOT\_SUPPORTED**</dt> <dt>25</dt> </dl>     | Filtered Enumerations are not supported.<br/>                                       |
| <span id="CIM_ERR_CONTINUATION_ON_ERROR_NOT_SUPPORTED"></span><span id="cim_err_continuation_on_error_not_supported"></span><dl> <dt>**CIM\_ERR\_CONTINUATION\_ON\_ERROR\_NOT\_SUPPORTED**</dt> <dt>26</dt> </dl> | Continue on error is not supported.<br/>                                            |
| <span id="CIM_ERR_SERVER_LIMITS_EXCEEDED"></span><span id="cim_err_server_limits_exceeded"></span><dl> <dt>**CIM\_ERR\_SERVER\_LIMITS\_EXCEEDED**</dt> <dt>27</dt> </dl>                                          | The WBEM Server limits have been exceeded (e.g. memory, connections, ...)<br/>      |
| <span id="CIM_ERR_SERVER_IS_SHUTTING_DOWN"></span><span id="cim_err_server_is_shutting_down"></span><dl> <dt>**CIM\_ERR\_SERVER\_IS\_SHUTTING\_DOWN**</dt> <dt>28</dt> </dl>                                      | The WBEM Server is shutting down.<br/>                                              |
| <span id="CIM_ERR_QUERY_FEATURE_NOT_SUPPORTED"></span><span id="cim_err_query_feature_not_supported"></span><dl> <dt>**CIM\_ERR\_QUERY\_FEATURE\_NOT\_SUPPORTED**</dt> <dt>29</dt> </dl>                          | The specified Query Feature is not supported.<br/>                                  |
| <span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span><dl> <dt>**DMTF Reserved**</dt> <dt>30 65535</dt> </dl>                                                           | Reserved for future use.<br/>                                                       |



 

</dd> <dt>

**CIMStatusCodeDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/win32/wmisdk/standard-qualifiers) ("CIM\_Error.CIMStatusCode")
</dt> </dl>

A free-form string containing a human-readable description of the **CIMStatusCode** property. This description can extend, but must be consistent with, the value of **CIMStatusCode**.

</dd> <dt>

**ErrorSource**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/win32/wmisdk/standard-qualifiers) ("CIM\_Error.ErrorSourceFormat")
</dt> </dl>

Identifies the entity or instance generating the error. If this entity is modeled in the CIM Schema, this property contains the path of the instance encoded as a string parameter. If not modeled, the property contains some identifying string that names the entity that generated the error. The path or identifying string is formatted per the **ErrorSourceFormat** property.

</dd> <dt>

**ErrorSourceFormat**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/win32/wmisdk/standard-qualifiers) ("CIM\_Error.ErrorSource", "CIM\_Error.OtherErrorSourceFormat")
</dt> </dl>

Describes the format of the **ErrorSource** property.

The possible values are.



| Value                                                                                                                                                                                                                                                     | Meaning                                                                                          |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>0</dt> </dl>                               | The format is unknown or not meaningfully interpretable by a CIM client application. <br/> |
| <span id="Other"></span><span id="other"></span><span id="OTHER"></span><dl> <dt>**Other**</dt> <dt>1</dt> </dl>                                       | The format is defined by the value of the OtherErrorSourceFormat property.<br/>            |
| <span id="CIMObjectPath"></span><span id="cimobjectpath"></span><span id="CIMOBJECTPATH"></span><dl> <dt>**CIMObjectPath**</dt> <dt>2</dt> </dl>       | A CIM Object Path as defined in the CIM Infrastructure specification.<br/>                 |
| <span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span><dl> <dt>**DMTF Reserved**</dt> <dt>3 65535</dt> </dl> | Reserved for future use.<br/>                                                              |



 

</dd> <dt>

**ErrorType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/win32/wmisdk/standard-qualifiers) ("CIM\_Error.OtherErrorType")
</dt> </dl>

Primary classification of the error.

The possible values are.



| Value                                                                                                                                                                                                                                                                                                        | Meaning                                                                                                                                                  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>0</dt> </dl>                                                                                  | Unknown.<br/>                                                                                                                                      |
| <span id="Other"></span><span id="other"></span><span id="OTHER"></span><dl> <dt>**Other**</dt> <dt>1</dt> </dl>                                                                                          | Other.<br/>                                                                                                                                        |
| <span id="Communications_Error"></span><span id="communications_error"></span><span id="COMMUNICATIONS_ERROR"></span><dl> <dt>**Communications Error**</dt> <dt>2</dt> </dl>                              | Errors of this type are principally associated with the procedures and/or processes required to convey information from one point to another.<br/> |
| <span id="Quality_of_Service_Error"></span><span id="quality_of_service_error"></span><span id="QUALITY_OF_SERVICE_ERROR"></span><dl> <dt>**Quality of Service Error**</dt> <dt>3</dt> </dl>              | Quality of Service Error. Errors of this type are principally associated with failures that result in reduced functionality or performance.<br/>   |
| <span id="Software_Error"></span><span id="software_error"></span><span id="SOFTWARE_ERROR"></span><dl> <dt>**Software Error**</dt> <dt>4</dt> </dl>                                                      | Error of this type are principally associated with a software or processing fault.<br/>                                                            |
| <span id="Hardware_Error"></span><span id="hardware_error"></span><span id="HARDWARE_ERROR"></span><dl> <dt>**Hardware Error**</dt> <dt>5</dt> </dl>                                                      | Errors of this type are principally associated with an equipment or hardware failure.<br/>                                                         |
| <span id="Environmental_Error"></span><span id="environmental_error"></span><span id="ENVIRONMENTAL_ERROR"></span><dl> <dt>**Environmental Error**</dt> <dt>6</dt> </dl>                                  | Errors of this type are principally associated with a failure condition relating the to facility, or other environmental considerations.<br/>      |
| <span id="Security_Error"></span><span id="security_error"></span><span id="SECURITY_ERROR"></span><dl> <dt>**Security Error**</dt> <dt>7</dt> </dl>                                                      | Errors of this type are associated with security violations, detection of viruses, and similar issues.<br/>                                        |
| <span id="Oversubscription_Error"></span><span id="oversubscription_error"></span><span id="OVERSUBSCRIPTION_ERROR"></span><dl> <dt>**Oversubscription Error**</dt> <dt>8</dt> </dl>                      | Errors of this type are principally associated with the failure to allocate sufficient resources to complete the operation.<br/>                   |
| <span id="Unavailable_Resource_Error"></span><span id="unavailable_resource_error"></span><span id="UNAVAILABLE_RESOURCE_ERROR"></span><dl> <dt>**Unavailable Resource Error**</dt> <dt>9</dt> </dl>      | Errors of this type are principally associated with the failure to access a required resource.<br/>                                                |
| <span id="Unsupported_Operation_Error"></span><span id="unsupported_operation_error"></span><span id="UNSUPPORTED_OPERATION_ERROR"></span><dl> <dt>**Unsupported Operation Error**</dt> <dt>10</dt> </dl> | Errors of this type are principally associated with requests that are not supported.<br/>                                                          |
| <span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span><dl> <dt>**DMTF Reserved**</dt> <dt>11 65535</dt> </dl>                                                   |                                                                                                                                                          |



 

</dd> <dt>

**Message**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/win32/wmisdk/standard-qualifiers) ("CIM\_Error.MessageID", "CIM\_Error.MessageArguments")
</dt> </dl>

The formatted message. This message is constructed by combining some or all of the dynamic elements specified in the **MessageArguments** property with the static elements defined in the **MessageID**.

</dd> <dt>

**MessageArguments**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/win32/wmisdk/standard-qualifiers) ("CIM\_Error.MessageID", "CIM\_Error.Message")
</dt> </dl>

An array containing the dynamic content of the message.

</dd> <dt>

**MessageID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers), [**ModelCorrespondence**](/windows/win32/wmisdk/standard-qualifiers) ("CIM\_Error.Message", "CIM\_Error.MessageArguments")
</dt> </dl>

An externally defined string that uniquely identifies, within the scope of the **OwningEntity**, the format of the Message.

</dd> <dt>

**OtherErrorSourceFormat**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/win32/wmisdk/standard-qualifiers) ("CIM\_Error.ErrorSourceFormat")
</dt> </dl>

Describes other values for **ErrorSourceFormat**. When **ErrorSourceFormat** is **Other**, this property must be non-**NULL**. For all other values of **ErrorSourceFormat**, this property must be set to **NULL**.

</dd> <dt>

**OtherErrorType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/win32/wmisdk/standard-qualifiers) ("CIM\_Error.ErrorType")
</dt> </dl>

A free-form string describing the error when the **ErrorType** property is **Other**.

</dd> <dt>

**OwningEntity**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string that uniquely identifies the entity that owns the definition of the format of the Message described in this instance. **OwningEntity** must include a copyrighted, trademarked or otherwise unique name that is owned by the business entity or standards body defining the format.

</dd> <dt>

**PerceivedSeverity**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

An enumerated value that describes the severity of the error as determined by the notifier.

The possible values are.



| Value                                                                                                                                                                                                                                                                           | Meaning                                                                        |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>0</dt> </dl>                                                     | The severity is unknown.<br/>                                            |
| <span id="Other"></span><span id="other"></span><span id="OTHER"></span><dl> <dt>**Other**</dt> <dt>1</dt> </dl>                                                             | The severity's value can be found in the OtherSeverity property.<br/>    |
| <span id="Information"></span><span id="information"></span><span id="INFORMATION"></span><dl> <dt>**Information**</dt> <dt>2</dt> </dl>                                     | Provides an informative response.<br/>                                   |
| <span id="Degraded_Warning"></span><span id="degraded_warning"></span><span id="DEGRADED_WARNING"></span><dl> <dt>**Degraded/Warning**</dt> <dt>3</dt> </dl>                 | An action may be needed.<br/>                                            |
| <span id="Minor"></span><span id="minor"></span><span id="MINOR"></span><dl> <dt>**Minor**</dt> <dt>4</dt> </dl>                                                             | An action is needed, but the situation is not serious at this time.<br/> |
| <span id="Major"></span><span id="major"></span><span id="MAJOR"></span><dl> <dt>**Major**</dt> <dt>5</dt> </dl>                                                             | Action is needed immediately.<br/>                                       |
| <span id="Critical"></span><span id="critical"></span><span id="CRITICAL"></span><dl> <dt>**Critical**</dt> <dt>6</dt> </dl>                                                 | Action is needed immediately, and the scope is broad.<br/>               |
| <span id="Fatal_NonRecoverable"></span><span id="fatal_nonrecoverable"></span><span id="FATAL_NONRECOVERABLE"></span><dl> <dt>**Fatal/NonRecoverable**</dt> <dt>7</dt> </dl> | An error has occurred, but it too late to take action.<br/>              |
| <span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span><dl> <dt>**DMTF Reserved**</dt> <dt>8 65535</dt> </dl>                       | Reserved for future use.<br/>                                            |



 

</dd> <dt>

**ProbableCause**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/win32/wmisdk/standard-qualifiers) ("CIM\_Error.ProbableCauseDescription")
</dt> </dl>

An enumerated value that describes the probable cause of the error.

The possible values are.



| Value                                                                                                                                                                                                                                                                                                                                                                    | Meaning                             |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>0</dt> </dl>                                                                                                                                              |                                     |
| <span id="Other"></span><span id="other"></span><span id="OTHER"></span><dl> <dt>**Other**</dt> <dt>1</dt> </dl>                                                                                                                                                      |                                     |
| <span id="Adapter_Card_Error"></span><span id="adapter_card_error"></span><span id="ADAPTER_CARD_ERROR"></span><dl> <dt>**Adapter/Card Error**</dt> <dt>2</dt> </dl>                                                                                                  |                                     |
| <span id="Application_Subsystem_Failure"></span><span id="application_subsystem_failure"></span><span id="APPLICATION_SUBSYSTEM_FAILURE"></span><dl> <dt>**Application Subsystem Failure**</dt> <dt>3</dt> </dl>                                                      |                                     |
| <span id="Bandwidth_Reduced"></span><span id="bandwidth_reduced"></span><span id="BANDWIDTH_REDUCED"></span><dl> <dt>**Bandwidth Reduced**</dt> <dt>4</dt> </dl>                                                                                                      |                                     |
| <span id="Connection_Establishment_Error"></span><span id="connection_establishment_error"></span><span id="CONNECTION_ESTABLISHMENT_ERROR"></span><dl> <dt>**Connection Establishment Error**</dt> <dt>5</dt> </dl>                                                  |                                     |
| <span id="Communications_Protocol_Error"></span><span id="communications_protocol_error"></span><span id="COMMUNICATIONS_PROTOCOL_ERROR"></span><dl> <dt>**Communications Protocol Error**</dt> <dt>6</dt> </dl>                                                      |                                     |
| <span id="Communications_Subsystem_Failure"></span><span id="communications_subsystem_failure"></span><span id="COMMUNICATIONS_SUBSYSTEM_FAILURE"></span><dl> <dt>**Communications Subsystem Failure**</dt> <dt>7</dt> </dl>                                          |                                     |
| <span id="Configuration_Customization_Error"></span><span id="configuration_customization_error"></span><span id="CONFIGURATION_CUSTOMIZATION_ERROR"></span><dl> <dt>**Configuration/Customization Error**</dt> <dt>8</dt> </dl>                                      |                                     |
| <span id="Congestion"></span><span id="congestion"></span><span id="CONGESTION"></span><dl> <dt>**Congestion**</dt> <dt>9</dt> </dl>                                                                                                                                  |                                     |
| <span id="Corrupt_Data"></span><span id="corrupt_data"></span><span id="CORRUPT_DATA"></span><dl> <dt>**Corrupt Data**</dt> <dt>10</dt> </dl>                                                                                                                         |                                     |
| <span id="CPU_Cycles_Limit_Exceeded"></span><span id="cpu_cycles_limit_exceeded"></span><span id="CPU_CYCLES_LIMIT_EXCEEDED"></span><dl> <dt>**CPU Cycles Limit Exceeded**</dt> <dt>11</dt> </dl>                                                                     |                                     |
| <span id="Dataset_Modem_Error"></span><span id="dataset_modem_error"></span><span id="DATASET_MODEM_ERROR"></span><dl> <dt>**Dataset/Modem Error**</dt> <dt>12</dt> </dl>                                                                                             |                                     |
| <span id="Degraded_Signal"></span><span id="degraded_signal"></span><span id="DEGRADED_SIGNAL"></span><dl> <dt>**Degraded Signal**</dt> <dt>13</dt> </dl>                                                                                                             |                                     |
| <span id="DTE-DCE_Interface_Error"></span><span id="dte-dce_interface_error"></span><span id="DTE-DCE_INTERFACE_ERROR"></span><dl> <dt>**DTE-DCE Interface Error**</dt> <dt>14</dt> </dl>                                                                             |                                     |
| <span id="Enclosure_Door_Open"></span><span id="enclosure_door_open"></span><span id="ENCLOSURE_DOOR_OPEN"></span><dl> <dt>**Enclosure Door Open**</dt> <dt>15</dt> </dl>                                                                                             |                                     |
| <span id="Equipment_Malfunction"></span><span id="equipment_malfunction"></span><span id="EQUIPMENT_MALFUNCTION"></span><dl> <dt>**Equipment Malfunction**</dt> <dt>16</dt> </dl>                                                                                     |                                     |
| <span id="Excessive_Vibration"></span><span id="excessive_vibration"></span><span id="EXCESSIVE_VIBRATION"></span><dl> <dt>**Excessive Vibration**</dt> <dt>17</dt> </dl>                                                                                             |                                     |
| <span id="File_Format_Error"></span><span id="file_format_error"></span><span id="FILE_FORMAT_ERROR"></span><dl> <dt>**File Format Error**</dt> <dt>18</dt> </dl>                                                                                                     |                                     |
| <span id="Fire_Detected"></span><span id="fire_detected"></span><span id="FIRE_DETECTED"></span><dl> <dt>**Fire Detected**</dt> <dt>19</dt> </dl>                                                                                                                     |                                     |
| <span id="Flood_Detected"></span><span id="flood_detected"></span><span id="FLOOD_DETECTED"></span><dl> <dt>**Flood Detected**</dt> <dt>20</dt> </dl>                                                                                                                 |                                     |
| <span id="Framing_Error"></span><span id="framing_error"></span><span id="FRAMING_ERROR"></span><dl> <dt>**Framing Error**</dt> <dt>21</dt> </dl>                                                                                                                     |                                     |
| <span id="HVAC_Problem"></span><span id="hvac_problem"></span><span id="HVAC_PROBLEM"></span><dl> <dt>**HVAC Problem**</dt> <dt>22</dt> </dl>                                                                                                                         |                                     |
| <span id="Humidity_Unacceptable"></span><span id="humidity_unacceptable"></span><span id="HUMIDITY_UNACCEPTABLE"></span><dl> <dt>**Humidity Unacceptable**</dt> <dt>23</dt> </dl>                                                                                     |                                     |
| <span id="I_O_Device_Error"></span><span id="i_o_device_error"></span><span id="I_O_DEVICE_ERROR"></span><dl> <dt>**I/O Device Error**</dt> <dt>24</dt> </dl>                                                                                                         |                                     |
| <span id="Input_Device_Error"></span><span id="input_device_error"></span><span id="INPUT_DEVICE_ERROR"></span><dl> <dt>**Input Device Error**</dt> <dt>25</dt> </dl>                                                                                                 |                                     |
| <span id="LAN_Error"></span><span id="lan_error"></span><span id="LAN_ERROR"></span><dl> <dt>**LAN Error**</dt> <dt>26</dt> </dl>                                                                                                                                     |                                     |
| <span id="Non-Toxic_Leak_Detected"></span><span id="non-toxic_leak_detected"></span><span id="NON-TOXIC_LEAK_DETECTED"></span><dl> <dt>**Non-Toxic Leak Detected**</dt> <dt>27</dt> </dl>                                                                             |                                     |
| <span id="Local_Node_Transmission_Error"></span><span id="local_node_transmission_error"></span><span id="LOCAL_NODE_TRANSMISSION_ERROR"></span><dl> <dt>**Local Node Transmission Error**</dt> <dt>28</dt> </dl>                                                     |                                     |
| <span id="Loss_of_Frame"></span><span id="loss_of_frame"></span><span id="LOSS_OF_FRAME"></span><dl> <dt>**Loss of Frame**</dt> <dt>29</dt> </dl>                                                                                                                     |                                     |
| <span id="Loss_of_Signal"></span><span id="loss_of_signal"></span><span id="LOSS_OF_SIGNAL"></span><dl> <dt>**Loss of Signal**</dt> <dt>30</dt> </dl>                                                                                                                 |                                     |
| <span id="Material_Supply_Exhausted"></span><span id="material_supply_exhausted"></span><span id="MATERIAL_SUPPLY_EXHAUSTED"></span><dl> <dt>**Material Supply Exhausted**</dt> <dt>31</dt> </dl>                                                                     |                                     |
| <span id="Multiplexer_Problem"></span><span id="multiplexer_problem"></span><span id="MULTIPLEXER_PROBLEM"></span><dl> <dt>**Multiplexer Problem**</dt> <dt>32</dt> </dl>                                                                                             |                                     |
| <span id="Out_of_Memory"></span><span id="out_of_memory"></span><span id="OUT_OF_MEMORY"></span><dl> <dt>**Out of Memory**</dt> <dt>33</dt> </dl>                                                                                                                     |                                     |
| <span id="Output_Device_Error"></span><span id="output_device_error"></span><span id="OUTPUT_DEVICE_ERROR"></span><dl> <dt>**Output Device Error**</dt> <dt>34</dt> </dl>                                                                                             |                                     |
| <span id="Performance_Degraded"></span><span id="performance_degraded"></span><span id="PERFORMANCE_DEGRADED"></span><dl> <dt>**Performance Degraded**</dt> <dt>35</dt> </dl>                                                                                         |                                     |
| <span id="Power_Problem"></span><span id="power_problem"></span><span id="POWER_PROBLEM"></span><dl> <dt>**Power Problem**</dt> <dt>36</dt> </dl>                                                                                                                     |                                     |
| <span id="Pressure_Unacceptable"></span><span id="pressure_unacceptable"></span><span id="PRESSURE_UNACCEPTABLE"></span><dl> <dt>**Pressure Unacceptable**</dt> <dt>37</dt> </dl>                                                                                     |                                     |
| <span id="Processor_Problem__Internal_Machine_Error_"></span><span id="processor_problem__internal_machine_error_"></span><span id="PROCESSOR_PROBLEM__INTERNAL_MACHINE_ERROR_"></span><dl> <dt>**Processor Problem (Internal Machine Error)**</dt> <dt>38</dt> </dl> |                                     |
| <span id="Pump_Failure"></span><span id="pump_failure"></span><span id="PUMP_FAILURE"></span><dl> <dt>**Pump Failure**</dt> <dt>39</dt> </dl>                                                                                                                         |                                     |
| <span id="Queue_Size_Exceeded"></span><span id="queue_size_exceeded"></span><span id="QUEUE_SIZE_EXCEEDED"></span><dl> <dt>**Queue Size Exceeded**</dt> <dt>40</dt> </dl>                                                                                             |                                     |
| <span id="Receive_Failure"></span><span id="receive_failure"></span><span id="RECEIVE_FAILURE"></span><dl> <dt>**Receive Failure**</dt> <dt>41</dt> </dl>                                                                                                             |                                     |
| <span id="Receiver_Failure"></span><span id="receiver_failure"></span><span id="RECEIVER_FAILURE"></span><dl> <dt>**Receiver Failure**</dt> <dt>42</dt> </dl>                                                                                                         |                                     |
| <span id="Remote_Node_Transmission_Error"></span><span id="remote_node_transmission_error"></span><span id="REMOTE_NODE_TRANSMISSION_ERROR"></span><dl> <dt>**Remote Node Transmission Error**</dt> <dt>43</dt> </dl>                                                 |                                     |
| <span id="Resource_at_or_Nearing_Capacity"></span><span id="resource_at_or_nearing_capacity"></span><span id="RESOURCE_AT_OR_NEARING_CAPACITY"></span><dl> <dt>**Resource at or Nearing Capacity**</dt> <dt>44</dt> </dl>                                             |                                     |
| <span id="Response_Time_Excessive"></span><span id="response_time_excessive"></span><span id="RESPONSE_TIME_EXCESSIVE"></span><dl> <dt>**Response Time Excessive**</dt> <dt>45</dt> </dl>                                                                             |                                     |
| <span id="Retransmission_Rate_Excessive"></span><span id="retransmission_rate_excessive"></span><span id="RETRANSMISSION_RATE_EXCESSIVE"></span><dl> <dt>**Retransmission Rate Excessive**</dt> <dt>46</dt> </dl>                                                     |                                     |
| <span id="Software_Error"></span><span id="software_error"></span><span id="SOFTWARE_ERROR"></span><dl> <dt>**Software Error**</dt> <dt>47</dt> </dl>                                                                                                                 |                                     |
| <span id="Software_Program_Abnormally_Terminated"></span><span id="software_program_abnormally_terminated"></span><span id="SOFTWARE_PROGRAM_ABNORMALLY_TERMINATED"></span><dl> <dt>**Software Program Abnormally Terminated**</dt> <dt>48</dt> </dl>                 |                                     |
| <span id="Software_Program_Error__Incorrect_Results_"></span><span id="software_program_error__incorrect_results_"></span><span id="SOFTWARE_PROGRAM_ERROR__INCORRECT_RESULTS_"></span><dl> <dt>**Software Program Error (Incorrect Results)**</dt> <dt>49</dt> </dl> |                                     |
| <span id="Storage_Capacity_Problem"></span><span id="storage_capacity_problem"></span><span id="STORAGE_CAPACITY_PROBLEM"></span><dl> <dt>**Storage Capacity Problem**</dt> <dt>50</dt> </dl>                                                                         |                                     |
| <span id="Temperature_Unacceptable"></span><span id="temperature_unacceptable"></span><span id="TEMPERATURE_UNACCEPTABLE"></span><dl> <dt>**Temperature Unacceptable**</dt> <dt>51</dt> </dl>                                                                         |                                     |
| <span id="Threshold_Crossed"></span><span id="threshold_crossed"></span><span id="THRESHOLD_CROSSED"></span><dl> <dt>**Threshold Crossed**</dt> <dt>52</dt> </dl>                                                                                                     |                                     |
| <span id="Timing_Problem"></span><span id="timing_problem"></span><span id="TIMING_PROBLEM"></span><dl> <dt>**Timing Problem**</dt> <dt>53</dt> </dl>                                                                                                                 |                                     |
| <span id="Toxic_Leak_Detected"></span><span id="toxic_leak_detected"></span><span id="TOXIC_LEAK_DETECTED"></span><dl> <dt>**Toxic Leak Detected**</dt> <dt>54</dt> </dl>                                                                                             |                                     |
| <span id="Transmit_Failure"></span><span id="transmit_failure"></span><span id="TRANSMIT_FAILURE"></span><dl> <dt>**Transmit Failure**</dt> <dt>55</dt> </dl>                                                                                                         |                                     |
| <span id="Transmitter_Failure"></span><span id="transmitter_failure"></span><span id="TRANSMITTER_FAILURE"></span><dl> <dt>**Transmitter Failure**</dt> <dt>56</dt> </dl>                                                                                             |                                     |
| <span id="Underlying_Resource_Unavailable"></span><span id="underlying_resource_unavailable"></span><span id="UNDERLYING_RESOURCE_UNAVAILABLE"></span><dl> <dt>**Underlying Resource Unavailable**</dt> <dt>57</dt> </dl>                                             |                                     |
| <span id="Version_Mismatch"></span><span id="version_mismatch"></span><span id="VERSION_MISMATCH"></span><dl> <dt>**Version Mismatch**</dt> <dt>58</dt> </dl>                                                                                                         |                                     |
| <span id="Previous_Alert_Cleared"></span><span id="previous_alert_cleared"></span><span id="PREVIOUS_ALERT_CLEARED"></span><dl> <dt>**Previous Alert Cleared**</dt> <dt>59</dt> </dl>                                                                                 |                                     |
| <span id="Login_Attempts_Failed"></span><span id="login_attempts_failed"></span><span id="LOGIN_ATTEMPTS_FAILED"></span><dl> <dt>**Login Attempts Failed**</dt> <dt>60</dt> </dl>                                                                                     |                                     |
| <span id="Software_Virus_Detected"></span><span id="software_virus_detected"></span><span id="SOFTWARE_VIRUS_DETECTED"></span><dl> <dt>**Software Virus Detected**</dt> <dt>61</dt> </dl>                                                                             |                                     |
| <span id="Hardware_Security_Breached"></span><span id="hardware_security_breached"></span><span id="HARDWARE_SECURITY_BREACHED"></span><dl> <dt>**Hardware Security Breached**</dt> <dt>62</dt> </dl>                                                                 |                                     |
| <span id="Denial_of_Service_Detected"></span><span id="denial_of_service_detected"></span><span id="DENIAL_OF_SERVICE_DETECTED"></span><dl> <dt>**Denial of Service Detected**</dt> <dt>63</dt> </dl>                                                                 |                                     |
| <span id="Security_Credential_Mismatch"></span><span id="security_credential_mismatch"></span><span id="SECURITY_CREDENTIAL_MISMATCH"></span><dl> <dt>**Security Credential Mismatch**</dt> <dt>64</dt> </dl>                                                         |                                     |
| <span id="Unauthorized_Access"></span><span id="unauthorized_access"></span><span id="UNAUTHORIZED_ACCESS"></span><dl> <dt>**Unauthorized Access**</dt> <dt>65</dt> </dl>                                                                                             |                                     |
| <span id="Alarm_Received"></span><span id="alarm_received"></span><span id="ALARM_RECEIVED"></span><dl> <dt>**Alarm Received**</dt> <dt>66</dt> </dl>                                                                                                                 |                                     |
| <span id="Loss_of_Pointer"></span><span id="loss_of_pointer"></span><span id="LOSS_OF_POINTER"></span><dl> <dt>**Loss of Pointer**</dt> <dt>67</dt> </dl>                                                                                                             |                                     |
| <span id="Payload_Mismatch"></span><span id="payload_mismatch"></span><span id="PAYLOAD_MISMATCH"></span><dl> <dt>**Payload Mismatch**</dt> <dt>68</dt> </dl>                                                                                                         |                                     |
| <span id="Transmission_Error"></span><span id="transmission_error"></span><span id="TRANSMISSION_ERROR"></span><dl> <dt>**Transmission Error**</dt> <dt>69</dt> </dl>                                                                                                 |                                     |
| <span id="Excessive_Error_Rate"></span><span id="excessive_error_rate"></span><span id="EXCESSIVE_ERROR_RATE"></span><dl> <dt>**Excessive Error Rate**</dt> <dt>70</dt> </dl>                                                                                         |                                     |
| <span id="Trace_Problem"></span><span id="trace_problem"></span><span id="TRACE_PROBLEM"></span><dl> <dt>**Trace Problem**</dt> <dt>71</dt> </dl>                                                                                                                     |                                     |
| <span id="Element_Unavailable"></span><span id="element_unavailable"></span><span id="ELEMENT_UNAVAILABLE"></span><dl> <dt>**Element Unavailable**</dt> <dt>72</dt> </dl>                                                                                             |                                     |
| <span id="Element_Missing"></span><span id="element_missing"></span><span id="ELEMENT_MISSING"></span><dl> <dt>**Element Missing**</dt> <dt>73</dt> </dl>                                                                                                             |                                     |
| <span id="Loss_of_Multi_Frame"></span><span id="loss_of_multi_frame"></span><span id="LOSS_OF_MULTI_FRAME"></span><dl> <dt>**Loss of Multi Frame**</dt> <dt>74</dt> </dl>                                                                                             |                                     |
| <span id="Broadcast_Channel_Failure"></span><span id="broadcast_channel_failure"></span><span id="BROADCAST_CHANNEL_FAILURE"></span><dl> <dt>**Broadcast Channel Failure**</dt> <dt>75</dt> </dl>                                                                     |                                     |
| <span id="Invalid_Message_Received"></span><span id="invalid_message_received"></span><span id="INVALID_MESSAGE_RECEIVED"></span><dl> <dt>**Invalid Message Received**</dt> <dt>76</dt> </dl>                                                                         |                                     |
| <span id="Routing_Failure"></span><span id="routing_failure"></span><span id="ROUTING_FAILURE"></span><dl> <dt>**Routing Failure**</dt> <dt>77</dt> </dl>                                                                                                             |                                     |
| <span id="Backplane_Failure"></span><span id="backplane_failure"></span><span id="BACKPLANE_FAILURE"></span><dl> <dt>**Backplane Failure**</dt> <dt>78</dt> </dl>                                                                                                     |                                     |
| <span id="Identifier_Duplication"></span><span id="identifier_duplication"></span><span id="IDENTIFIER_DUPLICATION"></span><dl> <dt>**Identifier Duplication**</dt> <dt>79</dt> </dl>                                                                                 |                                     |
| <span id="Protection_Path_Failure"></span><span id="protection_path_failure"></span><span id="PROTECTION_PATH_FAILURE"></span><dl> <dt>**Protection Path Failure**</dt> <dt>80</dt> </dl>                                                                             |                                     |
| <span id="Sync_Loss_or_Mismatch"></span><span id="sync_loss_or_mismatch"></span><span id="SYNC_LOSS_OR_MISMATCH"></span><dl> <dt>**Sync Loss or Mismatch**</dt> <dt>81</dt> </dl>                                                                                     |                                     |
| <span id="Terminal_Problem"></span><span id="terminal_problem"></span><span id="TERMINAL_PROBLEM"></span><dl> <dt>**Terminal Problem**</dt> <dt>82</dt> </dl>                                                                                                         |                                     |
| <span id="Real_Time_Clock_Failure"></span><span id="real_time_clock_failure"></span><span id="REAL_TIME_CLOCK_FAILURE"></span><dl> <dt>**Real Time Clock Failure**</dt> <dt>83</dt> </dl>                                                                             |                                     |
| <span id="Antenna_Failure"></span><span id="antenna_failure"></span><span id="ANTENNA_FAILURE"></span><dl> <dt>**Antenna Failure**</dt> <dt>84</dt> </dl>                                                                                                             |                                     |
| <span id="Battery_Charging_Failure"></span><span id="battery_charging_failure"></span><span id="BATTERY_CHARGING_FAILURE"></span><dl> <dt>**Battery Charging Failure**</dt> <dt>85</dt> </dl>                                                                         |                                     |
| <span id="Disk_Failure"></span><span id="disk_failure"></span><span id="DISK_FAILURE"></span><dl> <dt>**Disk Failure**</dt> <dt>86</dt> </dl>                                                                                                                         |                                     |
| <span id="Frequency_Hopping_Failure"></span><span id="frequency_hopping_failure"></span><span id="FREQUENCY_HOPPING_FAILURE"></span><dl> <dt>**Frequency Hopping Failure**</dt> <dt>87</dt> </dl>                                                                     |                                     |
| <span id="Loss_of_Redundancy"></span><span id="loss_of_redundancy"></span><span id="LOSS_OF_REDUNDANCY"></span><dl> <dt>**Loss of Redundancy**</dt> <dt>88</dt> </dl>                                                                                                 |                                     |
| <span id="Power_Supply_Failure"></span><span id="power_supply_failure"></span><span id="POWER_SUPPLY_FAILURE"></span><dl> <dt>**Power Supply Failure**</dt> <dt>89</dt> </dl>                                                                                         |                                     |
| <span id="Signal_Quality_Problem"></span><span id="signal_quality_problem"></span><span id="SIGNAL_QUALITY_PROBLEM"></span><dl> <dt>**Signal Quality Problem**</dt> <dt>90</dt> </dl>                                                                                 |                                     |
| <span id="Battery_Discharging"></span><span id="battery_discharging"></span><span id="BATTERY_DISCHARGING"></span><dl> <dt>**Battery Discharging**</dt> <dt>91</dt> </dl>                                                                                             |                                     |
| <span id="Battery_Failure"></span><span id="battery_failure"></span><span id="BATTERY_FAILURE"></span><dl> <dt>**Battery Failure**</dt> <dt>92</dt> </dl>                                                                                                             |                                     |
| <span id="Commercial_Power_Problem"></span><span id="commercial_power_problem"></span><span id="COMMERCIAL_POWER_PROBLEM"></span><dl> <dt>**Commercial Power Problem**</dt> <dt>93</dt> </dl>                                                                         |                                     |
| <span id="Fan_Failure"></span><span id="fan_failure"></span><span id="FAN_FAILURE"></span><dl> <dt>**Fan Failure**</dt> <dt>94</dt> </dl>                                                                                                                             |                                     |
| <span id="Engine_Failure"></span><span id="engine_failure"></span><span id="ENGINE_FAILURE"></span><dl> <dt>**Engine Failure**</dt> <dt>95</dt> </dl>                                                                                                                 |                                     |
| <span id="Sensor_Failure"></span><span id="sensor_failure"></span><span id="SENSOR_FAILURE"></span><dl> <dt>**Sensor Failure**</dt> <dt>96</dt> </dl>                                                                                                                 |                                     |
| <span id="Fuse_Failure"></span><span id="fuse_failure"></span><span id="FUSE_FAILURE"></span><dl> <dt>**Fuse Failure**</dt> <dt>97</dt> </dl>                                                                                                                         |                                     |
| <span id="Generator_Failure"></span><span id="generator_failure"></span><span id="GENERATOR_FAILURE"></span><dl> <dt>**Generator Failure**</dt> <dt>98</dt> </dl>                                                                                                     |                                     |
| <span id="Low_Battery"></span><span id="low_battery"></span><span id="LOW_BATTERY"></span><dl> <dt>**Low Battery**</dt> <dt>99</dt> </dl>                                                                                                                             |                                     |
| <span id="Low_Fuel"></span><span id="low_fuel"></span><span id="LOW_FUEL"></span><dl> <dt>**Low Fuel**</dt> <dt>100</dt> </dl>                                                                                                                                        |                                     |
| <span id="Low_Water"></span><span id="low_water"></span><span id="LOW_WATER"></span><dl> <dt>**Low Water**</dt> <dt>101</dt> </dl>                                                                                                                                    |                                     |
| <span id="Explosive_Gas"></span><span id="explosive_gas"></span><span id="EXPLOSIVE_GAS"></span><dl> <dt>**Explosive Gas**</dt> <dt>102</dt> </dl>                                                                                                                    |                                     |
| <span id="High_Winds"></span><span id="high_winds"></span><span id="HIGH_WINDS"></span><dl> <dt>**High Winds**</dt> <dt>103</dt> </dl>                                                                                                                                |                                     |
| <span id="Ice_Buildup"></span><span id="ice_buildup"></span><span id="ICE_BUILDUP"></span><dl> <dt>**Ice Buildup**</dt> <dt>104</dt> </dl>                                                                                                                            |                                     |
| <span id="Smoke"></span><span id="smoke"></span><span id="SMOKE"></span><dl> <dt>**Smoke**</dt> <dt>105</dt> </dl>                                                                                                                                                    |                                     |
| <span id="Memory_Mismatch"></span><span id="memory_mismatch"></span><span id="MEMORY_MISMATCH"></span><dl> <dt>**Memory Mismatch**</dt> <dt>106</dt> </dl>                                                                                                            |                                     |
| <span id="Out_of_CPU_Cycles"></span><span id="out_of_cpu_cycles"></span><span id="OUT_OF_CPU_CYCLES"></span><dl> <dt>**Out of CPU Cycles**</dt> <dt>107</dt> </dl>                                                                                                    |                                     |
| <span id="Software_Environment_Problem"></span><span id="software_environment_problem"></span><span id="SOFTWARE_ENVIRONMENT_PROBLEM"></span><dl> <dt>**Software Environment Problem**</dt> <dt>108</dt> </dl>                                                        |                                     |
| <span id="Software_Download_Failure"></span><span id="software_download_failure"></span><span id="SOFTWARE_DOWNLOAD_FAILURE"></span><dl> <dt>**Software Download Failure**</dt> <dt>109</dt> </dl>                                                                    |                                     |
| <span id="Element_Reinitialized"></span><span id="element_reinitialized"></span><span id="ELEMENT_REINITIALIZED"></span><dl> <dt>**Element Reinitialized**</dt> <dt>110</dt> </dl>                                                                                    |                                     |
| <span id="Timeout"></span><span id="timeout"></span><span id="TIMEOUT"></span><dl> <dt>**Timeout**</dt> <dt>111</dt> </dl>                                                                                                                                            |                                     |
| <span id="Logging_Problems"></span><span id="logging_problems"></span><span id="LOGGING_PROBLEMS"></span><dl> <dt>**Logging Problems**</dt> <dt>112</dt> </dl>                                                                                                        |                                     |
| <span id="Leak_Detected"></span><span id="leak_detected"></span><span id="LEAK_DETECTED"></span><dl> <dt>**Leak Detected**</dt> <dt>113</dt> </dl>                                                                                                                    |                                     |
| <span id="Protection_Mechanism_Failure"></span><span id="protection_mechanism_failure"></span><span id="PROTECTION_MECHANISM_FAILURE"></span><dl> <dt>**Protection Mechanism Failure**</dt> <dt>114</dt> </dl>                                                        |                                     |
| <span id="Protecting_Resource_Failure"></span><span id="protecting_resource_failure"></span><span id="PROTECTING_RESOURCE_FAILURE"></span><dl> <dt>**Protecting Resource Failure**</dt> <dt>115</dt> </dl>                                                            |                                     |
| <span id="Database_Inconsistency"></span><span id="database_inconsistency"></span><span id="DATABASE_INCONSISTENCY"></span><dl> <dt>**Database Inconsistency**</dt> <dt>116</dt> </dl>                                                                                |                                     |
| <span id="Authentication_Failure"></span><span id="authentication_failure"></span><span id="AUTHENTICATION_FAILURE"></span><dl> <dt>**Authentication Failure**</dt> <dt>117</dt> </dl>                                                                                |                                     |
| <span id="Breach_of_Confidentiality"></span><span id="breach_of_confidentiality"></span><span id="BREACH_OF_CONFIDENTIALITY"></span><dl> <dt>**Breach of Confidentiality**</dt> <dt>118</dt> </dl>                                                                    |                                     |
| <span id="Cable_Tamper"></span><span id="cable_tamper"></span><span id="CABLE_TAMPER"></span><dl> <dt>**Cable Tamper**</dt> <dt>119</dt> </dl>                                                                                                                        |                                     |
| <span id="Delayed_Information"></span><span id="delayed_information"></span><span id="DELAYED_INFORMATION"></span><dl> <dt>**Delayed Information**</dt> <dt>120</dt> </dl>                                                                                            |                                     |
| <span id="Duplicate_Information"></span><span id="duplicate_information"></span><span id="DUPLICATE_INFORMATION"></span><dl> <dt>**Duplicate Information**</dt> <dt>121</dt> </dl>                                                                                    |                                     |
| <span id="Information_Missing"></span><span id="information_missing"></span><span id="INFORMATION_MISSING"></span><dl> <dt>**Information Missing**</dt> <dt>122</dt> </dl>                                                                                            |                                     |
| <span id="Information_Modification"></span><span id="information_modification"></span><span id="INFORMATION_MODIFICATION"></span><dl> <dt>**Information Modification**</dt> <dt>123</dt> </dl>                                                                        |                                     |
| <span id="Information_Out_of_Sequence"></span><span id="information_out_of_sequence"></span><span id="INFORMATION_OUT_OF_SEQUENCE"></span><dl> <dt>**Information Out of Sequence**</dt> <dt>124</dt> </dl>                                                            |                                     |
| <span id="Key_Expired"></span><span id="key_expired"></span><span id="KEY_EXPIRED"></span><dl> <dt>**Key Expired**</dt> <dt>125</dt> </dl>                                                                                                                            |                                     |
| <span id="Non-Repudiation_Failure"></span><span id="non-repudiation_failure"></span><span id="NON-REPUDIATION_FAILURE"></span><dl> <dt>**Non-Repudiation Failure**</dt> <dt>126</dt> </dl>                                                                            |                                     |
| <span id="Out_of_Hours_Activity"></span><span id="out_of_hours_activity"></span><span id="OUT_OF_HOURS_ACTIVITY"></span><dl> <dt>**Out of Hours Activity**</dt> <dt>127</dt> </dl>                                                                                    |                                     |
| <span id="Out_of_Service"></span><span id="out_of_service"></span><span id="OUT_OF_SERVICE"></span><dl> <dt>**Out of Service**</dt> <dt>128</dt> </dl>                                                                                                                |                                     |
| <span id="Procedural_Error"></span><span id="procedural_error"></span><span id="PROCEDURAL_ERROR"></span><dl> <dt>**Procedural Error**</dt> <dt>129</dt> </dl>                                                                                                        |                                     |
| <span id="Unexpected_Information"></span><span id="unexpected_information"></span><span id="UNEXPECTED_INFORMATION"></span><dl> <dt>**Unexpected Information**</dt> <dt>130</dt> </dl>                                                                                |                                     |
| <span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span><dl> <dt>**DMTF Reserved**</dt> <dt>131 65535</dt> </dl>                                                                                                              | Reserved for future use.<br/> |



 

</dd> <dt>

**ProbableCauseDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/win32/wmisdk/standard-qualifiers) ("CIM\_Error.ProbableCause")
</dt> </dl>

A free-form string describing the probable cause of the error.

</dd> <dt>

**RecommendedActions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

A free-form string describing recommended actions to take to resolve the error.

</dd> </dl>

## Requirements

| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\standardcimv2<br/>                                                          |
| MOF<br/>                      | <dl> <dt>NetTCPIP.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetTCPIP.dll</dt> </dl> |
