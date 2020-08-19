---
title: Remote Registry Access in 64-bit Windows
description: The registry redirector provides remote access to the registry on 64-bit Windows through the RegConnectRegistry function.
ms.assetid: 7873c1e2-53fb-4c93-bf4c-251a13cd8db7
keywords:
- remote registry access 64-bit Windows Programming
ms.topic: article
ms.date: 05/31/2018
---

# Remote Registry Access in 64-bit Windows

The registry redirector provides remote access to the registry on 64-bit Windows through the [**RegConnectRegistry**](/windows/desktop/api/winreg/nf-winreg-regconnectregistrya) function.

If the client is a 32-bit application, it accesses the server's default 32-bit registry view. If the client is a 64-bit application, it accesses the 64-bit registry view.

**Windows Server 2003:** All clients access the 64-bit registry view unless the application uses the KEY\_WOW64\_32KEY flag. This behavior changed with Windows Server 2003 with Service Pack 1 (SP1) and Windows XP Professional x64 Edition, provided that both the client and the server are running these versions of Windows.

## Related topics

<dl> <dt>

[Registry Redirector](registry-redirector.md)
</dt> <dt>

[Registry Reflection](registry-reflection.md)
</dt> </dl>

 

 