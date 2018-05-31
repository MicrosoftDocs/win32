---
title: '\_IVMRCClientControlEvents OnStateChanged method'
description: Called when the VMRC client connection state changes.
ms.assetid: 24615b12-f256-465f-802b-5c59e5e60fbe
keywords:
- OnStateChanged method Virtual Server
- OnStateChanged method Virtual Server , _IVMRCClientControlEvents interface
- _IVMRCClientControlEvents interface Virtual Server , OnStateChanged method
- OnStateChanged method Virtual Server , VMRCClientControl interface
- VMRCClientControl interface Virtual Server , OnStateChanged method
topic_type:
- apiref
api_name:
- _IVMRCClientControlEvents.OnStateChanged
- VMRCClientControl.OnStateChanged
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# \_IVMRCClientControlEvents::OnStateChanged method

The **OnStateChanged** method is called when the VMRC client connection state changes.

## Syntax


```C++
HRESULT OnStateChanged(
  [in] VMRCState state
);
```



## Parameters

<dl> <dt>

*state* \[in\]
</dt> <dd>

The current VMRC client connection state.

</dd> </dl>

## Return value

A [**32-bit value**](hresult-codes-specific-to-the-virtual-server.md) that describes an error or warning.

## Remarks

This method is called when the connection state of the VMRC client control object changes. The client program must implement this interface method to receive notification of the event originating from the [**IVMRCClientControl**](ivmrcclientcontrol.md) object.

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |



## See also

<dl> <dt>

[**\_IVMRCClientControlEvents**](-ivmrcclientcontrolevents.md)
</dt> </dl>

 

 





