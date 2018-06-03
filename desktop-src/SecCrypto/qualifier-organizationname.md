---
Description: Retrieves the name of the organization associated with the qualifier.
ms.assetid: 4ceb2c0f-903d-4fcd-8446-abf3175fe8e0
title: Qualifier.OrganizationName property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Qualifier.OrganizationName property

\[The **OrganizationName** property is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509Extension Class**](https://www.bing.com/search?q=**X509Extension Class**) in the [**System.Security.Cryptography.X509Certificates**](https://www.bing.com/search?q=**System.Security.Cryptography.X509Certificates**) namespace by calling the constructor that takes an OID as a parameter, and then use the OID for Certificate Policies to process qualifiers that are part of the policy information in the Certificate Policies extension.\]

The **OrganizationName** property retrieves the name of the organization associated with the qualifier. This property may be empty.

## Syntax


```VB
Qualifier.OrganizationName As String
```



## Property value

The name of the organization associated with the qualifier.

## Requirements



|                            |                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**Qualifier**](qualifier.md)
</dt> </dl>

 

 




