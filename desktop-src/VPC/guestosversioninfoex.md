---
title: GUESTOSVERSIONINFOEX structure (VPCCOMInterfaces.h)
description: Contains operating system version information for the guest operating system.
ms.assetid: 9cfd5cac-c8ea-4e09-ba47-3563554bdafa
keywords:
- GUESTOSVERSIONINFOEX structure Virtual PC
topic_type:
- apiref
api_name:
- GUESTOSVERSIONINFOEX
api_location:
- VPCCOMInterfaces.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# GUESTOSVERSIONINFOEX structure

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Contains operating system version information for the guest operating system.

## Syntax


```C++
typedef struct _GUESTOSVERSIONINFOEX {
  long    dwOSVersionInfoSize;
  long    dwMajorVersion;
  long    dwMinorVersion;
  long    dwBuildNumber;
  long    dwPlatformId;
  wchar_t szCSDVersion[128];
  short   wServicePackMajor;
  short   wServicePackMinor;
  short   wSuiteMask;
  byte    wProductType;
  byte    wReserved;
} GUESTOSVERSIONINFOEX;
```



## Members

<dl> <dt>

**dwOSVersionInfoSize**
</dt> <dd>

The size of this data structure, in bytes. Set this member to `sizeof(GUESTOSVERSIONINFOEX)`.

</dd> <dt>

**dwMajorVersion**
</dt> <dd>

The major version number.

</dd> <dt>

**dwMinorVersion**
</dt> <dd>

The minor version number.

</dd> <dt>

**dwBuildNumber**
</dt> <dd>

The build number.

</dd> <dt>

**dwPlatformId**
</dt> <dd>

The operating system platform. This member can be **VER\_PLATFORM\_WIN32\_NT** (2).

</dd> <dt>

**szCSDVersion**
</dt> <dd>

A null-terminated string, such as "Service Pack 3", that indicates the latest Service Pack installed on the system. If no Service Pack has been installed, the string is empty.

</dd> <dt>

**wServicePackMajor**
</dt> <dd>

The major version number of the latest Service Pack installed.

</dd> <dt>

**wServicePackMinor**
</dt> <dd>

The minor version number of the latest Service Pack installed.

</dd> <dt>

**wSuiteMask**
</dt> <dd>

A bitmask that identifies the product suites available on the system. This member can be a combination of the following values.



| Value                                                                                                                                                                                                                                                                                          | Meaning                                                                                                                                                                                                           |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="VER_SUITE_BACKOFFICE"></span><span id="ver_suite_backoffice"></span><dl> <dt>**VER\_SUITE\_BACKOFFICE**</dt> <dt>0x00000004</dt> </dl>                                            | Microsoft BackOffice components are installed.<br/>                                                                                                                                                         |
| <span id="VER_SUITE_BLADE"></span><span id="ver_suite_blade"></span><dl> <dt>**VER\_SUITE\_BLADE**</dt> <dt>0x00000400</dt> </dl>                                                           | Windows Server 2003, Web Edition is installed.<br/>                                                                                                                                                         |
| <span id="VER_SUITE_COMPUTE_SERVER"></span><span id="ver_suite_compute_server"></span><dl> <dt>**VER\_SUITE\_COMPUTE\_SERVER**</dt> <dt>0x00004000</dt> </dl>                               | Windows Server 2003, Compute Cluster Edition is installed.<br/>                                                                                                                                             |
| <span id="VER_SUITE_DATACENTER"></span><span id="ver_suite_datacenter"></span><dl> <dt>**VER\_SUITE\_DATACENTER**</dt> <dt>0x00000080</dt> </dl>                                            | Windows Server 2008 Datacenter, Windows Server 2003, Datacenter Edition, or Windows 2000 Datacenter Server is installed.<br/>                                                                               |
| <span id="VER_SUITE_ENTERPRISE"></span><span id="ver_suite_enterprise"></span><dl> <dt>**VER\_SUITE\_ENTERPRISE**</dt> <dt>0x00000002</dt> </dl>                                            | Windows Server 2008 Enterprise, Windows Server 2003, Enterprise Edition, or Windows 2000 Advanced Server is installed. Refer to the Remarks section for more information about this bit flag.<br/>          |
| <span id="VER_SUITE_EMBEDDEDNT"></span><span id="ver_suite_embeddednt"></span><dl> <dt>**VER\_SUITE\_EMBEDDEDNT**</dt> <dt>0x00000040</dt> </dl>                                            | Windows XP Embedded is installed.<br/>                                                                                                                                                                      |
| <span id="VER_SUITE_PERSONAL"></span><span id="ver_suite_personal"></span><dl> <dt>**VER\_SUITE\_PERSONAL**</dt> <dt>0x00000200</dt> </dl>                                                  | Windows Vista Home Premium, Windows Vista Home Basic, or Windows XP Home Edition is installed.<br/>                                                                                                         |
| <span id="VER_SUITE_SINGLEUSERTS"></span><span id="ver_suite_singleuserts"></span><dl> <dt>**VER\_SUITE\_SINGLEUSERTS**</dt> <dt>0x00000100</dt> </dl>                                      | Remote Desktop is supported, but only one interactive session is supported. This value is set unless the system is running in application server mode.<br/>                                                 |
| <span id="VER_SUITE_SMALLBUSINESS"></span><span id="ver_suite_smallbusiness"></span><dl> <dt>**VER\_SUITE\_SMALLBUSINESS**</dt> <dt>0x00000001</dt> </dl>                                   | Microsoft Small Business Server was once installed on the system, but may have been upgraded to another version of Windows. Refer to the Remarks section for more information about this bit flag.<br/>     |
| <span id="VER_SUITE_SMALLBUSINESS_RESTRICTED"></span><span id="ver_suite_smallbusiness_restricted"></span><dl> <dt>**VER\_SUITE\_SMALLBUSINESS\_RESTRICTED**</dt> <dt>0x00000020</dt> </dl> | Microsoft Small Business Server is installed with the restrictive client license in force. Refer to the Remarks section for more information about this bit flag.<br/>                                      |
| <span id="VER_SUITE_STORAGE_SERVER"></span><span id="ver_suite_storage_server"></span><dl> <dt>**VER\_SUITE\_STORAGE\_SERVER**</dt> <dt>0x00002000</dt> </dl>                               | Windows Storage Server 2003 R2 or Windows Storage Server 2003is installed.<br/>                                                                                                                             |
| <span id="VER_SUITE_TERMINAL"></span><span id="ver_suite_terminal"></span><dl> <dt>**VER\_SUITE\_TERMINAL**</dt> <dt>0x00000010</dt> </dl>                                                  | Terminal Services is installed. This value is always set.<br/> If **VER\_SUITE\_TERMINAL** is set but **VER\_SUITE\_SINGLEUSERTS** is not set, the system is running in application server mode.<br/> |
| <span id="VER_SUITE_WH_SERVER"></span><span id="ver_suite_wh_server"></span><dl> <dt>**VER\_SUITE\_WH\_SERVER**</dt> <dt>0x00008000</dt> </dl>                                              | Windows Home Server is installed.<br/>                                                                                                                                                                      |



 

</dd> <dt>

**wProductType**
</dt> <dd>

Any additional information about the system. This member can be one of the following values.



| Value                                                                                                                                                                                                                                                           | Meaning                                                                                                                                                                                                                                                                                      |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="VER_NT_DOMAIN_CONTROLLER"></span><span id="ver_nt_domain_controller"></span><dl> <dt>**VER\_NT\_DOMAIN\_CONTROLLER**</dt> <dt>0x0000002</dt> </dl> | The system is a domain controller and the operating system is Windows Server 2008 R2, Windows Server 2008, Windows Server 2003 R2, Windows Server 2003, or Windows 2000 Server.<br/>                                                                                                   |
| <span id="VER_NT_SERVER"></span><span id="ver_nt_server"></span><dl> <dt>**VER\_NT\_SERVER**</dt> <dt>0x0000003</dt> </dl>                                   | The operating system is Windows Server 2008 R2, Windows Server 2008, Windows Server 2003 R2, Windows Server 2003, or Windows 2000 Server.<br/> Note that a server that is also a domain controller is reported as **VER\_NT\_DOMAIN\_CONTROLLER**, not **VER\_NT\_SERVER**.<br/> |
| <span id="VER_NT_WORKSTATION"></span><span id="ver_nt_workstation"></span><dl> <dt>**VER\_NT\_WORKSTATION**</dt> <dt>0x0000001</dt> </dl>                    | The operating system is Windows 7, Windows Vista, Windows XP, or Windows 2000 Professional.<br/>                                                                                                                                                                                       |



 

</dd> <dt>

**wReserved**
</dt> <dd>

Reserved for future use.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |



## See also

<dl> <dt>

[**IVMGuestOS::GetOsVersionInfo**](ivmguestos-getosversioninfo.md)
</dt> </dl>

 

