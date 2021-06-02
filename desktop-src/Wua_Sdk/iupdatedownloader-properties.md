---
description: The IUpdateDownloader interface defines the following properties.
ms.assetid: b6a30356-f97d-408f-becd-a467e9f8e79f
title: IUpdateDownloader Properties
ms.topic: article
ms.date: 05/31/2018
---

# IUpdateDownloader Properties

The [**IUpdateDownloader**](/windows/desktop/api/Wuapi/nn-wuapi-iupdatedownloader) interface defines the following properties.



| Property                                                             | Description                                                                                                                                                                |
|----------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ClientApplicationID**](/windows/desktop/api/Wuapi/nf-wuapi-iupdatedownloader-get_clientapplicationid) | Gets and sets the current client application.                                                                                                                              |
| [**IsForced**](/windows/desktop/api/Wuapi/nf-wuapi-iupdatedownloader-get_isforced)                       | Gets and sets a Boolean value that indicates whether the Windows Update Agent (WUA) forces the download of updates that are already installed or that cannot be installed. |
| [**Priority**](/windows/desktop/api/Wuapi/nf-wuapi-iupdatedownloader-get_priority)                       | Gets and sets the priority level of the download.                                                                                                                          |
| [**Updates**](/windows/desktop/api/Wuapi/nf-wuapi-iupdatedownloader-get_updates)                         | Gets and sets an interface that contains a read-only collection of the updates that are specified for download.                                                            |



 

 

 



