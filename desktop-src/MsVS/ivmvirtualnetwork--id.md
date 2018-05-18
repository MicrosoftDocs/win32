---
title: IVMVirtualNetwork \_ID property
description: The \_ID property contains an internal ID for this virtual network.
ms.assetid: '8bd27cab-f492-49b4-9d63-ad5c4cd866c9'
keywords: ["_ID property Virtual Server", "_ID property Virtual Server , IVMVirtualNetwork interface", "IVMVirtualNetwork interface Virtual Server , _ID property"]
topic_type:
- apiref
api_name:
- IVMVirtualNetwork._ID
- IVMVirtualNetwork.get__ID
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualNetwork::\_ID property

The **\_ID** property contains an internal ID for this virtual network.

This property is read-only.

## Syntax


```C++
HRESULT get__ID(
  [out] VARIANT *identifier
);
```



## Property value

The internal ID for this virtual network.

## Error codes



| Name                                                                                           | Meaning                                             |
|------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| <dl> <dt> S\_OK</dt> </dl>              | The operation was successful.<br/>            |
| <dl> <dt>E\_POINTER</dt> </dl>          | The parameter *identifier* was **NULL**.<br/> |
| <dl> <dt> DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>        |



## Remarks

Not usable by scripting languages.

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualNetwork**](ivmvirtualnetwork.md)
</dt> </dl>

 

 





