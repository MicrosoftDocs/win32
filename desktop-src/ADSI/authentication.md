---
title: Authentication (ADSI)
description: In ADSI, credentials that consist of a user name and password are used to provide or restrict access to objects in the directory service.
ms.assetid: eef6451d-ebb8-4e22-84f4-61b8be73068a
ms.tgt_platform: multiple
keywords:
- Authentication ADSI
- ADSI, Using, Authentication
ms.topic: article
ms.date: 05/31/2018
---

# Authentication (ADSI)

In ADSI, credentials that consist of a user name and password are used to provide or restrict access to objects in the directory service. The [**ADsGetObject**](/windows/desktop/api/Adshlp/nf-adshlp-adsgetobject) function uses the credentials of the calling thread for authentication. The [**ADsOpenObject**](/windows/desktop/api/Adshlp/nf-adshlp-adsopenobject) function and [**IADsOpenDSObject::OpenDSObject**](/windows/desktop/api/Iads/nf-iads-iadsopendsobject-opendsobject) method can be used to specify credentials other than those of the calling thread. When an object is bound to with an authenticated user, the user is allowed access to the object as supported by the underlying directory service security requirements.

> [!Note]  
> The [**ADsOpenObject**](/windows/desktop/api/Adshlp/nf-adshlp-adsopenobject) function and [**IADsOpenDSObject::OpenDSObject**](/windows/desktop/api/Iads/nf-iads-iadsopendsobject-opendsobject) method should not be used to validate user credentials.

 

The following code example shows how to use the [**OpenDSObject**](/windows/desktop/api/Iads/nf-iads-iadsopendsobject-opendsobject) method to authenticate a user.


```VB
Dim MyNamespace As IADsOpenDSObject
Dim X
oUsername="MyUserName"
oPassword="MyPassword"

OnError GoTo CleanuUp
 
Set MyNamespace = GetObject("LDAP:")

' For authentication, pass a variable for the user name and password to be used for 
' authentication. For security reasons, it is recommended that you use the ADS_SECURE_AUTHENTICATION flag.
' 
Set X = MyNamespace.OpenDSObject(DN, oUserName, oPassword, ADS_SECURE_AUTHENTICATION)     

CleanUp:
    MsgBox ("An error has occurred.")
    Set MyNamespace = Nothing
    Set X = Nothing
```



 

 




