---
title: IWMDRMLicenseManagement BackupLicenses method (Wmdrmsdk.h)
description: The BackupLicenses method creates a backup of the licenses in the local license store.
ms.assetid: f265254d-b240-4a9f-9c67-de9c92e8a14d
keywords:
- BackupLicenses method windows Media Format
- BackupLicenses method windows Media Format , IWMDRMLicenseManagement interface
- IWMDRMLicenseManagement interface windows Media Format , BackupLicenses method
topic_type:
- apiref
api_name:
- IWMDRMLicenseManagement.BackupLicenses
api_location:
- Wmdrmsdk.lib
- Wmdrmsdk.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMDRMLicenseManagement::BackupLicenses method

The **BackupLicenses** method creates a backup of the licenses in the local license store.

## Syntax


```C++
HRESULT BackupLicenses(
  [in]  BSTR     bstrBackupDirectory,
  [in]  DWORD    dwFlags,
  [out] IUnknown **ppunkCancelationCookie
);
```



## Parameters

<dl> <dt>

*bstrBackupDirectory* \[in\]
</dt> <dd>

UNC path of the location to which the licenses will be backed up.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Flags specifying the backup options to use. The only flag currently supported is WMDRM\_BACKUP\_OVERWRITE, which configures the method to overwrite any existing backup files in the directory.

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

This method executes asynchronously. It returns immediately after being called and then generates a series of **MEWMDRMLicenseBackupProgress** events followed by an **MEWMDRMLicenseBackupCompleted** event when processing is complete. The value of each of the **MEWMDRMLicenseBackupProgress** events obtained by calling **IMFMediaEvent::GetValue** is an **IUnknown** pointer. You can call the **QueryInterface** method of the retrieved **IUnknown** interface to get an instance of the [**IWMDRMLicenseBackupRestoreStatus**](iwmdrmlicensebackuprestorestatus.md) interface.

For more information about using the asynchronous methods of the Windows Media DRM Client Extended APIs, see [Using the Media Foundation Event Model](using-the-media-foundation-model.md).

Not all licenses are permitted to be backed up. This method only backs up licenses that allow it.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wmdrmsdk.h</dt> </dl>   |
| Library<br/> | <dl> <dt>Wmdrmsdk.lib</dt> </dl> |



## See also

<dl> <dt>

[**IWMDRMLicenseManagement Interface**](iwmdrmlicensemanagement.md)
</dt> </dl>

 

 





