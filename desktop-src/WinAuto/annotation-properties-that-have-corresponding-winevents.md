---
title: Annotation Properties That Have Corresponding WinEvents
description: Be careful when overriding properties that change frequently, particularly those that are examined by clients as a result of a WinEvent (such as State, Value, and, for some controls, the Name properties).
ms.assetid: 2505d015-9381-4e1c-a10f-6db3fbb25ca3
ms.topic: article
ms.date: 05/31/2018
---

# Annotation Properties That Have Corresponding WinEvents

Be careful when overriding properties that change frequently, particularly those that are examined by clients as a result of a WinEvent (such as [**State**](state-property.md), [**Value**](value-property.md), and, for some controls, the [**Name**](name-property.md) properties).

In many cases, especially for USER and ComCtl controls, the WinEvent signaling a property change is sent before the owner of the control is notified (typically via [WM\_NOTIFY](../controls/wm-notify.md)). Updating the property using [**SetPropValue**](/windows/desktop/api/Oleacc/nf-oleacc-iaccpropservices-setpropvalue) in the WM\_NOTIFY handler will be too late; clients using in-context hooking will already have accessed the old value.

You can handle these types of properties by using callback server objects (using [**SetPropServer**](/windows/desktop/api/Oleacc/nf-oleacc-iaccpropservices-setpropserver)); however, the server cannot use any state that is updated in the WM\_NOTIFY handler because that handler will not yet have been called. For example, instead of using a cached current value variable that is updated in the WM\_NOTIFY handler and will be out-of-date, the [**IAccPropServer::GetPropValue**](/windows/desktop/api/Oleacc/nf-oleacc-iaccpropserver-getpropvalue) callback object should send a message directly to the control to get its true current value to generate the required property.

 

 