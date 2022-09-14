---
description: The DoConfigure method must be implemented by the monitor. The MCSVC calls this method to obtain configuration information for the capture.
ms.assetid: bc2a3246-28dc-4452-a98e-a8a2447bb127
title: IMonitor::DoConfigure method (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IMonitor.DoConfigure
api_type: 
- COM
api_location: 
- Netmon.h
---

# IMonitor::DoConfigure method

The **DoConfigure** method must be implemented by the monitor. The MCSVC calls this method to obtain configuration information for the capture.

## Syntax


```C++
HRESULT STDMETHODCALLTYPE DoConfigure(
  [in]  char *pName,
  [in]  char *pConfiguration,
  [out] char **ppScriptInstance
);
```



## Parameters

<dl> <dt>

*pName* \[in\]
</dt> <dd>

Name of an instance of the monitor.

</dd> <dt>

*pConfiguration* \[in\]
</dt> <dd>

Configuration string provided by the MCSVC. The monitor must parse this string for configuration data.

</dd> <dt>

*ppScriptInstance* \[out\]
</dt> <dd>

Address of the HTML string used to configure the monitor. If a default script is used for configuration, this value should be set to **NULL**.

</dd> </dl>

## Return value

If the method is successful, the return value is S\_OK (which is the same as NOERROR), and the MCSVC will run the monitor.

If the method is unsuccessful, the return value is an error code. A return value of NMERR\_MONITOR\_CONFIG\_FAILED is acceptable, but when this error is returned, the monitor cannot start until a future **DoConfigure** call succeeds. Any other error prevents the instance of the monitor from being enabled.

## Remarks

The MCSVC calls this method after it has connected to the network and before the [IRTC::Configure](irtc-configure.md) method is called.

The monitor can store information provided by this call, update the HTML script or configuration string, and set the [capture filter](capture-filters.md) in the NPP BLOB.

The MCSVC may call this method several times, but it cannot be not called while the monitor is capturing data. Note that every time an [NPP](network-packet-providers.md) starts a capture, the connection to the network must be configured. This restriction includes situations in which the NPP starts and stops the same capture.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



 

 




