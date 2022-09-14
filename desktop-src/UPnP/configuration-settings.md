---
title: Configuration Settings
description: The behavior of the Control Point API and Device Host API can be modified by changing settings in the registry.
ms.assetid: 81893cde-d28f-41ec-a6c1-159b3eb84274
ms.topic: article
ms.date: 05/31/2018
---

# Configuration Settings

The behavior of the [Control Point API](control-point-api.md) and [Device Host API](device-host-api.md) can be modified by changing settings in the registry.

There are seven registry values that affect behavior:

-   **DownloadScope**
-   **DeviceLifeTime**
-   \\**UPnP Device Host**\\**File Size Limit**
-   \\**Windows**\\**CurrentVersion**\\**UPnP**\\**File Size Limit**
-   **MaxCache**
-   **TTL**
-   **ReceiveScope**

There are two registry values called **File Size Limit**, one for description documents and the other for responses that use Simple Object Access Protocol (SOAP).

The location of each of the seven values in the registry is as follows:

```
HKEY_LOCAL_MACHINE
   SOFTWARE
      Microsoft
         UPnPControl Point
            DownloadScope
         UPnP Device Host
            Devices
               DeviceLifeTime
            File Size Limit
         Windows
            CurrentVersion
               UPnP
                  File Size Limit
   SYSTEM
      CurentControlSet
         Services
            SSDPSRV
               Parameters
                  MaxCache
                  TTL
                  ReceiveScope
```

## Registry Value Descriptions

The registry values are explained in the following list. Each registry value is a **REG\_DWORD** (a 32-bit integer). The effect of each value is global.

<dl> <dt>

<span id="DownloadScope"></span><span id="downloadscope"></span><span id="DOWNLOADSCOPE"></span>**DownloadScope**
</dt> <dd>

Specifies which IP addresses are valid for the device description document URL. If the IP address of the host that is specified in the description document URL is not within the scope specified by **DownloadScope**, that IP address is not valid and the device object will not be created.

The valid values are shown in the following table. The default value is 1.



| Value of **DownloadScope** | Meaning                                                                                                                                                                                                    |
|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0                          | Host's IP address must be a subnet address.                                                                                                                                                                |
| 1                          | Host's IP address must be a subnet address or a private address which is one of 10.*x*.*x*.*x*, 192.168.*x*.*x*, 172.16.*x*.*x* (as specified by RFC 1918), or 169.254.*x*.*x* (as specified by RFC 3330). |
| 2                          | Host's IP address must be a subnet address, private address, or an address that is within the time-to-live (TTL) hops from the control point.                                                              |
| 3                          | Host's IP address can be any address.                                                                                                                                                                      |
| >3                      | Same as that for the value 0.                                                                                                                                                                              |



 

</dd> <dt>

<span id="DeviceLifeTime"></span><span id="devicelifetime"></span><span id="DEVICELIFETIME"></span>**DeviceLifeTime**
</dt> <dd>

Optional. Specifies a device's lifetime, in seconds, which overrides the value provided in the device's announcement message. If **DeviceLifeTime** is present, the value specified in the device's announcement is ignored and the registry value is used instead. This applies to all devices.

Valid values range from 900 through **MAX\_DWORD**. The default value is 1800. If **DeviceLifeTime** is set to 0, the default value is used.

</dd> <dt>

<span id="_UPnP_Device_HostFile_Size_Limit"></span><span id="_upnp_device_hostfile_size_limit"></span><span id="_UPNP_DEVICE_HOSTFILE_SIZE_LIMIT"></span>\\**UPnP Device Host**\\**File Size Limit**
</dt> <dd>

Specifies the maximum size, in bytes, of each description document. This setting is not configurable in versions of Windows preceding Windows XP Service Pack 2. In the previous versions, this setting is hard-coded as 102400.

Valid values range from 10240 through **MAX\_DWORD**. The default value is 102400.

</dd> <dt>

<span id="_WindowsCurrentVersionUPnPFile_Size_Limit"></span><span id="_windowscurrentversionupnpfile_size_limit"></span><span id="_WINDOWSCURRENTVERSIONUPNPFILE_SIZE_LIMIT"></span>\\**Windows**\\**CurrentVersion**\\**UPnP**\\**File Size Limit**
</dt> <dd>

Specifies the maximum size, in bytes, of the SOAP response that is acceptable. This setting is not configurable in versions of Windows preceding Windows XP Service Pack 2. In the previous versions, this setting is hard-coded as 102400.

Valid values range from 10240 through **MAX\_DWORD**. The default value is 102400.

</dd> <dt>

<span id="MaxCache"></span><span id="maxcache"></span><span id="MAXCACHE"></span>**MaxCache**
</dt> <dd>

Specifies the maximum number of entries allowed in the Simple Service Discovery Protocol (SSDP) cache.

Valid values range from 10 through 30000. The default value is 1000.

</dd> <dt>

<span id="TTL"></span><span id="ttl"></span>**TTL**
</dt> <dd>

Specifies the time-to-live for an SSDP packet. That is, **TTL** specifies the number of hops allowed for a packet.

Valid values range from 1 through 255. The default value is 1.

</dd> <dt>

<span id="ReceiveScope"></span><span id="receivescope"></span><span id="RECEIVESCOPE"></span>**ReceiveScope**
</dt> <dd>

Specifies which IP addresses are valid sources of a message. If an incoming message originates from an address that is not within the scope specified by **ReceiveScope**, the message is ignored. This setting is not configurable in versions of Windows preceding Windows XP Service Pack 2. In the previous versions, a message is accepted without regard to its source.

The valid values are shown in the following table. The default value is 1.



| Value of **ReceiveScope** | Meaning                                                                                                                                                                                                      |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0                         | Sender's IP address must be a subnet address.                                                                                                                                                                |
| 1                         | Sender's IP address must be a subnet address or a private address which is one of 10.*x*.*x*.*x*, 192.168.*x*.*x*, 172.16.*x*.*x* (as specified by RFC 1918), or 169.254.*x*.*x* (as specified by RFC 3330). |
| 2                         | Not used. If **ReceiveScope** is set to 2, the default value is used.                                                                                                                                        |
| 3                         | Sender's IP address can be any address.                                                                                                                                                                      |



 

</dd> </dl>

## Related topics

<dl> <dt>

[Overview of UPnP Architecture](overview-of-universal-plug-and-play.md)
</dt> </dl>

 

 




