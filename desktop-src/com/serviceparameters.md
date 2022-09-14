---
title: ServiceParameters
description: Specifies the command-line parameters to be passed to an object installed for use by COM through the LocalService registry value.
ms.assetid: da11e422-c0f2-4e44-9728-740ea6b61421
keywords:
- ServiceParameters registry value COM
ms.topic: article
ms.date: 05/31/2018
---

# ServiceParameters

Specifies the command-line parameters to be passed to an object installed for use by COM through the [**LocalService**](localservice.md) registry value.

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Classes\AppID
   {AppID_GUID}
      ServiceParameters = parameter
```

## Remarks

This is a **REG\_SZ** value. This string is passed to the service as a command-line argument as it is being launched.

## Related topics

<dl> <dt>

[**LocalService**](localservice.md)
</dt> <dt>

[Registering COM Servers](registering-com-servers.md)
</dt> </dl>

 

 




