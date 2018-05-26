---
title: Data Binding through IPropertyNotifySink
description: Data Binding through IPropertyNotifySink
ms.assetid: 275a84b3-65d8-43de-bfba-72e3e5ee59fe
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Data Binding through IPropertyNotifySink

Objects that support properties, for example, through OLE Automation and the **IDispatch** interface, may want to allow clients to be notified when certain properties change value. Such a property is called a bindable property because the notifications allow a client to synchronize its own display of the object's current property values. In addition, the same objects may wish to allow a client to control when certain properties are allowed to change. Such properties are called request edit properties.

The [**IPropertyNotifySink**](/windows/win32/OCIdl/nn-ocidl-ipropertynotifysink?branch=master) is a standard notification interface that supports bindable and request-edit properties. **IPropertyNotifySink** is supported from an object with properties as an outgoing interface. That is, the interface itself is implemented by a client's sink object, and the client connects the sink to the supporting object through the connection point mechanism described earlier. The **IPropertyNotifySink**is defined as follows:

``` syntax
interface IPropertyNotifySink : IUnknown 
  { 
    HRESULT OnChanged([in] DISPID dispID); 
    HRESULT OnRequestEdit([in] DISPID dispID); 
  } 
 
```

When an object wishes to notify its connected sinks that a bindable property identified with a given DISPID has changed, it calls [**OnChanged**](/windows/win32/OCIdl/nf-ocidl-ipropertynotifysink-onchanged?branch=master). If an object changes multiple properties at once, it can pass DISPID\_UNKNOWN to **OnChanged** in which case a client refreshes its cache of all property values of interest.

When a request edit property is about to change, an object can ask the client whether it will allow that change to occur. The object calls [**OnRequestEdit**](/windows/win32/OCIdl/nf-ocidl-ipropertynotifysink-onrequestedit?branch=master) passing the DISPID of the property in question (or DISPID\_UNKNOWN to identify all properties). The client's sink returns S\_OK to indicate that the change is allowed, or S\_FALSE (or an error) to indicate that change is not allowed. When an object calls **OnRequestEdit**, it is required to obey the client's wishes by following the exact semantics of S\_OK and S\_FALSE return values.

Note that [**OnRequestEdit**](/windows/win32/OCIdl/nf-ocidl-ipropertynotifysink-onrequestedit?branch=master) cannot be used for data validation because at the time of the call, the new value of the property is not yet available. The notification can only be used to control a read-only state for a property.

Objects control which properties are bindable and request edit and mark such properties in the object's type information. In the type information, the attribute bindable marks a property as supporting [**OnChanged**](/windows/win32/OCIdl/nf-ocidl-ipropertynotifysink-onchanged?branch=master). The attribute requestedit marks a property as supporting [**OnRequestEdit**](/windows/win32/OCIdl/nf-ocidl-ipropertynotifysink-onrequestedit?branch=master).

One property can support both behaviors in which case [**OnRequestEdit**](/windows/win32/OCIdl/nf-ocidl-ipropertynotifysink-onrequestedit?branch=master) is called first, and only if change is allowed is [**OnChanged**](/windows/win32/OCIdl/nf-ocidl-ipropertynotifysink-onchanged?branch=master) called.

The one exception to the behavior of such properties is that no notifications are sent as a result of an object's initialization or loading procedures. At such times, it is assumed that all properties change and that all must be allowed to change. Notifications to this interface are therefore only meaningful in the context of a fully initialized/loaded object.

Two other attributes can be applied to properties in an object's type information. The defaultbind attribute marks a bindable property as being the one that best represents the state of the object as a whole. The displaybind attribute marks a bindable property as suitable for display in a client's own user interface.

## Related topics

<dl> <dt>

[Property Pages and Property Sheets](property-pages-and-property-sheets.md)
</dt> </dl>

 

 




