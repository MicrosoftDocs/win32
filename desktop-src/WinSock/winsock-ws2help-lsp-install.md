---
description: Winsock catalog change event for a layered service provider (LSP) installation operation.
ms.assetid: 76A3D175-8CDC-486C-8341-D6314BCEC113
title: WINSOCK_WS2HELP_LSP_INSTALL event
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WINSOCK_WS2HELP_LSP_INSTALL
api_type: 
- NA
api_location: 
---

# WINSOCK\_WS2HELP\_LSP\_INSTALL event

> [!Note]  
> Layered Service Providers are deprecated. Starting with Windows 8 and Windows Server 2012, use [Windows Filtering Platform](../fwp/windows-filtering-platform-start-page.md).

 

The **WINSOCK\_WS2HELP\_LSP\_INSTALL** event is a Winsock catalog change event for a layered service provider (LSP) installation operation.


```C++
const EVENT_DESCRIPTOR WINSOCK_WS2HELP_LSP_INSTALL = {0x1, 0x0, 0x10, 0x0, 0x0, 0x0, 0x8000000000000000};
```



## Parameters

<dl> <dt>

*LSP Name* 
</dt> <dd>

The name of the LSP as obtained from the **szProtocol** member of the [**WSAPROTOCOL\_INFO**](/windows/win32/api/winsock2/ns-winsock2-wsaprotocol_infoa) structure for the LSP being installed.

</dd> <dt>

*Catalog* 
</dt> <dd>

The Winsock catalog (32-bit or 64-bit) where the LSP is being installed. This is an integer value that is either 32 or 64.

</dd> <dt>

*Installer* 
</dt> <dd>

The module filename of the application making the LSP install call.

</dd> <dt>

*GUID* 
</dt> <dd>

The GUID value of the Winsock transport provider that the LSP is being installed under.

</dd> <dt>

*Category* 
</dt> <dd>

The **dwCatalogEntryId** member of the [**WSAPROTOCOL\_INFO**](/windows/win32/api/winsock2/ns-winsock2-wsaprotocol_infoa) structure for the LSP being installed.

</dd> </dl>

## Remarks

The **WINSOCK\_WS2HELP\_LSP\_INSTALL** event is traced for an LSP install operation when a protocol entry is installed into the Winsock catalog.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Control of Winsock Tracing](control-of-winsock-tracing.md)
</dt> <dt>

[Winsock Tracing](winsock-tracing.md)
</dt> <dt>

[Winsock Tracing Levels](winsock-tracing-levels.md)
</dt> <dt>

[Winsock Catalog Change Tracing Details](winsock-layered-service-provider-tracing-event-details.md)
</dt> </dl>

 

 
