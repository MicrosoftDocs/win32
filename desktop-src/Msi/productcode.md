---
Description: The ProductCode property is a unique identifier for the particular product release, represented as a string GUID, for example &\#0034;{12345678-1234-1234-1234-123456789012}&\#0034;.
ms.assetid: 14538e8b-3a7f-4d73-8c54-a0f83b013a42
title: ProductCode property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ProductCode property

The **ProductCode** property is a unique identifier for the particular product release, represented as a string [GUID](guid.md), for example "{12345678-1234-1234-1234-123456789012}". Letters used in this GUID must be uppercase. This ID must vary for different versions and languages.

A product upgrade that updates a product into an entirely new product must also change the product code. The 32-bit and 64-bit versions of an application's package must be assigned different product codes.

The **ProductCode** is advertised as a product property, and is the primary method of specifying the product. This property is REQUIRED.

## Requirements



|                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 




