---
Description: A print processor's EnumPrintProcessorDatatypes function enumerates the data types that the print processor supports.
ms.assetid: 018880d0-0b0b-4130-bd8f-93814e40fe1e
title: EnumPrintProcessorDatatypesA function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# EnumPrintProcessorDatatypesA function

A print processor's **EnumPrintProcessorDatatypes** function enumerates the data types that the print processor supports.

## Syntax


```C++
BOOL EnumPrintProcessorDatatypes(
  _In_opt_  LPTSTR  pName,
  _In_      LPTSTR  pPrintProcessorName,
            DWORD   Level,
  _Out_opt_ LPBYTE  pDatatypes,
            DWORD   cbBuf,
  _Out_     LPDWORD pcbNeeded,
  _Out_     LPDWORD pcReturned
);
```



## Parameters

<dl> <dt>

*pName* \[in, optional\]
</dt> <dd>

Caller-supplied pointer to a string representing name of the server on which the print processor is installed. If **NULL**, the server is the local system.

</dd> <dt>

*pPrintProcessorName* \[in\]
</dt> <dd>

Caller-supplied pointer to a string representing the print processor name.

</dd> <dt>

*Level* 
</dt> <dd>

Caller-supplied value indicating the type of the structures to be returned in the buffer pointed to by *pDatatypes*. This value must be 1, indicating that the structure is DATATYPES\_INFO\_1.

</dd> <dt>

*pDatatypes* \[out, optional\]
</dt> <dd>

Caller-supplied pointer to a buffer to receive an array of DATATYPES\_INFO\_1 structures, followed by a set of character strings representing data type names. The DATATYPES\_INFO\_1 structure is described in the Microsoft Windows SDK documentation. The structure member *pName* must be of type LPWSTR.

</dd> <dt>

*cbBuf* 
</dt> <dd>

Caller-supplied value representing the size, in bytes, of the buffer pointed to by *pDatatypes*.

</dd> <dt>

*pcbNeeded* \[out\]
</dt> <dd>

Caller-supplied pointer to a location to receive the minimum required size for the buffer pointed to by *pDatatypes*.

</dd> <dt>

*pcReturned* \[out\]
</dt> <dd>

Caller-supplied pointer to a location to receive the number of DATATYPES\_INFO\_1 structures returned in the buffer pointed to by *pDatatypes*.

</dd> </dl>

## Return value

If the operation succeeds, the function should return **TRUE**. If the operation fails, the function should call **SetLastError** to set an error code, and then return **FALSE**.

## Remarks

Print processors are required to export an **EnumPrintProcessorDatatypes** function. The local print provider calls the function during initialization. The function is also called when an application calls the spooler's version of the same function.

The function must return an array of DATATYPES\_INFO\_1 structures, with each structure pointing to a string that represents a data type. The actual strings must also be included in the buffer, after the structure array. See [Sample Print Processor](https://www.bing.com/search?q=Sample+Print+Processor) for an example.

The function should return the number of DATATYPES\_INFO\_1 structures returned (that is, the number of data types supported) in the location pointed to by *pcReturned*.

The function should return the minimum required buffer size in the location pointed to by *pcbNeeded*. If the supplied buffer is too small, the function should specify a value for *pcbNeeded*, set the error code to ERROR\_INSUFFICIENT\_BUFFER, and return **FALSE**.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Winspool.h (include Winspool.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20EnumPrintProcessorDatatypesA%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




