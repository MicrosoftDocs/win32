---
title: Rational object
description: Holds the rational values found in Exchangeable Image File (EXIF) tags. It is a supported element type of the Vector object and can be created using \ 0034;WIA.Rational \ 0034; as the ProgID in a call to CreateObject. The Rational object is a container.
ms.assetid: 71d8ebe8-7098-4995-b4e2-a16da582b9d8
keywords:
- Rational object WIA Automation
- Rational object WIA Automation , described
topic_type:
- apiref
api_name:
- Rational
api_location:
- Wiaaut.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# Rational object

Holds the rational values found in Exchangeable Image File (EXIF) tags. It is a supported element type of the [**Vector**](-wiaaut-vector.md) object and can be created using "WIA.Rational" as the ProgID in a call to [CreateObject](http://msdn.microsoft.com/library/7t9k08y5(VS.71).aspx). The **Rational** object is a container.

## Members

The **Rational** object has these types of members:

-   [Properties](#properties)

### Properties

The **Rational** object has these properties.



| Property                                                        | Access type           | Description                                                                                               |
|:----------------------------------------------------------------|:----------------------|:----------------------------------------------------------------------------------------------------------|
| [**Denominator**](-wiaaut-irational-denominator.md)<br/> | Read/write<br/> | Sets or retrieves the **Rational** value [**Denominator**](-wiaaut-irational-denominator.md).<br/> |
| [**Numerator**](-wiaaut-irational-numerator.md)<br/>     | Read/write<br/> | Sets or retrieves the **Rational** value [**Numerator**](-wiaaut-irational-numerator.md).<br/>     |
| [**Value (Rational)**](-wiaaut-irational-value.md)<br/>  | Read-only<br/>  | Retrieves the **Rational** value as a **Double**.<br/>                                              |



 

## Remarks

Note that the [**Value (Rational)**](-wiaaut-irational-value.md) property is read-only. This is because there can be more than one way to represent a rational value as a floating point number. To set the value of a **Rational** object, you must set its [**Numerator**](-wiaaut-irational-numerator.md) and [**Denominator**](-wiaaut-irational-denominator.md) separately.

For example code, see [Set Rational Numerator and Denominator](https://www.bing.com/search?q=Set Rational Numerator and Denominator) in Shared Samples.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**Denominator**](-wiaaut-irational-denominator.md)
</dt> <dt>

[**Numerator**](-wiaaut-irational-numerator.md)
</dt> <dt>

[**Value (Rational)**](-wiaaut-irational-value.md)
</dt> </dl>

 

 





