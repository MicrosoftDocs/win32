---
Description: The print spooler's IsValidDevmode function verifies that the contents of a DEVMODE structure are valid.
ms.assetid: 74da159d-7edc-44fc-abd9-aa068c4de7f2
title: IsValidDevmodeA function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IsValidDevmodeA function

The print spooler's `IsValidDevmode` function verifies that the contents of a [**DEVMODE**](https://www.bing.com/search?q=**DEVMODE**) structure are valid.

## Syntax


```C++
BOOL IsValidDevmode(
  _In_opt_ PDEVMODEW pDevmode,
           size_t    DevModeSize
);
```



## Parameters

<dl> <dt>

*pDevmode* \[in, optional\]
</dt> <dd>

Pointer to the DEVMODE structure to be validated.

</dd> <dt>

*DevModeSize* 
</dt> <dd>

Size, in bytes, of the buffer pointed to by *pDevmode*.

</dd> </dl>

## Return value

If the DEVMODE structure is valid, or if the function succeeds in repairing the structure to make it valid, the function returns **TRUE**. Otherwise, the function returns **FALSE**. The caller can obtain an error code by calling **GetLastError**.

## Remarks

Before using a DEVMODE structure obtained from a possibly unreliable source, a printer driver can call this function to verify that the structure is valid. This function validates only the public members of the DEVMODE structure. It does not check the private members of the structure.

The **dmSize** member of the DEVMODE structure specifies the size of the DEVMODE structure, not including any private, driver-specified data appended to the structure. The **dmDriverExtra** member specifies the size of the private data appended to the structure, if there is any. Callers should set *DevModeSize* to **dmSize**+**dmDriverExtra** only if they can guarantee that the input buffer size is at least that large.

This function does not require the caller to obtain elevated privileges.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Version<br/>         | Available in Windows XP with Service Pack 2 and later versions of Windows.<br/>                      |
| Header<br/>          | <dl> <dt>Winspool.h (include Winspool.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Winspool.lib</dt> </dl>                    |
| DLL<br/>             | <dl> <dt>Winspool.drv</dt> </dl>                    |



## See also

<dl> <dt>

[**DEVMODE**](https://www.bing.com/search?q=**DEVMODE**)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IsValidDevmodeA%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





