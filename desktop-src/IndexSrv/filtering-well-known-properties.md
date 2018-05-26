---
title: Filtering Well-Known Properties
description: Filtering Well-Known Properties
ms.assetid: 74c0da33-d0a5-4718-b995-a309c2761c96
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Filtering Well-Known Properties

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Microsoft encourages all [**IFilter**](/windows/win32/Filter/nn-filter-ifilter?branch=master) interface implementers to adopt sets of well-known properties so that client applications can use one query to search for these properties on all file classes that have **IFilter** interface support. Clients calling **IFilter** interface implementations can request a set of properties they would like to see during the [**IFilter::Init**](/windows/win32/Filter/nf-filter-ifilter-init?branch=master) method call.

Properties have unique identifiers made up of the globally unique identifier (GUID) of a property set, followed by a property ID. The property ID can be a unique number within the property set for properties with type PRSPEC\_PROPID or a unique string corresponding to the name of the property for properties of type PRSPEC\_LPWSTR. The following list describes the well-known properties used by Indexing Service.



| Property Name | Property Set GUID/ Property ID or Name                        | Description                                            |
|---------------|---------------------------------------------------------------|--------------------------------------------------------|
| Text          | B725F130-47EF-101A-A5F1-02608C9EEBAC 19<br/>            | From storage properties of a file                      |
| Description   | D1B5D3F0-C0B3-11CF-9A92-00A0C908DBF1 "DESCRIPTION"<br/> | From HTML Filter; can be used to generate Abstract     |
| Title         | F29F85E0-4FF9-1068-AB91-08002B27B3D9 2<br/>             | From Microsoft Office Summary Information property set |
| Subject       | F29F85E0-4FF9-1068-AB91-08002B27B3D9 3<br/>             | From Office Summary Information property set           |
| Author        | F29F85E0-4FF9-1068-AB91-08002B27B3D9 4<br/>             | From Office Summary Information property set           |
| Keywords      | F29F85E0-4FF9-1068-AB91-08002B27B3D9 5<br/>             | From Office Summary Information property set           |
| Comments      | F29F85E0-4FF9-1068-AB91-08002B27B3D9 6<br/>             | From Office Summary Information property set           |



 

 

 





