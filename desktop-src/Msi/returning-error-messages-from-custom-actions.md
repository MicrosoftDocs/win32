---
description: This section describes how to send messages from custom actions that actually perform a part of the installation by calling a dynamic link library or script.
ms.assetid: 637efccf-920d-421d-9183-528cc3515bf8
title: Returning Error Messages from Custom Actions
ms.topic: article
ms.date: 05/31/2018
---

# Returning Error Messages from Custom Actions

This section describes how to send messages from custom actions that actually perform a part of the installation by calling a dynamic link library or script. Note that [Custom Action Type 19](custom-action-type-19.md) only sends a specified error message, returns failure, and then terminates the installation. Custom Action Type 19 does not perform any part of the installation.

To send an error message from a custom action that uses a [dynamic-link library](dynamic-link-libraries.md) (DLL), have the custom action call [**MsiProcessMessage**](/windows/desktop/api/Msiquery/nf-msiquery-msiprocessmessage). Note that custom actions launched by a [DoAction ControlEvent](doaction-controlevent.md) can send messages with the [**Message**](session-message.md) method but cannot send a message with **MsiProcessMessage**. On systems earlier than Windows Server 2003, custom actions launched by a DoAction ControlEvent cannot send messages with **MsiProcessMessage** or **Message** method. For more information, see [Sending Messages to Windows Installer Using MsiProcessMessage](sending-messages-to-windows-installer-using-msiprocessmessage.md).

**To display an error message from within a custom action using a DLL**

1.  The custom action should call [**MsiProcessMessage**](/windows/desktop/api/Msiquery/nf-msiquery-msiprocessmessage) and pass in the parameters *hInstall*, *eMessageType*, and *hRecord*. The handle to the installation, [Custom Action Type 19](custom-action-type-19.md), may be provided to the custom action as described in [Accessing the Current Installer Session from Inside a Custom Action](accessing-the-current-installer-session-from-inside-a-custom-action.md) or from [**MsiOpenProduct**](/windows/desktop/api/Msi/nf-msi-msiopenproducta) or [**MsiOpenPackage**](/windows/desktop/api/Msi/nf-msi-msiopenpackagea).
2.  The parameter *eMessageType* should specify one of the message types as listed in [**MsiProcessMessage**](/windows/desktop/api/Msiquery/nf-msiquery-msiprocessmessage).
3.  The *hRecord* parameter of the [**MsiProcessMessage**](/windows/desktop/api/Msiquery/nf-msiquery-msiprocessmessage) function depends upon the message type. See [Sending Messages to Windows Installer Using MsiProcessMessage](sending-messages-to-windows-installer-using-msiprocessmessage.md). If the message contains formatted data, enter the message into the [Error](error-table.md) table using the formatting described in [Formatted](formatted.md).

To send an error message from a custom action that uses [Scripts](scripts.md), the custom action may call the [**Message**](session-message.md) method of the [**Session**](session-object.md) object.

**To display an error message from within a custom action using script**

1.  The custom action should call the [**Message**](session-message.md) method of the [**Session**](session-object.md) object and pass in the parameters *kind* and *record*.
2.  The parameter *kind* should specify one of the message types listed in the [**Message**](session-message.md) method.
3.  The *record* parameter of the [**Message**](session-message.md) method depends upon the message type. If the message contains formatted data, enter the message into the [Error](error-table.md) table using the formatting described in [Formatted](formatted.md).

Custom actions using [Executable Files](executable-files.md) cannot send a message by calling [**MsiProcessMessage**](/windows/desktop/api/Msiquery/nf-msiquery-msiprocessmessage) or the [**Message**](session-message.md) method because they cannot get a handle to the installation.

## Related topics

<dl> <dt>

[Custom Action Return Values](custom-action-return-values.md)
</dt> </dl>

 

 



