---
title: ADSI Constants
description: The following table lists constants defined and used in Active Directory Service Interfaces (ADSI).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 'facc00e8-2ecd-4428-bddd-cfa1ff1b8538'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
keywords: ["ADS_EXT_INITCREDENTIALS", "ADS_EXT_INITIALIZE_COMPLETE", "ADS_EXT_MAXEXTDISPID", "ADS_EXT_MINEXTDISPID", "ADS_VLV_RESPONSE", "DBPROPFLAGS_ADSISEARCH"]
---

# ADSI Constants

The following table lists constants defined and used in Active Directory Service Interfaces (ADSI).



| ADSI constant                      | Value                                   | Description                                                                                                                                                                                                      |
|------------------------------------|-----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **ADS\_EXT\_INITCREDENTIALS**      | 1                                       | A control code that indicates that the custom data supplied to the [**IADsExtension::Operate**](iadsextension-operate.md) method contains user credentials.                                                     |
| **ADS\_EXT\_INITIALIZE\_COMPLETE** | 2                                       | A control code used with [**IADsExtension::Operate**](iadsextension-operate.md) to indicate that extensions can perform any necessary initialization, depending on the features supported by the parent object. |
| **ADS\_EXT\_MAXEXTDISPID**         | 16777215                                | The highest DISPID an extension object can use for its methods and properties.                                                                                                                                   |
| **ADS\_EXT\_MINEXTDISPID**         | 1                                       | The lowest DISPID an extension object can use for its methods and properties.                                                                                                                                    |
| **ADS\_VLV\_RESPONSE**             | L"fc8cb04d-311d-406c-8cb9-1ae8b843b419" | Used with the [**IDirectorySearch::GetColumn**](idirectorysearch-getcolumn.md) method to retrieve VLV search metadata. For more information, see [How to Search Using VLV](how-to-search-using-vlv.md).        |
| **DBPROPFLAGS\_ADSISEARCH**        | 0x0000C000                              | Used to work with the OLE DB provider.                                                                                                                                                                           |



 

 

 




