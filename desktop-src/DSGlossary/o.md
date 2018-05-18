---
Description: Glossary page
Robots: 'noindex, nofollow'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: 'VS\|dsglossary\|~\\adsi\\o.htm'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
title: O
---

# O

<dl> <dt>

<span id="_ds_object"></span><span id="_DS_OBJECT"></span>**object**
</dt> <dd>

In ADSI, refers to a [*COM*](c.md#-ds-component-object-model) object that implements one or more interfaces.

In Active Directory®, the basic named unit of storage. A directory object is an instance of an object class, which is defined in the [Active Directory Schema](https://msdn.microsoft.com/library/ms674984).

</dd> <dt>

<span id="_ds_object_class"></span><span id="_DS_OBJECT_CLASS"></span>**object class**
</dt> <dd>

A formal definition of a specific kind of object that can be stored in the directory. An object class is a distinct, named set of attributes that represents something concrete, such as a user, a printer, or an application. The terms *object class* and [*class*](c.md#-ds-class) are used interchangeably.

</dd> <dt>

<span id="_ds_object_class_instance"></span><span id="_DS_OBJECT_CLASS_INSTANCE"></span>**object class instance**
</dt> <dd>

Represents a discreet occurrence of an *object class*.

</dd> <dt>

<span id="_ds_object_identifier"></span><span id="_DS_OBJECT_IDENTIFIER"></span>**object identifier (OID)**
</dt> <dd>

A numeric value that unambiguously identifies an *object class*, attribute, or syntax in a [*directory service*](d.md#-ds-directory-service). An OID is represented as a dotted decimal string (for example, "1.2.3.4").

</dd> <dt>

<span id="_ds_oid"></span><span id="_DS_OID"></span>**OID**
</dt> <dd>

See *object identifier*.

</dd> <dt>

<span id="_ds_operation_policy"></span><span id="_DS_OPERATION_POLICY"></span>**operation policy**
</dt> <dd>

An operation is the interaction that a subject wants to have with an object. For example, when a user (the subject), wants to access (the operation), a given server (the object), over the network, a policy determines whether that access will be allowed.

</dd> <dt>

<span id="_ds_operational_attribute"></span><span id="_DS_OPERATIONAL_ATTRIBUTE"></span>**operational attribute**
</dt> <dd>

An attribute implemented internally by a particular directory implementation. Operational attributes do not appear in the schema and must be requested explicitly. Operational Attributes occurred originally in the X.500 specifications for a directory service and have been carried over into the LDAP version 3 specifications (RFC 2251). RFC 2251 requires support for certain operational attributes; a given directory implementation may implement any number of others.

</dd> </dl>

 

 



