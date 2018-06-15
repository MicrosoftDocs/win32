---
Description: 'The DoInitialize method must be implemented by the monitor. The MCSVC calls this method to obtain a capture filter immediately before calling the NPP's IRTC::Connect method.'
ms.assetid: '5e43be75-21b3-4f37-ad53-3ffdd55f56a1'
title: 'IMonitor::DoInitialize method'
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IMonitor::DoInitialize method

The **DoInitialize** method must be implemented by the monitor. The MCSVC calls this method to obtain a capture filter immediately before calling the NPP's [IRTC::Connect](irtc-connect.md) method.

## Syntax


```C++
HRESULT DoInitialize(
  [in]      IUnknown *pUnkMonitorCtrl,
  [in, out] HBLOB    hNPPBlob
);
```



## Parameters

<dl> <dt>

*pUnkMonitorCtrl* \[in\]
</dt> <dd>

An [IUnknown](https://msdn.microsoft.com/en-us/library/ms680509(v=VS.85).aspx) pointer passed in by the MCSVC. To obtain a supported monitor control interface, the monitor must call [IUnknown::QueryInterface](https://msdn.microsoft.com/en-us/library/ms682521(v=VS.85).aspx) on the pointer.

</dd> <dt>

*hNPPBlob* \[in, out\]
</dt> <dd>

On input, a handle to an NPP BLOB.

On output, an NPP BLOB that contains a capture filter.

</dd> </dl>

## Return value

If the method is successful, the return value is S\_OK (which is the same as NOERROR).

If the method is unsuccessful, the return value is an error code. On error, the MCSVC will not create the monitor or call [IUnknown::Release](https://msdn.microsoft.com/en-us/library/ms682317(v=VS.85).aspx) on the interface pointer.

## Remarks

The MCSVC calls the **DoInitialize** method to perform any required monitor initialization.

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



 

 




