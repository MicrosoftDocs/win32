---
title: Remote Desktop Services programming guidelines
description: Topics that provide guidelines for developing applications in a Remote Desktop Services environment.
ms.assetid: e0cd52c5-40d7-4a48-9d10-fdbcea46a5a0
ms.tgt_platform: multiple
keywords:
- Remote Desktop Services Remote Desktop Services , programming guidelines
- programming guidelines Remote Desktop Services
ms.topic: article
ms.date: 05/31/2018
---

# Remote Desktop Services programming guidelines

Most existing 32-bit or 64-bit Windows-based applications run "as is" in a Remote Desktop Services (formerly known as Terminal Services) environment. However, some applications function correctly and perform well in a Remote Desktop Services environment, while others do not. The following topics provide guidelines for developing applications in a Remote Desktop Services environment.

## In this section

<dl> <dt>

[Multiple-user guidelines](multiple-user-guidelines.md)
</dt> <dd>

Guidelines for developing applications for multiple users in a Remote Desktop Services environment.

</dd> <dt>

[Performance guidelines](performance-guidelines.md)
</dt> <dd>

Guidelines for developing applications that perform well in a Remote Desktop Services environment.

</dd> <dt>

[General programming guidelines](general-programming-guidelines.md)
</dt> <dd>

Guidelines for developing applications in a Remote Desktop Services environment.

</dd> </dl>

Many of these guidelines are good programming practices that will benefit applications running in any Windows environment. However, some recommended optimizations, such as limiting graphic effects, are optimizations that you would want only when your application is running under Remote Desktop Services. For a code example that shows how to detect a Remote Desktop Services environment, see [Detecting the Remote Desktop Services Environment](detecting-the-terminal-services-environment.md).

## Related topics

<dl> <dt>


</dt> <dt>

[Terminal Services Is Now Remote Desktop Services](terminal-services-is-now-remote-desktop-services.md)
</dt> <dt>

[Administrative Template File Format](/previous-versions/windows/desktop/Policy/administrative-template-file-format)
</dt> <dt>

[Registry Key Security and Access Rights](/windows/desktop/SysInfo/registry-key-security-and-access-rights)
</dt> <dt>

[Registry Hives](/windows/desktop/SysInfo/registry-hives)
</dt> <dt>

[Security Descriptors](/windows/desktop/SecAuthZ/security-descriptors)
</dt> <dt>

[Standard Access Rights](/windows/desktop/SecAuthZ/standard-access-rights)
</dt> <dt>

[Access Control Model](/windows/desktop/SecAuthZ/access-control-model)
</dt> </dl>

 

 