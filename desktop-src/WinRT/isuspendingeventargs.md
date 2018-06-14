---
Description: Provides data for an app suspending event.
ms.assetid: 2590AFAA-679C-49F1-804F-D429BB971727
title: ISuspendingEventArgs interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# ISuspendingEventArgs interface

Provides data for an app suspending event.

## Members

The **ISuspendingEventArgs** interface inherits from [**IInspectable**](/windows/desktop/api/Inspectable/nn-inspectable-iinspectable). **ISuspendingEventArgs** also has these types of members:

-   [Properties](#properties)

### Properties

The **ISuspendingEventArgs** interface has these properties.



| Property                                                                           | Access type           | Description                                   |
|:-----------------------------------------------------------------------------------|:----------------------|:----------------------------------------------|
| [**SuspendingOperation**](isuspendingeventargs-suspendingoperation.md)<br/> | Read/write<br/> | Gets the app suspending operation.<br/> |



 

## Remarks

This object is accessed when you implement event handlers like [**SuspendingEventHandler**](https://msdn.microsoft.com/en-us/library/BR242303(v=Win.10).aspx), [**SuspendingEventHandler**](https://msdn.microsoft.com/en-us/library/BR244262(v=Win.10).aspx), and [**add\_Suspending**](https://msdn.microsoft.com/en-us/library/Hh438376(v=VS.85).aspx) to respond to app suspending events.

## Requirements



|                                     |                                                                                                         |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                          |
| Header<br/>                   | <dl> <dt>Windows.ApplicationModel.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Windows.ApplicationModel.idl</dt> </dl> |



## See also

<dl> <dt>

[**IInspectable**](/windows/desktop/api/Inspectable/nn-inspectable-iinspectable)
</dt> <dt>

[**ISuspendingOperation**](isuspendingoperation.md)
</dt> <dt>

[**ISuspendingDeferral**](isuspendingdeferral.md)
</dt> </dl>

 

 




