---
Description: Provides data for an app suspending event.
ms.assetid: 2590AFAA-679C-49F1-804F-D429BB971727
title: ISuspendingEventArgs interface
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ISuspendingEventArgs interface

Provides data for an app suspending event.

## Members

The **ISuspendingEventArgs** interface inherits from [**IInspectable**](/windows/win32/Inspectable/nn-inspectable-iinspectable?branch=master). **ISuspendingEventArgs** also has these types of members:

-   [Properties](#properties)

### Properties

The **ISuspendingEventArgs** interface has these properties.



| Property                                                                           | Access type           | Description                                   |
|:-----------------------------------------------------------------------------------|:----------------------|:----------------------------------------------|
| [**SuspendingOperation**](isuspendingeventargs-suspendingoperation.md)<br/> | Read/write<br/> | Gets the app suspending operation.<br/> |



 

## Remarks

This object is accessed when you implement event handlers like [**SuspendingEventHandler**](w_ui_webui.suspendingeventhandler), [**SuspendingEventHandler**](w_ui_xaml.suspendingeventhandler), and [**add\_Suspending**](icoreapplication-add-suspending.md) to respond to app suspending events.

## Requirements



|                                     |                                                                                                         |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                          |
| Header<br/>                   | <dl> <dt>Windows.ApplicationModel.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Windows.ApplicationModel.idl</dt> </dl> |



## See also

<dl> <dt>

[**IInspectable**](/windows/win32/Inspectable/nn-inspectable-iinspectable?branch=master)
</dt> <dt>

[**ISuspendingOperation**](isuspendingoperation.md)
</dt> <dt>

[**ISuspendingDeferral**](isuspendingdeferral.md)
</dt> </dl>

 

 




