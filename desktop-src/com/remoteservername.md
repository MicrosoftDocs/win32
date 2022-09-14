---
title: RemoteServerName
description: Configures the client to request the object be run at a particular computer whenever an activation function is called for which a COSERVERINFO structure is not specified.
ms.assetid: 0413564e-e8ba-4e6e-ad29-62997c63aab3
keywords:
- RemoteServerName registry value COM
ms.topic: article
ms.date: 05/31/2018
---

# RemoteServerName

Configures the client to request the object be run at a particular computer whenever an activation function is called for which a [**COSERVERINFO**](/windows/win32/api/objidlbase/ns-objidlbase-coserverinfo) structure is not specified.

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Classes\AppID
   {AppID_GUID}
      RemoteServerName = name
```

## Remarks

**RemoteServerName** allows simple configuration management of client applications; they may be written without hard-coded server names and can be configured by modifying the **RemoteServerName** registry values of the classes of objects they use.

As described in the documentation for the [**CLSCTX**](/windows/win32/api/wtypesbase/ne-wtypesbase-clsctx) enumeration and the [**COSERVERINFO**](/windows/win32/api/objidlbase/ns-objidlbase-coserverinfo) structure, one of the parameters of the distributed COM activation is a pointer to a **COSERVERINFO** structure. When this value is not **NULL**, the information in the **COSERVERINFO** structure overrides the setting of the **RemoteServerName** key for the function call.

## Related topics

<dl> <dt>

[Registering COM Servers](registering-com-servers.md)
</dt> </dl>

 

 