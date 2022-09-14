---
description: Winsock catalog change event for a layered service provider (LSP) removal operation.
ms.assetid: 86FF17F7-8CCF-4A03-899F-42BFACDF3F54
title: WINSOCK_WS2HELP_LSP_REMOVE event
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WINSOCK_WS2HELP_LSP_REMOVE
api_type: 
- NA
api_location: 
---

# WINSOCK\_WS2HELP\_LSP\_REMOVE event

> [!Note]  
> Layered Service Providers are deprecated. Starting with Windows 8 and Windows Server 2012, use [Windows Filtering Platform](../fwp/windows-filtering-platform-start-page.md).

 

The **WINSOCK\_WS2HELP\_LSP\_REMOVE** event is a Winsock catalog change event for a layered service provider (LSP) removal operation.


```C++
const EVENT_DESCRIPTOR WINSOCK_WS2HELP_LSP_REMOVE = {0x2, 0x0, 0x10, 0x0, 0x0, 0x0, 0x8000000000000000};
```



## Parameters

<dl> <dt>

*LSP Name* 
</dt> <dd>

The name of the LSP as obtained from the **szProtocol** member of the [**WSAPROTOCOL\_INFO**](/windows/win32/api/winsock2/ns-winsock2-wsaprotocol_infoa) structure for the LSP being removed.

</dd> <dt>

*Catalog* 
</dt> <dd>

The Winsock catalog (32-bit or 64-bit) where the LSP is being removed. This is an integer value that is either 32 or 64.

</dd> <dt>

*Installer* 
</dt> <dd>

The module filename of the application making the LSP remove call.

</dd> <dt>

*GUID* 
</dt> <dd>

The GUID value of the Winsock transport provider that the LSP is being removed from.

</dd> <dt>

*Category* 
</dt> <dd>

The **dwCatalogEntryId** member of the [**WSAPROTOCOL\_INFO**](/windows/win32/api/winsock2/ns-winsock2-wsaprotocol_infoa) structure for the LSP being removed.

</dd> </dl>

## Remarks

The **WINSOCK\_WS2HELP\_LSP\_REMOVE** event is traced for an LSP removal operation when a protocol entry is removed from the Winsock catalog.

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

 

 
