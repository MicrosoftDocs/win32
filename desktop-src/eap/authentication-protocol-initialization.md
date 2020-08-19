---
title: Authentication Protocol Initialization
description: The EAP secured connection is initialized between the client and server in similar ways for RAS and wireless (802.1X) clients.
ms.assetid: 1cd5bfc9-2ba3-477c-9bbb-73578a5623c2
ms.topic: article
ms.date: 05/31/2018
---

# Authentication Protocol Initialization

The EAP secured connection is initialized between the client and server in similar ways for RAS and wireless (802.1X) clients.

## Client

When the client attempts to establish the connection, the authentication service obtains [identity information](obtaining-identity-information.md) for the user. If the **RAS\_EAP\_VALUENAME\_INVOKE\_NAMEDLG** value is present in the registry for this authentication protocol and this value is set to zero, the authentication service calls [**RasEapGetIdentity**](/previous-versions/windows/desktop/api/Raseapif/nf-raseapif-raseapgetidentity). This function typically displays a user interface that allows the identity information to be of a type specific to the authentication protocol; for example, a certificate or numeric ID. If **RAS\_EAP\_VALUENAME\_INVOKE\_NAMEDLG** is not present, or is set to one, the authentication service displays the standard system user-name dialog.

Once the authentication service has obtained the identity information for the user, it calls the authentication protocol's implementation of [**RasEapBegin**](/previous-versions/windows/desktop/legacy/aa363520(v=vs.85)). This call allows the authentication protocol to allocate and initialize a work buffer that the service passes on subsequent calls to [**RasEapMakeMessage**](/previous-versions/windows/desktop/legacy/aa363532(v=vs.85)) and [**RasEapEnd**](/previous-versions/windows/desktop/legacy/aa363521(v=vs.85)). The work buffer is opaque to the service and never accesses the contents of the work buffer. If the authentication protocol creates a distinct work buffer for each EAP session, then the work buffer is session and thread safe. Because the authentication protocol allocates the memory for the work buffer, the authentication protocol should also free this memory using the [**RasEapFreeMemory**](/previous-versions/windows/desktop/api/Raseapif/nf-raseapif-raseapfreememory) function.

In the call to [**RasEapBegin**](/previous-versions/windows/desktop/legacy/aa363520(v=vs.85)), the service also passes a [**PPP\_EAP\_INPUT**](/windows/desktop/api/Raseapif/ns-raseapif-ppp_eap_input) structure that contains pointers to the configuration information for the connection, and the identity information for the user. The service always passes in a value for the **pszIdentity** member of **PPP\_EAP\_INPUT**. However, the **pszPassword** member of [**PPP\_EAP\_INPUT**](/windows/desktop/api/Raseapif/ns-raseapif-ppp_eap_input) may be **NULL**.

Within the [**PPP\_EAP\_INPUT**](/windows/desktop/api/Raseapif/ns-raseapif-ppp_eap_input) structure, the **fAuthenticator** member indicates whether the authentication protocol is being invoked to be authenticated (on the client) or as the authenticator (on the server).

## Server

On the server, the **bInitialID** member of [**PPP\_EAP\_INPUT**](/windows/desktop/api/Raseapif/ns-raseapif-ppp_eap_input) specifies the ID that the server uses for the first EAP packet. The server increments this ID for subsequent packets.

Also on the server, the **pUserAttributes** pointer in [**PPP\_EAP\_INPUT**](/windows/desktop/api/Raseapif/ns-raseapif-ppp_eap_input) points to an array of attributes of the [**RAS\_AUTH\_ATTRIBUTE\_TYPE**](/windows/win32/api/raseapif/ne-raseapif-ras_auth_attribute_type) type. These are attributes for the user that were obtained from the client.

If the [**RasEapBegin**](/previous-versions/windows/desktop/legacy/aa363520(v=vs.85)) call returns any value other than **NO\_ERROR**, the session is disconnected. The returned error is logged (on the server), or displayed to the user (on the client).

 

 