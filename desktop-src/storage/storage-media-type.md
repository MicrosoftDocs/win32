---
title: STORAGE\_MEDIA\_TYPE enumeration
description: The STORAGE\_MEDIA\_TYPE enumeration is used in conjunction with the IOCTL\_STORAGE\_GET\_MEDIA\_TYPES\_EX request to query the class driver for the types of media that a device supports.
ms.assetid: '70214b6e-92d2-418a-ad8a-8701df02fdc3'
keywords: ["STORAGE_MEDIA_TYPE enumeration Storage Devices", "PSTORAGE_MEDIA_TYPE enumeration pointer Storage Devices"]
topic_type:
- apiref
api_name:
- STORAGE_MEDIA_TYPE
api_location:
- ntddstor.h
api_type:
- HeaderDef
---

# STORAGE\_MEDIA\_TYPE enumeration

The STORAGE\_MEDIA\_TYPE enumeration is used in conjunction with the [**IOCTL\_STORAGE\_GET\_MEDIA\_TYPES\_EX**](ioctl-storage-get-media-types-ex.md) request to query the class driver for the types of media that a device supports.

## Syntax


```C++
typedef enum _STORAGE_MEDIA_TYPE { 
  DDS_4mm             = 0x20,
  MiniQic             = 0x21,
  Travan              = 0x22,
  QIC                 = 0x23,
  MP_8mm              = 0x24,
  AME_8mm             = 0x25,
  AIT1_8mm            = 0x26,
  DLT                 = 0x27,
  NCTP                = 0x28,
  IBM_3480            = 0x29,
  IBM_3490E           = 0x2A,
  IBM_Magstar_3590    = 0x2B,
  IBM_Magstar_MP      = 0x2C,
  STK_DATA_D3         = 0x2D,
  SONY_DTF            = 0x2E,
  DV_6mm              = 0x2F,
  DMI                 = 0x30,
  SONY_D2             = 0x31,
  CLEANER_CARTRIDGE   = 0x32,
  CD_ROM              = 0x33,
  CD_R                = 0x34,
  CD_RW               = 0x35,
  DVD_ROM             = 0x36,
  DVD_R               = 0x37,
  DVD_RW              = 0x38,
  MO_3_RW             = 0x39,
  MO_5_WO             = 0x3A,
  MO_5_RW             = 0x3B,
  MO_5_LIMDOW         = 0x3C,
  PC_5_WO             = 0x3D,
  PC_5_RW             = 0x3E,
  PD_5_RW             = 0x3F,
  ABL_5_WO            = 0x40,
  PINNACLE_APEX_5_RW  = 0x41,
  SONY_12_WO          = 0x42,
  PHILIPS_12_WO       = 0x43,
  HITACHI_12_WO       = 0x44,
  CYGNET_12_WO        = 0x45,
  KODAK_14_WO         = 0x46,
  MO_NFR_525          = 0x47,
  NIKON_12_RW         = 0x48,
  IOMEGA_ZIP          = 0x49,
  IOMEGA_JAZ          = 0x4A,
  SYQUEST_EZ135       = 0x4B,
  SYQUEST_EZFLYER     = 0x4C,
  SYQUEST_SYJET       = 0x4D,
  AVATAR_F2           = 0x4E,
  MP2_8mm             = 0x4F,
  DST_S               = 0x50,
  DST_M               = 0x51,
  DST_L               = 0x52,
  VXATape_1           = 0x53,
  VXATape_2           = 0x54,
  STK_9840            = 0x55,
  LTO_Ultrium         = 0x56,
  LTO_Accelis         = 0x57,
  DVD_RAM             = 0x58,
  AIT_8mm             = 0x59,
  ADR_1               = 0x5A,
  ADR_2               = 0x5B,
  STK_9940            = 0x5C,
  SAIT                = 0x5D,
  VXATape             = 0x5E
} STORAGE_MEDIA_TYPE, *PSTORAGE_MEDIA_TYPE;
```



## Constants

<dl> <dt>

<span id="DDS_4mm"></span><span id="dds_4mm"></span><span id="DDS_4MM"></span>**DDS\_4mm**
</dt> <dd>

Indicates a DAT DDS1 or DDS2 tape device (all vendors).

</dd> <dt>

<span id="MiniQic"></span><span id="miniqic"></span><span id="MINIQIC"></span>**MiniQic**
</dt> <dd>

Indicates a mini-QIC tape device.

</dd> <dt>

<span id="Travan"></span><span id="travan"></span><span id="TRAVAN"></span>**Travan**
</dt> <dd>

Indicates a Travan TR-1, 2 or 3 tape device.

</dd> <dt>

<span id="QIC"></span><span id="qic"></span>**QIC**
</dt> <dd>

Indicates a QIC tape device.

</dd> <dt>

<span id="MP_8mm"></span><span id="mp_8mm"></span><span id="MP_8MM"></span>**MP\_8mm**
</dt> <dd>

Indicates an 8mm Exabyte metal particle tape device.

</dd> <dt>

<span id="AME_8mm"></span><span id="ame_8mm"></span><span id="AME_8MM"></span>**AME\_8mm**
</dt> <dd>

Indicates an 8mm Exabyte advanced metal tape device.

</dd> <dt>

<span id="AIT1_8mm"></span><span id="ait1_8mm"></span><span id="AIT1_8MM"></span>**AIT1\_8mm**
</dt> <dd>

Indicates an 8mm Sony AIT tape device.

</dd> <dt>

<span id="DLT"></span><span id="dlt"></span>**DLT**
</dt> <dd>

Indicates a DLT compact IIIxt or IV tape device.

</dd> <dt>

<span id="NCTP"></span><span id="nctp"></span>**NCTP**
</dt> <dd>

Indicates a Philips NCTP tape device.

</dd> <dt>

<span id="IBM_3480"></span><span id="ibm_3480"></span>**IBM\_3480**
</dt> <dd>

Indicates an IBM 3480 tape device.

</dd> <dt>

<span id="IBM_3490E"></span><span id="ibm_3490e"></span>**IBM\_3490E**
</dt> <dd>

Indicates an IBM 3490E tape device.

</dd> <dt>

<span id="IBM_Magstar_3590"></span><span id="ibm_magstar_3590"></span><span id="IBM_MAGSTAR_3590"></span>**IBM\_Magstar\_3590**
</dt> <dd>

Indicates an IBM Magstar 3590 tape device.

</dd> <dt>

<span id="IBM_Magstar_MP"></span><span id="ibm_magstar_mp"></span><span id="IBM_MAGSTAR_MP"></span>**IBM\_Magstar\_MP**
</dt> <dd>

Indicates an IBM Magstar MP tape device.

</dd> <dt>

<span id="STK_DATA_D3"></span><span id="stk_data_d3"></span>**STK\_DATA\_D3**
</dt> <dd>

Indicates an STK data D3 tape device.

</dd> <dt>

<span id="SONY_DTF"></span><span id="sony_dtf"></span>**SONY\_DTF**
</dt> <dd>

Indicates a Sony DTF tape device.

</dd> <dt>

<span id="DV_6mm"></span><span id="dv_6mm"></span><span id="DV_6MM"></span>**DV\_6mm**
</dt> <dd>

Indicates a 6mm digital video tape device.

</dd> <dt>

<span id="DMI"></span><span id="dmi"></span>**DMI**
</dt> <dd>

Indicates a Exabyte DMI tape device and compatible devices.

</dd> <dt>

<span id="SONY_D2"></span><span id="sony_d2"></span>**SONY\_D2**
</dt> <dd>

Indicates a Sony D2S or D2L tape device.

</dd> <dt>

<span id="CLEANER_CARTRIDGE"></span><span id="cleaner_cartridge"></span>**CLEANER\_CARTRIDGE**
</dt> <dd>

Indicates a drive type that supports drive cleaners.

</dd> <dt>

<span id="CD_ROM"></span><span id="cd_rom"></span>**CD\_ROM**
</dt> <dd>

Indicates a CD optical disk.

</dd> <dt>

<span id="CD_R"></span><span id="cd_r"></span>**CD\_R**
</dt> <dd>

Indicates a CD-recordable (write once) optical disk.

</dd> <dt>

<span id="CD_RW"></span><span id="cd_rw"></span>**CD\_RW**
</dt> <dd>

Indicates a CD-rewritable optical disk.

</dd> <dt>

<span id="DVD_ROM"></span><span id="dvd_rom"></span>**DVD\_ROM**
</dt> <dd>

Indicates a DVD-ROM optical disk.

</dd> <dt>

<span id="DVD_R"></span><span id="dvd_r"></span>**DVD\_R**
</dt> <dd>

Indicates a DVD-recordable (write once) optical disk.

</dd> <dt>

<span id="DVD_RW"></span><span id="dvd_rw"></span>**DVD\_RW**
</dt> <dd>

Indicates a DVD-rewritable optical disk.

</dd> <dt>

<span id="MO_3_RW"></span><span id="mo_3_rw"></span>**MO\_3\_RW**
</dt> <dd>

Indicates a 3.5" rewritable MO optical disk.

</dd> <dt>

<span id="MO_5_WO"></span><span id="mo_5_wo"></span>**MO\_5\_WO**
</dt> <dd>

Indicates a MO 5.25" write once optical disk.

</dd> <dt>

<span id="MO_5_RW"></span><span id="mo_5_rw"></span>**MO\_5\_RW**
</dt> <dd>

Indicates a MO 5.25" rewritable (not LIMDOW) optical disk.

</dd> <dt>

<span id="MO_5_LIMDOW"></span><span id="mo_5_limdow"></span>**MO\_5\_LIMDOW**
</dt> <dd>

Indicates a MO 5.25" rewritable (LIMDOW) optical disk.

</dd> <dt>

<span id="PC_5_WO"></span><span id="pc_5_wo"></span>**PC\_5\_WO**
</dt> <dd>

Indicates a phase change 5.25" write once optical disk.

</dd> <dt>

<span id="PC_5_RW"></span><span id="pc_5_rw"></span>**PC\_5\_RW**
</dt> <dd>

Indicates a phase change 5.25" rewritable optical disk.

</dd> <dt>

<span id="PD_5_RW"></span><span id="pd_5_rw"></span>**PD\_5\_RW**
</dt> <dd>

Indicates a phase change dual rewritable optical disk.

</dd> <dt>

<span id="ABL_5_WO"></span><span id="abl_5_wo"></span>**ABL\_5\_WO**
</dt> <dd>

Indicates a ablative 5.25" write once optical disk.

</dd> <dt>

<span id="PINNACLE_APEX_5_RW"></span><span id="pinnacle_apex_5_rw"></span>**PINNACLE\_APEX\_5\_RW**
</dt> <dd>

Indicates a pinnacle apex 4.6-GB rewritable optical disk.

</dd> <dt>

<span id="SONY_12_WO"></span><span id="sony_12_wo"></span>**SONY\_12\_WO**
</dt> <dd>

Indicates a Sony 12" write once optical disk.

</dd> <dt>

<span id="PHILIPS_12_WO"></span><span id="philips_12_wo"></span>**PHILIPS\_12\_WO**
</dt> <dd>

Indicates a Philips/LMS 12" write once optical disk.

</dd> <dt>

<span id="HITACHI_12_WO"></span><span id="hitachi_12_wo"></span>**HITACHI\_12\_WO**
</dt> <dd>

Indicates a Hitachi 12" write once optical disk.

</dd> <dt>

<span id="CYGNET_12_WO"></span><span id="cygnet_12_wo"></span>**CYGNET\_12\_WO**
</dt> <dd>

Indicates a Cygnet/ATG 12" write once optical disk.

</dd> <dt>

<span id="KODAK_14_WO"></span><span id="kodak_14_wo"></span>**KODAK\_14\_WO**
</dt> <dd>

Indicates a Kodak 14" write once optical disk.

</dd> <dt>

<span id="MO_NFR_525"></span><span id="mo_nfr_525"></span>**MO\_NFR\_525**
</dt> <dd>

Indicates a near field recording (Terastor) optical disk.

</dd> <dt>

<span id="NIKON_12_RW"></span><span id="nikon_12_rw"></span>**NIKON\_12\_RW**
</dt> <dd>

Indicates a Nikon 12" rewritable optical disk.

</dd> <dt>

<span id="IOMEGA_ZIP"></span><span id="iomega_zip"></span>**IOMEGA\_ZIP**
</dt> <dd>

Indicates Iomega zip magnetic disk device.

</dd> <dt>

<span id="IOMEGA_JAZ"></span><span id="iomega_jaz"></span>**IOMEGA\_JAZ**
</dt> <dd>

Indicates an Iomega Jaz magnetic disk device.

</dd> <dt>

<span id="SYQUEST_EZ135"></span><span id="syquest_ez135"></span>**SYQUEST\_EZ135**
</dt> <dd>

Indicates a Syquest EZ135 magnetic disk device.

</dd> <dt>

<span id="SYQUEST_EZFLYER"></span><span id="syquest_ezflyer"></span>**SYQUEST\_EZFLYER**
</dt> <dd>

Indicates a Syquest EzFlyer magnetic disk device.

</dd> <dt>

<span id="SYQUEST_SYJET"></span><span id="syquest_syjet"></span>**SYQUEST\_SYJET**
</dt> <dd>

Indicates a Syquest SyJet magnetic disk device.

</dd> <dt>

<span id="AVATAR_F2"></span><span id="avatar_f2"></span>**AVATAR\_F2**
</dt> <dd>

Indicates a 2.5" Floppy device.

</dd> <dt>

<span id="MP2_8mm"></span><span id="mp2_8mm"></span><span id="MP2_8MM"></span>**MP2\_8mm**
</dt> <dd>

Indicates an 8mm Hitachi tape device.

</dd> <dt>

<span id="DST_S"></span><span id="dst_s"></span>**DST\_S**
</dt> <dd>

Indicates a type DST Ampex small tape device.

</dd> <dt>

<span id="DST_M"></span><span id="dst_m"></span>**DST\_M**
</dt> <dd>

Indicates a type DST Ampex medium tape device.

</dd> <dt>

<span id="DST_L"></span><span id="dst_l"></span>**DST\_L**
</dt> <dd>

Indicates a type DST Ampex large tape device.

</dd> <dt>

<span id="VXATape_1"></span><span id="vxatape_1"></span><span id="VXATAPE_1"></span>**VXATape\_1**
</dt> <dd>

Indicates an 8mm Ecrix tape device.

</dd> <dt>

<span id="VXATape_2"></span><span id="vxatape_2"></span><span id="VXATAPE_2"></span>**VXATape\_2**
</dt> <dd>

Indicates an 8mm Ecrix tape device.

</dd> <dt>

<span id="STK_9840"></span><span id="stk_9840"></span>**STK\_9840**
</dt> <dd>

Indicates an STK 9840 device.

</dd> <dt>

<span id="LTO_Ultrium"></span><span id="lto_ultrium"></span><span id="LTO_ULTRIUM"></span>**LTO\_Ultrium**
</dt> <dd>

Indicates an IBM, HP, or Seagate LTO Ultrium device.

</dd> <dt>

<span id="LTO_Accelis"></span><span id="lto_accelis"></span><span id="LTO_ACCELIS"></span>**LTO\_Accelis**
</dt> <dd>

Indicates an IBM, HP, or Seagate LTO Accelis

</dd> <dt>

<span id="DVD_RAM"></span><span id="dvd_ram"></span>**DVD\_RAM**
</dt> <dd>

Indicates a DVD-RAM optical device.

</dd> <dt>

<span id="AIT_8mm"></span><span id="ait_8mm"></span><span id="AIT_8MM"></span>**AIT\_8mm**
</dt> <dd>

Indicates an AIT2 or higher 8mm tape device.

</dd> <dt>

<span id="ADR_1"></span><span id="adr_1"></span>**ADR\_1**
</dt> <dd>

Indicates an on-stream ADR media type device.

</dd> <dt>

<span id="ADR_2"></span><span id="adr_2"></span>**ADR\_2**
</dt> <dd>

Indicates an on-stream ADR media type device.

</dd> <dt>

<span id="STK_9940"></span><span id="stk_9940"></span>**STK\_9940**
</dt> <dd>

STK 9940

</dd> <dt>

<span id="SAIT"></span><span id="sait"></span>**SAIT**
</dt> <dd>

SAIT Tapes

</dd> <dt>

<span id="VXATape"></span><span id="vxatape"></span><span id="VXATAPE"></span>**VXATape**
</dt> <dd>

VXA (Ecrix 8mm) Tape

</dd> </dl>

## Requirements



|                   |                                                                                                                          |
|-------------------|--------------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h or Minitape.h)</dt> </dl> |



## See also

<dl> <dt>

[**DEVICE\_MEDIA\_INFO**](device-media-info.md)
</dt> <dt>

[**GET\_MEDIA\_TYPES**](get-media-types.md)
</dt> <dt>

[**IOCTL\_STORAGE\_GET\_MEDIA\_TYPES\_EX**](ioctl-storage-get-media-types-ex.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_MEDIA_TYPE%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






