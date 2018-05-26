---
Description: The XcvData function uses a CONFIG\_INFO\_DATA\_1 structure when it obtains configuration data for a particular port.
ms.assetid: abf484e4-6a11-4727-b195-5eaf6683113e
title: CONFIG\_INFO\_DATA\_1 structure
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CONFIG\_INFO\_DATA\_1 structure

The [**XcvData**](print.xcvdata) function uses a CONFIG\_INFO\_DATA\_1 structure when it obtains configuration data for a particular port.

## Syntax


```C++
typedef struct _CONFIG_INFO_DATA_1 {
  BYTE  Reserved[128];
  DWORD dwVersion;
} CONFIG_INFO_DATA_1, *PCONFIG_INFO_DATA_1;
```



## Members

<dl> <dt>

**Reserved**
</dt> <dd>

Is reserved for system use. This member should be set to a zero-length string.

</dd> <dt>

**dwVersion**
</dt> <dd>

Specifies the version of the PORT\_DATA\_1 structure (currently equal to 1) that will contain the configuration information.

</dd> </dl>

## Remarks

When the [**XcvData**](print.xcvdata) function is called to obtain port configuration information, its *pInputData* parameter must be set with the address of a CONFIG\_INFO\_DATA\_1 structure, and its *pOutputData* parameter must be set with the address of a [**PORT\_DATA\_1**](port-data-1.md) structure, which will be filled in when the function returns. Set this function's *pszDataName* parameter to the string L"GetConfigInfo".

See [TCPMON Xcv Interface](print.tcpmon_xcv_interface) for more information.

## Requirements



|                   |                                                                                                        |
|-------------------|--------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Tcpxcv.h (include Tcpxcv.h)</dt> </dl> |



## See also

<dl> <dt>

[**XcvData**](print.xcvdata)
</dt> <dt>

[**PORT\_DATA\_1**](port-data-1.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20CONFIG_INFO_DATA_1%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





