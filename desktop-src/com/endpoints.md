---
title: Endpoints
description: Configures a COM application to use a specified TCP port number for DCOM communications.
ms.assetid: 2a286a13-24b8-418a-b29b-5543a1c56c45
keywords:
- Endpoints registry value COM
ms.topic: article
ms.date: 05/31/2018
---

# Endpoints

Configures a COM application to use a specified TCP port number for DCOM communications.

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Classes\AppID
   {AppID_GUID}
      Endpoints = ncacn_ip_tcp,0,port
```

## Remarks

This is a **REG\_MULTI\_SZ** value.

The *port* value is a number between 1024 and 65535 that specifies the TCP port number that your COM application will use for DCOM communications. If you do not specify this registry key, port numbers for DCOM communications are dynamically assigned. In most scenarios, you might prefer to leave this registry key undefined and allow DCOM to dynamically assign port numbers.

 

 




