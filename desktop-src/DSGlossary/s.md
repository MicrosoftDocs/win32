---
Description: Glossary page
Robots: noindex, nofollow
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: VS\|dsglossary\|~\\adsi\\s.htm
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
title: S
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# S

<dl> <dt>

<span id="_ds_sacl"></span><span id="_DS_SACL"></span>**SACL**
</dt> <dd>

See *system access-control list*.

</dd> <dt>

<span id="_ds_schema"></span><span id="_DS_SCHEMA"></span>**schema**
</dt> <dd>

The Active Directory schema contains formal definitions of every [*object class*](o.md#-ds-object-class) that can be created in an Active Directory forest. The schema also contains formal definitions of every attribute that can exist in an Active Directory object. See [Active Directory Schema](https://msdn.microsoft.com/library/ms674984).

In ADSI, the schema management interfaces supply a means of reading and setting the data associated with class, attribute, and syntax definitions. Use these interfaces with the Active Directory schema as well as with the schemas of other directory services.

</dd> <dt>

<span id="_ds_schema_partition"></span><span id="_DS_SCHEMA_PARTITION"></span>**schema partition**
</dt> <dd>

A [*directory partition*](d.md#-ds-directory-partition) that contains the **classSchema** and **attributeSchema** objects that define the types of objects that can exist in the Active Directory forest. Every domain controller in an enterprise forest has a replica of the same schema partition.

</dd> <dt>

<span id="_ds_security_identifier"></span><span id="_DS_SECURITY_IDENTIFIER"></span>**security identifier (SID)**
</dt> <dd>

A variable length value that uniquely identifies a security principal, such as a user or group. SIDs are used in security descriptors and access-control entries.

</dd> <dt>

<span id="_ds_service_principal_name"></span><span id="_DS_SERVICE_PRINCIPAL_NAME"></span>**service principal name (SPN)**
</dt> <dd>

The name by which a client uniquely identifies an instance of a service. See [Service Principal Names](https://msdn.microsoft.com/library/ms677949).

</dd> <dt>

<span id="_ds_site"></span><span id="_DS_SITE"></span>**site**
</dt> <dd>

A location in a network where Active Directory servers are held. A site is defined as one or more well connected TCP/IP subnets. "Well connected" means that network connectivity is highly reliable and fast. Defining a site as a set of subnets allows administrators to quickly and easily configure Active Directory access and replication topology to take advantage of the physical network. When users log in, Active Directory clients find Active Directory servers in the same site as the user. Due to the fact that computers in the same site are close to each other in network terms, communication among computers is reliable, fast, and efficient.

</dd> <dt>

<span id="_ds_structure_rules"></span><span id="_DS_STRUCTURE_RULES"></span>**structure rules**
</dt> <dd>

Defines the possible tree structure of Active Directory, that is, which object classes can contain which object classes. In Active Directory, the **possSuperiors** and **systemPossSuperiors** attributes in the schema definition of each object class specifies the object classes that can contain instances of the class. See [Characteristics of Object Classes](https://msdn.microsoft.com/library/ms675579).

</dd> <dt>

<span id="_ds_system_access_control_list"></span><span id="_DS_SYSTEM_ACCESS_CONTROL_LIST"></span>**system access-control list (SACL)**
</dt> <dd>

A *system access-control list* controls the generation of audit messages for attempts to access a securable object. The ability to get or set an object's SACL is controlled by a privilege typically held only by system administrators.

</dd> </dl>

 

 



