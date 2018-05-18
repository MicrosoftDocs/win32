---
title: MultiPoint Services
description: MultiPoint Services provides interfaces for software developers on Windows Server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'f0d4261d-1e1e-4082-bae1-3372e9cbe5f8'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
---

# MultiPoint Services

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

> [!Note]  
> MultiPoint Server 2012 was the last version of MultiPoint Server to be available as a product. In Windows Server 2016, the features from MultiPoint Server were added as a server role called MultiPoint Services .

 

MultiPoint Services is a server role in Windows Server 2016 that allows multiple users to simultaneously use the same computer from separate computing stations. Each user connects to the host computer using a MultiPoint station that consists of a hub, monitor, and input devices; such as a mouse and keyboard. This gives them the full experience of a Windows OS, without the need to purchase and maintain separate workstations.

MultiPoint Services provides interfaces for software developers on Windows Server. Developers can use the MultiPoint Services interfaces to handle the display of screen data from third party input devices that are connected to a MultiPoint station. These topics describe the MultiPoint Services interfaces.

## Runtime Requirements

MultiPoint Services requires Windows Server 2016 or later. For information about the run-time requirements for a particular programming element, see the Requirements section of the reference topic for that element.

To register a custom presenter, add a **REG\_DWORD** value to this registry key:

```
HKLM
   Software
      Microsoft
         Windows MultiPoint Server
            Plugins
               CustomPresenter
```

The name of the value must be a ProgID for a class that implements the [**IWmsCustomPresenterPlugin**](iwmscustompresenterplugin.md) interface.

## In this section

<dl> <dt>

[MultiPoint Services Reference](multipoint-reference.md)
</dt> <dd>

These topics contain reference content for the programming elements provided by MultiPoint Services.

</dd> </dl>

## Related topics

<dl> <dt>

[Windows MultiPoint Server 2012](https://technet.microsoft.com/library/jj916259.aspx)
</dt> </dl>

 

 




