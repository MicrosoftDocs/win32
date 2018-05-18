---
Description: 'The PRINTPROCESSOROPENDATA structure is used as an input parameter to a print processor''s OpenPrintProcessor function.'
ms.assetid: 'd7160747-d81c-407a-bbf0-7ec5b3210c13'
title: PRINTPROCESSOROPENDATA structure
---

# PRINTPROCESSOROPENDATA structure

The PRINTPROCESSOROPENDATA structure is used as an input parameter to a print processor's [**OpenPrintProcessor**](openprintprocessor.md) function.

## Syntax


```C++
typedef struct _PRINTPROCESSOROPENDATA {
  PDEVMODE pDevMode;
  LPWSTR   pDatatype;
  LPWSTR   pParameters;
  LPWSTR   pDocumentName;
  DWORD    JobId;
  LPWSTR   pOutputFile;
  LPWSTR   pPrinterName;
} PRINTPROCESSOROPENDATA, *PPRINTPROCESSOROPENDATA, *LPPRINTPROCESSOROPENDATA;
```



## Members

<dl> <dt>

**pDevMode**
</dt> <dd>

Spooler-supplied pointer to a [**DEVMODEW**](display.devmodew) structure.

</dd> <dt>

**pDatatype**
</dt> <dd>

Spooler-supplied pointer to a string representing the print job's data type.

</dd> <dt>

**pParameters**
</dt> <dd>

Spooler-supplied pointer to a parameter string, as specified in a JOB\_INFO\_2 structure supplied to a call to the **SetJob** function, described in the Microsoft Windows SDK documentation.

</dd> <dt>

**pDocumentName**
</dt> <dd>

Spooler-supplied pointer to a string representing the name of the input document associated with the print job.

</dd> <dt>

**JobId**
</dt> <dd>

Spooler-supplied value identifying the print job.

</dd> <dt>

**pOutputFile**
</dt> <dd>

Spooler-supplied pointer to a string representing the name of the output spool file.

</dd> <dt>

**pPrinterName**
</dt> <dd>

Spooler-supplied pointer to a string representing the name of the printer to be used.

</dd> </dl>

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Winsplp.h (include Winsplp.h)</dt> </dl> |



## See also

<dl> <dt>

[**OpenPrintProcessor**](openprintprocessor.md)
</dt> <dt>

[**DEVMODEW**](display.devmodew)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20PRINTPROCESSOROPENDATA%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





