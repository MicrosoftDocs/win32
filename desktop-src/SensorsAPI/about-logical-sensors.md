---
Description: Logical sensors provide data without depending on hardware devices.
ms.assetid: fb0f0324-d72e-4759-9f4d-deedf8848e21
title: About Logical Sensors
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# About Logical Sensors

*Logical sensors* provide data without depending on hardware devices. For example, a logical sensor could provide data about the user's current location by using a service that looks up an IP address in a table. Logical sensors are implemented as sensor drivers. For information about how to implement a sensor driver, see the Windows Driver Kit.

After a logical sensor is installed on the user's computer, you can use it in the same way as a hardware-based sensor. The Sensor API will provide an [**ISensor**](/windows/desktop/api/sensorsapi/nn-sensorsapi-isensor) interface to represent the logical sensor, and your program can request data through the same mechanisms as you would use for any other type of sensor. Logical sensors can also use the platform-defined sensor categories, types, data types, properties, and events. Or you can define custom values.

The [**ILogicalSensorManager**](https://msdn.microsoft.com/en-us/library/Dd318934(v=VS.85).aspx) interface enables developers who create logical sensors to manage connections to the Sensor and Location platform.

> [!Note]  
> As with other drivers, installing or uninstalling a logical sensor driver requires administrator privileges.

 

To try using a sample logical sensor, see [About the Samples and Tools](about-the-samples.md).

## Managing Logical Sensors

[**ILogicalSensorManager**](https://msdn.microsoft.com/en-us/library/Dd318934(v=VS.85).aspx) has the following methods:

-   [**Connect**](https://msdn.microsoft.com/en-us/library/Dd374029(v=VS.85).aspx)
-   [**Disconnect**](https://msdn.microsoft.com/en-us/library/Dd374030(v=VS.85).aspx)
-   [**Uninstall**](https://msdn.microsoft.com/en-us/library/Dd374031(v=VS.85).aspx)

When you call [**Connect**](https://msdn.microsoft.com/en-us/library/Dd374029(v=VS.85).aspx), the Sensor API creates an instance of the sensor driver, if one does not already exist, and then connects the logical sensor to the platform. This means that the logical sensor appears with other sensors in the **Location and Other Sensors** Control Panel. When you call [**Disconnect**](https://msdn.microsoft.com/en-us/library/Dd374030(v=VS.85).aspx), the Sensor API disconnects the logical sensor and removes it from the Control Panel. Calling **Disconnect** does not remove the logical sensor from **Device Manager**. Therefore, future calls to **Connect** will result in a much faster connection to the logical sensor.

To remove a logical sensor, you must call [**Uninstall**](https://msdn.microsoft.com/en-us/library/Dd374031(v=VS.85).aspx). Uninstalling a logical sensor removes the sensor from **Device Manager**. Because logical sensor devices exist only in memory, a logical sensor is uninstalled when the user restarts Windows.

The Sensor API identifies a particular logical sensor by its *logical ID*, which is a **GUID**. Each time you connect to a particular logical sensor, you must provide a logical ID. Each time you disconnect or uninstall a particular sensor, you must provide the same logical ID that you used to connect. If you connect to the same logical sensor driver multiple times by using different logical IDs, you will create a separate instance of the logical sensor for each new logical ID. Even if you call [**Disconnect**](https://msdn.microsoft.com/en-us/library/Dd374030(v=VS.85).aspx) for each logical ID, these separate instances will remain in **Device Manager** until you call [**Uninstall**](https://msdn.microsoft.com/en-us/library/Dd374031(v=VS.85).aspx) for each logical sensor, or the user restarts Windows.

## Related topics

<dl> <dt>

[Using Logical Sensors](using-logical-sensors.md)
</dt> </dl>

 

 



