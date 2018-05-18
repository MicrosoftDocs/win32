---
Description: 'The IMonitorEventer interface provides methods for submitting events and allocating and freeing monitor resources.'
ms.assetid: 'd59a8b42-cce3-410b-a62e-97d66d058d90'
title: IMonitorEventer interface
---

# IMonitorEventer interface

The **IMonitorEventer** interface provides methods for submitting events and allocating and freeing monitor resources.

## Members

The **IMonitorEventer** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IMonitorEventer** also has these types of members:

-   [Methods](#methods)

### Methods

The **IMonitorEventer** interface has these methods.



| Method                                                 | Description                                        |
|:-------------------------------------------------------|:---------------------------------------------------|
| [**FreeEventData**](imonitoreventer-freeeventdata.md) | Frees space allocated for monitor data.<br/> |
| [**GetEventData**](imonitoreventer-geteventdata.md)   | Allocates space for monitor data.<br/>       |
| [**SendNMEvent**](imonitoreventer-sendnmevent.md)     | Submits events to WMI.<br/>                  |



 

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



 

 




