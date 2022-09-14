---
title: Using Remote Desktop Services
description: How to program in the Remote Desktop Services environment and how to extend Remote Desktop Services (formerly known as Terminal Services) technology to the web by using Remote Desktop Web Connection.
ms.assetid: 17a8055c-3fde-4ba0-9ed9-af0ebe0a36b9
ms.tgt_platform: multiple
keywords:
- Remote Desktop Services Remote Desktop Services , using
ms.topic: article
ms.date: 05/31/2018
---

# Using Remote Desktop Services

The following sections describe how to program in the Remote Desktop Services environment and how to extend Remote Desktop Services (formerly known as Terminal Services) technology to the web by using Remote Desktop Web Connection. If you are looking for user information for Remote Desktop connections, See [Connect to another computer using Remote Desktop Connection](https://windows.microsoft.com/windows/connect-using-remote-desktop-connection#connect-using-remote-desktop-connection=windows-7).

> [!Note]  
> This topic is for software developers.

 

## In this section

<dl> <dt>

[Detecting Whether the Remote Desktop Services Role Is Installed](detecting-whether-terminal-services-is-installed.md)
</dt> <dd>

C# code example that shows a method that returns **True** if the Remote Desktop Services server role is installed and running or **false** otherwise, beginning with Windows Server 2008.

</dd> <dt>

[Extending Terminal Services Session Broker](extending-ts-session-broker.md)
</dt> <dd>

You can extend TS Session Broker by using the [**IWTSSBPlugin**](/windows/desktop/api/Tssbx/nn-tssbx-iwtssbplugin) COM interface.

</dd> <dt>

[Implementing a Custom Audio Endpoint Enumerator](implementing-an-audio-endpoint-enumerator.md)
</dt> <dd>

Beginning with Windows Server 2008 R2, you can implement a custom remote audio endpoint enumerator as part of a Remote Desktop protocol provider.

</dd> <dt>

[Session Monikers](session-monikers.md)
</dt> <dd>

Distributed COM (DCOM) enables object activation on a per-session basis by using a system-supplied session moniker.

</dd> <dt>

[Using the ADSI Extension for Remote Desktop Services User Configuration](using-the-adsi-extension-for-terminal-services-user-configuration.md)
</dt> <dd>

Administration of Remote Desktop Services-specific user properties is possible by using the methods implemented by the Active Directory Service Interfaces (ADSI) extension, which is packaged with the dynamic-link library Tsuserex.dll.

</dd> <dt>

[Using the Remote Desktop Services API](using-the-terminal-services-api.md)
</dt> <dd>

Describes how you can use the Remote Desktop Services API to enable applications to perform tasks in a Remote Desktop Services environment.

</dd> <dt>

[Using the Remote Desktop Virtualization API](using-the-remote-desktop-virtualization-api.md)
</dt> <dd>

Developers can use this API to customize the logic that Remote Desktop Connection Broker (RD Connection Broker) uses to determine the best destination for an incoming client connection.

</dd> <dt>

[WSDL Interface for Custom VDI Solutions](wsdl-interface-for-custom-vdi-solutions.md)
</dt> <dd>

Developers can create custom web services that manage virtual desktop infrastructure (VDI) solutions.

</dd> </dl>

For more information, see [Remote Desktop Services Programming Guidelines](terminal-services-programming-guidelines.md).

## Related topics

<dl> <dt>

[Terminal Services Is Now Remote Desktop Services](terminal-services-is-now-remote-desktop-services.md)
</dt> <dt>

[Detecting the Remote Desktop Services Environment](detecting-the-terminal-services-environment.md)
</dt> </dl>

 

 




