---
title: IWMDRMSecurity PerformSecurityUpdate method (Wmdrmsdk.h)
description: The PerformSecurityUpdate method initiates a security update to the DRM subsystem on the local computer.
ms.assetid: e450a1e3-6024-4c00-9978-fbc88fde2101
keywords:
- PerformSecurityUpdate method windows Media Format
- PerformSecurityUpdate method windows Media Format , IWMDRMSecurity interface
- IWMDRMSecurity interface windows Media Format , PerformSecurityUpdate method
topic_type:
- apiref
api_name:
- IWMDRMSecurity.PerformSecurityUpdate
api_location:
- Wmdrmsdk.lib
- Wmdrmsdk.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMDRMSecurity::PerformSecurityUpdate method

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **PerformSecurityUpdate** method initiates a security update to the DRM subsystem on the local computer.

## Syntax


```C++
HRESULT PerformSecurityUpdate(
  [in]  DWORD    dwFlags,
  [out] IUnknown **ppunkCancelationCookie
);
```



## Parameters

<dl> <dt>

*dwFlags* \[in\]
</dt> <dd>

Update option expressed as one of the following flags.



| Flag                                          | Description                                                                                     |
|-----------------------------------------------|-------------------------------------------------------------------------------------------------|
| WMDRM\_SECURITY\_PERFORM\_INDIV               | Causes the DRM component to be individualized only if the version of the client is out of date. |
| WMDRM\_SECURITY\_PERFORM\_REVOCATION\_REFRESH | Causes the revocation lists on the client computer to be updated.                               |
| WMDRM\_SECURITY\_PERFORM\_FORCE\_INDIV        | Causes the DRM component to be individualized even if the version of the client is up to date.  |



 

</dd> <dt>

*ppunkCancelationCookie* \[out\]
</dt> <dd>

Address of a variable that receives a pointer to an object that can be used to cancel this operation.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## Remarks

This method executes asynchronously. It returns immediately after being called and then generates events depending on the flag set in the *dwFlags* parameter.

For individualization (flag set to WMDRM\_SECURITY\_PERFORM\_INDIV or WMDRM\_SECURITY\_PERFORM\_FORCE\_INDIV), a series of **MEWMDRMIndividualizationProgress** events is generated followed by an **MEWMDRMIndividualizationCompleted** event when processing is complete. The value of each of the **MEWMDRMIndividualizationProgress** events obtained by calling **IMFMediaEvent::GetValue** is an **IUnknown** pointer. You can call the **QueryInterface** method of the retrieved **IUnknown** interface to get an instance of the [**IWMDRMIndividualizationStatus**](iwmdrmindividualizationstatus.md) interface.

For refreshing the revocation lists (flag set to WMDRM\_SECURITY\_PERFORM\_REVOCATION\_REFRESH), an **MEWMDRMREvocationDownloadCompleted** event is generated when processing is complete.

> [!Note]  
> When **PerformSecurityUpdate** completes individualization, the only existing objects that will reflect the new individualized state are those that inherit from **IWMDRMSecurity**. All other existing objects will not be updated. You must release and re-create any other objects so that they will reflect the new individualized state.

 

For more information about using the asynchronous methods of the Windows Media DRM Client Extended APIs, see [Using the Media Foundation Event Model](using-the-media-foundation-model.md).

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wmdrmsdk.h</dt> </dl>   |
| Library<br/> | <dl> <dt>Wmdrmsdk.lib</dt> </dl> |



## See also

<dl> <dt>

[**Automated Component Revocation and Renewal**](automated-component-revocation-and-renewal.md)
</dt> <dt>

[**DRM Individualization Example**](drm-individualization-example.md)
</dt> <dt>

[**IWMDRMSecurity Interface**](iwmdrmsecurity.md)
</dt> <dt>

[**Performing DRM Individualization**](performing-drm-individualization.md)
</dt> </dl>

 

 





