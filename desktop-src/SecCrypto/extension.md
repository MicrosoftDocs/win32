---
Description: Represents a single certificate extension.
ms.assetid: 489c58b6-a704-4f54-bc64-34eacafc347c
title: Extension object
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# Extension object

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**X509Extension Class**](https://www.bing.com/search?q=**X509Extension Class**) in the [**System.Security.Cryptography.X509Certificates**](https://www.bing.com/search?q=**System.Security.Cryptography.X509Certificates**) namespace.\]

The **Extension** object represents a single certificate extension.

## When to use

The **Extension** object is used to perform the following tasks:

-   Retrieve the OID of the certificate extension.
-   Retrieve the certificate extension data represented by an [**EncodedData**](encodeddata.md) object.
-   Determine whether the certificate extension is marked as critical.

## Members

The **Extension** object has these types of members:

-   [Properties](#properties)

### Properties

The **Extension** object has these properties.



| Property                                                | Access type          | Description                                                                                   |
|:--------------------------------------------------------|:---------------------|:----------------------------------------------------------------------------------------------|
| [**EncodedData**](extension-encodeddata.md)<br/> | Read-only<br/> | Retrieves the encoded data for the extension.<br/>                                      |
| [**IsCritical**](extension-iscritical.md)<br/>   | Read-only<br/> | Retrieves a Boolean value that indicates whether the extension is marked critical.<br/> |
| [**OID**](extension-oid.md)<br/>                 | Read-only<br/> | Retrieves the object identifier for the extension. This is the default property.<br/>   |



 

## Remarks

The **Extension** object cannot be created.

The **Extension** object is used by the [**Extensions**](extensions.md) collection object.

## Requirements



|                                  |                                                                                        |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| Header<br/>                | <dl> <dt>Mmcobj.h</dt> </dl>    |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



 

 




