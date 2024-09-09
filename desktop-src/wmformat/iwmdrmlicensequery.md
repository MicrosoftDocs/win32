---
title: IWMDRMLicenseQuery interface
description: The IWMDRMLicenseQuery interface enables applications to query the rights and license state for a protected file.
ms.assetid: 4ec8ff9f-0acb-4389-8995-65f24736491b
keywords:
- IWMDRMLicenseQuery interface windows Media Format
- IWMDRMLicenseQuery interface windows Media Format , described
topic_type:
- apiref
api_name:
- IWMDRMLicenseQuery
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# IWMDRMLicenseQuery interface

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **IWMDRMLicenseQuery** interface enables applications to query the rights and license state for a protected file. This interface uses the Key ID to perform queries on the local license store.

To obtain an instance of this interface, call [**IWMDRMProvider::CreateObject**](iwmdrmprovider-createobject.md). Pass **IID\_IWMDRMLicenseQuery** as the *riid* parameter.

## Members

The **IWMDRMLicenseQuery** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IWMDRMLicenseQuery** also has these types of members:

-   [Methods](#methods)

### Methods

The **IWMDRMLicenseQuery** interface has these methods.



| Method                                                                                | Description                                                                                      |
|:--------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------|
| [**QueryActionAllowed**](iwmdrmlicensequery-queryactionallowed.md)                   | Queries the local license store for permissions to perform actions by Key ID.<br/>         |
| [**QueryLicenseState**](iwmdrmlicensequery-querylicensestate.md)                     | Queries the local license store for license state data by Key ID and specific rights.<br/> |
| [**SetActionAllowedQueryParams**](iwmdrmlicensequery-setactionallowedqueryparams.md) | Sets environmental parameters to improve the accuracy of license queries.<br/>             |



 

## Remarks

The methods of **IWMDRMLicenseQuery** do not provide information about individual licenses. Instead, the license data is aggregated by the DRM subsystem before the query results are returned.

## See also

<dl> <dt>

[**Interfaces**](drm-interfaces.md)
</dt> </dl>

 

