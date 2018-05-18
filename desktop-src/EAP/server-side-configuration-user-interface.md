---
title: Server-Side Configuration User Interface
description: Implement a configuration UI for the server by implementing the COM interface, IEAPProviderConfig.
ms.assetid: 'b205c573-6694-42c0-b4f1-1480932dd644'
---

# Server-Side Configuration User Interface

Implement a configuration UI for the server by implementing the COM interface, [**IEAPProviderConfig**](ieapproviderconfig.md). This COM interface derives from [**IUnknown**](_com_iunknown) and adds three methods: [**IEAPProviderConfig::Initialize**](ieapproviderconfig-initialize.md), [**IEAPProviderConfig::ServerInvokeConfigUI**](ieapproviderconfig-serverinvokeconfigui.md), and [**IEAPProviderConfig::Uninitialize**](ieapproviderconfig-uninitialize.md).

The UI should support remote administration. In other words, although the UI will configure the authentication protocol on the server, the UI itself may be running on a different computer. To support remote administration, separate the UI code from the code that actually performs the configuration. The configuration code resides on the server on which the authentication protocol runs.

Use the Active Template Library (ATL) to implement [**IEAPProviderConfig**](ieapproviderconfig.md). For more information, see the sample server-side configuration UI in the SDK samples directory. The class identifier (CLSID) for the configuration UI object should be placed in the registry with a value name of [RAS\_EAP\_VALUENAME\_CONFIG\_CLSID](authentication-protocol-registry-values.md#ras-eap-valuename-config-clsid). For more information, see [Authentication Protocol Registry Values](authentication-protocol-registry-values.md).

When the user clicks the Configure button for an authentication protocol in the Properties dialog box for Routing and RAS, the system checks whether a RAS\_EAP\_VALUENAME\_CONFIG\_CLSID value for this authentication protocol exists in the registry. If so, COM instantiates the configuration UI object. If the system is unable to find RAS\_EAP\_VALUENAME\_CONFIG\_CLSID in the registry and the system has access to Directory Services (DS), the system attempts to instantiate the object from the Class Store.

In the case where the user is connected to multiple machines simultaneously, multiple configuration UI objects are instantiated.

 

 




