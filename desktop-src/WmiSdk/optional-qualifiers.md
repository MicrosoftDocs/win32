---
description: Optional qualifiers address recurring situations not common to all CIM-compliant implementations, which are not required to interpret these qualifiers.
ms.assetid: f31162d1-25e6-494a-bc7d-f66955b514a6
ms.tgt_platform: multiple
title: Optional Qualifiers
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Optional
api_type: 
- NA
api_location: 
---

# Optional Qualifiers

Optional qualifiers address recurring situations not common to all CIM-compliant implementations, which are not required to interpret these qualifiers. Optional qualifiers are provided in the specification to avoid random user-defined qualifiers that might occur in these recurring situations.

<dt>

<span id="Delete"></span><span id="delete"></span><span id="DELETE"></span>**Delete**
</dt> <dd>

Data type: **boolean**

Applies to: associations, references

For associations, indicates whether the qualified association must be deleted if any of the objects referenced in the association are deleted and if the respective object referenced in the association is qualified with **IfDeleted**. The default is **FALSE**.

For references, this qualifier indicates whether the referenced object must be deleted if the association containing the reference is deleted and qualified with **IfDeleted**, or if any of the objects referenced in the association are deleted and the respective object referenced in the association is qualified with **IfDeleted**.

Usage: Applications must track associations and references marked with the **Delete** qualifier and delete the association or reference appropriately. If an object in the association has been deleted but is not marked with **IfDeleted**, then the association should not be deleted.

This usage rule must be verified when the CIM security model is defined.

</dd> <dt>

<span id="Expensive"></span><span id="expensive"></span><span id="EXPENSIVE"></span>**Expensive**
</dt> <dd>

Data type: **boolean**

Applies to: properties, references, classes, associations, methods

Indicates whether the implied action requires extensive computation. The default is **FALSE**.

</dd> <dt>

<span id="IfDeleted"></span><span id="ifdeleted"></span><span id="IFDELETED"></span>**IfDeleted**
</dt> <dd>

Data type: **boolean**

Applies to: associations and references

Indicates whether all objects within an association that is qualified by **Delete** must be deleted if the referenced object or the association is deleted. The default is **FALSE**.

</dd> <dt>

<span id="Indexed"></span><span id="indexed"></span><span id="INDEXED"></span>**Indexed**
</dt> <dd>

Data type: **boolean**

Applies to: properties, methods

Indicates whether a class property should be indexed. When applied to properties in classes hosted by the repository, this only has the meaning of creating (at the time of class creation) a fast secondary query lookup for that property.

Only the value **TRUE** (default) is allowed.

</dd> <dt>

<span id="Invisible"></span><span id="invisible"></span><span id="INVISIBLE"></span>**Invisible**
</dt> <dd>

Data type: **boolean**

Applies to: associations, properties, methods, references, classes

Indicates whether the association is defined only for internal purposes (for example, for definition of dependency semantics) and should not be displayed (for example, in maps). The default is **FALSE**.

</dd> <dt>

<span id="Large"></span><span id="large"></span><span id="LARGE"></span>**Large**
</dt> <dd>

Data type: **boolean**

Applies to: properties, classes

Indicates whether the property or class requires a large amount of storage space. The default is **FALSE**.

</dd> <dt>

<span id="Not_Null"></span><span id="not_null"></span><span id="NOT_NULL"></span>**Not\_Null**
</dt> <dd>

Data type: **boolean**

Applies to: properties

Indicates whether a class property cannot take on a value of **NULL** (**VT\_NULL**). Only the value **TRUE** (default) is allowed.

If this qualifier is specified, WMI does not allow creation of instances with the property set to **NULL**, and **NULL** properties return the **WBEM\_E\_ILLEGAL\_NULL** error code.

Note that the [**Key**](standard-qualifiers.md) and **Indexed** qualifiers already imply this behavior.

</dd> <dt>

<span id="Provider"></span><span id="provider"></span><span id="PROVIDER"></span>**Provider**
</dt> <dd>

Data type: **string**

Applies to: Any

Indication that the schema element is dynamic and thus populated by a provider. The default is **NULL**. This qualifier is an implementation-specific handle to the instrumentation.

</dd> <dt>

<span id="Experimental"></span><span id="experimental"></span><span id="EXPERIMENTAL"></span>**Experimental**
</dt> <dd>

Data type: **boolean**

Applies to: any

Indicates that the specified element has been proposed to be a part of a future release of the CIM Schemas, but is not yet part of the standard Schema. Instead, the element is available for users to experiment, implement, and provide feedback on. Based on feedback, the element may added to the standard as presented, modified, or removed. The default is **FALSE**. An implementation does not have to support an element with this qualifier.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

Data type: **string**

Applies to: properties, references, methods, parameters

Specific type assigned to a data item. The default is **NULL**.

Usage: You must use the **SyntaxType** qualifier with this qualifier.

</dd> <dt>

<span id="SyntaxType"></span><span id="syntaxtype"></span><span id="SYNTAXTYPE"></span>**SyntaxType**
</dt> <dd>

Data type: **string**

Applies to: properties, references, methods, parameters

Format of the **Syntax** qualifier. The default is **NULL**.

Usage: You must use the **Syntax** qualifier with this qualifier.

</dd> <dt>

<span id="TriggerType"></span><span id="triggertype"></span><span id="TRIGGERTYPE"></span>**TriggerType**
</dt> <dd>

Data type: **string**

Applies to: classes, properties, methods, associations, indications, references

Circumstances under which a trigger is fired. The default is **NULL**. The trigger types vary by meta-model construct.

For classes and associations, the legal values are:

Create

Delete

Update

Access

For properties and references, the legal values are: Update and Access.

For methods, the legal values are Before and After.

For indications, the legal value is Thrown.

</dd> <dt>

<span id="UnknownValues"></span><span id="unknownvalues"></span><span id="UNKNOWNVALUES"></span>**UnknownValues**
</dt> <dd>

Data type: **string array**

Applies to: properties

Set of values indicating that the value of the associated property is unknown (the property cannot be considered as having a valid or meaningful value). The default is **NULL**.

The conventions and restrictions used for defining unknown values are the same as those applicable to the [**ValueMap**](standard-qualifiers.md) qualifier.

Note that this qualifier cannot be overridden. It is unreasonable to permit a subclass to treat a value as a known value when it is treated as unknown by some parent class.

</dd> <dt>

<span id="UnsupportedValues"></span><span id="unsupportedvalues"></span><span id="UNSUPPORTEDVALUES"></span>**UnsupportedValues**
</dt> <dd>

Data type: **string array**

Applies to: properties

Set of values indicating that the value of the associated property is unsupported (the property cannot be considered as having a valid or meaningful value). The default is **NULL**.

The conventions and restrictions used for defining unsupported values are the same as those applicable to the [**ValueMap**](standard-qualifiers.md) qualifier.

Note this qualifier cannot be overridden. It is unreasonable to permit a subclass to treat a value as a supported value that is treated as unknown by some parent class.

</dd> </dl>

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

 

 




