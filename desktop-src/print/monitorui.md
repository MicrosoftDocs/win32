---
Description: 'The MONITORUI structure contains pointers to the functions within a port monitor UI DLL that the print spooler calls.'
ms.assetid: 'baa80f8c-68ed-43a3-8c82-79a4388f9ab6'
title: MONITORUI structure
---

# MONITORUI structure

The MONITORUI structure contains pointers to the functions within a port monitor UI DLL that the print spooler calls.

## Syntax


```C++
typedef struct _MONITORUI {
  DWORD dwMonitorUISize;
  BOOL  (WINAPI *pfnAddPortUI)(
      _In_opt_ PCWSTR pszServer, 
      _In_ HWND hWnd, 
      _In_ PCWSTR pszMonitorNameIn, 
      _Out_opt_ PWSTR ppszPortNameOut);
  BOOL  (WINAPI *pfnConfigurePortUI)(
      _In_opt_ PCWSTR pName, 
      _In_ HWND hWnd, 
      _In_ PCWSTR pPortName);
  BOOL  (WINAPI *pfnDeletePortUI)(
      _In_opt_ PCWSTR pszServer, 
      _In_ HWND hWnd, 
      _In_ PCWSTR pszPortName);
} MONITORUI, *PMONITORUI;
```



## Members

<dl> <dt>

**dwMonitorUISize**
</dt> <dd>

Size, in bytes, of the MONITORUI structure.

</dd> <dt>

**pfnAddPortUI**
</dt> <dd></dd> <dt>

**pfnConfigurePortUI**
</dt> <dd></dd> <dt>

**pfnDeletePortUI**
</dt> <dd></dd> </dl>

## Remarks

All structure members must be initialized by the port monitor UI DLL. The structure's address is passed to the print spooler as the return value for the [**InitializePrintMonitorUI**](initializeprintmonitorui.md) function.

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Winsplp.h (include Winsplp.h)</dt> </dl> |



## See also

<dl> <dt>

[**InitializePrintMonitorUI**](initializeprintmonitorui.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20MONITORUI%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





