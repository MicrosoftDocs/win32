---
title: delete timeout
description: Deletes a global timeout and makes the HTTP.sys service revert to default values.
ms.assetid: 5fcd5df4-023e-486d-b41a-639e210a128f
keywords:
- delete timeout HTTP
topic_type:
- apiref
api_name:
- delete timeout
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# delete timeout

Deletes a global timeout and makes the HTTP.sys service revert to default values.

``` syntax
delete timeout [timeouttype=]{idleconnectiontimeout|headerwaittimeout}
 
```

## Parameters

<dl> <dt>

<span id="_timeouttype___idleconnectiontimeout_headerwaittimeout_"></span><span id="_TIMEOUTTYPE___IDLECONNECTIONTIMEOUT_HEADERWAITTIMEOUT_"></span>**\[timeouttype=\]{idleconnectiontimeout\|headerwaittimeout}**
</dt> <dd>

Specifies the type of timeout setting.

</dd> </dl>

## Examples

**delete timeout timeouttype=idleconnectiontimeout**

**delete timeout timeouttype=headerwaittimeout**

 

 




