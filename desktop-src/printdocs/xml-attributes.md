---
description: This topic is not current. For the most current information, see the Print Schema Specification.
ms.assetid: 41bc10fe-6c00-44c5-ba9a-10414b31cbdf
title: XML Attributes
ms.topic: article
ms.date: 05/31/2018
---

# XML Attributes

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

There are a number of XML attributes that appear in several element types defined in the Print Schema Framework. XML attributes with the same name generally have the same meaning and obey the same rules regardless of the element type they reside in. Therefore, the XML attributes are listed here by name and not by their host element type. Privately-defined XML attributes are not permitted. Only the XML attributes defined here may be used in a PrintCapabilities document or a PrintTicket, and then only in the defined context.

Although private parties are not permitted to introduce new definitions into another party's namespace, they are permitted utilize existing names from another private namespace as long as its use is consistent with the usage established by the other party. Thus an Option may contain ScoredProperty elements defined by several different parties, each residing in different namespaces.



<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute Name</th>
<th>Data Types and Values</th>
<th>Purpose</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>name <br/></td>
<td>XML QName<br/></td>
<td>This XML attribute identifies the element instance. It distinguishes one element from another of the same element type. This XML attribute is so widely used it is referred to as the name attribute.<br/></td>
<td>The following restrictions pertain to the name attribute.<br/>
<ul>
<li>The name attribute must be in the form of a valid XML-defined QName. That is, it must be qualified by a valid XML namespace. The QNames appearing as values of name attributes must be explicitly namespace-qualified even if a default namespace is defined. <br/></li>
<li>Character content must be that of a valid XML-defined QName. <br/></li>
<li>Privately-defined names must be qualified with a namespace that is uniquely associated with the party that introduced the name attribute.<br/></li>
<li>Sibling Uniqueness requirement: No two sibling elements belonging to the same element type may have the same name attribute. The only exception is Option elements, where the name attribute can be used to define an Option. Thus multiple-sibling Option elements may have the same name attribute.<br/></li>
<li>The following element types may contain name attributes: Property, ScoredProperty, ParameterDef, Option, and Feature.<br/></li>
<li>name attributes are required to appear in each of the element types that contain them, except in the case of some previously defined public Print Schema Option elements, such as DocumentNUp.<br/></li>
</ul>
The following example shows how to identify an Option instance using a 'name' attribute. This is the correct way to define Option elements. A provider should not have unnamed Options, unless they are publicly defined in the Print Schema, such as DocumentNUp.<br/>
<pre class="syntax" data-space="preserve"><code>  <psf:Option name=&quot;psk:StapleBottomRight&quot;>
    <psf:ScoredProperty name=&quot;psk:Angle&quot;>
      <psf:Value xsi:type=&quot;xs:integer&quot;>_Undefined_</psf:Value>
    </psf:ScoredProperty>
    <psf:ScoredProperty name=&quot;psk:SheetCapacity&quot; >
      <psf:Value xsi:type=&quot;xs:integer&quot;>_Undefined_</psf:Value>
    </psf:ScoredProperty>
  </psf:Option></code></pre></td>
</tr>
<tr class="even">
<td>propagate <br/></td>
<td>Enumeration<br/> No values are currently defined.<br/></td>
<td>The propagate attribute is not used in the initial version of the Print Schema Framework. It is documented here so that PrintCapabilities or PrintTicket validation code implemented for the initial version of the Print Schema Framework can process any subsequent schema versions without error.<br/></td>

</tr>
<tr class="odd">
<td>constrained <br/></td>
<td>Enumeration<br/> Allowed values:<br/>
<ul>
<li>None <br/></li>
<li>PrintTicketSettings <br/></li>
<li>AdminSettings <br/></li>
<li>DeviceSettings <br/></li>
</ul></td>
<td>Indicates whether the Option is available for selection or for use. <br/></td>
<td>The allowed values of the constrained attribute have the following meanings. Note that these values are listed in order, from least restrictive (None) to most restrictive (DeviceSettings).<br/> None <br/>
<ul>
<li>The Option is not constrained. <br/></li>
</ul>
PrintTicketSettings <br/>
<ul>
<li>The Option is constrained by the PrintTicket settings. This implies that changing the configuration can remove the constraint. <br/></li>
</ul>
AdminSettings <br/>
<ul>
<li>The Option is constrained by the administrator's settings; the Option cannot be enabled by the user.<br/></li>
</ul>
DeviceSettings <br/>
<ul>
<li>The Option is constrained by the device settings or the physically installed device options; the Option cannot be enabled by either the user or the administrator.<br/></li>
</ul>
When the PrintCapabilities provider reports values of the constrained attribute, the most restrictive constraint found should be reported. For example, if an Option is constrained by both an administrator setting and a device setting, the PrintCapabilities provider should report DeviceSettings.<br/></td>
</tr>
<tr class="even">
<td>xmlns <br/></td>
<td>URI<br/></td>
<td>This XML attribute establishes a link between a namespace uniform resource identifier (URI) and the namespace prefix that appears in the XML QName. You must establish such a link to the namespace URI defined for the Print Schema Framework before you can use any of the Framework-defined element tags, Attributes, name attributes, and so on. You may declare this namespace to be the default to avoid actually qualifying the element tags with a namespace prefix, although all other QNames must be explicitly qualified. The standard namespace must be defined in the appropriate root element. Observe all XML rules and conventions regarding use of the xmlns attribute.<br/> The URI for the Print Schema Framework is http://schemas.microsoft.com/windows/2003/08/printing/printschemaframework.<br/> The URI for the Print Schema Keywords is http://schemas.microsoft.com/windows/2003/08/printing/printschemakeywords.<br/></td>

</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 




