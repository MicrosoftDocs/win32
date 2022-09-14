---
title: Windows Deployment Services Structures
description: The following structures are used with Windows Deployment Services.
ms.assetid: 2e52a6ae-cecb-45de-b777-108836ed5264
ms.topic: article
ms.date: 05/31/2018
---

# Windows Deployment Services Structures

The following structures are used with Windows Deployment Services.



| Structure                                                                         | Description                                                                                                        |
|-----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| [**PXE\_ADDRESS**](/windows/win32/api/wdspxe/ns-wdspxe-pxe_address)                                               | Specifies the network address for a packet.                                                                        |
| [**PXE\_DHCP\_MESSAGE**](/windows/win32/api/wdspxe/ns-wdspxe-pxe_dhcp_message)                                    | This structure is used with the Windows Deployment Services PXE Server API.                                        |
| [**PXE\_DHCP\_OPTION**](/windows/win32/api/wdspxe/ns-wdspxe-pxe_dhcp_option)                                      | This structure is used with the Windows Deployment Services PXE Server API.                                        |
| [**PXE\_PROVIDER**](/windows/win32/api/wdspxe/ns-wdspxe-pxe_provider)                                             | Describes a provider.                                                                                              |
| [**WDS\_CLI\_CRED**](/windows/win32/api/wdsclientapi/ns-wdsclientapi-wds_cli_cred)                                            | Contains credentials used to authorize a client session.                                                           |
| [**WDS\_TRANSPORTCLIENT\_REQUEST**](/windows/desktop/api/Wdstci/ns-wdstci-wds_transportclient_request)              | Used by the [**WdsTransportClientStartSession**](/windows/desktop/api/Wdstci/nf-wdstci-wdstransportclientstartsession) function.                     |
| [**TRANSPORTCLIENT\_SESSION\_INFO**](/windows/desktop/api/Wdstci/ns-wdstci-transportclient_session_info)            | Used by the [*PFN\_WdsTransportClientSessionStartEx*](/windows/desktop/api/Wdstci/nc-wdstci-pfn_wdstransportclientsessionstartex) callback function. |
| [**WDS\_TRANSPORTPROVIDER\_INIT\_PARAMS**](/windows/desktop/api/Wdstpdi/ns-wdstpdi-wds_transportprovider_init_params) | Used by the [**WdsTransportProviderInitialize**](/windows/desktop/api/wdstpdi/nf-wdstpdi-wdstransportproviderinitialize) callback function.            |
| [**WDS\_TRANSPORTPROVIDER\_SETTINGS**](/windows/desktop/api/Wdstpdi/ns-wdstpdi-wds_transportprovider_settings)        | Used by the [**WdsTransportProviderInitialize**](/windows/desktop/api/wdstpdi/nf-wdstpdi-wdstransportproviderinitialize) callback function.            |



 

The following is available beginning with Windows 8 and Windows Server 2012.

| Structure                                          | Description                                               |
|----------------------------------------------------|-----------------------------------------------------------|
| [**PXE\_DHCPV6\_OPTION**](/windows/win32/api/wdspxe/ns-wdspxe-pxe_dhcpv6_option)   | Used with the Windows Deployment Services PXE Server API. |
| [**PXE\_DHCPV6\_MESSAGE**](/windows/win32/api/wdspxe/ns-wdspxe-pxe_dhcpv6_message) | A DHCPV6 message.                                         |



 

 

 




