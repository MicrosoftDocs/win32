---
title: Windows Deployment Services Structures
description: The following structures are used with Windows Deployment Services.
ms.assetid: '2e52a6ae-cecb-45de-b777-108836ed5264'
---

# Windows Deployment Services Structures

The following structures are used with Windows Deployment Services.



| Structure                                                                         | Description                                                                                                        |
|-----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| [**PXE\_ADDRESS**](pxe-address.md)                                               | Specifies the network address for a packet.                                                                        |
| [**PXE\_DHCP\_MESSAGE**](pxe-dhcp-message.md)                                    | This structure is used with the Windows Deployment Services PXE Server API.                                        |
| [**PXE\_DHCP\_OPTION**](pxe-dhcp-option.md)                                      | This structure is used with the Windows Deployment Services PXE Server API.                                        |
| [**PXE\_PROVIDER**](pxe-provider.md)                                             | Describes a provider.                                                                                              |
| [**WDS\_CLI\_CRED**](wds-cli-cred.md)                                            | Contains credentials used to authorize a client session.                                                           |
| [**WDS\_TRANSPORTCLIENT\_REQUEST**](wds-transportclient-request.md)              | Used by the [**WdsTransportClientStartSession**](wdstransportclientstartsession.md) function.                     |
| [**TRANSPORTCLIENT\_SESSION\_INFO**](transportclient-session-info.md)            | Used by the [*PFN\_WdsTransportClientSessionStartEx*](pfn-wdstransportclientsessionstartex.md) callback function. |
| [**WDS\_TRANSPORTPROVIDER\_INIT\_PARAMS**](wds-transportprovider-init-params.md) | Used by the [**WdsTransportProviderInitialize**](wdstransportproviderinitialize.md) callback function.            |
| [**WDS\_TRANSPORTPROVIDER\_SETTINGS**](wds-transportprovider-settings.md)        | Used by the [**WdsTransportProviderInitialize**](wdstransportproviderinitialize.md) callback function.            |



 

The following is available beginning with Windows 8 and Windows Server 2012.

| Structure                                          | Description                                               |
|----------------------------------------------------|-----------------------------------------------------------|
| [**PXE\_DHCPV6\_OPTION**](pxe-dhcpv6-option.md)   | Used with the Windows Deployment Services PXE Server API. |
| [**PXE\_DHCPV6\_MESSAGE**](pxe-dhcpv6-message.md) | A DHCPV6 message.                                         |



 

 

 




