---
title: ADSI Extended Error Messages
description: This topic contains a list of topics that explain how to work with ADSI error messages that are returned by IADs, IADsContainer, IDirectoryObject, and IDirectorySearch.
ms.assetid: cfec86cb-fe90-4e2b-8c9d-06e175253fa4
ms.tgt_platform: multiple
keywords:
- ADSI Extended Error Messages
ms.topic: article
ms.date: 05/31/2018
---

# ADSI Extended Error Messages

Apart from the **HRESULT** values, several ADSI system providers (mostly LDAP) return additional error data for operations performed by the following interfaces:

-   [**IADs**](/windows/desktop/api/Iads/nn-iads-iads)
-   [**IADsContainer**](/windows/desktop/api/Iads/nn-iads-iadscontainer)
-   [**IDirectoryObject**](/windows/desktop/api/Iads/nn-iads-idirectoryobject)
-   [**IDirectorySearch**](/windows/desktop/api/Iads/nn-iads-idirectorysearch)

A part of such extended error data is the string sent by the server as a part of the message result.

Call [**ADsGetLastError**](/windows/desktop/api/Adshlp/nf-adshlp-adsgetlasterror) to retrieve such extended error messages. The first parameter of this function, *lpError*, is a **DWORD** value. For an Active Directory server, ADSI attempts to map an LDAP error message to an appropriate Win32 error code and assigns the Win32 error code value to *lpError*. Failing to resolve the mapping, ADSI assigns **ERROR\_INVALID\_DATA** to *lpError*, as it does for any other directory server. In all cases, ADSI faithfully relays the string of the error description from the server to the client through *lpErrorBuf*, the second parameter of the **ADsGetLastError** function.

 

 




