---
title: objectCategory vs. objectClass
description: Both the objectCategory and objectClass attributes can refer to a given schema class of a directory object.
ms.assetid: 66dadedb-61e4-4184-9b87-0fff036a94d9
ms.tgt_platform: multiple
keywords:
- objectCategory vs. objectClass ADSI
- attributes ASI , searching on objectCategory and objectClass attributes
ms.topic: article
ms.date: 05/31/2018
---

# objectCategory vs. objectClass

Both the **objectCategory** and **objectClass** attributes can refer to a given schema class of a directory object. However, there is an important distinction in semantics between the two. "objectClass=joy" refers to such directory objects in which "joy" represents any class in the object class hierarchy. "objectCategory=joy", on the other hand, refers to those directory objects in which "joy" identifies a specific class in the object class hierarchy.

**objectClass** can take multiple values whereas **objectCategory** takes a single value. Because of this, **objectCategory** is better suited for type matching of objects in a directory search. ADSI uses this as the default matching criterion. Searches using one **objectClass** are not scalable to large databases. ADSI supports "(objectCategory=SomeDN)" and "(objectCategory=Ldap\_Display\_Name\_of\_Class)" syntaxes.

The exception to all of this is that the LDAP search filter "(objectClass=\*)" does not specify a search on object class, but merely tests for the presence of the objects.

 

 




