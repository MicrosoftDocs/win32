---
title: ISystemMediaTransportControlsDisplayUpdater CopyFromFileAsync method
description: Initializes the media properties using the specified file. IRandomAccessStreamReference.
ms.assetid: F6147CD0-034B-486D-BC6A-C52CA0A2F179
keywords:
- CopyFromFileAsync method
- CopyFromFileAsync method, ISystemMediaTransportControlsDisplayUpdater interface
- ISystemMediaTransportControlsDisplayUpdater interface, CopyFromFileAsync method
topic_type:
- apiref
api_name:
- ISystemMediaTransportControlsDisplayUpdater.CopyFromFileAsync
api_location:
- Windows.Media.SystemMediaTransportControls.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ISystemMediaTransportControlsDisplayUpdater::CopyFromFileAsync method

Initializes the media properties using the specified file. IRandomAccessStreamReference

## Syntax


```C++
HRESULT CopyFromFileAsync(
        MediaPlaybackType type,
        IStorageFile      *source,
  [out] IAsyncOperation   **operation
);
```



## Parameters

<dl> <dt>

*type* 
</dt> <dd>

Type: **[**MediaPlaybackType**](https://msdn.microsoft.com/library/windows/apps/dn278668)**

The type of media being played.

</dd> <dt>

*source* 
</dt> <dd>

Type: **[**IStorageFile**](https://msdn.microsoft.com/library/windows/apps/br227102)\***

The file to initialize the media properties.

</dd> <dt>

*operation* \[out\]
</dt> <dd>

Type: **[**IAsyncOperation**](https://msdn.microsoft.com/library/windows/desktop/br205802)\*\***

An asynchronous operation that returns a boolean indicating the success of the operation upon completion.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                                           |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                                                      |
| Header<br/>                   | <dl> <dt>Windows.Media.SystemMediaTransportControls.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Windows.Media.SystemMediaTransportControls.idl</dt> </dl> |



## See also

<dl> <dt>

[**ISystemMediaTransportControlsDisplayUpdater**](isystemmediatransportcontrolsdisplayupdater.md)
</dt> </dl>

 

 





