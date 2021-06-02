---
description: You can control the ability of a process to access securable objects or to perform system administration tasks.
ms.assetid: a5d8eaaa-4585-44a3-ab92-2a323d9af80c
title: Specifying a Security Descriptor From an INF File
ms.topic: article
ms.date: 05/31/2018
---

# Specifying a Security Descriptor From an INF File

You can control the ability of a process to access securable objects or to perform system administration tasks. A securable object is an object that can have a security descriptor. All named objects are securable. Some unnamed objects, such as process and thread objects, can have security descriptors too. For more information about controlling access to securable objects see [Access Control](/windows/desktop/SecAuthZ/access-control).

[Security descriptors](/windows/desktop/SecAuthZ/security-descriptors) contain the security information associated with securable objects. For most securable objects, you can specify an object's security descriptor in the function call that creates the object. For example, you can specify a security descriptor in the [**CreateFile**](/windows/desktop/api/fileapi/nf-fileapi-createfilea) and [**CreateProcess**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-createprocessa) functions.

To set a security descriptor from an INF file, add an INF-writer authored Security section immediately following the section that installs the file, registry key, or component. The Security section should contain one line with the string security descriptor written on it using the format for [Security Descriptor Strings](/windows/desktop/SecAuthZ/security-descriptor-strings). The line should also be enclosed by quotation marks (").

For example, the following INF file snippet would create a registry key to which only administrators and the system have access. Note that this example requires administrative privileges.

``` syntax
[DDInstall]
AddReg=mydevice.reg
 
[mydevice.reg]
include Registry information here
 
[mydevice.reg.Security]
"D:P(A;CI;GA;;;BA)(A;CI;GA;;;SY)"
```

In this case, the meaning of the string is that administrators have full control, system has full control, and access is inheritable to all subkeys. For more information see [Security Descriptor Definition Language](/windows/desktop/SecAuthZ/security-descriptor-definition-language).

 

 
