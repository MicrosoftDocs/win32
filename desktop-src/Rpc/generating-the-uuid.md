---
title: Generating the UUID
description: The first step in defining the interface is to use the uuidgen utility to generate a universally unique identifier (UUID).
ms.assetid: 870641b7-affc-4de4-bc7f-4c8ca2873fb6
keywords:
- Remote Procedure Call RPC , tasks, generating the UUID
ms.topic: article
ms.date: 05/31/2018
---

# Generating the UUID

The first step in defining the interface is to use the **uuidgen** utility to generate a universally unique identifier (UUID). A UUID enables the client and server applications identify each other. The **uuidgen** utility (Uuidgen.exe) is automatically installed when you install the Platform Software Development Kit (SDK).

The following command generates a UUID and creates a template file called Hello.idl.

**uuidgen /i /ohello.idl**

Your hello.idl template will look like this (with a different UUID, of course).

``` syntax
[
    uuid(7a98c250-6808-11cf-b73b-00aa00b677a7),
    version(1.0)
]
interface INTERFACENAME
{
 
}
```

 

 




