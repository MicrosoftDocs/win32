---
title: Overloading IPropertyNotifySink
description: Overloading IPropertyNotifySink
ms.assetid: c6d52da0-7b7e-4ca8-b903-310bf988d2f7
ms.topic: article
ms.date: 05/31/2018
---

# Overloading IPropertyNotifySink

Many ActiveX control containers implement a modeless property browsing window. If a control's properties are altered through the control's property pages, then the control's properties can get out of sync with the container's view of those properties (the control is always right, of course). To ensure that it always has the current values for a control's properties, an ActiveX control container can overload the [**IPropertyNotifySink**](/windows/desktop/api/OCIdl/nn-ocidl-ipropertynotifysink) interface (data binding) and also use it to be notified that a control property has changed. This technique is optional and is not required of ActiveX control containers or ActiveX controls.

Note that a control should use [**OnRequestEdit**](/windows/desktop/api/OCIdl/nf-ocidl-ipropertynotifysink-onrequestedit) only for data binding; it is free to use [**OnChanged**](/windows/desktop/api/OCIdl/nf-ocidl-ipropertynotifysink-onchanged) for either or both purposes.

 

 




