---
title: Client-Side Configuration User Interface
description: The vendor that implements the authentication protocol may also provide a configuration user interface (UI) for the protocol.
ms.assetid: 956a7ad6-1fd5-4938-aa2f-4de646dfd6c2
ms.topic: article
ms.date: 06/14/2023
ms.contributor: samyun
---

# Client-Side Configuration User Interface

The vendor that implements the authentication protocol may also provide a configuration user interface (UI) for the protocol. The configuration UI may be implemented in the same DLL as the authentication protocol, or in a separate DLL. Also, the DLL that implements the configuration UI may support more than one authentication protocol. The path to the DLL for the configuration UI is stored in the RAS\_EAP\_VALUENAME\_CONFIGUI registry value, under the key for the authentication protocol. For more information about creating this registry value, see [EAP Installation](eap-installation.md).

The DLL for the configuration user interface should export entry points for the following functions:

[**RasEapInvokeConfigUI**](/windows/desktop/api/Raseapif/nf-raseapif-raseapinvokeconfigui)

[**RasEapFreeMemory**](/windows/desktop/api/Raseapif/nf-raseapif-raseapfreememory)

When the user creates a configuration entry for a particular connection, whether for a RAS or wireless client, the user is able to select the authentication protocol that the service should use with that entry. If the authentication protocol is configurable, the service calls [**RasEapInvokeConfigUI**](/windows/desktop/api/Raseapif/nf-raseapif-raseapinvokeconfigui) to invoke the configuration UI. The configuration UI stores the configuration information returned by **RasEapInvokeConfigUI** in the configuration entry.

The configuration information should be generic to all users on the client computer. Information specific to a particular user or users should not be stored in the entry. The authentication protocol should obtain user-specific information by using the [identity functions](obtaining-identity-information.md) or [interactive user-interface](interactive-user-interface.md). The authentication protocol can store this information in the registry by passing it to the authentication service in the *pEapOutput* parameter of [**RasEapMakeMessage**](/previous-versions/windows/desktop/legacy/aa363532(v=vs.85)).

The configuration information should also not be specific to the current machine; it should be portable from machine to machine.

When the authentication service calls the [**RasEapBegin**](/previous-versions/windows/desktop/legacy/aa363520(v=vs.85)) function for the authentication protocol, it passes a [**PPP\_EAP\_INPUT**](/windows/desktop/api/Raseapif/ns-raseapif-ppp_eap_input) structure that contains a pointer to the configuration information. After the call to **RasEapBegin** completes, the authentication service calls [**RasEapFreeMemory**](/windows/desktop/api/Raseapif/nf-raseapif-raseapfreememory) to free the memory occupied by the configuration information. Therefore, the authentication protocol should copy the configuration information into a private memory buffer during the call to **RasEapBegin**.

The vendor may add a value under the registry key for the authentication protocol that specifies default configuration information for the protocol. The vendor may also add a value that specifies whether the user is required to enter configuration information when they create a phone-book entry. For more information, see [Authentication Protocol Registry Values](authentication-protocol-registry-values.md).
