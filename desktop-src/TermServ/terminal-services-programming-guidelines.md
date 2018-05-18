---
title: Remote Desktop Services programming guidelines
description: Topics that provide guidelines for developing applications in a Remote Desktop Services environment.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e0cd52c5-40d7-4a48-9d10-fdbcea46a5a0'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
keywords: ["Remote Desktop Services Remote Desktop Services , programming guidelines", "programming guidelines Remote Desktop Services"]
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

[Administrative Template File Format](https://msdn.microsoft.com/library/aa372405)
</dt> <dt>

[Registry Key Security and Access Rights](https://msdn.microsoft.com/library/windows/desktop/ms724878)
</dt> <dt>

[Registry Hives](https://msdn.microsoft.com/library/windows/desktop/ms724877)
</dt> <dt>

[Security Descriptors](https://msdn.microsoft.com/library/windows/desktop/aa379563)
</dt> <dt>

[Standard Access Rights](https://msdn.microsoft.com/library/windows/desktop/aa379607)
</dt> <dt>

[Access Control Model](https://msdn.microsoft.com/library/windows/desktop/aa374876)
</dt> </dl>

 

 




