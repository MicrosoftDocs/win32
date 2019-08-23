---
title: Creating a Query Filter
description: A query filter instructs Active Directory Domain Services to find data in an LDAP query syntax. All the specified data access technologies listed in the Choosing the Search Technology topic support LDAP query syntax.
ms.assetid: 0bd652f0-41a6-4a0d-8742-9d6a2a7f168a
ms.tgt_platform: multiple
keywords:
- Active Directory examples Active Directory , creating a query filter
- query filters
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Query Filter

A query filter instructs Active Directory Domain Services to find data in an LDAP query syntax. All the specified data access technologies listed in the [Choosing the Search Technology](choosing-the-search-technology.md) topic support LDAP query syntax.

The LDAP query syntax is as follows:


```C++
<expression><expression>...
```



A filter can contain one, or more, expressions. An expression has the following form:


```C++
(<logicaloperator><comparison><comparison...>)
```



where "&lt;logicaloperator&gt;" is one of the following.



| Operator        | Description                |
|-----------------|----------------------------|
| "\|"<br/> | Logical **OR**<br/>  |
| "&"<br/>  | Logical **AND**<br/> |
| "!"<br/>  | Logical **NOT**<br/> |



 

and "&lt;comparison&gt;" is the following:


```C++
(<attribute><operator><value>)
```



where "&lt;attribute&gt;" is the **lDAPDisplayName** of the attribute to evaluate, "&lt;value&gt;" is the value to compare against, and "&lt;operator&gt;" is one of the following comparison operators.



| Operator           | Description                         |
|--------------------|-------------------------------------|
| "="<br/>     | Equals<br/>                   |
| "~="<br/>    | Approximately equals<br/>     |
| "<="<br/> | Less than or equal to<br/>    |
| ">="<br/> | Greater than or equal to<br/> |



 

In addition, depending on the attribute syntax, the "&lt;value&gt;" may contain the wildcard symbol ("\*"). A "&lt;value&gt;" that contains only a wildcard will check for the existence of any value in "&lt;attribute&gt;". If no value is set for "&lt;attribute&gt;", the test will fail.

If any of the following special characters must appear in the query filter as literals, they must be replaced by the listed escape sequence.



| ASCII character    | Escape sequence substitute |
|--------------------|----------------------------|
| \*<br/>      | "\\2a"<br/>          |
| (<br/>       | "\\28"<br/>          |
| )<br/>       | "\\29"<br/>          |
| \\<br/>      | "\\5c"<br/>          |
| **NUL**<br/> | "\\00"<br/>          |



 

In addition, arbitrary binary data may be represented using the escape sequence syntax by encoding each byte of binary data with the backslash followed by two hexadecimal digits. For example, the four-byte value 0x00000004 is encoded as "\\00\\00\\00\\04" in a filter string.

## Examples

The following query string will search for all objects of type "computer".


```C++
(objectCategory=computer)
```



The following query string will search for all objects of type "computer" with a name that begins with "desktop".


```C++
(&(objectCategory=computer)(name=desktop*))
```



The following query string will search for all objects of type "computer" with a name that begins with "desktop" or a name that begins with "notebook".


```C++
(&(objectCategory=computer)(|(name=desktop*)(name=notebook*)))
```



The following query string will search for all objects of type "user" that have a home phone number.


```C++
(&(objectCategory=user)(homePhone=*))
```



For more information about query filter strings, and usage examples, see:

-   [Finding Objects by Class](finding-objects-by-class.md)
-   [Finding Objects by Name](finding-objects-by-name.md)
-   [Finding a List of Attributes To Query](finding-a-list-of-attributes-to-query.md)
-   [Checking the Query Filter Syntax](checking-the-query-filter-syntax.md)
-   [How to Specify Comparison Values](how-to-specify-comparison-values.md)

 

 





