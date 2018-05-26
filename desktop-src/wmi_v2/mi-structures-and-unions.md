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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MI Structures and Unions

WMI provides the following structures and unions.

## In this section

<dl> <dt>

[**MI\_Application**](/windows/previous-versions/Mi/ns-mi-_mi_application?branch=master)
</dt> <dd>

Represents the initialized infrastructure.

</dd> <dt>

[**MI\_ApplicationFT**](/windows/previous-versions/Mi/ns-mi-_mi_applicationft?branch=master)
</dt> <dd>

A support structure used in the [**MI\_Application**](/windows/previous-versions/Mi/ns-mi-_mi_application?branch=master) structure. Use the functions with the name prefix "MI\_Application\_" to manipulate these structures.

</dd> <dt>

[**MI\_Array**](/windows/previous-versions/Mi/ns-mi-_mi_array?branch=master)
</dt> <dd>

Generalized type that represents an array. It can be generalized because all arrays are the same size, except the data element type will be specialized.

</dd> <dt>

[**MI\_ArrayField**](/windows/previous-versions/Mi/ns-mi-_mi_arrayfield?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_BooleanA**](/windows/previous-versions/Mi/ns-mi-_mi_booleana?branch=master)
</dt> <dd>

Represents an array of [**MI\_Boolean**](/windows/previous-versions/Mi/ns-mi-_mi_booleana?branch=master) types.

</dd> <dt>

[**MI\_BooleanAField**](/windows/previous-versions/Mi/ns-mi-_mi_booleanafield?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_BooleanField**](/windows/previous-versions/Mi/ns-mi-_mi_booleanfield?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_Char16A**](/windows/previous-versions/Mi/ns-mi-_mi_char16a?branch=master)
</dt> <dd>

Represents an array of [**MI\_Char16**](/windows/previous-versions/Mi/ns-mi-_mi_char16a?branch=master) types.

</dd> <dt>

[**MI\_Char16AField**](/windows/previous-versions/Mi/ns-mi-_mi_char16afield?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_Char16Field**](/windows/previous-versions/Mi/ns-mi-_mi_char16field?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_ClassDecl**](/windows/previous-versions/Mi/ns-mi-_mi_classdecl?branch=master)
</dt> <dd>

This structure outlines the class declaration. It contains class name and hierarchy, properties, qualifiers, and methods.

</dd> <dt>

[**MI\_ClassFT**](/windows/previous-versions/Mi/ns-mi-_mi_classft?branch=master)
</dt> <dd>

A support structure used in the [**MI\_Class**](/windows/previous-versions/Mi/ns-mi-_mi_class?branch=master) structure. Use the functions with the name prefix "MI\_Class\_" to manipulate these structures.

</dd> <dt>

[**MI\_ClientFT\_V1**](/windows/previous-versions/Mi/ns-mi-_mi_clientft_v1?branch=master)
</dt> <dd>

Client function tables.

</dd> <dt>

[**MI\_ConstBooleanA**](/windows/previous-versions/Mi/ns-mi-_mi_constbooleana?branch=master)
</dt> <dd>

Represents an array of **MI\_ConstBoolean** types.

</dd> <dt>

[**MI\_ConstBooleanAField**](/windows/previous-versions/Mi/ns-mi-_mi_constbooleanafield?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_ConstBooleanField**](/windows/previous-versions/Mi/ns-mi-_mi_constbooleanfield?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_ConstChar16A**](/windows/previous-versions/Mi/ns-mi-_mi_constchar16a?branch=master)
</dt> <dd>

Represents an array of **MI\_Char16** types.

</dd> <dt>

[**MI\_ConstChar16AField**](/windows/previous-versions/Mi/ns-mi-_mi_constchar16afield?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_ConstChar16Field**](/windows/previous-versions/Mi/ns-mi-_mi_constchar16field?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_ConstDatetimeA**](/windows/previous-versions/Mi/ns-mi-_mi_constdatetimea?branch=master)
</dt> <dd>

Represents an array of **MI\_Datatime** types.

</dd> <dt>

[**MI\_ConstDatetimeAField**](/windows/previous-versions/Mi/ns-mi-_mi_constdatetimeafield?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_ConstDatetimeField**](/windows/previous-versions/Mi/ns-mi-_mi_constdatetimefield?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_ConstInstanceA**](/windows/previous-versions/Mi/ns-mi-_mi_constinstancea?branch=master)
</dt> <dd>

Represents an array of [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) types.

</dd> <dt>

[**MI\_ConstInstanceAField**](/windows/previous-versions/Mi/ns-mi-_mi_constinstanceafield?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_ConstInstanceField**](/windows/previous-versions/Mi/ns-mi-_mi_constinstancefield?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_ConstReal32A**](/windows/previous-versions/Mi/ns-mi-_mi_constreal32a?branch=master)
</dt> <dd>

Represents an array of **MI\_Real32** types

</dd> <dt>

[**MI\_ConstReal32AField**](/windows/previous-versions/Mi/ns-mi-_mi_constreal32afield?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_ConstReal32Field**](/windows/previous-versions/Mi/ns-mi-_mi_constreal32field?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_ConstReal64A**](/windows/previous-versions/Mi/ns-mi-_mi_constreal64a?branch=master)
</dt> <dd>

Represents an array of **MI\_Real64** types.

</dd> <dt>

[**MI\_ConstReal64AField**](/windows/previous-versions/Mi/ns-mi-_mi_constreal64afield?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_ConstReal64Field**](/windows/previous-versions/Mi/ns-mi-_mi_constreal64field?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_ConstReferenceA**](/windows/previous-versions/Mi/ns-mi-_mi_constreferencea?branch=master)
</dt> <dd>

Represents an array of [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) types.

</dd> <dt>

[**MI\_ConstReferenceAField**](/windows/previous-versions/Mi/ns-mi-_mi_constreferenceafield?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_ConstReferenceField**](/windows/previous-versions/Mi/ns-mi-_mi_constreferencefield?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_ConstSint16A**](/windows/previous-versions/Mi/ns-mi-_mi_constsint16a?branch=master)
</dt> <dd>

Represents an array of **MI\_Sint16** types.

</dd> <dt>

[**MI\_ConstSint16AField**](/windows/previous-versions/Mi/ns-mi-_mi_constsint16afield?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_ConstSint16Field**](/windows/previous-versions/Mi/ns-mi-_mi_constsint16field?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure

</dd> <dt>

[**MI\_ConstSint32A**](/windows/previous-versions/Mi/ns-mi-_mi_constsint32a?branch=master)
</dt> <dd>

Represents an array of **MI\_Sint32** types.

</dd> <dt>

[**MI\_ConstSint32AField**](/windows/previous-versions/Mi/ns-mi-_mi_constsint32afield?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_ConstSint32Field**](/windows/previous-versions/Mi/ns-mi-_mi_constsint32field?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_ConstSint64A**](/windows/previous-versions/Mi/ns-mi-_mi_constsint64a?branch=master)
</dt> <dd>

Represents an array of **MI\_Sint64** types.

</dd> <dt>

[**MI\_ConstSint64AField**](/windows/previous-versions/Mi/ns-mi-_mi_constsint64afield?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_ConstSint64Field**](/windows/previous-versions/Mi/ns-mi-_mi_constsint64field?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_ConstSint8A**](/windows/previous-versions/Mi/ns-mi-_mi_constsint8a?branch=master)
</dt> <dd>

Represents an array of **MI\_Sint8** types.

</dd> <dt>

[**MI\_ConstSint8AField**](/windows/previous-versions/Mi/ns-mi-_mi_constsint8afield?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_ConstSint8Field**](/windows/previous-versions/Mi/ns-mi-_mi_constsint8field?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_ConstStringA**](/windows/previous-versions/Mi/ns-mi-_mi_conststringa?branch=master)
</dt> <dd>

Represents an array of **MI\_Char** types.

</dd> <dt>

[**MI\_ConstStringAField**](/windows/previous-versions/Mi/ns-mi-_mi_conststringafield?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_ConstStringField**](/windows/previous-versions/Mi/ns-mi-_mi_conststringfield?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_ConstUint16A**](/windows/previous-versions/Mi/ns-mi-_mi_constuint16a?branch=master)
</dt> <dd>

Represents an array of **MI\_Uint16A** types.

</dd> <dt>

[**MI\_ConstUint16AField**](/windows/previous-versions/Mi/ns-mi-_mi_constuint16afield?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_ConstUint16Field**](/windows/previous-versions/Mi/ns-mi-_mi_constuint16field?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_ConstUint32A**](/windows/previous-versions/Mi/ns-mi-_mi_constuint32a?branch=master)
</dt> <dd>

Represents an array of **MI\_Uint32** types.

</dd> <dt>

[**MI\_ConstUint32AField**](/windows/previous-versions/Mi/ns-mi-_mi_constuint32afield?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_ConstUint32Field**](/windows/previous-versions/Mi/ns-mi-_mi_constuint32field?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_ConstUint64A**](/windows/previous-versions/Mi/ns-mi-_mi_constuint64a?branch=master)
</dt> <dd>

Represents an array of **MI\_Uint64** types.

</dd> <dt>

[**MI\_ConstUint64AField**](/windows/previous-versions/Mi/ns-mi-_mi_constuint64afield?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_ConstUint64Field**](/windows/previous-versions/Mi/ns-mi-_mi_constuint64field?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_ConstUint8A**](/windows/previous-versions/Mi/ns-mi-_mi_constuint8a?branch=master)
</dt> <dd>

Represents an array of **MI\_Uint8** types.

</dd> <dt>

[**MI\_ConstUint8AField**](/windows/previous-versions/Mi/ns-mi-_mi_constuint8afield?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_ConstUint8Field**](/windows/previous-versions/Mi/ns-mi-_mi_constuint8field?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_Context**](/windows/previous-versions/Mi/ns-mi-_mi_context?branch=master)
</dt> <dd>

Holds context for the operation that the provider needs to carry out. There are a set of MI\_Context\_\* APIs to perform such actions as reporting operation results and retrieving the options/settings associated with an operation. The context object is valid only until the final result for the operation is sent.

</dd> <dt>

[**MI\_ContextFT**](/windows/previous-versions/Mi/ns-mi-_mi_contextft?branch=master)
</dt> <dd>

A support structure used in the [**MI\_Context**](/windows/previous-versions/Mi/ns-mi-_mi_context?branch=master) structure. Use the functions with the name prefix "MI\_Context\_" to manipulate these structures.

</dd> <dt>

[**MI\_Datetime**](/windows/previous-versions/Mi/ns-mi-_mi_datetime?branch=master)
</dt> <dd>

Represents a union of [**MI\_Timestamp**](/windows/previous-versions/Mi/ns-mi-_mi_timestamp?branch=master) and [**MI\_Interval**](/windows/previous-versions/Mi/ns-mi-_mi_interval?branch=master).

</dd> <dt>

[**MI\_DatetimeA**](/windows/previous-versions/Mi/ns-mi-_mi_datetimea?branch=master)
</dt> <dd>

Represents an array of [**MI\_Datetime**](/windows/previous-versions/Mi/ns-mi-_mi_datetime?branch=master) types.

</dd> <dt>

[**MI\_DatetimeAField**](/windows/previous-versions/Mi/ns-mi-_mi_datetimeafield?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_DatetimeField**](/windows/previous-versions/Mi/ns-mi-_mi_datetimefield?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_Deserializer**](/windows/previous-versions/Mi/ns-mi-_mi_deserializer?branch=master)
</dt> <dd>

Deserialization object as created from [**MI\_Application\_NewDeserializer**](/windows/previous-versions/Mi/nf-mi-mi_application_newdeserializer?branch=master). The object itself should not be manually used or changed as it is used internally.

</dd> <dt>

[**MI\_DeserializerFT**](/windows/previous-versions/Mi/ns-mi-_mi_deserializerft?branch=master)
</dt> <dd>

A support structure used in the [**MI\_ClientFT\_V1**](/windows/previous-versions/Mi/ns-mi-_mi_clientft_v1?branch=master) structure. Use the functions with the name prefix "MI\_Deserializer\_" to manipulate these structures.

</dd> <dt>

[**MI\_DestinationOptions**](/windows/previous-versions/Mi/ns-mi-_mi_destinationoptions?branch=master)
</dt> <dd>

Represents a set of destination options. Destination options are a set of configurations that define the way an operation communicates with the server.

</dd> <dt>

[**MI\_DestinationOptionsFT**](/windows/previous-versions/Mi/ns-mi-_mi_destinationoptionsft?branch=master)
</dt> <dd>

A support structure used in the [**MI\_DestinationOptions**](/windows/previous-versions/Mi/ns-mi-_mi_destinationoptions?branch=master) structure. Use the functions with the name prefix "MI\_DestinationOptions\_" to manipulate these structures.

</dd> <dt>

[**MI\_FeatureDecl**](/windows/previous-versions/Mi/ns-mi-_mi_featuredecl?branch=master)
</dt> <dd>

Contains properties that are common to the [**MI\_PropertyDecl**](/windows/previous-versions/Mi/ns-mi-_mi_propertydecl?branch=master)[**MI\_ParameterDecl**](/windows/previous-versions/Mi/ns-mi-_mi_parameterdecl?branch=master) and [**MI\_MethodDecl**](/windows/previous-versions/Mi/ns-mi-_mi_methoddecl?branch=master) structures.

</dd> <dt>

[**MI\_Filter**](/windows/previous-versions/Mi/ns-mi-_mi_filter?branch=master)
</dt> <dd>

Contains a reference to the function table [**MI\_FilterFT**](/windows/previous-versions/Mi/ns-mi-_mi_filterft?branch=master).

</dd> <dt>

[**MI\_FilterFT**](/windows/previous-versions/Mi/ns-mi-_mi_filterft?branch=master)
</dt> <dd>

A support structure used in the [**MI\_Filter**](/windows/previous-versions/Mi/ns-mi-_mi_filter?branch=master) structure. Use the functions with the name prefix "MI\_Filter\_" to manipulate these structures.

</dd> <dt>

[**MI\_HostedProvider**](/windows/previous-versions/Mi/ns-mi-_mi_hostedprovider?branch=master)
</dt> <dd>

Represents the hosting of a provider in a client application.

</dd> <dt>

[**MI\_HostedProviderFT**](/windows/previous-versions/Mi/ns-mi-_mi_hostedproviderft?branch=master)
</dt> <dd>

A support structure used in the [**MI\_HostedProvider**](/windows/previous-versions/Mi/ns-mi-_mi_hostedprovider?branch=master) structure. Use the functions with the name prefix "MI\_HostedProvider\_" to manipulate these structures.

</dd> <dt>

[**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master)
</dt> <dd>

This structure represents a CIM instance. This object should not be accessed directly. Instead, the **MI\_Instance\_\*** functions should be used.

</dd> <dt>

[**MI\_InstanceA**](/windows/previous-versions/Mi/ns-mi-_mi_instancea?branch=master)
</dt> <dd>

Represents an array of [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structures.

</dd> <dt>

[**MI\_InstanceAField**](/windows/previous-versions/Mi/ns-mi-_mi_instanceafield?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_InstanceField**](/windows/previous-versions/Mi/ns-mi-_mi_instancefield?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_InstanceExFT**](/windows/previous-versions/mi/ns-mi-_mi_instanceexft?branch=master)
</dt> <dd>

Extends the [**MI\_InstanceFT**](/windows/previous-versions/Mi/ns-mi-_mi_instanceft?branch=master) structure.

</dd> <dt>

[**MI\_InstanceFT**](/windows/previous-versions/Mi/ns-mi-_mi_instanceft?branch=master)
</dt> <dd>

A support structure used in the [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure. Use the functions with the name prefix **MI\_Instance\_** to manipulate these structures.

</dd> <dt>

[**MI\_Interval**](/windows/previous-versions/Mi/ns-mi-_mi_interval?branch=master)
</dt> <dd>

[**MI\_Interval**](/windows/previous-versions/Mi/ns-mi-_mi_interval?branch=master) represents an interval of time.

</dd> <dt>

[**MI\_MethodDecl**](/windows/previous-versions/Mi/ns-mi-_mi_methoddecl?branch=master)
</dt> <dd>

Represents a CIM method.

</dd> <dt>

[**MI\_Module**](/windows/previous-versions/Mi/ns-mi-_mi_module?branch=master)
</dt> <dd>

Generated by the provider, this object contains all the data needed by the provider manager to manage the providers within this module.

</dd> <dt>

[**\_MI\_Module\_Self**](/windows/previous-versions/mispace_wmi/?branch=master)
</dt> <dd>

An optional user-defined structure containing provider state data.

</dd> <dt>

[**MI\_ObjectDecl**](/windows/previous-versions/Mi/ns-mi-_mi_objectdecl?branch=master)
</dt> <dd>

Contains properties common to the [**MI\_ClassDecl**](/windows/previous-versions/Mi/ns-mi-_mi_classdecl?branch=master) and [**MI\_PropertyDecl**](/windows/previous-versions/Mi/ns-mi-_mi_propertydecl?branch=master) structures.

</dd> <dt>

[**MI\_Operation**](/windows/previous-versions/Mi/ns-mi-_mi_operation?branch=master)
</dt> <dd>

Represents a single operations execution. This object holds the internal function tables for carrying out actions on the operation.

</dd> <dt>

[**MI\_OperationCallbacks**](/windows/previous-versions/Mi/ns-mi-_mi_operationcallbacks?branch=master)
</dt> <dd>

Structure that holds all callback function pointers for carrying out operations.

</dd> <dt>

[**MI\_OperationFT**](/windows/previous-versions/Mi/ns-mi-_mi_operationft?branch=master)
</dt> <dd>

A support structure used in the [**MI\_Operation**](/windows/previous-versions/Mi/ns-mi-_mi_operation?branch=master) structure. Use the functions with the name prefix "MI\_Operation\_" to manipulate these structures.

</dd> <dt>

[**MI\_OperationOptions**](/windows/previous-versions/Mi/ns-mi-_mi_operationoptions?branch=master)
</dt> <dd>

Represents a set of operation options.

</dd> <dt>

[**MI\_OperationOptionsFT**](/windows/previous-versions/Mi/ns-mi-_mi_operationoptionsft?branch=master)
</dt> <dd>

A support structure used in the [**MI\_OperationOptions**](/windows/previous-versions/Mi/ns-mi-_mi_operationoptions?branch=master) structure. Use the functions with the name prefix "MI\_OperationOptions\_" to manipulate these structures.

</dd> <dt>

[**MI\_ParameterDecl**](/windows/previous-versions/Mi/ns-mi-_mi_parameterdecl?branch=master)
</dt> <dd>

Represents CIM method parameters.

</dd> <dt>

[**MI\_ParameterSet**](/windows/previous-versions/Mi/ns-mi-_mi_parameterset?branch=master)
</dt> <dd>

Holds the method parameters of a class definition.

</dd> <dt>

[**MI\_ParameterSetFT**](/windows/previous-versions/Mi/ns-mi-_mi_parametersetft?branch=master)
</dt> <dd>

A support structure used in the [**MI\_ParameterSet**](/windows/previous-versions/Mi/ns-mi-_mi_parameterset?branch=master) structure. Use the functions with the name prefix MI\_ParameterSet\_ to manipulate these structures.

</dd> <dt>

[**MI\_PropertyDecl**](/windows/previous-versions/Mi/ns-mi-_mi_propertydecl?branch=master)
</dt> <dd>

Represents a class property (element) in a class's declaration.

</dd> <dt>

[**MI\_PropertySet**](/windows/previous-versions/Mi/ns-mi-_mi_propertyset?branch=master)
</dt> <dd>

Implements a set of property names.

</dd> <dt>

[**MI\_PropertySetFT**](/windows/previous-versions/Mi/ns-mi-_mi_propertysetft?branch=master)
</dt> <dd>

A support structure used in the [**MI\_PropertySet**](/windows/previous-versions/Mi/ns-mi-_mi_propertyset?branch=master) structure. Use the functions with the name prefix "MI\_PropertySet\_" to manipulate these structures.

</dd> <dt>

[**MI\_ProviderFT**](/windows/previous-versions/Mi/ns-mi-_mi_providerft?branch=master)
</dt> <dd>

A support structure used in the [**MI\_ClassDecl**](/windows/previous-versions/Mi/ns-mi-_mi_classdecl?branch=master) and [**MI\_Module**](/windows/previous-versions/Mi/ns-mi-_mi_module?branch=master) structures.

</dd> <dt>

[**MI\_Qualifier**](/windows/previous-versions/Mi/ns-mi-_mi_qualifier?branch=master)
</dt> <dd>

Represents a CIM qualifier.

</dd> <dt>

[**MI\_QualifierDecl**](/windows/previous-versions/Mi/ns-mi-_mi_qualifierdecl?branch=master)
</dt> <dd>

Represents a CIM qualifier declaration.

</dd> <dt>

[**MI\_QualifierSet**](/windows/previous-versions/Mi/ns-mi-_mi_qualifierset?branch=master)
</dt> <dd>

Allows the developer to view the qualifiers of a class definition.

</dd> <dt>

[**MI\_QualifierSetFT**](/windows/previous-versions/Mi/ns-mi-_mi_qualifiersetft?branch=master)
</dt> <dd>

A support structure used in the [**MI\_QualifierSet**](/windows/previous-versions/Mi/ns-mi-_mi_qualifierset?branch=master) structure. Use the functions with the name prefix "MI\_QualifierSet\_" to manipulate these structures.

</dd> <dt>

[**MI\_Real32A**](/windows/previous-versions/Mi/ns-mi-_mi_real32a?branch=master)
</dt> <dd>

Represents an array of **MI\_Real32** types.

</dd> <dt>

[**MI\_Real32AField**](/windows/previous-versions/Mi/ns-mi-_mi_real32afield?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_Real32Field**](/windows/previous-versions/Mi/ns-mi-_mi_real32field?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_Real64A**](/windows/previous-versions/Mi/ns-mi-_mi_real64a?branch=master)
</dt> <dd>

Represents an array of **MI\_Real64** types.

</dd> <dt>

[**MI\_Real64AField**](/windows/previous-versions/Mi/ns-mi-_mi_real64afield?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_Real64Field**](/windows/previous-versions/Mi/ns-mi-_mi_real64field?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_ReferenceA**](/windows/previous-versions/Mi/ns-mi-_mi_referencea?branch=master)
</dt> <dd>

Represents an array of pointers to [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) types.

</dd> <dt>

[**MI\_ReferenceAField**](/windows/previous-versions/Mi/ns-mi-_mi_referenceafield?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_ReferenceField**](/windows/previous-versions/Mi/ns-mi-_mi_referencefield?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_SchemaDecl**](/windows/previous-versions/Mi/ns-mi-_mi_schemadecl?branch=master)
</dt> <dd>

Represents the schema objects in a CIM schema, which include CIM classes and CIM qualifier declarations.

</dd> <dt>

[**MI\_Serializer**](/windows/previous-versions/Mi/ns-mi-_mi_serializer?branch=master)
</dt> <dd>

An object tied to a specific serialization technique.

</dd> <dt>

[**MI\_SerializerFT**](/windows/previous-versions/Mi/ns-mi-_mi_serializerft?branch=master)
</dt> <dd>

A support structure used in the [**MI\_ClientFT\_V1**](/windows/previous-versions/Mi/ns-mi-_mi_clientft_v1?branch=master) structure. Use the functions with the name prefix "MI\_Serializer\_" to manipulate these structures.

</dd> <dt>

[**MI\_Server**](/windows/previous-versions/Mi/ns-mi-_mi_server?branch=master)
</dt> <dd>

This structure defines default function tables for all types: Context, Instance, PropertySet, and Filter.

</dd> <dt>

[**MI\_ServerFT**](/windows/previous-versions/Mi/ns-mi-_mi_serverft?branch=master)
</dt> <dd>

A support structure used in the [**MI\_Server**](/windows/previous-versions/Mi/ns-mi-_mi_server?branch=master) structure. Use the functions with the name prefix "MI\_Server\_" to manipulate these structures.

</dd> <dt>

[**MI\_Session**](/windows/previous-versions/Mi/ns-mi-_mi_session?branch=master)
</dt> <dd>

An object that is associated with a destination and has a set of credentials and options associated with it. .

</dd> <dt>

[**MI\_SessionFT**](/windows/previous-versions/mi/ns-mi-_mi_sessionft?branch=master)
</dt> <dd>

Function table for all actions on a session object.

</dd> <dt>

[**MI\_SessionCallbacks**](/windows/previous-versions/Mi/ns-mi-_mi_sessioncallbacks?branch=master)
</dt> <dd>

A container for callback function pointers that handle logging and error messages.

</dd> <dt>

[**MI\_Sint16A**](/windows/previous-versions/Mi/ns-mi-_mi_sint16a?branch=master)
</dt> <dd>

Represents an array of **MI\_Sint16** types.

</dd> <dt>

[**MI\_Sint16AField**](/windows/previous-versions/Mi/ns-mi-_mi_sint16afield?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_Sint16Field**](/windows/previous-versions/Mi/ns-mi-_mi_sint16field?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_Sint32A**](/windows/previous-versions/Mi/ns-mi-_mi_sint32a?branch=master)
</dt> <dd>

Represents an array of **MI\_Sint32** types.

</dd> <dt>

[**MI\_Sint32AField**](/windows/previous-versions/Mi/ns-mi-_mi_sint32afield?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_Sint32Field**](/windows/previous-versions/Mi/ns-mi-_mi_sint32field?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_Sint64A**](/windows/previous-versions/Mi/ns-mi-_mi_sint64a?branch=master)
</dt> <dd>

Represents an array of **MI\_Sint64** types.

</dd> <dt>

[**MI\_Sint64AField**](/windows/previous-versions/Mi/ns-mi-_mi_sint64afield?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_Sint64Field**](/windows/previous-versions/Mi/ns-mi-_mi_sint64field?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_Sint8A**](/windows/previous-versions/Mi/ns-mi-_mi_sint8a?branch=master)
</dt> <dd>

Represents an array of **MI\_Sint8** types.

</dd> <dt>

[**MI\_Sint8AField**](/windows/previous-versions/Mi/ns-mi-_mi_sint8afield?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_Sint8Field**](/windows/previous-versions/Mi/ns-mi-_mi_sint8field?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_StringA**](/windows/previous-versions/Mi/ns-mi-_mi_stringa?branch=master)
</dt> <dd>

Represents an array of pointers to null-terminated **MI\_Char**\* strings.

</dd> <dt>

[**MI\_StringAField**](/windows/previous-versions/Mi/ns-mi-_mi_stringafield?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_StringField**](/windows/previous-versions/Mi/ns-mi-_mi_stringfield?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptions**](/windows/previous-versions/Mi/ns-mi-_mi_subscriptiondeliveryoptions?branch=master)
</dt> <dd>

The subscription options object stores configuration options used for passing into subscription operations.

</dd> <dt>

[**MI\_SubscriptionDeliveryOptionsFT**](/windows/previous-versions/Mi/ns-mi-_mi_subscriptiondeliveryoptionsft?branch=master)
</dt> <dd>

A support structure used in the [**MI\_SubscriptionDeliveryOptions**](/windows/previous-versions/Mi/ns-mi-_mi_subscriptiondeliveryoptions?branch=master) structure. Use the functions with the name prefix "MI\_SubscriptionDeliveryOptions\_" to manipulate these structures.

</dd> <dt>

[**MI\_Timestamp**](/windows/previous-versions/Mi/ns-mi-_mi_timestamp?branch=master)
</dt> <dd>

[**MI\_Timestamp**](/windows/previous-versions/Mi/ns-mi-_mi_timestamp?branch=master) specifies a timestamp or a specific point in time.

</dd> <dt>

[**MI\_Uint16A**](/windows/previous-versions/Mi/ns-mi-_mi_uint16a?branch=master)
</dt> <dd>

Represents an array of **MI\_Uint16** types.

</dd> <dt>

[**MI\_Uint16AField**](/windows/previous-versions/Mi/ns-mi-_mi_uint16afield?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_Uint16Field**](/windows/previous-versions/Mi/ns-mi-_mi_uint16field?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_Uint32A**](/windows/previous-versions/Mi/ns-mi-_mi_uint32a?branch=master)
</dt> <dd>

Represents an array of **MI\_Uint32** types.

</dd> <dt>

[**MI\_Uint32AField**](/windows/previous-versions/Mi/ns-mi-_mi_uint32afield?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_Uint32Field**](/windows/previous-versions/Mi/ns-mi-_mi_uint32field?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_Uint64A**](/windows/previous-versions/Mi/ns-mi-_mi_uint64a?branch=master)
</dt> <dd>

Represents an array of **MI\_Uint64** types.

</dd> <dt>

[**MI\_Uint64AField**](/windows/previous-versions/Mi/ns-mi-_mi_uint64afield?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_Uint64Field**](/windows/previous-versions/Mi/ns-mi-_mi_uint64field?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_Uint8A**](/windows/previous-versions/Mi/ns-mi-_mi_uint8a?branch=master)
</dt> <dd>

Represents an array of **MI\_Uint8** types.

</dd> <dt>

[**MI\_Uint8AField**](/windows/previous-versions/Mi/ns-mi-_mi_uint8afield?branch=master)
</dt> <dd>

Represents a property inside an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) structure.

</dd> <dt>

[**MI\_Uint8Field**](/windows/previous-versions/Mi/ns-mi-_mi_uint8field?branch=master)
</dt> <dd>

Represents a property inside an MI\_Instance structure.

</dd> <dt>

[**MI\_UserCredentials**](/windows/previous-versions/Mi/ns-mi-_mi_usercredentials?branch=master)
</dt> <dd>

A user's credentials. It includes an authentication type and either a username and password or a certificate thumbprint.

</dd> <dt>

[**MI\_UsernamePasswordCreds**](/windows/previous-versions/Mi/ns-mi-_mi_usernamepasswordcreds?branch=master)
</dt> <dd>

A username/password combination used for subscription operations.

</dd> <dt>

[**MI\_UtilitiesFT**](/windows/previous-versions/Mi/ns-mi-_mi_utilitiesft?branch=master)
</dt> <dd>

A support structure used in the [**MI\_ClientFT\_V1**](/windows/previous-versions/Mi/ns-mi-_mi_clientft_v1?branch=master) structure. Use the functions with the name prefix "MI\_Utilities\_" to manipulate these structures.

</dd> <dt>

[**MI\_Value**](/windows/previous-versions/mi/ns-mi-_mi_value?branch=master)
</dt> <dd>

A union of all CIM data types.

</dd> </dl>

 

 




