---
title: ADSI Objects of WinNT
description: The ADSI WinNT provider implement the following COM objects to support features and services of various ADSI interfaces.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 'ce6f8638-aa9e-4036-b597-077da4c3c534'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
keywords: ["WinNT service provider ADSI ,ADSI objects"]
---

# ADSI Objects of WinNT

The ADSI WinNT provider implement the following COM objects to support features and services of various ADSI interfaces.



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>ADSI Object</th>
<th>Description</th>
<th>Supported Interfaces</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Class</strong></td>
<td>An ADSI object that represents a class definition.</td>
<td><dl> <dt>[<strong>IADs</strong>](iads.md)</dt> <dt>[<strong>IADsClass</strong>](iadsclass.md)</dt> </dl></td>
</tr>
<tr class="even">
<td><strong>Computer</strong></td>
<td>An ADSI object that represents a computer.</td>
<td><dl> <dt>[<strong>IADs</strong>](iads.md)</dt> <dt>[<strong>IADsComputer</strong>](iadscomputer.md)</dt> <dt>[<strong>IADsComputerOperations</strong>](iadscomputeroperations.md)</dt> <dt>[<strong>IADsContainer</strong>](iadscontainer.md)</dt> <dt>[<strong>IADsPropertyList</strong>](iadspropertylist.md)</dt> </dl></td>
</tr>
<tr class="odd">
<td><strong>Domain</strong></td>
<td>An ADSI object that represents a domain over the network.</td>
<td><dl> <dt>[<strong>IADs</strong>](iads.md)</dt> <dt>[<strong>IADsDomain</strong>](iadsdomain.md)</dt> <dt>[<strong>IADsContainer</strong>](iadscontainer.md)</dt> <dt>[<strong>IADsPropertyList</strong>](iadspropertylist.md)</dt> </dl></td>
</tr>
<tr class="even">
<td><strong>FileService</strong></td>
<td>An ADSI object that represents a file service.</td>
<td><dl> <dt>[<strong>IADs</strong>](iads.md)</dt> <dt>[<strong>IADsFileService</strong>](iadsfileservice.md)</dt> <dt>[<strong>IADsFileServiceOperations</strong>](iadsfileserviceoperations.md)</dt> <dt>[<strong>IADsContainer</strong>](iadscontainer.md)</dt> <dt>[<strong>IADsPropertyList</strong>](iadspropertylist.md)</dt> </dl></td>
</tr>
<tr class="odd">
<td><strong>FileShare</strong></td>
<td>An ADSI object that represents a file share.</td>
<td><dl> <dt>[<strong>IADs</strong>](iads.md)</dt> <dt>[<strong>IADsFileShare</strong>](iadsfileshare.md)</dt> <dt>[<strong>IADsPropertyList</strong>](iadspropertylist.md)</dt> </dl></td>
</tr>
<tr class="even">
<td><strong>FPNWFileService</strong></td>
<td>An ADSI object that represents a file service.</td>
<td><dl> <dt>[<strong>IADs</strong>](iads.md)</dt> <dt>[<strong>IADsFileService</strong>](iadsfileservice.md)</dt> <dt>[<strong>IADsFileServiceOperations</strong>](iadsfileserviceoperations.md)</dt> <dt>[<strong>IADsContainer</strong>](iadscontainer.md)</dt> </dl></td>
</tr>
<tr class="odd">
<td><strong>FPNWFileShare</strong></td>
<td>An ADSI object that represents a file share.</td>
<td><dl> <dt>[<strong>IADs</strong>](iads.md)</dt> <dt>[<strong>IADsFileShare</strong>](iadsfileshare.md)</dt> <dt>[<strong>IADsPropertyList</strong>](iadspropertylist.md)</dt> </dl></td>
</tr>
<tr class="even">
<td><strong>FPNWResource</strong></td>
<td>An ADSI object that represents a resource.</td>
<td><dl> <dt>[<strong>IADs</strong>](iads.md)</dt> <dt>[<strong>IADsResource</strong>](iadsresource.md)</dt> <dt>[<strong>IADsPropertyList</strong>](iadspropertylist.md)</dt> </dl></td>
</tr>
<tr class="odd">
<td><strong>FPNWResourcesCollection</strong></td>
<td>An ADSI object that represents a collection of resources.</td>
<td>[<strong>IADsCollection</strong>](iadscollection.md)</td>
</tr>
<tr class="even">
<td><strong>FPNWSession</strong></td>
<td>An ADSI object that represents a session.</td>
<td><dl> <dt>[<strong>IADs</strong>](iads.md)</dt> <dt>[<strong>IADsSession</strong>](iadssession.md)</dt> <dt>[<strong>IADsPropertyList</strong>](iadspropertylist.md)</dt> </dl></td>
</tr>
<tr class="odd">
<td><strong>FPNWSessionsCollection</strong></td>
<td>An ADSI object that represents a collection of sessions.</td>
<td>[<strong>IADsCollection</strong>](iadscollection.md)</td>
</tr>
<tr class="even">
<td><strong>Group</strong></td>
<td>An ADSI object that represents a group.</td>
<td><dl> <dt>[<strong>IADs</strong>](iads.md)</dt> <dt>[<strong>IADsGroup</strong>](iadsgroup.md)</dt> <dt>[<strong>IADsPropertyList</strong>](iadspropertylist.md)</dt> </dl>
<blockquote>
[!Note]<br />
GetInfo cannot be used for groups that contain members that are wellKnown security principals in the WinNT scope.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td><strong>GroupCollection</strong></td>
<td>An ADSI object that represents a collection of groups.</td>
<td><dl> <dt>[<strong>IADs</strong>](iads.md)</dt> <dt>[<strong>IADsMembers</strong>](iadsmembers.md)</dt> </dl></td>
</tr>
<tr class="even">
<td><strong>LocalGroup</strong></td>
<td>An ADSI object that represents a local group.</td>
<td><dl> <dt>[<strong>IADs</strong>](iads.md)</dt> <dt>[<strong>IADsGroup</strong>](iadsgroup.md)</dt> <dt>[<strong>IADsPropertyList</strong>](iadspropertylist.md)</dt> </dl></td>
</tr>
<tr class="odd">
<td><strong>LocalgroupCollection</strong></td>
<td>An ADSI object that represents a collection of local groups.</td>
<td><dl> <dt>[<strong>IADs</strong>](iads.md)</dt> <dt>[<strong>IADsMembers</strong>](iadsmembers.md)</dt> </dl></td>
</tr>
<tr class="even">
<td><strong>Namespace</strong></td>
<td>An ADSI object that represents the WinNT namespace.</td>
<td><dl> <dt>[<strong>IADs</strong>](iads.md)</dt> <dt>[<strong>IADsContainer</strong>](iadscontainer.md)</dt> <dt>[<strong>IADsOpenDSObject</strong>](iadsopendsobject.md)</dt> </dl></td>
</tr>
<tr class="odd">
<td><strong>PrintJob</strong></td>
<td>An ADSI object that represents a print job.</td>
<td><dl> <dt>[<strong>IADs</strong>](iads.md)</dt> <dt>[<strong>IADsPrintJob</strong>](iadsprintjob.md)</dt> <dt>[<strong>IADsPrintJobOperations</strong>](iadsprintjoboperations.md)</dt> <dt>[<strong>IADsPropertyList</strong>](iadspropertylist.md)</dt> </dl></td>
</tr>
<tr class="even">
<td><strong>PrintJobsCollection</strong></td>
<td>An ADSI object that represents a collection of print jobs.</td>
<td>[<strong>IADsCollection</strong>](iadscollection.md)</td>
</tr>
<tr class="odd">
<td><strong>PrintQueue</strong></td>
<td>An ADSI object that represents a print queue.</td>
<td><dl> <dt>[<strong>IADs</strong>](iads.md)</dt> <dt>[<strong>IADsPrintQueue</strong>](iadsprintqueue.md)</dt> <dt>[<strong>IADsPrintQueueOperations</strong>](iadsprintqueueoperations.md)</dt> <dt>[<strong>IADsPropertyList</strong>](iadspropertylist.md)</dt> </dl></td>
</tr>
<tr class="even">
<td><strong>Property</strong></td>
<td>An ADSI object that represents an attribute definition.</td>
<td><dl> <dt>[<strong>IADs</strong>](iads.md)</dt> <dt>[<strong>IADsProperty</strong>](iadsproperty.md)</dt> </dl></td>
</tr>
<tr class="odd">
<td><strong>Resource</strong></td>
<td>An ADSI object that represents a resource.</td>
<td><dl> <dt>[<strong>IADs</strong>](iads.md)</dt> <dt>[<strong>IADsResource</strong>](iadsresource.md)</dt> <dt>[<strong>IADsPropertyList</strong>](iadspropertylist.md)</dt> </dl></td>
</tr>
<tr class="even">
<td><strong>ResourcesCollection</strong></td>
<td>An ADSI object that represents a collection of resources.</td>
<td>[<strong>IADsCollection</strong>](iadscollection.md)</td>
</tr>
<tr class="odd">
<td><strong>Schema</strong></td>
<td>An ADSI object that represents the schema container.</td>
<td><dl> <dt>[<strong>IADs</strong>](iads.md)</dt> <dt>[<strong>IADsContainer</strong>](iadscontainer.md)</dt> </dl></td>
</tr>
<tr class="even">
<td><strong>Service</strong></td>
<td>An ADSI object that represents a service.</td>
<td><dl> <dt>[<strong>IADs</strong>](iads.md)</dt> <dt>[<strong>IADsService</strong>](iadsservice.md)</dt> <dt>[<strong>IADsServiceOperations</strong>](iadsserviceoperations.md)</dt> <dt>[<strong>IADsPropertyList</strong>](iadspropertylist.md)</dt> </dl></td>
</tr>
<tr class="odd">
<td><strong>Session</strong></td>
<td>An ADSI object that represents a session.</td>
<td><dl> <dt>[<strong>IADs</strong>](iads.md)</dt> <dt>[<strong>IADsSession</strong>](iadssession.md)</dt> <dt>[<strong>IADsPropertyList</strong>](iadspropertylist.md)</dt> </dl></td>
</tr>
<tr class="even">
<td><strong>SessionsCollection</strong></td>
<td>An ADSI object that represents a collection of sessions.</td>
<td>[<strong>IADsCollection</strong>](iadscollection.md)</td>
</tr>
<tr class="odd">
<td><strong>Syntax</strong></td>
<td>An ADSI object that represents the syntax of an attribute.</td>
<td><dl> <dt>[<strong>IADs</strong>](iads.md)</dt> <dt>[<strong>IADsSyntax</strong>](iadssyntax.md)</dt> </dl></td>
</tr>
<tr class="even">
<td><strong>User</strong></td>
<td>An ADSI object that represents a user account.</td>
<td><dl> <dt>[<strong>IADs</strong>](iads.md)</dt> <dt>[<strong>IADsUser</strong>](iadsuser.md)</dt> <dt>[<strong>IADsPropertyList</strong>](iadspropertylist.md)</dt> </dl></td>
</tr>
<tr class="odd">
<td><strong>UserGroupCollection</strong></td>
<td>An ADSI object that represents a collection of user groups.</td>
<td>[<strong>IADsMembers</strong>](iadsmembers.md)</td>
</tr>
</tbody>
</table>



 

 

 





