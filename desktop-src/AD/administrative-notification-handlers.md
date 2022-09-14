---
title: Administrative Notification Handlers
description: The Microsoft Active Directory Users and Computers MMC snap-in provides a mechanism to enable components to receive notifications when the user deletes, renames, moves, or changes the properties of an object using the snap-in.
ms.assetid: 49dbb995-c760-4fac-a72f-d5d94afb63c7
ms.tgt_platform: multiple
keywords:
- Administrative Notification Handlers AD
ms.topic: article
ms.date: 05/31/2018
---

# Administrative Notification Handlers

The Microsoft Active Directory Users and Computers MMC snap-in provides a mechanism to enable components to receive notifications when the user deletes, renames, moves, or changes the properties of an object using the snap-in. The component that receives the notifications is known as a "notification handler".

This is useful when multiple objects are linked together and must exist within the same container. If one of the linked objects is moved, a notification is supplied to the notification handler and the notification handler can move the other linked objects to the same folder.

When one of the operations is performed and one or more notification handlers is installed, the Users and Computers snap-in will display a confirmation dialog box that lists the notification handlers and a check box for each handler. If the check box for a handler is selected, the handler is notified. If the check box is not selected, the handler is not notified.

## Implementing a Notification Handler

A notification handler is a COM object implemented as an in-proc server. The notification handler must implement the [**IDsAdminNotifyHandler**](/windows/desktop/api/DSAdmin/nn-dsadmin-idsadminnotifyhandler) interface.

When an event occurs that will cause a notification, the Users and Computers snap-in enumerates the registered notification handlers and creates each one using the CLSID for the handler. After the handler is created, the snap-in calls the [**IDsAdminNotifyHandler::Initialize**](/windows/desktop/api/DSAdmin/nf-dsadmin-idsadminnotifyhandler-initialize) method. The **Initialize** method supplies the snap-in with the events the handler should receive.

If the event is one that should be sent to the notification handler, the snap-in calls the [**IDsAdminNotifyHandler::Begin**](/windows/desktop/api/DSAdmin/nf-dsadmin-idsadminnotifyhandler-begin) method. The **Begin** method provides the handler with the event occurring, data about the object that the event is occurring on and, depending on the event, data about what the object will become. The **Begin** method also provides the snap-in with the text that should be displayed for the handler in the confirmation dialog box.

When the [**Begin**](/windows/desktop/api/DSAdmin/nf-dsadmin-idsadminnotifyhandler-begin) method for each handler has been called, the snap-in displays the confirmation dialog box. The confirmation dialog box prompts the user to select which handlers will receive the notification. If the user presses the **No** push button in the confirmation dialog, none of the handlers are notified. If the user presses the **Yes** push button, each of the handlers selected in the confirmation dialog box receive the notification. The snap-in sends the notification to the handler by calling the [**IDsAdminNotifyHandler::Notify**](/windows/desktop/api/DSAdmin/nf-dsadmin-idsadminnotifyhandler-notify) method.

After all of the handlers have been notified, the snap-in calls the [**IDsAdminNotifyHandler::End**](/windows/desktop/api/DSAdmin/nf-dsadmin-idsadminnotifyhandler-end) method. The **End** method is always called, even if the [**Notify**](/windows/desktop/api/DSAdmin/nf-dsadmin-idsadminnotifyhandler-notify) method is not called.

## Registering a Notification Handler in the Windows Registry

Like all COM servers, a notification handler must be registered in the Windows registry. The handler is registered under the following key:


```C++
HKEY_CLASSES_ROOT - CLSID - <CLSID>
```



**&lt;CLSID&gt;** is the string representation of the CLSID as produced by the [**StringFromCLSID**](/windows/win32/api/combaseapi/nf-combaseapi-stringfromclsid) function. Under the **&lt;CLSID&gt;** key, there is an **InProcServer32** key that identifies the object as a 32-bit in-proc server. Under the **InProcServer32** key, the location of the DLL is specified in the default value and the threading model is specified in the **ThreadingModel** value. All notification handlers must use the **Apartment** threading model.

## Registering a Notification Handler with an Active Directory Server

Within Active Directory Domain Services, notification handler registration is specific to one locale. If the notification handler applies to all locales, it must be registered in the **displaySpecifier** object in all of the locale subcontainers in the DisplaySpecifiers container. If the notification handler is localized for a certain locale, it is registered in the **displaySpecifier** object in that locale's subcontainer. For more information about the DisplaySpecifiers container and locales, see [Display Specifiers](display-specifiers.md) and [DisplaySpecifiers Container](displayspecifiers-container.md).

Notification handlers are registered under the **dsUIAdminNotification** attribute in the **DS-UI-Default-Settings** container. This a multi-valued Unicode string value where each value requires the following format:


```C++
<order number>,<CLSID>
```



The "&lt;order number&gt;" is an unsigned number that represents the position of the handler in the confirmation dialog. When the confirmation dialog is displayed, the values are sorted using a comparison of each value's "&lt;order number&gt;". If more than one value has the same "&lt;order number&gt;", those handlers are displayed in the order they are read from the Active Directory server. A non-existing, that is, one not used by other values in the property, "&lt;order number&gt;" should be used if possible. There is no prescribed starting position, and gaps can appear in the "&lt;order number&gt;" sequence.

The "&lt;CLSID&gt;" is the string representation of the CLSID as produced by the [**StringFromCLSID**](/windows/win32/api/combaseapi/nf-combaseapi-stringfromclsid) function.

 

 
