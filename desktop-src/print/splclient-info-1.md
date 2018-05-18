---
Description: 'The SPLCLIENT\_INFO\_1 structure is used as input to the GenerateCopyFilePaths function that is exported by Point and Print DLLs.'
ms.assetid: 'a9659f77-e84b-471a-a778-a4628d89ce19'
title: 'SPLCLIENT\_INFO\_1 structure'
---

# SPLCLIENT\_INFO\_1 structure

The SPLCLIENT\_INFO\_1 structure is used as input to the [**GenerateCopyFilePaths**](generatecopyfilepaths.md) function that is exported by [Point and Print DLLs](print.point_and_print_dlls).

## Syntax


```C++
typedef struct _SPLCLIENT_INFO_1 {
  DWORD  dwSize;
  LPWSTR pMachineName;
  LPWSTR pUserName;
  DWORD  dwBuildNum;
  DWORD  dwMajorVersion;
  DWORD  dwMinorVersion;
  WORD   wProcessorArchitecture;
} SPLCLIENT_INFO_1, *PSPLCLIENT_INFO_1, *LPSPLCLIENT_INFO_1;
```



## Members

<dl> <dt>

**dwSize**
</dt> <dd>

Size of the SPLCLIENT\_INFO\_1 structure.

</dd> <dt>

**pMachineName**
</dt> <dd>

Not used.

</dd> <dt>

**pUserName**
</dt> <dd>

Not used.

</dd> <dt>

**dwBuildNum**
</dt> <dd>

The build number of the version of the NT-based operating system running on the client, as returned by the Microsoft Window SDK **GetVersionEx** function.

</dd> <dt>

**dwMajorVersion**
</dt> <dd>

The major version number of the NT-based operating system print spooler running on the client.

</dd> <dt>

**dwMinorVersion**
</dt> <dd>

The minor version number of the NT-based operating system print spooler running on the client.

</dd> <dt>

**wProcessorArchitecture**
</dt> <dd>

The client's processor architecture, as returned by the Window SDK **GetSystemInfo** function.

</dd> </dl>

## Remarks

Values for all structure members are supplied by the print spooler before the spooler calls [**GenerateCopyFilePaths**](generatecopyfilepaths.md).

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Winsplp.h (include Winsplp.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20SPLCLIENT_INFO_1%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




