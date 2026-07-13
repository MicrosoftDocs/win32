---
title: Authentication (ADSI)
description: In ADSI, credentials that consist of a user name and password are used to provide or restrict access to objects in the directory service.
ms.assetid: eef6451d-ebb8-4e22-84f4-61b8be73068a
ms.tgt_platform: multiple
keywords:
- Authentication ADSI
- ADSI, Using, Authentication
ms.topic: concept-article
ms.date: 08/20/2024
---

# Authentication (ADSI)

In ADSI, credentials that consist of a user name and password are used to provide or restrict access to objects in the directory service. The [ADsGetObject](/windows/win32/api/Adshlp/nf-adshlp-adsgetobject) function uses the credentials of the calling thread for authentication. The [ADsOpenObject](/windows/win32/api/Adshlp/nf-adshlp-adsopenobject) function and [IADsOpenDSObject::OpenDSObject](/windows/win32/api/Iads/nf-iads-iadsopendsobject-opendsobject) method can be used to specify credentials other than those of the calling thread. When an object is bound to with an authenticated user, the user is allowed access to the object as supported by the underlying directory service security requirements.

> [!NOTE]
> The [ADsOpenObject](/windows/win32/api/Adshlp/nf-adshlp-adsopenobject) function and [IADsOpenDSObject::OpenDSObject](/windows/win32/api/Iads/nf-iads-iadsopendsobject-opendsobject) method should not be used to validate user credentials.

> [!IMPORTANT]
> Microsoft does not recommend the username and password flow because the application will be asking a user for their password directly, which is an insecure pattern. In most scenarios, there exist more secure flows that you can use.

The following code example shows how to use the [OpenDSObject](/windows/win32/api/Iads/nf-iads-iadsopendsobject-opendsobject) method to authenticate a user.

```VB
Dim MyNamespace As IADsOpenDSObject
Dim X
oUsername=GetUsernameFromSecureConfig() ' Get the username from a secure location (not shown)
oPassword=GetPasswordFromSecureConfig() ' Get the password from a secure location (not shown)

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
