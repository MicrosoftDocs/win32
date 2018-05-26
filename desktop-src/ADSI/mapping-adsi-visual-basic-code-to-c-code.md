---
title: Mapping ADSI Visual Basic Code to C++ Code
description: ADSI consists of more than 50 interfaces.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 6316f504-265e-44d4-ba24-e6289065981b
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Mapping ADSI Visual Basic Code to C++ Code

ADSI consists of more than 50 interfaces. Most directory operations can be completed using only five interfaces. They are:

-   [**IADsOpenDSObject**](/windows/win32/Iads/nn-iads-iadsopendsobject?branch=master)
-   [**IADs**](/windows/win32/Iads/nn-iads-iads?branch=master)
-   [**IADsContainer**](/windows/win32/Iads/nn-iads-iadscontainer?branch=master)
-   [**IDirectoryObject**](/windows/win32/Iads/nn-iads-idirectoryobject?branch=master)
-   [**IDirectorySearch**](/windows/win32/Iads/nn-iads-idirectorysearch?branch=master)

The following table lists mappings from ADSI VB/VBS code to C++ code. Be aware that this is not a complete list.



| VBS Code                           | VC Code                                                               |
|------------------------------------|-----------------------------------------------------------------------|
| Set obj = GetObject()              | hr = AdsGetObject()                                                   |
| obj.Put obj.Get obj.Parent         | IADs or IDirectoryObject                                              |
| obj.Create obj.Delete obj.MoveHere | IADsContainer                                                         |
| For each… in…                      | AdsBuildEnumerator() ADsEnumerateNext()                               |
| Connection, Command, RecordSet     | IDirectorySearch                                                      |
| Security descriptor, ACL, ACE      | IADsSecurityDescriptor, IADsAccessControlList, IADsAccessControlEntry |



 

 

 




