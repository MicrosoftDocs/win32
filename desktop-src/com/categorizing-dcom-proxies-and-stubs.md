---
title: Categorizing DCOM Proxies and Stubs
description: Categorizing DCOM Proxies and Stubs
ms.assetid: f5d117d6-6c2c-4beb-8869-1581a5b1846f
ms.topic: article
ms.date: 05/31/2018
---

# Categorizing DCOM Proxies and Stubs

DCOM marshals references to objects by constructing OBJREFs that contain CLSIDs. These CLSIDs are vulnerable to security attacks because arbitrary DLLs can be loaded during marshaling. However, the EOAC\_NO\_CUSTOM\_MARSHAL flag can be specified when calling [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity) (see [**EOLE\_AUTHENTICATION\_CAPABILITIES**](/windows/win32/api/objidlbase/ne-objidlbase-eole_authentication_capabilities)). Setting this flag helps protect server security when using DCOM because it reduces the chances of executing arbitrary DLLs. When this flag is set, the server allows the marshaling only of CLSIDs that are implemented in ole32.dll, comadmin.dll, comsvcs.dll, or es.dll, or that implement the CATID\_MARSHALER category ID.

CATID\_MARSHALER is a component category GUID that can be associated with a CLSID that is being custom marshaled. The interfaces being custom marshaled with this CLSID are allowed when the EOAC\_NO\_CUSTOM\_MARSHAL is set via [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity).

## Related topics

<dl> <dt>

[Component Categories](component-categories.md)
</dt> </dl>

 

 