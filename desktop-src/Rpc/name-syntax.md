---
title: Name Syntax
description: Remote Procedure Call (RPC) and name syntax.
ms.assetid: eb370106-bd88-4c21-b287-7b2b174185d4
ms.topic: article
ms.date: 05/31/2018
---

# Name Syntax

Microsoft RPC accepts names that conform to the following syntax:

``` syntax
/.:/name[/name...]/.../domainname/name[/name...]
```

## Parameters

<dl> <dt>

<span id="name"></span><span id="NAME"></span>name
</dt> <dd>

Specifies an identifier that can contain any character except the delimiting slash (/) character.

</dd> <dt>

<span id="domainname"></span><span id="DOMAINNAME"></span>domainname
</dt> <dd>

Specifies the name of the domain.

</dd> </dl>

A parameter that selects the name-syntax type and the string that specifies the name are supplied to many of the name service interface (NSI) RPC functions.

Only one name-syntax type is supported by Microsoft RPC, as specified by the constant RPC\_C\_NS\_SYNTAX\_DCE. This constant is defined in the header file RPCNSI.H.

The name syntax specified by RPC\_C\_NS\_SYNTAX\_DCE is an extension of the OSF\_DCE Cell Directory Service (CDS) name syntax. The ability to specify a domain name represents an extension to that syntax. There is no absolute limit on the number of names that can be separated by slash characters as long as the overall string is less than 256 characters.

The slashes allow you to specify a logical structure to the name, but they do not correspond to a logical structure in the objects themselves.

 

 




