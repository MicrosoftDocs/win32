---
Description: The UNIDRV\_PRIVATE\_DEVMODE structure enables Unidrv plug-ins to determine the size of the private portion of Unidrvs DEVMODEW structure.
ms.assetid: 91b8ba63-5276-43f8-81a6-07afc1a77ced
title: UNIDRV\_PRIVATE\_DEVMODE structure
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# UNIDRV\_PRIVATE\_DEVMODE structure

The UNIDRV\_PRIVATE\_DEVMODE structure enables Unidrv plug-ins to determine the size of the private portion of Unidrv's DEVMODEW structure.

## Syntax


```C++
typedef struct _UNIDRV_PRIVATE_DEVMODE {
  WORD wReserved[4];
  WORD wSize;
} UNIDRV_PRIVATE_DEVMODE, *PUNIDRV_PRIVATE_DEVMODE;
```



## Members

<dl> <dt>

**wReserved**
</dt> <dd>

Reserved for system use.

</dd> <dt>

**wSize**
</dt> <dd>

The size, in bytes, of the private portion of Unidrv's [**DEVMODEW**](display.devmodew) structure.

</dd> </dl>

## Remarks

This structure and associated macro are available in Windows 2000 and later. For information about the public and private sections of the DEVMODEW structure, see [The DEVMODEW Structure](display.the_devmodew_structure).

Printoem.h defines a macro for determining the size of the private portion of Unidrv's DEVMODEW structure.


```
#define GET_UNIDRV_PRIVATE_DEVMODE_SIZE(pdm)\
( ( (pdm)->dmDriverExtra > (FIELD_OFFSET(UNIDRV_PRIVATE_DEVMODE, wSize) + sizeof(WORD)) ) ? \
((PUNIDRV_PRIVATE_DEVMODE)((PBYTE)(pdm) + (pdm)-> dmSize)) -> wSize : 0 )
```



The pdm argument in the **GET\_UNIDRV\_PRIVATE\_DEVMODE\_SIZE** macro is a pointer to a DEVMODEW structure. The macro determines whether the value of the **dmDriverExtra** member of the DEVMODEW structure is larger than the byte offset of the **wSize** member of the UNIDRV\_PRIVATE\_DEVMODE structure. If so, the macro returns the value of the **wSize** member in the UNIDRV\_PRIVATE\_DEVMODE structure. If not, the macro returns zero.

To safely determine the address of the private portion of your plug-in's DEVMODEW structure, do the following:

1.  Call the **GET\_UNIDRV\_PRIVATE\_DEVMODE\_SIZE** macro, passing the address of the DEVMODEW structure in the call.

2.  Verify that (pdm)-&gt;dmDriverExtra is larger than the value returned by the macro. (The macro returns the value of the **wSize** member of the UNIDRV\_PRIVATE\_DEVMODE structure.)

3.  Determine the address of the private portion of your plug-in's DEVMODEW structure as follows.

    ```
    pdmPlugin = (PBYTE)(pdm) + (pdm)->dmSize + wSize;
    ```

    

    The preceding example starts with the address of the public DEVMODEW structure (pdm), adds the number of bytes of this structure (pdm-&gt;dmSize), and then adds the size in bytes of the Unidrv private DEVMODEW structure (**wSize**). A plug-in's private DEVMODEW data begins at this memory address. If there are multiple plug-ins chained together, the address returned by this example is that of the first plug-in's private DEVMODEW data. The second plug-in's private DEVMODEW data follows the first plug-in's private DEVMODEW data, the third plug-in's private DEVMODEW data follows that of the second plug-in's private DEVMODEW data, and so on. A plug-in developer who needs to determine the address of the *n*-th plug-in's private DEVMODEW data must know the sizes of the private DEVMODEW data for the first *n* - 1 plug-ins.

4.  Verify that the private portion of your plug-in's DEVMODEW structure begins with a valid [**OEM\_DMEXTRAHEADER**](oem-dmextraheader.md) structure.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Printoem.h (include Printoem.h)</dt> </dl> |



## See also

<dl> <dt>

[**PSCRIPT5\_PRIVATE\_DEVMODE**](pscript5-private-devmode.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20UNIDRV_PRIVATE_DEVMODE%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





