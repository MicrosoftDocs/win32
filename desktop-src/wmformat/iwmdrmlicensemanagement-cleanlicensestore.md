---
title: IWMDRMLicenseManagement CleanLicenseStore method (Wmdrmsdk.h)
description: The CleanLicenseStore method removes unusable licenses from the temporary license store and defragments the local license store to improve performance.
ms.assetid: 07ddd6f8-a091-4c18-81d3-c4d0c6026b6b
keywords:
- CleanLicenseStore method windows Media Format
- CleanLicenseStore method windows Media Format , IWMDRMLicenseManagement interface
- IWMDRMLicenseManagement interface windows Media Format , CleanLicenseStore method
topic_type:
- apiref
api_name:
- IWMDRMLicenseManagement.CleanLicenseStore
api_location:
- Wmdrmsdk.lib
- Wmdrmsdk.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMDRMLicenseManagement::CleanLicenseStore method

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **CleanLicenseStore** method removes unusable licenses from the temporary license store and defragments the local license store to improve performance.

## Syntax


```C++
HRESULT CleanLicenseStore(
  [in]  DWORD    dwFlags,
  [out] IUnknown **ppunkCancelationCookie
);
```



## Parameters

<dl> <dt>

*dwFlags* \[in\]
</dt> <dd>

Flags specifying the license store cleaning options to use. Set to one of the constants in the following table.



| Constant                            | Description                                                                                                                                                                    |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WMDRM\_CLEAN\_LICENSE\_STORE\_SYNC  | The clean operation will be performed synchronously. This method will not return until the operation is complete.                                                              |
| WMDRM\_CLEAN\_LICENSE\_STORE\_ASYNC | The clean operation will be performed asynchronously. This method will return immediately. When the operation is complete, the media event MELicenseStoreCleaned will be sent. |



 

</dd> <dt>

*ppunkCancelationCookie* \[out\]
</dt> <dd>

Pointer that receives a pointer to the **IUnknown** interface of an object that identifies this asynchronous call. This interface pointer can be used to cancel the asynchronous call by calling the [**IWMDRMEventGenerator::CancelAsyncOperation**](iwmdrmeventgenerator-cancelasyncoperation.md) method.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                                            | Description                                                            |
|--------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                   | The method succeeded.<br/>                                       |
| <dl> <dt>**DRM\_E\_LICENSENOTFOUND**</dt> </dl> | There is no temporary license store on the client computer.<br/> |



 

## Remarks

This method executes asynchronously. It returns immediately after being called and then generates an **MEWMDRMLicenseStoreCleaned** event when processing is complete.

For more information about using the asynchronous methods of the Windows Media DRM Client Extended APIs, see [Using the Media Foundation Event Model](using-the-media-foundation-model.md).

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wmdrmsdk.h</dt> </dl>   |
| Library<br/> | <dl> <dt>Wmdrmsdk.lib</dt> </dl> |



## See also

<dl> <dt>

[**IWMDRMLicenseManagement Interface**](iwmdrmlicensemanagement.md)
</dt> </dl>

 

 





