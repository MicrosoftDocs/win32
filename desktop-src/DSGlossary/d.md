---
Description: Glossary page
Robots: 'noindex, nofollow'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: 'VS\|dsglossary\|~\\adsi\\d.htm'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
title: D
---

# D

<dl> <dt>

<span id="_ds_dacl"></span><span id="_DS_DACL"></span>**DACL**
</dt> <dd>

See *discretionary access-control list*.

</dd> <dt>

<span id="_ds_data_model"></span><span id="_DS_DATA_MODEL"></span>**data model**
</dt> <dd>

Active Directory *data model* is derived from the [*X.500*](x.md#-ds-x-500) data model. The directory holds objects that represent various elements described by attributes. The types of objects stored in the directory are defined in the [*schema*](s.md#-ds-schema). For each [*object class*](o.md#-ds-object-class), the schema defines what attributes an instance of the class must have, what additional attributes it may have, and which object classes can be a parent of the current object class.

</dd> <dt>

<span id="_ds_dc"></span><span id="_DS_DC"></span>**DC**
</dt> <dd>

See *domain controller* or *domain component*.

</dd> <dt>

<span id="_ds_delegation"></span><span id="_DS_DELEGATION"></span>**delegation**
</dt> <dd>

*Delegation* is one of the most important security features of Active Directory. Delegation allows a higher administrative authority to grant specific administrative rights for [*containers*](c.md#-ds-container) and subtrees to individuals and groups. This eliminates the need for domain administrators with broad authority over large segments of users. An [*access-control entry*](a.md#-ds-access-control-entry) can grant specific administrative rights on the objects in a container to a user or group. Rights are granted for specific operations on specific [*object classes*](o.md#-ds-object-class) using an ACE in the container [*access-control list*](a.md#-ds-access-control-list).

</dd> <dt>

<span id="_ds_directory"></span><span id="_DS_DIRECTORY"></span>**directory**
</dt> <dd>

A *directory* is a store for [*object*](o.md#-ds-object) data. For example, a telephone directory stores telephone subscriber data. In a file system, the directory stores file data. In a distributed computing system, like the Internet, there are many objects, such as printers, fax servers, applications, databases, and users.

</dd> <dt>

<span id="_ds_directory_client"></span><span id="_DS_DIRECTORY_CLIENT"></span>**directory client**
</dt> <dd>

A server, workstation, or application that accesses a *directory service*, using the LDAP protocol, to query the directory for object data.

</dd> <dt>

<span id="_ds_directory_partition"></span><span id="_DS_DIRECTORY_PARTITION"></span>**directory partition**
</dt> <dd>

A directory partition, or naming context, is a contiguous Active Directory subtree replicated on one, or more, Windows 2000 domain controllers in a forest. By default, each domain controller has a replica of three partitions: the [*schema partition*](s.md#-ds-schema-partition), the [*configuration partition*](c.md#-ds-configuration-partition), and a *domain partition*.

</dd> <dt>

<span id="_ds_directory_service"></span><span id="_DS_DIRECTORY_SERVICE"></span>**directory service**
</dt> <dd>

A service that provides access to data and objects in a directory or network environment.

</dd> <dt>

<span id="_ds_directory_system_agent"></span><span id="_DS_DIRECTORY_SYSTEM_AGENT"></span>**directory system agent**
</dt> <dd>

The *directory system agent* is the process that provides access to the physical storage for Active Directory.

</dd> <dt>

<span id="_ds_discretionary_access_control_list"></span><span id="_DS_DISCRETIONARY_ACCESS_CONTROL_LIST"></span>**discretionary access-control list**
</dt> <dd>

A list controlled by the owner of an object and that specifies the access that particular users or groups can have to the object.

</dd> <dt>

<span id="_ds_distinguished_name"></span><span id="_DS_DISTINGUISHED_NAME"></span>**distinguished name**
</dt> <dd>

A fully qualified unique name, used to identify an object in a directory, that specifies the complete path to the object through the hierarchy of directory containers.

</dd> <dt>

<span id="_ds_dn"></span><span id="_DS_DN"></span>**DN**
</dt> <dd>

See *distinguished name*.

</dd> <dt>

<span id="_ds_dns"></span><span id="_DS_DNS"></span>**DNS**
</dt> <dd>

See *Domain Name System*.

</dd> <dt>

<span id="_ds_domain"></span><span id="_DS_DOMAIN"></span>**domain**
</dt> <dd>

In Active Directory, a collection of computer, user, and group objects defined by the administrator. These objects share a common directory database, security policies, and security relationships with other domains.

</dd> <dt>

<span id="_ds_domain_component"></span><span id="_DS_DOMAIN_COMPONENT"></span>**domain component**
</dt> <dd>

A *domain component* is used to indicate an element of a *distinguished name* that is part of a *domain*. For example, "CN=Jeff Smith,CN=Users,DC=Fabrikam,DC=com" contains the Domain Components "Fabrikam" and "com".

</dd> <dt>

<span id="_ds_domain_controller"></span><span id="_DS_DOMAIN_CONTROLLER"></span>**domain controller**
</dt> <dd>

A server computer, running on Windows NT, Windows 2000, or Windows Server 2003 that contains a replica of all the objects and object attributes in the *domain*.

</dd> <dt>

<span id="_ds_domain_forest"></span><span id="_DS_DOMAIN_FOREST"></span>**domain forest**
</dt> <dd>

Also called a [*forest*](f.md#-ds-forest). A logical structure formed by combining two or more Windows 2000 or Windows Server 2003 *domain trees*.

</dd> <dt>

<span id="_ds_domain_local_group"></span><span id="_DS_DOMAIN_LOCAL_GROUP"></span>**domain local group**
</dt> <dd>

A [*group*](g.md#-ds-group) that can contain members from any domain, but can be granted permissions only to resources in its own domain.

</dd> <dt>

<span id="_ds_domain_name_service"></span><span id="_DS_DOMAIN_NAME_SERVICE"></span>**Domain Name System**
</dt> <dd>

A hierarchical naming system for identifying Transmission Control Protocol/Internet Protocol (TCP/IP) hosts on the Internet.

</dd> <dt>

<span id="_ds_domain_partition"></span><span id="_DS_DOMAIN_PARTITION"></span>**domain partition**
</dt> <dd>

A [*directory partition*](#-ds-directory-partition) that contains the objects, such as users and computers, associated with the local domain.

</dd> <dt>

<span id="_ds_domain_tree"></span><span id="_DS_DOMAIN_TREE"></span>**domain tree**
</dt> <dd>

A hierarchical grouping of Windows 2000 or Windows Server 2003 domains.

</dd> <dt>

<span id="_ds_dsa"></span><span id="_DS_DSA"></span>**DSA**
</dt> <dd>

See *directory system agent*.

</dd> </dl>

 

 



