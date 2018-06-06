---
Description: Provides read-only access to the extended key usage (EKU) properties of a certificate.
ms.assetid: e974e9e2-1011-48b7-9ebc-e754e4990286
title: ExtendedKeyUsage object
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# ExtendedKeyUsage object

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**X509EnhancedKeyUsageExtension Class**](https://www.bing.com/search?q=**X509EnhancedKeyUsageExtension+Class**) in the [**System.Security.Cryptography.X509Certificates**](https://www.bing.com/search?q=**System.Security.Cryptography.X509Certificates**) namespace.\]

The **ExtendedKeyUsage** object provides read-only access to the extended key usage (EKU) properties of a certificate.

## Members

The **ExtendedKeyUsage** object has these types of members:

-   [Properties](#properties)

### Properties

The **ExtendedKeyUsage** object has these properties.



| Property                                                     | Access type          | Description                                                                                                                             |
|:-------------------------------------------------------------|:---------------------|:----------------------------------------------------------------------------------------------------------------------------------------|
| [**EKUs**](extendedkeyusage-ekus.md)<br/>             | Read-only<br/> | [**EKUs**](ekus.md) collection that contains the [**EKU**](eku.md) objects for the certificate.<br/>                            |
| [**IsCritical**](extendedkeyusage-iscritical.md)<br/> | Read-only<br/> | Retrieves a **Boolean** value that indicates whether the EKU extension is marked critical.<br/>                                   |
| [**IsPresent**](extendedkeyusage-ispresent.md)<br/>   | Read-only<br/> | Retrieves a **Boolean** value that indicates whether the EKU extension is present.<br/> This is the default property. <br/> |



 

## Remarks

The **ExtendedKeyUsage** object cannot be created.

## Requirements



|                                  |                                                                                        |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**Cryptography Objects**](cryptography-objects.md)
</dt> </dl>

 

 




