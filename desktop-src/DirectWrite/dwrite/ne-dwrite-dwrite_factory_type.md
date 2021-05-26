---
UID: NE:dwrite.DWRITE_FACTORY_TYPE
title: DWRITE_FACTORY_TYPE (dwrite.h)
description: Specifies the type of DirectWrite factory object.
tech.root: DirectWrite
ms.date: 11/11/2020
ms.topic: reference
req.header: dwrite.h
req.include-header: dwrite_core.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
targetos: Windows
req.typenames: 
req.redist: 
f1_keywords:
 - DWRITE_FACTORY_TYPE
 - dwrite/DWRITE_FACTORY_TYPE
dev_langs:
 - c++
topic_type:
 - APIRef
 - kbSyntax
api_type:
 - HeaderDef
api_location:
 - dwrite.h
api_name:
 - DWRITE_FACTORY_TYPE
---

# DWRITE_FACTORY_TYPE enumeration (dwrite.h)

Specifies the type of DirectWrite factory object.

> [!IMPORTANT]
> This API is available as part of the DWriteCore implementation of [DirectWrite](../direct-write-portal.md). DWriteCore is a form of DirectWrite that runs on versions of Windows down to Windows 8, and opens the door for you to use it cross-platform. For more info, and code examples, see [DWriteCore overview](../dwritecore-overview.md).

## Syntax
```cpp
typedef enum DWRITE_FACTORY_TYPE {
  DWRITE_FACTORY_TYPE_SHARED,
  DWRITE_FACTORY_TYPE_ISOLATED,
  DWRITE_FACTORY_TYPE_ISOLATED2
} ;
```

## Constants

| Name | Description |
| ---- |:---- |
| DWRITE_FACTORY_TYPE_SHARED | Indicates that the DirectWrite factory is a shared factory and that it allows for the reuse of cached font data across multiple in-process components. Such factories also take advantage of cross process font caching components for better performance. |
| DWRITE_FACTORY_TYPE_ISOLATED | Indicates that the DirectWrite factory object is isolated. Objects created from the isolated factory do not interact with internal DirectWrite state from other components. |
| DWRITE_FACTORY_TYPE_ISOLATED2 | Indicates that the DirectWrite factory object is restricted. Objects created from a restricted factory don't use nor modify internal state or cached data used by other factories. In addition, the system font collection contains only well-known fonts.|

## Examples

See the [DWriteCore overview](../dwritecore-overview.md) topic, and the [DWriteCoreGallery](https://github.com/microsoft/Project-Reunion-Samples/tree/main/DWriteCore/DWriteCoreGallery) sample app.

## Remarks

A DirectWrite factory object contains information about its internal state, such as font loader registration and cached font data. In most cases you should use the shared factory object, because it allows multiple components that use DirectWrite to share internal DirectWrite state information, thereby reducing memory usage. However, there are cases when it is desirable to reduce the impact of a component on the rest of the process, such as a plug-in from an untrusted source,  by sandboxing and isolating it from the rest of the process components. In such cases, you should use an isolated factory for the sandboxed component.

A restricted factory is more locked down than an isolated factory. It doesn't interact with a cross-process nor persistent font cache in any way. In addition, the system font collection returned from this factory includes only well-known fonts. If you pass **DWRITE_FACTORY_TYPE_ISOLATED2** to a version of DWrite that's older than DWriteCore, then [DWriteCreateFactory](/windows/win32/api/dwrite/nf-dwrite-dwritecreatefactory) returns **E_INVALIDARG**.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum supported client** | Windows 10, Project Reunion [Win32 apps] |
| **Header** | dwrite.h (include dwrite_core.h) |