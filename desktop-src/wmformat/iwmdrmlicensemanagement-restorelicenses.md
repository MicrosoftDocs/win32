---
title: IWMDRMLicenseManagement RestoreLicenses method (Wmdrmsdk.h)
description: The RestoreLicenses method restores licenses from a license backup that was created by calling the BackupLicenses method.
ms.assetid: 83e4b748-0f69-4a9e-b531-047c9a2be1fe
keywords:
- RestoreLicenses method windows Media Format
- RestoreLicenses method windows Media Format , IWMDRMLicenseManagement interface
- IWMDRMLicenseManagement interface windows Media Format , RestoreLicenses method
topic_type:
- apiref
api_name:
- IWMDRMLicenseManagement.RestoreLicenses
api_location:
- Wmdrmsdk.lib
- Wmdrmsdk.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMDRMLicenseManagement::RestoreLicenses method

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **RestoreLicenses** method restores licenses from a license backup that was created by calling the [**BackupLicenses**](iwmdrmlicensemanagement-backuplicenses.md) method.

## Syntax


```C++
HRESULT RestoreLicenses(
  [in]  BSTR     bstrBackupDirectory,
  [in]  DWORD    dwFlags,
  [out] IUnknown **ppunkCancelationCookie
);
```



## Parameters

<dl> <dt>

*bstrBackupDirectory* \[in\]
</dt> <dd>

UNC path of the location from which the licenses will be restored.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Flags specifying the restore options to use. The only flag currently supported is WMDRM\_RESTORE\_INDIVIDUALIZE, which configures the method to perform individualization as part of the restoration, if required.

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

This method executes asynchronously. It returns immediately after being called and then generates a series of **MEWMDRMLicenseRestoreProgress** events followed by an **MEWMDRMLicenseRestoreCompleted** event when processing is complete. The value of each of the **MEWMDRMLicenseRestoreProgress** events obtained by calling **IMFMediaEvent::GetValue** is an **IUnknown** pointer. You can call the **QueryInterface** method of the retrieved **IUnknown** interface to get an instance of the [**IWMDRMLicenseBackupRestoreStatus**](iwmdrmlicensebackuprestorestatus.md) interface.

For more information about using the asynchronous methods of the Windows Media DRM Client Extended APIs, see [Using the Media Foundation Event Model](using-the-media-foundation-model.md).

The backup can be from the local machine or from a different machine.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wmdrmsdk.h</dt> </dl>   |
| Library<br/> | <dl> <dt>Wmdrmsdk.lib</dt> </dl> |



## See also

<dl> <dt>

[**IWMDRMLicenseManagement Interface**](iwmdrmlicensemanagement.md)
</dt> </dl>

 

 





