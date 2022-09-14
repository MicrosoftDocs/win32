---
title: Deciding What to Find
description: Before you search a directory, consider how your search will perform based on your approach. The data and properties to be returned affect where you bind to start a search, the depth of your search, your query filter, and search performance.
ms.assetid: 788fa12c-9086-4d8b-bd2e-e96a494a26ad
ms.tgt_platform: multiple
keywords:
- search criteria Active Directory
- deciding what to find Active Directory
ms.topic: article
ms.date: 05/31/2018
---

# Deciding What to Find

Before you search a directory, consider how your search will perform based on your approach. The data and properties to be returned affect where you bind to start a search, the depth of your search, your query filter, and search performance.

For example, if you want search for all user objects with surname Smith:



| Area                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Where to search            | A specific container or organizational unit (OU) within a domain, a specific domain, a specific domain tree, or the entire forest. If you search for objects within a specific container or domain, the search query will perform better by binding directly to that container or domain   instead of performing a subtree search on a domain tree.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Type of search             | If you verify the existence of, or retrieve the properties of a particular object that has a distinguished name (DN) you already know, you should perform a base search, which searches only the object you have bound to.<br/> If you know an object is a direct descendant of a particular container, bind to that container and do a one-level search (**attributeSchema** and **classSchema** objects in the schema container and extended-right objects in the extended-rights container are good examples).<br/> If you do not know exactly where the object is, or if you want to search the object you have bound to and all the child objects below it in the directory hierarchy, perform a subtree search.<br/>                                                       |
| Use indexes where possible | Finally, if you look for a specific class of object, the query filter should have expressions that evaluate properties that are defined for that class.<br/> To search for group objects, include the expression (objectCategory=group) in the filter. To search for user objects, specify (&(objectClass=user)(objectCategory=person)) because the computer class derives from the user class, so (objectClass=user) would return both users and computers and also because both contact and user objects have an **objectCategory** of person, so (objectCategory=person) would return both users and contacts.<br/> For more information, see [Object Class and Object Category](object-class-and-object-category.md) and [Indexed Attributes](indexed-attributes.md).<br/> |



 

 

 





