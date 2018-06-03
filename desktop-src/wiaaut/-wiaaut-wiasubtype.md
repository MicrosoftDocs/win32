---
title: WiaSubType enumeration
description: Specifies more detail about the property value. Use the SubType property on the Property object to obtain these details for the property.
ms.assetid: c259b2f8-fa2a-4913-b6c5-6a1b56f2f079
keywords:
- WiaSubType enumeration WIA Automation
- WiaDeviceType enumeration WIA Automation
topic_type:
- apiref
api_name:
- WiaDeviceType
api_location:
- Wiaaut.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# WiaSubType enumeration

Specifies more detail about the property value. Use the [**SubType**](-wiaaut-iproperty-subtype.md) property on the [**Property**](-wiaaut-property.md) object to obtain these details for the property.

## Members



| Member                 | Description                                                                                                                                                                                                                        | Value |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|
| **UnspecifiedSubType** | This property has no subtype.<br/>                                                                                                                                                                                           | 0     |
| **RangeSubType**       | This property takes a range of values from [**SubTypeMin**](-wiaaut-iproperty-subtypemin.md) to [**SubTypeMax**](-wiaaut-iproperty-subtypemax.md) in [**SubTypeStep**](-wiaaut-iproperty-subtypestep.md) increments.<br/> | 1     |
| **ListSubType**        | This property takes one of a list of values from [**SubTypeValues**](-wiaaut-iproperty-subtypevalues.md).<br/>                                                                                                              | 2     |
| **FlagSubType**        | This property takes a flag composed of bits listed in [**SubTypeValues**](-wiaaut-iproperty-subtypevalues.md). Flag values are combined using the OR operation.<br/>                                                        | 3     |



## Remarks

The value of the [**SubType**](-wiaaut-iproperty-subtype.md) property on a [**Property**](-wiaaut-property.md) object can return one of the members of the **WiaSubType** enumeration. This enumeration provides more information about the valid values for the property.

For example code, see [Display Detailed Property Information](https://www.bing.com/search?q=Display Detailed Property Information) in Shared Samples.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



 

 





