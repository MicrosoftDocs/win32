---
Description: 'This topic describes how to manage global configuration data.'
ms.assetid: '9cd41d10-1616-4e2d-9abe-e452c582d3b6'
title: Managing Global Configuration Data
---

# Managing Global Configuration Data

You must establish a connection with the fax server before you can retrieve or change configuration information for a fax server. The information includes settings for retransmission, branding, archiving, and cover pages; discount rate periods; and the status of the fax server queue.

## In the Win32 Environment

The [**FaxGetConfiguration**](-mfax-faxgetconfiguration.md) function permits a fax client application to query the global configuration settings for a fax server. The function returns the information in a [**FAX\_CONFIGURATION**](-mfax-fax-configuration-str.md) structure.

Because the [**FaxGetConfiguration**](-mfax-faxgetconfiguration.md) function allocates the memory required for the [**FAX\_CONFIGURATION**](-mfax-fax-configuration-str.md) structure, the application must call the [**FaxFreeBuffer**](-mfax-faxfreebuffer.md) function to deallocate the resources.

To modify a fax server's global configuration settings, an application can call the [**FaxSetConfiguration**](-mfax-faxsetconfiguration.md) function.

Note that an application must first call the [**FaxConnectFaxServer**](-mfax-faxconnectfaxserver.md) function to obtain a fax server handle before calling the [**FaxGetConfiguration**](-mfax-faxgetconfiguration.md) function and the [**FaxSetConfiguration**](-mfax-faxsetconfiguration.md) function.

## In the COM Implementation Environment

You must establish a connection with an active fax server before you can retrieve or set information about [**FaxServer**](-mfax-faxserver.md) objects. For more information, see [Connecting to a Fax Server](-mfax-connecting-to-a-fax-server.md).

If you are writing a C/C++ application, you can use the property methods of the [**IFaxServer**](-mfax-ifaxserver-client.md) interface to retrieve and set global information about [**FaxServer**](-mfax-faxserver.md) objects. For a list of properties and methods, see [**IFaxServer**](-mfax-ifaxserver-client.md).

If you are writing a Microsoft Visual Basic application, you can retrieve and set the properties of [**FaxServer**](-mfax-faxserver.md) objects. See [**FaxServer**](-mfax-faxserver-object-visual-basic-.md) for a list of properties and methods of the object.

 

 



