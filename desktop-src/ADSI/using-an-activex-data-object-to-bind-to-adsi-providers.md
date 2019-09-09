---
title: Using an ActiveX Data Object to Bind to ADSI Providers
description: Since ADSI is also an OLE DB provider, you can use an ActiveX Data Object (ADO) to connect to ADSI providers.
ms.assetid: b42d804b-f1eb-4085-88aa-015a92309ee8
ms.tgt_platform: multiple
keywords:
- ActiveX data object ADSI
- ActiveX data object ADSI ,using ADO to bind to ADSI providers
- service providers ADSI ,using ActiveX data object to bind to
ms.topic: article
ms.date: 05/31/2018
---

# Using an ActiveX Data Object to Bind to ADSI Providers

Since ADSI is also an OLE DB provider, you can use an ActiveX Data Object (ADO) to connect to ADSI providers. As with other ADO providers, to connect to an OLE DB provider, you must create a new connection object and, optionally, specify the credentials. The name of the ADSI OLE DB provider is **ADsDSOObject**.

For example:


```VB
Dim con As New Connection 
'VBScript use: con = CreateObject("ADODB.Connection")
con.Provider = "ADsDSOObject"
con.Open "YourDescriptionHere"
```



In the previous example, you are connected on behalf of the current user. To specify different credentials, use connection properties:


```VB
con.Provider = "ADsDSOObject"
con.Properties("User ID") = "jeffsmith"
con.Properties("Password") = "guesswhat?"
con.Properties("Encrypt Password") = True
con.Open "YourDescriptionHere"
```



ADSI OLE DB defines the following connection properties.



| Property           | Data type   | Default   |
|--------------------|-------------|-----------|
| "User ID"          | **BSTR**    | **NULL**  |
| "Password"         | **BSTR**    | **NULL**  |
| "Encrypt Password" | **BOOLEAN** | **FALSE** |
| "ADSI Flag"        | **Long**    | 0         |



 

Using OLE DB ADO, you cannot bind to a specific object. You can, however, query a specific object and get a result set back. Only ADSI providers that support [**IDirectorySearch**](/windows/desktop/api/Iads/nn-iads-idirectorysearch) benefit from having ADO as a programming model.

The ADSI Flag property is used to specify the binding authentication option. This property can be a combination of flags from the [**ADS\_AUTHENTICATION\_ENUM**](/windows/win32/api/iads/ne-iads-ads_authentication_enum) enumeration.

 

 




