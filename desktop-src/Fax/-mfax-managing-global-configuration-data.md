---
Description: This topic describes how to manage global configuration data.
ms.assetid: 9cd41d10-1616-4e2d-9abe-e452c582d3b6
title: Managing Global Configuration Data
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Managing Global Configuration Data

You must establish a connection with the fax server before you can retrieve or change configuration information for a fax server. The information includes settings for retransmission, branding, archiving, and cover pages; discount rate periods; and the status of the fax server queue.

## In the Win32 Environment

The [**FaxGetConfiguration**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxgetconfigurationa) function permits a fax client application to query the global configuration settings for a fax server. The function returns the information in a [**FAX\_CONFIGURATION**](/previous-versions/windows/desktop/api/Winfax/ns-winfax-_fax_configurationa) structure.

Because the [**FaxGetConfiguration**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxgetconfigurationa) function allocates the memory required for the [**FAX\_CONFIGURATION**](/previous-versions/windows/desktop/api/Winfax/ns-winfax-_fax_configurationa) structure, the application must call the [**FaxFreeBuffer**](/previous-versions/windows/desktop/api/Winfax/nc-winfax-pfaxfreebuffer) function to deallocate the resources.

To modify a fax server's global configuration settings, an application can call the [**FaxSetConfiguration**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxsetconfigurationa) function.

Note that an application must first call the [**FaxConnectFaxServer**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxconnectfaxservera) function to obtain a fax server handle before calling the [**FaxGetConfiguration**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxgetconfigurationa) function and the [**FaxSetConfiguration**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxsetconfigurationa) function.

## In the COM Implementation Environment

You must establish a connection with an active fax server before you can retrieve or set information about [**FaxServer**](-mfax-faxserver.md) objects. For more information, see [Connecting to a Fax Server](-mfax-connecting-to-a-fax-server.md).

If you are writing a C/C++ application, you can use the property methods of the [**IFaxServer**](/previous-versions/windows/desktop/api/faxcom/nn-faxcom-ifaxserver) interface to retrieve and set global information about [**FaxServer**](-mfax-faxserver.md) objects. For a list of properties and methods, see [**IFaxServer**](/previous-versions/windows/desktop/api/faxcom/nn-faxcom-ifaxserver).

If you are writing a Microsoft Visual Basic application, you can retrieve and set the properties of [**FaxServer**](-mfax-faxserver.md) objects. See [**FaxServer**](-mfax-faxserver-object-visual-basic-.md) for a list of properties and methods of the object.

 

 



