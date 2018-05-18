---
Description: 'The IPrintOemUni::DevMode method, provided by rendering plug-ins for Unidrv, performs operations on private DEVMODEW members.'
ms.assetid: 'df6bde70-ba14-411b-88a1-b45f2e2756ef'
title: 'IPrintOemUni::DevMode method'
---

# IPrintOemUni::DevMode method

The `IPrintOemUni::DevMode` method, provided by rendering plug-ins for Unidrv, performs operations on private [**DEVMODEW**](display.devmodew) members.

## Syntax


```C++
STDMETHOD DevMode(
   DWORD       dwMode,
   POEMDMPARAM pOemDMParam
);
```



## Parameters

<dl> <dt>

*dwMode* 
</dt> <dd>

Specifies a caller-supplied constant. See the Remarks section for more information.

</dd> <dt>

*pOemDMParam* 
</dt> <dd>

Caller-supplied pointer to an [**OEMDMPARAM**](oemdmparam.md) structure.

</dd> </dl>

## Return value

The method must return one of the following values.



| Return code                                                                            | Description                         |
|----------------------------------------------------------------------------------------|-------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>   | The operation succeeded.<br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl> | The operation failed<br/>     |



 

## Remarks

A rendering plug-in for Unidrv must implement the `IPrintOemUni::DevMode` method.

If you are providing a user interface plug-in for Unidrv, and if you are adding private members to the driver's [**DEVMODEW**](display.devmodew) structure, you must implement both the `IPrintOemUI::DevMode` and the `IPrintOemUni::DevMode` methods. The code implementing these methods must be identical and can be placed in a library that is statically linked to both the UI plug-in and the rendering plug-in.

The `IPrintOemUni::DevMode` method must perform the operation indicated by its *dwMode* value. Each time `IPrintOemUni::DevMode` is called, *dwMode* contains one of the following constants, which are listed in the order they are received:

<dl> <dt>

<span id="OEMDM_SIZE"></span><span id="oemdm_size"></span>OEMDM\_SIZE
</dt> <dd>

Indicates that the `IPrintOemUni::DevMode` method should return the size of the memory allocation needed to store the render plug-in's private DEVMODEW members. This constant is set the first time the method is called. The method should place the number of bytes needed in the [**OEMDMPARAM**](oemdmparam.md) structure's **cbBufSize** member.

The printer driver DLL allocates the specified amount of memory and passes its address to the rendering plug-in in subsequent calls to `IPrintOemUni::DevMode`.

</dd> <dt>

<span id="OEMDM_DEFAULT"></span><span id="oemdm_default"></span>OEMDM\_DEFAULT
</dt> <dd>

Indicates that the `IPrintOemUni::DevMode` method should fill the private DEVMODEW members with their default values. For this operation, the [**OEMDMPARAM**](oemdmparam.md) structure's **pOEMDMOut** and **cbBufSize** members contain the address and size of the area that has been allocated for storage of private DEVMODEW members. The method should write the private DEVMODEW default values into the buffer pointed to by the **pOEMDMOut** member, and return the number of bytes written by placing it in the **cbBufSize** member.

</dd> <dt>

<span id="OEMDM_CONVERT"></span><span id="oemdm_convert"></span>OEMDM\_CONVERT
</dt> <dd>

Indicates the `IPrintOemUni::DevMode` method should convert private DEVMODEW members to the current version, if necessary. (EMF spooling can occur over a network, and the system that spooled the EMF records might be running an older or newer version of the printer driver or user interface plug-in.) A private DEVMODEW section's version number is contained in its [**OEM\_DMEXTRAHEADER**](oem-dmextraheader.md) structure.

The public and private members of the DEVMODEW structure to be converted are pointed to by the [**OEMDMPARAM**](oemdmparam.md) structure's **pPublicDMIn** and **pOEMDMIn** members. The `IPrintOemUni::DevMode` method should place converted private members in the memory space described by the structure's **pOEMDMOut** and **cbBufSize** members, and it should return the count of written bytes by placing it in the structure's **cbBufSize** member. The value returned in **cbBufSize** cannot be larger than the value received.

</dd> <dt>

<span id="OEMDM_MERGE"></span><span id="oemdm_merge"></span>OEMDM\_MERGE
</dt> <dd>

Indicates that the `IPrintOemUni::DevMode` method should validate the information contained in private DEVMODEW members and merge validated values into a private DEVMODEW structure containing default values. For this constant, the method receives the following DEVMODEW contents:

-   The [**OEMDMPARAM**](oemdmparam.md) structure's **pPublicDMIn** and **pOEMDMIn** members point to the public and private members of the DEVMODEW structure to be validated.

-   The [**OEMDMPARAM**](oemdmparam.md) structure's **pPublicDMOut** and **pOEMDMOut** members point to current default DEVMODEW values (obtained from property sheet contents).

The method should validate the contents of each private DEVMODEW member pointed to by *pOEMDMIn*. Each valid value should be copied to the output buffer pointed to by *pOEMDMOut*, overwriting the default. For invalid input values, the default output value should not be modified. (Finding invalid values is not considered an error, so the method should return S\_OK.)

</dd> </dl>

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPrintOemUni**](iprintoemuni-interface.md)
</dt> <dt>

[**IPrintOemUI::DevMode**](iprintoemui-devmode.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemUni::DevMode%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





