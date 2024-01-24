---
description: Describes the **ISuspendingEventArgs** interface, and documents its members, properties, remarks, and requirements.
ms.assetid: 2590AFAA-679C-49F1-804F-D429BB971727
title: ISuspendingEventArgs interface (Windows.ApplicationModel.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- ISuspendingEventArgs
api_type:
- COM
api_location:
- Windows.ApplicationModel.h
---

# ISuspendingEventArgs interface

Provides data for an app suspending event.

## Members

The **ISuspendingEventArgs** interface inherits from [**IInspectable**](/windows/win32/api/inspectable/nn-inspectable-iinspectable). **ISuspendingEventArgs** also has these types of members:

-   [Properties](#properties)

### Properties

The **ISuspendingEventArgs** interface has these properties.

| Property                                                                           | Access type           | Description                                   |
|:-----------------------------------------------------------------------------------|:----------------------|:----------------------------------------------|
| [**SuspendingOperation**](isuspendingeventargs-suspendingoperation.md)<br/> | Read/write<br/> | Gets the app suspending operation.<br/> |

## Remarks

This object is accessed when you implement event handlers like [**SuspendingEventHandler**](/uwp/api/windows.ui.webui.suspendingeventhandler), [**SuspendingEventHandler**](/uwp/api/windows.ui.xaml.suspendingeventhandler), and [**add\_Suspending**](/previous-versions//hh438376(v=vs.85)) to respond to app suspending events.

## Requirements

| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                          |
| Header<br/>                   | <dl> <dt>Windows.ApplicationModel.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Windows.ApplicationModel.idl</dt> </dl> |



## See also

* [**IInspectable**](/windows/win32/api/inspectable/nn-inspectable-iinspectable)
* [**ISuspendingOperation**](isuspendingoperation.md)
* [**ISuspendingDeferral**](isuspendingdeferral.md)
* 
