---
title: Extending Terminal Services Session Broker
description: You can extend TS \ 160;Session Broker by using the IWTSSBPlugin COM interface.
ms.assetid: f111d6e6-90ca-4eff-ab0e-02de25f7d6ad
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Extending Terminal Services Session Broker

Terminal Services Session Broker (TS Session Broker) determines whether a user who initiates a connection has a session open already. If so, TS Session Broker routes the incoming connection to the Remote Desktop Session Host (RD Session Host) server with the existing session. If not, TS Session Broker routes the incoming connection to the RD Session Host server with the fewest sessions.

You can extend TS Session Broker by using the [**IWTSSBPlugin**](/windows/desktop/api/Tssbx/nn-tssbx-iwtssbplugin) COM interface. You can use this interface to manage connections to RD Session Host servers as well as any kind of Remote Desktop Protocol (RDP) connection, for example, connections to guest virtual machines that are running Windows Vista Enterprise Centralized Desktop (VECD) on a Windows Server 2008 Hyper-V virtual machine host.

The [**IWTSSBPlugin**](/windows/desktop/api/Tssbx/nn-tssbx-iwtssbplugin) interface offers several benefits:

-   It is not necessary to install an agent on the client or the RD Session Host server.
-   The plug-in can interact seamlessly with other Remote Desktop Services role services, such as Remote Desktop Gateway (RD Gateway), and rely on information from TS Session Broker about session and computer states.
-   You can use the plug-in to manage connections with client or server devices that support RDP 5.2 or later.
-   You can use the plug-in to enable Windows Vista Enterprise Centralized Desktop solutions.

When you implement the methods of this interface, keep the following points in mind:

-   TS Session Broker might call the methods of this COM object from multiple threads.
-   If any of the called methods do not return immediately and successfully, TS Session Broker makes no more calls to the plug-in and reverts to its native load-balancing logic. To resume calls to the plug-in, you must restart the Terminal Services Session Broker service.
-   You must register the plug-in as a system-wide COM object by using Regsvr32.exe. Because the Terminal Services Session Broker service runs under the "NetworkService" account, you must give the "NetworkService" account the required launch, activation, and access permissions by using Dcomcnfg.exe. The Terminal Services Session Broker service looks for the CLSID of the COM object that represents the plug-in in the following registry subkey:

    **HKEY\_LOCAL\_MACHINE**\\**SYSTEM**\\**CurrentControlSet**\\**Services**\\**Tssdis**\\**Parameters**\\**ExtensibilityPluginCLSID**

For more information about Dcomcnfg.exe, see [Enabling COM Security Using DCOMCNFG](/windows/desktop/com/enabling-com-security-using-dcomcnfg).

## Related topics

<dl> <dt>

[**IWTSSBPlugin**](/windows/desktop/api/Tssbx/nn-tssbx-iwtssbplugin)
</dt> </dl>

 

 