---
description: The IDownloadJob interface defines the following properties.
ms.assetid: 50e672d7-0ad6-402d-878c-4ac79b70a036
title: IDownloadJob Properties
ms.topic: article
ms.date: 05/31/2018
---

# IDownloadJob Properties

The [**IDownloadJob**](/windows/desktop/api/Wuapi/nn-wuapi-idownloadjob) interface defines the following properties.



| Property                                        | Description                                                                                                                                              |
|-------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AsyncState**](/windows/desktop/api/Wuapi/nf-wuapi-idownloadjob-get_asyncstate)   | Gets the caller-specific state object that is passed to the [**IUpdateDownloader.BeginDownload**](/windows/desktop/api/Wuapi/nf-wuapi-iupdatedownloader-begindownload) method.           |
| [**IsCompleted**](/windows/desktop/api/Wuapi/nf-wuapi-idownloadjob-get_iscompleted) | Gets the setting that indicates whether the call to [**IUpdateDownloader.BeginDownload**](/windows/desktop/api/Wuapi/nf-wuapi-iupdatedownloader-begindownload) was processed completely. |
| [**Updates**](/windows/desktop/api/Wuapi/nf-wuapi-idownloadjob-get_updates)         | Gets an interface that contains a read-only collection of the updates that are specified in a download.                                                  |



 

 

 



