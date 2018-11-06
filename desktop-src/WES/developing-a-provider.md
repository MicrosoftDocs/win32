---
title: Developing a Provider
description: To write the events that you define in your manifest, you use the functions included in the Event Tracing (ETW) API. For details on writing a provider, see Providing Events.
ms.assetid: 23de19c4-5f8d-4faa-acd9-fe6208ca17a9
ms.topic: article
ms.date: 05/31/2018
---

# Developing a Provider

To write the events that you define in your manifest, you use the functions included in the [Event Tracing](https://msdn.microsoft.com/library/windows/desktop/bb968803) (ETW) API. For details on writing a provider, see [Providing Events](https://msdn.microsoft.com/library/windows/desktop/aa364098).

After writing the provider, use the WevtUtil.exe tool to register the provider and schema. For details on using WevtUtil, see [Windows Event Log Tools](windows-event-log-tools.md). The following shows how to use WevtUtil to register a provider and to remove the registration.


```cmd
wevtutil im provider.man

wevtutil um provider.man
```



 

 




