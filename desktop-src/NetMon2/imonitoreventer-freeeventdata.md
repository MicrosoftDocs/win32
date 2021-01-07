---
description: The FreeEventData method frees space allocated for the NMEVENTDATA structure.
ms.assetid: f86dcfd8-5a3b-4ce3-9d45-04545b030a89
title: IMonitorEventer::FreeEventData method (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IMonitorEventer.FreeEventData
api_type: 
- COM
api_location: 
- Netmon.h
---

# IMonitorEventer::FreeEventData method

The **FreeEventData** method frees space allocated for the [**NMEVENTDATA**](nmeventdata.md) structure.

## Syntax


```C++
HRESULT FreeEventData(
  [in] PNMEVENTDATA pNMEventData
);
```



## Parameters

<dl> <dt>

*pNMEventData* \[in\]
</dt> <dd>

Address of the [**NMEVENTDATA**](nmeventdata.md) structure, the memory of which is freed.

</dd> </dl>

## Return value

This method returns S\_OK.

## Remarks

Monitors call this method to free the memory they allocate for the event data structure. Be aware that while the monitor still has a pointer to strings in an allocated [**NMEVENTDATA**](nmeventdata.md) structure, the memory for these strings must be freed before the **FreeEventData** method is called.

For more information about how to allocate memory for an [**NMEVENTDATA**](nmeventdata.md) structure, see [**IMonitorEventer::GetEventData**](imonitoreventer-geteventdata.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



## See also

<dl> <dt>

[**IMonitorEventer**](imonitoreventer.md)
</dt> <dt>

[**IMonitorEventer::GetEventData**](imonitoreventer-geteventdata.md)
</dt> <dt>

[**NMEVENTDATA**](nmeventdata.md)
</dt> </dl>

 

 




