---
description: The OnStart method is an optional method that can be implemented by the monitor. The MCSVC calls this method to request that the monitor start the capture.
ms.assetid: 992ee27e-aaba-4e65-989b-e3f0fbd542ea
title: IMonitor::OnStart method (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IMonitor.OnStart
api_type: 
- COM
api_location: 
- Netmon.h
---

# IMonitor::OnStart method

The **OnStart** method is an optional method that can be implemented by the monitor. The MCSVC calls this method to request that the monitor start the capture.

## Syntax


```C++
HRESULT OnStart(
  [in] IUnknown *pUnkNPP
);
```



## Parameters

<dl> <dt>

*pUnkNPP* \[in\]
</dt> <dd>

An [IUnknown](/windows/win32/api/unknwn/nn-unknwn-iunknown) pointer to the [IRTC](irtc.md) interface. The monitor can use this interface to obtain statistics that can be used to determine if the capture should be started.

</dd> </dl>

## Return value

If the method is successful, the return value is S\_OK (which is the same as NOERROR). When S\_OK is returned, the MCSVC calls the [IRTC::Start](irtc-start.md) method.

If the method is unsuccessful, the return value is an error code. The MCSVC will not start the capture if any error code is returned.

## Remarks

The MCSVC calls this method before the NPP's [IRTC::Start](irtc-start.md) method is called to start the capture.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



## See also

<dl> <dt>

[IMonitor](imonitor.md)
</dt> <dt>

[Network Packet Providers](network-packet-providers.md)
</dt> </dl>

 

