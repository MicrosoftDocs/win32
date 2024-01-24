---
description: Describes possible machine architectures.
ms.assetid: 1E5E4F98-925B-424D-9B3D-BC6716FBF990
title: Image File Machine Constants (Winnt.h)
ms.topic: reference
ms.date: 05/31/2018
---

# Image File Machine Constants

Describes possible machine architectures. Used in [**GetSystemWow64Directory2**](/windows/desktop/api/wow64apiset/nf-wow64apiset-getsystemwow64directory2a), [**IsWow64GuestMachineSupported**](/windows/desktop/api/wow64apiset/nf-wow64apiset-iswow64guestmachinesupported) and [**IsWow64Process2**](/windows/win32/api/wow64apiset/nf-wow64apiset-iswow64process2).

<dl> <dt>

<span id="IMAGE_FILE_MACHINE_UNKNOWN"></span><span id="image_file_machine_unknown"></span>**IMAGE\_FILE\_MACHINE\_UNKNOWN**
</dt> <dd> <dl> <dt>

0
</dt> <dt>



Unknown


</dt> </dl> </dd> <dt>

<span id="IMAGE_FILE_MACHINE_TARGET_HOST"></span><span id="image_file_machine_target_host"></span>**IMAGE\_FILE\_MACHINE\_TARGET\_HOST**
</dt> <dd> <dl> <dt>

0x0001
</dt> <dt>



Interacts with the host and not a WOW64 guest

> [!Note]  
> This constant is available starting with Windows 10, version 1607 and Windows Server 2016.

 


</dt> </dl> </dd> <dt>

<span id="IMAGE_FILE_MACHINE_I386"></span><span id="image_file_machine_i386"></span>**IMAGE\_FILE\_MACHINE\_I386**
</dt> <dd> <dl> <dt>

0x014c
</dt> <dt>



Intel 386


</dt> </dl> </dd> <dt>

<span id="IMAGE_FILE_MACHINE_R3000"></span><span id="image_file_machine_r3000"></span>**IMAGE\_FILE\_MACHINE\_R3000**
</dt> <dd> <dl> <dt>

0x0162
</dt> <dt>



MIPS little-endian, 0x160 big-endian


</dt> </dl> </dd> <dt>

<span id="IMAGE_FILE_MACHINE_R4000"></span><span id="image_file_machine_r4000"></span>**IMAGE\_FILE\_MACHINE\_R4000**
</dt> <dd> <dl> <dt>

0x0166
</dt> <dt>



MIPS little-endian


</dt> </dl> </dd> <dt>

<span id="IMAGE_FILE_MACHINE_R10000"></span><span id="image_file_machine_r10000"></span>**IMAGE\_FILE\_MACHINE\_R10000**
</dt> <dd> <dl> <dt>

0x0168
</dt> <dt>



MIPS little-endian


</dt> </dl> </dd> <dt>

<span id="IMAGE_FILE_MACHINE_WCEMIPSV2"></span><span id="image_file_machine_wcemipsv2"></span>**IMAGE\_FILE\_MACHINE\_WCEMIPSV2**
</dt> <dd> <dl> <dt>

0x0169
</dt> <dt>



MIPS little-endian WCE v2


</dt> </dl> </dd> <dt>

<span id="IMAGE_FILE_MACHINE_ALPHA"></span><span id="image_file_machine_alpha"></span>**IMAGE\_FILE\_MACHINE\_ALPHA**
</dt> <dd> <dl> <dt>

0x0184
</dt> <dt>



Alpha\_AXP


</dt> </dl> </dd> <dt>

<span id="IMAGE_FILE_MACHINE_SH3"></span><span id="image_file_machine_sh3"></span>**IMAGE\_FILE\_MACHINE\_SH3**
</dt> <dd> <dl> <dt>

0x01a2
</dt> <dt>



SH3 little-endian


</dt> </dl> </dd> <dt>

<span id="IMAGE_FILE_MACHINE_SH3DSP"></span><span id="image_file_machine_sh3dsp"></span>**IMAGE\_FILE\_MACHINE\_SH3DSP**
</dt> <dd> <dl> <dt>

0x01a3
</dt> <dt>



SH3DSP


</dt> </dl> </dd> <dt>

<span id="IMAGE_FILE_MACHINE_SH3E"></span><span id="image_file_machine_sh3e"></span>**IMAGE\_FILE\_MACHINE\_SH3E**
</dt> <dd> <dl> <dt>

0x01a4
</dt> <dt>



SH3E little-endian


</dt> </dl> </dd> <dt>

<span id="IMAGE_FILE_MACHINE_SH4"></span><span id="image_file_machine_sh4"></span>**IMAGE\_FILE\_MACHINE\_SH4**
</dt> <dd> <dl> <dt>

0x01a6
</dt> <dt>



SH4 little-endian


</dt> </dl> </dd> <dt>

<span id="IMAGE_FILE_MACHINE_SH5"></span><span id="image_file_machine_sh5"></span>**IMAGE\_FILE\_MACHINE\_SH5**
</dt> <dd> <dl> <dt>

0x01a8
</dt> <dt>



SH5


</dt> </dl> </dd> <dt>

<span id="IMAGE_FILE_MACHINE_ARM"></span><span id="image_file_machine_arm"></span>**IMAGE\_FILE\_MACHINE\_ARM**
</dt> <dd> <dl> <dt>

0x01c0
</dt> <dt>



ARM Little-Endian


</dt> </dl> </dd> <dt>

<span id="IMAGE_FILE_MACHINE_THUMB"></span><span id="image_file_machine_thumb"></span>**IMAGE\_FILE\_MACHINE\_THUMB**
</dt> <dd> <dl> <dt>

0x01c2
</dt> <dt>



ARM Thumb/Thumb-2 Little-Endian


</dt> </dl> </dd> <dt>

<span id="IMAGE_FILE_MACHINE_ARMNT"></span><span id="image_file_machine_armnt"></span>**IMAGE\_FILE\_MACHINE\_ARMNT**
</dt> <dd> <dl> <dt>

0x01c4
</dt> <dt>



ARM Thumb-2 Little-Endian

> [!Note]  
> This constant is available starting with Windows 7 and Windows Server 2008 R2.

 


</dt> </dl> </dd> <dt>

<span id="IMAGE_FILE_MACHINE_AM33"></span><span id="image_file_machine_am33"></span>**IMAGE\_FILE\_MACHINE\_AM33**
</dt> <dd> <dl> <dt>

0x01d3
</dt> <dt>



TAM33BD


</dt> </dl> </dd> <dt>

<span id="IMAGE_FILE_MACHINE_POWERPC"></span><span id="image_file_machine_powerpc"></span>**IMAGE\_FILE\_MACHINE\_POWERPC**
</dt> <dd> <dl> <dt>

0x01F0
</dt> <dt>



IBM PowerPC Little-Endian


</dt> </dl> </dd> <dt>

<span id="IMAGE_FILE_MACHINE_POWERPCFP"></span><span id="image_file_machine_powerpcfp"></span>**IMAGE\_FILE\_MACHINE\_POWERPCFP**
</dt> <dd> <dl> <dt>

0x01f1
</dt> <dt>



POWERPCFP


</dt> </dl> </dd> <dt>

<span id="IMAGE_FILE_MACHINE_IA64"></span><span id="image_file_machine_ia64"></span>**IMAGE\_FILE\_MACHINE\_IA64**
</dt> <dd> <dl> <dt>

0x0200
</dt> <dt>



Intel 64


</dt> </dl> </dd> <dt>

<span id="IMAGE_FILE_MACHINE_MIPS16"></span><span id="image_file_machine_mips16"></span>**IMAGE\_FILE\_MACHINE\_MIPS16**
</dt> <dd> <dl> <dt>

0x0266
</dt> <dt>



MIPS


</dt> </dl> </dd> <dt>

<span id="IMAGE_FILE_MACHINE_ALPHA64"></span><span id="image_file_machine_alpha64"></span>**IMAGE\_FILE\_MACHINE\_ALPHA64**
</dt> <dd> <dl> <dt>

0x0284
</dt> <dt>



ALPHA64


</dt> </dl> </dd> <dt>

<span id="IMAGE_FILE_MACHINE_MIPSFPU"></span><span id="image_file_machine_mipsfpu"></span>**IMAGE\_FILE\_MACHINE\_MIPSFPU**
</dt> <dd> <dl> <dt>

0x0366
</dt> <dt>



MIPS


</dt> </dl> </dd> <dt>

<span id="IMAGE_FILE_MACHINE_MIPSFPU16"></span><span id="image_file_machine_mipsfpu16"></span>**IMAGE\_FILE\_MACHINE\_MIPSFPU16**
</dt> <dd> <dl> <dt>

0x0466
</dt> <dt>



MIPS


</dt> </dl> </dd> <dt>

<span id="IMAGE_FILE_MACHINE_AXP64"></span><span id="image_file_machine_axp64"></span>**IMAGE\_FILE\_MACHINE\_AXP64**
</dt> <dd> <dl> <dt>

0x0284
</dt> <dt>



AXP64


</dt> </dl> </dd> <dt>

<span id="IMAGE_FILE_MACHINE_TRICORE"></span><span id="image_file_machine_tricore"></span>**IMAGE\_FILE\_MACHINE\_TRICORE**
</dt> <dd> <dl> <dt>

0x0520
</dt> <dt>



Infineon


</dt> </dl> </dd> <dt>

<span id="IMAGE_FILE_MACHINE_CEF"></span><span id="image_file_machine_cef"></span>**IMAGE\_FILE\_MACHINE\_CEF**
</dt> <dd> <dl> <dt>

0x0CEF
</dt> <dt>



CEF


</dt> </dl> </dd> <dt>

<span id="IMAGE_FILE_MACHINE_EBC"></span><span id="image_file_machine_ebc"></span>**IMAGE\_FILE\_MACHINE\_EBC**
</dt> <dd> <dl> <dt>

0x0EBC
</dt> <dt>



EFI Byte Code


</dt> </dl> </dd> <dt>

<span id="IMAGE_FILE_MACHINE_AMD64"></span><span id="image_file_machine_amd64"></span>**IMAGE\_FILE\_MACHINE\_AMD64**
</dt> <dd> <dl> <dt>

0x8664
</dt> <dt>



AMD64 (K8)


</dt> </dl> </dd> <dt>

<span id="IMAGE_FILE_MACHINE_M32R"></span><span id="image_file_machine_m32r"></span>**IMAGE\_FILE\_MACHINE\_M32R**
</dt> <dd> <dl> <dt>

0x9041
</dt> <dt>



M32R little-endian


</dt> </dl> </dd> <dt>

<span id="IMAGE_FILE_MACHINE_ARM64"></span><span id="image_file_machine_arm64"></span>**IMAGE\_FILE\_MACHINE\_ARM64**
</dt> <dd> <dl> <dt>

0xAA64
</dt> <dt>



ARM64 Little-Endian

> [!Note]  
> This constant is available starting with Windows 8.1 and Windows Server 2012 R2.

 


</dt> </dl> </dd> <dt>

<span id="IMAGE_FILE_MACHINE_CEE"></span><span id="image_file_machine_cee"></span>**IMAGE\_FILE\_MACHINE\_CEE**
</dt> <dd> <dl> <dt>

0xC0EE
</dt> <dt>



CEE


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Winnt.h</dt> </dl> |



 

 




