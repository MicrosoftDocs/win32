---
title: BcdDeviceObjectElementTypes enumeration
description: Specifies the device object element types.
ms.assetid: 70851efa-5797-4084-b994-1f5f94b26e90
keywords:
- BcdDeviceObjectElementTypes enumeration Boot Config
topic_type:
- apiref
api_name:
- BcdDeviceObjectElementTypes
api_type:
- NA
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# BcdDeviceObjectElementTypes enumeration

Specifies the device object element types.

## Syntax


```C++
typedef enum BcdDeviceObjectElementTypes { 
  BcdDeviceInteger_RamdiskImageOffset            = 0x35000001,
  BcdDeviceInteger_TftpClientPort                = 0x35000002,
  BcdDeviceInteger_SdiDevice                     = 0x31000003,
  BcdDeviceInteger_SdiPath                       = 0x32000004,
  BcdDeviceInteger_RamdiskImageLength            = 0x35000005,
  BcdDeviceBoolean_RamdiskExportAsCd             = 0x36000006,
  BcdDeviceInteger_RamdiskTftpBlockSize          = 0x36000007,
  BcdDeviceInteger_RamdiskTftpWindowSize         = 0x36000008,
  BcdDeviceBoolean_RamdiskMulticastEnabled       = 0x36000009,
  BcdDeviceBoolean_RamdiskMulticastTftpFallback  = 0x3600000A,
  BcdDeviceBoolean_RamdiskTftpVarWindow          = 0x3600000B
} BcdDeviceObjectElementTypes;
```



## Constants

<dl> <dt>

<span id="BcdDeviceInteger_RamdiskImageOffset"></span><span id="bcddeviceinteger_ramdiskimageoffset"></span><span id="BCDDEVICEINTEGER_RAMDISKIMAGEOFFSET"></span>**BcdDeviceInteger\_RamdiskImageOffset**
</dt> <dd>

The RAM disk image offset. The element data format is [**BcdIntegerElement**](bcdintegerelement.md).

</dd> <dt>

<span id="BcdDeviceInteger_TftpClientPort"></span><span id="bcddeviceinteger_tftpclientport"></span><span id="BCDDEVICEINTEGER_TFTPCLIENTPORT"></span>**BcdDeviceInteger\_TftpClientPort**
</dt> <dd>

The IP port number to be used for Trivial File Transfer Protocol (TFTP) reads. The element data format is [**BcdIntegerElement**](bcdintegerelement.md).

If this value is not specified, the default TFTP protocol port is used.

</dd> <dt>

<span id="BcdDeviceInteger_SdiDevice"></span><span id="bcddeviceinteger_sdidevice"></span><span id="BCDDEVICEINTEGER_SDIDEVICE"></span>**BcdDeviceInteger\_SdiDevice**
</dt> <dd>

The device that contains the SDI object. The element data format is [**BcdDeviceElement**](bcddeviceelement.md).

</dd> <dt>

<span id="BcdDeviceInteger_SdiPath"></span><span id="bcddeviceinteger_sdipath"></span><span id="BCDDEVICEINTEGER_SDIPATH"></span>**BcdDeviceInteger\_SdiPath**
</dt> <dd>

The path from the root of the SDI device to the RAM disk file. The element data format is [**BcdStringElement**](bcdstringelement.md).

</dd> <dt>

<span id="BcdDeviceInteger_RamdiskImageLength"></span><span id="bcddeviceinteger_ramdiskimagelength"></span><span id="BCDDEVICEINTEGER_RAMDISKIMAGELENGTH"></span>**BcdDeviceInteger\_RamdiskImageLength**
</dt> <dd>

The length of the image for the RAM disk. The element data format is [**BcdIntegerElement**](bcdintegerelement.md).

</dd> <dt>

<span id="BcdDeviceBoolean_RamdiskExportAsCd"></span><span id="bcddeviceboolean_ramdiskexportascd"></span><span id="BCDDEVICEBOOLEAN_RAMDISKEXPORTASCD"></span>**BcdDeviceBoolean\_RamdiskExportAsCd**
</dt> <dd>

Enables exporting the RAM disk as a CD. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

</dd> <dt>

<span id="BcdDeviceInteger_RamdiskTftpBlockSize"></span><span id="bcddeviceinteger_ramdisktftpblocksize"></span><span id="BCDDEVICEINTEGER_RAMDISKTFTPBLOCKSIZE"></span>**BcdDeviceInteger\_RamdiskTftpBlockSize**
</dt> <dd>

Defines the TFTP block size for the RAM disk Windows Imaging (WIM) file. The element data format is [**BcdIntegerElement**](bcdintegerelement.md).

</dd> <dt>

<span id="BcdDeviceInteger_RamdiskTftpWindowSize"></span><span id="bcddeviceinteger_ramdisktftpwindowsize"></span><span id="BCDDEVICEINTEGER_RAMDISKTFTPWINDOWSIZE"></span>**BcdDeviceInteger\_RamdiskTftpWindowSize**
</dt> <dd>

Defines the TFTP window size for the RAM disk WIM file. The element data format is [**BcdIntegerElement**](bcdintegerelement.md).

</dd> <dt>

<span id="BcdDeviceBoolean_RamdiskMulticastEnabled"></span><span id="bcddeviceboolean_ramdiskmulticastenabled"></span><span id="BCDDEVICEBOOLEAN_RAMDISKMULTICASTENABLED"></span>**BcdDeviceBoolean\_RamdiskMulticastEnabled**
</dt> <dd>

Enables or disables multicast for the RAM disk WIM file. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

</dd> <dt>

<span id="BcdDeviceBoolean_RamdiskMulticastTftpFallback"></span><span id="bcddeviceboolean_ramdiskmulticasttftpfallback"></span><span id="BCDDEVICEBOOLEAN_RAMDISKMULTICASTTFTPFALLBACK"></span>**BcdDeviceBoolean\_RamdiskMulticastTftpFallback**
</dt> <dd>

Enables fallback to TFTP if multicast fails. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

</dd> <dt>

<span id="BcdDeviceBoolean_RamdiskTftpVarWindow"></span><span id="bcddeviceboolean_ramdisktftpvarwindow"></span><span id="BCDDEVICEBOOLEAN_RAMDISKTFTPVARWINDOW"></span>**BcdDeviceBoolean\_RamdiskTftpVarWindow**
</dt> <dd>

Enables or disables the TFTP variable window size extension. The element data format is [**BcdBooleanElement**](bcdbooleanelement.md).

**Note**  This value is supported starting in Windows 8 and Windows Server 2012.

</dd> </dl>

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[BCD WMI Provider Enumerations](bcd-enumerations.md)
</dt> <dt>

[**BcdIntegerElement**](bcdintegerelement.md)
</dt> <dt>

[**BcdStringElement**](bcdstringelement.md)
</dt> <dt>

[**GetElement**](getelement-bcdobject.md)
</dt> <dt>

[**BcdElementType**](bcdelementtype.md)
</dt> </dl>

 

 





