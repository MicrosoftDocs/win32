---
title: WmsCustomPresenterErrorCode enumeration
description: Defines error codes returned by OnError methods of the MultiPoint Services Interfaces.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4b65a5a3-1083-440c-b7cb-bc72757d8f89
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- WmsCustomPresenterErrorCode enumeration
topic_type:
- apiref
api_name:
- WmsCustomPresenterErrorCode
api_location:
- WmsStationPresenter.idl
api_type:
- IDLDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
---

# WmsCustomPresenterErrorCode enumeration

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Defines error codes returned by **OnError** methods of the [MultiPoint Services Interfaces](multipoint-interfaces.md).

## Syntax


```C++
typedef enum  { 
  CustomPresenterNone          = 0x0000,
  PresentationDeviceTooNarrow  = 0x0001,
  PresentationDeviceTooShort   = 0x0002,
  StationPresenterNotSupplied  = 0x0003,
  MousePresenterNotSupplied    = 0x0004,
  PresenterTooBig              = 0x0005
} WmsCustomPresenterErrorCode;
```



## Constants

<dl> <dt>

<span id="CustomPresenterNone"></span><span id="custompresenternone"></span><span id="CUSTOMPRESENTERNONE"></span>**CustomPresenterNone**
</dt> <dd>

A custom input device was not specified.

</dd> <dt>

<span id="PresentationDeviceTooNarrow"></span><span id="presentationdevicetoonarrow"></span><span id="PRESENTATIONDEVICETOONARROW"></span>**PresentationDeviceTooNarrow**
</dt> <dd>

The screen is to narrow.

</dd> <dt>

<span id="PresentationDeviceTooShort"></span><span id="presentationdevicetooshort"></span><span id="PRESENTATIONDEVICETOOSHORT"></span>**PresentationDeviceTooShort**
</dt> <dd>

The screen is too short.

</dd> <dt>

<span id="StationPresenterNotSupplied"></span><span id="stationpresenternotsupplied"></span><span id="STATIONPRESENTERNOTSUPPLIED"></span>**StationPresenterNotSupplied**
</dt> <dd>

An input device isn't specified.

</dd> <dt>

<span id="MousePresenterNotSupplied"></span><span id="mousepresenternotsupplied"></span><span id="MOUSEPRESENTERNOTSUPPLIED"></span>**MousePresenterNotSupplied**
</dt> <dd>

A mouse isn't specified.

</dd> <dt>

<span id="PresenterTooBig"></span><span id="presentertoobig"></span><span id="PRESENTERTOOBIG"></span>**PresenterTooBig**
</dt> <dd>

The dimensions of the frame buffer for the input device are too big.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| IDL<br/>                      | <dl> <dt>WmsStationPresenter.idl</dt> </dl> |



## See also

<dl> <dt>

[MultiPoint Services Enumerations](multipoint-enumerations.md)
</dt> </dl>

 

 





