---
title: CHANGER\_INITIALIZE\_ELEMENT\_STATUS structure
description: The CHANGER\_INITIALIZE\_ELEMENT\_STATUS structure is used in conjunction with the IOCTL\_CHANGER\_INITIALIZE\_ELEMENT\_STATUS request to initialize the status of all elements or of a specified number of elements of a particular type.
ms.assetid: fd26a97d-cbea-4ab4-b54e-1831d6e3a8ed
keywords:
- CHANGER_INITIALIZE_ELEMENT_STATUS structure Storage Devices
- PCHANGER_INITIALIZE_ELEMENT_STATUS structure pointer Storage Devices
topic_type:
- apiref
api_name:
- CHANGER_INITIALIZE_ELEMENT_STATUS
api_location:
- ntddchgr.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CHANGER\_INITIALIZE\_ELEMENT\_STATUS structure

The CHANGER\_INITIALIZE\_ELEMENT\_STATUS structure is used in conjunction with the [**IOCTL\_CHANGER\_INITIALIZE\_ELEMENT\_STATUS**](ioctl-changer-initialize-element-status.md) request to initialize the status of all elements or of a specified number of elements of a particular type.

## Syntax


```C++
typedef struct _CHANGER_INITIALIZE_ELEMENT_STATUS {
  CHANGER_ELEMENT_LIST ElementList;
  BOOLEAN              BarCodeScan;
} CHANGER_INITIALIZE_ELEMENT_STATUS, *PCHANGER_INITIALIZE_ELEMENT_STATUS;
```



## Members

<dl> <dt>

**ElementList**
</dt> <dd>

Contains a structure of type [**CHANGER\_ELEMENT\_LIST**](changer-element-list.md) that specifies the element type and the number of elements. If the **Features0** member of the [**GET\_CHANGER\_PARAMETERS**](get-changer-parameters.md) structure is set to CHANGER\_INIT\_ELEM\_STAT\_WITH\_RANGE, the changer supports initializing a range of elements. In this case, the element type can be **ChangerTransport**, **ChangerSlot**, **ChangerDrive**, or **ChangerIEPort** and **ElementList** can specify a number of elements to initialize. Otherwise, the element type must be **AllElements** and the number of elements is ignored.

</dd> <dt>

**BarCodeScan**
</dt> <dd>

Instructs the changer driver, when **TRUE**, to initialize elements by scanning bar codes. When **FALSE**, the changer driver takes no action. This member is applicable only if the **Features0** member of GET\_CHANGER\_PARAMETERS is set to CHANGER\_BAR\_CODE\_SCANNER\_INSTALLED. If the changer has nonvolatile RAM, a bar code scan can serve as an optimization.

</dd> </dl>

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddchgr.h</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_CHANGER\_INITIALIZE\_ELEMENT\_STATUS**](ioctl-changer-initialize-element-status.md)
</dt> <dt>

[**ChangerInitializeElementStatus**](changerinitializeelementstatus.md)
</dt> <dt>

[**GET\_CHANGER\_PARAMETERS**](get-changer-parameters.md)
</dt> <dt>

[**CHANGER\_ELEMENT\_LIST**](changer-element-list.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20CHANGER_INITIALIZE_ELEMENT_STATUS%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






