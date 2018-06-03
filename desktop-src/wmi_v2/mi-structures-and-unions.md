---
title: MI Structures and Unions
description: WMI provides the following structures and unions.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5146DF83-CE41-4218-B8FA-7E5699589D74
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MI Structures and Unions

WMI provides the following structures and unions.

## In this section

<dl> <dt>

[**MI\_Application**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_application)
</dt> <dd>

Represents the initialized infrastructure.

</dd> <dt>

[**MI\_ApplicationFT**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_applicationft)
</dt> <dd>

A support structure used in the [**MI\_Application**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_application) structure. Use the functions with the name prefix "MI\_Application\_" to manipulate these structures.

</dd> <dt>

[**MI\_Array**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_array)
</dt> <dd>

Generalized type that represents an array. It can be generalized because all arrays are the same size, except the data element type will be specialized.

</dd> <dt>

[**MI\_ArrayField**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_arrayfield)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_BooleanA**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_booleana)
</dt> <dd>

Represents an array of [**MI\_Boolean**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_booleana) types.

</dd> <dt>

[**MI\_BooleanAField**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_booleanafield)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_BooleanField**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_booleanfield)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_Char16A**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_char16a)
</dt> <dd>

Represents an array of [**MI\_Char16**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_char16a) types.

</dd> <dt>

[**MI\_Char16AField**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_char16afield)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_Char16Field**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_char16field)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_ClassDecl**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_classdecl)
</dt> <dd>

This structure outlines the class declaration. It contains class name and hierarchy, properties, qualifiers, and methods.

</dd> <dt>

[**MI\_ClassFT**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_classft)
</dt> <dd>

A support structure used in the [**MI\_Class**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_class) structure. Use the functions with the name prefix "MI\_Class\_" to manipulate these structures.

</dd> <dt>

[**MI\_ClientFT\_V1**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_clientft_v1)
</dt> <dd>

Client function tables.

</dd> <dt>

[**MI\_ConstBooleanA**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_constbooleana)
</dt> <dd>

Represents an array of **MI\_ConstBoolean** types.

</dd> <dt>

[**MI\_ConstBooleanAField**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_constbooleanafield)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_ConstBooleanField**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_constbooleanfield)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_ConstChar16A**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_constchar16a)
</dt> <dd>

Represents an array of **MI\_Char16** types.

</dd> <dt>

[**MI\_ConstChar16AField**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_constchar16afield)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_ConstChar16Field**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_constchar16field)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_ConstDatetimeA**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_constdatetimea)
</dt> <dd>

Represents an array of **MI\_Datatime** types.

</dd> <dt>

[**MI\_ConstDatetimeAField**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_constdatetimeafield)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_ConstDatetimeField**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_constdatetimefield)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_ConstInstanceA**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_constinstancea)
</dt> <dd>

Represents an array of [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) types.

</dd> <dt>

[**MI\_ConstInstanceAField**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_constinstanceafield)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_ConstInstanceField**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_constinstancefield)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_ConstReal32A**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_constreal32a)
</dt> <dd>

Represents an array of **MI\_Real32** types

</dd> <dt>

[**MI\_ConstReal32AField**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_constreal32afield)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_ConstReal32Field**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_constreal32field)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_ConstReal64A**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_constreal64a)
</dt> <dd>

Represents an array of **MI\_Real64** types.

</dd> <dt>

[**MI\_ConstReal64AField**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_constreal64afield)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_ConstReal64Field**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_constreal64field)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_ConstReferenceA**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_constreferencea)
</dt> <dd>

Represents an array of [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) types.

</dd> <dt>

[**MI\_ConstReferenceAField**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_constreferenceafield)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_ConstReferenceField**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_constreferencefield)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_ConstSint16A**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_constsint16a)
</dt> <dd>

Represents an array of **MI\_Sint16** types.

</dd> <dt>

[**MI\_ConstSint16AField**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_constsint16afield)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_ConstSint16Field**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_constsint16field)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure

</dd> <dt>

[**MI\_ConstSint32A**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_constsint32a)
</dt> <dd>

Represents an array of **MI\_Sint32** types.

</dd> <dt>

[**MI\_ConstSint32AField**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_constsint32afield)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_ConstSint32Field**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_constsint32field)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_ConstSint64A**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_constsint64a)
</dt> <dd>

Represents an array of **MI\_Sint64** types.

</dd> <dt>

[**MI\_ConstSint64AField**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_constsint64afield)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_ConstSint64Field**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_constsint64field)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_ConstSint8A**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_constsint8a)
</dt> <dd>

Represents an array of **MI\_Sint8** types.

</dd> <dt>

[**MI\_ConstSint8AField**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_constsint8afield)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_ConstSint8Field**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_constsint8field)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_ConstStringA**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_conststringa)
</dt> <dd>

Represents an array of **MI\_Char** types.

</dd> <dt>

[**MI\_ConstStringAField**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_conststringafield)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_ConstStringField**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_conststringfield)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_ConstUint16A**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_constuint16a)
</dt> <dd>

Represents an array of **MI\_Uint16A** types.

</dd> <dt>

[**MI\_ConstUint16AField**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_constuint16afield)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_ConstUint16Field**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_constuint16field)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_ConstUint32A**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_constuint32a)
</dt> <dd>

Represents an array of **MI\_Uint32** types.

</dd> <dt>

[**MI\_ConstUint32AField**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_constuint32afield)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_ConstUint32Field**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_constuint32field)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_ConstUint64A**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_constuint64a)
</dt> <dd>

Represents an array of **MI\_Uint64** types.

</dd> <dt>

[**MI\_ConstUint64AField**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_constuint64afield)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_ConstUint64Field**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_constuint64field)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_ConstUint8A**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_constuint8a)
</dt> <dd>

Represents an array of **MI\_Uint8** types.

</dd> <dt>

[**MI\_ConstUint8AField**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_constuint8afield)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_ConstUint8Field**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_constuint8field)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_Context**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_context)
</dt> <dd>

Holds context for the operation that the provider needs to carry out. There are a set of MI\_Context\_\* APIs to perform such actions as reporting operation results and retrieving the options/settings associated with an operation. The context object is valid only until the final result for the operation is sent.

</dd> <dt>

[**MI\_ContextFT**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_contextft)
</dt> <dd>

A support structure used in the [**MI\_Context**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_context) structure. Use the functions with the name prefix "MI\_Context\_" to manipulate these structures.

</dd> <dt>

[**MI\_Datetime**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_datetime)
</dt> <dd>

Represents a union of [**MI\_Timestamp**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_timestamp) and [**MI\_Interval**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_interval).

</dd> <dt>

[**MI\_DatetimeA**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_datetimea)
</dt> <dd>

Represents an array of [**MI\_Datetime**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_datetime) types.

</dd> <dt>

[**MI\_DatetimeAField**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_datetimeafield)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_DatetimeField**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_datetimefield)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_Deserializer**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_deserializer)
</dt> <dd>

Deserialization object as created from [**MI\_Application\_NewDeserializer**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_application_newdeserializer). The object itself should not be manually used or changed as it is used internally.

</dd> <dt>

[**MI\_DeserializerFT**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_deserializerft)
</dt> <dd>

A support structure used in the [**MI\_ClientFT\_V1**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_clientft_v1) structure. Use the functions with the name prefix "MI\_Deserializer\_" to manipulate these structures.

</dd> <dt>

[**MI\_DestinationOptions**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_destinationoptions)
</dt> <dd>

Represents a set of destination options. Destination options are a set of configurations that define the way an operation communicates with the server.

</dd> <dt>

[**MI\_DestinationOptionsFT**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_destinationoptionsft)
</dt> <dd>

A support structure used in the [**MI\_DestinationOptions**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_destinationoptions) structure. Use the functions with the name prefix "MI\_DestinationOptions\_" to manipulate these structures.

</dd> <dt>

[**MI\_FeatureDecl**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_featuredecl)
</dt> <dd>

Contains properties that are common to the [**MI\_PropertyDecl**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_propertydecl)[**MI\_ParameterDecl**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_parameterdecl) and [**MI\_MethodDecl**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_methoddecl) structures.

</dd> <dt>

[**MI\_Filter**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_filter)
</dt> <dd>

Contains a reference to the function table [**MI\_FilterFT**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_filterft).

</dd> <dt>

[**MI\_FilterFT**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_filterft)
</dt> <dd>

A support structure used in the [**MI\_Filter**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_filter) structure. Use the functions with the name prefix "MI\_Filter\_" to manipulate these structures.

</dd> <dt>

[**MI\_HostedProvider**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_hostedprovider)
</dt> <dd>

Represents the hosting of a provider in a client application.

</dd> <dt>

[**MI\_HostedProviderFT**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_hostedproviderft)
</dt> <dd>

A support structure used in the [**MI\_HostedProvider**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_hostedprovider) structure. Use the functions with the name prefix "MI\_HostedProvider\_" to manipulate these structures.

</dd> <dt>

[**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance)
</dt> <dd>

This structure represents a CIM instance. This object should not be accessed directly. Instead, the **MI\_Instance\_\*** functions should be used.

</dd> <dt>

[**MI\_InstanceA**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instancea)
</dt> <dd>

Represents an array of [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structures.

</dd> <dt>

[**MI\_InstanceAField**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instanceafield)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_InstanceField**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instancefield)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_InstanceExFT**](/previous-versions/windows/desktop/api/mi/ns-mi-_mi_instanceexft)
</dt> <dd>

Extends the [**MI\_InstanceFT**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instanceft) structure.

</dd> <dt>

[**MI\_InstanceFT**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instanceft)
</dt> <dd>

A support structure used in the [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure. Use the functions with the name prefix **MI\_Instance\_** to manipulate these structures.

</dd> <dt>

[**MI\_Interval**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_interval)
</dt> <dd>

[**MI\_Interval**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_interval) represents an interval of time.

</dd> <dt>

[**MI\_MethodDecl**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_methoddecl)
</dt> <dd>

Represents a CIM method.

</dd> <dt>

[**MI\_Module**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_module)
</dt> <dd>

Generated by the provider, this object contains all the data needed by the provider manager to manage the providers within this module.

</dd> <dt>

[**\_MI\_Module\_Self**](/previous-versions/windows/desktop/api/mispace_wmi/)
</dt> <dd>

An optional user-defined structure containing provider state data.

</dd> <dt>

[**MI\_ObjectDecl**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_objectdecl)
</dt> <dd>

Contains properties common to the [**MI\_ClassDecl**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_classdecl) and [**MI\_PropertyDecl**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_propertydecl) structures.

</dd> <dt>

[**MI\_Operation**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_operation)
</dt> <dd>

Represents a single operations execution. This object holds the internal function tables for carrying out actions on the operation.

</dd> <dt>

[**MI\_OperationCallbacks**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_operationcallbacks)
</dt> <dd>

Structure that holds all callback function pointers for carrying out operations.

</dd> <dt>

[**MI\_OperationFT**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_operationft)
</dt> <dd>

A support structure used in the [**MI\_Operation**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_operation) structure. Use the functions with the name prefix "MI\_Operation\_" to manipulate these structures.

</dd> <dt>

[**MI\_OperationOptions**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_operationoptions)
</dt> <dd>

Represents a set of operation options.

</dd> <dt>

[**MI\_OperationOptionsFT**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_operationoptionsft)
</dt> <dd>

A support structure used in the [**MI\_OperationOptions**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_operationoptions) structure. Use the functions with the name prefix "MI\_OperationOptions\_" to manipulate these structures.

</dd> <dt>

[**MI\_ParameterDecl**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_parameterdecl)
</dt> <dd>

Represents CIM method parameters.

</dd> <dt>

[**MI\_ParameterSet**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_parameterset)
</dt> <dd>

Holds the method parameters of a class definition.

</dd> <dt>

[**MI\_ParameterSetFT**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_parametersetft)
</dt> <dd>

A support structure used in the [**MI\_ParameterSet**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_parameterset) structure. Use the functions with the name prefix MI\_ParameterSet\_ to manipulate these structures.

</dd> <dt>

[**MI\_PropertyDecl**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_propertydecl)
</dt> <dd>

Represents a class property (element) in a class's declaration.

</dd> <dt>

[**MI\_PropertySet**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_propertyset)
</dt> <dd>

Implements a set of property names.

</dd> <dt>

[**MI\_PropertySetFT**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_propertysetft)
</dt> <dd>

A support structure used in the [**MI\_PropertySet**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_propertyset) structure. Use the functions with the name prefix "MI\_PropertySet\_" to manipulate these structures.

</dd> <dt>

[**MI\_ProviderFT**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_providerft)
</dt> <dd>

A support structure used in the [**MI\_ClassDecl**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_classdecl) and [**MI\_Module**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_module) structures.

</dd> <dt>

[**MI\_Qualifier**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_qualifier)
</dt> <dd>

Represents a CIM qualifier.

</dd> <dt>

[**MI\_QualifierDecl**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_qualifierdecl)
</dt> <dd>

Represents a CIM qualifier declaration.

</dd> <dt>

[**MI\_QualifierSet**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_qualifierset)
</dt> <dd>

Allows the developer to view the qualifiers of a class definition.

</dd> <dt>

[**MI\_QualifierSetFT**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_qualifiersetft)
</dt> <dd>

A support structure used in the [**MI\_QualifierSet**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_qualifierset) structure. Use the functions with the name prefix "MI\_QualifierSet\_" to manipulate these structures.

</dd> <dt>

[**MI\_Real32A**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_real32a)
</dt> <dd>

Represents an array of **MI\_Real32** types.

</dd> <dt>

[**MI\_Real32AField**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_real32afield)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_Real32Field**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_real32field)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_Real64A**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_real64a)
</dt> <dd>

Represents an array of **MI\_Real64** types.

</dd> <dt>

[**MI\_Real64AField**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_real64afield)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_Real64Field**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_real64field)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_ReferenceA**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_referencea)
</dt> <dd>

Represents an array of pointers to [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) types.

</dd> <dt>

[**MI\_ReferenceAField**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_referenceafield)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_ReferenceField**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_referencefield)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_SchemaDecl**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_schemadecl)
</dt> <dd>

Represents the schema objects in a CIM schema, which include CIM classes and CIM qualifier declarations.

</dd> <dt>

[**MI\_Serializer**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_serializer)
</dt> <dd>

An object tied to a specific serialization technique.

</dd> <dt>

[**MI\_SerializerFT**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_serializerft)
</dt> <dd>

A support structure used in the [**MI\_ClientFT\_V1**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_clientft_v1) structure. Use the functions with the name prefix "MI\_Serializer\_" to manipulate these structures.

</dd> <dt>

[**MI\_Server**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_server)
</dt> <dd>

This structure defines default function tables for all types: Context, Instance, PropertySet, and Filter.

</dd> <dt>

[**MI\_ServerFT**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_serverft)
</dt> <dd>

A support structure used in the [**MI\_Server**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_server) structure. Use the functions with the name prefix "MI\_Server\_" to manipulate these structures.

</dd> <dt>

[**MI\_Session**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_session)
</dt> <dd>

An object that is associated with a destination and has a set of credentials and options associated with it. .

</dd> <dt>

[**MI\_SessionFT**](/previous-versions/windows/desktop/api/mi/ns-mi-_mi_sessionft)
</dt> <dd>

Function table for all actions on a session object.

</dd> <dt>

[**MI\_SessionCallbacks**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_sessioncallbacks)
</dt> <dd>

A container for callback function pointers that handle logging and error messages.

</dd> <dt>

[**MI\_Sint16A**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_sint16a)
</dt> <dd>

Represents an array of **MI\_Sint16** types.

</dd> <dt>

[**MI\_Sint16AField**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_sint16afield)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_Sint16Field**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_sint16field)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_Sint32A**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_sint32a)
</dt> <dd>

Represents an array of **MI\_Sint32** types.

</dd> <dt>

[**MI\_Sint32AField**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_sint32afield)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_Sint32Field**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_sint32field)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_Sint64A**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_sint64a)
</dt> <dd>

Represents an array of **MI\_Sint64** types.

</dd> <dt>

[**MI\_Sint64AField**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_sint64afield)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_Sint64Field**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_sint64field)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_Sint8A**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_sint8a)
</dt> <dd>

Represents an array of **MI\_Sint8** types.

</dd> <dt>

[**MI\_Sint8AField**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_sint8afield)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_Sint8Field**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_sint8field)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_StringA**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_stringa)
</dt> <dd>

Represents an array of pointers to null-terminated **MI\_Char**\* strings.

</dd> <dt>

[**MI\_StringAField**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_stringafield)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_StringField**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_stringfield)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_subscriptiondeliveryoptions)
</dt> <dd>

The subscription options object stores configuration options used for passing into subscription operations.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptionsFT**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_subscriptiondeliveryoptionsft)
</dt> <dd>

A support structure used in the [**MI\_SubscriptionDeliveryOptions**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_subscriptiondeliveryoptions) structure. Use the functions with the name prefix "MI\_SubscriptionDeliveryOptions\_" to manipulate these structures.

</dd> <dt>

[**MI\_Timestamp**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_timestamp)
</dt> <dd>

[**MI\_Timestamp**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_timestamp) specifies a timestamp or a specific point in time.

</dd> <dt>

[**MI\_Uint16A**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_uint16a)
</dt> <dd>

Represents an array of **MI\_Uint16** types.

</dd> <dt>

[**MI\_Uint16AField**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_uint16afield)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_Uint16Field**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_uint16field)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_Uint32A**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_uint32a)
</dt> <dd>

Represents an array of **MI\_Uint32** types.

</dd> <dt>

[**MI\_Uint32AField**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_uint32afield)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_Uint32Field**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_uint32field)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_Uint64A**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_uint64a)
</dt> <dd>

Represents an array of **MI\_Uint64** types.

</dd> <dt>

[**MI\_Uint64AField**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_uint64afield)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_Uint64Field**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_uint64field)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_Uint8A**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_uint8a)
</dt> <dd>

Represents an array of **MI\_Uint8** types.

</dd> <dt>

[**MI\_Uint8AField**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_uint8afield)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_instance) structure.

</dd> <dt>

[**MI\_Uint8Field**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_uint8field)
</dt> <dd>

Represents a property inside an MI\_Instance structure.

</dd> <dt>

[**MI\_UserCredentials**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_usercredentials)
</dt> <dd>

A user's credentials. It includes an authentication type and either a username and password or a certificate thumbprint.

</dd> <dt>

[**MI\_UsernamePasswordCreds**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_usernamepasswordcreds)
</dt> <dd>

A username/password combination used for subscription operations.

</dd> <dt>

[**MI\_UtilitiesFT**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_utilitiesft)
</dt> <dd>

A support structure used in the [**MI\_ClientFT\_V1**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_clientft_v1) structure. Use the functions with the name prefix "MI\_Utilities\_" to manipulate these structures.

</dd> <dt>

[**MI\_Value**](/previous-versions/windows/desktop/api/mi/ns-mi-_mi_value)
</dt> <dd>

A union of all CIM data types.

</dd> </dl>

 

 




