---
Description: The IKsPin interface provides a method to retrieve the mediums supported by a pin on a kernel-mode filter. IKsPin has additional methods besides the one shown here, but they are not supported for DirectShow.
ms.assetid: 14d9bef2-e8f0-49d5-bd89-69a95814cf8c
title: IKsPin interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IKsPin interface

The `IKsPin` interface provides a method to retrieve the mediums supported by a pin on a kernel-mode filter. `IKsPin` has additional methods besides the one shown here, but they are not supported for DirectShow.

## Members

The **IKsPin** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/33f1d79a-33fc-4ce5-a372-e08bda378332) interface. **IKsPin** also has these types of members:

-   [Methods](#methods)

### Methods

The **IKsPin** interface has these methods.



| Method                                          | Description                                          |
|:------------------------------------------------|:-----------------------------------------------------|
| [**KsQueryMediums**](ikspin-ksquerymediums.md) | Retrieves the mediums supported by a pin.<br/> |



 

## Remarks

You must include Ks.h before Ksproxy.h.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Ksproxy.h</dt> </dl>    |
| Library<br/>                  | <dl> <dt>Strmiids.lib</dt> </dl> |



 

 




