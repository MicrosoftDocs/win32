---
title: IWMDRMLicenseManagement AcquireLicense method (Wmdrmsdk.h)
description: The AcquireLicense method asynchronously acquires a license from a specified URL.
ms.assetid: 2e134f39-1f45-4d3a-b7c7-460aa0a250d0
keywords:
- AcquireLicense method windows Media Format
- AcquireLicense method windows Media Format , IWMDRMLicenseManagement interface
- IWMDRMLicenseManagement interface windows Media Format , AcquireLicense method
topic_type:
- apiref
api_name:
- IWMDRMLicenseManagement.AcquireLicense
api_location:
- Wmdrmsdk.lib
- Wmdrmsdk.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMDRMLicenseManagement::AcquireLicense method

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **AcquireLicense** method asynchronously acquires a license from a specified URL.

## Syntax


```C++
HRESULT AcquireLicense(
  [in]  BSTR     bstrURL,
  [in]  BSTR     bstrHeaderData,
  [in]  BSTR     bstrActions,
  [in]  DWORD    dwFlags,
  [out] IUnknown **ppunkCancelationCookie
);
```



## Parameters

<dl> <dt>

*bstrURL* \[in\]
</dt> <dd>

URL of the license server from which to acquire the license. Pass **NULL** to have the method parse the URL from the content header.

</dd> <dt>

*bstrHeaderData* \[in\]
</dt> <dd>

Content header to be passed to the license server. If *bstrURL* is **NULL**, the method will parse the URL from this header. If *dwFlags* is set to WMDRM\_ACQUIRE\_LICENSE\_LEGACY\_NONSILENT, set this value to the key ID instead of the entire content header.

</dd> <dt>

*bstrActions* \[in\]
</dt> <dd>

String containing zero or more actions for which to request permission in the license. The string must be formatted as follows:

-   Each action must be defined within an ACTION element. The data of the element is the action string.
-   All ACTION elements must be contained within an ACTIONLIST element.

    For example, the string to request a license to play content is formatted like this:

    ```C++
    <ACTIONLIST><ACTION></ACTION></ACTIONLIST>
    ```

    

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

License acquisition option flags. Set to one of the constants in the following table.



| Constant                                   | Description                                                                                                              |
|--------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| WMDRM\_ACQUIRE\_LICENSE\_SILENT            | The license will be issued directly over the Internet without any confirmation from the client application.              |
| WMDRM\_ACQUIRE\_LICENSE\_NONSILENT         | The DRM subsystem will create a license request which will be returned asynchronously for posting to the license server. |
| WMDRM\_ACQUIRE\_LICENSE\_LEGACY\_NONSILENT | The same as WMDRM\_ACQUIRE\_LICENSE\_NONSILENT, except that a DRM version 1 license challenge will be created.           |



 

</dd> <dt>

*ppunkCancelationCookie* \[out\]
</dt> <dd>

Pointer that receives a pointer to the **IUnknown** interface of an object that identifies this asynchronous call. This interface pointer can be used to cancel the asynchronous call by calling the [**IWMDRMEventGenerator::CancelAsyncOperation**](iwmdrmeventgenerator-cancelasyncoperation.md) method.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## Remarks

This method executes asynchronously. It returns immediately after being called and then generates an **MEWMDRMLicenseAcquisitionCompleted** event when processing is complete. For non-silent license acquisition operations, the value of the event obtained by calling **IMFMediaEvent::GetValue** is an **IUnknown** pointer. You can call the **QueryInterface** method of the retrieved **IUnknown** interface to get an instance of the [**IWMDRMNonSilentLicenseAquisition**](iwmdrmnonsilentlicenseaquisition.md) interface.

For more information about using the asynchronous methods of the Windows Media DRM Client Extended APIs, see [Using the Media Foundation Event Model](using-the-media-foundation-model.md).

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wmdrmsdk.h</dt> </dl>   |
| Library<br/> | <dl> <dt>Wmdrmsdk.lib</dt> </dl> |



## See also

<dl> <dt>

[**IWMDRMLicenseManagement Interface**](iwmdrmlicensemanagement.md)
</dt> <dt>

[**Silent License Acquisition**](silent-license-acquisition.md)
</dt> </dl>

 

 





