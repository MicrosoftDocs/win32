---
Description: Contains a super-set of the information in both a SPLCLIENT\_INFO\_1 and SPLCLIENT\_INFO\_2 structure. It also contains additional information needed by the provider.
ms.assetid: 076ECB20-CFAD-4A16-9B01-6936E0DD7E50
title: SPLCLIENT\_INFO\_3\_VISTA structure
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SPLCLIENT\_INFO\_3\_VISTA structure

Contains a super-set of the information in both a [**SPLCLIENT\_INFO\_1**](RID) and **SPLCLIENT\_INFO\_2** structure. It also contains additional information needed by the provider.

## Syntax


```C++
typedef struct _SPLCLIENT_INFO_3_VISTA {
  UINT             cbSize;
  DWORD            dwFlags;
  DWORD            dwSize;
  PWSTR            pMachineName;
  PWSTR            pUserName;
  DWORD            dwBuildNum;
             DWORD dwMajorVersion;
  DWORD            dwMinorVersion;
  WORD             wProcessorArchitecture;
  UINT64           hSplPrinter;
} SPLCLIENT_INFO_3_VISTA;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

Specifies the size in bytes of this structure.

</dd> <dt>

**dwFlags**
</dt> <dd>

Specifies open printer additional flags to the provider.

</dd> <dt>

**dwSize**
</dt> <dd>

Reserved. Used for compatibility with the [**SPLCLIENT\_INFO\_1**](RID) structure.

</dd> <dt>

**pMachineName**
</dt> <dd>

Specifies the client machine name.

</dd> <dt>

**pUserName**
</dt> <dd>

Specifies the client user name.

</dd> <dt>

**dwBuildNum**
</dt> <dd>

Specifies the client build number.

</dd> <dt>

**dwMajorVersion**
</dt> <dd>

Specifies the major version of the client machine.

</dd> <dt>

**dwMinorVersion**
</dt> <dd>

Specifies the minor version of the client machine.

</dd> <dt>

**wProcessorArchitecture**
</dt> <dd>

Specifies the client machine architecture.

</dd> <dt>

**hSplPrinter**
</dt> <dd>

Specifies the server-side handle to be used for direct calls.

</dd> </dl>

## Requirements



|                   |                                                                                      |
|-------------------|--------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Winsplp.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20SPLCLIENT_INFO_3_VISTA%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




