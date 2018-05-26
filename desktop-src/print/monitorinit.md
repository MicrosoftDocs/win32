---
Description: The MONITORINIT structure is used as an input parameter to a print monitors InitializePrintMonitor2 function.
ms.assetid: 3445997f-a607-4071-b05e-c1a8d01892b2
title: MONITORINIT structure
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MONITORINIT structure

The MONITORINIT structure is used as an input parameter to a print monitor's [**InitializePrintMonitor2**](initializeprintmonitor2.md) function.

## Syntax


```C++
typedef struct _MONITORINIT {
  DWORD       cbSize;
  HANDLE      hSpooler;
  HKEYMONITOR hckRegistryRoot;
  PMONITORREG pMonitorReg;
  BOOL        bLocal;
  LPCWSTR     pszServerName;
} MONITORINIT, *PMONITORINIT;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

Size, in bytes, of the MONITORINIT structure.

</dd> <dt>

**hSpooler**
</dt> <dd>

Spooler handle, for use as input to functions identified by the MONITORREG structure.

</dd> <dt>

**hckRegistryRoot**
</dt> <dd>

Registry handle, for use as input to functions identified by the MONITORREG structure.

</dd> <dt>

**pMonitorReg**
</dt> <dd>

Pointer to a [**MONITORREG**](monitorreg.md) structure.

</dd> <dt>

**bLocal**
</dt> <dd>

**TRUE** if the monitor is being called by a local node spooler. **FALSE** if the monitor is being called by a cluster spooler. (Monitors can usually ignore this member.)

</dd> <dt>

**pszServerName**
</dt> <dd>

Caller-supplied pointer to a string representing a server name.

</dd> </dl>

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Winsplp.h (include Winsplp.h)</dt> </dl> |



## See also

<dl> <dt>

[**InitializePrintMonitor2**](initializeprintmonitor2.md)
</dt> <dt>

[**MONITORREG**](monitorreg.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20MONITORINIT%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





