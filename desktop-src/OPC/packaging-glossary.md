---
title: Packaging API Glossary
description: This topic provides definitions for Packaging API terms.
Robots: noindex, nofollow
ms.assetid: 751e39e2-01a8-4a34-a102-71046f4f8631
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Packaging API Glossary

<dl> <dt>

<span id="opc.opc_glossary_content_type"></span><span id="OPC.OPC_GLOSSARY_CONTENT_TYPE"></span>**content type**
</dt> <dd>

The media type of the data stream of a part in a package. Content types are defined by the package format designer and must adhere to the requirements in section 8.1.2 Content Types of OpenXML, ECMA-376 1st edition Part 2. See also: part, part content, package format designer, Content Types stream.

</dd> <dt>

<span id="opc.opc_glossary_content_types_stream"></span><span id="OPC.OPC_GLOSSARY_CONTENT_TYPES_STREAM"></span>**Content Types stream**
</dt> <dd>

The XML-markup stream that identifies the content type of each part in a package. This stream is not URI-addressable. The structure and use of this stream is defined in OpenXML, ECMA-376 1st edition Part 2. See also: part, content type, part content.

</dd> <dt>

<span id="opc.opc_glossary_core_properties_part"></span><span id="OPC.OPC_GLOSSARY_CORE_PROPERTIES_PART"></span>**Core Properties part**
</dt> <dd>

The part that stores the XML markup of the core properties data in a package. The structure and use of this part is defined in section 10. Core Properties of OpenXML, ECMA-376 1st edition Part 2. See also: part, content type, and part content.

</dd> <dt>

<span id="opc.opc_glossary_digital_signature_origin_part"></span><span id="OPC.OPC_GLOSSARY_DIGITAL_SIGNATURE_ORIGIN_PART"></span>**Digital Signature Origin part**
</dt> <dd>

The part that has relationships that target the parts that store signature markup. The structure and use of the Digital Signature Origin part is defined in section 12.2.1 Digital Signature Origin Part of OpenXML, ECMA-376 1st edition Part 2. See also: part, signature part.

</dd> <dt>

<span id="opc.opc_glossary_interleaved_part"></span><span id="OPC.OPC_GLOSSARY_INTERLEAVED_PART"></span>**interleaved part**
</dt> <dd>

A part that has been divided into pieces in a physical package. Pieces are not individually addressable; their content is accessed by accessing the interleaved part to which they belong. See also: part, piece.

</dd> <dt>

<span id="opc.opc_glossary_opc"></span><span id="OPC.OPC_GLOSSARY_OPC"></span>**OPC**
</dt> <dd>

See other term: Open Packaging Conventions

</dd> <dt>

<span id="opc.opc_glossary_open_packaging_conventions"></span><span id="OPC.OPC_GLOSSARY_OPEN_PACKAGING_CONVENTIONS"></span>**Open Packaging Conventions**
</dt> <dd>

Part 2: Open Packaging Conventions (ECMA-376 1st edition Part 2) of the OpenXML standard. It describes the requirements for packages and for software that implements package-processing operations.

</dd> <dt>

<span id="opc.opc_glossary_package"></span><span id="OPC.OPC_GLOSSARY_PACKAGE"></span>**package**
</dt> <dd>

A logical entity that aggregates resources. The logical organization of a package resembles a directed graph and can be mapped to various physical structures, such as a file or a distributed system. The structure and use of packages are defined in OpenXML, ECMA-376 1st edition Part 2. See also: physical package.

</dd> <dt>

<span id="opc.opc_glossary_package_component"></span><span id="OPC.OPC_GLOSSARY_PACKAGE_COMPONENT"></span>**package component**
</dt> <dd>

Any data component or resource in a package, including parts, relationships, and the Content Types stream. See also: part, relationship, and Content Types stream.

</dd> <dt>

<span id="opc.opc_glossary_package_consumer"></span><span id="OPC.OPC_GLOSSARY_PACKAGE_CONSUMER"></span>**package consumer**
</dt> <dd>

Software that reads packages by using input and output operations that are specified in OpenXML, ECMA-376 1st edition Part 2. See also: package producer.

</dd> <dt>

<span id="opc.opc_glossary_package_format_designer"></span><span id="OPC.OPC_GLOSSARY_PACKAGE_FORMAT_DESIGNER"></span>**package format designer**
</dt> <dd>



</dd> <dt>

<span id="opc.opc_glossary_package_producer"></span><span id="OPC.OPC_GLOSSARY_PACKAGE_PRODUCER"></span>**package producer**
</dt> <dd>

Software that writes packages by using input and output operations that are specified in OpenXML, ECMA-376 1st edition Part 2. See also: package consumer.

</dd> <dt>

<span id="opc.opc_glossary_package_relationship"></span><span id="OPC.OPC_GLOSSARY_PACKAGE_RELATIONSHIP"></span>**package relationship**
</dt> <dd>

A relationship that has a package as its source. Package relationships are stored in the "/\_rels/.rels" Relationships part and are defined in OpenXML, ECMA-376 1st edition Part 2. See also: part, relationship, source, Relationships part, and part relationship.

</dd> <dt>

<span id="opc.opc_glossary_package_root"></span><span id="OPC.OPC_GLOSSARY_PACKAGE_ROOT"></span>**package root**
</dt> <dd>

The URI of the top organizational level (root) of a package, represented by the "/" string. See also: package.

</dd> <dt>

<span id="opc.opc_glossary_package_signature"></span><span id="OPC.OPC_GLOSSARY_PACKAGE_SIGNATURE"></span>**package signature**
</dt> <dd>

A digital signature that has been or will be generated for a package. See also: package.

</dd> <dt>

<span id="opc.opc_glossary_part"></span><span id="OPC.OPC_GLOSSARY_PART"></span>**part**
</dt> <dd>

A resource that stores data in a package. The structure and use of parts is defined in section 8. Package Model and section 9. Physical Package of OpenXML, ECMA-376 1st edition Part 2. See also: part name, content type, and part content.

</dd> <dt>

<span id="opc.opc_glossary_part_content"></span><span id="OPC.OPC_GLOSSARY_PART_CONTENT"></span>**part content**
</dt> <dd>

The data stream of a part in a package. For example, the byte stream of a JPEG image or an XML document. See also: part, and content type.

</dd> <dt>

<span id="opc.opc_glossary_part_name"></span><span id="OPC.OPC_GLOSSARY_PART_NAME"></span>**part name**
</dt> <dd>

The package-relative URI of a part in a package. The syntax for this URI is defined in section 8.1.1 Part Names of OpenXML, ECMA-376 1st edition Part 2. See also: part.

</dd> <dt>

<span id="opc.opc_glossary_part_relationship"></span><span id="OPC.OPC_GLOSSARY_PART_RELATIONSHIP"></span>**part relationship**
</dt> <dd>

A relationship that has a part as its source. All relationships that have the same source are stored in a single Relationships part. See also: part, relationship, source, Relationships part, and package relationship.

</dd> <dt>

<span id="opc.opc_glossary_physical_package"></span><span id="OPC.OPC_GLOSSARY_PHYSICAL_PACKAGE"></span>**physical package**
</dt> <dd>

An instance of a package that has been mapped to a physical structure such as a file or a distributed system. See also: package.

</dd> <dt>

<span id="opc.opc_glossary_piece"></span><span id="OPC.OPC_GLOSSARY_PIECE"></span>**piece**
</dt> <dd>

A file that contains data for an interleaved part. A piece is not individually addressable and its content can only be accessed by accessing the interleaved part to which the piece belongs. The requirements and use of pieces are defined in section 9.1.4 Interleaving of OpenXML, ECMA-376 1st edition Part 2. See also: part, and interleaved part.

</dd> <dt>

<span id="opc.opc_glossary_reference"></span><span id="OPC.OPC_GLOSSARY_REFERENCE"></span>**reference**
</dt> <dd>

Identifier of package components and XML elements that have been or will be signed. When a signature is generated, references are serialized in the signature markup as &lt;Reference&gt; elements. See also: package component, package signature, and signature markup.

</dd> <dt>

<span id="opc.opc_glossary_referenced_type"></span><span id="OPC.OPC_GLOSSARY_REFERENCED_TYPE"></span>**referenced type**
</dt> <dd>

The type of the XML element that is referenced for signing. Specifying the type of a referenced element is optional. See also: reference, and signature markup.

</dd> <dt>

<span id="opc.opc_glossary_relationship"></span><span id="OPC.OPC_GLOSSARY_RELATIONSHIP"></span>**relationship**
</dt> <dd>

A link, as in a directed graph, that connects one package resource to another. Relationships have a source and a target. When a package is saved, relationships in the package are serialized as XML markup (relationship markup) and stored in Relationships parts. The requirements and use of relationships are defined in section 8.3 Relationships of OpenXML, ECMA-376 1st edition Part 2. See also: resource, source, target, relationship markup, and Relationships part.

</dd> <dt>

<span id="opc.opc_glossary_relationship_markup"></span><span id="OPC.OPC_GLOSSARY_RELATIONSHIP_MARKUP"></span>**relationship markup**
</dt> <dd>

XML markup that is the serialized representation of relationships in a package. Relationship markup is the part content of a Relationships part and is defined in section 8.3.3 Relationship Markup of OpenXML, ECMA-376 1st edition Part 2. See also: relationship, Relationships part, and part content.

</dd> <dt>

<span id="opc.opc_glossary_relationship_type"></span><span id="OPC.OPC_GLOSSARY_RELATIONSHIP_TYPE"></span>**relationship type**
</dt> <dd>

A URI that defines the role of the relationship as specified by the package format designer or in OpenXML, ECMA-376 1st edition Part 2. See also: part, relationship, and package format designer.

</dd> <dt>

<span id="opc.opc_glossary_relationships_part"></span><span id="OPC.OPC_GLOSSARY_RELATIONSHIPS_PART"></span>**Relationships part**
</dt> <dd>

A specialized part that stores the relationship markup that represents all the relationships that have a common source. There is one Relationships part for every resource that is the source of a relationship in the package. The structure and use of Relationships parts are defined in section 8.3.1 Relationships Part of OpenXML, ECMA-376 1st edition Part 2. See also: part, relationship, relationship markup, and source.

</dd> <dt>

<span id="opc.opc_glossary_relationships_transform"></span><span id="OPC.OPC_GLOSSARY_RELATIONSHIPS_TRANSFORM"></span>**Relationships transform**
</dt> <dd>

A package-specific transform method that is applied to the relationship markup of selected relationships in a Relationships part that has been referenced for signing. The algorithm and use of the Relationships transform are described in section 12. Digital Signatures of OpenXML, ECMA-376 1st edition Part 2. See also: transform method, relationship, relationship markup, Relationships part.

</dd> <dt>

<span id="opc.opc_glossary_resource"></span><span id="OPC.OPC_GLOSSARY_RESOURCE"></span>**resource**
</dt> <dd>

A URI-addressable entity that is located inside or outside of a package. Packages and parts are resources. See also: package, and part.

</dd> <dt>

<span id="opc.opc_glossary_signature"></span><span id="OPC.OPC_GLOSSARY_SIGNATURE"></span>**signature**
</dt> <dd>

See other term: package signature

</dd> <dt>

<span id="opc.opc_glossary_signature_markup"></span><span id="OPC.OPC_GLOSSARY_SIGNATURE_MARKUP"></span>**signature markup**
</dt> <dd>

XML markup that is the serialized representation of a generated package signature. This markup is stored in the Digital Signature XML Signature part. The structure and use of signature markup and the Digital Signature XML Signature part are described in section 12. Digital Signatures of OpenXML, ECMA-376 1st edition Part 2. See also: signature part, and package signature.

</dd> <dt>

<span id="opc.opc_glossary_signature_part"></span><span id="OPC.OPC_GLOSSARY_SIGNATURE_PART"></span>**signature part**
</dt> <dd>

A part that is used to store package signature information. The structure and use of signature parts are described in section 12. Digital Signatures of OpenXML, ECMA-376 1st edition Part 2. See also: part, and Digital Signature Origin part.

</dd> <dt>

<span id="opc.opc_glossary_signing_time"></span><span id="OPC.OPC_GLOSSARY_SIGNING_TIME"></span>**signing time**
</dt> <dd>

The date and time when a package signature was generated. See also: package signature.

</dd> <dt>

<span id="opc.opc_glossary_source"></span><span id="OPC.OPC_GLOSSARY_SOURCE"></span>**source**
</dt> <dd>

The package or part that is the origin of a relationship in a package. See also: package, part, relationship, target, and resource.

</dd> <dt>

<span id="opc.opc_glossary_target"></span><span id="OPC.OPC_GLOSSARY_TARGET"></span>**target**
</dt> <dd>

The resource that is the destination of a relationship in a package. See also: package, part, relationship, source, and resource.

</dd> <dt>

<span id="opc.opc_glossary_transform_method"></span><span id="OPC.OPC_GLOSSARY_TRANSFORM_METHOD"></span>**transform method**
</dt> <dd>

An algorithm that processes XML markup. Transform methods are often used to process XML markup into a canonical (standard) form. See also: Relationships transform.

</dd> <dt>

<span id="opc.opc_glossary_xml_paper_specification"></span><span id="OPC.OPC_GLOSSARY_XML_PAPER_SPECIFICATION"></span>**XML Paper Specification**
</dt> <dd>

A specification that describes a file format that is used to store documents, to process them for printing, and to print them. This means that the documents will not change as they go through the printing process. The XPS format conforms to the Open Packaging Conventions (OpenXML, ECMA-376 1st edition Part 2). See also: package.

</dd> <dt>

<span id="opc.opc_glossary_xps"></span><span id="OPC.OPC_GLOSSARY_XPS"></span>**XPS**
</dt> <dd>

See other term: XML Paper Specification

</dd> </dl>

 

 




