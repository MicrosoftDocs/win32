---
Description: Glossary page
Robots: noindex, nofollow
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: VS\|dsglossary\|~\\adsi\\c.htm
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
title: C
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# C

<dl> <dt>

<span id="_ds_canonical_name"></span><span id="_DS_CANONICAL_NAME"></span>**canonical name**
</dt> <dd>

The distinguished name, rendered as, root first, delimited with the forward slash (/), and without the LDAP attribute tags (CN=, DC=). For example, "Fabrikam.Com/Users/Jeff Smith".

</dd> <dt>

<span id="_ds_castle"></span><span id="_DS_CASTLE"></span>**castle**
</dt> <dd>

A small group of computers, on a network, that trust each other and share a common user database.

</dd> <dt>

<span id="_ds_class"></span><span id="_DS_CLASS"></span>**class**
</dt> <dd>

See [*object class*](https://www.bing.com/search?q=*object class*).

</dd> <dt>

<span id="_ds_class_instance"></span><span id="_DS_CLASS_INSTANCE"></span>**class instance**
</dt> <dd>

A specific occurrence of a class defined in a [*directory service*](https://www.bing.com/search?q=*directory service*) schema. For example, **user** objects with the attributes "Jeff Smith" or "Eva Corets" would represent instances of the user class.

</dd> <dt>

<span id="_ds_cn"></span><span id="_DS_CN"></span>**CN**
</dt> <dd>

See *common name*.

</dd> <dt>

<span id="_ds_collection"></span><span id="_DS_COLLECTION"></span>**collection**
</dt> <dd>

A set of directory objects that can be represented using the same data type. In ADSI, you can use the [**IADsCollection**](https://msdn.microsoft.com/library/aa705975) interface to work with collections.

</dd> <dt>

<span id="_ds_com"></span><span id="_DS_COM"></span>**COM**
</dt> <dd>

See *Component Object Model*.

</dd> <dt>

<span id="_ds_common_name"></span><span id="_DS_COMMON_NAME"></span>**common name**
</dt> <dd>

A naming attribute from which an object distinguished name is formed. For most object classes, the naming attribute is the Common-Name. For example, a user object with its **cn** set to "Jeff Smith" might have a distinguished name of "CN=Jeff Smith,CN=Users,DC=Fabrikam,DC=com".

</dd> <dt>

<span id="_ds_component_object_model"></span><span id="_DS_COMPONENT_OBJECT_MODEL"></span>**Component Object Model**
</dt> <dd>

A programming model that defines how software components interact regardless of where the components are physically located. See [The Component Object Model](https://www.bing.com/search?q=The Component Object Model).

</dd> <dt>

<span id="_ds_configuration_partition"></span><span id="_DS_CONFIGURATION_PARTITION"></span>**configuration partition**
</dt> <dd>

A [*directory partition*](https://www.bing.com/search?q=*directory partition*) that contains replication topology and other configuration data that must be replicated throughout the forest. Every domain controller in an enterprise forest has a replica of the same configuration partition.

</dd> <dt>

<span id="_ds_container"></span><span id="_DS_CONTAINER"></span>**container**
</dt> <dd>

A directory object that can contain other directory objects. In Active Directory, the schema definition of each object class determines the types of objects that can be containers of instances of the class. See [Containers and Leaves](https://msdn.microsoft.com/library/ms675741) and [**IADsContainer**](https://msdn.microsoft.com/library/aa705985).

</dd> <dt>

<span id="_ds_content_rules"></span><span id="_DS_CONTENT_RULES"></span>**content rules**
</dt> <dd>

A set of rules that define attributes of class instances stored in a [*directory service*](https://www.bing.com/search?q=*directory service*). In Active Directory, the schema definition of each class specifies the mandatory (**mustHave**) and optional (**mayHave**) attributes for instances of the class.

</dd> </dl>

 

 



