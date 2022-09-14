---
title: Virtual Channel Client Registration
description: You must store the name of the client DLL in the registry.
ms.assetid: bf84b2f4-55c2-45fd-bba7-8ff3efe4b1fd
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Virtual Channel Client Registration

You must store the name of the client DLL in the registry.

In the registry, add a subkey to one of the following locations:

**HKEY\_CURRENT\_USER**\\**Software**\\**Microsoft**\\**Terminal Server Client**\\**Default**\\**Addins**

**HKEY\_CURRENT\_USER**\\**Software**\\**Microsoft**\\**Terminal Server Client**\\**connection**\\**Addins**

> [!Note]  
> In the registry path, *connection* represents the name of a connection in Connection Manager.

 

Entries under the **\\Default\\Addins** key apply to all connections. Entries under the **\\***connection***\\Addins** key apply only to the connection identified by *connection*. Connections can be created and managed by using Connection Manager.

The subkey can be given any name. It must contain a **REG\_SZ** or **REG\_EXPAND\_SZ** value and may optionally contain a **REG\_DWORD** value. The syntax of the **REG\_SZ** or **REG\_EXPAND\_SZ** value is as follows.

``` syntax
Name = DLLname
```

If **Name** is a **REG\_EXPAND\_SZ** value, it can contain unexpanded environment variables that are expanded at runtime.

The value of *DLLname* can be a fully qualified path. If *DLLname* does not contain a path, the standard DLL search strategy is used. For more information, see the Remarks section for [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya).

 

 