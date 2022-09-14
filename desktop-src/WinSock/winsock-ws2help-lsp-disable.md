---
description: Winsock catalog change event for a layered service provider (LSP) disable operation.
ms.assetid: 6BCEECB1-92AD-47D8-952B-D0FD2A78EB45
title: WINSOCK_WS2HELP_LSP_DISABLE event
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WINSOCK_WS2HELP_LSP_DISABLE
api_type: 
- NA
api_location: 
---

# WINSOCK\_WS2HELP\_LSP\_DISABLE event

> [!Note]  
> Layered Service Providers are deprecated. Starting with Windows 8 and Windows Server 2012, use [Windows Filtering Platform](../fwp/windows-filtering-platform-start-page.md).

 

The **WINSOCK\_WS2HELP\_LSP\_DISABLE** event is a Winsock catalog change event for a layered service provider (LSP) disable operation.


```C++
const EVENT_DESCRIPTOR WINSOCK_WS2HELP_LSP_DISABLE = {0x3, 0x0, 0x10, 0x0, 0x0, 0x0, 0x8000000000000000};
```



## Parameters

<dl> <dt>

*LSP Name* 
</dt> <dd>

The name of the LSP as obtained from the **szProtocol** member of the [**WSAPROTOCOL\_INFO**](/windows/win32/api/winsock2/ns-winsock2-wsaprotocol_infoa) structure for the LSP being disabled.

</dd> <dt>

*Catalog* 
</dt> <dd>

The Winsock catalog (32-bit or 64-bit) where the LSP is being disabled. This is an integer value that is either 32 or 64.

</dd> <dt>

*Installer* 
</dt> <dd>

The module filename of the application making the LSP disable call.

</dd> <dt>

*GUID* 
</dt> <dd>

The GUID value of the Winsock transport provider that the LSP is being disabled.

</dd> <dt>

*Category* 
</dt> <dd>

The **dwCatalogEntryId** member of the [**WSAPROTOCOL\_INFO**](/windows/win32/api/winsock2/ns-winsock2-wsaprotocol_infoa) structure for the LSP being disabled.

</dd> </dl>

This event has no parameters.

## Remarks

The **WINSOCK\_WS2HELP\_LSP\_DISABLE** event is traced for an LSP disable operation when a protocol entry is disabled in the Winsock catalog.

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

 

 
