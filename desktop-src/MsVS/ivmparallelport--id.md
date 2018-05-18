---
title: IVMParallelPort \_ID property
description: The \_ID property contains an internal ID number for this parallel port.
ms.assetid: 'a819388d-9ff6-4595-81da-1a02ca01a1d9'
keywords: ["_ID property Virtual Server", "_ID property Virtual Server , IVMParallelPort interface", "IVMParallelPort interface Virtual Server , _ID property"]
topic_type:
- apiref
api_name:
- IVMParallelPort._ID
- IVMParallelPort.get__ID
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMParallelPort::\_ID property

The **\_ID** property contains an internal ID number for this parallel port.

This property is read-only.

## Syntax


```C++
HRESULT get__ID(
  [out] long *identifier
);
```



## Property value

The internal ID number for this parallel port.

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

[**IVMParallelPort**](ivmparallelport.md)
</dt> </dl>

 

 





