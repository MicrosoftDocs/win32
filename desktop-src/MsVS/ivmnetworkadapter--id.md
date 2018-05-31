---
title: IVMNetworkAdapter \_ID property
description: The \_ID property contains an internal ID number for this network adapter.
ms.assetid: b46fa209-3122-4afa-864f-8ca0c8645a48
keywords:
- _ID property Virtual Server
- _ID property Virtual Server , IVMNetworkAdapter interface
- IVMNetworkAdapter interface Virtual Server , _ID property
topic_type:
- apiref
api_name:
- IVMNetworkAdapter._ID
- IVMNetworkAdapter.get__ID
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IVMNetworkAdapter::\_ID property

The **\_ID** property contains an internal ID number for this network adapter.

This property is read-only.

## Syntax


```C++
HRESULT get__ID(
  [out] long *identifier
);
```



## Property value

The internal ID number for this network adapter.

## Error codes



| Name                                                                                           | Meaning                                             |
|------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| <dl> <dt> S\_OK</dt> </dl>              | The operation was successful.<br/>            |
| <dl> <dt>E\_POINTER</dt> </dl>          | The parameter *identifier* was **NULL**.<br/> |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl>  | The virtual machine cannot be found.<br/>     |
| <dl> <dt> DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>        |



## Remarks

Not usable by scripting languages.

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMNetworkAdapter**](ivmnetworkadapter.md)
</dt> </dl>

 

 





