---
description: Contains information about the severity, cause, recommended actions, and other data related to the failure of a CIM Operation.
ms.assetid: 128B9ECE-D26C-4A7D-BFB7-69CD986B0DBA
title: Msvm_Error class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_Error
- Msvm_Error.ErrorType
- Msvm_Error.OtherErrorType
- Msvm_Error.OwningEntity
- Msvm_Error.MessageID
- Msvm_Error.Message
- Msvm_Error.MessageArguments
- Msvm_Error.PerceivedSeverity
- Msvm_Error.ProbableCause
- Msvm_Error.ProbableCauseDescription
- Msvm_Error.RecommendedActions
- Msvm_Error.ErrorSource
- Msvm_Error.ErrorSourceFormat
- Msvm_Error.OtherErrorSourceFormat
- Msvm_Error.CIMStatusCode
- Msvm_Error.CIMStatusCodeDescription
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_Error class

A specialized class that contains information about the severity, cause, recommended actions, and other data related to the failure of a CIM Operation.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_Error : CIM_Error
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

The **Msvm\_Error** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_Error** class has these properties.

<dl> <dt>

**CIMStatusCode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The CIM status code that characterizes this instance. This property defines the status codes that may be return by a conforming CIM Server or Listener. Not all status codes are valid for each operation. The specification for each operation should define the status codes that may be returned by that operation. The following values for CIM status code are defined. This property is inherited from [**CIM\_Error**](/previous-versions//cc150671(v=vs.85)).



| Value                                                                                                                                                                                                                                                                                          | Meaning                                                                                   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| <span id="CIM_ERR_FAILED"></span><span id="cim_err_failed"></span><dl> <dt>**CIM\_ERR\_FAILED**</dt> <dt>1</dt> </dl>                                                                       | A general error occurred that is not covered by a more specific error code.<br/>    |
| <span id="CIM_ERR_ACCESS_DENIED"></span><span id="cim_err_access_denied"></span><dl> <dt>**CIM\_ERR\_ACCESS\_DENIED**</dt> <dt>2</dt> </dl>                                                 | Access to a CIM resource was not available to the client.<br/>                      |
| <span id="CIM_ERR_INVALID_NAMESPACE"></span><span id="cim_err_invalid_namespace"></span><dl> <dt>**CIM\_ERR\_INVALID\_NAMESPACE**</dt> <dt>3</dt> </dl>                                     | The target namespace does not exist.<br/>                                           |
| <span id="CIM_ERR_INVALID_PARAMETER"></span><span id="cim_err_invalid_parameter"></span><dl> <dt>**CIM\_ERR\_INVALID\_PARAMETER**</dt> <dt>4</dt> </dl>                                     | One or more parameter values passed to the method were invalid.<br/>                |
| <span id="CIM_ERR_INVALID_CLASS"></span><span id="cim_err_invalid_class"></span><dl> <dt>**CIM\_ERR\_INVALID\_CLASS**</dt> <dt>5</dt> </dl>                                                 | The specified class does not exist.<br/>                                            |
| <span id="CIM_ERR_NOT_FOUND"></span><span id="cim_err_not_found"></span><dl> <dt>**CIM\_ERR\_NOT\_FOUND**</dt> <dt>6</dt> </dl>                                                             | The requested object could not be found.<br/>                                       |
| <span id="CIM_ERR_NOT_SUPPORTED"></span><span id="cim_err_not_supported"></span><dl> <dt>**CIM\_ERR\_NOT\_SUPPORTED**</dt> <dt>7</dt> </dl>                                                 | The requested operation is not supported.<br/>                                      |
| <span id="CIM_ERR_CLASS_HAS_CHILDREN"></span><span id="cim_err_class_has_children"></span><dl> <dt>**CIM\_ERR\_CLASS\_HAS\_CHILDREN**</dt> <dt>8</dt> </dl>                                 | Operation cannot be carried out on this class because it has instances.<br/>        |
| <span id="CIM_ERR_CLASS_HAS_INSTANCES"></span><span id="cim_err_class_has_instances"></span><dl> <dt>**CIM\_ERR\_CLASS\_HAS\_INSTANCES**</dt> <dt>9</dt> </dl>                              | Operation cannot be carried out on this class since it has instances.<br/>          |
| <span id="CIM_ERR_INVALID_SUPERCLASS"></span><span id="cim_err_invalid_superclass"></span><dl> <dt>**CIM\_ERR\_INVALID\_SUPERCLASS**</dt> <dt>10</dt> </dl>                                 | Operation cannot be carried out since the specified superclass does not exist.<br/> |
| <span id="CIM_ERR_ALREADY_EXISTS"></span><span id="cim_err_already_exists"></span><dl> <dt>**CIM\_ERR\_ALREADY\_EXISTS**</dt> <dt>11</dt> </dl>                                             | Operation cannot be carried out because an object already exists.<br/>              |
| <span id="CIM_ERR_NO_SUCH_PROPERTY"></span><span id="cim_err_no_such_property"></span><dl> <dt>**CIM\_ERR\_NO\_SUCH\_PROPERTY**</dt> <dt>12</dt> </dl>                                      | The specified Property does not exist.<br/>                                         |
| <span id="CIM_ERR_TYPE_MISMATCH"></span><span id="cim_err_type_mismatch"></span><dl> <dt>**CIM\_ERR\_TYPE\_MISMATCH**</dt> <dt>13</dt> </dl>                                                | The value supplied is incompatible with the type.<br/>                              |
| <span id="CIM_ERR_QUERY_LANGUAGE_NOT_SUPPORTED"></span><span id="cim_err_query_language_not_supported"></span><dl> <dt>**CIM\_ERR\_QUERY\_LANGUAGE\_NOT\_SUPPORTED**</dt> <dt>14</dt> </dl> | The query language is not recognized or supported.<br/>                             |
| <span id="CIM_ERR_INVALID_QUERY"></span><span id="cim_err_invalid_query"></span><dl> <dt>**CIM\_ERR\_INVALID\_QUERY**</dt> <dt>15</dt> </dl>                                                | The query is not valid for the specified query language.<br/>                       |
| <span id="CIM_ERR_METHOD_NOT_AVAILABLE"></span><span id="cim_err_method_not_available"></span><dl> <dt>**CIM\_ERR\_METHOD\_NOT\_AVAILABLE**</dt> <dt>16</dt> </dl>                          | The extrinsic method could not be executed.<br/>                                    |
| <span id="CIM_ERR_METHOD_NOT_FOUND"></span><span id="cim_err_method_not_found"></span><dl> <dt>**CIM\_ERR\_METHOD\_NOT\_FOUND**</dt> <dt>17</dt> </dl>                                      | The specified extrinsic method does not exist.<br/>                                 |
| <span id="CIM_ERR_UNEXPECTED_RESPONSE"></span><span id="cim_err_unexpected_response"></span><dl> <dt>**CIM\_ERR\_UNEXPECTED\_RESPONSE**</dt> <dt>18</dt> </dl>                              | The returned response to the asynchronous operation was not expected.<br/>          |
| <span id="CIM_ERR_INVALID_RESPONSE_DESTINATION"></span><span id="cim_err_invalid_response_destination"></span><dl> <dt>**CIM\_ERR\_INVALID\_RESPONSE\_DESTINATION**</dt> <dt>19</dt> </dl>  | The specified destination for the asynchronous response is not valid.<br/>          |
| <span id="CIM_ERR_NAMESPACE_NOT_EMPTY"></span><span id="cim_err_namespace_not_empty"></span><dl> <dt>**CIM\_ERR\_NAMESPACE\_NOT\_EMPTY**</dt> <dt>20</dt> </dl>                             | The specified namespace is not empty.<br/>                                          |
| <span id="DMTF_Reserved_"></span><span id="dmtf_reserved_"></span><span id="DMTF_RESERVED_"></span><dl> <dt>**DMTF Reserved** </dt> <dt>21 = *value* </dt> </dl>                            | Reserved values.<br/>                                                               |



 

</dd> <dt>

**CIMStatusCodeDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string containing a user-readable description of the **CIMStatusCode** property. This description may extend, but must be consistent with, the definition of **CIMStatusCode**. This property is inherited from [**CIM\_Error**](/previous-versions//cc150671(v=vs.85)).

</dd> <dt>

**ErrorSource**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The identifying information of the entity (the instance) generating the error. If this entity is modeled in the CIM Schema, this property contains the path of the instance encoded as a string parameter. If not modeled, the property contains some identifying string that names the entity that generated the error. The path or identifying string is formatted per the **ErrorSourceFormat** property. This property is inherited from [**CIM\_Error**](/previous-versions//cc150671(v=vs.85)).

</dd> <dt>

**ErrorSourceFormat**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The format of the **ErrorSource** property is interpretable based on the value of this property. This property is inherited from [**CIM\_Error**](/previous-versions//cc150671(v=vs.85)), and it is always set to 0.



| Value                                                                                                                                                                                                                                                        | Meaning                                                                                                                                 |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>0</dt> </dl>                                  | The format is unknown or not meaningfully interpretable by a CIM client application.<br/>                                         |
| <span id="Other"></span><span id="other"></span><span id="OTHER"></span><dl> <dt>**Other**</dt> <dt>1</dt> </dl>                                          | The format is defined by the value of the **OtherErrorSourceFormat** property.<br/>                                               |
| <span id="CIMObjectHandle"></span><span id="cimobjecthandle"></span><span id="CIMOBJECTHANDLE"></span><dl> <dt>**CIMObjectHandle**</dt> <dt>2 </dt> </dl> | A CIM Object Handle, encoded using the MOF syntax defined for the objectHandle non-terminal, is used to identify the entity.<br/> |



 

</dd> <dt>

**ErrorType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Primary classification of the error. The following values are defined. This property is inherited from [**CIM\_Error**](/previous-versions//cc150671(v=vs.85)).



| Value                                                                                                                                                                                                                                                                                                         | Meaning                                                                                                                                                  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>0</dt> </dl>                                                                                   |                                                                                                                                                          |
| <span id="Other"></span><span id="other"></span><span id="OTHER"></span><dl> <dt>**Other**</dt> <dt>1</dt> </dl>                                                                                           |                                                                                                                                                          |
| <span id="Communications_Error"></span><span id="communications_error"></span><span id="COMMUNICATIONS_ERROR"></span><dl> <dt>**Communications Error**</dt> <dt>2</dt> </dl>                               | Errors of this type are principally associated with the procedures and/or processes required to convey information from one point to another.<br/> |
| <span id="Quality_of_Service_Error"></span><span id="quality_of_service_error"></span><span id="QUALITY_OF_SERVICE_ERROR"></span><dl> <dt>**Quality of Service Error**</dt> <dt>3</dt> </dl>               | Errors of this type are principally associated with failures that result in reduced functionality or performance.<br/>                             |
| <span id="Software_Error"></span><span id="software_error"></span><span id="SOFTWARE_ERROR"></span><dl> <dt>**Software Error**</dt> <dt>4</dt> </dl>                                                       | Error of this type are principally associated with a software or processing fault.<br/>                                                            |
| <span id="Hardware_Error"></span><span id="hardware_error"></span><span id="HARDWARE_ERROR"></span><dl> <dt>**Hardware Error**</dt> <dt>5</dt> </dl>                                                       | Errors of this type are principally associated with an equipment or hardware failure.<br/>                                                         |
| <span id="Environmental_Error"></span><span id="environmental_error"></span><span id="ENVIRONMENTAL_ERROR"></span><dl> <dt>**Environmental Error**</dt> <dt>6</dt> </dl>                                   | Errors of this type are principally associated with a failure condition relating to the facility, or other environmental considerations.<br/>      |
| <span id="Security_Error"></span><span id="security_error"></span><span id="SECURITY_ERROR"></span><dl> <dt>**Security Error**</dt> <dt>7</dt> </dl>                                                       | Errors of this type are associated with security violations, detection of viruses, and similar issues.<br/>                                        |
| <span id="Oversubscription_Error"></span><span id="oversubscription_error"></span><span id="OVERSUBSCRIPTION_ERROR"></span><dl> <dt>**Oversubscription Error**</dt> <dt>8</dt> </dl>                       | Errors of this type are principally associated with the failure to allocate sufficient resources to complete the operation.<br/>                   |
| <span id="Unavailable_Resource_Error"></span><span id="unavailable_resource_error"></span><span id="UNAVAILABLE_RESOURCE_ERROR"></span><dl> <dt>**Unavailable Resource Error**</dt> <dt>9</dt> </dl>       | Errors of this type are principally associated with the failure to access a required resource.<br/>                                                |
| <span id="Unsupported_Operation_Error"></span><span id="unsupported_operation_error"></span><span id="UNSUPPORTED_OPERATION_ERROR"></span><dl> <dt>**Unsupported Operation Error**</dt> <dt>10 </dt> </dl> | Errors of this type are principally associated with requests that are not supported.<br/>                                                          |



 

</dd> <dt>

**Message**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The formatted message. This message is constructed by applying the dynamic content of the message, described in **MessageArguments**, to the format string uniquely identified, within the scope of the **OwningEntity**, by **MessageID**. This property is inherited from [**CIM\_Error**](/previous-versions//cc150671(v=vs.85)).

</dd> <dt>

**MessageArguments**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array containing the dynamic content of the message. This property is inherited from [**CIM\_Error**](/previous-versions//cc150671(v=vs.85)).

</dd> <dt>

**MessageID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

An opaque string that uniquely identifies, within the scope of the **OwningEntity**, the format of the message. This property is inherited from [**CIM\_Error**](/previous-versions//cc150671(v=vs.85)).

</dd> <dt>

**OtherErrorSourceFormat**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string defining "Other" values for **ErrorSourceFormat**. This value must be set to a non-NULL value when **ErrorSourceFormat** is set to a value of 1 (Other). For all other values of **ErrorSourceFormat**, the value of this string must be set to **Null**. This property is inherited from [**CIM\_Error**](/previous-versions//cc150671(v=vs.85)).

</dd> <dt>

**OtherErrorType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string that describes the **ErrorType** when 1, (Other), is specified as the **ErrorType**. This property is inherited from [**CIM\_Error**](/previous-versions//cc150671(v=vs.85)).

</dd> <dt>

**OwningEntity**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string that uniquely identifies the entity that owns the definition of the format of the message described in this instance. **OwningEntity** must include a copyrighted, trademarked, or otherwise unique name that is owned by the business entity or standards body defining the format. This property is inherited from [**CIM\_Error**](/previous-versions//cc150671(v=vs.85)).

</dd> <dt>

**PerceivedSeverity**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

An enumerated value that describes the severity of the error from the notifier's point of view: 2 - Low should be used for noncritical issues such as invalid parameters, incorrect usage, unsupported functionality. 3 - Medium should be used to indicate action is needed, but the situation is not serious at this time. 4 - High should be used to indicate action is needed now. 5 - Fatal should be used to indicate a loss of data or unrecoverable system or service failure. This property is inherited from [**CIM\_Error**](/previous-versions//cc150671(v=vs.85)).

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Low"></span><span id="low"></span><span id="LOW"></span>**Low** (2)
</dt> <dt>

<span id="Medium"></span><span id="medium"></span><span id="MEDIUM"></span>**Medium** (3)
</dt> <dt>

<span id="High"></span><span id="high"></span><span id="HIGH"></span>**High** (4)
</dt> <dt>

<span id="Fatal_"></span><span id="fatal_"></span><span id="FATAL_"></span>**Fatal** (5 )
</dt> </dl>

</dd> <dt>

**ProbableCause**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

An enumerated value that describes the probable cause of the error. This property is inherited from [**CIM\_Error**](/previous-versions//cc150671(v=vs.85)).

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)
</dt> <dt>

<span id="Adapter_Card_Error"></span><span id="adapter_card_error"></span><span id="ADAPTER_CARD_ERROR"></span>**Adapter/Card Error** (2)
</dt> <dt>

<span id="Application_Subsystem_Failure"></span><span id="application_subsystem_failure"></span><span id="APPLICATION_SUBSYSTEM_FAILURE"></span>**Application Subsystem Failure** (3)
</dt> <dt>

<span id="Bandwidth_Reduced"></span><span id="bandwidth_reduced"></span><span id="BANDWIDTH_REDUCED"></span>**Bandwidth Reduced** (4)
</dt> <dt>

<span id="Connection_Establishment_Error"></span><span id="connection_establishment_error"></span><span id="CONNECTION_ESTABLISHMENT_ERROR"></span>**Connection Establishment Error** (5)
</dt> <dt>

<span id="Communications_Protocol_Error"></span><span id="communications_protocol_error"></span><span id="COMMUNICATIONS_PROTOCOL_ERROR"></span>**Communications Protocol Error** (6)
</dt> <dt>

<span id="Communications_Subsystem_Failure"></span><span id="communications_subsystem_failure"></span><span id="COMMUNICATIONS_SUBSYSTEM_FAILURE"></span>**Communications Subsystem Failure** (7)
</dt> <dt>

<span id="Configuration_Customization_Error"></span><span id="configuration_customization_error"></span><span id="CONFIGURATION_CUSTOMIZATION_ERROR"></span>**Configuration/Customization Error** (8)
</dt> <dt>

<span id="Congestion"></span><span id="congestion"></span><span id="CONGESTION"></span>**Congestion** (9)
</dt> <dt>

<span id="Corrupt_Data"></span><span id="corrupt_data"></span><span id="CORRUPT_DATA"></span>**Corrupt Data** (10)
</dt> <dt>

<span id="CPU_Cycles_Limit_Exceeded"></span><span id="cpu_cycles_limit_exceeded"></span><span id="CPU_CYCLES_LIMIT_EXCEEDED"></span>**CPU Cycles Limit Exceeded** (11)
</dt> <dt>

<span id="Dataset_Modem_Error"></span><span id="dataset_modem_error"></span><span id="DATASET_MODEM_ERROR"></span>**Dataset/Modem Error** (12)
</dt> <dt>

<span id="Degraded_Signal"></span><span id="degraded_signal"></span><span id="DEGRADED_SIGNAL"></span>**Degraded Signal** (13)
</dt> <dt>

<span id="DTE-DCE_Interface_Error"></span><span id="dte-dce_interface_error"></span><span id="DTE-DCE_INTERFACE_ERROR"></span>**DTE-DCE Interface Error** (14)
</dt> <dt>

<span id="Enclosure_Door_Open"></span><span id="enclosure_door_open"></span><span id="ENCLOSURE_DOOR_OPEN"></span>**Enclosure Door Open** (15)
</dt> <dt>

<span id="Equipment_Malfunction"></span><span id="equipment_malfunction"></span><span id="EQUIPMENT_MALFUNCTION"></span>**Equipment Malfunction** (16)
</dt> <dt>

<span id="Excessive_Vibration"></span><span id="excessive_vibration"></span><span id="EXCESSIVE_VIBRATION"></span>**Excessive Vibration** (17)
</dt> <dt>

<span id="File_Format_Error"></span><span id="file_format_error"></span><span id="FILE_FORMAT_ERROR"></span>**File Format Error** (18)
</dt> <dt>

<span id="Fire_Detected"></span><span id="fire_detected"></span><span id="FIRE_DETECTED"></span>**Fire Detected** (19)
</dt> <dt>

<span id="Flood_Detected"></span><span id="flood_detected"></span><span id="FLOOD_DETECTED"></span>**Flood Detected** (20)
</dt> <dt>

<span id="Framing_Error"></span><span id="framing_error"></span><span id="FRAMING_ERROR"></span>**Framing Error** (21)
</dt> <dt>

<span id="HVAC_Problem"></span><span id="hvac_problem"></span><span id="HVAC_PROBLEM"></span>**HVAC Problem** (22)
</dt> <dt>

<span id="Humidity_Unacceptable"></span><span id="humidity_unacceptable"></span><span id="HUMIDITY_UNACCEPTABLE"></span>**Humidity Unacceptable** (23)
</dt> <dt>

<span id="I_O_Device_Error"></span><span id="i_o_device_error"></span><span id="I_O_DEVICE_ERROR"></span>**I/O Device Error** (24)
</dt> <dt>

<span id="Input_Device_Error"></span><span id="input_device_error"></span><span id="INPUT_DEVICE_ERROR"></span>**Input Device Error** (25)
</dt> <dt>

<span id="LAN_Error"></span><span id="lan_error"></span><span id="LAN_ERROR"></span>**LAN Error** (26)
</dt> <dt>

<span id="Non-Toxic_Leak_Detected"></span><span id="non-toxic_leak_detected"></span><span id="NON-TOXIC_LEAK_DETECTED"></span>**Non-Toxic Leak Detected** (27)
</dt> <dt>

<span id="Local_Node_Transmission_Error"></span><span id="local_node_transmission_error"></span><span id="LOCAL_NODE_TRANSMISSION_ERROR"></span>**Local Node Transmission Error** (28)
</dt> <dt>

<span id="Loss_of_Frame"></span><span id="loss_of_frame"></span><span id="LOSS_OF_FRAME"></span>**Loss of Frame** (29)
</dt> <dt>

<span id="Loss_of_Signal"></span><span id="loss_of_signal"></span><span id="LOSS_OF_SIGNAL"></span>**Loss of Signal** (30)
</dt> <dt>

<span id="__31____________Material_Supply_Exhausted"></span><span id="__31____________material_supply_exhausted"></span><span id="__31____________MATERIAL_SUPPLY_EXHAUSTED"></span>**//31 Material Supply Exhausted** (31)
</dt> <dt>

<span id="Multiplexer_Problem"></span><span id="multiplexer_problem"></span><span id="MULTIPLEXER_PROBLEM"></span>**Multiplexer Problem** (32)
</dt> <dt>

<span id="Out_of_Memory"></span><span id="out_of_memory"></span><span id="OUT_OF_MEMORY"></span>**Out of Memory** (33)
</dt> <dt>

<span id="Output_Device_Error"></span><span id="output_device_error"></span><span id="OUTPUT_DEVICE_ERROR"></span>**Output Device Error** (34)
</dt> <dt>

<span id="Performance_Degraded"></span><span id="performance_degraded"></span><span id="PERFORMANCE_DEGRADED"></span>**Performance Degraded** (35)
</dt> <dt>

<span id="Power_Problem"></span><span id="power_problem"></span><span id="POWER_PROBLEM"></span>**Power Problem** (36)
</dt> <dt>

<span id="Pressure_Unacceptable"></span><span id="pressure_unacceptable"></span><span id="PRESSURE_UNACCEPTABLE"></span>**Pressure Unacceptable** (37)
</dt> <dt>

<span id="Processor_Problem__Internal_Machine_Error_"></span><span id="processor_problem__internal_machine_error_"></span><span id="PROCESSOR_PROBLEM__INTERNAL_MACHINE_ERROR_"></span>**Processor Problem (Internal Machine Error)** (38)
</dt> <dt>

<span id="Pump_Failure"></span><span id="pump_failure"></span><span id="PUMP_FAILURE"></span>**Pump Failure** (39)
</dt> <dt>

<span id="Queue_Size_Exceeded"></span><span id="queue_size_exceeded"></span><span id="QUEUE_SIZE_EXCEEDED"></span>**Queue Size Exceeded** (40)
</dt> <dt>

<span id="Receive_Failure"></span><span id="receive_failure"></span><span id="RECEIVE_FAILURE"></span>**Receive Failure** (41)
</dt> <dt>

<span id="Receiver_Failure"></span><span id="receiver_failure"></span><span id="RECEIVER_FAILURE"></span>**Receiver Failure** (42)
</dt> <dt>

<span id="Remote_Node_Transmission_Error"></span><span id="remote_node_transmission_error"></span><span id="REMOTE_NODE_TRANSMISSION_ERROR"></span>**Remote Node Transmission Error** (43)
</dt> <dt>

<span id="Resource_at_or_Nearing_Capacity"></span><span id="resource_at_or_nearing_capacity"></span><span id="RESOURCE_AT_OR_NEARING_CAPACITY"></span>**Resource at or Nearing Capacity** (44)
</dt> <dt>

<span id="Response_Time_Excessive"></span><span id="response_time_excessive"></span><span id="RESPONSE_TIME_EXCESSIVE"></span>**Response Time Excessive** (45)
</dt> <dt>

<span id="Retransmission_Rate_Excessive"></span><span id="retransmission_rate_excessive"></span><span id="RETRANSMISSION_RATE_EXCESSIVE"></span>**Retransmission Rate Excessive** (46)
</dt> <dt>

<span id="Software_Error"></span><span id="software_error"></span><span id="SOFTWARE_ERROR"></span>**Software Error** (47)
</dt> <dt>

<span id="Software_Program_Abnormally_Terminated"></span><span id="software_program_abnormally_terminated"></span><span id="SOFTWARE_PROGRAM_ABNORMALLY_TERMINATED"></span>**Software Program Abnormally Terminated** (48)
</dt> <dt>

<span id="Software_Program_Error__Incorrect_Results_"></span><span id="software_program_error__incorrect_results_"></span><span id="SOFTWARE_PROGRAM_ERROR__INCORRECT_RESULTS_"></span>**Software Program Error (Incorrect Results)** (49)
</dt> <dt>

<span id="Storage_Capacity_Problem"></span><span id="storage_capacity_problem"></span><span id="STORAGE_CAPACITY_PROBLEM"></span>**Storage Capacity Problem** (50)
</dt> <dt>

<span id="Temperature_Unacceptable"></span><span id="temperature_unacceptable"></span><span id="TEMPERATURE_UNACCEPTABLE"></span>**Temperature Unacceptable** (51)
</dt> <dt>

<span id="Threshold_Crossed"></span><span id="threshold_crossed"></span><span id="THRESHOLD_CROSSED"></span>**Threshold Crossed** (52)
</dt> <dt>

<span id="Timing_Problem"></span><span id="timing_problem"></span><span id="TIMING_PROBLEM"></span>**Timing Problem** (53)
</dt> <dt>

<span id="Toxic_Leak_Detected"></span><span id="toxic_leak_detected"></span><span id="TOXIC_LEAK_DETECTED"></span>**Toxic Leak Detected** (54)
</dt> <dt>

<span id="Transmit_Failure"></span><span id="transmit_failure"></span><span id="TRANSMIT_FAILURE"></span>**Transmit Failure** (55)
</dt> <dt>

<span id="Transmitter_Failure"></span><span id="transmitter_failure"></span><span id="TRANSMITTER_FAILURE"></span>**Transmitter Failure** (56)
</dt> <dt>

<span id="Underlying_Resource_Unavailable"></span><span id="underlying_resource_unavailable"></span><span id="UNDERLYING_RESOURCE_UNAVAILABLE"></span>**Underlying Resource Unavailable** (57)
</dt> <dt>

<span id="Version_Mismatch"></span><span id="version_mismatch"></span><span id="VERSION_MISMATCH"></span>**Version Mismatch** (58)
</dt> <dt>

<span id="Previous_Alert_Cleared"></span><span id="previous_alert_cleared"></span><span id="PREVIOUS_ALERT_CLEARED"></span>**Previous Alert Cleared** (59)
</dt> <dt>

<span id="__60____________Login_Attempts_Failed"></span><span id="__60____________login_attempts_failed"></span><span id="__60____________LOGIN_ATTEMPTS_FAILED"></span>**//60 Login Attempts Failed** (60)
</dt> <dt>

<span id="Software_Virus_Detected"></span><span id="software_virus_detected"></span><span id="SOFTWARE_VIRUS_DETECTED"></span>**Software Virus Detected** (61)
</dt> <dt>

<span id="Hardware_Security_Breached"></span><span id="hardware_security_breached"></span><span id="HARDWARE_SECURITY_BREACHED"></span>**Hardware Security Breached** (62)
</dt> <dt>

<span id="Denial_of_Service_Detected"></span><span id="denial_of_service_detected"></span><span id="DENIAL_OF_SERVICE_DETECTED"></span>**Denial of Service Detected** (63)
</dt> <dt>

<span id="Security_Credential_Mismatch"></span><span id="security_credential_mismatch"></span><span id="SECURITY_CREDENTIAL_MISMATCH"></span>**Security Credential Mismatch** (64)
</dt> <dt>

<span id="Unauthorized_Access"></span><span id="unauthorized_access"></span><span id="UNAUTHORIZED_ACCESS"></span>**Unauthorized Access** (65)
</dt> <dt>

<span id="Alarm_Received"></span><span id="alarm_received"></span><span id="ALARM_RECEIVED"></span>**Alarm Received** (66)
</dt> <dt>

<span id="Loss_of_Pointer"></span><span id="loss_of_pointer"></span><span id="LOSS_OF_POINTER"></span>**Loss of Pointer** (67)
</dt> <dt>

<span id="Payload_Mismatch"></span><span id="payload_mismatch"></span><span id="PAYLOAD_MISMATCH"></span>**Payload Mismatch** (68)
</dt> <dt>

<span id="Transmission_Error"></span><span id="transmission_error"></span><span id="TRANSMISSION_ERROR"></span>**Transmission Error** (69)
</dt> <dt>

<span id="Excessive_Error_Rate"></span><span id="excessive_error_rate"></span><span id="EXCESSIVE_ERROR_RATE"></span>**Excessive Error Rate** (70)
</dt> <dt>

<span id="Trace_Problem"></span><span id="trace_problem"></span><span id="TRACE_PROBLEM"></span>**Trace Problem** (71)
</dt> <dt>

<span id="Element_Unavailable"></span><span id="element_unavailable"></span><span id="ELEMENT_UNAVAILABLE"></span>**Element Unavailable** (72)
</dt> <dt>

<span id="Element_Missing"></span><span id="element_missing"></span><span id="ELEMENT_MISSING"></span>**Element Missing** (73)
</dt> <dt>

<span id="Loss_of_Multi_Frame"></span><span id="loss_of_multi_frame"></span><span id="LOSS_OF_MULTI_FRAME"></span>**Loss of Multi Frame** (74)
</dt> <dt>

<span id="Broadcast_Channel_Failure"></span><span id="broadcast_channel_failure"></span><span id="BROADCAST_CHANNEL_FAILURE"></span>**Broadcast Channel Failure** (75)
</dt> <dt>

<span id="Invalid_Message_Received"></span><span id="invalid_message_received"></span><span id="INVALID_MESSAGE_RECEIVED"></span>**Invalid Message Received** (76)
</dt> <dt>

<span id="Routing_Failure"></span><span id="routing_failure"></span><span id="ROUTING_FAILURE"></span>**Routing Failure** (77)
</dt> <dt>

<span id="Backplane_Failure"></span><span id="backplane_failure"></span><span id="BACKPLANE_FAILURE"></span>**Backplane Failure** (78)
</dt> <dt>

<span id="Identifier_Duplication"></span><span id="identifier_duplication"></span><span id="IDENTIFIER_DUPLICATION"></span>**Identifier Duplication** (79)
</dt> <dt>

<span id="Protection_Path_Failure"></span><span id="protection_path_failure"></span><span id="PROTECTION_PATH_FAILURE"></span>**Protection Path Failure** (80)
</dt> <dt>

<span id="Sync_Loss_or_Mismatch"></span><span id="sync_loss_or_mismatch"></span><span id="SYNC_LOSS_OR_MISMATCH"></span>**Sync Loss or Mismatch** (81)
</dt> <dt>

<span id="Terminal_Problem"></span><span id="terminal_problem"></span><span id="TERMINAL_PROBLEM"></span>**Terminal Problem** (82)
</dt> <dt>

<span id="Real_Time_Clock_Failure"></span><span id="real_time_clock_failure"></span><span id="REAL_TIME_CLOCK_FAILURE"></span>**Real Time Clock Failure** (83)
</dt> <dt>

<span id="Antenna_Failure"></span><span id="antenna_failure"></span><span id="ANTENNA_FAILURE"></span>**Antenna Failure** (84)
</dt> <dt>

<span id="Battery_Charging_Failure"></span><span id="battery_charging_failure"></span><span id="BATTERY_CHARGING_FAILURE"></span>**Battery Charging Failure** (85)
</dt> <dt>

<span id="Disk_Failure"></span><span id="disk_failure"></span><span id="DISK_FAILURE"></span>**Disk Failure** (86)
</dt> <dt>

<span id="Frequency_Hopping_Failure"></span><span id="frequency_hopping_failure"></span><span id="FREQUENCY_HOPPING_FAILURE"></span>**Frequency Hopping Failure** (87)
</dt> <dt>

<span id="Loss_of_Redundancy"></span><span id="loss_of_redundancy"></span><span id="LOSS_OF_REDUNDANCY"></span>**Loss of Redundancy** (88)
</dt> <dt>

<span id="Power_Supply_Failure"></span><span id="power_supply_failure"></span><span id="POWER_SUPPLY_FAILURE"></span>**Power Supply Failure** (89)
</dt> <dt>

<span id="Signal_Quality_Problem"></span><span id="signal_quality_problem"></span><span id="SIGNAL_QUALITY_PROBLEM"></span>**Signal Quality Problem** (90)
</dt> <dt>

<span id="__91____________Battery_Discharging"></span><span id="__91____________battery_discharging"></span><span id="__91____________BATTERY_DISCHARGING"></span>**//91 Battery Discharging** (91)
</dt> <dt>

<span id="Battery_Failure"></span><span id="battery_failure"></span><span id="BATTERY_FAILURE"></span>**Battery Failure** (92)
</dt> <dt>

<span id="Commercial_Power_Problem"></span><span id="commercial_power_problem"></span><span id="COMMERCIAL_POWER_PROBLEM"></span>**Commercial Power Problem** (93)
</dt> <dt>

<span id="Fan_Failure"></span><span id="fan_failure"></span><span id="FAN_FAILURE"></span>**Fan Failure** (94)
</dt> <dt>

<span id="Engine_Failure"></span><span id="engine_failure"></span><span id="ENGINE_FAILURE"></span>**Engine Failure** (95)
</dt> <dt>

<span id="Sensor_Failure"></span><span id="sensor_failure"></span><span id="SENSOR_FAILURE"></span>**Sensor Failure** (96)
</dt> <dt>

<span id="Fuse_Failure"></span><span id="fuse_failure"></span><span id="FUSE_FAILURE"></span>**Fuse Failure** (97)
</dt> <dt>

<span id="Generator_Failure"></span><span id="generator_failure"></span><span id="GENERATOR_FAILURE"></span>**Generator Failure** (98)
</dt> <dt>

<span id="Low_Battery"></span><span id="low_battery"></span><span id="LOW_BATTERY"></span>**Low Battery** (99)
</dt> <dt>

<span id="Low_Fuel"></span><span id="low_fuel"></span><span id="LOW_FUEL"></span>**Low Fuel** (100)
</dt> <dt>

<span id="Low_Water"></span><span id="low_water"></span><span id="LOW_WATER"></span>**Low Water** (101)
</dt> <dt>

<span id="Explosive_Gas"></span><span id="explosive_gas"></span><span id="EXPLOSIVE_GAS"></span>**Explosive Gas** (102)
</dt> <dt>

<span id="High_Winds"></span><span id="high_winds"></span><span id="HIGH_WINDS"></span>**High Winds** (103)
</dt> <dt>

<span id="Ice_Buildup"></span><span id="ice_buildup"></span><span id="ICE_BUILDUP"></span>**Ice Buildup** (104)
</dt> <dt>

<span id="Smoke"></span><span id="smoke"></span><span id="SMOKE"></span>**Smoke** (105)
</dt> <dt>

<span id="Memory_Mismatch"></span><span id="memory_mismatch"></span><span id="MEMORY_MISMATCH"></span>**Memory Mismatch** (106)
</dt> <dt>

<span id="Out_of_CPU_Cycles"></span><span id="out_of_cpu_cycles"></span><span id="OUT_OF_CPU_CYCLES"></span>**Out of CPU Cycles** (107)
</dt> <dt>

<span id="Software_Environment_Problem"></span><span id="software_environment_problem"></span><span id="SOFTWARE_ENVIRONMENT_PROBLEM"></span>**Software Environment Problem** (108)
</dt> <dt>

<span id="Software_Download_Failure"></span><span id="software_download_failure"></span><span id="SOFTWARE_DOWNLOAD_FAILURE"></span>**Software Download Failure** (109)
</dt> <dt>

<span id="Element_Reinitialized"></span><span id="element_reinitialized"></span><span id="ELEMENT_REINITIALIZED"></span>**Element Reinitialized** (110)
</dt> <dt>

<span id="Timeout"></span><span id="timeout"></span><span id="TIMEOUT"></span>**Timeout** (111)
</dt> <dt>

<span id="Logging_Problems"></span><span id="logging_problems"></span><span id="LOGGING_PROBLEMS"></span>**Logging Problems** (112)
</dt> <dt>

<span id="Leak_Detected"></span><span id="leak_detected"></span><span id="LEAK_DETECTED"></span>**Leak Detected** (113)
</dt> <dt>

<span id="Protection_Mechanism_Failure"></span><span id="protection_mechanism_failure"></span><span id="PROTECTION_MECHANISM_FAILURE"></span>**Protection Mechanism Failure** (114)
</dt> <dt>

<span id="__115____________Protecting_Resource_Failure"></span><span id="__115____________protecting_resource_failure"></span><span id="__115____________PROTECTING_RESOURCE_FAILURE"></span>**//115 Protecting Resource Failure** (115)
</dt> <dt>

<span id="Database_Inconsistency"></span><span id="database_inconsistency"></span><span id="DATABASE_INCONSISTENCY"></span>**Database Inconsistency** (116)
</dt> <dt>

<span id="Authentication_Failure"></span><span id="authentication_failure"></span><span id="AUTHENTICATION_FAILURE"></span>**Authentication Failure** (117)
</dt> <dt>

<span id="Breach_of_Confidentiality"></span><span id="breach_of_confidentiality"></span><span id="BREACH_OF_CONFIDENTIALITY"></span>**Breach of Confidentiality** (118)
</dt> <dt>

<span id="Cable_Tamper"></span><span id="cable_tamper"></span><span id="CABLE_TAMPER"></span>**Cable Tamper** (119)
</dt> <dt>

<span id="Delayed_Information"></span><span id="delayed_information"></span><span id="DELAYED_INFORMATION"></span>**Delayed Information** (120)
</dt> <dt>

<span id="Duplicate_Information"></span><span id="duplicate_information"></span><span id="DUPLICATE_INFORMATION"></span>**Duplicate Information** (121)
</dt> <dt>

<span id="Information_Missing"></span><span id="information_missing"></span><span id="INFORMATION_MISSING"></span>**Information Missing** (122)
</dt> <dt>

<span id="Information_Modification"></span><span id="information_modification"></span><span id="INFORMATION_MODIFICATION"></span>**Information Modification** (123)
</dt> <dt>

<span id="Information_Out_of_Sequence"></span><span id="information_out_of_sequence"></span><span id="INFORMATION_OUT_OF_SEQUENCE"></span>**Information Out of Sequence** (124)
</dt> <dt>

<span id="Key_Expired"></span><span id="key_expired"></span><span id="KEY_EXPIRED"></span>**Key Expired** (125)
</dt> <dt>

<span id="Non-Repudiation_Failure"></span><span id="non-repudiation_failure"></span><span id="NON-REPUDIATION_FAILURE"></span>**Non-Repudiation Failure** (126)
</dt> <dt>

<span id="Out_of_Hours_Activity"></span><span id="out_of_hours_activity"></span><span id="OUT_OF_HOURS_ACTIVITY"></span>**Out of Hours Activity** (127)
</dt> <dt>

<span id="Out_of_Service"></span><span id="out_of_service"></span><span id="OUT_OF_SERVICE"></span>**Out of Service** (128)
</dt> <dt>

<span id="Procedural_Error"></span><span id="procedural_error"></span><span id="PROCEDURAL_ERROR"></span>**Procedural Error** (129)
</dt> <dt>

<span id="Unexpected_Information_"></span><span id="unexpected_information_"></span><span id="UNEXPECTED_INFORMATION_"></span>**Unexpected Information** (130 )
</dt> </dl>

</dd> <dt>

**ProbableCauseDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string that describes the probable cause of the error. This property is inherited from [**CIM\_Error**](/previous-versions//cc150671(v=vs.85)).

</dd> <dt>

**RecommendedActions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string that describes recommended actions to take to resolve the error. This property is inherited from [**CIM\_Error**](/previous-versions//cc150671(v=vs.85)).

</dd> </dl>

## Remarks

Access to the **Msvm\_Error** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](/windows/desktop/WmiSdk/user-account-control-and-wmi).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_Error**](cim-error.md)
</dt> <dt>

[**CIM\_Error**](/previous-versions//cc150671(v=vs.85))
</dt> <dt>

[Virtual System Management Classes](virtual-system-management-classes.md)
</dt> </dl>

 

