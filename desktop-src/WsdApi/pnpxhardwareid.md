---
description: Specifies the PnP-X Hardware Identifier of the service.
ms.assetid: aa4c935f-0d60-4603-ae96-d5cabdf9af00
title: PnPXHardwareId element
ms.topic: reference
ms.date: 05/31/2018
---

# PnPXHardwareId element

Specifies the PnP-X Hardware Identifier of the service. PnP matches this element with the hardware description(s) provided in the \[PnpxDevice\] section of the device's INF file. Based on this information, the PnP service selects and loads the most appropriate device driver.

## Usage

``` syntax
<PnPXHardwareId/>
```

## Attributes

There are no attributes.

## Child elements

There are no child elements.

## Parent elements



| Element                             | Description                                                                            |
|-------------------------------------|----------------------------------------------------------------------------------------|
| [**hosted**](hosted.md)<br/> | Defines elements for the services defined by the service host. <br/> <br/> |



## Remarks

To specify more than one hardware ID, separate the identifiers with a space character, for example, "PnPX\_SampleService\_HWID\_1 PnPX\_SampleService\_HWID\_2 PnPX\_SampleService1\_HWID\_3".

## Element information



| Label | Value |
|-------------------------------------|---------------|
| Minimum supported system<br/> | Windows Vista |
| Can be empty                        | Yes           |



 

 




