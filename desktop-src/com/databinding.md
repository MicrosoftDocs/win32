---
title: Databinding
description: Databinding
ms.assetid: 7fc5f036-8b36-4e0e-a257-173010fe127a
ms.topic: article
ms.date: 05/31/2018
---

# Databinding

A new databinding attribute has been added to allow properties distinguish between communicating changes only when focus leaves the control or during all property change notifications.

The new attribute, known as ImmediateBind, enables controls to differentiate two different types of bindable properties. One type of bindable property needs to notify every change to the database, for example with a check box control where every change needs to be sent through to the underlying database even though the control has not lost the focus. However controls such as a listbox only wish to have the change of a property notified to the database when the control loses focus, as the user may have changed the highlighted selection with the arrow keys before finding the desired setting, to have the change notification sent to the database every time that the user hit the arrow key would be give unacceptable performance. The new immediate bind property allows individual bindable properties on a form to have this behavior specified, when this bit is set all changes will be notified.

The new ImmediateBind bit maps through to the new VARFLAG\_FIMMEDIATEBIND (0x80) and the FUNCFLAG\_FIMMEDIATEBIND (0x80) bits in the VARFLAGS and FUNCFLAGS enumerations for the [ITypeInfo](/windows/win32/api/oaidl/nn-oaidl-itypeinfo) interface allowing for the properties attributes to be inspected.

 

 