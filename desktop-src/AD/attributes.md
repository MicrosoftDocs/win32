---
title: Attributes (AD DS)
description: Each object in Active Directory Domain Services contains a set of attributes that define the characteristics of the object.
ms.assetid: 9efa7ae1-b6a9-4b95-b031-b502772c536c
ms.tgt_platform: multiple
keywords:
- attributes AD
ms.topic: article
ms.date: 05/31/2018
---

# Attributes (AD DS)

Each object in Active Directory Domain Services contains a set of attributes that define the characteristics of the object. Each attribute is described by an [**attributeSchema**](/windows/desktop/ADSchema/c-attributeschema) object in the schema container that defines the attribute. The attribute definition includes a variety of data, for example, what object types that the attribute applies to and the syntax type of the attribute. For more information about attribute schema definitions, see [Characteristics of Attributes](characteristics-of-attributes.md).

The following list lists the type of attributes that are stored in Active Directory Domain Services.

<dl> <dt>

<span id="Domain-replicated__stored_attributes"></span><span id="domain-replicated__stored_attributes"></span><span id="DOMAIN-REPLICATED__STORED_ATTRIBUTES"></span>Domain-replicated, stored attributes
</dt> <dd>

Some attributes are stored in the directory (such as [**cn**](/windows/desktop/ADSchema/a-cn), [**nTSecurityDescriptor**](/windows/desktop/ADSchema/a-ntsecuritydescriptor), and [**objectGUID**](/windows/desktop/ADSchema/a-objectguid)) and replicated to all domain controllers in a domain. A subset of these attributes is also replicated to the global catalog. If you enumerate attributes of an object from the global catalog, only the attributes replicated to the global catalog are returned. Some attributes are also indexed because including an indexed property in a query improves the query performance.

</dd> <dt>

<span id="Non-replicated__locally_stored_attributes"></span><span id="non-replicated__locally_stored_attributes"></span><span id="NON-REPLICATED__LOCALLY_STORED_ATTRIBUTES"></span>Non-replicated, locally stored attributes
</dt> <dd>

Non-replicated attributes, such as [**badPwdCount**](/windows/desktop/ADSchema/a-badpwdcount), [**Last-Logon**](/windows/desktop/ADSchema/a-lastlogon), and [**Last-Logoff**](/windows/desktop/ADSchema/a-lastlogoff) are stored on each domain controller, but are not replicated. The non-replicated attributes are attributes that pertain to a particular domain controller. For example, **Last-Logon** attribute is the last date and time that the user's network logon was validated by that particular domain controller that returned the property. These attributes can be retrieved in the same way as the domain-wide attributes described previously. However, for these attributes, each domain controller stores only values that pertain to that particular domain controller. For example, to obtain the last time that a user logged on to the domain, retrieve the **Last-Logon** attribute for the user from every domain controller in the domain and find that latest date and time.

</dd> <dt>

<span id="Non-stored__constructed_attributes"></span><span id="non-stored__constructed_attributes"></span><span id="NON-STORED__CONSTRUCTED_ATTRIBUTES"></span>Non-stored, constructed attributes
</dt> <dd>

A user object also has constructed attributes that are not stored in the directory, but are calculated by the domain controller, such as [**canonicalName**](/windows/desktop/ADSchema/a-canonicalname) and [**allowedAttributes**](/windows/desktop/ADSchema/a-allowedattributes).

</dd> </dl>

 

 