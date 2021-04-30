---
description: The Sensor API provides a method you can use to prompt the user for permissions to use a sensor or collection of sensors.
ms.assetid: c755edcf-18c1-43d5-9dfe-c073e1f96b5f
title: Managing User Permissions
ms.topic: article
ms.date: 05/31/2018
---

# Managing User Permissions

The Sensor API provides a method you can use to prompt the user for permissions to use a sensor or collection of sensors.

Because sensors can reveal sensitive information, Windows requires that users enable sensors before your program can access any data.

You may want to request permission when you want to use sensors for which the current [**SensorState**](/windows/win32/api/sensorsapi/ne-sensorsapi-sensorstate) is SENSOR\_STATE\_ACCESS\_DENIED.

To request permissions, call the [**ISensorManager::RequestPermissions**](/windows/win32/api/sensorsapi/nf-sensorsapi-isensormanager-requestpermissions) method. When you call this method, Windows opens the **Enable sensors** dialog box to prompt the user to enable the sensors you requested. This dialog box provides the user with the names of the sensors you requested. The user can choose one of the following options:

-   **Enable these sensors**.
-   **Don't enable these sensors**.
-   **Open Control Panel for more options**.

If a user chooses **Don't enable these sensors**, Windows will not show the **Enable sensors** dialog box again for those particular sensors, even if your program calls [**RequestPermissions**](/windows/win32/api/sensorsapi/nf-sensorsapi-isensormanager-requestpermissions). If the user chooses any other option, Windows will allow the dialog box to be displayed when requested. If your call to **RequestPermissions** contains some sensors that the user has previously chosen to keep disabled, the Sensor API will remove these sensors from the list of sensors the user sees.

### Modal or Modeless Behavior

The [**RequestPermissions**](/windows/win32/api/sensorsapi/nf-sensorsapi-isensormanager-requestpermissions) method takes a **Boolean** argument that determines whether the **Enable sensors** dialog box is displayed as a modal or modeless window. This setting also affects whether the behavior of the dialog box return code is synchronous or asynchronous.

When modal, the dialog box has exclusive focus among application windows until the user chooses an option, and the **HRESULT** return code from your call to [**RequestPermissions**](/windows/win32/api/sensorsapi/nf-sensorsapi-isensormanager-requestpermissions) indicates the user choice. When modeless, the dialog box does not have exclusive focus and your call to **RequestPermissions** returns immediately. In this case, the return code indicates whether the method succeeded, but cannot be used to ascertain the user's choice. You can then determine which sensors have been enabled by handling the [**OnStateChanged**](/windows/win32/api/sensorsapi/nf-sensorsapi-isensorevents-onstatechanged) event and checking each sensor for SENSOR\_STATE\_READY.

For more information about return codes, see the [**RequestPermissions**](/windows/win32/api/sensorsapi/nf-sensorsapi-isensormanager-requestpermissions) reference page.

### Best Practice: Avoid Multiple Modeless Calls to RequestPermissions

Repeated modeless calls to [**RequestPermissions**](/windows/win32/api/sensorsapi/nf-sensorsapi-isensormanager-requestpermissions) will display multiple instances of the **Enable these sensors** dialog box, and can potentially flood the screen with dialog boxes, resulting in a poor user experience. If you think that after your first call to **RequestPermissions**, other location sensors might be installed, requiring another call to **RequestPermissions**, you should either call **RequestPermissions** modally, or wait until all location sensors are installed to make a modeless call.

## Related topics

<dl> <dt>

[Privacy and Security in the Sensor and Location Platform](privacy-and-security-in-the-sensor-and-location-platform.md)
</dt> <dt>

[Requesting User Permissions](requesting-user-permissions.md)
</dt> </dl>

 

 
