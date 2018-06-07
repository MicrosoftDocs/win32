---
Description: The PSCRIPT5\_PRIVATE\_DEVMODE structure enables Pscript5 plug-ins to determine the size of the private portion of Pscript5's DEVMODEW structure.
ms.assetid: e2ae002b-2bc9-4e5e-b9b6-bb76849c2cba
title: PSCRIPT5\_PRIVATE\_DEVMODE structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# PSCRIPT5\_PRIVATE\_DEVMODE structure

The PSCRIPT5\_PRIVATE\_DEVMODE structure enables Pscript5 plug-ins to determine the size of the private portion of Pscript5's DEVMODEW structure.

## Syntax


```C++
typedef struct _PSCRIPT5_PRIVATE_DEVMODE {
  WORD wReserved[57];
  WORD wSize;
} PSCRIPT5_PRIVATE_DEVMODE, *PPSCRIPT5_PRIVATE_DEVMODE;
```



## Members

<dl> <dt>

**wReserved**
</dt> <dd>

Reserved for system use.

</dd> <dt>

**wSize**
</dt> <dd>

The size, in bytes, of the private portion of Pscript5's [**DEVMODEW**](https://msdn.microsoft.com/b2369876-9a79-40c8-8d27-c8b9d8e68e6b) structure.

</dd> </dl>

## Remarks

This structure and associated macro are available in Windows 2000 and later. For information about the public and private sections of the DEVMODEW structure, see [The DEVMODEW Structure](https://www.bing.com/search?q=The+DEVMODEW+Structure).

Printoem.h defines a macro that you can use to determine the size of the private portion of Pscript5's DEVMODEW structure.


```
#define GET_PSCRIPT5_PRIVATE_DEVMODE_SIZE(pdm)\
( ( (pdm)->dmDriverExtra > (FIELD_OFFSET(PSCRIPT5_PRIVATE_DEVMODE, wSize) + sizeof(WORD)) ) ? \
((PPSCRIPT5_PRIVATE_DEVMODE)((PBYTE)(pdm) + (pdm)-> dmSize)) -> wSize : 0 )
```



The *pdm* argument in the **GET\_PSCRIPT5\_PRIVATE\_DEVMODE\_SIZE** macro is a pointer to a DEVMODEW structure. The macro determines whether the value of the **dmDriverExtra** member of the DEVMODEW structure is larger than the byte offset of the **wSize** member of the PSCRIPT5\_PRIVATE\_DEVMODE structure. If so, the macro returns the value of the **wSize** member in the PSCRIPT5\_PRIVATE\_DEVMODE structure. If not, the macro returns zero.

To safely determine the address of the private portion of your plug-in's DEVMODEW structure, do the following:

1.  Call the **GET\_PSCRIPT5\_PRIVATE\_DEVMODE\_SIZE** macro, passing the address of the DEVMODEW structure in the call.

2.  Verify that (pdm)-&gt;dmDriverExtra is larger than the value returned by the macro. (The macro returns the value of the **wSize** member of the PSCRIPT5\_PRIVATE\_DEVMODE structure.)

3.  Determine the address of the private portion of your plug-in's DEVMODEW structure as follows.

    ```
    pdmPlugin = (PBYTE)(pdm) + (pdm)->dmSize + wSize;
    ```

    

    The preceding example starts with the address of the public DEVMODEW structure (*pdm*), adds the number of bytes of this structure (*pdm-*&gt;**dmSize**), and then adds the size in bytes of the Pscript5 private DEVMODEW structure (**wSize**). A plug-in's private DEVMODEW data begins at this memory address. If there are multiple plug-ins chained together, the address returned by this example is that of the first plug-in's private DEVMODEW data. The second plug-in's private DEVMODEW data follows the first plug-in's private DEVMODEW data, the third plug-in's private DEVMODEW data follows that of the second plug-in's private DEVMODEW data, and so on. A plug-in developer who needs to determine the address of the *n*-th plug-in's private DEVMODEW data must know the sizes of the private DEVMODEW data for the first *n* - 1 plug-ins.

4.  Verify that the private portion of your plug-in's DEVMODEW structure begins with a valid [**OEM\_DMEXTRAHEADER**](oem-dmextraheader.md) structure.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Printoem.h (include Printoem.h)</dt> </dl> |



## See also

<dl> <dt>

[**UNIDRV\_PRIVATE\_DEVMODE**](unidrv-private-devmode.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20PSCRIPT5_PRIVATE_DEVMODE%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





