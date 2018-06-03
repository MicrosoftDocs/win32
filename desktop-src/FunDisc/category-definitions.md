---
Description: Categories are the namespaces in which components which provide similar base functionality are grouped.
ms.assetid: 84633d91-d193-437c-b1cf-9bc491ad416c
title: Category Definitions
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Category Definitions

\[Function Discovery is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Categories are the namespaces in which components which provide similar base functionality are grouped.

The following are the built-in Function Discovery categories.



| Constant/value                                                                                                                                                                                                                                                                                                 | Description                                        |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------|
| <span id="FCTN_CATEGORY_DEVICES"></span><span id="fctn_category_devices"></span><dl> <dt>**FCTN\_CATEGORY\_DEVICES**</dt> </dl>                                                                                                                         | Not used.<br/>                               |
| <span id="FCTN_CATEGORY_NETBIOS"></span><span id="fctn_category_netbios"></span><dl> <dt>**FCTN\_CATEGORY\_NETBIOS**</dt> <dt> L"Provider\\\\Microsoft.Networking.Netbios"</dt> </dl>                       | The NetBIOS provider.<br/>                   |
| <span id="FCTN_CATEGORY_NETWORKDEVICES"></span><span id="fctn_category_networkdevices"></span><dl> <dt>**FCTN\_CATEGORY\_NETWORKDEVICES**</dt> <dt>L"Layered\\\\Microsoft.Networking.Devices"</dt> </dl>    | Network devices.<br/>                        |
| <span id="FCTN_CATEGORY_PNP"></span><span id="fctn_category_pnp"></span><dl> <dt>**FCTN\_CATEGORY\_PNP**</dt> <dt>L"Provider\\\\Microsoft.Base.PnP"</dt> </dl>                                              | The PnP provider.<br/>                       |
| <span id="FCTN_CATEGORY_PNPXASSOCIATION"></span><span id="fctn_category_pnpxassociation"></span><dl> <dt>**FCTN\_CATEGORY\_PNPXASSOCIATION**</dt> <dt> L"Provider\\\\Microsoft.PnPX.Association"</dt> </dl> | The PnP-X association provider.<br/>         |
| <span id="FCTN_CATEGORY_PUBLICATION"></span><span id="fctn_category_publication"></span><dl> <dt>**FCTN\_CATEGORY\_PUBLICATION**</dt> <dt>L"Provider\\\\Microsoft.Base.Publication"</dt> </dl>              | The publication provider.<br/>               |
| <span id="FCTN_CATEGORY_REGISTRY"></span><span id="fctn_category_registry"></span><dl> <dt>**FCTN\_CATEGORY\_REGISTRY**</dt> <dt>L"Provider\\\\Microsoft.Base.Registry"</dt> </dl>                          | The registry provider.<br/>                  |
| <span id="FCTN_CATEGORY_SSDP"></span><span id="fctn_category_ssdp"></span><dl> <dt>**FCTN\_CATEGORY\_SSDP**</dt> <dt>L"Provider\\\\Microsoft.Networking.SSDP"</dt> </dl>                                    | The SSDP provider.<br/>                      |
| <span id="FCTN_CATEGORY_WCN"></span><span id="fctn_category_wcn"></span><dl> <dt>**FCTN\_CATEGORY\_WCN**</dt> <dt>L"Provider\\\\Microsoft.Networking.WCN"</dt> </dl>                                        | The Windows Connect Now (WCN) provider.<br/> |
| <span id="FCTN_CATEGORY_WSDISCOVERY"></span><span id="fctn_category_wsdiscovery"></span><dl> <dt>**FCTN\_CATEGORY\_WSDISCOVERY**</dt> <dt>L"Provider\\\\Microsoft.Networking.WSD"</dt> </dl>                | The WSD provider.<br/>                       |



## Remarks

Providers can define and use their own categories.

The category type (layered or provider) is specified at the beginning of the value string.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>FunctionDiscoveryCategories.h</dt> </dl> |



## See also

<dl> <dt>

[Built-in Providers](built-in-providers.md)
</dt> <dt>

[Function Discovery Categories](function-discovery-categories.md)
</dt> <dt>

[**Subcategory Definitions**](subcategory-definitions.md)
</dt> </dl>

 

 




