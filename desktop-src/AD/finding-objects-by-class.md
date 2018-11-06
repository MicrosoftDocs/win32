---
title: Finding Objects by Class
description: A typical search queries for a specific object class.
ms.assetid: 1805f98a-7e6b-4b4a-b173-dfb5d17e539a
ms.tgt_platform: multiple
keywords:
- Finding Objects by Class AD
- Active Directory, using, searching, by class
- object AD , searching by class
ms.topic: article
ms.date: 05/31/2018
---

# Finding Objects by Class

A typical search queries for a specific object class. The following code example searches for computers with location in Building 7N.


```C++
(&(objectCategory=computer)(location=Building 7N))
```



Consider why **objectClass** is not used. Do not use **objectClass** without another comparison that contains an indexed attribute. Index attributes can increase the efficiency of a query. The **objectClass** attribute is multi-valued and not indexed. To specify the type or class of an object, use **objectCategory**.

Less efficient:


```C++
(objectClass=computer)
```



More Efficient:


```C++
(objectCategory=computer)
```



Be aware that there are some cases where a combination of **objectClass** and **objectCategory** must be used. The user class and contact class should be specified as follows.


```C++
(&(objectClass=user)(objectCategory=person))
 
(&(objectClass=contact)(objectCategory=person))
```



Be aware that you could search for both users and contacts with the following.


```C++
(objectCategory=person)
```



 

 




