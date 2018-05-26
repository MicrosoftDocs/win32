---
title: How-to set the API security mode
description: You can choose which security mode your File API application runs in by using the IpcSetGlobalProperty function.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 3B088F14-81C5-4C78-8DED-F5F153353EE0
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# How-to: set the API security mode

You can choose which security mode your File API application runs in by using the [**IpcSetGlobalProperty**](ipcsetglobalproperty.md) function.

To initialize your application to run in *server mode*, call the [**IpcSetGlobalProperty**](ipcsetglobalproperty.md) function and set the security mode to [**IPC\_API\_MODE\_SERVER**](api-mode-values.md). By default, your application will run in *client mode*, **IPC\_API\_MODE\_CLIENT**.

For more information on *server mode*, see [Application types](application-types.md).

> \[!Important\]  
> The security mode should be set before any other Rights Management Services SDK 2.1 function is called. After the security mode has been set, it cannot be changed for the current process.

 

## Related topics

<dl> <dt>

[Application types](application-types.md)
</dt> <dt>

[Developer concepts](https://msdn.microsoft.com/library/windows/desktop/jj127291)
</dt> <dt>

[**API mode values**](api-mode-values.md)
</dt> <dt>

[**IpcSetGlobalProperty**](ipcsetglobalproperty.md)
</dt> </dl>

 

 




