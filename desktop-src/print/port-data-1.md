---
Description: The XcvData function uses a PORT\_DATA\_1 structure when it adds a port or configures an existing port.
ms.assetid: d4fb5bf9-7982-4abd-91ba-59b7798a18c7
title: PORT\_DATA\_1 structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# PORT\_DATA\_1 structure

The [**XcvData**](https://www.bing.com/search?q=**XcvData**) function uses a PORT\_DATA\_1 structure when it adds a port or configures an existing port.

## Syntax


```C++
typedef struct _PORT_DATA_1 {
  WCHAR sztPortName[MAX_PORTNAME_LEN];
  DWORD dwVersion;
  DWORD dwProtocol;
  DWORD cbSize;
  DWORD dwReserved;
  WCHAR sztHostAddress[MAX_NETWORKNAME_LEN];
  WCHAR sztSNMPCommunity[MAX_SNMP_COMMUNITY_STR_LEN];
  DWORD dwDoubleSpool;
  WCHAR sztQueue[MAX_QUEUENAME_LEN];
  WCHAR sztIPAddress[MAX_IPADDR_STR_LEN];
  BYTE  Reserved[540];
  DWORD dwPortNumber;
  DWORD dwSNMPEnabled;
  DWORD dwSNMPDevIndex;
} PORT_DATA_1, *PPORT_DATA_1;
```



## Members

<dl> <dt>

**sztPortName**
</dt> <dd>

Specifies the name of the port. The MAX\_PORTNAME\_LEN constant is defined in tcpxcv.h.

</dd> <dt>

**dwVersion**
</dt> <dd>

Specifies the version number of the PORT\_DATA\_1 structure, which is currently 1.

</dd> <dt>

**dwProtocol**
</dt> <dd>

Specifies the protocol to use for the port. This value can be either PROTOCOL\_RAWTCP\_TYPE or PROTOCOL\_LPR\_TYPE, constants that are defined in tcpxcv.h.

</dd> <dt>

**cbSize**
</dt> <dd>

Specifies the size, in bytes of this structure. Use **sizeof**(PORT\_DATA\_1) for this value.

</dd> <dt>

**dwReserved**
</dt> <dd>

Reserved, must be set to zero.

</dd> <dt>

**sztHostAddress**
</dt> <dd>

Specifies the IP Address or host name of the printer. The MAX\_NETWORKNAME\_LEN constant is defined in tcpxcv.h.

</dd> <dt>

**sztSNMPCommunity**
</dt> <dd>

Specifies the SNMP community name of the printer. The MAX\_SNMP\_COMMUNITY\_STR\_LEN constant is defined in tcpxcv.h.

</dd> <dt>

**dwDoubleSpool**
</dt> <dd>

If **TRUE**, indicates that double spooling is enabled. If **FALSE**, double spooling is disabled.

</dd> <dt>

**sztQueue**
</dt> <dd>

Specifies the LPR queue name. The MAX\_QUEUENAME\_LEN constant is defined in tcpxcv.h.

</dd> <dt>

**sztIPAddress**
</dt> <dd>

Specifies the IP address of the printer. The MAX\_IPADDR\_STR\_LEN constant is defined in tcpxcv.h.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved, must be set to zero.

</dd> <dt>

**dwPortNumber**
</dt> <dd>

Specifies the port number of the device.

</dd> <dt>

**dwSNMPEnabled**
</dt> <dd>

If **TRUE**, indicates that the device supports Simple Network Management Protocol (SNMP).

</dd> <dt>

**dwSNMPDevIndex**
</dt> <dd>

Specifies the SNMP device index.

</dd> </dl>

## Remarks

When the [**XcvData**](https://www.bing.com/search?q=**XcvData**) function is called either to add a port or configure an existing port, its *pOutputData* parameter must be set with the address of a PORT\_DATA\_1 structure, which will be filled in when the function returns. To add a port, set this function's *pszDataName* parameter to the string L"AddPort". To configure a port, set this parameter to L"ConfigPort".

See [TCPMON Xcv Interface](https://www.bing.com/search?q=TCPMON+Xcv+Interface) for more information.

## Requirements



|                   |                                                                                                        |
|-------------------|--------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Tcpxcv.h (include Tcpxcv.h)</dt> </dl> |



## See also

<dl> <dt>

[**XcvData**](https://www.bing.com/search?q=**XcvData**)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20PORT_DATA_1%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





