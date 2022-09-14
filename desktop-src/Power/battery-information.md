---
description: Batteries can provide power for portable computers and computers running on an uninterruptible power supply (UPS).
ms.assetid: 3580b37d-611c-46b4-9300-4943833d6852
title: Battery Information
ms.topic: article
ms.date: 05/31/2018
---

# Battery Information

Batteries can provide power for portable computers and computers running on an uninterruptible power supply (UPS). On these computers, the operating system provides information on the state of the battery so applications can provide useful functions for the user. (Some older nonstandard battery systems and UPSs are not supported.)

Note that this overview assumes you are familiar with [device management](/windows/desktop/DevIO/device-management).

To obtain information about the battery status, use the [**GetSystemPowerStatus**](/windows/desktop/api/Winbase/nf-winbase-getsystempowerstatus) function, which returns general information about all power sources in the system. You should use **GetSystemPowerStatus** whenever possible.

In some cases, however, detailed information about each individual battery is necessary. For this purpose, each battery device exposes an IOCTL interface. The following IOCTL operations are performed using the [**DeviceIoControl**](/windows/desktop/api/ioapiset/nf-ioapiset-deviceiocontrol) function:

<dl>

[**IOCTL\_BATTERY\_QUERY\_INFORMATION**](ioctl-battery-query-information.md)  
[**IOCTL\_BATTERY\_QUERY\_STATUS**](ioctl-battery-query-status.md)  
[**IOCTL\_BATTERY\_QUERY\_TAG**](ioctl-battery-query-tag.md)  
[**IOCTL\_BATTERY\_SET\_INFORMATION**](ioctl-battery-set-information.md)  
</dl>

To use this interface, an application must follow several steps. First, it must use setup routines to enumerate all devices that have a battery class interface. Note that these devices represent the battery ports, not actual batteries present in the system. The application must then open a handle to each device so it can use the [**DeviceIoControl**](/windows/desktop/api/ioapiset/nf-ioapiset-deviceiocontrol) function to send requests to the device, and then acquire tags for any batteries that are inserted. After completing these steps, the application can send queries to each battery device.

## Battery Tags

Because each battery device represents a slot into which a battery can be inserted, there must be a way to determine when the battery is removed and reinserted, replaced, or changed in any other way. To do this, each battery in a particular slot is assigned a tag. This tag must be used for all queries for information. If the tag provided by the application does not match the battery, the query fails, indicating to the application that the battery has changed in some way. To successfully complete the query, a new battery tag is required. Acquire the tag using the [**IOCTL\_BATTERY\_QUERY\_TAG**](ioctl-battery-query-tag.md) operation. If a battery is present in that slot, the tag returned can be passed to any of the other battery IOCTLs to perform other functions. On a multi-battery system, each battery device (slot) issues battery tags independently, so the tag from two separate devices could at times be identical.

A change in the battery tag does not necessarily mean that the battery was removed and reinserted or replaced. A new tag can be generated if there is a change in any of the data that would normally be static. For example, when a battery is done charging, the last fully charged capacity may have changed. The tag can also change if battery communication was temporarily lost or if there was an improper notification from the BIOS. On some systems, the battery tag may be updated whenever the AC status changes. This behavior is due to a characteristic of the battery system and isn't common.

Whenever the battery tag is updated, the battery should be treated as if it were a new battery and all cached data should be re-read. If an application needs to know if the same physical battery is present, it should check the value of **BatteryUniqueID** in the output buffer of [**IOCTL\_BATTERY\_QUERY\_INFORMATION**](ioctl-battery-query-information.md) when called with the **BatteryUniqueID** information level.

## Related topics

<dl> <dt>

[About Power Management](about-power-management.md)
</dt> <dt>

[Enumerating Battery Devices](enumerating-battery-devices.md)
</dt> </dl>

 

 
