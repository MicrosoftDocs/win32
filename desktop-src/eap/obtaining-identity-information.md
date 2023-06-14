---
title: Obtaining Identity Information
description: The vendor that implements the authentication protocol may also provide a function interface that obtains initial identifying information for the user requesting authentication.
ms.assetid: 773c9fdb-c810-4cea-afed-df6484a9c9c9
ms.topic: article
ms.date: 06/14/2023
ms.contributor: samyun
---

# Obtaining Identity Information

The vendor that implements the authentication protocol may also provide a function interface that obtains initial identifying information for the user requesting authentication.

The vendor should implement the following functions.

- [**RasEapGetIdentity**](/windows/desktop/api/Raseapif/nf-raseapif-raseapgetidentity)
- [**RasEapFreeMemory**](/windows/desktop/api/Raseapif/nf-raseapif-raseapfreememory)

These functions may be implemented in the same DLL as the authentication protocol, or in a separate DLL. Also, the DLL that implements the identity functions may support more than one authentication protocol. The path to the DLL for these functions is stored in the [RAS\_EAP\_VALUENAME\_IDENTITY](authentication-protocol-registry-values.md) registry value, under the key for the authentication protocol. For more information about creating this registry value, see [EAP Installation](eap-installation.md).

The [**RasEapGetIdentity**](/windows/desktop/api/Raseapif/nf-raseapif-raseapgetidentity) function typically displays a user interface (UI) to obtain identity information for the user. However, if the *dwFlags* parameter contains the RAS\_EAP\_FLAG\_NON\_INTERACTIVE flag, **RasEapGetIdentity** should not display a UI.

If [**RasEapGetIdentity**](/windows/desktop/api/Raseapif/nf-raseapif-raseapgetidentity) does display a UI, the UI must support [**WM\_COMMAND**](../menurc/wm-command.md) messages where the value of [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85))(*wParam*) is equal to IDCANCEL.

The authentication service calls [**RasEapGetIdentity**](/windows/desktop/api/Raseapif/nf-raseapif-raseapgetidentity) if the [RAS\_EAP\_VALUENAME\_INVOKE\_NAMEDLG](authentication-protocol-registry-values.md) value that is in the registry for this EAP is set to zero. If RAS\_EAP\_VALUENAME\_INVOKE\_NAMEDLG is not present, or is present and is set to one, the authentication service displays the standard system user name dialog box.

In addition to RAS\_EAP\_VALUENAME\_INVOKE\_NAMEDLG, the EAP vendor may create a related value, [RAS\_EAP\_VALUENAME\_INVOKE\_PWDDLG](authentication-protocol-registry-values.md), in the registry. If this value is present and is set to zero, the service will not display the standard system password dialog. This value is useful when implementing a biometric method such as a fingerprint scan to authenticate the user. If both the RAS\_EAP\_VALUENAME\_INVOKE\_NAMEDLG and RAS\_EAP\_VALUENAME\_INVOKE\_PWDDLG values are zero, an identity UI could be used to obtain both the identity and biometric information. However, if only RAS\_EAP\_VALUENAME\_INVOKE\_PWDDLG is zero, the authentication service will not call [**RasEapGetIdentity**](/windows/desktop/api/Raseapif/nf-raseapif-raseapgetidentity). In this case, you could use the [interactive user interface](interactive-user-interface.md) to obtain the biometric information.

For more information on these registry values, see [Authentication Protocol Registry Values](authentication-protocol-registry-values.md).

The information obtained by [**RasEapGetIdentity**](/windows/desktop/api/Raseapif/nf-raseapif-raseapgetidentity) is passed to the authentication protocol during the call to [**RasEapBegin**](/previous-versions/windows/desktop/legacy/aa363520(v=vs.85)). The information is pointed to by the **pszIdentity** and **pUserData** members of the [**PPP\_EAP\_INPUT**](/windows/desktop/api/Raseapif/ns-raseapif-ppp_eap_input) structure. To save this information in the registry on the client computer, the authentication protocol should return the information in the *pEapOutput* parameter of [**RasEapMakeMessage**](/previous-versions/windows/desktop/legacy/aa363532(v=vs.85)).

After the call to [**RasEapBegin**](/previous-versions/windows/desktop/legacy/aa363520(v=vs.85)), the authentication service calls [**RasEapFreeMemory**](/windows/desktop/api/Raseapif/nf-raseapif-raseapfreememory) to free the memory occupied by this data. Therefore, the authentication protocol should copy the information into a private memory buffer during the call to **RasEapBegin**.
