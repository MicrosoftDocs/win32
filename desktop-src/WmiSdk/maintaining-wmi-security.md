---
description: WMI security focuses on protecting access to namespace data. WMI first grants access to groups of users as specified by the WMI Control and DCOM settings and then providers determine if the user should have access to namespace data.
ms.assetid: 88a2538a-ae30-4a1a-9d16-f0cd9419b2ed
ms.tgt_platform: multiple
title: Maintaining WMI Security
ms.topic: article
ms.date: 05/31/2018
---

# Maintaining WMI Security

WMI security focuses on protecting access to namespace data. WMI first grants access to groups of users as specified by the [*WMI Control*](gloss-w.md) and DCOM settings and then providers determine if the user should have access to namespace data.

The following sections are discussed in this topic:

-   [Namespace Security](#namespace-security)
-   [Distributed Component Object Model (DCOM) Security Settings.](#distributed-component-object-model-dcom-security-settings)
-   [WMI, Shared Service Hosts, and Authentication](#wmi-shared-service-hosts-and-authentication)
-   [Security for WMI Client Scripts and Applications](#security-for-wmi-client-scripts-and-applications)
-   [Related topics](#related-topics)

## Namespace Security

Namespace security depends on standard Windows user [*security identifiers (SID)*](gloss-s.md) and the [*security descriptor*](gloss-s.md) for the WMI namespace.

You can set namespace security by performing the following actions:

-   Grant or deny access rights to namespaces for users using the WMI Control or when the namespace is created. For more information, see [Setting Namespace Security with the WMI Control](setting-namespace-security-with-the-wmi-control.md) and [Setting Namespace Security When the Namespace is Created](setting-namespace-security-when-the-namespace-is-created.md).
-   Use the WMI Control Security tab to establish security auditing. Security auditing results in event log entries when a user fails or succeeds in an audited action, such as writing data to a WMI object or reading the security descriptor. For more information, see [Access to WMI Namespaces](access-to-wmi-namespaces.md).
-   Use the MOF file that defines the namespace to require a user to make an encrypted connection. For more information, see [Requiring an Encrypted Connection to a Namespace](requiring-an-encrypted-connection-to-a-namespace.md).

## Distributed Component Object Model (DCOM) Security Settings.

DCOM security requires an authentication setting and an impersonation setting. Authentication means that one process identifies itself to another. Impersonation identifies the authority that a client grants a server to call different processes. During a security check, the server impersonates the client. For more information, see [Securing C++ Clients and Providers](securing-c---clients-and-providers.md) or [Securing Scripting Clients](securing-scripting-clients.md).

Scripts and C/C++/C# applications either establish an authentication and impersonation levels when they connect to a WMI namespace or they use the default settings. Connections to remote computers require different settings than to the WMI namespaces on the local computer. For more information, see [Connecting to WMI on a Remote Computer](connecting-to-wmi-on-a-remote-computer.md).

## WMI, Shared Service Hosts, and Authentication

WMI resides in a shared service host with several other services running under the NetworkService account. In a Svchost process, WMI shares the same authentication as the other processes in the host.

Provider DLLs are loaded into separate service host processes from WMI. The **HostingModel** property in the [**\_\_Win32Provider**](--win32provider.md) system class that represents a provider specifies the system account under which the provider runs. Setting this property causes the provider to be loaded into a shared host process that has a specified level of privilege. For more information, see [Provider Hosting and Security](provider-hosting-and-security.md).

## Security for WMI Client Scripts and Applications

Scripts and applications must establish the correct security to connect to WMI namespaces on local and remote computers. For more information, see [Securing C++ Clients and Providers](securing-c---clients-and-providers.md), [Securing Scripting Clients](securing-scripting-clients.md), and [Securing WMI Events](securing-wmi-events.md).

The following table lists the topics on maintaining WMI security.



| Topic                                                                                              | Description                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Securing WMI Namespaces](securing-wmi-namespaces.md)                                             | You can limit namespace data access to authorized users through the WMI Control.                                                                                      |
| [Securing Your Provider](securing-your-provider.md)                                               | Information about writing secure providers.                                                                                                                           |
| [Securing C++ Clients and Providers](securing-c---clients-and-providers.md)                       | Both C++ providers and client applications must perform many of the same operations to maintain WMI security.                                                         |
| [Securing Scripting Clients](securing-scripting-clients.md)                                       | Scripts and Visual Basic applications (automation clients) must set appropriate security to get access to WMI data and events.                                        |
| [Securing WMI Events](securing-wmi-events.md)                                                     | WMI events are delivered by the event provider to a temporary or permanent consumer. Events are delivered in the form of an instance of an event class.               |
| [Changing Access Security on Securable Objects](changing-access-security-on-securable-objects.md) | With appropriate permissions, you can call methods on the WMI objects that represent securable objects that read or change security descriptors on securable objects. |



 

## Related topics

<dl> <dt>

[Using WMI](using-wmi.md)
</dt> </dl>

 

 



