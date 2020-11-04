---
title: Active Directory Schema Terminology
description: The following terms are commonly used to refer to the Active Directory schema.
ms.assetid: 22c5756f-d663-4cb7-aab0-956b22a01e9d
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Active Directory Schema Terminology

The following terms are commonly used to refer to the Active Directory schema.


<dl> <dt>

<span id="Attribute"></span><span id="attribute"></span><span id="ATTRIBUTE"></span>Attribute
</dt> <dd>

Data items used to describe the objects that are represented by the classes that are defined in the schema. Attributes are defined in the schema separately from the classes; this allows a single attribute definition to be applied to many classes. For example, [**Description**](a-description.md) is an attribute that can be applied to any class in the schema. The **Description** attribute is defined once in the schema, assuring consistency, rather than having a different definition for **Description** of a user and **Description** of a printer.

> [!Note]  
> The term *property* is frequently used interchangeably with the term *attribute*.

 

</dd> <dt>

<span id="Attribute_Instance"></span><span id="attribute_instance"></span><span id="ATTRIBUTE_INSTANCE"></span>Attribute Instance
</dt> <dd>

An occurrence of an attribute that is defined in the schema. This term is used to distinguish between the definition of an attribute and a discrete occurrence of the attribute. For example, storing a User object for "Jeff Smith" with the [**Common-Name**](a-cn.md) attribute set to "Jeff Smith" creates an instance of [**Common-Name**](a-cn.md).

</dd> <dt>

<span id="Class"></span><span id="class"></span><span id="CLASS"></span>Class
</dt> <dd>

A formal description of a discrete, identifiable type of object stored in the directory service. For example, [**User**](c-user.md), [**Print-Queue**](c-printqueue.md), and [**Group**](c-group.md) are all classes. Furthermore, there are 3 distinct categories of classes: [Structural Classes](classes-structural.md), [Abstract Classes](classes-abstract.md), and [Auxiliary Classes](classes-auxiliary.md).

</dd> <dt>

<span id="Class_Instance"></span><span id="class_instance"></span><span id="CLASS_INSTANCE"></span>Class Instance
</dt> <dd>

An occurrence of a class that is defined in the schema. This term is used to distinguish between the definition of a class and a discrete occurrence of the class. For example, storing a [**User**](c-user.md) object for "Jeff Smith" in the directory service creates an instance of [**User**](c-user.md).

</dd> <dt>

<span id="Content_Rules"></span><span id="content_rules"></span><span id="CONTENT_RULES"></span>Content Rules
</dt> <dd>

The definition of the possible contents of the class instances that are stored in the directory service. In NT Directory Services (NTDS), upon which Active Directory is based, the content rules are completely expressed by the [**Must-Contain**](a-mustcontain.md) and [**May-Contain**](a-maycontain.md) attributes of the schema definitions for each class.

</dd> <dt>

<span id="Derivation"></span><span id="derivation"></span><span id="DERIVATION"></span>Derivation
</dt> <dd>

See *Inheritance*.

</dd> <dt>

<span id="Directory_Information_Tree"></span><span id="directory_information_tree"></span><span id="DIRECTORY_INFORMATION_TREE"></span>Directory Information Tree
</dt> <dd>

The directory itself, represented as a tree structure in which the vertices are the directory entries (class instances) and the connecting lines the parent-child relationships between the entries.

</dd> <dt>

<span id="DIT"></span><span id="dit"></span>DIT
</dt> <dd>

See *Directory Information Tree*.

</dd> <dt>

<span id="Control_Access_Rights"></span><span id="control_access_rights"></span><span id="CONTROL_ACCESS_RIGHTS"></span>Control Access Rights
</dt> <dd>

A class that describes an access right not tied to a resource, but an action. For example, a user can be granted the right to create relative ID values.

</dd> <dt>

<span id="Inheritance"></span><span id="inheritance"></span><span id="INHERITANCE"></span>Inheritance
</dt> <dd>

The ability to build new object classes from existing object classes. The new object is defined as a *subclass* of the parent object. The parent object becomes a *superclass* of the new object. A subclass inherits the attributes of the parent, including structure rules and content rules.

</dd> <dt>

<span id="LDAP"></span><span id="ldap"></span>LDAP
</dt> <dd>

See *Lightweight Directory Access Protocol*.

</dd> <dt>

<span id="Lightweight_Directory_Access_Protocol"></span><span id="lightweight_directory_access_protocol"></span><span id="LIGHTWEIGHT_DIRECTORY_ACCESS_PROTOCOL"></span>Lightweight Directory Access Protocol
</dt> <dd>

A standard Internet communications protocol used to communicate with the NTDS. LDAP version 2 and version 3 are supported.

</dd> <dt>

<span id="NT_Security_Descriptor"></span><span id="nt_security_descriptor"></span><span id="NT_SECURITY_DESCRIPTOR"></span>NT Security Descriptor
</dt> <dd>

See *Security Descriptor*.

</dd> <dt>

<span id="Object"></span><span id="object"></span><span id="OBJECT"></span>Object
</dt> <dd>

A unit of data storage in the directory service. Directory service objects are not to be confused with COM objects or other object-oriented system objects, which have an executable component and run-time behavior. Directory service objects consist only of data. A directory service object is defined by a [**Class-Schema**](c-classschema.md) object and a group of [**Attribute-Schema**](c-attributeschema.md) objects referenced by the [**Class-Schema**](c-classschema.md) object.

[**Class-Schema**](c-classschema.md) and [**Attribute-Schema**](c-attributeschema.md) objects are themselves directory service objects, and have definitions in the schema like any other objects. See *Class*.

</dd> <dt>

<span id="Object_Identifier"></span><span id="object_identifier"></span><span id="OBJECT_IDENTIFIER"></span>Object Identifier
</dt> <dd>

Unique numeric values, issued by various issuing authorities, to uniquely identify data elements, syntaxes, and various other parts of distributed applications. Object Identifiers (OIDs) are found in OSI applications, X.500 Directories, SNMP, and other applications where uniqueness is important. OIDs are based on a tree structure, in which a superior issuing authority, such as the ISO, allocates a branch of the tree to a sub-authority, which in turn can allocate sub-branches.

OIDs in the NTDS include some issued by the ISO for X.500 classes and attributes, and some issued by Microsoft. OID notation is a dotted string of numbers, for example "1.2.840.113556.1.5.4", which translates as listed in the following list. 

| Value  | Description                                                                                  |
|--------|----------------------------------------------------------------------------------------------|
| 1      | ISO - the "root authority", issued "1.2" to ANSI, which in turn...                           |
| 2      | ANSI ...issued "1.2.840" to USA, which in turn...                                            |
| 840    | USA ...issued "1.2.840.113556" to Microsoft...                                               |
| 113556 | Microsoft ...where Microsoft internally manages several OID branches under "1.2.840.113556". |
| 1      | Microsoft DS                                                                                 |
| 5      | NTDS Classes                                                                                 |
| 4      | Builtin-Domain                                                                               |



 

</dd> <dt>

<span id="OID"></span><span id="oid"></span>OID
</dt> <dd>

See *Object Identifier*.

</dd> <dt>

<span id="Schema"></span><span id="schema"></span><span id="SCHEMA"></span>Schema
</dt> <dd>

A formal definition of the directory service contents and structure. The schema defines all attributes and classes. For each class, the [**Poss-Superiors**](a-posssuperiors.md), [**Must-Contain**](a-mustcontain.md), and [**May-Contain**](a-maycontain.md) attributes are defined. [**Poss-Superiors**](a-posssuperiors.md) defines the possible tree structures for the directory service by specifying what classes can be the parent for any given class. [**Must-Contain**](a-mustcontain.md) and [**May-Contain**](a-maycontain.md) list the attributes for a class that must be present to store the class and what additional attributes may optionally be present.

</dd> <dt>

<span id="Security_Descriptor"></span><span id="security_descriptor"></span><span id="SECURITY_DESCRIPTOR"></span>Security Descriptor
</dt> <dd>

Information about the ownership of an object and the permissions that other users have on that object. The [**NT-Security-Descriptor**](a-ntsecuritydescriptor.md) property of a schema entry contains a string that represents the security descriptor of the object. For more information about the format of the information in this field, see [Security Descriptor String Format](/windows/desktop/SecAuthZ/security-descriptor-string-format).

</dd> <dt>

<span id="Structure_Rules"></span><span id="structure_rules"></span><span id="STRUCTURE_RULES"></span>Structure Rules
</dt> <dd>

The definition of the possible tree structure or structures. In the NTDS, the structure rules are completely expressed by the Poss-superiors attribute present on each [**Class-Schema**](c-classschema.md) object. See *Schema*.

</dd> <dt>

<span id="Subclass"></span><span id="subclass"></span><span id="SUBCLASS"></span>Subclass
</dt> <dd>

A [**Class-Schema**](c-classschema.md) object that inherits from another [**Class-Schema**](c-classschema.md) object. See *Inheritance*.

</dd> <dt>

<span id="Superclass"></span><span id="superclass"></span><span id="SUPERCLASS"></span>Superclass
</dt> <dd>

A [**Class-Schema**](c-classschema.md) object from which one or more other [**Class-Schema**](c-classschema.md) objects inherit. See *Inheritance*.

</dd> <dt>

<span id="Tree"></span><span id="tree"></span><span id="TREE"></span>Tree
</dt> <dd>

See *Directory Information Tree*.

</dd> <dt>

<span id="X.500"></span><span id="x.500"></span>X.500
</dt> <dd>

A family of standards developed jointly by the ISO and ITU, formerly known as the CCITT, that specify the naming, data representation, and communications protocols for a directory service.

</dd> </dl>

 

 