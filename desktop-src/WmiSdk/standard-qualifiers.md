---
description: All CIM-compliant implementations must handle a standard set of qualifiers.
ms.assetid: 671ea769-f68d-4788-96f5-c4f86ab3b00e
ms.tgt_platform: multiple
title: Standard Qualifiers
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Standard
api_type: 
- NA
api_location: 
---

# Standard Qualifiers

All CIM-compliant implementations must handle a standard set of qualifiers. Any specific object does not have all of the qualifiers listed. Usually, extension classes supply additional qualifiers to facilitate provision of class instances and other operations on the class.

It is the responsibility of the provider to enforce the qualifiers. WMI does not enforce qualifiers, but uses them only to inform the user about how the property is used.

> [!Note]  
> WMI is compliant with the CIM 2.5 specification.

 

Qualifiers have the following limitations:

-   Not all standard qualifiers can be used together.
-   Not all qualifiers can be applied to all constructs, such as association or reference. These limitations are identified in the Applies to list.
-   For a particular construct, such as association or reference, the use of the legal qualifiers can be further constrained because some qualifiers are mutually exclusive, the use of one qualifier may imply some restrictions on the value of another, and so on. These usage rules are documented.
-   Legal qualifiers are inherited by entities such as properties, methods, instances, or subclasses only, not by associations or references. For example, the **MaxLen** qualifier that applies to properties is not inherited by references.

The following lists WMI standard qualifiers.

<dt>

<span id="Abstract"></span><span id="abstract"></span><span id="ABSTRACT"></span>**Abstract**
</dt> <dd>

Data type: **boolean**

Applies to: classes, associations, indications

Indicates whether the class is abstract and serves only as a base for new classes. The default is **FALSE**. You cannot create instances of abstract classes. The absence of this qualifier indicates that the class is not abstract; therefore, this qualifier is required for all abstract classes.

</dd> <dt>

<span id="Aggregate"></span><span id="aggregate"></span><span id="AGGREGATE"></span>**Aggregate**
</dt> <dd>

Data type: **boolean**

Applies to: references

Indicates whether the reference is the parent component of an aggregation association. The default is **FALSE**.

Usage: The **Aggregation** and **Aggregate** qualifiers are used together   **Aggregation** qualifies the association, and **Aggregate** specifies the parent reference.

</dd> <dt>

<span id="Aggregation"></span><span id="aggregation"></span><span id="AGGREGATION"></span>**Aggregation**
</dt> <dd>

Data type: **boolean**

Applies to: associations

Indicates whether the association is an aggregation. The default is **FALSE**. Used with **Aggregate**. This qualifier is required for all aggregation associations.

</dd> <dt>

<span id="Alias"></span><span id="alias"></span><span id="ALIAS"></span>**Alias**
</dt> <dd>

Data type: **string**

Applies to: properties, references, methods

Alternate name for a property or method in the schema. The default is **NULL**.

</dd> <dt>

<span id="ArrayType"></span><span id="arraytype"></span><span id="ARRAYTYPE"></span>**ArrayType**
</dt> <dd>

Data type: **string**

Applies to: properties, parameters

Type of the qualified array.

Valid values are:

-   bag (default)
-   indexed
-   ordered

Usage: Apply this type of qualifier only to properties and parameters that are arrays (defined by using bracket syntax).

</dd> <dt>

<span id="BitMap"></span><span id="bitmap"></span><span id="BITMAP"></span>**BitMap**
</dt> <dd>

Data type: **string array**

Applies to: properties, methods, parameters

Map of significant bit positions where each significant position can be "on" or "off". Each "on" bit maps to a corresponding value in the **BitValues** array. By having multiple bits "on", multiple concurrent values in the **BitValues** array are indicated. The default is **NULL**.

For more information, see [BitMap and BitValues](bitmap-and-bitvalues.md).

</dd> <dt>

<span id="BitValues"></span><span id="bitvalues"></span><span id="BITVALUES"></span>**BitValues**
</dt> <dd>

Data type: **string array**

Applies to: properties, methods, parameters

Translation of a bit position value into an associated **string**. The default is **NULL**.

For more information, see [BitMap and BitValues](bitmap-and-bitvalues.md).

</dd> <dt>

<span id="Constructor"></span><span id="constructor"></span><span id="CONSTRUCTOR"></span>**Constructor**
</dt> <dd>

Data type: **boolean**

Applies to: methods

Indicates whether the method creates instances. These methods are not constrained to acting on a single instance or a single class. For example, a constructor can create association instances as well as instances of the class that defines the constructor.

The **Constructor** qualifier is intended for information only and it is not expected that it is acted on by the object manager. The object manager does not have to call constructor methods when an object is created. Also when a constructor is called, the object manager does not have to invoke any constructor methods defined for any parent class of the original class. The default is **FALSE**.

</dd> <dt>

<span id="CreateBy"></span><span id="createby"></span><span id="CREATEBY"></span>**CreateBy**
</dt> <dd>

Data type: **string**

Applies to: classes

Name of the method by which instances of this class are created. The value is either "PutInstance" or the name of another method that creates the instances. The default is **NULL**.

Usage: This qualifier can only be used if the **SupportsCreate** qualifier is present.

</dd> <dt>

<span id="DeleteBy"></span><span id="deleteby"></span><span id="DELETEBY"></span>**DeleteBy**
</dt> <dd>

Data type: **string**

Applies to: classes

Name of the method by which instances of this class are deleted. The value is either "DeleteInstance", or the name of another method that deletes the instances. The default is **NULL**.

Usage: This qualifier can only be used if the **SupportsDelete** qualifier is present.

</dd> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Data type: **string**

Applies to: any

Description of a named element. The default is **NULL**.

</dd> <dt>

<span id="Destructor"></span><span id="destructor"></span><span id="DESTRUCTOR"></span>**Destructor**
</dt> <dd>

Data type: **boolean**

Applies to: methods

Indicates whether the method deletes instances. Methods using the **Destructor** qualifier delete the instance(s) to which the destructor is applied, and are not constrained to acting on a single instance or class. For example, a destructor might delete association instances as well as instances of the class that defines the destructor.

The **Destructor** qualifier is intended for information only and it is not expected that it is acted on by the object manager. There is no obligation for the object manager to call a method that has the **Destructor** qualifier when an instance is deleted. Also, when a destructor is called, the object manager does not have to invoke any destructor methods defined for any parent class of the original class. The default is **FALSE**.

</dd> <dt>

<span id="DisplayName"></span><span id="displayname"></span><span id="DISPLAYNAME"></span>**DisplayName**
</dt> <dd>

Data type: **string**

Applies to: any

Name displayed in the UI instead of the actual name of the element. The default is **NULL**.

</dd> <dt>

<span id="EmbeddedInstance"></span><span id="embeddedinstance"></span><span id="EMBEDDEDINSTANCE"></span>**EmbeddedInstance**
</dt> <dd>

Data type: **string**

Applies to: any

The qualified string type element contains an embedded instance. The qualifier value specifies the name of a CIM class in the same namespace as the class owning the qualified element. The embedded instance is an instance of the specified class, including instances of its subclasses. The default is **NULL**.

</dd> <dt>

<span id="Gauge"></span><span id="gauge"></span><span id="GAUGE"></span>**Gauge**
</dt> <dd>

Data type: **boolean**

Applies to: any

Indicates whether the property represents a non-negative integer, which can increase or decrease, but never exceed a maximum value. The default is **FALSE**.

The maximum value of the property cannot be greater than 2^*n* - 1. *N* can be 8, 16, 32, or 64 depending on the data type of the property to which this qualifier is applied. The value of a gauge has its maximum value whenever the information being modeled is greater or equal to that maximum value. If the information being modeled subsequently decreases below the maximum value, the gauge also decreases. This qualifier is applicable only to properties with an unsigned integer data type.

</dd> <dt>

<span id="In"></span><span id="in"></span><span id="IN"></span>**In**
</dt> <dd>

Data type: **boolean**

Applies to: parameters

Indicates whether the parameter is used to pass values to a method. The default is **TRUE**.

</dd> <dt>

<span id="In__Out"></span><span id="in__out"></span><span id="IN__OUT"></span>**In, Out**
</dt> <dd>

Data type: **boolean**

Applies to: parameters

Indicates whether the parameter is both an input and output parameter.

</dd> <dt>

<span id="Key"></span><span id="key"></span><span id="KEY"></span>[**Key**](key-qualifier.md)
</dt> <dd>

Data type: **boolean**

Applies to: properties, references

Indicates whether the property is part of the namespace handle. If more than one property has the [**Key**](key-qualifier.md) qualifier, then all such properties collectively form the key (a compound key). When taken together, the key properties must supply a unique reference for each class instance. If this qualifier is placed on a property, only the value **TRUE** is allowed.

</dd> <dt>

<span id="Lazy"></span><span id="lazy"></span><span id="LAZY"></span>**Lazy**
</dt> <dd>

Applies to: properties

Indicates that the property is resource-intensive to return and requires a lot of processor time and memory. WMI improves the performance of queries by not attempting to return the properties marked with the **Lazy** qualifier.

</dd> <dt>

<span id="MappingStrings"></span><span id="mappingstrings"></span><span id="MAPPINGSTRINGS"></span>**MappingStrings**
</dt> <dd>

Data type: **string array**

Applies to: classes, properties, associations, indications, references

Set of values that indicate a path to a location where you can find more information about the origin of a property, class, association, indication, or reference. The mapping string can be a directory path, a URL, a registry key, an include file, reference to a CIM class, or some other format. The default is **NULL**.

</dd> <dt>

<span id="Max"></span><span id="max"></span><span id="MAX"></span>**Max**
</dt> <dd>

Data type: **int**

Applies to: references

Maximum number of values a given reference can have for each set of other reference values in the association. The default is **NULL**. For example, if an association relates A instances to B instances and there must be at most one A instance for each B instance, then the reference to A should have a maximum of one qualifier.

</dd> <dt>

<span id="MaxLen"></span><span id="maxlen"></span><span id="MAXLEN"></span>**MaxLen**
</dt> <dd>

Data type: **int**

Applies to: properties, methods, parameters

Maximum length (in characters) of a **string** data item and indicates support of fixed-length arrays.

If a fixed-length array is encountered, the **MaxLen** qualifier contains the fixed length found during parsing. If a variable-length array is encountered, then this qualifier is not used. **MaxLen** is used to suggest the maximum number of elements that should be stored in an array. When overriding the default value, any unsigned integer value (**uint32**) can be specified. A value of **NULL** (default) implies unlimited length.

</dd> <dt>

<span id="MaxValue"></span><span id="maxvalue"></span><span id="MAXVALUE"></span>**MaxValue**
</dt> <dd>

Data type: **int**

Applies to: properties, methods, parameters

Maximum value of the object. The default is **NULL**.

</dd> <dt>

<span id="Min"></span><span id="min"></span><span id="MIN"></span>**Min**
</dt> <dd>

Data type: **int**

Applies to: references

Minimum cardinality of the reference (the minimum number of values a given reference can have for each set of other reference values in the association). The default is 0.

For example, if an association relates A instances to B instances, and there must be at least one A instance for each B instance, then the reference to A should have a minimum of one qualifier.

</dd> <dt>

<span id="MinValue"></span><span id="minvalue"></span><span id="MINVALUE"></span>**MinValue**
</dt> <dd>

Data type: **int**

Applies to: properties, methods, parameters

Indicates the minimum value of the object. The default is **NULL**.

</dd> <dt>

<span id="ModelCorrespondence"></span><span id="modelcorrespondence"></span><span id="MODELCORRESPONDENCE"></span>**ModelCorrespondence**
</dt> <dd>

Data type: **string array**

Applies to: properties

Set of values that indicate correspondence between an object's property and other properties in the CIM schema. The default is **NULL**.

Object properties are identified using the following syntax.

<schema name> "\_" <class or association name> "." <property name>

</dd> <dt>

<span id="Nonlocal"></span><span id="nonlocal"></span><span id="NONLOCAL"></span>**Nonlocal**
</dt> <dd>

Data type: **string**

Applies to: references

Location of an instance, the value of which is <*namespacetype*>://<*namespacehandle*> The default is **NULL**.

Usage: This qualifier cannot be used with the **NonlocalType** qualifier.

</dd> <dt>

<span id="NonlocalType"></span><span id="nonlocaltype"></span><span id="NONLOCALTYPE"></span>**NonlocalType**
</dt> <dd>

Data type: **string**

Applies to: references

Type of location of an instance. Its value is &lt;namespacetype&gt;. The default is **NULL**.

Usage: This qualifier cannot be used with the **Nonlocal** qualifier.

</dd> <dt>

<span id="NullValue"></span><span id="nullvalue"></span><span id="NULLVALUE"></span>**NullValue**
</dt> <dd>

Data type: **string**

Applies to: properties

Value that indicates that the associated property is **NULL** (the property does not have a valid or meaningful value). The default is **NULL**.

The conventions and restrictions used for defining **NULL** values are the same as those applicable to the **ValueMap** qualifier. Note this qualifier cannot be overridden. It is unreasonable to permit a subclass to return a different **NULL** value than that of the parent class.

</dd> <dt>

<span id="Out"></span><span id="out"></span><span id="OUT"></span>**Out**
</dt> <dd>

Data type: **boolean**

Applies to: parameters

Indicates whether the parameter returns values from a method. The default is **FALSE**.

</dd> <dt>

<span id="Override"></span><span id="override"></span><span id="OVERRIDE"></span>**Override**
</dt> <dd>

Data type: **string**

Applies to: properties, methods, references

Parent class or subordinate construct (property, method, or reference) which is overridden by the property, method, or reference of the same name in the derived class. The default is **NULL**.

The format is:

\[<*class*>.\]<*subordinate construct*>

If the class name is omitted, the override applies to the subordinate construct in the parent class in the class hierarchy.

Usage: The **Override** qualifier can refer to constructs based on the same meta model only. It is not allowed to change a construct name or signature during an override operation.

</dd> <dt>

<span id="OverrideValue"></span><span id="overridevalue"></span><span id="OVERRIDEVALUE"></span>**OverrideValue**
</dt> <dd>

Applies to: classes

Indicates whether the property value on a subclass overrides the value in a parent class. The functional implication is that, if you perform a query against the parent class, and if your **WHERE** clause includes this property, the parent must return an instance with the overridden value. As a result, Windows Management adjusts the **WHERE** clause of the query sent to the parent class to exclude references to this property.

</dd> <dt>

<span id="Propagated"></span><span id="propagated"></span><span id="PROPAGATED"></span>**Propagated**
</dt> <dd>

Data type: **string**

Applies to: properties

Name of the key being propagated. The default is **NULL**.

Use of this qualifier assumes the existence of only one weak qualifier on a reference that has the containing class as its target. The associated property must have the same value as the property named by the qualifier in the class on the other side of the weak association. The format is:

\[<*class*>.\]<*subordinate construct*>

Usage: When the **Propagated** qualifier is used, the [**Key**](key-qualifier.md) qualifier must be specified with a value of **TRUE**.

</dd> <dt>

<span id="Read"></span><span id="read"></span><span id="READ"></span>**Read**
</dt> <dd>

Data type: **boolean**

Applies to: properties

Indicates whether the property is readable. The default is **TRUE**.

</dd> <dt>

<span id="Required"></span><span id="required"></span><span id="REQUIRED"></span>**Required**
</dt> <dd>

Data type: **boolean**

Applies to: properties

Indicates whether a non-null value is required for the property. The default is **FALSE**.

</dd> <dt>

<span id="Revision"></span><span id="revision"></span><span id="REVISION"></span>**Revision**
</dt> <dd>

Data type: **string**

Applies to: classes, associations, indications, schemas

Minor revision number of the schema object. The default is **NULL**.

Usage: The **Version** qualifier must be present to supply the major version number when the **Revision** qualifier is used.

</dd> <dt>

<span id="Schema"></span><span id="schema"></span><span id="SCHEMA"></span>**Schema**
</dt> <dd>

Data type: **string**

Applies to: properties, methods

Name of the schema in which the feature is defined. The default is **NULL**.

</dd> <dt>

<span id="Source"></span><span id="source"></span><span id="SOURCE"></span>**Source**
</dt> <dd>

Data type: **string**

Applies to: classes, associations, indications, references

Location of an instance. The default is **NULL**.

The qualifier's value is <*namespacetype*>://<*namespacehandle*>.

Usage: The **Source** qualifier cannot be used with the **SourceType** qualifier.

</dd> <dt>

<span id="SourceType"></span><span id="sourcetype"></span><span id="SOURCETYPE"></span>**SourceType**
</dt> <dd>

Data type: **string**

Applies to: classes, associations, indications, references

Type of location of an instance. The value of this qualifier is <*namespacetype*>. The default is **NULL**.

Usage: The **SourceType** qualifier cannot be used with the **Source** qualifier.

</dd> <dt>

<span id="SupportsCreate"></span><span id="supportscreate"></span><span id="SUPPORTSCREATE"></span>**SupportsCreate**
</dt> <dd>

Data type: **boolean**

Applies to: classes

Indicates whether the class supports the creation of instances. The default is **FALSE**.

</dd> <dt>

<span id="SupportsDelete"></span><span id="supportsdelete"></span><span id="SUPPORTSDELETE"></span>**SupportsDelete**
</dt> <dd>

Data type: **boolean**

Applies to: classes

Indicates whether the class supports the deletion of instances. The default is **FALSE**.

</dd> <dt>

<span id="SupportsUpdate"></span><span id="supportsupdate"></span><span id="SUPPORTSUPDATE"></span>**SupportsUpdate**
</dt> <dd>

Data type: **boolean**

Applies to: classes

Indicates whether the class supports the modification (updating) of instances. The default is **FALSE**.

</dd> <dt>

<span id="Terminal"></span><span id="terminal"></span><span id="TERMINAL"></span>**Terminal**
</dt> <dd>

Data type: **boolean**

Applies to: classes

Indicates whether the class can have subclasses. The default is **FALSE**.

If a subclass is declared, the compiler generates an error.

Usage: This qualifier cannot coexist with the **Abstract** qualifier. If both the **Terminal** and **Abstract** qualifiers are specified, the compiler generates an error.

</dd> <dt>

<span id="Units"></span><span id="units"></span><span id="UNITS"></span>**Units**
</dt> <dd>

Data type: **string**

Applies to: properties, methods, parameters

Type of unit in which the associated data item is expressed. The default is **NULL**.

For example, a size data item might have a value of "bytes" for **Units**.

</dd> <dt>

<span id="ValueMap"></span><span id="valuemap"></span><span id="VALUEMAP"></span>**ValueMap**
</dt> <dd>

Data type: **string array**

Applies to: properties, methods, parameters

Set of permissible values for a property, method return type, or method parameter. The default is **NULL**.

Usage: This qualifier can be used alone or in combination with the **Values** qualifier. When used in combination with the **Values** qualifier, the location of the value in the **ValueMap** array provides the location of the corresponding entry in the **Values** array. Use the **ValueMap** qualifier only with string and integer values. The syntax for representing an integer value in the value map array is \[+\|=\]digit\[\*digit\]. The content, maximum number of digits, and represented value are constrained by the type of the associated property. For example, uint8 may not be signed, must be less than four digits, and must represent a value less than 256.

</dd> <dt>

<span id="Values"></span><span id="values"></span><span id="VALUES"></span>**Values**
</dt> <dd>

Data type: **string array**

Applies to: properties, methods, parameters

Set of values translating an integer value into an associated string. The default is **NULL**.

This property also specifies an array of string values to be mapped to an enumeration property. This qualifier can be applied to either an integer property or a string property, and the mapping can be implicit or explicit. If the mapping is implicit, integer or string property values represent ordinal positions in the **Values** array. If the mapping is explicit, the property must be an integer, and valid property values are listed in the array defined by the **ValueMap** qualifier. For more information, see [Value Map](value-map.md).

If a **ValueMap** qualifier is not present, the **Values** array is indexed (zero-relative) by using the value in the associated property, method return type, or method parameter. If a **ValueMap** qualifier is present, the values index is defined by the location of the property value in the value map.

</dd> <dt>

<span id="Version"></span><span id="version"></span><span id="VERSION"></span>**Version**
</dt> <dd>

Data type: **string**

Applies to: classes, schemas, associations, indications

Major version number of the schema object. The default is **NULL**. The version number is incremented when changes are made to the schema that alter the interface.

</dd> <dt>

<span id="Weak"></span><span id="weak"></span><span id="WEAK"></span>**Weak**
</dt> <dd>

Data type: **boolean**

Applies to: references

Indicates whether the keys of the referenced class include the keys of the other participants in the association. The default is **FALSE**.

This qualifier is used when the identity of the referenced class depends on the identity of the other participants in the association. No more than one reference to any given class can be weak. The other classes in the association must define a key. The keys of the other classes in the association are repeated in the referenced class and are tagged with a **Propagated** qualifier.

</dd> <dt>

<span id="Write"></span><span id="write"></span><span id="WRITE"></span>**Write**
</dt> <dd>

Data type: **boolean**

Applies to: properties

Indicates that applications or scripts can change the property value. The account that runs the application must have access to the namespace that contains instances of the class. The provider implementation may also limit access to provider data. A value of **TRUE** indicates that the property is readable and writeable by consumers that are allowed access by WMI and the provider. The default is **FALSE**.

A property that lacks the **Write** qualifier may still be writeable. The provider implementation may allow any properties in the provider classes to be changed, whether the **Write** qualifier is present.

</dd> <dt>

<span id="WriteAtCreate"></span><span id="writeatcreate"></span><span id="WRITEATCREATE"></span>**WriteAtCreate**
</dt> <dd>

Data type: **boolean**

Applies to: properties

Indicates whether the property is writeable at instance creation. This qualifier may be used in conjunction with the **WriteAtCreate** qualifier. The default is **FALSE**.

</dd> <dt>

<span id="WriteAtUpdate"></span><span id="writeatupdate"></span><span id="WRITEATUPDATE"></span>**WriteAtUpdate**
</dt> <dd>

Data type: **boolean**

Applies to: properties

Indicates whether the property is writeable at instance update. This qualifier may be used in conjunction with the **WriteAtCreate** qualifier. The default is **FALSE**.

</dd> </dl>

## Examples

For more information on retrieving qualifiers, see the [Get-WmiClassMethodsAndWritableWmiProperties](https://Gallery.TechNet.Microsoft.Com/10670e14-4cf1-4ce5-99d0-fc4ca80dac2c) PowerShell code sample on the TechNet Gallery.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |



## See also

<dl> <dt>

[WMI Qualifiers](wmi-qualifiers.md)
</dt> <dt>

[Adding a Qualifier](adding-a-qualifier.md)
</dt> </dl>

 

 




