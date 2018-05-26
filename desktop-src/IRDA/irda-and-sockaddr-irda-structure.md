---
title: IrDA and SOCKADDR\_IRDA Structure
description: The SOCKADDR\_IRDA structure is used for IrDA sockets. For convenience, the structure definition is presented here (if discrepancies exist, the reference in Windows Sockets is definitive).
ms.assetid: eb452166-baa4-46f8-88f2-a250119c38a4
keywords:
- IrDA and SOCKADDR_IRDA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IrDA and SOCKADDR\_IRDA Structure

The **SOCKADDR\_IRDA** structure is used for IrDA sockets. For convenience, the structure definition is presented here (if discrepancies exist, the reference in Windows Sockets is definitive).

``` syntax
#include <windows.h>

typedef struct _SOCKADDR_IRDA
{
  u_short    irdaAddressFamily;
  u_char     irdaDeviceID[4];
  char       irdaServiceName[25];
} SOCKADDR_IRDA, *PSOCKADDR_IRDA, FAR *LPSOCKADDR_IRDA;
```

<dl> <dt>

<span id="irdaAddressFamily"></span><span id="irdaaddressfamily"></span><span id="IRDAADDRESSFAMILY"></span>**irdaAddressFamily**
</dt> <dd>

For IrDA applications, the **irdaAddressFamily** member is always AF\_IRDA.

</dd> <dt>

<span id="irdaDeviceID"></span><span id="irdadeviceid"></span><span id="IRDADEVICEID"></span>**irdaDeviceID**
</dt> <dd>

Client applications fill in all fields. The **irdaDeviceID** member is the device address of the device that the client connects to using the Windows Sockets [**connect**](https://msdn.microsoft.com/library/windows/desktop/ms737625) function; the device address is returned from a previous discovery operation initiated by a Windows Sockets [**getsockopt**](https://msdn.microsoft.com/library/windows/desktop/ms738544) function call with the IRLMP\_ENUMDEVICES option. The **irdaDeviceID** member is ignored by the server application.

</dd> <dt>

<span id="irdaServiceName"></span><span id="irdaservicename"></span><span id="IRDASERVICENAME"></span>**irdaServiceName**
</dt> <dd>

Server applications use **irdaServiceName** to specify their well-known service name during a call to the Windows Sockets [**bind**](https://msdn.microsoft.com/library/windows/desktop/ms737550) function.

</dd> </dl>

## Remarks

IrDA applications must not issue a [**connect**](https://msdn.microsoft.com/library/windows/desktop/ms737625) function call after issuing a [**bind**](https://msdn.microsoft.com/library/windows/desktop/ms737550) call.

 

 




