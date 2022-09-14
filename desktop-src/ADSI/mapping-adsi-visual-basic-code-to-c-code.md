---
title: Mapping ADSI Visual Basic Code to C++ Code
description: ADSI consists of more than 50 interfaces.
ms.assetid: 6316f504-265e-44d4-ba24-e6289065981b
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Mapping ADSI Visual Basic Code to C++ Code

ADSI consists of more than 50 interfaces. Most directory operations can be completed using only five interfaces. They are:

-   [**IADsOpenDSObject**](/windows/desktop/api/Iads/nn-iads-iadsopendsobject)
-   [**IADs**](/windows/desktop/api/Iads/nn-iads-iads)
-   [**IADsContainer**](/windows/desktop/api/Iads/nn-iads-iadscontainer)
-   [**IDirectoryObject**](/windows/desktop/api/Iads/nn-iads-idirectoryobject)
-   [**IDirectorySearch**](/windows/desktop/api/Iads/nn-iads-idirectorysearch)

The following table lists mappings from ADSI VB/VBS code to C++ code. Be aware that this is not a complete list.



| VBS Code                           | VC Code                                                               |
|------------------------------------|-----------------------------------------------------------------------|
| Set obj = GetObject()              | hr = AdsGetObject()                                                   |
| obj.Put obj.Get obj.Parent         | IADs or IDirectoryObject                                              |
| obj.Create obj.Delete obj.MoveHere | IADsContainer                                                         |
| For each… in…                      | AdsBuildEnumerator() ADsEnumerateNext()                               |
| Connection, Command, RecordSet     | IDirectorySearch                                                      |
| Security descriptor, ACL, ACE      | IADsSecurityDescriptor, IADsAccessControlList, IADsAccessControlEntry |



 

 

 




