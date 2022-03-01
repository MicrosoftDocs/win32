---
title: add timeout
description: Adds a global timeout to the HTTP.sys service.
ms.assetid: c59a64e2-36aa-4428-b727-df21f5632d0d
keywords:
- add timeout HTTP
topic_type:
- apiref
api_name:
- add timeout
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# add timeout

Adds a global timeout to the HTTP.sys service.

``` syntax
add timeout [timeouttype=]{idleconnectiontimeout|headerwaittimeout}
            [value=]u-short
```

## Parameters

**\[timeouttype=\]{idleconnectiontimeout\|headerwaittimeout}**

Specifies the type of timeout for setting.

__\[value=\]__*u-short*

Specifies the value of the timeout (in seconds). If value is hexadecimal, then add the prefix 0x.

## Examples

**add timeout timeouttype=idleconnectiontimeout value=120**

**add timeout timeouttype=headerwaittimeout value=0x40**
