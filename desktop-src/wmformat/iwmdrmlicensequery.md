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
ms.date: 05/31/2018
api_location: 
---

# IWMDRMLicenseQuery interface

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

 

