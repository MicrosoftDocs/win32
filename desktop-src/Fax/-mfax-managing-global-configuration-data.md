---
Description: This topic describes how to manage global configuration data.
ms.assetid: 9cd41d10-1616-4e2d-9abe-e452c582d3b6
title: Managing Global Configuration Data
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Managing Global Configuration Data

You must establish a connection with the fax server before you can retrieve or change configuration information for a fax server. The information includes settings for retransmission, branding, archiving, and cover pages; discount rate periods; and the status of the fax server queue.

## In the Win32 Environment

The [**FaxGetConfiguration**](/windows/previous-versions/Winfax/nf-winfax-faxgetconfigurationa?branch=master) function permits a fax client application to query the global configuration settings for a fax server. The function returns the information in a [**FAX\_CONFIGURATION**](/windows/previous-versions/Winfax/ns-winfax-_fax_configurationa?branch=master) structure.

Because the [**FaxGetConfiguration**](/windows/previous-versions/Winfax/nf-winfax-faxgetconfigurationa?branch=master) function allocates the memory required for the [**FAX\_CONFIGURATION**](/windows/previous-versions/Winfax/ns-winfax-_fax_configurationa?branch=master) structure, the application must call the [**FaxFreeBuffer**](/windows/previous-versions/Winfax/nc-winfax-pfaxfreebuffer?branch=master) function to deallocate the resources.

To modify a fax server's global configuration settings, an application can call the [**FaxSetConfiguration**](/windows/previous-versions/Winfax/nf-winfax-faxsetconfigurationa?branch=master) function.

Note that an application must first call the [**FaxConnectFaxServer**](/windows/previous-versions/Winfax/nf-winfax-faxconnectfaxservera?branch=master) function to obtain a fax server handle before calling the [**FaxGetConfiguration**](/windows/previous-versions/Winfax/nf-winfax-faxgetconfigurationa?branch=master) function and the [**FaxSetConfiguration**](/windows/previous-versions/Winfax/nf-winfax-faxsetconfigurationa?branch=master) function.

## In the COM Implementation Environment

You must establish a connection with an active fax server before you can retrieve or set information about [**FaxServer**](-mfax-faxserver.md) objects. For more information, see [Connecting to a Fax Server](-mfax-connecting-to-a-fax-server.md).

If you are writing a C/C++ application, you can use the property methods of the [**IFaxServer**](/windows/previous-versions/faxcom/nn-faxcom-ifaxserver?branch=master) interface to retrieve and set global information about [**FaxServer**](-mfax-faxserver.md) objects. For a list of properties and methods, see [**IFaxServer**](/windows/previous-versions/faxcom/nn-faxcom-ifaxserver?branch=master).

If you are writing a Microsoft Visual Basic application, you can retrieve and set the properties of [**FaxServer**](-mfax-faxserver.md) objects. See [**FaxServer**](-mfax-faxserver-object-visual-basic-.md) for a list of properties and methods of the object.

 

 



