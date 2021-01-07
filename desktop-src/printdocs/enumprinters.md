---
description: The EnumPrinters function enumerates available printers, print servers, domains, or print providers.
ms.assetid: 0d0cc726-c515-4146-9273-cdf1db3c76b7
title: EnumPrinters function (Winspool.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EnumPrinters
- EnumPrintersA
- EnumPrintersW
api_type: 
- DllExport
api_location: 
- Winspool.drv
---

# EnumPrinters function

The **EnumPrinters** function enumerates available printers, print servers, domains, or print providers.

## Syntax


```C++
BOOL EnumPrinters(
  _In_  DWORD   Flags,
  _In_  LPTSTR  Name,
  _In_  DWORD   Level,
  _Out_ LPBYTE  pPrinterEnum,
  _In_  DWORD   cbBuf,
  _Out_ LPDWORD pcbNeeded,
  _Out_ LPDWORD pcReturned
);
```



## Parameters

<dl> <dt>

*Flags* \[in\]
</dt> <dd>

The types of print objects that the function should enumerate. This value can be one or more of the following values.



| Value                                                                                                                                                                                               | Meaning                                                                                                                                                                                                                                                |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="PRINTER_ENUM_LOCAL"></span><span id="printer_enum_local"></span><dl> <dt>**PRINTER\_ENUM\_LOCAL**</dt> </dl>                       | If the PRINTER\_ENUM\_NAME flag is not also passed, the function ignores the *Name* parameter, and enumerates the locally installed printers. If PRINTER\_ENUM\_NAME is also passed, the function enumerates the local printers on *Name*. <br/> |
| <span id="PRINTER_ENUM_NAME"></span><span id="printer_enum_name"></span><dl> <dt>**PRINTER\_ENUM\_NAME**</dt> </dl>                          | The function enumerates the printer identified by *Name*. This can be a server, a domain, or a print provider. If *Name* is **NULL**, the function enumerates available print providers.<br/>                                                    |
| <span id="PRINTER_ENUM_SHARED"></span><span id="printer_enum_shared"></span><dl> <dt>**PRINTER\_ENUM\_SHARED**</dt> </dl>                    | The function enumerates printers that have the shared attribute. Cannot be used in isolation; use an OR operation to combine with another PRINTER\_ENUM type.<br/>                                                                               |
| <span id="PRINTER_ENUM_CONNECTIONS"></span><span id="printer_enum_connections"></span><dl> <dt>**PRINTER\_ENUM\_CONNECTIONS**</dt> </dl>     | The function enumerates the list of printers to which the user has made previous connections.<br/>                                                                                                                                               |
| <span id="PRINTER_ENUM_NETWORK"></span><span id="printer_enum_network"></span><dl> <dt>**PRINTER\_ENUM\_NETWORK**</dt> </dl>                 | The function enumerates network printers in the computer's domain. This value is valid only if *Level* is 1.<br/>                                                                                                                                |
| <span id="PRINTER_ENUM_REMOTE"></span><span id="printer_enum_remote"></span><dl> <dt>**PRINTER\_ENUM\_REMOTE**</dt> </dl>                    | The function enumerates network printers and print servers in the computer's domain. This value is valid only if *Level* is 1.<br/>                                                                                                              |
| <span id="PRINTER_ENUM_CATEGORY_3D"></span><span id="printer_enum_category_3d"></span><dl> <dt>**PRINTER\_ENUM\_CATEGORY\_3D**</dt> </dl>    | The function enumerates only 3D printers.<br/>                                                                                                                                                                                                   |
| <span id="PRINTER_ENUM_CATEGORY_ALL"></span><span id="printer_enum_category_all"></span><dl> <dt>**PRINTER\_ENUM\_CATEGORY\_ALL**</dt> </dl> | The function enumerates all print devices, including 3D printers.<br/>                                                                                                                                                                           |



 

If *Level* is 4, you can only use the PRINTER\_ENUM\_CONNECTIONS and PRINTER\_ENUM\_LOCAL constants.

> [!Note]  
> 3D print devices are not enumerated by default. You must include both **PRINTER\_ENUM\_CATEGORY\_3D** and **PRINTER\_ENUM\_LOCAL** to enumerate only 3D printers. To include 3D printers, along with all other local printers, use **PRINTER\_ENUM\_CATEGORY\_ALL** and **PRINTER\_ENUM\_LOCAL**.

 

</dd> <dt>

*Name* \[in\]
</dt> <dd>

If *Level* is 1, *Flags* contains PRINTER\_ENUM\_NAME, and *Name* is non-**NULL**, then *Name* is a pointer to a null-terminated string that specifies the name of the object to enumerate. This string can be the name of a server, a domain, or a print provider.

If *Level* is 1, *Flags* contains PRINTER\_ENUM\_NAME, and *Name* is **NULL**, then the function enumerates the available print providers.

If *Level* is 1, *Flags* contains PRINTER\_ENUM\_REMOTE, and *Name* is **NULL**, then the function enumerates the printers in the user's domain.

If *Level* is 2 or 5,*Name* is a pointer to a null-terminated string that specifies the name of a server whose printers are to be enumerated. If this string is **NULL**, then the function enumerates the printers installed on the local computer.

If *Level* is 4, *Name* should be **NULL**. The function always queries on the local computer.

When *Name* is **NULL**, setting *Flags* to PRINTER\_ENUM\_LOCAL \| PRINTER\_ENUM\_CONNECTIONS enumerates printers that are installed on the local machine. These printers include those that are physically attached to the local machine as well as remote printers to which it has a network connection.

When *Name* is not **NULL**, setting *Flags* to PRINTER\_ENUM\_LOCAL \| PRINTER\_ENUM\_NAME enumerates the local printers that are installed on the server *Name*.

</dd> <dt>

*Level* \[in\]
</dt> <dd>

The type of data structures pointed to by *pPrinterEnum*. Valid values are 1, 2, 4, and 5, which correspond to the [**PRINTER\_INFO\_1**](printer-info-1.md), [**PRINTER\_INFO\_2**](printer-info-2.md) , [**PRINTER\_INFO\_4**](printer-info-4.md), and [**PRINTER\_INFO\_5**](printer-info-5.md) data structures.

This value can be 1, 2, 4, or 5.

</dd> <dt>

*pPrinterEnum* \[out\]
</dt> <dd>

A pointer to a buffer that receives an array of [**PRINTER\_INFO\_1**](printer-info-1.md), [**PRINTER\_INFO\_2**](printer-info-2.md), [**PRINTER\_INFO\_4**](printer-info-4.md), or [**PRINTER\_INFO\_5**](printer-info-5.md) structures. Each structure contains data that describes an available print object.

If *Level* is 1, the array contains [**PRINTER\_INFO\_1**](printer-info-1.md) structures. If *Level* is 2, the array contains [**PRINTER\_INFO\_2**](printer-info-2.md) structures. If *Level* is 4, the array contains [**PRINTER\_INFO\_4**](printer-info-4.md) structures. If *Level* is 5, the array contains [**PRINTER\_INFO\_5**](printer-info-5.md) structures.

The buffer must be large enough to receive the array of data structures and any strings or other data to which the structure members point. If the buffer is too small, the *pcbNeeded* parameter returns the required buffer size.

</dd> <dt>

*cbBuf* \[in\]
</dt> <dd>

The size, in bytes, of the buffer pointed to by *pPrinterEnum*.

</dd> <dt>

*pcbNeeded* \[out\]
</dt> <dd>

A pointer to a value that receives the number of bytes copied if the function succeeds or the number of bytes required if *cbBuf* is too small.

</dd> <dt>

*pcReturned* \[out\]
</dt> <dd>

A pointer to a value that receives the number of [**PRINTER\_INFO\_1**](printer-info-1.md), [**PRINTER\_INFO\_2**](printer-info-2.md) , [**PRINTER\_INFO\_4**](printer-info-4.md), or [**PRINTER\_INFO\_5**](printer-info-5.md) structures that the function returns in the array to which *pPrinterEnum* points.

</dd> </dl>

## Return value

If the function succeeds, the return value is a nonzero value.

If the function fails, the return value is zero.

## Remarks

Do not call this method in [**DllMain**](/windows/desktop/Dlls/dllmain).

> [!Note]  
> This is a blocking or synchronous function and might not return immediately. How quickly this function returns depends on run-time factors such as network status, print server configuration, and printer driver implementation factors that are difficult to predict when writing an application. Calling this function from a thread that manages interaction with the user interface could make the application appear to be unresponsive.

 

If **EnumPrinters** returns a [**PRINTER\_INFO\_1**](printer-info-1.md) structure in which PRINTER\_ENUM\_CONTAINER is specified, this indicates that there is a hierarchy of printer objects. An application can enumerate the hierarchy by calling **EnumPrinters** again, setting *Name* to the value of the **PRINTER\_INFO\_1** structure's **pName** member.

The **EnumPrinters** function does not retrieve security information. If [**PRINTER\_INFO\_2**](printer-info-2.md) structures are returned in the array pointed to by *pPrinterEnum*, their *pSecurityDescriptor* members will be set to **NULL**.

To get information about the default printer, call [**GetDefaultPrinter**](getdefaultprinter.md).

The [**PRINTER\_INFO\_4**](printer-info-4.md) structure provides an easy and extremely fast way to retrieve the names of the printers installed on a local machine, as well as the remote connections that a user has established. When **EnumPrinters** is called with a **PRINTER\_INFO\_4** data structure, that function queries the registry for the specified information, then returns immediately. This differs from the behavior of **EnumPrinters** when called with other levels of **PRINTER\_INFO\_\*** data structures. In particular, when **EnumPrinters** is called with a level 2 ([**PRINTER\_INFO\_2**](printer-info-2.md)) data structure, it performs an [**OpenPrinter**](openprinter.md) call on each remote connection. If a remote connection is down, or the remote server no longer exists, or the remote printer no longer exists, the function must wait for RPC to time out and consequently fail the **OpenPrinter** call. This can take a while. Passing a **PRINTER\_INFO\_4** structure lets an application retrieve a bare minimum of required information; if more detailed information is desired, a subsequent **EnumPrinters** level 2 call can be made.

**Windows Vista:** The printer data returned by **EnumPrinters** is retrieved from a local cache when the value of *Level* is 4.

The following table shows the **EnumPrinters** output for various *Flags* values when the *Level* parameter is set to 1.

In the *Name* parameter column of the table, you should substitute an appropriate name for Print Provider, Domain, and Machine. For example, for "Print Provider," you could use the name of the network print provider or the name of the local print provider. To retrieve print provider names, call **EnumPrinters** with *Name* set to **NULL**.



| *Flags* parameter                                  | *Name* parameter                            | Result                                                                                            |
|----------------------------------------------------|---------------------------------------------|---------------------------------------------------------------------------------------------------|
| PRINTER\_ENUM\_LOCAL (and not PRINTER\_ENUM\_NAME) | The *Name* parameter is ignored.<br/> | All local printers.<br/>                                                                    |
| PRINTER\_ENUM\_NAME                                | "Print Provider"<br/>                 | All domain names<br/>                                                                       |
| PRINTER\_ENUM\_NAME                                | "Print Provider!Domain"<br/>          | All printers and print servers in the computer's domain<br/>                                |
| PRINTER\_ENUM\_NAME                                | "Print Provider!!\\\\Machine"<br/>    | All printers shared at \\\\Machine<br/>                                                     |
| PRINTER\_ENUM\_NAME                                | An empty string, ""<br/>              | All local printers.<br/>                                                                    |
| PRINTER\_ENUM\_NAME                                | **NULL**<br/>                         | All print providers in the computer's domain<br/>                                           |
| PRINTER\_ENUM\_CONNECTIONS                         | The *Name* parameter is ignored.<br/> | All connected remote printers<br/>                                                          |
| PRINTER\_ENUM\_NETWORK                             | The *Name* parameter is ignored.<br/> | All printers in the computer's domain<br/>                                                  |
| PRINTER\_ENUM\_REMOTE                              | An empty string, ""<br/>              | All printers and print servers in the computer's domain<br/>                                |
| PRINTER\_ENUM\_REMOTE                              | "Print Provider"<br/>                 | Same as PRINTER\_ENUM\_NAME<br/>                                                            |
| PRINTER\_ENUM\_REMOTE                              | "Print Provider!Domain"<br/>          | All printers and print servers in computer's domain, regardless of *Domain* specified.<br/> |
| PRINTER\_ENUM\_CATEGORY\_3D                        | The *Name* parameter is ignored.<br/> | Only 3D printers are enumerated.<br/>                                                       |
| PRINTER\_ENUM\_CATEGORY\_ALL                       | The *Name* parameter is ignored.<br/> | 3D printers are enumerated, along with all other printers.<br/>                             |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Winspool.h (include Windows.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Winspool.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Winspool.drv</dt> </dl>                   |
| Unicode and ANSI names<br/>   | **EnumPrintersW** (Unicode) and **EnumPrintersA** (ANSI)<br/>                                       |



## See also

<dl> <dt>

[Printing](printdocs-printing.md)
</dt> <dt>

[Print Spooler API Functions](printing-and-print-spooler-functions.md)
</dt> <dt>

[**AddPrinter**](addprinter.md)
</dt> <dt>

[**DeletePrinter**](deleteprinter.md)
</dt> <dt>

[**GetPrinter**](getprinter.md)
</dt> <dt>

[**PRINTER\_INFO\_1**](printer-info-1.md)
</dt> <dt>

[**PRINTER\_INFO\_2**](printer-info-2.md)
</dt> <dt>

[**PRINTER\_INFO\_4**](printer-info-4.md)
</dt> <dt>

[**PRINTER\_INFO\_5**](printer-info-5.md)
</dt> <dt>

[**SetPrinter**](setprinter.md)
</dt> </dl>

 

