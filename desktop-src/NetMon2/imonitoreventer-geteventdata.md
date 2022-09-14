---
description: The GetEventData method allocates space for the NMEVENTDATA and NMCOLUMNINFO structures.
ms.assetid: b24a2a30-4543-4311-87ec-66872463aed7
title: IMonitorEventer::GetEventData method (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IMonitorEventer.GetEventData
api_type: 
- COM
api_location: 
- Netmon.h
---

# IMonitorEventer::GetEventData method

The **GetEventData** method allocates space for the [NMEVENTDATA](nmeventdata.md) and [NMCOLUMNINFO](nmcolumninfo.md) structures.

## Syntax


```C++
HRESULT GetEventData(
  [in]  BYTE         bNumColumns,
  [out] PNMEVENTDATA *ppNMEventData
);
```



## Parameters

<dl> <dt>

*bNumColumns* \[in\]
</dt> <dd>

Number of **NMCOLUMNINFO** structures needed.

</dd> <dt>

*ppNMEventData* \[out\]
</dt> <dd>

Address of the **NMEVENTDATA** structure that is returned.

</dd> </dl>

## Return value

If the method is successful, the return value is S\_OK.

If the method is unsuccessful, the return value is NMERR\_OUT\_OF\_MEMORY.

## Remarks

Monitors call this method to allocate memory for the event data and column information structures. To free memory allocated for an **NMEVENTDATA** structure, see [IMonitorEventer::FreeEventData](imonitoreventer-freeeventdata.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



## See also

<dl> <dt>

[IMonitorEventer](imonitoreventer.md)
</dt> <dt>

[IMonitorEventer::FreeEventData](imonitoreventer-freeeventdata.md)
</dt> <dt>

[NMEVENTDATA](nmeventdata.md)
</dt> <dt>

[NMCOLUMNINFO](nmcolumninfo.md)
</dt> </dl>

 

 




