---
description: Winsock Catalog Change Tracing Details
ms.assetid: 4C86618D-4E79-486E-997F-9E2509FBF6B6
title: Winsock Catalog Change Tracing Details
ms.topic: article
ms.date: 05/31/2018
---

# Winsock Catalog Change Tracing Details

> [!Note]  
> Layered Service Providers are deprecated. Starting with Windows 8 and Windows Server 2012, use [Windows Filtering Platform](../fwp/windows-filtering-platform-start-page.md).

 

Winsock Catalog Change event tracing for layered Service providers (LSPs) is related to LSP installation, LSP removal, LSP disable, and Winsock catalog reset operations. All of the following events are written to the *Microsoft-Windows-Winsock-WS2HELP/Operational* channel which is different from the other Winsock network event tracing logged on Windows Vista and later.

The following details each of the Winsock LSP events that can be traced and describes which parameters and information are logged.

## LSP Install

Event ID = 1

Level = 4 (Information)

The following Winsock LSP events are traced for an LSP install operation:

-   A protocol entry is installed into the Winsock catalog.

The following parameters are logged for a LSP install event:



| Parameter                                                                                                | Description                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="LSP_Name"></span><span id="lsp_name"></span><span id="LSP_NAME"></span>LSP Name<br/>     | The name of the LSP as obtained from the **szProtocol** member of the [**WSAPROTOCOL\_INFO**](/windows/win32/api/winsock2/ns-winsock2-wsaprotocol_infoa) structure for the LSP being installed.<br/> |
| <span id="Catalog"></span><span id="catalog"></span><span id="CATALOG"></span>Catalog<br/>         | The Winsock catalog (32-bit or 64-bit) where the LSP is being installed. This is an integer value that is either 32 or 64.<br/>                                   |
| <span id="Installer"></span><span id="installer"></span><span id="INSTALLER"></span>Installer<br/> | The module filename of the application making the LSP install call.<br/>                                                                                          |
| <span id="GUID"></span><span id="guid"></span>GUID<br/>                                            | The GUID value of the Winsock transport provider that the LSP is being installed under.<br/>                                                                      |
| <span id="Category"></span><span id="category"></span><span id="CATEGORY"></span>Category<br/>     | The **dwCatalogEntryId** member of the [**WSAPROTOCOL\_INFO**](/windows/win32/api/winsock2/ns-winsock2-wsaprotocol_infoa) structure for the LSP being installed.<br/>                                |



 

## LSP Uninstall

Event ID = 2

Level = 4 (Information)

The following Winsock LSP events are traced for an LSP uninstall operation:

-   A protocol entry is removed from the Winsock catalog.

The following parameters are logged for a LSP uninstall event:



| Parameter                                                                                                | Description                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="LSP_Name"></span><span id="lsp_name"></span><span id="LSP_NAME"></span>LSP Name<br/>     | The name of the LSP as obtained from the **szProtocol** member of the [**WSAPROTOCOL\_INFO**](/windows/win32/api/winsock2/ns-winsock2-wsaprotocol_infoa) structure for the LSP being removed.<br/> |
| <span id="Catalog"></span><span id="catalog"></span><span id="CATALOG"></span>Catalog<br/>         | The Winsock catalog (32-bit or 64-bit) where the LSP is being removed. This is an integer value that is either 32 or 64.<br/>                                   |
| <span id="Installer"></span><span id="installer"></span><span id="INSTALLER"></span>Installer<br/> | The module filename of the application making the LSP remove call.<br/>                                                                                         |
| <span id="GUID"></span><span id="guid"></span>GUID<br/>                                            | The GUID value of the Winsock transport provider that the LSP is removed from.<br/>                                                                             |
| <span id="Category"></span><span id="category"></span><span id="CATEGORY"></span>Category<br/>     | The **dwCatalogEntryId** member of the [**WSAPROTOCOL\_INFO**](/windows/win32/api/winsock2/ns-winsock2-wsaprotocol_infoa) structure for the LSP being removed.<br/>                                |



 

## LSP Disable

Event ID = 3

Level = 4 (Information)

The following Winsock LSP events are traced for an LSP disable operation:

-   A protocol entry is disabled in the Winsock catalog.

The following parameters are logged for a LSP disable event:



| Parameter                                                                                                | Description                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="LSP_Name"></span><span id="lsp_name"></span><span id="LSP_NAME"></span>LSP Name<br/>     | The name of the LSP as obtained from the **szProtocol** member of the [**WSAPROTOCOL\_INFO**](/windows/win32/api/winsock2/ns-winsock2-wsaprotocol_infoa) structure for the LSP being disabled.<br/> |
| <span id="Catalog"></span><span id="catalog"></span><span id="CATALOG"></span>Catalog<br/>         | The Winsock catalog (32-bit or 64-bit) where the LSP is being disabled. This is an integer value that is either 32 or 64.<br/>                                   |
| <span id="Installer"></span><span id="installer"></span><span id="INSTALLER"></span>Installer<br/> | The module filename of the application making the LSP disable call.<br/>                                                                                         |
| <span id="GUID"></span><span id="guid"></span>GUID<br/>                                            | The GUID value of the Winsock transport provider where the LSP is being disabled.<br/>                                                                           |
| <span id="Category"></span><span id="category"></span><span id="CATEGORY"></span>Category<br/>     | The **dwCatalogEntryId** member of the [**WSAPROTOCOL\_INFO**](/windows/win32/api/winsock2/ns-winsock2-wsaprotocol_infoa) structure for the LSP being disabled.<br/>                                |



 

## Winsock Catalog Reset

Event ID = 4

Level = 4 (Information)

The following Winsock LSP events are traced for a Winsock catalog reset operation:

-   The Winsock catalog is reset.

The following parameters are logged for a Winsock catalog reset event:



| Parameter                                                                                        | Description                                                                                                              |
|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| <span id="Catalog"></span><span id="catalog"></span><span id="CATALOG"></span>Catalog<br/> | The Winsock catalog (32-bit or 64-bit) that is being reset. This is an integer value that is either 32 or 64.<br/> |



 

## Related topics

<dl> <dt>

[Control of Winsock Tracing](control-of-winsock-tracing.md)
</dt> <dt>

[Winsock Tracing](winsock-tracing.md)
</dt> <dt>

[Winsock Tracing Levels](winsock-tracing-levels.md)
</dt> <dt>

[Winsock Network Event Tracing Details](winsock-tracing-event-details.md)
</dt> </dl>

 

 
