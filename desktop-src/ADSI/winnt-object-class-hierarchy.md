---
title: WinNT Object Class Hierarchy
description: The WinNT object class hierarchy starts from the Namespace object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '01dfdfec-cfdf-43ee-bf2f-c05a741bfb22'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
keywords: ["WinNT service provider ADSI ,object class hierarchy"]
---

# WinNT Object Class Hierarchy

The WinNT object class hierarchy starts from the Namespace object.



| Object class                   | Description                                                                       |
|--------------------------------|-----------------------------------------------------------------------------------|
| Namespace<br/>           | Top-level object container.<br/>                                            |
| Domain<br/>              | The Windows NT domain.<br/>                                                 |
| User<br/>                | User account.<br/>                                                          |
| Group<br/>               | Group account for managing access rights.<br/>                              |
| UserGroupCollection<br/> | A set of user groups implementing [**IADsMembers**](iadsmembers.md).<br/>  |
| GroupCollection<br/>     | A set of other groups implementing [**IADsMembers**](iadsmembers.md).<br/> |
| Computer<br/>            | Windows NT 4.0 server or workstation.<br/>                                  |
| PrintJob<br/>            | Print job in the print queue.<br/>                                          |
| PrintJobsCollection<br/> | A set of print jobs.<br/>                                                   |
| PrintQueue<br/>          | Print queue on a printer spooler.<br/>                                      |
| Service<br/>             | Application running as a service.<br/>                                      |
| FileService<br/>         | Services accessing file system.<br/>                                        |
| FileShare<br/>           | File share point.<br/>                                                      |
| Resource<br/>            | A resource in the service.<br/>                                             |
| Session<br/>             | An active file service connection.<br/>                                     |
| User<br/>                | Local user account.<br/>                                                    |
| Group<br/>               | Local group.<br/>                                                           |
| UserCollection<br/>      | Collection of local users.<br/>                                             |
| GroupCollection<br/>     | Collection of local groups.<br/>                                            |
| Schema<br/>              | WinNT Schema container.<br/>                                                |
| Class<br/>               | Schema class definition.<br/>                                               |
| Property<br/>            | Schema attribute definition.<br/>                                           |
| Syntax<br/>              | Syntax of a property.<br/>                                                  |



 

 

 





