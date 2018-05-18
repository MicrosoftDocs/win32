---
title: Setting Up the Extension DLLs
description: At startup, NPS checks the registry for a list of third-party DLLs to call.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 'fbbd9031-3ebe-47b8-8d8b-e359fa7d4b67'
ms.prod: 'windows-server-dev'
ms.technology: 'network-policy-and-access-services'
ms.tgt_platform: multiple
---

# Setting Up the Extension DLLs

> [!Note]  
> Internet Authentication Service (IAS) was renamed Network Policy Server (NPS) starting with Windows Server 2008. The content of this topic applies to both IAS and NPS. Throughout the text, NPS is used to refer to all versions of the service, including the versions originally referred to as IAS.

 

At startup, NPS checks the registry for a list of third-party DLLs to call.

To set up an Authentication or Authorization DLL on an NPS server, list the paths to the DLLs in values below the following registry key:

**HKLM\\System\\CurrentControlSet\\Services\\AuthSrv\\Parameters\\**

If the **AuthSrv** and **Parameters** keys do not exist, create them.

The value in which to list the Authentication Extension DLLs is:

**ExtensionDLLs**

The value in which to list the Authorization Extension DLLs is:

**AuthorizationDLLs**

Both the **ExtensionDLLs** and **AuthorizationDLLs** values must be of type **REG\_MULTI\_SZ**. This type allows you to list multiple DLLs.

## Related topics

<dl> <dt>

[Invoking the Extension DLLs](https://msdn.microsoft.com/library/bb891988)
</dt> <dt>

[User Identification Attributes](https://msdn.microsoft.com/library/bb892029)
</dt> </dl>

 

 




