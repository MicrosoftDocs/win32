---
title: ADSI Objects of WinNT
description: The ADSI WinNT provider implement the following COM objects to support features and services of various ADSI interfaces.
ms.assetid: ce6f8638-aa9e-4036-b597-077da4c3c534
ms.tgt_platform: multiple
keywords:
- WinNT service provider ADSI ,ADSI objects
ms.topic: article
ms.date: 05/31/2018
---

# ADSI Objects of WinNT

The ADSI WinNT provider implement the following COM objects to support features and services of various ADSI interfaces.




| ADSI Object | Description | Supported Interfaces | 
|-------------|-------------|----------------------|
| <strong>Class</strong> | An ADSI object that represents a class definition. | <dl><dt><a href="/windows/desktop/api/Iads/nn-iads-iads"><strong>IADs</strong></a></dt><dt><a href="/windows/desktop/api/Iads/nn-iads-iadsclass"><strong>IADsClass</strong></a></dt></dl> | 
| <strong>Computer</strong> | An ADSI object that represents a computer. | <dl><dt><a href="/windows/desktop/api/Iads/nn-iads-iads"><strong>IADs</strong></a></dt><dt><a href="/windows/desktop/api/Iads/nn-iads-iadscomputer"><strong>IADsComputer</strong></a></dt><dt><a href="/windows/desktop/api/Iads/nn-iads-iadscomputeroperations"><strong>IADsComputerOperations</strong></a></dt><dt><a href="/windows/desktop/api/Iads/nn-iads-iadscontainer"><strong>IADsContainer</strong></a></dt><dt><a href="/windows/desktop/api/Iads/nn-iads-iadspropertylist"><strong>IADsPropertyList</strong></a></dt></dl> | 
| <strong>Domain</strong> | An ADSI object that represents a domain over the network. | <dl><dt><a href="/windows/desktop/api/Iads/nn-iads-iads"><strong>IADs</strong></a></dt><dt><a href="/windows/desktop/api/Iads/nn-iads-iadsdomain"><strong>IADsDomain</strong></a></dt><dt><a href="/windows/desktop/api/Iads/nn-iads-iadscontainer"><strong>IADsContainer</strong></a></dt><dt><a href="/windows/desktop/api/Iads/nn-iads-iadspropertylist"><strong>IADsPropertyList</strong></a></dt></dl> | 
| <strong>FileService</strong> | An ADSI object that represents a file service. | <dl><dt><a href="/windows/desktop/api/Iads/nn-iads-iads"><strong>IADs</strong></a></dt><dt><a href="/windows/desktop/api/Iads/nn-iads-iadsfileservice"><strong>IADsFileService</strong></a></dt><dt><a href="/windows/desktop/api/Iads/nn-iads-iadsfileserviceoperations"><strong>IADsFileServiceOperations</strong></a></dt><dt><a href="/windows/desktop/api/Iads/nn-iads-iadscontainer"><strong>IADsContainer</strong></a></dt><dt><a href="/windows/desktop/api/Iads/nn-iads-iadspropertylist"><strong>IADsPropertyList</strong></a></dt></dl> | 
| <strong>FileShare</strong> | An ADSI object that represents a file share. | <dl><dt><a href="/windows/desktop/api/Iads/nn-iads-iads"><strong>IADs</strong></a></dt><dt><a href="/windows/desktop/api/Iads/nn-iads-iadsfileshare"><strong>IADsFileShare</strong></a></dt><dt><a href="/windows/desktop/api/Iads/nn-iads-iadspropertylist"><strong>IADsPropertyList</strong></a></dt></dl> | 
| <strong>FPNWFileService</strong> | An ADSI object that represents a file service. | <dl><dt><a href="/windows/desktop/api/Iads/nn-iads-iads"><strong>IADs</strong></a></dt><dt><a href="/windows/desktop/api/Iads/nn-iads-iadsfileservice"><strong>IADsFileService</strong></a></dt><dt><a href="/windows/desktop/api/Iads/nn-iads-iadsfileserviceoperations"><strong>IADsFileServiceOperations</strong></a></dt><dt><a href="/windows/desktop/api/Iads/nn-iads-iadscontainer"><strong>IADsContainer</strong></a></dt></dl> | 
| <strong>FPNWFileShare</strong> | An ADSI object that represents a file share. | <dl><dt><a href="/windows/desktop/api/Iads/nn-iads-iads"><strong>IADs</strong></a></dt><dt><a href="/windows/desktop/api/Iads/nn-iads-iadsfileshare"><strong>IADsFileShare</strong></a></dt><dt><a href="/windows/desktop/api/Iads/nn-iads-iadspropertylist"><strong>IADsPropertyList</strong></a></dt></dl> | 
| <strong>FPNWResource</strong> | An ADSI object that represents a resource. | <dl><dt><a href="/windows/desktop/api/Iads/nn-iads-iads"><strong>IADs</strong></a></dt><dt><a href="/windows/desktop/api/Iads/nn-iads-iadsresource"><strong>IADsResource</strong></a></dt><dt><a href="/windows/desktop/api/Iads/nn-iads-iadspropertylist"><strong>IADsPropertyList</strong></a></dt></dl> | 
| <strong>FPNWResourcesCollection</strong> | An ADSI object that represents a collection of resources. | <a href="/windows/desktop/api/Iads/nn-iads-iadscollection"><strong>IADsCollection</strong></a> | 
| <strong>FPNWSession</strong> | An ADSI object that represents a session. | <dl><dt><a href="/windows/desktop/api/Iads/nn-iads-iads"><strong>IADs</strong></a></dt><dt><a href="/windows/desktop/api/Iads/nn-iads-iadssession"><strong>IADsSession</strong></a></dt><dt><a href="/windows/desktop/api/Iads/nn-iads-iadspropertylist"><strong>IADsPropertyList</strong></a></dt></dl> | 
| <strong>FPNWSessionsCollection</strong> | An ADSI object that represents a collection of sessions. | <a href="/windows/desktop/api/Iads/nn-iads-iadscollection"><strong>IADsCollection</strong></a> | 
| <strong>Group</strong> | An ADSI object that represents a group. | <dl><dt><a href="/windows/desktop/api/Iads/nn-iads-iads"><strong>IADs</strong></a></dt><dt><a href="/windows/desktop/api/Iads/nn-iads-iadsgroup"><strong>IADsGroup</strong></a></dt><dt><a href="/windows/desktop/api/Iads/nn-iads-iadspropertylist"><strong>IADsPropertyList</strong></a></dt></dl><blockquote>[!Note]<br />GetInfo cannot be used for groups that contain members that are wellKnown security principals in the WinNT scope.</blockquote><br /> | 
| <strong>GroupCollection</strong> | An ADSI object that represents a collection of groups. | <dl><dt><a href="/windows/desktop/api/Iads/nn-iads-iads"><strong>IADs</strong></a></dt><dt><a href="/windows/desktop/api/Iads/nn-iads-iadsmembers"><strong>IADsMembers</strong></a></dt></dl> | 
| <strong>LocalGroup</strong> | An ADSI object that represents a local group. | <dl><dt><a href="/windows/desktop/api/Iads/nn-iads-iads"><strong>IADs</strong></a></dt><dt><a href="/windows/desktop/api/Iads/nn-iads-iadsgroup"><strong>IADsGroup</strong></a></dt><dt><a href="/windows/desktop/api/Iads/nn-iads-iadspropertylist"><strong>IADsPropertyList</strong></a></dt></dl> | 
| <strong>LocalgroupCollection</strong> | An ADSI object that represents a collection of local groups. | <dl><dt><a href="/windows/desktop/api/Iads/nn-iads-iads"><strong>IADs</strong></a></dt><dt><a href="/windows/desktop/api/Iads/nn-iads-iadsmembers"><strong>IADsMembers</strong></a></dt></dl> | 
| <strong>Namespace</strong> | An ADSI object that represents the WinNT namespace. | <dl><dt><a href="/windows/desktop/api/Iads/nn-iads-iads"><strong>IADs</strong></a></dt><dt><a href="/windows/desktop/api/Iads/nn-iads-iadscontainer"><strong>IADsContainer</strong></a></dt><dt><a href="/windows/desktop/api/Iads/nn-iads-iadsopendsobject"><strong>IADsOpenDSObject</strong></a></dt></dl> | 
| <strong>PrintJob</strong> | An ADSI object that represents a print job. | <dl><dt><a href="/windows/desktop/api/Iads/nn-iads-iads"><strong>IADs</strong></a></dt><dt><a href="/windows/desktop/api/Iads/nn-iads-iadsprintjob"><strong>IADsPrintJob</strong></a></dt><dt><a href="/windows/desktop/api/Iads/nn-iads-iadsprintjoboperations"><strong>IADsPrintJobOperations</strong></a></dt><dt><a href="/windows/desktop/api/Iads/nn-iads-iadspropertylist"><strong>IADsPropertyList</strong></a></dt></dl> | 
| <strong>PrintJobsCollection</strong> | An ADSI object that represents a collection of print jobs. | <a href="/windows/desktop/api/Iads/nn-iads-iadscollection"><strong>IADsCollection</strong></a> | 
| <strong>PrintQueue</strong> | An ADSI object that represents a print queue. | <dl><dt><a href="/windows/desktop/api/Iads/nn-iads-iads"><strong>IADs</strong></a></dt><dt><a href="/windows/desktop/api/Iads/nn-iads-iadsprintqueue"><strong>IADsPrintQueue</strong></a></dt><dt><a href="/windows/desktop/api/Iads/nn-iads-iadsprintqueueoperations"><strong>IADsPrintQueueOperations</strong></a></dt><dt><a href="/windows/desktop/api/Iads/nn-iads-iadspropertylist"><strong>IADsPropertyList</strong></a></dt></dl> | 
| <strong>Property</strong> | An ADSI object that represents an attribute definition. | <dl><dt><a href="/windows/desktop/api/Iads/nn-iads-iads"><strong>IADs</strong></a></dt><dt><a href="/windows/desktop/api/Iads/nn-iads-iadsproperty"><strong>IADsProperty</strong></a></dt></dl> | 
| <strong>Resource</strong> | An ADSI object that represents a resource. | <dl><dt><a href="/windows/desktop/api/Iads/nn-iads-iads"><strong>IADs</strong></a></dt><dt><a href="/windows/desktop/api/Iads/nn-iads-iadsresource"><strong>IADsResource</strong></a></dt><dt><a href="/windows/desktop/api/Iads/nn-iads-iadspropertylist"><strong>IADsPropertyList</strong></a></dt></dl> | 
| <strong>ResourcesCollection</strong> | An ADSI object that represents a collection of resources. | <a href="/windows/desktop/api/Iads/nn-iads-iadscollection"><strong>IADsCollection</strong></a> | 
| <strong>Schema</strong> | An ADSI object that represents the schema container. | <dl><dt><a href="/windows/desktop/api/Iads/nn-iads-iads"><strong>IADs</strong></a></dt><dt><a href="/windows/desktop/api/Iads/nn-iads-iadscontainer"><strong>IADsContainer</strong></a></dt></dl> | 
| <strong>Service</strong> | An ADSI object that represents a service. | <dl><dt><a href="/windows/desktop/api/Iads/nn-iads-iads"><strong>IADs</strong></a></dt><dt><a href="/windows/desktop/api/Iads/nn-iads-iadsservice"><strong>IADsService</strong></a></dt><dt><a href="/windows/desktop/api/Iads/nn-iads-iadsserviceoperations"><strong>IADsServiceOperations</strong></a></dt><dt><a href="/windows/desktop/api/Iads/nn-iads-iadspropertylist"><strong>IADsPropertyList</strong></a></dt></dl> | 
| <strong>Session</strong> | An ADSI object that represents a session. | <dl><dt><a href="/windows/desktop/api/Iads/nn-iads-iads"><strong>IADs</strong></a></dt><dt><a href="/windows/desktop/api/Iads/nn-iads-iadssession"><strong>IADsSession</strong></a></dt><dt><a href="/windows/desktop/api/Iads/nn-iads-iadspropertylist"><strong>IADsPropertyList</strong></a></dt></dl> | 
| <strong>SessionsCollection</strong> | An ADSI object that represents a collection of sessions. | <a href="/windows/desktop/api/Iads/nn-iads-iadscollection"><strong>IADsCollection</strong></a> | 
| <strong>Syntax</strong> | An ADSI object that represents the syntax of an attribute. | <dl><dt><a href="/windows/desktop/api/Iads/nn-iads-iads"><strong>IADs</strong></a></dt><dt><a href="/windows/desktop/api/Iads/nn-iads-iadssyntax"><strong>IADsSyntax</strong></a></dt></dl> | 
| <strong>User</strong> | An ADSI object that represents a user account. | <dl><dt><a href="/windows/desktop/api/Iads/nn-iads-iads"><strong>IADs</strong></a></dt><dt><a href="/windows/desktop/api/Iads/nn-iads-iadsuser"><strong>IADsUser</strong></a></dt><dt><a href="/windows/desktop/api/Iads/nn-iads-iadspropertylist"><strong>IADsPropertyList</strong></a></dt></dl> | 
| <strong>UserGroupCollection</strong> | An ADSI object that represents a collection of user groups. | <a href="/windows/desktop/api/Iads/nn-iads-iadsmembers"><strong>IADsMembers</strong></a> | 




 

 

 





