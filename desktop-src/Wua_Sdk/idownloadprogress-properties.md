---
description: The IDownloadProgress interface defines the following properties.
ms.assetid: 8f64c702-b2b5-4a5f-9365-bc962e35f499
title: IDownloadProgress Properties
ms.topic: article
ms.date: 05/31/2018
---

# IDownloadProgress Properties

The [**IDownloadProgress**](/windows/desktop/api/Wuapi/nn-wuapi-idownloadprogress) interface defines the following properties.



| Property                                                                               | Description                                                                                                                                      |
|----------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CurrentUpdateBytesDownloaded**](/windows/desktop/api/Wuapi/nf-wuapi-idownloadprogress-get_currentupdatebytesdownloaded) | Gets a string that specifies how much data has been transferred for the content file or files of the update that is being downloaded, in bytes.  |
| [**CurrentUpdateBytesToDownload**](/windows/desktop/api/Wuapi/nf-wuapi-idownloadprogress-get_currentupdatebytestodownload) | Gets a string that estimates how much data should be transferred for the content file or files of the update that is being downloaded, in bytes. |
| [**CurrentUpdateDownloadPhase**](/windows/desktop/api/Wuapi/nf-wuapi-idownloadprogress-get_currentupdatedownloadphase)     | Gets a [**DownloadPhase**](/windows/win32/api/wuapi/ne-wuapi-downloadphase) enumeration value that specifies the phase of the download that is currently in progress.          |
| [**CurrentUpdateIndex**](/windows/desktop/api/Wuapi/nf-wuapi-idownloadprogress-get_currentupdateindex)                     | Gets a zero-based index value that specifies the update that is currently being downloaded when multiple updates have been selected.             |
| [**CurrentUpdatePercentComplete**](/windows/desktop/api/Wuapi/nf-wuapi-idownloadprogress-get_currentupdatepercentcomplete) | Gets an estimate of the percentage of the current update that has been downloaded.                                                               |
| [**PercentComplete**](/windows/desktop/api/Wuapi/nf-wuapi-idownloadprogress-get_percentcomplete)                           | Gets an estimate of the percentage of all the updates that have been downloaded.                                                                 |
| [**TotalBytesDownloaded**](/windows/desktop/api/Wuapi/nf-wuapi-idownloadprogress-get_totalbytesdownloaded)                 | Gets a string that specifies the total amount of data that has been downloaded, in bytes.                                                        |
| [**TotalBytesToDownload**](/windows/desktop/api/Wuapi/nf-wuapi-idownloadprogress-get_totalbytestodownload)                 | Gets a string that represents the estimate of the total amount of data that will be downloaded, in bytes.                                        |



 

 

 



