---
Description: This tutorial summarizes typical programming tasks required to incorporate the functionality of the Fax Service Client API in a C/C++ fax client application if you are using the Component Object Model (COM) implementation.
ms.assetid: bb933251-b196-4a6b-aaa3-b2c75c2dcf4b
title: Using the COM Implementation in a C/C++ Program
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using the COM Implementation in a C/C++ Program

The following steps summarize typical programming tasks required to incorporate the functionality of the Fax Service Client API in a C/C++ fax client application if you are using the Component Object Model (COM) implementation.

## To code a fax client application

1.  Create an instance of a [**FaxServer**](-mfax-faxserver.md) object by calling the [CoCreateInstance](http://msdn.microsoft.com/en-us/library/ms686615.aspx) function. Then connect to an active fax server using a call to the [**IFaxServer::Connect**](/previous-versions/windows/desktop/api/faxcomex/) interface method. For more information, see [Connecting to a Fax Server](-mfax-connecting-to-a-fax-server.md) and [**IFaxServer**](/previous-versions/windows/desktop/api/faxcom/nn-faxcom-ifaxserver).

2.  Create the objects you need by calling one or more of the following [**IFaxServer**](/previous-versions/windows/desktop/api/faxcom/nn-faxcom-ifaxserver) interface methods.

    -   The [**IFaxServer::GetJobs**](/previous-versions/windows/desktop/api/faxcomex/) method to create a [FaxJobs](-mfax-faxjobs.md) object. Use this object to create [FaxJob](-mfax-faxjob.md) objects and enumerate the fax jobs associated with the connected fax server.
    -   The [**IFaxServer::GetPorts**](/previous-versions/windows/desktop/api/faxcomex/) method to create a [FaxPorts](-mfax-faxports.md) object. Use this object to create [FaxPort](-mfax-faxport.md) objects and enumerate fax port configuration information for a connected fax server.
    -   The [**IFaxServer::CreateDocument**](/previous-versions/windows/desktop/api/faxcomex/) method to create a [FaxDoc](-mfax-faxdoc.md) object. Use this object to transmit a fax and to retrieve and set the properties of FaxDoc objects.

3.  After creating an instance of a [FaxPort](-mfax-faxport.md) object for a specific port, call the [**IFaxPort::GetRoutingMethods**](/previous-versions/windows/desktop/api/Faxcom/nf-faxcom-ifaxport-getroutingmethods) interface method to create a [FaxRoutingMethods](-mfax-faxroutingmethods.md) object. Also call the [**IFaxRoutingMethods::get\_Item**](/previous-versions/windows/desktop/api/Faxcom/nf-faxcom-ifaxroutingmethods-get_item) interface method to create a [FaxRoutingMethod](-mfax-faxroutingmethod.md) object. The FaxRoutingMethod object allows you to query and modify the fax routing information for a fax port. For more information, see [Managing Fax Routing Data](-mfax-managing-fax-routing-data.md).

4.  To create a [FaxStatus](-mfax-faxstatus.md) object, call the [**IFaxPort::GetStatus**](/previous-versions/windows/desktop/api/Faxcom/nf-faxcom-ifaxport-getstatus) interface method. The FaxStatus object allows you to provide real-time status information about a fax port.

5.  After creating an instance of a [FaxDoc](-mfax-faxdoc.md) object, transmit a fax document by calling the [**IFaxDoc::Send**](/previous-versions/windows/desktop/api/Faxcom/) interface method. Note that the application must supply transmission information such as the fax number and the name of the file to transmit. The client can also supply other data that appears on the cover page by setting various properties of the FaxDoc object. For more information, see [Transmitting Faxes](-mfax-transmitting-faxes.md).

6.  Call the [SysFreeString](https://msdn.microsoft.com/windows/desktop/8f230ee3-5f6e-4cb9-a910-9c90b754dcd3) function when appropriate to deallocate the resources allocated by all interface methods that end with **get\_PropertyName**. For more information, see [Freeing Fax Resources](-mfax-freeing-fax-resources.md).

7.  Call the [**IFaxServer::Disconnect**](/previous-versions/windows/desktop/api/faxcomex/) interface method to terminate the connection to the fax server. Then call the [IUnknown](http://msdn.microsoft.com/en-us/library/ms680509.aspx)::[IUnknown::Release](http://msdn.microsoft.com/en-us/library/ms682317.aspx) method to allow the [**FaxServer**](-mfax-faxserver.md) object to deallocate itself. For more information, see [Disconnecting from a Fax Server](-mfax-disconnecting-from-a-fax-server.md).

In addition, the application may need to call other interface methods to query device or server configuration data, to manage fax jobs, and to destroy additional interface pointers. You may also need to create an instance of a [FaxTiff](-mfax-faxtiff.md) object and call [**IFaxTiff**](/previous-versions/windows/desktop/api/Faxcom/nn-faxcom-ifaxtiff) interface methods to retrieve information about a file the fax service has sent or received.

Note that a client application must call the [CoCreateInstance](http://msdn.microsoft.com/en-us/library/ms686615.aspx) function to create an instance of a [**FaxServer**](-mfax-faxserver.md) or [FaxTiff](-mfax-faxtiff.md) object. However, do not call the CoCreateInstance function to create [FaxDoc](-mfax-faxdoc.md), [FaxJobs](-mfax-faxjobs.md), [FaxJob](-mfax-faxjob.md), [FaxPorts](-mfax-faxports.md), [FaxPort](-mfax-faxport.md), [FaxStatus](-mfax-faxstatus.md), [FaxRoutingMethods](-mfax-faxroutingmethods.md), or [FaxRoutingMethod](-mfax-faxroutingmethod.md) objects. For more information about creating and deallocating fax client objects, see the steps listed with each interface topic and the hierarchical diagram in [The Fax Client Object Model](-mfax-the-fax-client-object-model.md).

For more information, see [Fax Server Configuration Management](-mfax-fax-server-configuration-management.md), [Fax Device Management](-mfax-fax-device-management.md), [Managing Fax Jobs](-mfax-managing-fax-jobs.md), and [General Fax Client Programming Tasks](-mfax-general-fax-client-programming-tasks.md).

 

 



