---
Description: 'The DEVQUERYPRINT\_INFO structure is used as an input parameter to a printer interface DLL''s DevQueryPrintEx function.'
ms.assetid: 'c46193f2-4c69-4aed-a063-2225faba9ee1'
title: 'DEVQUERYPRINT\_INFO structure'
---

# DEVQUERYPRINT\_INFO structure

The DEVQUERYPRINT\_INFO structure is used as an input parameter to a printer interface DLL's [**DevQueryPrintEx**](devqueryprintex.md) function.

## Syntax


```C++
typedef struct _DEVQUERYPRINT_INFO {
  WORD    cbSize;
  WORD    Level;
  HANDLE  hPrinter;
  DEVMODE *pDevMode;
  LPWSTR  pszErrorStr;
  DWORD   cchErrorStr;
  DWORD   cchNeeded;
} DEVQUERYPRINT_INFO, *PDEVQUERYPRINT_INFO;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

Spooler-supplied size, in bytes, of the DEVQUERYPRINT\_INFO structure.

</dd> <dt>

**Level**
</dt> <dd>

Spooler-supplied level of the DEVQUERYPRINT\_INFO structure. Currently, this member is always set to 1.

</dd> <dt>

**hPrinter**
</dt> <dd>

Spooler-supplied printer handle.

</dd> <dt>

**pDevMode**
</dt> <dd>

Spooler-supplied pointer to a [**DEVMODEW**](display.devmodew) structure describing printer characteristics required by the print job.

</dd> <dt>

**pszErrorStr**
</dt> <dd>

Spooler-supplied pointer to a buffer to receive a NULL-terminated error text string, if the print job cannot be printed.

</dd> <dt>

**cchErrorStr**
</dt> <dd>

Spooler-supplied size, in bytes, of the string buffer pointed to by **pszErrorStr**.

</dd> <dt>

**cchNeeded**
</dt> <dd>

Driver-supplied length, in bytes, of the error string supplied in the buffer pointed to by **pszErrorStr**. If the string is too large to fit in the buffer, the string should be truncated, but the untruncated length should be specified here.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Winddiui.h (include Winddiui.h)</dt> </dl> |



## See also

<dl> <dt>

[**DevQueryPrintEx**](devqueryprintex.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20DEVQUERYPRINT_INFO%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





