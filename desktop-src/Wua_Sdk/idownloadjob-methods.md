---
description: The IDownloadJob interface defines the following methods.
ms.assetid: b9a6b722-2e32-4177-bcef-514412e132ec
title: IDownloadJob Methods
ms.topic: reference
ms.date: 05/31/2018
---

# IDownloadJob Methods

The [**IDownloadJob**](/windows/desktop/api/Wuapi/nn-wuapi-idownloadjob) interface defines the following methods.



| Method                                            | Description                                                                                                            |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| [**CleanUp**](/windows/desktop/api/Wuapi/nf-wuapi-idownloadjob-cleanup)           | Waits for an asynchronous operation to be completed and releases all callbacks.                                        |
| [**GetProgress**](/windows/desktop/api/Wuapi/nf-wuapi-idownloadjob-getprogress)   | Returns an [**IDownloadProgress**](/windows/desktop/api/Wuapi/nn-wuapi-idownloadprogress) interface that describes the current progress of a download. |
| [**RequestAbort**](/windows/desktop/api/Wuapi/nf-wuapi-idownloadjob-requestabort) | Makes a request to end an asynchronous download.                                                                       |



 

 

 



