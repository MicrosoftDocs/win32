---
description: Learn about the Value element, which associates a literal with a type. The data type of Value must be string, integer, decimal, or QName. 
ms.assetid: 933528f6-8f34-4509-887c-c7c223c79367
title: Value
ms.topic: article
ms.date: 05/31/2018
---

# Value

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

A Value element associates a literal with a type.

## Element Tag

&lt;Value&gt;

## XML Attributes

The following table lists the XML attributes that may be pertain to this element.



| XML Attribute       | Details                                                                                                                                                                          |
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| xsi:type<br/> | Specifies the data type of Value, which must be one of the following XSD-defined types: string, integer, decimal, QName. If missing, the default data type is string.<br/> |



 

For more information, please see [XML Attributes](xml-attributes.md) section.

## Element Information

The following table lists the elements that may be parents of this element, the elements that may be children of this element, and any restrictions on the element itself.



| Category                   | Details                                                                                                                                                   |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Parent elements<br/> | ParameterInit <br/> Property<br/> ScoredProperty<br/>                                                                                   |
| Child elements<br/>  | Only character or integer content is permitted.<br/>                                                                                                |
| This element<br/>    | Null content is allowed. Character content must conform to syntax defined by data type.<br/> Duplicate child siblings are not permitted.<br/> |



 

## Configuration Dependencies

Value elements that appear within ScoredProperty element may not have any configuration dependencies. Value elements that appear within Property elements may have arbitrary dependencies on the configuration.

## Element Usage

A Value element may appear within a Property or ScoredProperty element. The purpose of the Value element is to represent a value as a standard XML data type. The data type is specified as an XML attribute of the Value element, xsi:type. Note that not all XSD-defined or XML-defined types are supported. For a list of supported types, see [Summary of Element Types](summary-of-element-types.md). A Value element can contain only character content. Nothing else may appear as content in a Value element.

> [!Note]  
> Some Print Schema-defined Property and ScoredProperty elements do not contain a Value element, because their purpose is simply to be parents of subproperties. You should not add a Value element to such properties as these, properties that do not contain a Value element.

 

To conform to the Print Schema Framework, which requires either a Value element or subelements be present in the elements that support values, an absent or undefined value should be represented by presenting the Value element as an empty element; that is, as &lt;Value&gt;&lt;/Value&gt;.

## Example

Define a Value of type decimal and initialize it to "128.5".

``` syntax
<Value xsi:type="decimal">128.5</Value>
```

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 




