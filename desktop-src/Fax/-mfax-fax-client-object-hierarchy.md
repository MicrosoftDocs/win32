---
Description: 'Most of the Component Object Model (COM) interfaces in the Fax Service Client API are hierarchical in nature.'
ms.assetid: 'ee48c2cc-36aa-4c73-b847-07ab54ab3b8d'
title: Fax Client Object Hierarchy
---

# Fax Client Object Hierarchy

Most of the Component Object Model (COM) interfaces in the Fax Service Client API are hierarchical in nature. For example, the client application must call the [**IFaxServer::Connect**](-mfax-ifaxserver-client-mfax-ifaxserver-connect-client-cpp.md) method (or the **Connect** Microsoft Visual Basic method of the [FaxServer](-mfax-faxserver-client.md) object) to establish a connection with a fax server before accessing other interfaces that begin with **IFax**, or other fax client objects. (The [FaxTiff](-mfax-faxtiff.md) object is an exception: a fax server connection is not required to access a FaxTiff object.)

After a client application establishes a connection through remote procedure call (RPC) to an active fax server, the application can call other interface methods. This is because the active [FaxServer](-mfax-faxserver-client.md) object "knows" the fax server to which it is connected. For example, the application can call one of the following methods.

-   The [**IFaxServer::GetJobs**](-mfax-ifaxserver-client-mfax-ifaxserver-getjobs-cpp.md) method (or the **GetJobs** Visual Basic method of the [FaxServer](-mfax-faxserver-client.md) object) to create a [FaxJobs](-mfax-faxjobs.md) object and retrieve a list of the fax jobs associated with the connected fax server.
-   The [**IFaxServer::GetPorts**](-mfax-ifaxserver-client-mfax-ifaxserver-getports-cpp.md) method (or the **GetPorts** Visual Basic method of the [FaxServer](-mfax-faxserver-client.md) object) to create a [FaxPorts](-mfax-faxports.md) object and retrieve a list of ports associated with the connected fax server.
-   The [**IFaxServer::CreateDocument**](-mfax-ifaxserver-client-mfax-ifaxserver-createdocument-cpp.md) method (or the **CreateDocument** Visual Basic method of the [FaxServer](-mfax-faxserver-client.md) object) to create a [FaxDoc](-mfax-faxdoc.md) object and send a fax transmission.

A client application should not call the [CoCreateInstance](http://msdn.microsoft.com/en-us/library/ms686615.aspx) function to create these objects or objects derived from them. For more information about creating fax client objects, see the steps that are listed with each interface topic, the [Fax Service Client API Visual Basic Reference](-mfax-fax-service-client-api-visual-basic-reference.md), and the hierarchical diagram in [The Fax Client Object Model](-mfax-the-fax-client-object-model.md).

 

 



