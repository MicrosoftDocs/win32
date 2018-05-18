---
title: Interactive User Interface
description: The vendor that implements the authentication protocol may also provide an interactive user interface (UI) for the protocol.
ms.assetid: '4f8ba0a4-3b52-4e7c-9e67-748f8d81d7a2'
---

# Interactive User Interface

The vendor that implements the authentication protocol may also provide an interactive user interface (UI) for the protocol. The interactive UI allows the authentication protocol to obtain additional information from the user as needed during the course of the authentication session.

The interactive UI can be implemented in the same DLL as the authentication protocol or in a separate DLL. Also, the DLL that implements the interactive UI can support more than one authentication protocol. The path to the DLL for the interactive UI is stored in the [RAS\_EAP\_VALUENAME\_INTERACTIVEUI](authentication-protocol-registry-values.md#ras-eap-valuename-interactiveui) registry value, under the key for the authentication protocol. For more information about creating this registry value, see [EAP Installation](eap-installation.md).

The DLL for the interactive UI should export entry points for the following functions:<dl>

[**RasEapInvokeInteractiveUI**](raseapinvokeinteractiveui.md)  
[**RasEapFreeMemory**](raseapfreememory.md)  
</dl>

The interactive user interface must support [**WM\_COMMAND**](_win32_wm_command_cpp) messages where [**LOWORD**](_win32_loword_cpp)(*wParam*) equals IDCANCEL.

To display the interactive UI, the authentication protocol should set the **fInvokeInteractiveUI** member of the [**PPP\_EAP\_OUTPUT**](ppp-eap-output.md) structure to **TRUE**. The authentication protocol may optionally set the **pUIContextData** and **dwSizeOfUIContextData** members to **TRUE** as well. The authentication service uses the values of these members to pass context data to the interactive UI. The authentication protocol returns the **PPP\_EAP\_OUTPUT** structure as a parameter in the [**RasEapMakeMessage**](raseapmakemessage.md) function.

The authentication service invokes the interactive UI by calling [**RasEapInvokeInteractiveUI**](raseapinvokeinteractiveui.md). The service then passes the authentication protocol a pointer to the data returned by the interactive UI in the subsequent call to [**RasEapMakeMessage**](raseapmakemessage.md). The pointer is passed as a member of a [**PPP\_EAP\_INPUT**](ppp-eap-input.md) structure. After **RasEapMakeMessage** returns, the service calls [**RasEapFreeMemory**](raseapfreememory.md) to free the memory occupied by the information. Therefore, the authentication protocol should copy the information into a private memory buffer during the call to **RasEapMakeMessage**.

 

 




