---
Description: In most situations, a fax client application must establish a connection to a fax server before the application can use other fax features.
ms.assetid: da213475-2cfb-4524-80af-51c1ee0bf658
title: Connecting to a Fax Server
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Connecting to a Fax Server

In most situations, a fax client application must establish a connection to a fax server before the application can use other fax features. The following table compares client-server connectivity in Windows 2000, Windows XP, and Windows Server 2003.



| Server/Client                                            | Windows 2000 Personal Fax | Windows XP Fax                                | Windows Server 2003 Fax |
|----------------------------------------------------------|---------------------------|-----------------------------------------------|-------------------------|
| Windows 2000 Personal Fax                                | Only to local computer    | Not supported                                 | Not supported           |
| Windows 2000 Server (provides Windows 2000 Personal Fax) | Only to local computer    | Not supported                                 | Not supported           |
| Windows XP Fax                                           | Not supported             | Supported, only local submission of new faxes | Supported               |
| Windows Server 2003 Fax                                  | Not supported             | Supported                                     | Supported               |



 

## In the Win32 Environment

To establish the connection to the local fax server, a fax client application must call the [**FaxConnectFaxServer**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxconnectfaxservera) function successfully before it calls any other fax client function. **FaxConnectFaxServer** returns a fax server handle that is required to call many other fax client functions. The **FaxConnectFaxServer** function can only be used only with a local server.

Note that a connection to a fax server is not required to print a fax document to a fax printer device context. An application can provide transmission information directly to the fax client Windows Graphics Device Interface (GDI) functions, and transmit the active document by printing it to a printer device context. The fax client GDI functions include the [**FaxStartPrintJob**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxstartprintjoba) and the [**FaxPrintCoverPage**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxprintcoverpagea) functions. For more information, see [Printing a Fax to a Device Context](-mfax-printing-a-fax-to-a-device-context.md).

Call the [**FaxClose**](/previous-versions/windows/desktop/api/Winfax/nc-winfax-pfaxclose) function to disconnect from the fax server and deallocate the handle that the [**FaxConnectFaxServer**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxconnectfaxservera) function returns.

## In the COM Implementation Environment

If you are writing a C/C++ application, you must call the [CoCreateInstance](http://msdn.microsoft.com/en-us/library/ms686615.aspx) function to retrieve a pointer to an [**IFaxServer**](/previous-versions/windows/desktop/api/faxcom/nn-faxcom-ifaxserver) interface and create an instance of a [FaxServer](-mfax-faxserver-client.md) object. Then you must call the [**IFaxServer::Connect**](/previous-versions/windows/desktop/api/faxcomex/) method to initiate a connection with an active fax server. The server connection is required before the application can access most interfaces that begin with **IFax**. (A fax server connection is not required to access an [**IFaxTiff**](/previous-versions/windows/desktop/api/Faxcom/nn-faxcom-ifaxtiff) interface.) For more information about creating a FaxServer object, and for a list of properties and methods, see **IFaxServer**.

If you are writing a Microsoft Visual Basic application, you must call the Visual Basic [**CreateObject**](https://msdn.microsoft.com/windows/desktop/ec11fd03-b420-412f-b25a-057f877cefbc) function to create an instance of a [FaxServer](-mfax-faxserver-client.md) object. Then you must call the [**Connect**](/previous-versions/windows/desktop/api/FaxComex/nf-faxcomex-ifaxserver-connect) method of the FaxServer object to initiate a connection with an active fax server. The server connection is required before the application can access most other objects that begin with **Fax**. (A fax server connection is not required to access a [**IFaxTiff**](/previous-versions/windows/desktop/api/Faxcom/nn-faxcom-ifaxtiff) object.) See FaxServer object (Visual Basic) for more information about the steps required to create the object, and for a list of properties and methods of the object.

## Related topics

<dl> <dt>

[Disconnecting from a Fax Server](-mfax-disconnecting-from-a-fax-server.md)
</dt> </dl>

 

 



