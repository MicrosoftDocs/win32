---
title: IWMDRMLicenseQuery QueryLicenseState method (Wmdrmsdk.h)
description: The QueryLicenseState method queries the local license store for license information that applies to a Key ID for one or more specific rights.
ms.assetid: 17f40c56-2266-4c94-9e95-a33a92ddef74
keywords:
- QueryLicenseState method windows Media Format
- QueryLicenseState method windows Media Format , IWMDRMLicenseQuery interface
- IWMDRMLicenseQuery interface windows Media Format , QueryLicenseState method
topic_type:
- apiref
api_name:
- IWMDRMLicenseQuery.QueryLicenseState
api_location:
- Wmdrmsdk.lib
- Wmdrmsdk.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMDRMLicenseQuery::QueryLicenseState method

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **QueryLicenseState** method queries the local license store for license information that applies to a Key ID for one or more specific rights.

## Syntax


```C++
HRESULT QueryLicenseState(
  [in]  BSTR                   bstrKID,
  [in]  DWORD                  cActionsToQuery,
  [in]  BSTR                   rgbstrActionsToQuery[],
  [out] DRM_LICENSE_STATE_DATA rgResultStateData[]
);
```



## Parameters

<dl> <dt>

*bstrKID* \[in\]
</dt> <dd>

Key ID for which to query. Only licenses that apply to this Key ID will be evaluated.

</dd> <dt>

*cActionsToQuery* \[in\]
</dt> <dd>

The number of actions for which to query. This value must be set to the number of elements in the arrays passed for the *rgbstrActionsToQuery* and *rgResultStateData* parameters.

</dd> <dt>

*rgbstrActionsToQuery\[\]* \[in\]
</dt> <dd>

Array of one or more rights for which to query. This array must contain as many elements as specified by *cActionsToQuery*. Each element must be set to one of the following constants.



| Constant                                        | Description                                                                                                                                        |
|-------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| g\_wszWMDRM\_LicenseState\_Backup               | Include to query for the details about the right to back up and restore the license.                                                               |
| g\_wszWMDRM\_LicenseState\_CollaborativePlay    | Include to query for the details about the right to share the content with a group of users as part of a collaborative playback scenario.          |
| g\_wszWMDRM\_LicenseState\_Copy                 | Include to query for the details about the right to copy the content to external devices or media.                                                 |
| g\_wszWMDRM\_LicenseState\_CopyToCD             | Include to query for the details about the right to copy the content to CD.                                                                        |
| g\_wszWMDRM\_LicenseState\_CopyToNonSDMIDevice  | Include to query for the details about the right to copy the content to a device that does not support the secure digital media initiative (SDMI). |
| g\_wszWMDRM\_LicenseState\_CopyToSDMIDevice     | Include to query for the details about the right to copy the content to a device that supports the SDMI.                                           |
| g\_wszWMDRM\_LicenseState\_CreateThumbnailImage | Include to query for the details about the right to create a thumbnail image from the content.                                                     |
| g\_wszWMDRM\_LicenseState\_Playback             | Include to query for the details about the right to play the content.                                                                              |
| g\_wszWMDRM\_LicenseState\_PlaylistBurn         | Include to query for the details about the right to copy the content to CD as part of a playlist.                                                  |



 

</dd> <dt>

*rgResultStateData\[\]* \[out\]
</dt> <dd>

Array of one or more [**DRM\_LICENSE\_STATE\_DATA**](drmdrm-license-state-data.md) structures that receive the license state information that applies to the right in the corresponding element of the *rgbstrActionsToQuery* parameter.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## Remarks

All licenses that apply to the specified Key ID will be searched and evaluated. The results are aggregated, so each **DRM\_LICENSE\_STATE\_DATA** structure may contain information from multiple licenses.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wmdrmsdk.h</dt> </dl>   |
| Library<br/> | <dl> <dt>Wmdrmsdk.lib</dt> </dl> |



## See also

<dl> <dt>

[**IWMDRMLicenseQuery Interface**](iwmdrmlicensequery.md)
</dt> </dl>

 

 





