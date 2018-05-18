---
title: MSFC\_FibrePortHBAAttributes structure
description: A WMI provider uses the MSFC\_FibrePortHBAAttributes WMI class to expose attribute information associated with a fibre channel port.
ms.assetid: 'e8a31f48-bad2-49d1-81be-d345d87a0fd5'
keywords: ["MSFC_FibrePortHBAAttributes structure Storage Devices", "PMSFC_FibrePortHBAAttributes structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- MSFC_FibrePortHBAAttributes
api_location:
- hbapiwmi.h
api_type:
- HeaderDef
---

# MSFC\_FibrePortHBAAttributes structure

A WMI provider uses the MSFC\_FibrePortHBAAttributes WMI class to expose attribute information associated with a fibre channel port.

## Syntax


```C++
typedef struct _MSFC_FibrePortHBAAttributes {
  ULONGLONG                     UniquePortId;
  ULONG                         HBAStatus;
  MSFC_HBAPortAttributesResults Attributes;
} MSFC_FibrePortHBAAttributes, *PMSFC_FibrePortHBAAttributes;
```



## Members

<dl> <dt>

**UniquePortId**
</dt> <dd>

Unique identifier for the port. This identifier must be unique among all ports on all adapters. The same value for the identifier must be used for the same port in other classes that expose port information.

</dd> <dt>

**HBAStatus**
</dt> <dd>

Contains the status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233).

</dd> <dt>

**Attributes**
</dt> <dd>

Contains a structure of type [**MSFC\_HBAPortAttributesResults**](msfc-hbaportattributesresults.md) that contains information about the port attributes.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbapiwmi.h (include Hbapiwmi.h)</dt> </dl> |



## See also

<dl> <dt>

[HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233)
</dt> <dt>

[**MSFC\_HBAPortAttributesResults**](msfc-hbaportattributesresults.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MSFC_FibrePortHBAAttributes%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






