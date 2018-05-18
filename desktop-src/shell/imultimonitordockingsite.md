---
Description: 'Implemented by the browser. Exposes methods that manage which monitor contains the Windows taskbar on a multiple monitor system.'
title: IMultiMonitorDockingSite interface
---

# IMultiMonitorDockingSite interface

Implemented by the browser. Exposes methods that manage which monitor contains the Windows taskbar on a multiple monitor system.

## Members

The **IMultiMonitorDockingSite** interface inherits from the [**IUnknown**](com.iunknown) interface. **IMultiMonitorDockingSite** also has these types of members:

-   [Methods](#methods)

### Methods

The **IMultiMonitorDockingSite** interface has these methods.



| Method                                                            | Description                                                                                |
|:------------------------------------------------------------------|:-------------------------------------------------------------------------------------------|
| [**GetMonitor**](imultimonitordockingsite-getmonitor.md)         | Gets the current default monitor.<br/>                                               |
| [**RequestMonitor**](imultimonitordockingsite-requestmonitor.md) | Verifies that the monitor is active and available.<br/>                              |
| [**SetMonitor**](imultimonitordockingsite-setmonitor.md)         | Changes which monitor is used for docked toolbars on a multiple monitor system.<br/> |



 

## Remarks

You do not typically implement the **IMultiMonitorDockingSite** interface. The Shell browser implements this interface to support multiple monitors.

## Requirements



|                                     |                                                                        |
|-------------------------------------|------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                   |



 

 




