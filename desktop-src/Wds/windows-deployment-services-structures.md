---
title: Windows Deployment Services Structures
description: The following structures are used with Windows Deployment Services.
ms.assetid: 2e52a6ae-cecb-45de-b777-108836ed5264
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Windows Deployment Services Structures

The following structures are used with Windows Deployment Services.



| Structure                                                                         | Description                                                                                                        |
|-----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| [**PXE\_ADDRESS**](/windows/win32/WdsPxe/ns-wdspxe-tagpxe_address?branch=master)                                               | Specifies the network address for a packet.                                                                        |
| [**PXE\_DHCP\_MESSAGE**](/windows/win32/WdsPxe/ns-wdspxe-tagpxe_dhcp_message?branch=master)                                    | This structure is used with the Windows Deployment Services PXE Server API.                                        |
| [**PXE\_DHCP\_OPTION**](/windows/win32/WdsPxe/ns-wdspxe-tagpxe_dhcp_option?branch=master)                                      | This structure is used with the Windows Deployment Services PXE Server API.                                        |
| [**PXE\_PROVIDER**](/windows/win32/WdsPxe/ns-wdspxe-tagpxe_provider?branch=master)                                             | Describes a provider.                                                                                              |
| [**WDS\_CLI\_CRED**](/windows/win32/WdsClientAPI/ns-wdsclientapi-tagwds_cli_cred?branch=master)                                            | Contains credentials used to authorize a client session.                                                           |
| [**WDS\_TRANSPORTCLIENT\_REQUEST**](/windows/win32/Wdstci/ns-wdstci-_wds_transportclient_request?branch=master)              | Used by the [**WdsTransportClientStartSession**](/windows/win32/Wdstci/nf-wdstci-wdstransportclientstartsession?branch=master) function.                     |
| [**TRANSPORTCLIENT\_SESSION\_INFO**](/windows/win32/Wdstci/ns-wdstci-_transportclient_session_info?branch=master)            | Used by the [*PFN\_WdsTransportClientSessionStartEx*](/windows/win32/Wdstci/nc-wdstci-pfn_wdstransportclientsessionstartex?branch=master) callback function. |
| [**WDS\_TRANSPORTPROVIDER\_INIT\_PARAMS**](/windows/win32/Wdstpdi/ns-wdstpdi-_wds_transportprovider_init_params?branch=master) | Used by the [**WdsTransportProviderInitialize**](/windows/win32/wdstpdi/nf-wdstpdi-wdstransportproviderinitialize?branch=master) callback function.            |
| [**WDS\_TRANSPORTPROVIDER\_SETTINGS**](/windows/win32/Wdstpdi/ns-wdstpdi-_wds_transportprovider_settings?branch=master)        | Used by the [**WdsTransportProviderInitialize**](/windows/win32/wdstpdi/nf-wdstpdi-wdstransportproviderinitialize?branch=master) callback function.            |



 

The following is available beginning with Windows 8 and Windows Server 2012.

| Structure                                          | Description                                               |
|----------------------------------------------------|-----------------------------------------------------------|
| [**PXE\_DHCPV6\_OPTION**](/windows/win32/WdsPxe/ns-wdspxe-tagpxe_dhcpv6_option?branch=master)   | Used with the Windows Deployment Services PXE Server API. |
| [**PXE\_DHCPV6\_MESSAGE**](/windows/win32/WdsPxe/ns-wdspxe-tagpxe_dhcpv6_message?branch=master) | A DHCPV6 message.                                         |



 

 

 




