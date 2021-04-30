---
description: This topic is not current. For current information, see the Print Schema Specification.
ms.assetid: f1c73aed-fca4-47f6-bb98-bab40a6a9b2e
title: ParameterDef and ParameterInit Elements
ms.topic: article
ms.date: 05/31/2018
---

# ParameterDef and ParameterInit Elements

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

A ParameterDef element differs from a ParameterInit element in that it describes the value that a ParameterInit element can contain, while a ParameterInit element assigns a value to the parameter. A ParameterDef element consists of a specific set of Property elements, which are children of the ParameterDef element, that specify the type of data, maximum, minimum, and default values for the data, and other information. These Property elements are discussed later in this topic.

ParameterDef elements can appear only in their allowed context. For the initial version of the Print Schema they may be located at the root level of the PrintCapabilities document. The name attribute of the ParameterDef element defines the parameter name. Each ParameterDef element in the PrintCapabilities document must be assigned a unique name attribute.

> [!Note]
> to Print Capabilities Document Providers:
> 
> The meaning of a parameter name is universal; that is, if a ParameterDef element in one PrintCapabilities document has the same name attribute (the string formed from the namespace and the descriptive name of the ParameterDef element) as a ParameterDef element in another PrintCapabilities document, it is assumed that both of these elements represent the same concept and should be interpreted in the same manner. Thus a ParameterDef element defined in a PrintTicket for one PrintCapabilities document can be used to initialize the ParameterInit element of the same name defined in a different PrintCapabilities document.

 

## Relationship to XML Attributes

As is true of all name attributes, the parameter name is in the form of an XML QName. A Schema-defined parameter construct has a name that is qualified by the public namespace, forming the name attribute, while the name attribute of a privately-defined parameter construct is qualified by a private namespace that is unique to the creator.

## Relationship between ParameterDef and Property Element Types

ParameterDef elements that are defined in the Print Schema Keywords must be fully defined in a PrintCapabilities document. The Print Schema Keywords document provides nominal values for some Property elements of a ParameterDef element (such as DefaultValue and others), but the author of a PrintCapabilities document is responsible for defining the remaining Property elements. In any case, all Property elements must be explicitly defined in a ParameterDef element, including those that are defined in the Print Schema Keywords.

Certain Property elements of each ParameterDef element appearing in the Print Schema Keywords are designated as *immutable*. This means that all PrintCapabilities document definitions of Print Schema Keywords-defined ParameterDef elements must preserve these Property elements without modification. These immutable Property elements allow the parameter constructs to be portable and unambiguous across all PrintCapabilities documents. A prime example is the units used in a ParameterDef element. These units should be immutable, to promote a consistent understanding of their meaning. Property elements of a ParameterDef that are designated as not immutable may be redefined within a PrintCapabilities document.

A ParameterDef element is composed of the following Property elements. All must be present unless otherwise noted.



<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Property Name</th>
<th>Values</th>
<th>Description</th>
<th>Immutable?</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DataType <br/></td>
<td>integer <br/> decimal<br/> string<br/> No default value.<br/></td>
<td>Specifies whether the parameter value is an integer, or floating point number, or a text string. The value of a parameter is expressed in the same format as the corresponding XSD basic data type; that is, as an integer, decimal, or string. <br/></td>
<td>Yes<br/></td>
</tr>
<tr class="even">
<td>DefaultValue <br/></td>
<td>The type specified by the DataType Property.<br/> No default value.<br/></td>
<td>Specifies the value with which to initialize a user interface (UI) control.<br/>
<ul>
<li>or <br/></li>
</ul>
Specifies the value to use if the relevant parameter element is missing from the PrintTicket.<br/></td>
<td>No<br/></td>
</tr>
<tr class="odd">
<td>Mandatory <br/></td>
<td>Unconditional: the ParameterInit element must always be supplied. <br/> Conditional: the ParameterInit element is required only if the parameter is referenced within an Option element in a PrintTicket.<br/> DefaultValue: Conditional.<br/></td>
<td>Indicates when a ParameterInit element must appear explicitly. If Conditional, the ParameterInit must be initialized if the PrintTicket contains an Option that references the parameter.<br/> Used by UI Clients and PrintCapabilities or PrintTicket providers. Note that in any constraint, the Mandatory Property of the ParameterDef element must be set to Unconditional. The ParameterDef must have a defined Value, otherwise the dependent Value or constraint could not be evaluated.<br/></td>
<td>No<br/></td>
</tr>
<tr class="even">
<td>MaxLength <br/></td>
<td>integer if DataType Property specifies string.<br/> DefaultValue: No maximum value is enforced.<br/></td>
<td>For string-valued parameters, specifies the longest allowed string. UI and PrintCapabilities or PrintTicket providers use this Property to validate the ParameterDef element.<br/></td>
<td>No<br/></td>
</tr>
<tr class="odd">
<td>MaxValue <br/></td>
<td>integer if DataType Property specifies integer.<br/> decimal if DataType Property specifies decimal.<br/> DefaultValue: No maximum value is enforced.<br/></td>
<td>For integer-or decimal-valued ParameterDef elements, defines the largest allowed value.<br/></td>
<td>No<br/></td>
</tr>
<tr class="even">
<td>MinLength <br/></td>
<td>integer if DataType Property specifies string. <br/> DefaultValue: No minimum value is enforced.<br/></td>
<td>For string values, defines the shortest allowed string. UI and PrintCapabilities or PrintTicket providers use this Property to validate the ParameterDef element.<br/></td>
<td>No<br/></td>
</tr>
<tr class="odd">
<td>MinValue <br/></td>
<td>integer if DataType Property specifies integer.<br/> decimal if DataType Property specifies decimal.<br/> DefaultValue: No minimum value is enforced.<br/></td>
<td>For integer- or decimal-valued parameters, defines the smallest allowed value. <br/></td>
<td>No<br/></td>
</tr>
<tr class="even">
<td>Multiple <br/></td>
<td>integer if DataType Property specifies integer.<br/> decimal if DataType Property specifies decimal.<br/> DefaultValue: 1<br/></td>
<td>For integer- or decimal-valued parameters, the value of the parameter should be a multiple of this number. For more information, see <a href="#notes-on-multiple">Notes on Multiple</a> following this table.<br/></td>
<td>No<br/></td>
</tr>
<tr class="odd">
<td>UnitType <br/></td>
<td>string value indicating the units used for the parameter.<br/> No default value.<br/></td>
<td>Indicates the units in which the parameter is expressed. For example, angles in tenths of degrees, lengths in microns, and so on.<br/></td>
<td>Yes<br/></td>
</tr>
</tbody>
</table>



 

## Notes on Multiple

For ParameterInit elements with integer or decimal values, the value of the ParameterInit should be a multiple of this number. For example, decimal-valued ParameterInit elements can be limited to tenths by setting this property to 0.1. UI elements use this Property when they construct dialogs and UI controls. In addition, PrintTicket validation code can use this Property to round the value of a ParameterInit to the nearest value indicated by Multiple. Note: Device drivers and PrintCapabilities providers should not assume that ParameterInit values are multiples of this Property value. Each provider must be able to round arbitrary values to the nearest useable value due to the possibility that different providers might specify different and conflicting values for this property.

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 




