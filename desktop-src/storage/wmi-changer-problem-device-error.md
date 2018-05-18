---
title: WMI\_CHANGER\_PROBLEM\_DEVICE\_ERROR structure
description: When the ChangerPerformDiagnostics routine performs diagnostic tests on a changer device it returns the results in a WMI\_CHANGER\_PROBLEM\_DEVICE\_ERROR structure.
ms.assetid: 'c2c0f2eb-cb35-4f23-beb6-7f0eaeda845a'
keywords: ["WMI_CHANGER_PROBLEM_DEVICE_ERROR structure Storage Devices", "PWMI_CHANGER_PROBLEM_DEVICE_ERROR structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- WMI_CHANGER_PROBLEM_DEVICE_ERROR
api_location:
- wmidata.h
api_type:
- HeaderDef
---

# WMI\_CHANGER\_PROBLEM\_DEVICE\_ERROR structure

When the [**ChangerPerformDiagnostics**](changerperformdiagnostics.md) routine performs diagnostic tests on a changer device it returns the results in a WMI\_CHANGER\_PROBLEM\_DEVICE\_ERROR structure.

## Syntax


```C++
typedef struct _WMI_CHANGER_PROBLEM_DEVICE_ERROR {
  ULONG ChangerProblemType;
} WMI_CHANGER_PROBLEM_DEVICE_ERROR, *PWMI_CHANGER_PROBLEM_DEVICE_ERROR;
```



## Members

<dl> <dt>

**ChangerProblemType**
</dt> <dd>

Contains one of the enumeration values defined for the [**CHANGER\_DEVICE\_PROBLEM\_TYPE**](changer-device-problem-type.md) enumeration data type. The minidriver sets **ChangerProblemType** to the appropriate enumerator value.

</dd> </dl>

## Requirements



|                   |                                                                                      |
|-------------------|--------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmidata.h</dt> </dl> |



## See also

<dl> <dt>

[**ChangerPerformDiagnostics**](changerperformdiagnostics.md)
</dt> <dt>

[**CHANGER\_DEVICE\_PROBLEM\_TYPE**](changer-device-problem-type.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20WMI_CHANGER_PROBLEM_DEVICE_ERROR%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






