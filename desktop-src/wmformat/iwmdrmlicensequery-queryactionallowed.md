---
title: IWMDRMLicenseQuery QueryActionAllowed method (Wmdrmsdk.h)
description: The QueryActionAllowed method performs a query on the local license store to retrieve the license status for one or more DRM actions that apply to a specified Key ID.
ms.assetid: 814c2850-c036-4c44-a64e-861e88f16fb1
keywords:
- QueryActionAllowed method windows Media Format
- QueryActionAllowed method windows Media Format , IWMDRMLicenseQuery interface
- IWMDRMLicenseQuery interface windows Media Format , QueryActionAllowed method
topic_type:
- apiref
api_name:
- IWMDRMLicenseQuery.QueryActionAllowed
api_location:
- Wmdrmsdk.lib
- Wmdrmsdk.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMDRMLicenseQuery::QueryActionAllowed method

The **QueryActionAllowed** method performs a query on the local license store to retrieve the license status for one or more DRM actions that apply to a specified Key ID.

## Syntax


```C++
HRESULT QueryActionAllowed(
  [in]  BSTR  bstrKID,
  [in]  BSTR  bstrMinReqIndivVersion,
  [in]  DWORD cActionsToQuery,
  [in]  BSTR  rgbstrActionsToQuery[],
  [out] DWORD rgdwQueryResult[]
);
```



## Parameters

<dl> <dt>

*bstrKID* \[in\]
</dt> <dd>

Key ID for which to query. Only licenses that apply to this Key ID will be evaluated.

</dd> <dt>

*bstrMinReqIndivVersion* \[in\]
</dt> <dd>

The minimum security version specified in the header of the ASF file. This parameter is optional. Pass **NULL** to perform the query without this information.

</dd> <dt>

*cActionsToQuery* \[in\]
</dt> <dd>

The number of actions for which to query. This value must be set to the number of elements in the arrays passed for the *rgbstrActionsToQuery* and *rgdwQueryResult* parameters.

</dd> <dt>

*rgbstrActionsToQuery\[\]* \[in\]
</dt> <dd>

Array of one or more rights for which to query. This array must contain as many elements as specified by *cActionsToQuery*. Each element must be set to one of the following constants:



| Constant                                         | Description                                                                      |
|--------------------------------------------------|----------------------------------------------------------------------------------|
| g\_wszWMDRM\_ActionAllowed\_Playback             | Include to query for the right to play the content.                              |
| g\_wszWMDRM\_ActionAllowed\_Copy                 | Include to query for the right to copy the content to external devices or media. |
| g\_wszWMDRM\_ActionAllowed\_PlaylistBurn         | Include to query for the right to copy the content to CD as part of a playlist.  |
| g\_wszWMDRM\_ActionAllowed\_CreateThumbnailImage | Include to query for the right to create a thumbnail image from the content.     |
| g\_wszWMDRM\_ActionAllowed\_CopyToCD             | Include to query for the right to copy the content to CD.                        |



 

</dd> <dt>

*rgdwQueryResult\[\]* \[out\]
</dt> <dd>

Array of one or more DWORD variables that receive the results of the query for the rights specified by *rgbstrActionsToQuery*. If an action is allowed, the corresponding element is set to zero. If an action is not allowed, the element is set to one or more values of the [**DRM\_ACTION\_ALLOWED\_QUERY\_RESULTS**](drm-action-allowed-query-results.md) enumeration combined by using the bitwise OR operation. This array must contain as many elements as specified by *cActionsToQuery*.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## Remarks

When querying for play and copy rights, you will get more accurate results by first setting environmental parameters. Use the [**SetActionAllowedQueryParams**](iwmdrmlicensequery-setactionallowedqueryparams.md) method to set the environmental parameters. The results of queries for the burn right are unaffected by the environmental parameters; you can safely use the defaults.

The results returned by the **QueryActionAllowed** method are aggregated from zero or more licenses in the local license store. The method may not search all of the licenses that apply to the Key ID if it encounters an enabled result.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wmdrmsdk.h</dt> </dl>   |
| Library<br/> | <dl> <dt>Wmdrmsdk.lib</dt> </dl> |



## See also

<dl> <dt>

[**IWMDRMLicenseQuery Interface**](iwmdrmlicensequery.md)
</dt> <dt>

[**Querying for Simple Rights Information**](querying-for-simple-rights-information.md)
</dt> </dl>

 

 





