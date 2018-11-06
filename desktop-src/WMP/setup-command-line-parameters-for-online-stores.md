---
title: Setup Command-line Parameters for Online Stores
description: Setup Command-line Parameters for Online Stores
ms.assetid: 26224d7c-ca12-43b9-9150-3d39bccb85d3
keywords:
- Windows Media Player online stores,setup command-line parameters
- online stores,setup command-line parameters
- type 1 online stores,setup command-line parameters
- type 2 online stores,setup command-line parameters
- setup command-line parameters
- Windows Media Player online stores,command-line parameters
- online stores,command-line parameters
- type 1 online stores,command-line parameters
- type 2 online stores,command-line parameters
- command-line parameters
- Windows Media Player online stores,parameters
- online stores,parameters
- type 1 online stores,parameters
- type 2 online stores,parameters
ms.topic: article
ms.date: 05/31/2018
---

# Setup Command-line Parameters for Online Stores

> [!Note]  
> This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

When installing Windows Media Player 10 or Windows Media Player 11 on Windows XP, you can append command-line parameters to specify the first online store that the user sees.

Syntax


```C++
MP10Setup.exe /q:A /c:"setup_wm.exe /Q /R:N /DefaultService:serviceKey /ServiceInfo:documentPath /ServiceExtra:queryString"
```



Parameters

DefaultService (required)

The key name for the online store. This value must match the key name in the **Key** attribute of the **ServiceInfo** element of the ServiceInfo document.

ServiceInfo (required)

The fully qualified path to a ServiceInfo document installed on the user's computer.

ServiceExtra (optional)

A query string that Windows Media Player 10 will append to the URL for the ServiceInfo document when it retrieves the document online.

## Remarks

For details about redistributing Windows Media Player software with your application, see [Redistributing Windows Media Player Software](redistributing-windows-media-player-software.md).

When the user's computer is not connected to the Internet, the information contained in the local ServiceInfo document is used to configure Windows Media Player for the initial active service.

Command-line parameters are case sensitive.

## Related topics

<dl> <dt>

[**Co-Branding Online Stores**](co-branding-online-stores.md)
</dt> <dt>

[**Information Common to Type 1 and Type 2 Online Stores**](information-common-to-type-1-and-type-2-online-stores.md)
</dt> <dt>

[**Install Element**](install-element.md)
</dt> <dt>

[**Setting the Initial Online Store**](setting-the-initial-online-store.md)
</dt> </dl>

 

 




