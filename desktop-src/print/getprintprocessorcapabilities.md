---
Description: 'A print processor''s GetPrintProcessorCapabilities function returns capabilities associated with a specified input data type.'
ms.assetid: '81aacb41-cba7-4bd0-aded-919a4df0b934'
title: GetPrintProcessorCapabilities function
---

# GetPrintProcessorCapabilities function

A print processor's **GetPrintProcessorCapabilities** function returns capabilities associated with a specified input data type.

## Syntax


```C++
DWORD GetPrintProcessorCapabilities(
  _In_  LPTSTR  pValueName,
  _In_  DWORD   dwAttributes,
  _Out_ LPBYTE  pData,
  _In_  DWORD   nSize,
  _Out_ LPDWORD pcbNeeded
);
```



## Parameters

<dl> <dt>

*pValueName* \[in\]
</dt> <dd>

Caller-supplied pointer to a string that represents a data type that is supported by the print processor. The string pointer must be of type LPWSTR.

</dd> <dt>

*dwAttributes* \[in\]
</dt> <dd>

Caller-supplied attributes flags. Refer to the **Attributes** member of PRINTER\_INFO\_*x* structures (described in the Microsoft Windows SDK documentation).

</dd> <dt>

*pData* \[out\]
</dt> <dd>

Caller-supplied pointer to a PRINTPROCESSOR\_CAPS\_1 or PRINTPROCESSOR\_CAPS\_2 structure (described in the Windows SDK documentation).

</dd> <dt>

*nSize* \[in\]
</dt> <dd>

Caller-supplied value that represents the size of the buffer pointed to by *pData*.

If the value is less than sizeof(PRINTPROCESSOR\_CAPS\_1), this function should supply a value that is equal to sizeof(PRINTPROCESSOR\_CAPS\_1) or sizeof(PRINTPROCESSOR\_CAPS\_2), depending on which structure is supported by the print processor.

> [!Note]  
> If the value is less than sizeof(PRINTPROCESSOR\_CAPS\_1), the winprint print processor will supply a value of sizeof(PRINTPROCESSOR\_CAPS\_2) for Windows Vista operating systems, or sizeof(PRINTPROCESSOR\_CAPS\_1) for earlier operating system versions.

 

</dd> <dt>

*pcbNeeded* \[out\]
</dt> <dd>

Caller-supplied pointer to a location to receive the minimum required size for the buffer pointed to by *pData*.

</dd> </dl>

## Return value

If the operation succeeds, the function should return ERROR\_SUCCESS. Otherwise, it should return a Win32 error code.

## Remarks

Print processors can optionally export a **GetPrintProcessorCapabilities** function. The function's purpose is to return a filled-in PRINTPROCESSOR\_CAPS\_1 or PRINTPROCESSOR\_CAPS\_2 structure for every input data type that the print processor supports.

The spooler calls a print processor's **GetPrintProcessorCapabilities** function when an application calls **GetPrinterData** (described in the Windows SDK documentation), specifying a value name with a format of PrintProcCaps\_*datatype*, where *datatype* is the name of an input data type. Before calling **GetPrintProcessorCapabilities,** the spooler removes the PrintProcCaps\_ prefix from the value name string.

The function should determine if the received buffer is large enough and, if it is, should fill in either the PRINTPROCESSOR\_CAPS\_1 or PRINTPROCESSOR\_CAPS\_2 structure (defined in the Windows SDK documentation) and return. The value of *nSize* determines whether PRINTPROCESSOR\_CAPS\_1 or PRINTPROCESSOR\_CAPS\_2 will be used.

The function should always use the location pointed to by *pcbNeeded* to return the required buffer size, whether or not the actual buffer is large enough.

The specified return value becomes the return value that the spooler provides for **GetPrinterData**.

## Requirements



|                            |                                                                                                          |
|----------------------------|----------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                       |
| Header<br/>          | <dl> <dt>Winsplp.h (include Winsplp.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GetPrintProcessorCapabilities%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




