---
title: NPS Extensions Functions
description: NPS Extensions Functions
ms.assetid: ca217314-00f9-4f9d-a9fe-ed928b3c3b3d
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# NPS Extensions Functions

> [!Note]  
> Internet Authentication Service (IAS) was renamed Network Policy Server (NPS) starting with Windows Server 2008. The content of this topic applies to both IAS and NPS. Throughout the text, NPS is used to refer to all versions of the service, including the versions originally referred to as IAS.

 

## Application Defined

The architecture for NPS Extension DLLs supports the following exported functions:

-   [**RadiusExtensionFreeAttributes**](https://docs.microsoft.com/windows/desktop/api/authif/nc-authif-pradius_extension_free_attributes)
-   [**RadiusExtensionInit**](https://docs.microsoft.com/windows/desktop/api/authif/nc-authif-pradius_extension_init)
-   [**RadiusExtensionProcess**](https://docs.microsoft.com/windows/desktop/api/authif/nc-authif-pradius_extension_process)
-   [**RadiusExtensionProcessEx**](https://docs.microsoft.com/windows/desktop/api/authif/nc-authif-pradius_extension_process_ex)
-   [**RadiusExtensionProcess2**](https://docs.microsoft.com/windows/desktop/api/authif/nc-authif-pradius_extension_process_2)
-   [**RadiusExtensionTerm**](https://docs.microsoft.com/windows/desktop/api/authif/nc-authif-pradius_extension_term)

The [**RadiusExtensionInit**](https://docs.microsoft.com/windows/desktop/api/authif/nc-authif-pradius_extension_init) and [**RadiusExtensionTerm**](https://docs.microsoft.com/windows/desktop/api/authif/nc-authif-pradius_extension_term) functions are optional.

The Extension DLL may export [**RadiusExtensionProcess2**](https://docs.microsoft.com/windows/desktop/api/authif/nc-authif-pradius_extension_process_2) instead of [**RadiusExtensionProcess**](https://docs.microsoft.com/windows/desktop/api/authif/nc-authif-pradius_extension_process) or [**RadiusExtensionProcessEx**](https://docs.microsoft.com/windows/desktop/api/authif/nc-authif-pradius_extension_process_ex).

If the Extension DLL exports [**RadiusExtensionProcessEx**](https://docs.microsoft.com/windows/desktop/api/authif/nc-authif-pradius_extension_process_ex), then it must also export [**RadiusExtensionFreeAttributes**](https://docs.microsoft.com/windows/desktop/api/authif/nc-authif-pradius_extension_free_attributes).

## System Defined

When NPS calls an implementation of [**RadiusExtensionProcess2**](https://docs.microsoft.com/windows/desktop/api/authif/nc-authif-pradius_extension_process_2), NPS passes the function a pointer to a [**RADIUS\_EXTENSION\_CONTROL\_BLOCK**](https://docs.microsoft.com/windows/desktop/api/authif/ns-authif-radius_extension_control_block) structure.

The [**RADIUS\_EXTENSION\_CONTROL\_BLOCK**](https://docs.microsoft.com/windows/desktop/api/authif/ns-authif-radius_extension_control_block) structure contains function pointers to the following functions provided by NPS:

-   [**GetRequest**](https://docs.microsoft.com/previous-versions/ms688263(v%3dvs.85))
-   [**GetResponse**](https://docs.microsoft.com/previous-versions/ms688270(v%3dvs.85))
-   [**SetResponseType**](https://docs.microsoft.com/previous-versions/ms688462(v%3dvs.85))

The functions [**GetRequest**](https://docs.microsoft.com/previous-versions/ms688263(v%3dvs.85)) and [**GetResponse**](https://docs.microsoft.com/previous-versions/ms688270(v%3dvs.85)) return pointers to a structure of type [**RADIUS\_ATTRIBUTE\_ARRAY**](https://docs.microsoft.com/windows/desktop/api/authif/ns-authif-radius_attribute_array).

The [**RADIUS\_ATTRIBUTE\_ARRAY**](https://docs.microsoft.com/windows/desktop/api/authif/ns-authif-radius_attribute_array) structure contains function pointers to the following functions provided by NPS:

-   [**Add**](https://docs.microsoft.com/previous-versions/ms688246(v%3dvs.85))
-   [**AttributeAt**](https://docs.microsoft.com/previous-versions/ms688253(v%3dvs.85))
-   [**GetSize**](https://docs.microsoft.com/previous-versions/ms688277(v%3dvs.85))
-   [**InsertAt**](https://docs.microsoft.com/previous-versions/ms688296(v%3dvs.85))
-   [**RemoveAt**](https://docs.microsoft.com/previous-versions/ms688452(v%3dvs.85))
-   [**SetAt**](https://docs.microsoft.com/previous-versions/ms688456(v%3dvs.85))

 

 




