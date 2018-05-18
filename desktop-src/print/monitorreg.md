---
Description: 'The MONITORREG structure supplies print monitors with the address of registry functions to use instead of Win32 registry API functions.'
ms.assetid: '57c146bc-574f-4137-89bb-e891e005de05'
title: MONITORREG structure
---

# MONITORREG structure

The MONITORREG structure supplies print monitors with the address of registry functions to use instead of Win32 registry API functions.

## Syntax


```C++
typedef struct _MONITORREG {
  DWORD cbSize;
  LONG  (WINAPI *fpCreateKey)(
      HKEYMONITOR hcKey, 
      LPCTSTR pszSubKey, 
      DWORD dwOptions, 
      REGSAM samDesired, 
      PSECURITY_ATTRIBUTES pSecurityAttributes, 
      HKEYMONITOR phckResult, 
      PDWORD pdwDisposition, 
      HANDLE hSpooler);
  LONG  (WINAPI *fpOpenKey)(
      HKEYMONITOR hcKey, 
      LPCTSTR pszSubKey, 
      REGSAM samDesired, 
      HKEYMONITOR phkResult, 
      HANDLE hSpooler);
  LONG  (WINAPI *fpCloseKey)(
      HKEYMONITOR hcKey, 
      HANDLE hSpooler);
  LONG  (WINAPI *fpDeleteKey)(
      HKEYMONITOR hcKey, 
      LPCTSTR pszSubKey, 
      HANDLE hSpooler);
  LONG  (WINAPI *fpEnumKey)(
      HKEYMONITOR hcKey, 
      DWORD dwIndex, 
      LPTSTR pszName, 
      PDWORD pcchName, 
      PFILETIME pftLastWriteTime, 
      HANDLE hSpooler);
  LONG  (WINAPI *fpQueryInfoKey)(
      HKEYMONITOR hcKey, 
      PDWORD pcSubKeys, 
      PDWORD pcbKey, 
      PDWORD pcValues, 
      PDWORD pcbValue, 
      PDWORD pcbData, 
      PDWORD pcbSecurityDescriptor, 
      PFILETIME pftLastWriteTime, 
      HANDLE hSpooler);
  LONG  (WINAPI *fpSetValue)(
      HKEYMONITOR hcKey, 
      LPCTSTR pszValue, 
      DWORD dwType, 
      const BYTE* pData, 
      DWORD cbData, 
      HANDLE hSpooler);
  LONG  (WINAPI *fpDeleteValue)(
      HKEYMONITOR hcKey, 
      LPCTSTR pszValue, 
      HANDLE hSpooler);
  LONG  (WINAPI *fpEnumValue)(
      HKEYMONITOR hcKey, 
      DWORD dwIndex, 
      LPTSTR pszValue, 
      PDWORD pcbValue, 
      PDWORD pTyp, 
      PBYTE pcbData, 
      PDWORD pcbData, 
      HANDLE hSpooler);
  LONG  (WINAPI *fpQueryValue)(
      HKEYMONITOR hcKey, 
      LPCTSTR pszValue, 
      PDWORD pType, 
      PBYTE pData, 
      PDWORD pcbData, 
      HANDLE hSpooler);
} MONITORREG, *PMONITORREG;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

Size, in bytes, of the MONITORREG structure.

</dd> <dt>

**fpCreateKey**
</dt> <dd></dd> <dt>

**fpOpenKey**
</dt> <dd></dd> <dt>

**fpCloseKey**
</dt> <dd></dd> <dt>

**fpDeleteKey**
</dt> <dd></dd> <dt>

**fpEnumKey**
</dt> <dd></dd> <dt>

**fpQueryInfoKey**
</dt> <dd></dd> <dt>

**fpSetValue**
</dt> <dd></dd> <dt>

**fpDeleteValue**
</dt> <dd></dd> <dt>

**fpEnumValue**
</dt> <dd></dd> <dt>

**fpQueryValue**
</dt> <dd></dd> </dl>

## Remarks

The MONITORREG structure's address is supplied in a [**MONITORINIT**](monitorinit.md) structure, which is passed to a print monitor's [**InitializePrintMonitor2**](initializeprintmonitor2.md) function.

When [storing port configuration information](print.storing_port_configuration_information), print monitors must not explicitly call either the Win32 registry API or the cluster registry API. Instead, they must call equivalent spooler registry functions. The MONITORREG structure supplies the addresses of these functions. The following table lists each spooler registry function and its equivalent cluster registry function.



| Spooler Registry Function   | Equivalent Cluster Registry Function  |
|-----------------------------|---------------------------------------|
| **CreateKey**<br/>    | **ClusterRegCreateKey**<br/>    |
| **OpenKey**<br/>      | **ClusterRegOpenKey**<br/>      |
| **CloseKey**<br/>     | **ClusterRegCloseKey**<br/>     |
| **DeleteKey**<br/>    | **ClusterRegDeleteKey**<br/>    |
| **EnumKey**<br/>      | **ClusterRegEnumKey**<br/>      |
| **QueryInfoKey**<br/> | **ClusterRegQueryInfoKey**<br/> |
| **SetValue**<br/>     | **ClusterRegSetValue**<br/>     |
| **DeleteValue**<br/>  | **ClusterRegDeleteValue**<br/>  |
| **EnumValue**<br/>    | **ClusterRegEnumValue**<br/>    |
| **QueryValue**<br/>   | **ClusterRegQueryValue**<br/>   |



 

Input and output parameters for these spooler functions match the parameters of the equivalent cluster registry functions (described in the Microsoft Windows SDK documentation), with the following exceptions:

-   Each spooler registry function requires an *hSpooler* input parameter. This is the spooler handle received in the [**MONITORINIT**](monitorinit.md) structure.

-   The spooler registry functions use HANDLE and PHANDLE parameter types instead of the HKEY and PHKEY types used by the cluster registry functions. Monitors receive the handle of the root registry location in the **hckRegistryRoot** member of the [**MONITORINIT**](monitorinit.md) structure.

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Winsplp.h (include Winsplp.h)</dt> </dl> |



## See also

<dl> <dt>

[**MONITORINIT**](monitorinit.md)
</dt> <dt>

[**InitializePrintMonitor2**](initializeprintmonitor2.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20MONITORREG%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





